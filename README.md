# WoW XP Helper

**RestedXP → Polestar con un solo pulsante**, per chi gioca a WoW Forever.

### [Apri WoW XP Helper](https://dav1dera.github.io/wow-xp-helper/)


## Installazione guidata: istruzioni complete

Apri il sito https://dav1dera.github.io/wow-xp-helper/ e segui tutti i passaggi visibili. Sono indicati i percorsi Windows, i pulsanti da premere, la posizione di ogni cartella e i controlli finali. Nessuna operazione essenziale richiede di espandere un menu.

### Prerequisiti

Servono Chrome o Edge aggiornato su Windows, WoW Forever e gli addon RestedXP (cartella RXPGuides) e Polestar. La cartella degli addon si trova in:

    World of Warcraft\_forever_\Interface\AddOns\

Non spostare o cancellare gli addon originali Polestar e RXPGuides.

### Passaggio 1 — Preparazione RestedXP

Se hai già le guide aggiornate in WoW, premi SÌ, LE HO GIÀ e passa al punto 2. Altrimenti recupera un codice di importazione da una fonte che hai il diritto di utilizzare, quindi esegui Import Guide in RestedXP. **Se devi sostituire vecchie guide importate**, e hai già il nuovo codice pronto, fai prima Import Guide → Purge → conferma → Reload. Purge elimina le guide importate: non usarlo se sono già aggiornate.

Dopo Import esegui Reload e controlla che i capitoli desiderati siano presenti, anche sopra il livello 20. La copertura fino al livello 60 dipende dalle guide effettivamente disponibili nella tua cache.

### Passaggio 2 — Conversione

Chiudi completamente WoW con Exit Game, poi conferma che le guide siano pronte e che WoW sia chiuso.

Metodo consigliato: scegli dalla pagina il file

    _forever_\WTF\Account\NOME_ACCOUNT\SavedVariables\RXPGuides.lua

e, per includere le guide iniziali, la cartella

    _forever_\Interface\AddOns\RXPGuides\

La pagina verifica che il file abbia il nome corretto e che la cartella contenga Guides/GuideList-forever.xml. Quindi premi CREA LE GUIDE PER POLESTAR. Puoi usare anche il metodo automatico scegliendo la cartella _forever_; se Chrome la blocca per sicurezza, torna al metodo file.

### Passaggio 3 — Installazione e verifica

1. Premi Win + E, apri la cartella AddOns del gioco.
2. Crea Desktop/Backup_PolestarPack; se hai vecchi pacchetti generati da precedenti prove, spostali dal gioco al backup con Ctrl+X e Ctrl+V. Esempi: PolestarPack_rxp-completo-160-1-1, PolestarPack_rxp-completo-160-1-2, PolestarPack_rxp-completo-160-2-1. Non spostare pacchetti di altri autori, né Polestar, Polestar_Options o RXPGuides.
3. Apri il file RestedXP_Speedrun_Horde_Alliance_1-60.zip dalla cartella Download, oppure il file ZIP appena scaricato col nome mostrato da Chrome. Estrai tutto.
4. Seleziona tutte le cartelle PolestarPack_* estratte e copiale direttamente in World of Warcraft/_forever_/Interface/AddOns/. Non creare un livello intermedio con il nome dello ZIP.
5. Riavvia WoW, controlla che gli addon siano attivi, digita /polestar guides e apri Community guides. Verifica la presenza delle Speedrun Horde 1–60 e Alliance 1–60, se entrambe convertite.
6. Digita /polestar packs. In Options → Community guides attiva il pacchetto e scegli Suggest guides from → RestedXP Speedrun della fazione del personaggio, per usarla come percorso suggerito. Fonte ufficiale: https://github.com/fitzforge/polestar/blob/next/docs/GUIDE_PACKS.md

Struttura corretta, se entrambi i pacchetti sono stati compilati:

    _forever_/
      Interface/
        AddOns/
          Polestar/
          RXPGuides/
          PolestarPack_rxp-completo-160-horde/
          PolestarPack_rxp-completo-160-alliance/
          PolestarPack_..._Human/   (solo se nello ZIP)

Le cartelle aggiuntive per le razze, ad esempio _Gnome o _Human, sono componenti tecnici dei pacchetti e vanno copiate insieme agli altri file.

