# ValiDay

Tracker d'habitudes mobile, en page unique, hébergé sur GitHub Pages à côté de « Suivi muscu » (`/validay/`).

- **Données** : uniquement sur l'appareil (`localStorage`, clé `validay.v1`). Export / import JSON depuis l'onglet Profil.
- **Hors ligne** : `sw.js` met la page et les icônes en cache ; la page s'installe sur l'écran d'accueil (`manifest.webmanifest`).
- **Thème** : noir et blanc, clair / sombre / automatique.

## Écrans

| Onglet | Contenu |
| --- | --- |
| Aujourd'hui | Progression du jour, bandeau de la semaine, coach, habitudes groupées par moment, journal du soir |
| Progrès | Taux jour / semaine / mois, calendrier, séries, taux par habitude et par catégorie, analyses, bilan hebdo |
| Focus | Minuteur 25 / 45 / 60 min (ou libre) avec pause, temps par catégorie, historique |
| Profil | Points, niveau, badges, jokers, journal, thème, rappels, catégories, export / import |

## Modifier

Tout est dans `index.html` (CSS puis JS). Pas d'étape de build.

## Agenda Google

ValiDay lit l'agenda via le script Apps Script de Suivi muscu (fonction `getAgenda`, déjà exposée par `doPost`). Aucun nouveau déploiement n'est nécessaire.

- Profil → Agenda Google : coller l'adresse `/exec` du script. Si elle est déjà enregistrée par Suivi muscu dans le même navigateur, elle est reprise automatiquement.
- Dans une habitude, activer « Seulement si prévu à l'agenda » et choisir un mot-clé (ex. `sport`). L'habitude n'est demandée que les jours où un événement contient ce mot.
- Un événement contenant le mot de repos (`repos` par défaut) valide l'habitude comme jour de repos.
- La synchronisation couvre 60 jours passés et 21 jours à venir. Elle se relance à l'ouverture de l'appli si la dernière date de plus de 15 minutes.

L'adresse `/exec` reste uniquement sur l'appareil, jamais dans ce dépôt.

## Tâches ponctuelles et Rappels iPhone

- Un événement d'agenda dont le titre commence par `À faire :` devient une tâche à cocher ce jour-là. Non faite, elle reste affichée « en retard » pendant 14 jours.
- Une tâche validée rapporte 20 ou 30 points (réglage dans Profil → Agenda, tâches & rappels).
- Retour vers l'agenda : la tâche validée reçoit `✓` devant le titre de l'événement (`marquerTache` dans `apps-script/Code.gs`).
- Rappels iPhone : le raccourci « ValiDay Rappels » envoie les rappels datés au script (`importerRappels`), qui les crée dans l'agenda. Il termine dans Rappels ceux qui ont été validés dans ValiDay. Le mode d'emploi pas à pas est dans l'appli : Profil → Agenda, tâches & rappels → Mode d'emploi.

Ces deux fonctions demandent de recoller `apps-script/Code.gs` dans Apps Script et de déployer une **nouvelle version** (l'adresse `/exec` ne change pas).

## Navigation

Quatre menus, de gauche à droite : Focus, Aujourd'hui, Progrès, Profil. On passe de l'un à l'autre en glissant. Appui long sur une habitude pour la modifier ; le bouton liste en haut d'Aujourd'hui affiche toutes les habitudes.
