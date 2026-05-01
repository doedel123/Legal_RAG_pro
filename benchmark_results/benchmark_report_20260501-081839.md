# RAG Benchmark Report

_Generiert: 2026-05-01T08:18:39_


- Queries: **18**
- Top-K: **10**
- Systeme: gemini, ours-mxbai

## Gesamtvergleich

| Metrik | gemini | ours-mxbai |
|--------|--------|--------|
| nDCG@10 | 0.921 | 0.954 |
| Relevance@10 | 72.8% | 76.7% |
| Relevance@3 | 90.7% | 88.9% |
| Top-1-Score | 2.67 | 2.78 |
| Mean-Score | 2.10 | 2.22 |
| Latenz (s) | 6.89 | 5.04 |

## Nach Kategorie


### alltagssprache

| Metrik | gemini | ours-mxbai |
|--------|--------|--------|
| nDCG@10 | 0.728 | 0.983 |
| Relevance@10 | 57.5% | 95.0% |
| Relevance@3 | 66.7% | 100.0% |

### cross-reference

| Metrik | gemini | ours-mxbai |
|--------|--------|--------|
| nDCG@10 | 0.941 | 0.914 |
| Relevance@10 | 56.7% | 46.7% |
| Relevance@3 | 88.9% | 66.7% |

### exakte-paragraphen

| Metrik | gemini | ours-mxbai |
|--------|--------|--------|
| nDCG@10 | 0.980 | 0.980 |
| Relevance@10 | 75.0% | 85.0% |
| Relevance@3 | 100.0% | 91.7% |

### konzept

| Metrik | gemini | ours-mxbai |
|--------|--------|--------|
| nDCG@10 | 0.995 | 0.938 |
| Relevance@10 | 85.0% | 72.5% |
| Relevance@3 | 100.0% | 91.7% |

### stpo-prozess

| Metrik | gemini | ours-mxbai |
|--------|--------|--------|
| nDCG@10 | 0.979 | 0.942 |
| Relevance@10 | 90.0% | 76.7% |
| Relevance@3 | 100.0% | 88.9% |

## Detail pro Query


### q01 — exakte-paragraphen

**Query:** Welche Voraussetzungen hat der gewerbsmaessige Bandenbetrug nach § 263 Abs. 5 StGB?

**Kontext:** Qualifikationstatbestand des Bandenbetrugs im Fischer-Kommentar

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours-mxbai | 0.96 | 70% | 67% | 3 | 6.0s |
| gemini | 1.00 | 80% | 100% | 3 | 7.1s |

#### ours-mxbai — Top 3
- **[Judge=3]** `§ 263 StGB – BT. Zweriindzwanzigster Abschnitt – Rn. 225` — Direkt relevant: erklärt Voraussetzungen Qualifikationstatbestand Abs. 5
  > IV. Qualifikation (Abs. 5). Abs. 5 enthält einen Qualifikationstatbestand, der die Tat in Fällen kumulativ gewerbs- und bandenmäßiger Begehung zum Verbrechen macht. Die Qualifikation ist in die Urteil...
- **[Judge=3]** `§ 263 StGB – BT. Zweijundzwanzigster Abschnitt – Rn. 213` — Direkt relevant zu Qualifikationstatbestand Bandenbetrug
  > 213 Sind beide Varianten erfüllt, ist eine Qualifikation nach Abs. 5 gegeben. Die Abgrenzung des Abs. 3 Nr. 1 zum Verbrechen nach Abs. 5 ist in Fällen bandenmäßiger Begehung schwierig, denn eine auf f...
- **[Judge=1]** `§ 263 StGB – I. Sonstige Vorschriften 239 – Rn. 263 (Teil 1)` — Inhaltsverzeichnis erwähnt Qualifikation, aber ohne Details
  > 3. Einzelne Fallgruppen ... 92 4. Rechtlich missbilligte, sittenwidrige und gesetzeswidrige wirtschaftliche Werte ... 101 VI. Schaden ... 110 1. Grundsätze der Schadensermittlung ... 111 2. Vermögensm...

