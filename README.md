# WoW XP Helper — RestedXP → Polestar OneClick

Web app for WoW Forever: recover locally available RestedXP guides and convert them to Polestar. The tool contains no guide content and does not unlock paid guides.

The user selects the WoW installation folder in Chrome/Edge. The app reads local RestedXP saved variables and addon source files, compiles using the open-source polestar-convert engine staged at deployment, downloads a PolestarPack ZIP and can install it into AddOns with user permission.

To deploy: GitHub Settings → Pages → Source: GitHub Actions; then Actions → Publish WoW XP Helper → Run workflow.

Expected Pages URL: https://dav1dera.github.io/wow-xp-helper/

Local source files and BattleTag are not uploaded by the app. Conversion success depends on the available files and upstream engine compatibility.