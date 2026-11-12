# Suivi muscu

Appli mobile de suivi de séances de musculation. L'interface est hébergée sur GitHub Pages ; les données restent dans un Google Sheet, via un script Google Apps Script.

## Contenu

| Fichier | Rôle |
| --- | --- |
| `index.html` | La page servie par GitHub Pages. **Générée** par `build.py`, ne pas la modifier à la main. |
| `apps-script/Code.gs` | Le script Google Apps Script : lit et écrit le Sheet, lit l'agenda, et contient toute l'interface dans `PAGE_HTML`. |
| `web/pont.html` | Le pont : recrée `google.script.run` hors d'Apps Script en appelant `doPost()` de `Code.gs`. |
| `build.py` | Assemble `index.html` à partir de `PAGE_HTML` et du pont. |

## Mise en route

1. **Apps Script** — dans le Google Sheet : Extensions → Apps Script, remplacer le contenu de `Code.gs` par celui de `apps-script/Code.gs`.
2. **Déploiement** — Déployer → Gérer les déploiements → modifier → *Nouvelle version*, avec « Exécuter en tant que : Moi » et « Qui a accès : Tout le monde ». Copier l'adresse qui se termine par `/exec`.
3. **Appli** — ouvrir la page GitHub Pages, coller cette adresse une fois. Elle est gardée sur l'appareil.

Pour changer d'adresse plus tard : ajouter `#config` à la fin de l'adresse de la page.

## Sécurité

L'adresse `/exec` n'est volontairement **pas** dans ce dépôt : toute personne qui la connaît peut lire et modifier les onglets `app_` du Sheet. Ne pas la publier ni la partager.

## Modifier l'appli

Modifier `apps-script/Code.gs` (ou `web/pont.html`), puis régénérer la page :

```bash
python3 build.py
```
