# Fordybelsestimen

Tines danske podcast om ledelse, teams og motivation.
Undertitel: *Ledelse, teams og motivation – fra bøgerne til mandag morgen.*

## Sådan laves et afsnit
- Claude skriver én kildefil pr. afsnit (ca. 9.000 ord, tre kapitler), en instruktion og en shownotes-fil med hele kildelisten.
- Tine laver lyden i NotebookLM: upload kildefilen, Studio → Lydoversigt → blyant ("Tilpas"): Dybdegående samtale, dansk, længde Standard (dansk har kun Kort/Standard), og instruktionen i tekstfeltet.
- Mål: ca. 45 min som **én** lydfil. Bliver den for kort: lav kapitlerne (`dele/`) hver for sig og sæt dem sammen (ffmpeg).

## Indholdsregler (Tines feedback)
- Voksne lyttere, enkelt sprog. Eksempler fra arbejdslivet og elitesporten. Ingen eksempler fra skole eller børn.
- Rolig, varm tone. Ingen fjollede jokes eller overdrevne udbrud.
- Kilderne kvalificerer podcasten: nævn dem i samtalen (hvem, hvad, år; forskning vs. bog/fortælling vs. rapport) og saml dem til sidst ("Afsnittets kilder").
- Favorit: Patrick Lencioni. Også Daniel Pink, Helle Hein, Edmondson, Deci & Ryan, Amabile, Kim Scott, Adam Grant, Bock, Kahneman, Buckingham & Goodall. Stærk evidens er ikke et krav.
- Rapporter: Randstad (Workmonitor, Employer Brand Research, Talent Trends), Gallup, Gartner, HBR, McKinsey, Deloitte, PwC, Mercer, Microsoft, LinkedIn, CIPD; dansk: STAR, DA, NFA, Lederne, Djøf. Opfind aldrig tal.

## Instruktion til NotebookLM (afsnit 1)
> Podcasten hedder Fordybelsestimen. Gennemgå alle tre kapitler i kilden i rækkefølge i én lang samtale. Nævn altid kilden ved navn – forfatter, organisation og årstal – når I bringer en pointe, et tal eller en historie. Slut med de vigtigste kilder. Forklar enkelt, men tal til voksne. Brug eksempler fra arbejdslivet og elitesporten. Rolig, varm tone – ingen fjollede jokes.

## Afsnit
1. `afsnit-01/` – Hvorfor gode teams går i stykker (Lencionis fem dysfunktioner). `Fordybelsestimen-01-Samlet.md` uploades; `dele/` er kapitlerne hver for sig.

## Sæsonplan
2 Ansvar (Lencioni, Sutton) · 3 Motivation (Pink, Deci & Ryan) · 4 Primadonnaer og ildsjæle (Hein, Herzberg) · 5 De små sejre (Amabile, Locke & Latham) · 6 Verdens kedeligste job (Lencioni, Gallup) · 7 Feedback (Scott, Stone & Heen, Kluger & DeNisi) · 8 Giverne og tagerne (Grant) · 9 Hvem skal på holdet (Lencioni, Bock, Kahneman) · 10 Myteknuseren (Buckingham & Goodall).

## Fravalgt / status
- Fravalgt: podcastside med computerstemmer og en 12-årig vært (for mekanisk, for kort, for barnligt).
- Den månedlige planlagte opgave "Fordybelsestimen – månedligt nyt afsnit" er sat på pause. Den beskriver stadig det gamle format og skal omskrives, før den slås til igen.