#### gemini — Top 3
- **[Judge=3]** `StGB_Kommentar_part42.md` — Definiert direkt Voraussetzungen des gewerbsmäßigen Bandenbetrugs
  > einen Qualifikationstatbestand, der die Tat in Fällen kumulativ gewerbs- und bandenmäßiger Begehung zum Verbrechen macht. Die Qualifikation ist in die Urteilsformel aufzunehmen (BGH NStZ-RR 2007, 269;...
- **[Judge=3]** `StGB_Kommentar_part42.md` — Direkt relevant für Bandenbetrug Abs. 5 Voraussetzungen
  > der Bande handeln; die Tat nach § 263 muss im inhaltlichen Zusammenhang mit der Bandenabrede stehen.  213 Sind beide Varianten erfüllt, ist eine Qualifikation nach Abs. 5 gegeben. Die Abgrenzung des A...
- **[Judge=3]** `StGB_Kommentar_part42.md` — Direkt relevant: Gewerbsmäßigkeit als Qualifikationsmerkmal erklärt
  > Rn. 227). Zur Anwendung früheren Rechts (§ 2 Abs. 3) vgl. NStZ-RR 2007, 193.  1. Gewerbs- und Bandenmäßigkeit (Abs. 3 S. 2 Nr. 1). a) Gewerbsmäßigkeit. Gewerbsmäßige Begehung (zum Begriff vgl. → Vor §...

### q02 — exakte-paragraphen

**Query:** Was regelt § 112 StPO zur Untersuchungshaft?

**Kontext:** Anordnungsvoraussetzungen der U-Haft (dringender Tatverdacht, Haftgrund) im Schmitt/Koehler

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours-mxbai | 1.00 | 100% | 100% | 3 | 4.4s |
| gemini | 0.99 | 70% | 100% | 3 | 6.4s |

#### ours-mxbai — Top 3
- **[Judge=3]** `§ 112 StPO – Rn. 112` — Direkter Gesetzestext zu § 112 StPO mit Übersicht
  > 112 (1) ¹ Die Untersuchungshaft darf gegen den Beschuldigten angeordnet werden, wenn er der Tat dringend verdächtig ist und ein Haftgrund besteht. ² Sie darf nicht angeordnet werden, wenn sie zu der B...
- **[Judge=3]** `§ 112 StPO – III. Flucht (Abs – Rn. 32 (Teil 2)` — Direkte Erläuterung zu § 112 StPO Verdunkelungsgefahr
  > Wenn die Verdunkelungshandlungen nicht geeignet sind, die Ermittlung der Wahrheit zu erschweren, darf UHaft nicht angeordnet werden. Der Haftgrund liegt daher nicht vor, wenn der Sachverhalt schon in ...
- **[Judge=3]** `§ 112 StPO – Rn. 112` — Direkt relevant: behandelt Voraussetzungen des Haftbefehls
  > Haftunfähigkeit des Beschuldigten schließt den Erlass des Haftbefehls nicht aus, sondern hindert nur seinen Vollzug (OLG Düsseldorf JZ 1984, 248; OLG Frankfurt a.M. NJW 1968, 2302; OLG Nürnberg OLGSt ...

#### gemini — Top 3
- **[Judge=3]** `Strafprozessordnung_part14.md` — Direkte Erläuterung der Anordnungsvoraussetzungen nach § 112 StPO
  > 723  Verhaftung und vorläufige Festnahme  § 112 StPO  A. Allgemeine Grundsätze. Die Ermächtigung zum Erlass eines Haftbefehls, v. der nach pflichtgemäßem Ermessen Gebrauch zu machen ist (BVerfGE 19, 3...
- **[Judge=3]** `Strafprozessordnung_part14.md` — Direkt relevant: § 112 StPO Haftbefehl-Voraussetzungen
  > daß die Ermittlung der Wahrheit erschwert werde (Verdunkelungsgefahr).  (3) Gegen den Beschuldigten, der einer Straftat nach § 6 Absatz 1 Nummer 1 oder § 13 Absatz 1 des Völkerstrafgesetzbuches oder §...
- **[Judge=3]** `Strafprozessordnung_part14.md` — Vollständiger Text zu § 112 StPO Untersuchungshaftvoraussetzungen
  > ist auch die Unterbrechung der Strafhaft zum Zweck der Vollziehung der in anderer Sache angeordneten UHaft zulässig. Zur Anfechtbarkeit der Entsch. vgl. § 119a.  15 G. Bestand des Haftbefehls. Wird de...

### q03 — exakte-paragraphen

**Query:** Welche Haftgruende nennt § 112 Abs. 2 StPO?

**Kontext:** Fluchtgefahr, Verdunkelungsgefahr, Flucht — im StPO-Kommentar

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours-mxbai | 0.98 | 90% | 100% | 3 | 4.5s |
| gemini | 0.95 | 60% | 100% | 2 | 6.6s |

#### ours-mxbai — Top 3
- **[Judge=3]** `§ 112 StPO – Rn. 112` — Beantwortet direkt die Frage nach Haftgruenden
  > 112 (1) ¹ Die Untersuchungshaft darf gegen den Beschuldigten angeordnet werden, wenn er der Tat dringend verdächtig ist und ein Haftgrund besteht. ² Sie darf nicht angeordnet werden, wenn sie zu der B...
- **[Judge=3]** `§ 112 StPO – III. Flucht (Abs – Rn. 23` — Behandelt Haftgruende § 112 Abs. 2 StPO direkt
  > Bei einer besonders hohen Straferwartung braucht daher nur geprüft zu werden, ob Umstände vorhanden sind, die die hieraus herzuleitende Fluchtgefahr ausräumen können (KG StV 1996, 383; OLG München Str...
- **[Judge=2]** `§ 112 StPO – III. Flucht (Abs – Rn. 32 (Teil 2)` — Behandelt Verdunkelungsgefahr detailliert, aber nicht alle Haftgruende
  > Wenn die Verdunkelungshandlungen nicht geeignet sind, die Ermittlung der Wahrheit zu erschweren, darf UHaft nicht angeordnet werden. Der Haftgrund liegt daher nicht vor, wenn der Sachverhalt schon in ...

#### gemini — Top 3
- **[Judge=2]** `Strafprozessordnung_part14.md` — Behandelt Haftgruende aber nicht vollstaendig Abs. 2
  > Jugendarrest nach § 16 JGG (Löwe/Rosenberg/Hilger Rn. 3), auch wenn dieser neben Jugendstrafe verhängt wird (§ 16a JGG). Gleichgültig ist, ob neben der Strafe weitere Rechtsfolgen (Einziehung uA) ange...
- **[Judge=3]** `Strafprozessordnung_part14.md` — Listet alle drei Haftgründe des § 112 Abs. 2 StPO
  > daß die Ermittlung der Wahrheit erschwert werde (Verdunkelungsgefahr).  (3) Gegen den Beschuldigten, der einer Straftat nach § 6 Absatz 1 Nummer 1 oder § 13 Absatz 1 des Völkerstrafgesetzbuches oder §...
- **[Judge=2]** `Strafprozessordnung_part14.md` — Thematisch relevant, behandelt Haftgruende aber nicht konkret
  > dass bestimmte Tatsachen Flucht- o. Verdunkelungsgefahr begründen. Ausreichend, aber auch erforderlich ist die Feststellung, dass eine verhältnismäßig geringe o. entfernte Gefahr dieser Art besteht (v...

### q04 — exakte-paragraphen

**Query:** Was regelt § 102 StPO zur Durchsuchung beim Beschuldigten?

**Kontext:** Durchsuchungsvoraussetzungen beim Verdaechtigen

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours-mxbai | 0.97 | 80% | 100% | 3 | 4.3s |
| gemini | 0.98 | 90% | 100% | 3 | 6.3s |

#### ours-mxbai — Top 3
- **[Judge=3]** `§ 102 StPO – Rn. 102` — Direkte Wiedergabe von § 102 StPO mit Durchsuchungsvoraussetzungen
  > 102 Bei dem, welcher als Täter oder Teilnehmer einer Straftat oder der Datenhehlerei, Begünstigung, Strafvereitelung oder Hehlerei  Köhler    Ermittlungsmaßnahmen  verdächtig ist, kann eine Durchsuchu...
- **[Judge=2]** `§ 102 StPO – Rn. 10` — Behandelt Durchsuchungsvoraussetzungen allgemein, nicht speziell § 102
  > II. Auffinden von Beweismitteln. Zu den Beweismitteln (→ § 94 Rn. 4 ff.) gehören auch die nur in § 103 erwähnten Spuren (SK-StPO/Jäger/Wohlers Rn. 21) u. Personen, die zu Beweiszwecken in Augenschein ...
- **[Judge=3]** `§ 102 StPO – Rn. 10` — Erklärt direkt § 102 StPO Durchsuchungsobjekte beim Verdächtigen
  > 10 III. Sachen. Sachen sind Kleidungsstücke, die der Verdächtige bei sich führt, ohne sie zu tragen, u. seine sonstige bewegliche Habe, gleichgültig, ob sie sich in seinem Umkreis, zB in Gepäckstücken...

#### gemini — Top 3
- **[Judge=3]** `Strafprozessordnung_part12.md` — Direkt relevant: § 102 StPO Durchsuchungsvoraussetzungen beim Beschuldigten
  > Abs. 6. Die Mitteilung, wie oft u. aus welchen Gründen die beantragte Maßnahme nicht durchgeführt worden ist, ist nicht vorgesehen, kann aber sinnvoll sein. Die danach iE anzugebenden Daten werden idR...
- **[Judge=3]** `Strafprozessordnung_part12.md` — Direkt zu § 102 StPO Durchsuchung beim Verdächtigen
  > über seinen Internet-Account faktischen Zugriff auf den konkreten Cloud-Speicherplatz, auf dem seine Daten gespeichert sind u. damit – was für eine Durchsuchung beim Verdächtigen nach § 102 ausreicht ...
- **[Judge=2]** `Strafprozessordnung_part12.md` — Behandelt Wohnungsbegriff und Anwendungsbereich von § 102 StPO
  > Dazu gehören auch Arbeits-, Betriebs- u. Geschäftsräume (BVerfG NJW 2003, 2669) sowie Räume, die nur vorübergehend benutzt o. mitbenutzt werden (Geschäft, Hotelzimmer; nicht aber Wohnungen anderer Bew...

### q05 — konzept

**Query:** Wann liegt eine konkludente Taeuschung im Sinne des § 263 StGB vor?

**Kontext:** Taeuschungshandlung durch schluessiges Verhalten

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours-mxbai | 0.83 | 70% | 67% | 1 | 4.8s |
| gemini | 1.00 | 100% | 100% | 3 | 7.4s |

#### ours-mxbai — Top 3
- **[Judge=1]** `§ 263 StGB – I. Vermögensbegriff  – Rn. 263` — Gesetzestext ohne konkrete Erlaeuterung zur konkludenten Taeuschung
  > 263 (1) Wer in der Absicht, sich oder einem Dritten einen rechtswidrigen Vermögensvorteil zu verschaffen, das Vermögen eines anderen dadurch beschädigt, daß er durch Vorspiegelung falscher oder durch ...
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 28` — Behandelt direkt konkludente Taeuschung bei § 263 StGB
  > In Fällen sog. „Kostenfallen“ im Internet (vgl. dazu Eisele NStZ 2010, 193), bei denen unerfahrene Verbraucher durch (wahre) Versprechen besonders günstiger Angebote zum Abschluss von Verträgen gebrac...
- **[Judge=2]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 263 (Tei` — Literaturverzeichnis zu konkludenter Täuschung, aber ohne Inhalte
  > Heghmanns, Strafbarkeit des „Phishing“ von Bankkontendaten und ihrer Verwertung, wistra 2007, 167; Hilgendorf, Tatsachenaussagen u. Werturteile im Strafrecht, 1998; Hillenkamp, Zum Schutz „deliktische...

#### gemini — Top 3
- **[Judge=3]** `StGB_Kommentar_part41.md` — Direkt relevant - definiert konkludente Taeuschung bei § 263
  > Dagegen ist ein offenes Nicht-Offenbaren kein „Unterdrücken“: Eine ausdrückliche Weigerung, vermögensrelevante Angaben zu machen oder Auskünfte zu erteilen, ist daher idR kein „Unterdrücken“ dieser Ta...
- **[Judge=3]** `StGB_Kommentar_part41.md` — Direkt relevant: konkludente Täuschung bei § 263
  > ein konkludenter Erklärungswert zukommen. Aus der bloßen Feststellung eines Irrtums kann aber nicht schon auf eine (konkludente) Täuschung geschlossen werden (BGHSt 47, 1 (5)). Grenzfälle sind immer w...
- **[Judge=3]** `StGB_Kommentar_part41.md` — Direkt relevant: behandelt konkludente Taeuschung bei § 263
  > liege, die Geschäftsgrundlage nicht selbst manipuliert zu haben (zust. Wittig SpuRt 1994, 134 (136); Pawlik (→ Rn. 1a) S. 170; aA Klimke JZ 1980, 581; Weber in Pfister (Hrsg.), Rechtsprobleme der Spor...

### q06 — konzept

**Query:** Was ist eine Vermoegensverfuegung und welche Anforderungen stellt die Rechtsprechung?

**Kontext:** Tatbestandsmerkmal der Vermoegensverfuegung beim Betrug

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours-mxbai | 0.95 | 70% | 100% | 3 | 5.3s |
| gemini | 0.98 | 60% | 100% | 3 | 7.6s |

#### ours-mxbai — Top 3
- **[Judge=3]** `§ 263 StGB – BT. Zweitundzwanzigster Abschnitt – Rn. 69` — Definiert Vermoegensverfuegung und nennt Rechtsprechungsanforderungen
  > 69 Anders ist es, wenn der Verfügende seinerseits nur (gutgläubige) Hilfsperson eines bösgläubigen Dritten ist. Hier ist auf den Irrtum des Entscheidungsbefugten abzustellen: Erkennt dieser die Unrich...
- **[Judge=2]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 87` — Behandelt Kausalitaet und Vermoegensschaden, nicht Verfuegung selbst
  > 87 5. Kausalität. Für die Vermögensverfügung muss der täuschungsbedingte Irrtum kausal sein (vgl. BGHSt 24, 257 (260); 24, 386 (389); NStZ 2003, 313 (314 f.); OLG Düsseldorf NJW 1987, 3145); Mitverurs...
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 76` — Direkt relevant: definiert Unmittelbarkeit der Vermögensverfügung
  > 76 3. Unmittelbarkeit der Verfügung. Neben der Freiwilligkeit ist das Merkmal der Unmittelbarkeit nach stRspr und hM das wichtigste Kriterium zur Beschränkung der § 263 unterfallenden Selbstschädigung...

#### gemini — Top 3
- **[Judge=3]** `StGB_Kommentar_part41.md` — Direkt relevant: Vermoegensverfuegung beim Betrug zentral behandelt
  > reicht nicht für sich allein für die Unterstellung aus, er hätte die Verfügung auch bei Kenntnis der wahren Sachlage vorgenommen; insbes. wenn die Verfügung pflichtändig ist (BGH(Z) GmbHR 2001, 1036 (...
- **[Judge=3]** `StGB_Kommentar_part41.md` — Direkt relevant: Definition und Rechtsprechung zur Vermoegensverfuegung
  > aber mögliche Kompensationen einbezieht (BGHSt 31, 178); teilweise wird die Zuordnung eines Tatumstands in der Rspr. auch eher offengelassen (vgl. etwa NStZ 2009, 329 (330) (Aushändigung einer EC-Zahl...
- **[Judge=3]** `StGB_Kommentar_part41.md` — Direkt relevant: Definition und Rechtsprechung zu Vermoegensverfuegung
  > wenn der Täter sich unter einem Vorwand Zugang zu Sachen des Opfers verschafft (BGHSt 14, 170 (171); 17, 205), oder bei der Ausstellung einer Blankovollmacht zum Zwecke der Kündigung von Versicherunge...

### q07 — konzept

**Query:** Was versteht man unter einem Gefaehrdungsschaden beim Betrug?

**Kontext:** Schadensbegriff, schadensgleiche Vermoegensgefaehrdung

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours-mxbai | 0.99 | 90% | 100% | 3 | 5.3s |
| gemini | 1.00 | 100% | 100% | 3 | 5.9s |

#### ours-mxbai — Top 3
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 159` — Direkt relevant: definiert Gefährdungsschaden beim Betrug
  > 159 b) Voraussetzungen. aa) Ein Gefährdungsschaden ist gegeben, wenn die Wahrscheinlichkeit des endgültigen Verlusts eines Vermögensbestandteils zum Zeitpunkt der täuschungsbedingten Verfügung so groß...
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 182` — Definiert direkt Gefaehrdungsschaden und dessen rechtliche Bewertung
  > 182 In Fällen des Gefährdungsschadens hat der BGH vielfach entschieden, die Kenntnis von Umständen, welche die Gefahr des Vermögensverlusts begründen, reiche oft, aber nicht in jedem Fall aus, um das ...
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 109` — Erwähnt explizit Gefährdungsschaden beim Betrug
  > VI. Schaden. Vermögensschaden ist ein negativer Saldo zwischen dem Wert des Vermögens vor und nach der irrtumsbedingten Vermögensverfügung des Getäuschten (Prinzip der Gesamtsaldierung; stRspr; vgl. B...

#### gemini — Top 3
- **[Judge=3]** `StGB_Kommentar_part42.md` — Definiert direkt Gefaehrdungsschaden beim Betrug
  > ff.); Schlösser NStZ 2009, 663 (664 f.).  158 Der 3. StS hat in BGHSt 54, 69 (122 ff.) (Anm. Joecks wistra 2010, 179; vgl. → Rn. 8; → Rn. 176) sowohl der Sache nach als auch begrifflich am „Gefährdung...
- **[Judge=3]** `StGB_Kommentar_part42.md` — Erklaert direkt Gefaehrdungsschaden beim Betrug
  > Wegner)).  Die Verlustgefahr muss bei lebensnaher Betrachtung zu einer Vermögensminderung zum Zeitpunkt der Verfügung führen (BVerfG NJW 2010, 3209 Rn. 138, 142 mwN; wistra 1995, 223; BayObLG NJW 1988...
- **[Judge=3]** `StGB_Kommentar_part42.md` — Erklärt direkt Gefährdungsschaden beim Betrug mit Details
  > und „Endgültigkeit“ vor (vgl. BGHR § 263 I VermSchad 3; NJW 2008, 2451; Nack StraFo 2008, 277; krit. aber auch insoweit zB Bung (→ Rn. 1a) S. 363, 365; Bernsmann GA 2007, 219 (229 ff.)); der Gefährdun...

### q08 — konzept

**Query:** Wie wird der Vorsatz beim Betrug bestimmt, insbesondere die Bereicherungsabsicht?

**Kontext:** Subjektiver Tatbestand § 263 StGB

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours-mxbai | 0.98 | 60% | 100% | 3 | 5.0s |
| gemini | 1.00 | 80% | 100% | 3 | 8.1s |

#### ours-mxbai — Top 3
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 176` — Direkt relevant: behandelt Vorsatz und Bereicherungsabsicht § 263
  > D. Subjektiver Tatbestand. § 263 setzt Vorsatz voraus; darüber hinaus ist die Absicht rechtswidriger Bereicherung erforderlich.   I. Vorsatz. 1. Täuschungsvorsatz. Der Vorsatz (bedingter Vorsatz genüg...
- **[Judge=3]** `§ 263 StGB – I. Sonstige Vorschriften 239 – Rn. 263 (Teil 1)` — Behandelt direkt Bereicherungsabsicht und subjektiven Tatbestand
  > 3. Einzelne Fallgruppen ... 92 4. Rechtlich missbilligte, sittenwidrige und gesetzeswidrige wirtschaftliche Werte ... 101 VI. Schaden ... 110 1. Grundsätze der Schadensermittlung ... 111 2. Vermögensm...
- **[Judge=2]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 187 (Tei` — Objektiver Tatbestand, nicht Vorsatz/Bereicherungsabsicht
  > 187 1. Stoffgleichheit. Der Vorteil muss die Kehrseite des Schadens und ihm „stoffgleich“ sein; er muss unmittelbare Folge der täuschungsbedingten Verfügung sein, welche den Schaden des Opfers herbeif...

#### gemini — Top 3
- **[Judge=3]** `StGB_Kommentar_part42.md` — Direkt relevant: behandelt Vorsatz und Bereicherungsabsicht bei § 263
  > rechtswidriger Bereicherung erforderlich.  179  I. Vorsatz. 1. Täuschungsvorsatz. Der Vorsatz (bedingter Vorsatz genügt; BGHSt 16, 1; 18, 235 (237); 48, 331 (346); stRspr; and. Dencker FS Grünwald, 19...
- **[Judge=3]** `StGB_Kommentar_part42.md` — Direkt relevant: behandelt Bereicherungsabsicht bei Betrug
  > daher zB Feigen FS Rudolphi, 2004, 445 (460 f.) mwN; Fischer StraFo 2008, 269 ff.; Fischer NStZ-Sonderheft f. Miebach 2009, 8 (13 ff.); Fischer StV 2010, 95 ff.; vgl. auch Nack StraFo 2008, 277 (278 f...
- **[Judge=3]** `StGB_Kommentar_part45.md` — Direkt relevant: behandelt Bereicherungsabsicht bei § 263 StGB
  > Nr. 9), also im Hinblick auf eine in einem Vermögensvorteil bestehende Gegenleistung ohne Rücksicht darauf, ob eine Bereicherung angestrebt oder erreicht wird.  II. Bereicherungsabsicht. Handeln in de...

### q09 — alltagssprache

**Query:** Hat der Angeklagte die Kunden über das Internet betrogen?

**Kontext:** Abstrakte Frage zu Internetbetrug, sucht Taeuschungshandlung + Schaden

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours-mxbai | 0.97 | 100% | 100% | 3 | 4.6s |
| gemini | 0.99 | 70% | 100% | 3 | 6.2s |

#### ours-mxbai — Top 3
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 5` — Definiert Betrug-Tatbestandsmerkmale: Täuschung, Irrtum, Vermögensschaden
  > 5 C. Grundtatbestand, Abs. 1. Tathandlung ist das Täuschen einer natürlichen Person (vgl. NStZ 2005, 213) über Tatsachen. Erfolg dieser Handlung muss ein Irrtum des Täuschungsadressaten sein; dieser m...
- **[Judge=2]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 87` — Behandelt Betrugstatbestand, aber nicht spezifisch Internetbetrug
  > 87 5. Kausalität. Für die Vermögensverfügung muss der täuschungsbedingte Irrtum kausal sein (vgl. BGHSt 24, 257 (260); 24, 386 (389); NStZ 2003, 313 (314 f.); OLG Düsseldorf NJW 1987, 3145); Mitverurs...
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 109` — Direkt relevant: zentrale Schadensdefinition beim Betrug
  > VI. Schaden. Vermögensschaden ist ein negativer Saldo zwischen dem Wert des Vermögens vor und nach der irrtumsbedingten Vermögensverfügung des Getäuschten (Prinzip der Gesamtsaldierung; stRspr; vgl. B...

#### gemini — Top 3
- **[Judge=3]** `StGB_Kommentar_part41.md` — Direkt relevant zu Internetbetrug und Täuschungshandlungen
  > darauf gestützt, dass der Täter das (regelmäßig massenhaft verbreitete) Schreiben planvoll und absichtlich so formuliert und gestaltet, dass es auf die Erzielung einer Fehlvorstellung (Zahlungspflicht...
- **[Judge=3]** `StGB_Kommentar_part41.md` — Direkter Bezug zu Internetbetrug und Taeuschungshandlungen
  > 2595; Routenplaner). Dies sind scheinbar unentgeltliche Informationsangebote (Wetterberichte; Routenplaner; Börsennachrichten, u.a.), die an versteckter Stelle Hinweise auf Kostenpflichtigkeit des Abr...
- **[Judge=2]** `StGB_Kommentar_part45.md` — Behandelt Internetbetrug mit falschen Identitaeten und Kundenkonten
  > erfasst (NStZ 2021, 43 (45) (eBay-Account); KG NStZ 2010, 576; aA OLG Hamm StV 2009, 475; vgl. → Rn. 6). Dasselbe gilt für das Anlegen eines Online-Kundenkontos unter fremdem Namen ohne Einwilligung d...

### q10 — alltagssprache

**Query:** Wann darf die Polizei bei jemandem zu Hause suchen?

**Kontext:** Durchsuchungsvoraussetzungen, §§ 102 ff. StPO

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours-mxbai | 0.98 | 80% | 100% | 3 | 4.7s |
| gemini | 0.00 | 0% | 0% | 0 | 6.1s |

#### ours-mxbai — Top 3
- **[Judge=3]** `§ 102 StPO – Rn. 102` — Direkt relevant zu Durchsuchungsvoraussetzungen bei Wohnungen
  > 102 Bei dem, welcher als Täter oder Teilnehmer einer Straftat oder der Datenhehlerei, Begünstigung, Strafvereitelung oder Hehlerei  Köhler    Ermittlungsmaßnahmen  verdächtig ist, kann eine Durchsuchu...
- **[Judge=3]** `§ 102 StPO – Rn. 3` — Direkt relevant zu Durchsuchungsvoraussetzungen bei Wohnungen
  > **Teilnehmer** nach §§ 25 ff. StGB, nicht die sog. notwendigen Teilnehmer (zum Begriff: Fischer/Fischer StGB Vor § 25 Rn. 7), stehen den Tatverdächtigen gleich. Bei jedem v. ihnen sowie bei den der Be...
- **[Judge=3]** `§ 102 StPO – Rn. 10` — Direkt relevant zu Durchsuchungsvoraussetzungen nach StPO
  > II. Auffinden von Beweismitteln. Zu den Beweismitteln (→ § 94 Rn. 4 ff.) gehören auch die nur in § 103 erwähnten Spuren (SK-StPO/Jäger/Wohlers Rn. 21) u. Personen, die zu Beweiszwecken in Augenschein ...

#### gemini — Top 3

### q11 — alltagssprache

**Query:** Was passiert wenn jemand luegt damit er Geld bekommt?

**Kontext:** Laienhafte Umschreibung des Betrugstatbestandes

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours-mxbai | 1.00 | 100% | 100% | 3 | 5.2s |
| gemini | 0.93 | 60% | 67% | 3 | 7.8s |

#### ours-mxbai — Top 3
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 5` — Definiert direkt den Betrugstatbestand mit Täuschung
  > 5 C. Grundtatbestand, Abs. 1. Tathandlung ist das Täuschen einer natürlichen Person (vgl. NStZ 2005, 213) über Tatsachen. Erfolg dieser Handlung muss ein Irrtum des Täuschungsadressaten sein; dieser m...
- **[Judge=3]** `§ 263 StGB – I. Vermögensbegriff  – Rn. 263` — Exakte Definition des Betrugstatbestandes - direkt relevant
  > 263 (1) Wer in der Absicht, sich oder einem Dritten einen rechtswidrigen Vermögensvorteil zu verschaffen, das Vermögen eines anderen dadurch beschädigt, daß er durch Vorspiegelung falscher oder durch ...
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 176` — Direkt relevant für subjektive Tatbestandsmerkmale des Betrugs
  > D. Subjektiver Tatbestand. § 263 setzt Vorsatz voraus; darüber hinaus ist die Absicht rechtswidriger Bereicherung erforderlich.   I. Vorsatz. 1. Täuschungsvorsatz. Der Vorsatz (bedingter Vorsatz genüg...

#### gemini — Top 3
- **[Judge=3]** `StGB_Kommentar_part41.md` — Direkt relevant: behandelt Betrug durch Tauschung fuer Geld
  > und des Vorsatzes, des aktiven Tuns und des Unterlassens: Wer annimmt, er werde bis zur Fälligkeit noch im Lotto gewinnen, ist jedenfalls zur Offenbarung dieser „Überzeugung“ verpflichtet (vgl. StV 19...
- **[Judge=1]** `StGB_Kommentar_part42.md` — Subventionsbetrug, nicht allgemeiner Betrug
  > oder mündlich Angaben macht, die entweder unrichtig (NStZ 2010, 327) oder unvollständig sind (wistra 2006, 262 (264)). Angaben iSv Nr. 1 sind ausdrückliche oder konkludente Gedankenerklärungen (vgl. N...
- **[Judge=3]** `StGB_Kommentar_part41.md` — Behandelt Betrugstatbestand mit Taeuschung zur Gelderlangung
  > Schadens setzt voraus, dass die Inanspruchnahme zweckwidrig erfolgte (NStZ 2006, 624 (624 f.) (Anm. Allgayer wistra 2006, 261); vgl. auch Gaede/Leydecker NJW 2009, 3542 (3544) (Förderung von vorgetäus...

### q12 — alltagssprache

**Query:** Wann muss jemand ins Gefaengnis waehrend die Tat noch nicht bewiesen ist?

**Kontext:** Untersuchungshaft, §§ 112 ff. StPO

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours-mxbai | 0.98 | 100% | 100% | 3 | 5.3s |
| gemini | 1.00 | 100% | 100% | 3 | 5.7s |

#### ours-mxbai — Top 3
- **[Judge=3]** `§ 112 StPO – Rn. 112` — Beantwortet direkt die Voraussetzungen der Untersuchungshaft
  > 112 (1) ¹ Die Untersuchungshaft darf gegen den Beschuldigten angeordnet werden, wenn er der Tat dringend verdächtig ist und ein Haftgrund besteht. ² Sie darf nicht angeordnet werden, wenn sie zu der B...
- **[Judge=3]** `§ 112 StPO – Rn. 112` — Erklaert dringenden Tatverdacht fuer Untersuchungshaft direkt
  > Haftunfähigkeit des Beschuldigten schließt den Erlass des Haftbefehls nicht aus, sondern hindert nur seinen Vollzug (OLG Düsseldorf JZ 1984, 248; OLG Frankfurt a.M. NJW 1968, 2302; OLG Nürnberg OLGSt ...
- **[Judge=3]** `§ 112 StPO – Rn. 11 (Teil 1)` — Verhältnismäßigkeitsprüfung bei Untersuchungshaft, direkt relevant
  > 11 Abzuwägen für die Beurteilung der Verhältnismäßigkeit sind die Schwere des Eingriffs in die Lebenssphäre des Beschuldigten, wobei auch sein Gesundheitszustand zu berücksichtigen ist (BGH StraFo 201...

#### gemini — Top 3
- **[Judge=3]** `Strafprozessordnung_part14.md` — Direkt relevant: behandelt Untersuchungshaft nach §§ 112 ff. StPO
  > B. Besondere Arten | 5 | | C. Auslieferungsverfahren | 8 | | D. Europäischer Haftbefehl | 9 | | I. Anwendungsbereich | 9a | | II. Ablehnung | 9b | | III. Erlass | 9e | | IV. Grundsatz der Spezialität ...
- **[Judge=3]** `Strafprozessordnung_part14.md` — Direkt relevant für Untersuchungshaft bei dringendem Tatverdacht
  > der Beschuldigte dringend verdächtig ist,  1. eine Straftat nach den §§ 174, 174a, 176 bis 176d, 177, 178, 184b Absatz 2 oder nach § 238 Abs. 2 und 3 des Strafgesetzbuches oder 2. wiederholt oder fort...
- **[Judge=3]** `Strafprozessordnung_part14.md` — Beantwortet direkt die Frage zur Untersuchungshaft
  > ist auch die Unterbrechung der Strafhaft zum Zweck der Vollziehung der in anderer Sache angeordneten UHaft zulässig. Zur Anfechtbarkeit der Entsch. vgl. § 119a.  15 G. Bestand des Haftbefehls. Wird de...

### q13 — stpo-prozess

**Query:** Welche Voraussetzungen hat die Untersuchungshaft wegen Fluchtgefahr?

**Kontext:** § 112 Abs. 2 Nr. 2 StPO Fluchtgefahr

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours-mxbai | 0.93 | 80% | 67% | 3 | 4.6s |
| gemini | 1.00 | 100% | 100% | 3 | 7.3s |

#### ours-mxbai — Top 3
- **[Judge=3]** `§ 112 StPO – Rn. 112` — Enthält vollständigen Gesetzestext zu § 112 StPO Fluchtgefahr
  > 112 (1) ¹ Die Untersuchungshaft darf gegen den Beschuldigten angeordnet werden, wenn er der Tat dringend verdächtig ist und ein Haftgrund besteht. ² Sie darf nicht angeordnet werden, wenn sie zu der B...
- **[Judge=1]** `§ 112 StPO – Rn. 112` — Allgemeine Haftvoraussetzungen, nicht spezifisch Fluchtgefahr
  > Haftunfähigkeit des Beschuldigten schließt den Erlass des Haftbefehls nicht aus, sondern hindert nur seinen Vollzug (OLG Düsseldorf JZ 1984, 248; OLG Frankfurt a.M. NJW 1968, 2302; OLG Nürnberg OLGSt ...
- **[Judge=3]** `§ 112 StPO – III. Flucht (Abs – Rn. 16` — Direkt relevant zu Fluchtgefahr nach § 112 Abs. 2 Nr. 2
  > 16 Bei Ergreifung des Beschuldigten aufgrund des nach Abs. 2 Nr. 1 erlassenen Haftbefehls entfällt der Haftgrund der Flucht. In der Regel wird die vorherige Flucht aber die Aufrechterhaltung des Haftb...

#### gemini — Top 3
- **[Judge=3]** `Strafprozessordnung_part14.md` — Direkt relevant: definiert Fluchtgefahr nach § 112 Abs. 2 Nr. 2
  > Flucht aber die Aufrechterhaltung des Haftbefehls wegen Fluchtgefahr nach Abs. 2 Nr. 2 rechtfertigen u. erforderlich machen.  17 IV. Fluchtgefahr (Abs. 2 Nr. 2). Fluchtgefahr (Abs. 2 Nr. 2) besteht, w...
- **[Judge=3]** `Strafprozessordnung_part14.md` — Direkt relevant zu Fluchtgefahr-Voraussetzungen § 112 StPO
  > 17a); allerdings ist bei einem nicht sesshaften Beschuldigten, dessen Asylbegehren noch nicht verbeschieden u. dessen dauerhafter Aufenthaltsstatus im Bundesgebiet daher fraglich ist, unabhängig v. de...
- **[Judge=3]** `Strafprozessordnung_part14.md` — Direkt relevant - behandelt Fluchtgefahr-Voraussetzungen nach § 112 StPO
  > § 230 Abs. 2 in Betracht zu ziehen; erg. → Rn. 17a). Bei Asylbewerbern ohne tragfähige soziale Bindungen im Inland ist ebenfalls nicht automatisch Fluchtgefahr anzunehmen (s. OLG Stuttgart StV 2016, 8...

### q14 — stpo-prozess

**Query:** Wie lange darf die Untersuchungshaft maximal dauern?

**Kontext:** § 121 StPO Sechs-Monats-Grenze, Haftpruefung OLG

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours-mxbai | 0.98 | 80% | 100% | 3 | 5.0s |
| gemini | 0.98 | 90% | 100% | 3 | 7.3s |

#### ours-mxbai — Top 3
- **[Judge=3]** `§ 121 StPO – Rn. 1` — Direkt relevant: maximale Dauer der Untersuchungshaft
  > Eine absolute Höchstgrenze für die Dauer v. UHaft sieht weder die StPO noch die EMRK vor (EGMR EuGRZ 1993, 384). Es kommt auf eine Abwägung aller Umstände des Einzelfalls an. Eine ein Jahr übersteigen...
- **[Judge=3]** `§ 121 StPO – Rn. 121` — Direkter Pararaph zur maximalen Untersuchungshaftdauer
  > 121 (1) Solange kein Urteil ergangen ist, das auf Freiheitsstrafe oder eine freiheitsentziehende Maßregel der Besserung und Sicherung erkennt, darf der Vollzug der Untersuchungshaft wegen derselben Ta...
- **[Judge=3]** `§ 121 StPO – Rn. 13` — Direkt zur Sechs-Monats-Grenze der Untersuchungshaft
  > 13 Das bedeutet: Wird UHaft vollzogen, so darf sie nicht aufgrund eines weiteren Haftbefehls, der bereits bei Erlass des 1. Haftbefehls bekannt gewesene Tatvorwürfe zum Gegenstand hat, über 6 Monate h...

#### gemini — Top 3
- **[Judge=3]** `Strafprozessordnung_part15.md` — Direkt relevant: behandelt Sechs-Monats-Grenze und OLG-Anordnung
  > hat der in UHaft (und einstweiliger Unterbringung) befindliche Beschuldigte nach Art. 5 Abs. 3 S. 2 EMRK (→ EMRK Art. 5 Rn. 10 ff.) u. aufgrund des aus Art. 2 Abs. 2 S. 2 GG herzuleitenden verfassungs...
- **[Judge=3]** `Strafprozessordnung_part15.md` — Behandelt direkt die Sechs-Monats-Grenze der Untersuchungshaft
  > beschiedene Haftbeschwerde (→ § 117 Rn. 13). Ist in dem rkr. Urt. aber auf eine Bewährungsstrafe o. nicht auf Freiheitsentzug erkannt, so muss der Haftbefehl aufgeh. werden. Zur Aufhebung v. Maßnahmen...
- **[Judge=2]** `Strafprozessordnung_part15.md` — Behandelt UHaft-Dauer, aber nicht konkrete Sechs-Monats-Grenze
  > § 120 Rn. 3 ff., → EMRK Art. 6 Rn. 7a ff.  Das Beschleunigungsgebot kann nach der Rspr. des EuGH Einschränkungen in Vorlagefällen nach Art. 267 AEUV erfahren. Danach darf ein nationales Gericht, das e...

### q15 — stpo-prozess

**Query:** Was regelt § 136 StPO zur Beschuldigtenvernehmung?

**Kontext:** Belehrungspflichten, Recht auf Verteidiger

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours-mxbai | 0.92 | 70% | 100% | 2 | 5.4s |
| gemini | 0.96 | 80% | 100% | 3 | 7.8s |

#### ours-mxbai — Top 3
- **[Judge=2]** `§ 16a StPO – ILL. für das Strafverfahren und das Bußgeldverf` — Behandelt Beschuldigtenvernehmung, aber nicht § 136 StPO direkt
  > (4) Zeugen können zur Aufenthaltsermittlung ausgeschrieben werden.  (5) Für die internationale Fahndung nach Personen, einschließlich der Fahndung nach Personen im SIS und aufgrund eines Europäischen ...
- **[Judge=3]** `§ 399 AO – Rn. 8` — Direkt relevant: behandelt § 136 StPO Belehrungspflichten
  > 8 a) Vernehmung des Beschuldigten. Spätestens vor Abschluss der Ermittlungen ist der Beschuldigte zu vernehmen (§ 163a I 1 StPO). In einfachen Sachen genügt es, dass ihm Gelegenheit gegeben wird, sich...
- **[Judge=3]** `§ 135 OWiG – A. 2 StPO – Rn. 41` — Direkt relevant: behandelt § 136 StPO Belehrungspflichten
  > ## Abschnitt 9b Vorläufiges Berufsverbot  ## § 132a Anordnung und Aufhebung eines vorläufigen Berufsverbots nicht abgedruckt⁶⁵  ## Zehnter Abschnitt Vernehmung des Beschuldigten  ## § 133 Ladung⁶⁶ VB ...

#### gemini — Top 3
- **[Judge=3]** `Strafprozessordnung_part01.md` — Direkt relevant zu § 136 StPO Belehrungspflichten
  > 367); ggf. ist eine Zeugenvernehmung (für richterliche Vernehmungen vgl. → StPO § 136 Rn. 3) als Beschuldigtenvernehmung fortzusetzen (BGHSt 22, 129 (132)). Ist die erforderliche Belehrung unterbliebe...
- **[Judge=2]** `Strafprozessordnung_part13.md` — Behandelt Belehrungspflichten § 136, aber Verdeckte Ermittler-Kontext
  > Tätigkeit auch § 136a beachten, soweit er nicht „legendenbedingte“ Täuschungen vornimmt (Krey Rechtsprobleme Rn. 221 ff.; Lagodny StV 1996, 172; Rogall NStZ 2008, 111; Alsberg Beweisantrag/Günte Rn. 9...
- **[Judge=2]** `Strafprozessordnung_part47.md` — Behandelt Belehrungspflichten bei Vernehmung nach § 136
  > sich zu der Beschuldigung äußert will, einer Aussagegenehmigung des Dienstherrn bedarf. ² Erklärt der Beschuldigte seine Aussagebereitschaft, soll ihm Gelegenheit gegeben werden, diese Aussagegenehmig...

### q16 — cross-reference

**Query:** Worin unterscheidet sich Betrug von Unterschlagung?

**Kontext:** Abgrenzung § 263 vs § 246 StGB

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours-mxbai | 0.86 | 40% | 67% | 2 | 5.2s |
| gemini | 0.96 | 20% | 67% | 2 | 7.3s |

#### ours-mxbai — Top 3
- **[Judge=2]** `§ 247 StGB – BT. Neunzehnter Abschnitt – Rn. 24` — Behandelt Konkurrenzen, erwähnt Betrug-Unterschlagung-Abgrenzung kurz
  > 24 L. Konkurrenzen im Übrigen. Bei Manifestation des Zueignungswillens hinsichtlich mehrerer Sachen durch eine Ausführungshandlung liegt nur eine Tat vor (wistra 2006, 227 (227 f.)). Zur Abgrenzung vo...
- **[Judge=1]** `§ 263 StGB – BT. Zweitundzwanzigster Abschnitt – Rn. 69` — Behandelt Betrug, aber nicht Abgrenzung zur Unterschlagung
  > 69 Anders ist es, wenn der Verfügende seinerseits nur (gutgläubige) Hilfsperson eines bösgläubigen Dritten ist. Hier ist auf den Irrtum des Entscheidungsbefugten abzustellen: Erkennt dieser die Unrich...
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 76` — Erklaert Dreiecksbetrug und Abgrenzung zu Diebstahl
  > 4. Dreiecksbetrug. Da die Getäuschte und die verfügende, nicht aber die verfügende und die geschädigte Person identisch sein müssen, ist der Tatbestand des § 263 nur erfüllt, wenn die Vermögensverfügu...

#### gemini — Top 3
- **[Judge=2]** `StGB_Kommentar_part45.md` — Behandelt Abgrenzung, aber fokussiert auf Untreue-Tateinheit
  > Unterschlagung einer Sache oder ihres Erlöses (BGHSt 13, 315; 18, 312), wenn der Zueignungsvorsatz erst später gefasst wird: sonst tritt § 246 gegenüber § 266 zurück (vgl. BGHSt 6, 308 (310); 8, 254 (...
- **[Judge=1]** `StGB_Kommentar_part38.md` — Tangential: § 247 zu Haus-/Familiendiebstahl, nicht Abgrenzung
  > geschieht; dagegen ist ein der Unterschlagung nachfolgender Sicherungsbetrug mitbestrafte Nachtat. Die veruntreuende Unterschlagung tritt gegenüber § 266 zurück.  25 M. Sonstige Vorschriften. § 246 is...
- **[Judge=2]** `StGB_Kommentar_part38.md` — Behandelt Abgrenzung § 246 zu § 263
  > Strafe angedroht ist; der Täter ist aus § 246 zu bestrafen. Bei Konkurrenz von § 246 Abs. 1 mit § 125 Abs. 1 ist ein Vorrang nicht gegeben; hier führt die den Täter „begünstigende“ Auslegung des BGH (...

### q17 — cross-reference

**Query:** Was sind die Unterschiede zwischen Diebstahl und Raub?

**Kontext:** § 242 vs § 249 StGB — Abgrenzung durch Gewalt/Drohung

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours-mxbai | 0.96 | 80% | 100% | 3 | 5.9s |
| gemini | 0.96 | 90% | 100% | 3 | 5.7s |

#### ours-mxbai — Top 3
- **[Judge=3]** `§ 249 StGB` — Direkt relevant: Raub-Abgrenzung, Wegnahme, Nötigungsmittel erklärt
  > NStZ 2023, 351). Danach ist § 249 gegenüber § 255 ein spezielles Delikt; in jedem Raub liegt eine räuberische Erpressung (aA die hM in der Literatur). Die Unterscheidung richtet sich nach dem äußeren ...
- **[Judge=3]** `§ 249 StGB – BT. Zwanzigster Abschnitt – Rn. 15` — Direkt relevant: Abgrenzung Diebstahl-Raub durch subjektiven Tatbestand
  > G. Subjektiver Tatbestand. Der Vorsatz muss entsprechend der Doppelnatur des Raubs sowohl Wegnahme (vgl. dazu → § 242 Rn. 29 ff.) als auch Nötigung (→ § 240 Rn. 53 f.) sowie deren Verknüpfung umfassen...
- **[Judge=3]** `§ 241a StGB – BT. Achtzchniter Abschnitt – Rn. 242` — Zeigt grundlegende Diebstahl-Definition für Abgrenzung zum Raub
  > 242 (1) Wer eine fremde bewegliche Sache einem anderen in der Absicht wegnimmt, die Sache sich oder einem Dritten rechtswidrig zuzueignen, wird mit Freiheitsstrafe bis zu fünf Jahren oder mit Geldstra...

#### gemini — Top 3
- **[Judge=3]** `StGB_Kommentar_part39.md` — Direkte Abgrenzung Raub zu Diebstahl mit Systematik
  > NStZ-RR 2010, 129; Maier NStZ-RR 2012, 297; 2013, 329 (364); 2015, 33; 2017, 1, 2018, 33; 2025, 129; 2025, 161.  2 B. Systematische Stellung. Raub als selbstständiges Delikt (BGHSt 20, 235 (237 f.)) r...
- **[Judge=3]** `StGB_Kommentar_part39.md` — Direkt relevant: definiert Raub mit Gewalt/Drohung-Abgrenzung
  > Raub  249 (1) Wer mit Gewalt gegen eine Person oder unter Anwendung von Drohungen mit gegenwärtiger Gefahr für Leib oder Leben eine fremde bewegliche Sache einem anderen in der Absicht wegnimmt, die S...
- **[Judge=2]** `StGB_Kommentar_part39.md` — Behandelt Raub-Kontext, aber fokussiert auf räuberischen Diebstahl
  > 2001, 31); aA NK-StGB/Kindhäuser Rn. 12); bei versuchtem § 251 ist Tateinheit gegeben (BGHSt 46, 24 (28) (Anm. Stein JR 2001, 70); BeckRS 2017, 129562). Hatte der Täter zumindest bedingten Vorsatz hin...

### q18 — cross-reference

**Query:** Wann wird Betrug zu Computerbetrug und umgekehrt?

**Kontext:** § 263 vs § 263a StGB — Abgrenzung bei elektronischer Datenverarbeitung

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours-mxbai | 0.92 | 20% | 33% | 3 | 5.0s |
| gemini | 0.90 | 60% | 100% | 2 | 7.4s |

#### ours-mxbai — Top 3
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 58` — Direkt relevant: Abgrenzung Betrug/Computerbetrug bei automatisierten Verfahren
  > 58 Im Geschäftsverkehr wird sich, wer die Berechtigung eines Leistungsverlangens oder -auftrags nicht zu prüfen hat, hierüber idR auch keine (richtigen oder falschen) Gedanken machen (NStZ 1997, 281; ...
- **[Judge=1]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 62` — Behandelt Betrug allgemein, nicht Abgrenzung zu Computerbetrug
  > Die Kausalität der Täuschung für den Irrtum und dessen Kausalität für die Vermögensverfügung müssen im Einzelfall festgestellt sein. Mitverursachung reicht aus. Dabei darf das Gericht auch bei Serien-...
- **[Judge=0]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 114` — Allgemeiner Schadensbegriff, kein Bezug zu Computerbetrug
  > 114 a) Quantifizierbarkeit der Vermögensminderung. Die Vermögensminderung muss quantifizierbar sein (RGSt 16, 4; 44, 249; BGHSt 16, 321). Grds. nicht ausreichend ist eine nicht quantifizierbare Einbuß...

#### gemini — Top 3
- **[Judge=2]** `StGB_Kommentar_part42.md` — Behandelt Computerbetrug, aber nicht die Abgrenzung
  > WeinG (OLG Koblenz OLGSt 109); mit § 29 BtMG (Anh. 4); mit § 5 HeilprG (BGHSt 8, 237), mit § 98 BVFG (BGHSt 9, 30), §§ 148, 148a GewO (NStZ 1992, 595), § 119 WpHG.  239 I. Sonstige Vorschriften. FAufs...
- **[Judge=2]** `StGB_Kommentar_part42.md` — Behandelt § 263a Varianten, aber nicht direkte Abgrenzung zu § 263
  > infolge des Unterlassens (zB pflichtwidriges Nichtingangsetzen) überhaupt nicht zu einem DV-Vorgang kommt.  9 III. Var. 3: Unbefugtes Verwenden von Daten. Die 3. Var. setzt in Abgrenzung zur 2. Var. d...
- **[Judge=3]** `StGB_Kommentar_part42.md` — Direkte Abgrenzung Betrug/Computerbetrug bei Unbefugtheitsauslegung
  > deren Erfassung die 3. Var. aufgenommen wurde (RegE 30); bei Verwendung „richtiger“ Daten verbliebe für die Alternative ein Anwendungsbereich nur in Versuchsfällen.  b) hM. Nach stRspr und hM ist das ...