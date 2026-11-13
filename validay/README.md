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