### Diagnostica rapida

- File RXPGuides.lua assente: importa in RestedXP, fai Reload, chiudi WoW e verifica la SavedVariables dell'account corretto. Non usare Purge dopo l'importazione.
- Chrome blocca la cartella del gioco: usa la modalità file.
- Cartella RXPGuides non accettata: verifica che contenga Guides/GuideList-forever.xml.
- ZIP scaricato ma nessuna guida visibile: controlla i percorsi e i pacchetti attivi con /polestar packs.
- Guide 1–20 mancanti: includi la cartella originale RXPGuides nella conversione.
- Guide avanzate mancanti: controlla l'importazione RestedXP e i dettagli tecnici della conversione.

Il risultato predefinito è un pacchetto Speedrun per ciascuna fazione, con i capitoli collegati. Dungeon e Survival sono opzionali. I pacchetti non sono garantiti completi fino al livello 60 se mancano i capitoli sorgenti o se il compilatore ne esclude alcuni.


## Risorse esterne: Inariaa e Forever Free RXP

Inariaa è la prima risorsa esterna elencata nell'interfaccia; Forever Free RXP è la seconda. Sono siti indipendenti e facoltativi. WoW XP Helper non esegue i generatori, non intercetta le loro comunicazioni e non condivide alcun archivio di guide. Le guide ufficiali già importate possono essere utilizzate direttamente.

Forever Free RXP dichiara di basarsi sul [Gist di imSp4rky](https://gist.github.com/imSp4rky/17759ae4bd9a78fdc898c901c2436be1). Quello script non include l'archivio cifrato usato per generare codici nuovi.

## Aggiornamento dalla versione divisa in 14 cartelle

Se hai già provato la vecchia compilazione, **sposta temporaneamente fuori da `Interface/AddOns` le vecchie cartelle `PolestarPack_AllianceSpeedrun*`, `PolestarPack_HordeSpeedrun*` e le vecchie cartelle di Dungeon generate dalla prova**, per evitare duplicati in Polestar. Non toccare gli addon originali `Polestar` e `RXPGuides`.

Il nuovo ZIP contiene **due pacchetti Speedrun separati per fazione** (uno Horde e uno Alliance), ognuno con le proprie tappe collegate da livello 1 a 60, ove disponibili. Può contenere **cartelle addon aggiuntive per razze specifiche** (per esempio `_Human`, `_Gnome`): sono componenti tecnici dello stesso pack, **non pack separati nella schermata Community**; vanno estratti e installati insieme al pack principale.

**Nota sulle prestazioni:** compilare tutte le guide 1–60 di ciascuna fazione in un unico pacchetto richiede più memoria e può impiegare più tempo dei gruppi da 32. Il lavoro avviene in un Web Worker così la pagina resta utilizzabile e offre **Annulla compilazione**. È ancora necessario un test end-to-end con una cache completa dell'utente: il successo di GitHub Actions convalida la pubblicazione, non la compilazione delle sue guide.

## Privacy, licenze e pubblicazione

I file locali vengono elaborati dal browser. **La cache RestedXP e i dati dell'account non vengono caricati da questo progetto.** Il codice del converter e i dati di gioco sono ospitati su GitHub Pages. Quando scegli la cartella WoW, Chrome/Edge deve chiederti il permesso di lettura e scrittura previsto dalle sue protezioni; il tool chiede conferma prima di sostituire una cartella PolestarPack preesistente.

Questo repository non distribuisce guide RestedXP o codici associati ai BattleTag. Usa soltanto guide che hai il diritto di convertire e non distribuire guide di altri senza permesso.

La GUI è rilasciata con licenza MIT. Il motore [polestar-convert](https://github.com/aronjanosch/polestar-convert) è MIT; il compilatore Polestar e i dati utilizzati hanno licenze proprie (incluse GPL-3.0). Gli asset pubblici vengono recuperati durante il workflow GitHub Actions \`.github/workflows/pages.yml\` con \`scripts/vendor_converter.py\`.

Il sito è pubblicato automaticamente su GitHub Pages dopo gli aggiornamenti al ramo \`main\`. La compilazione del sito è verificata da GitHub Actions; la compatibilità con ogni installazione Windows di WoW Forever deve essere verificata sul PC dell'utente.
