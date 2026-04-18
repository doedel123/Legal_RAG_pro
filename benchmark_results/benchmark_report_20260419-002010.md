# RAG Benchmark Report

_Generiert: 2026-04-19T00:20:10_


- Queries: **18**
- Top-K: **5**
- Systeme: ours-mxbai, ours-mxbai-voyage

## Gesamtvergleich

| Metrik | ours-mxbai | ours-mxbai-voyage |
|--------|--------|--------|
| nDCG@10 | 0.948 | 0.924 |
| Relevance@10 | 90.0% | 78.9% |
| Relevance@3 | 92.6% | 85.2% |
| Top-1-Score | 2.56 | 2.28 |
| Mean-Score | 2.53 | 2.29 |
| Latenz (s) | 5.63 | 5.60 |

## Nach Kategorie


### alltagssprache

| Metrik | ours-mxbai | ours-mxbai-voyage |
|--------|--------|--------|
| nDCG@10 | 0.990 | 0.927 |
| Relevance@10 | 100.0% | 95.0% |
| Relevance@3 | 100.0% | 91.7% |

### cross-reference

| Metrik | ours-mxbai | ours-mxbai-voyage |
|--------|--------|--------|
| nDCG@10 | 0.813 | 0.801 |
| Relevance@10 | 66.7% | 46.7% |
| Relevance@3 | 66.7% | 66.7% |

### exakte-paragraphen

| Metrik | ours-mxbai | ours-mxbai-voyage |
|--------|--------|--------|
| nDCG@10 | 0.989 | 0.991 |
| Relevance@10 | 100.0% | 95.0% |
| Relevance@3 | 100.0% | 100.0% |

### konzept

| Metrik | ours-mxbai | ours-mxbai-voyage |
|--------|--------|--------|
| nDCG@10 | 0.950 | 0.953 |
| Relevance@10 | 85.0% | 80.0% |
| Relevance@3 | 91.7% | 91.7% |

### stpo-prozess

| Metrik | ours-mxbai | ours-mxbai-voyage |
|--------|--------|--------|
| nDCG@10 | 0.969 | 0.912 |
| Relevance@10 | 93.3% | 66.7% |
| Relevance@3 | 100.0% | 66.7% |

## Detail pro Query


### q01 — exakte-paragraphen

**Query:** Welche Voraussetzungen hat der gewerbsmaessige Bandenbetrug nach § 263 Abs. 5 StGB?

**Kontext:** Qualifikationstatbestand des Bandenbetrugs im Fischer-Kommentar

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours-mxbai | 1.00 | 100% | 100% | 3 | 7.1s |
| ours-mxbai-voyage | 0.99 | 100% | 100% | 3 | 6.2s |

#### ours-mxbai — Top 3
- **[Judge=3]** `§ 263 StGB – I. Vermögensbegriff  – Rn. 263` — Enthält direkt § 263 Abs. 5 StGB mit allen Voraussetzungen
  > 263 (1) Wer in der Absicht, sich oder einem Dritten einen rechtswidrigen Vermögensvorteil zu verschaffen, das Vermögen eines anderen dadurch beschädigt, daß er durch Vorspiegelung falscher oder durch ...
- **[Judge=3]** `§ 263 StGB – BT. Zweijundzwanzigster Abschnitt – Rn. 213` — Behandelt direkt Abs. 5 Qualifikation und Bandenbetrug
  > 213 Sind beide Varianten erfüllt, ist eine Qualifikation nach Abs. 5 gegeben. Die Abgrenzung des Abs. 3 Nr. 1 zum Verbrechen nach Abs. 5 ist in Fällen bandenmäßiger Begehung schwierig, denn eine auf f...
- **[Judge=3]** `§ 263 StGB – BT. Zweriindzwanzigster Abschnitt – Rn. 225` — Beantwortet direkt Voraussetzungen des § 263 Abs. 5 StGB
  > IV. Qualifikation (Abs. 5). Abs. 5 enthält einen Qualifikationstatbestand, der die Tat in Fällen kumulativ gewerbs- und bandenmäßiger Begehung zum Verbrechen macht. Die Qualifikation ist in die Urteil...

#### ours-mxbai-voyage — Top 3
- **[Judge=3]** `§ 263 StGB – I. Vermögensbegriff  – Rn. 263` — Enthält § 263 Abs. 5 mit allen Tatbestandsmerkmalen
  > 263 (1) Wer in der Absicht, sich oder einem Dritten einen rechtswidrigen Vermögensvorteil zu verschaffen, das Vermögen eines anderen dadurch beschädigt, daß er durch Vorspiegelung falscher oder durch ...
- **[Judge=3]** `§ 263 StGB – BT. Zweijundzwanzigster Abschnitt – Rn. 213` — Direkt relevant: Behandelt Qualifikationstatbestand § 263 Abs. 5
  > 213 Sind beide Varianten erfüllt, ist eine Qualifikation nach Abs. 5 gegeben. Die Abgrenzung des Abs. 3 Nr. 1 zum Verbrechen nach Abs. 5 ist in Fällen bandenmäßiger Begehung schwierig, denn eine auf f...
- **[Judge=2]** `§ 263 StGB – I. Sonstige Vorschriften 239 – Rn. 263 (Teil 1)` — Inhaltsverzeichnis behandelt § 263 Abs. 5, aber keine konkreten Voraussetzungen
  > 3. Einzelne Fallgruppen ... 92 4. Rechtlich missbilligte, sittenwidrige und gesetzeswidrige wirtschaftliche Werte ... 101 VI. Schaden ... 110 1. Grundsätze der Schadensermittlung ... 111 2. Vermögensm...

### q02 — exakte-paragraphen

**Query:** Was regelt § 112 StPO zur Untersuchungshaft?

**Kontext:** Anordnungsvoraussetzungen der U-Haft (dringender Tatverdacht, Haftgrund) im Schmitt/Koehler

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours-mxbai | 0.99 | 100% | 100% | 3 | 4.6s |
| ours-mxbai-voyage | 1.00 | 100% | 100% | 3 | 5.1s |

#### ours-mxbai — Top 3
- **[Judge=3]** `§ 112 StPO – Rn. 112` — Vollständiger Gesetzestext zu Untersuchungshaft-Anordnungsvoraussetzungen
  > 112 (1) ¹ Die Untersuchungshaft darf gegen den Beschuldigten angeordnet werden, wenn er der Tat dringend verdächtig ist und ein Haftgrund besteht. ² Sie darf nicht angeordnet werden, wenn sie zu der B...
- **[Judge=3]** `§ 112 StPO – Rn. 112` — Erklärt direkt die Haftbefehlsvoraussetzungen nach § 112 StPO
  > Haftunfähigkeit des Beschuldigten schließt den Erlass des Haftbefehls nicht aus, sondern hindert nur seinen Vollzug (OLG Düsseldorf JZ 1984, 248; OLG Frankfurt a.M. NJW 1968, 2302; OLG Nürnberg OLGSt ...
- **[Judge=3]** `§ 112 StPO – III. Flucht (Abs – Rn. 23` — Direkt relevant: behandelt Haftgruende nach § 112 StPO
  > Bei einer besonders hohen Straferwartung braucht daher nur geprüft zu werden, ob Umstände vorhanden sind, die die hieraus herzuleitende Fluchtgefahr ausräumen können (KG StV 1996, 383; OLG München Str...

#### ours-mxbai-voyage — Top 3
- **[Judge=3]** `§ 112 StPO – Rn. 112` — Direkt relevant: § 112 StPO Anordnungsvoraussetzungen U-Haft
  > 112 (1) ¹ Die Untersuchungshaft darf gegen den Beschuldigten angeordnet werden, wenn er der Tat dringend verdächtig ist und ein Haftgrund besteht. ² Sie darf nicht angeordnet werden, wenn sie zu der B...
- **[Judge=3]** `§ 112 StPO – III. Flucht (Abs – Rn. 17` — Direkt relevant zu Haftgrund Fluchtgefahr § 112 StPO
  > Die Beurteilung der Fluchtgefahr erfordert die Berücksichtigung aller Umstände des Falles, insbes. der Art der dem Beschuldigten vorgeworfenen Tat, der Persönlichkeit des Beschuldigten, seiner Lebensv...
- **[Judge=3]** `§ 112 StPO – III. Flucht (Abs – Rn. 23` — Direkt relevant: Behandelt Haftgruende nach § 112 StPO
  > Bei einer besonders hohen Straferwartung braucht daher nur geprüft zu werden, ob Umstände vorhanden sind, die die hieraus herzuleitende Fluchtgefahr ausräumen können (KG StV 1996, 383; OLG München Str...

### q03 — exakte-paragraphen

**Query:** Welche Haftgruende nennt § 112 Abs. 2 StPO?

**Kontext:** Fluchtgefahr, Verdunkelungsgefahr, Flucht — im StPO-Kommentar

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours-mxbai | 0.99 | 100% | 100% | 3 | 5.9s |
| ours-mxbai-voyage | 0.99 | 100% | 100% | 3 | 5.8s |

#### ours-mxbai — Top 3
- **[Judge=3]** `§ 112 StPO – Rn. 112` — Vollständige Auflistung aller Haftgründe nach § 112 Abs. 2 StPO
  > 112 (1) ¹ Die Untersuchungshaft darf gegen den Beschuldigten angeordnet werden, wenn er der Tat dringend verdächtig ist und ein Haftgrund besteht. ² Sie darf nicht angeordnet werden, wenn sie zu der B...
- **[Judge=3]** `§ 112 StPO – III. Flucht (Abs – Rn. 23` — Erklärt direkt Haftgründe aus § 112 Abs. 2 StPO
  > Bei einer besonders hohen Straferwartung braucht daher nur geprüft zu werden, ob Umstände vorhanden sind, die die hieraus herzuleitende Fluchtgefahr ausräumen können (KG StV 1996, 383; OLG München Str...
- **[Judge=2]** `§ 112 StPO – III. Flucht (Abs – Rn. 32 (Teil 2)` — Behandelt Verdunkelungsgefahr als einen der drei Haftgruende
  > Wenn die Verdunkelungshandlungen nicht geeignet sind, die Ermittlung der Wahrheit zu erschweren, darf UHaft nicht angeordnet werden. Der Haftgrund liegt daher nicht vor, wenn der Sachverhalt schon in ...

#### ours-mxbai-voyage — Top 3
- **[Judge=3]** `§ 112 StPO – Rn. 112` — Listet direkt alle Haftgründe des § 112 Abs. 2 StPO
  > 112 (1) ¹ Die Untersuchungshaft darf gegen den Beschuldigten angeordnet werden, wenn er der Tat dringend verdächtig ist und ein Haftgrund besteht. ² Sie darf nicht angeordnet werden, wenn sie zu der B...
- **[Judge=3]** `§ 112 StPO – III. Flucht (Abs – Rn. 23` — Behandelt direkt Haftgruende nach § 112 Abs. 2 StPO
  > Bei einer besonders hohen Straferwartung braucht daher nur geprüft zu werden, ob Umstände vorhanden sind, die die hieraus herzuleitende Fluchtgefahr ausräumen können (KG StV 1996, 383; OLG München Str...
- **[Judge=2]** `§ 112 StPO – III. Flucht (Abs – Rn. 32 (Teil 2)` — Behandelt Verdunkelungsgefahr, aber nicht die anderen Haftgruende
  > Wenn die Verdunkelungshandlungen nicht geeignet sind, die Ermittlung der Wahrheit zu erschweren, darf UHaft nicht angeordnet werden. Der Haftgrund liegt daher nicht vor, wenn der Sachverhalt schon in ...

### q04 — exakte-paragraphen

**Query:** Was regelt § 102 StPO zur Durchsuchung beim Beschuldigten?

**Kontext:** Durchsuchungsvoraussetzungen beim Verdaechtigen

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours-mxbai | 0.97 | 100% | 100% | 3 | 5.0s |
| ours-mxbai-voyage | 0.99 | 80% | 100% | 3 | 4.5s |

#### ours-mxbai — Top 3
- **[Judge=3]** `§ 102 StPO – Rn. 102` — Direkt relevant: erklärt § 102 StPO Durchsuchungsvoraussetzungen
  > 102 Bei dem, welcher als Täter oder Teilnehmer einer Straftat oder der Datenhehlerei, Begünstigung, Strafvereitelung oder Hehlerei  Köhler    Ermittlungsmaßnahmen  verdächtig ist, kann eine Durchsuchu...
- **[Judge=2]** `§ 102 StPO – Rn. 10` — Behandelt Durchsuchungsvoraussetzungen, aber nicht spezifisch § 102
  > II. Auffinden von Beweismitteln. Zu den Beweismitteln (→ § 94 Rn. 4 ff.) gehören auch die nur in § 103 erwähnten Spuren (SK-StPO/Jäger/Wohlers Rn. 21) u. Personen, die zu Beweiszwecken in Augenschein ...
- **[Judge=3]** `§ 102 StPO – Rn. 3` — Erklärt direkt Durchsuchungsgegenstände nach § 102 StPO
  > **Teilnehmer** nach §§ 25 ff. StGB, nicht die sog. notwendigen Teilnehmer (zum Begriff: Fischer/Fischer StGB Vor § 25 Rn. 7), stehen den Tatverdächtigen gleich. Bei jedem v. ihnen sowie bei den der Be...

#### ours-mxbai-voyage — Top 3
- **[Judge=3]** `§ 102 StPO – Rn. 102` — Direkter Gesetzestext und umfassende Erläuterung zu § 102 StPO
  > 102 Bei dem, welcher als Täter oder Teilnehmer einer Straftat oder der Datenhehlerei, Begünstigung, Strafvereitelung oder Hehlerei  Köhler    Ermittlungsmaßnahmen  verdächtig ist, kann eine Durchsuchu...
- **[Judge=3]** `§ 102 StPO – Rn. 3` — Direkter § 102 StPO Bezug zu Durchsuchungsgegenstaenden
  > **Teilnehmer** nach §§ 25 ff. StGB, nicht die sog. notwendigen Teilnehmer (zum Begriff: Fischer/Fischer StGB Vor § 25 Rn. 7), stehen den Tatverdächtigen gleich. Bei jedem v. ihnen sowie bei den der Be...
- **[Judge=2]** `§ 102 StPO – Rn. 102` — Behandelt Durchsuchungsvoraussetzungen, aber fokussiert auf Tatverdacht allgemein
  > Köhler     Erstes Buch. Achter Abschnitt  Gesetz gebundenen Behörden u. Gremien ist nicht angezeigt (BGH JR 2019, 404 mAnm Löffelmann). Bei anonymen Hinweisen ist wegen der erhöhten Gefahr u. des nur ...

### q05 — konzept

**Query:** Wann liegt eine konkludente Taeuschung im Sinne des § 263 StGB vor?

**Kontext:** Taeuschungshandlung durch schluessiges Verhalten

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours-mxbai | 0.85 | 80% | 67% | 1 | 5.6s |
| ours-mxbai-voyage | 0.93 | 60% | 67% | 2 | 5.7s |

#### ours-mxbai — Top 3
- **[Judge=1]** `§ 263 StGB – I. Vermögensbegriff  – Rn. 263` — Gesetzestext ohne konkludente Taeuschung Details
  > 263 (1) Wer in der Absicht, sich oder einem Dritten einen rechtswidrigen Vermögensvorteil zu verschaffen, das Vermögen eines anderen dadurch beschädigt, daß er durch Vorspiegelung falscher oder durch ...
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 14` — Behandelt konkludente Täuschungshandlungen bei § 263 StGB
  > 14 II. Tathandlung. Der Begriff „Täuschen“ ist im Wortlaut des Abs. 1 nicht verwendet; er ergibt sich aus dem Zusammenhang zwischen der Beschreibung der Tathandlung (→ Rn. 18) und dem Irrtum als ihrem...
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 14` — Behandelt direkt konkludente Täuschung bei § 263 StGB
  > Rspr. und hM bejahen darüber hinaus aber die Möglichkeit einer Täuschung durch Unterlassen auch ohne Erklärung gegenüber dem Irrenden (→ Rn. 38; vgl. BGHSt 39, 392 (398); BayObLG NJW 1987, 1654 (mAnm ...

#### ours-mxbai-voyage — Top 3
- **[Judge=2]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 263 (Tei` — Literaturverzeichnis zu Betrug, enthält relevante Quellen zu konkludenter Täuschung
  > Heghmanns, Strafbarkeit des „Phishing“ von Bankkontendaten und ihrer Verwertung, wistra 2007, 167; Hilgendorf, Tatsachenaussagen u. Werturteile im Strafrecht, 1998; Hillenkamp, Zum Schutz „deliktische...
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 21` — Beantwortet direkt konkludente Täuschung § 263 StGB
  > 21 2. Konkludente Erklärungen. Auch durch eine schlüssige Handlung (konkludente Erklärung) kann vorspiegelt werden. Eine solche konkludente Erklärung durch aktives Tun ist von einer Erklärung durch Un...
- **[Judge=1]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 38` — Behandelt Täuschung durch Unterlassen, nicht konkludente Täuschung
  > 38 4. Täuschung durch Unterlassen. Eine Täuschung kann nach hM (aA Grünwald FS H. Mayer, 1966, 281; Kargl ZStW 119 (2007), 250 (287) mwN) auch durch Unterlassen begangen werden, wenn eine Garantenpfli...

### q06 — konzept

**Query:** Was ist eine Vermoegensverfuegung und welche Anforderungen stellt die Rechtsprechung?

**Kontext:** Tatbestandsmerkmal der Vermoegensverfuegung beim Betrug

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours-mxbai | 0.97 | 80% | 100% | 3 | 5.6s |
| ours-mxbai-voyage | 0.92 | 80% | 100% | 2 | 5.0s |

#### ours-mxbai — Top 3
- **[Judge=3]** `§ 263 StGB – BT. Zweitundzwanzigster Abschnitt – Rn. 69` — Direkt relevant: definiert Vermoegensverfuegung und Anforderungen
  > 69 Anders ist es, wenn der Verfügende seinerseits nur (gutgläubige) Hilfsperson eines bösgläubigen Dritten ist. Hier ist auf den Irrtum des Entscheidungsbefugten abzustellen: Erkennt dieser die Unrich...
- **[Judge=2]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 87` — Thematisch relevant: Kausalität und Vermögensschaden beim Betrug
  > 87 5. Kausalität. Für die Vermögensverfügung muss der täuschungsbedingte Irrtum kausal sein (vgl. BGHSt 24, 257 (260); 24, 386 (389); NStZ 2003, 313 (314 f.); OLG Düsseldorf NJW 1987, 3145); Mitverurs...
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 76` — Definiert Unmittelbarkeit bei Vermoegensverfuegung direkt
  > 76 3. Unmittelbarkeit der Verfügung. Neben der Freiwilligkeit ist das Merkmal der Unmittelbarkeit nach stRspr und hM das wichtigste Kriterium zur Beschränkung der § 263 unterfallenden Selbstschädigung...

#### ours-mxbai-voyage — Top 3
- **[Judge=2]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 87` — Behandelt Kausalität bei Vermögensverfügung, nicht Definition
  > 87 5. Kausalität. Für die Vermögensverfügung muss der täuschungsbedingte Irrtum kausal sein (vgl. BGHSt 24, 257 (260); 24, 386 (389); NStZ 2003, 313 (314 f.); OLG Düsseldorf NJW 1987, 3145); Mitverurs...
- **[Judge=3]** `§ 263 StGB – BT. Zweitundzwanzigster Abschnitt – Rn. 69` — Definiert Vermoegensverfuegung und zentrale Rechtsprechungsanforderungen
  > 69 Anders ist es, wenn der Verfügende seinerseits nur (gutgläubige) Hilfsperson eines bösgläubigen Dritten ist. Hier ist auf den Irrtum des Entscheidungsbefugten abzustellen: Erkennt dieser die Unrich...
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 76` — Behandelt direkt Vermoegensverfuegung beim Dreiecksbetrug und Zurechnung
  > 4. Dreiecksbetrug. Da die Getäuschte und die verfügende, nicht aber die verfügende und die geschädigte Person identisch sein müssen, ist der Tatbestand des § 263 nur erfüllt, wenn die Vermögensverfügu...

### q07 — konzept

**Query:** Was versteht man unter einem Gefaehrdungsschaden beim Betrug?

**Kontext:** Schadensbegriff, schadensgleiche Vermoegensgefaehrdung

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours-mxbai | 1.00 | 100% | 100% | 3 | 5.6s |
| ours-mxbai-voyage | 0.97 | 100% | 100% | 3 | 5.1s |

#### ours-mxbai — Top 3
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 159` — Direkte Definition und Voraussetzungen des Gefährdungsschadens beim Betrug
  > 159 b) Voraussetzungen. aa) Ein Gefährdungsschaden ist gegeben, wenn die Wahrscheinlichkeit des endgültigen Verlusts eines Vermögensbestandteils zum Zeitpunkt der täuschungsbedingten Verfügung so groß...
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 171` — Definiert direkt Gefaehrdungsschaden beim Betrug mit Beispielen
  > Die täuschungsbedingte Herausgabe von EC-Karten, Kreditkarten und weiteren Zugangsdaten zu Bank-Guthaben (PINs, TANs; Passwörter), sei es infolge persönlicher Täuschung oder von „Phishing“-Manipulatio...
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 109` — Behandelt direkt Gefährdungsschaden beim Betrug
  > VI. Schaden. Vermögensschaden ist ein negativer Saldo zwischen dem Wert des Vermögens vor und nach der irrtumsbedingten Vermögensverfügung des Getäuschten (Prinzip der Gesamtsaldierung; stRspr; vgl. B...

#### ours-mxbai-voyage — Top 3
- **[Judge=3]** `§ 263 StGB – BT. Zwei undzwanzigster Abschnitt – Rn. 263 (Te` — Direkt relevante Literaturuebersicht zum Gefaehrdungsschaden beim Betrug
  > Fischer/Lutz    Betrug und Untreue   rechts für das Strafrecht, FS Weber, 2004, 271; Eisele/Bechtel, Der Schadensbegriff bei den Vermögensdelikten, JuS 2018, 97; Ellbogen/Wichmann, Zu Problemen des är...
- **[Judge=2]** `§ 263 StGB – BT. Zwei undzwanzigster Abschnitt – Rn. 263 (Te` — Literaturverzeichnis zu Vermögensgefährdung und Schadensbegriff
  > Li, Der „wirtschaftliche“ Vermögensbegriff in der höchstrichterlichen Rechtsprechung, NZWiSt 2019, 405; Lin, Verteilung des tauschungsbedingten Irrtumsrisikos und Wertbilanzierung der gesamten Vermöge...
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 164` — Direkt relevant: definiert Gefaehrdungsschaden beim Betrug
  > 164 Es lassen sich im Übrigen Fallgruppen wie folgt unterscheiden:  aa) Der Abschluss eines unter Vorspiegelung von Leistungsfähigkeit und/oder Leistungswilligkeit erschlichenen Kaufvertrags kann eine...

### q08 — konzept

**Query:** Wie wird der Vorsatz beim Betrug bestimmt, insbesondere die Bereicherungsabsicht?

**Kontext:** Subjektiver Tatbestand § 263 StGB

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours-mxbai | 0.98 | 80% | 100% | 3 | 5.9s |
| ours-mxbai-voyage | 0.99 | 80% | 100% | 3 | 5.2s |

#### ours-mxbai — Top 3
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 176` — Direkt relevant: behandelt Vorsatz und Bereicherungsabsicht § 263
  > D. Subjektiver Tatbestand. § 263 setzt Vorsatz voraus; darüber hinaus ist die Absicht rechtswidriger Bereicherung erforderlich.   I. Vorsatz. 1. Täuschungsvorsatz. Der Vorsatz (bedingter Vorsatz genüg...
- **[Judge=3]** `§ 263 StGB – I. Sonstige Vorschriften 239 – Rn. 263 (Teil 1)` — Behandelt direkt Bereicherungsabsicht beim Betrug
  > 3. Einzelne Fallgruppen ... 92 4. Rechtlich missbilligte, sittenwidrige und gesetzeswidrige wirtschaftliche Werte ... 101 VI. Schaden ... 110 1. Grundsätze der Schadensermittlung ... 111 2. Vermögensm...
- **[Judge=2]** `§ 263 StGB – I. Vermögensbegriff  – Rn. 263` — Enthält Bereicherungsabsicht, aber ohne subjektive Tatbestandsdetails
  > 263 (1) Wer in der Absicht, sich oder einem Dritten einen rechtswidrigen Vermögensvorteil zu verschaffen, das Vermögen eines anderen dadurch beschädigt, daß er durch Vorspiegelung falscher oder durch ...

#### ours-mxbai-voyage — Top 3
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 176` — Direkt relevant: behandelt Vorsatz und Bereicherungsabsicht bei Betrug
  > D. Subjektiver Tatbestand. § 263 setzt Vorsatz voraus; darüber hinaus ist die Absicht rechtswidriger Bereicherung erforderlich.   I. Vorsatz. 1. Täuschungsvorsatz. Der Vorsatz (bedingter Vorsatz genüg...
- **[Judge=3]** `§ 263 StGB – I. Sonstige Vorschriften 239 – Rn. 263 (Teil 1)` — Direkt relevant: behandelt Bereicherungsabsicht beim Betrug
  > 3. Einzelne Fallgruppen ... 92 4. Rechtlich missbilligte, sittenwidrige und gesetzeswidrige wirtschaftliche Werte ... 101 VI. Schaden ... 110 1. Grundsätze der Schadensermittlung ... 111 2. Vermögensm...
- **[Judge=2]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 187 (Tei` — Stoffgleichheit relevant, aber nicht Vorsatz/Bereicherungsabsicht
  > 187 1. Stoffgleichheit. Der Vorteil muss die Kehrseite des Schadens und ihm „stoffgleich“ sein; er muss unmittelbare Folge der täuschungsbedingten Verfügung sein, welche den Schaden des Opfers herbeif...

### q09 — alltagssprache

**Query:** Hat der Angeklagte die Kunden über das Internet betrogen?

**Kontext:** Abstrakte Frage zu Internetbetrug, sucht Taeuschungshandlung + Schaden

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours-mxbai | 0.99 | 100% | 100% | 3 | 5.2s |
| ours-mxbai-voyage | 0.92 | 100% | 100% | 2 | 4.7s |

#### ours-mxbai — Top 3
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 109` — Direkt relevant für Betrugsschaden bei Internetbetrug
  > VI. Schaden. Vermögensschaden ist ein negativer Saldo zwischen dem Wert des Vermögens vor und nach der irrtumsbedingten Vermögensverfügung des Getäuschten (Prinzip der Gesamtsaldierung; stRspr; vgl. B...
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 5` — Definiert zentrale Betrugsmerkmale: Taeuschung, Irrtum, Schaden
  > 5 C. Grundtatbestand, Abs. 1. Tathandlung ist das Täuschen einer natürlichen Person (vgl. NStZ 2005, 213) über Tatsachen. Erfolg dieser Handlung muss ein Irrtum des Täuschungsadressaten sein; dieser m...
- **[Judge=2]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 263 (Tei` — Literaturverzeichnis zu Betrug, thematisch relevant aber oberflächlich
  > Heghmanns, Strafbarkeit des „Phishing“ von Bankkontendaten und ihrer Verwertung, wistra 2007, 167; Hilgendorf, Tatsachenaussagen u. Werturteile im Strafrecht, 1998; Hillenkamp, Zum Schutz „deliktische...

#### ours-mxbai-voyage — Top 3
- **[Judge=2]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 263 (Tei` — Thematisch relevant: Betrug, Phishing, Internet-Kontext behandelt
  > Heghmanns, Strafbarkeit des „Phishing“ von Bankkontendaten und ihrer Verwertung, wistra 2007, 167; Hilgendorf, Tatsachenaussagen u. Werturteile im Strafrecht, 1998; Hillenkamp, Zum Schutz „deliktische...
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 87` — Direkt relevant zu Betrug, behandelt Kausalität und Vermögensschaden
  > 87 5. Kausalität. Für die Vermögensverfügung muss der täuschungsbedingte Irrtum kausal sein (vgl. BGHSt 24, 257 (260); 24, 386 (389); NStZ 2003, 313 (314 f.); OLG Düsseldorf NJW 1987, 3145); Mitverurs...
- **[Judge=2]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 263 (Tei` — Betrugskommentar mit thematischem Bezug, aber keine Internetspezifika
  > Fischer/Lutz    Betrug und Untreue   schende Warnung": Eine Drohung?, FS Puppe, 2011, 1217; Kupper, Mengenbegriffe im Strafgesetzbuch, FS Kohlmann, 2003, 133; Lampe, Personales Unrecht im Betrug, FS O...

### q10 — alltagssprache

**Query:** Wann darf die Polizei bei jemandem zu Hause suchen?

**Kontext:** Durchsuchungsvoraussetzungen, §§ 102 ff. StPO

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours-mxbai | 0.97 | 100% | 100% | 3 | 5.6s |
| ours-mxbai-voyage | 0.97 | 100% | 100% | 3 | 5.4s |

#### ours-mxbai — Top 3
- **[Judge=3]** `§ 102 StPO – Rn. 102` — Behandelt direkt Durchsuchungsvoraussetzungen gem. § 102 StPO
  > 102 Bei dem, welcher als Täter oder Teilnehmer einer Straftat oder der Datenhehlerei, Begünstigung, Strafvereitelung oder Hehlerei  Köhler    Ermittlungsmaßnahmen  verdächtig ist, kann eine Durchsuchu...
- **[Judge=2]** `§ 102 StPO – Rn. 10` — Thematisch relevant: Durchsuchungsvoraussetzungen und -zwecke behandelt
  > II. Auffinden von Beweismitteln. Zu den Beweismitteln (→ § 94 Rn. 4 ff.) gehören auch die nur in § 103 erwähnten Spuren (SK-StPO/Jäger/Wohlers Rn. 21) u. Personen, die zu Beweiszwecken in Augenschein ...
- **[Judge=2]** `§ 102 StPO – Rn. 3` — Behandelt Durchsuchung von Wohnungen, aber spezielle Aspekte
  > **Teilnehmer** nach §§ 25 ff. StGB, nicht die sog. notwendigen Teilnehmer (zum Begriff: Fischer/Fischer StGB Vor § 25 Rn. 7), stehen den Tatverdächtigen gleich. Bei jedem v. ihnen sowie bei den der Be...

#### ours-mxbai-voyage — Top 3
- **[Judge=3]** `§ 102 StPO – Rn. 102` — Direkt relevant: Beantwortet zentrale Durchsuchungsvoraussetzungen bei Verdächtigen
  > 102 Bei dem, welcher als Täter oder Teilnehmer einer Straftat oder der Datenhehlerei, Begünstigung, Strafvereitelung oder Hehlerei  Köhler    Ermittlungsmaßnahmen  verdächtig ist, kann eine Durchsuchu...
- **[Judge=2]** `§ 102 StPO – Rn. 3` — Behandelt Durchsuchungsvoraussetzungen, aber spezielle Aspekte
  > **Teilnehmer** nach §§ 25 ff. StGB, nicht die sog. notwendigen Teilnehmer (zum Begriff: Fischer/Fischer StGB Vor § 25 Rn. 7), stehen den Tatverdächtigen gleich. Bei jedem v. ihnen sowie bei den der Be...
- **[Judge=3]** `§ 102 StPO – Rn. 10` — Direkt relevant - behandelt Durchsuchungsvoraussetzungen nach StPO
  > II. Auffinden von Beweismitteln. Zu den Beweismitteln (→ § 94 Rn. 4 ff.) gehören auch die nur in § 103 erwähnten Spuren (SK-StPO/Jäger/Wohlers Rn. 21) u. Personen, die zu Beweiszwecken in Augenschein ...

### q11 — alltagssprache

**Query:** Was passiert wenn jemand luegt damit er Geld bekommt?

**Kontext:** Laienhafte Umschreibung des Betrugstatbestandes

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours-mxbai | 1.00 | 100% | 100% | 3 | 5.2s |
| ours-mxbai-voyage | 0.81 | 80% | 67% | 1 | 9.2s |

#### ours-mxbai — Top 3
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 5` — Definiert exakt den Betrugstatbestand mit Täuschung
  > 5 C. Grundtatbestand, Abs. 1. Tathandlung ist das Täuschen einer natürlichen Person (vgl. NStZ 2005, 213) über Tatsachen. Erfolg dieser Handlung muss ein Irrtum des Täuschungsadressaten sein; dieser m...
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 176` — Direkt relevant für Betrug durch Täuschung zwecks Bereicherung
  > D. Subjektiver Tatbestand. § 263 setzt Vorsatz voraus; darüber hinaus ist die Absicht rechtswidriger Bereicherung erforderlich.   I. Vorsatz. 1. Täuschungsvorsatz. Der Vorsatz (bedingter Vorsatz genüg...
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 186` — Erklärt Bereicherungsabsicht als zentrales Betrugsmerkmal
  > 186 II. Bereicherungsabsicht. Die Tat muss subjektiv auf die Erlangung eines rechtswidrigen Vermögensvorteils für den Täuschenden oder einen Dritten gerichtet sein. Vermögensvorteil ist die Erhöhung d...

#### ours-mxbai-voyage — Top 3
- **[Judge=1]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 263 (Tei` — Literaturverzeichnis zu Betrug, keine Tatbestandsmerkmale erklärt
  > Heghmanns, Strafbarkeit des „Phishing“ von Bankkontendaten und ihrer Verwertung, wistra 2007, 167; Hilgendorf, Tatsachenaussagen u. Werturteile im Strafrecht, 1998; Hillenkamp, Zum Schutz „deliktische...
- **[Judge=2]** `§ 263 StGB – BT. Zweundzwanzigster Abschnitt – Rn. 153` — Behandelt Betrug durch Täuschung, spezifisch Vermögensschäden
  > 153 Nach hM kann ein Vermögensschaden aber auch durch Täuschung über charakterliche Mängel eintreten. Aus persönlicher Ungeeignetheit ergibt sich bei Beamten, da das Beamtenverhältnis seinen Schwerpun...
- **[Judge=3]** `§ 263 StGB – I. Vermögensbegriff  – Rn. 263` — Direkte Antwort auf Betrugstatbestand mit lügen für Geld
  > 263 (1) Wer in der Absicht, sich oder einem Dritten einen rechtswidrigen Vermögensvorteil zu verschaffen, das Vermögen eines anderen dadurch beschädigt, daß er durch Vorspiegelung falscher oder durch ...

### q12 — alltagssprache

**Query:** Wann muss jemand ins Gefaengnis waehrend die Tat noch nicht bewiesen ist?

**Kontext:** Untersuchungshaft, §§ 112 ff. StPO

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours-mxbai | 1.00 | 100% | 100% | 3 | 5.6s |
| ours-mxbai-voyage | 1.00 | 100% | 100% | 3 | 5.2s |

#### ours-mxbai — Top 3
- **[Judge=3]** `§ 112 StPO – Rn. 112` — Beantwortet direkt die Frage zur Untersuchungshaft
  > 112 (1) ¹ Die Untersuchungshaft darf gegen den Beschuldigten angeordnet werden, wenn er der Tat dringend verdächtig ist und ein Haftgrund besteht. ² Sie darf nicht angeordnet werden, wenn sie zu der B...
- **[Judge=3]** `§ 112 StPO – III. Flucht (Abs – Rn. 23` — Direkt relevant: Haftgruende Flucht- und Verdunkelungsgefahr
  > Bei einer besonders hohen Straferwartung braucht daher nur geprüft zu werden, ob Umstände vorhanden sind, die die hieraus herzuleitende Fluchtgefahr ausräumen können (KG StV 1996, 383; OLG München Str...
- **[Judge=3]** `§ 112 StPO – III. Flucht (Abs – Rn. 32 (Teil 2)` — Behandelt direkt Verdunkelungsgefahr als Haftgrund der Untersuchungshaft
  > Wenn die Verdunkelungshandlungen nicht geeignet sind, die Ermittlung der Wahrheit zu erschweren, darf UHaft nicht angeordnet werden. Der Haftgrund liegt daher nicht vor, wenn der Sachverhalt schon in ...

#### ours-mxbai-voyage — Top 3
- **[Judge=3]** `§ 112 StPO – Rn. 112` — Direkt relevant - zentrale Norm fuer Untersuchungshaft
  > 112 (1) ¹ Die Untersuchungshaft darf gegen den Beschuldigten angeordnet werden, wenn er der Tat dringend verdächtig ist und ein Haftgrund besteht. ² Sie darf nicht angeordnet werden, wenn sie zu der B...
- **[Judge=3]** `§ 112 StPO – Rn. 112` — Definiert dringenden Tatverdacht für Untersuchungshaft
  > Haftunfähigkeit des Beschuldigten schließt den Erlass des Haftbefehls nicht aus, sondern hindert nur seinen Vollzug (OLG Düsseldorf JZ 1984, 248; OLG Frankfurt a.M. NJW 1968, 2302; OLG Nürnberg OLGSt ...
- **[Judge=3]** `§ 112 StPO – III. Flucht (Abs – Rn. 32 (Teil 2)` — Direkt relevant: Verdunkelungsgefahr als Haftgrund bei Untersuchungshaft
  > Wenn die Verdunkelungshandlungen nicht geeignet sind, die Ermittlung der Wahrheit zu erschweren, darf UHaft nicht angeordnet werden. Der Haftgrund liegt daher nicht vor, wenn der Sachverhalt schon in ...

### q13 — stpo-prozess

**Query:** Welche Voraussetzungen hat die Untersuchungshaft wegen Fluchtgefahr?

**Kontext:** § 112 Abs. 2 Nr. 2 StPO Fluchtgefahr

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours-mxbai | 1.00 | 80% | 100% | 3 | 5.4s |
| ours-mxbai-voyage | 0.89 | 60% | 33% | 3 | 5.7s |

#### ours-mxbai — Top 3
- **[Judge=3]** `§ 112 StPO – Rn. 112` — Definiert exakt Fluchtgefahr-Voraussetzungen nach § 112 Abs. 2 Nr. 2
  > 112 (1) ¹ Die Untersuchungshaft darf gegen den Beschuldigten angeordnet werden, wenn er der Tat dringend verdächtig ist und ein Haftgrund besteht. ² Sie darf nicht angeordnet werden, wenn sie zu der B...
- **[Judge=3]** `§ 112 StPO – III. Flucht (Abs – Rn. 17 (Teil 1)` — Direkt relevant - definiert Fluchtgefahr-Voraussetzungen
  > 17 IV. Fluchtgefahr (Abs. 2 Nr. 2). Fluchtgefahr (Abs. 2 Nr. 2) besteht, wenn die Würdigung der Umstände des Falles es wahrscheinlicher macht, dass sich der Beschuldigte dem Strafverfahren entziehen, ...
- **[Judge=3]** `§ 112 StPO – III. Flucht (Abs – Rn. 16` — Direkt relevant: Fluchtgefahr nach § 112 Abs. 2 Nr. 2
  > 16 Bei Ergreifung des Beschuldigten aufgrund des nach Abs. 2 Nr. 1 erlassenen Haftbefehls entfällt der Haftgrund der Flucht. In der Regel wird die vorherige Flucht aber die Aufrechterhaltung des Haftb...

#### ours-mxbai-voyage — Top 3
- **[Judge=3]** `§ 112 StPO – Rn. 112` — Direkt relevant: behandelt § 112 Abs. 2 Nr. 2 StPO
  > 112 (1) ¹ Die Untersuchungshaft darf gegen den Beschuldigten angeordnet werden, wenn er der Tat dringend verdächtig ist und ein Haftgrund besteht. ² Sie darf nicht angeordnet werden, wenn sie zu der B...
- **[Judge=1]** `§ 112 StPO – III. Flucht (Abs – Rn. 23` — Behandelt Verdunkelungsgefahr, nicht Fluchtgefahr
  > Bei einer besonders hohen Straferwartung braucht daher nur geprüft zu werden, ob Umstände vorhanden sind, die die hieraus herzuleitende Fluchtgefahr ausräumen können (KG StV 1996, 383; OLG München Str...
- **[Judge=0]** `§ 112 StPO – III. Flucht (Abs – Rn. 32 (Teil 2)` — Behandelt Verdunkelungsgefahr, nicht Fluchtgefahr
  > Wenn die Verdunkelungshandlungen nicht geeignet sind, die Ermittlung der Wahrheit zu erschweren, darf UHaft nicht angeordnet werden. Der Haftgrund liegt daher nicht vor, wenn der Sachverhalt schon in ...

### q14 — stpo-prozess

**Query:** Wie lange darf die Untersuchungshaft maximal dauern?

**Kontext:** § 121 StPO Sechs-Monats-Grenze, Haftpruefung OLG

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours-mxbai | 1.00 | 100% | 100% | 3 | 5.4s |
| ours-mxbai-voyage | 1.00 | 100% | 100% | 3 | 5.4s |

#### ours-mxbai — Top 3
- **[Judge=3]** `§ 121 StPO – Rn. 121` — Beantwortet direkt die 6-Monats-Grenze der Untersuchungshaft
  > 121 (1) Solange kein Urteil ergangen ist, das auf Freiheitsstrafe oder eine freiheitsentziehende Maßregel der Besserung und Sicherung erkennt, darf der Vollzug der Untersuchungshaft wegen derselben Ta...
- **[Judge=3]** `§ 121 StPO – Rn. 1` — Direkt relevant: Höchstgrenzen und Ausnahmen der Untersuchungshaft
  > Eine absolute Höchstgrenze für die Dauer v. UHaft sieht weder die StPO noch die EMRK vor (EGMR EuGRZ 1993, 384). Es kommt auf eine Abwägung aller Umstände des Einzelfalls an. Eine ein Jahr übersteigen...
- **[Judge=3]** `§ 121 StPO – Rn. 1` — Beantwortet direkt die Frage zur maximalen Haftdauer
  > 1 A. Beschleunigungsgebot. Einen Anspruch auf beschleunigte Aburteilung hat der in UHaft (und einstweiliger Unterbringung) befindliche Beschuldigte nach Art. 5 Abs. 3 S. 2 EMRK (→ EMRK Art. 5 Rn. 10 f...

#### ours-mxbai-voyage — Top 3
- **[Judge=3]** `§ 121 StPO – Rn. 121` — Direkt relevant: beantwortet die Frage zur Haftdauer
  > 121 (1) Solange kein Urteil ergangen ist, das auf Freiheitsstrafe oder eine freiheitsentziehende Maßregel der Besserung und Sicherung erkennt, darf der Vollzug der Untersuchungshaft wegen derselben Ta...
- **[Judge=3]** `§ 121 StPO – Rn. 1` — Direkte Antwort: 6-Monats-Grenze, OLG-Verlaengerung
  > 1 A. Beschleunigungsgebot. Einen Anspruch auf beschleunigte Aburteilung hat der in UHaft (und einstweiliger Unterbringung) befindliche Beschuldigte nach Art. 5 Abs. 3 S. 2 EMRK (→ EMRK Art. 5 Rn. 10 f...
- **[Judge=3]** `§ 121 StPO – Rn. 1` — Direkt relevant: absolute Höchstgrenzen und Dauerbegrenzungen UHaft
  > Eine absolute Höchstgrenze für die Dauer v. UHaft sieht weder die StPO noch die EMRK vor (EGMR EuGRZ 1993, 384). Es kommt auf eine Abwägung aller Umstände des Einzelfalls an. Eine ein Jahr übersteigen...

### q15 — stpo-prozess

**Query:** Was regelt § 136 StPO zur Beschuldigtenvernehmung?

**Kontext:** Belehrungspflichten, Recht auf Verteidiger

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours-mxbai | 0.91 | 100% | 100% | 2 | 5.8s |
| ours-mxbai-voyage | 0.84 | 40% | 67% | 1 | 6.0s |

#### ours-mxbai — Top 3
- **[Judge=2]** `§ 500 StPO – ILL. für das Strafverfahren und das Bußgeldverf` — Behandelt Beschuldigtenvernehmung, aber nicht § 136 StPO direkt
  > (4) Zeugen können zur Aufenthaltsermittlung ausgeschrieben werden.  (5) Für die internationale Fahndung nach Personen, einschließlich der Fahndung nach Personen im SIS und aufgrund eines Europäischen ...
- **[Judge=2]** `StPO – III. Steuerstrafverfahren – Rn. 79` — Behandelt Belehrung bei informatorischer Befragung vs Beschuldigtenvernehmung
  > 79 3. Die informatorische Befragung der Tatverdächtigen, die nach diesen Grundsätzen noch keine Beschuldigten sind, ist Zeugenvernehmung. Die Bestrebungen des Schrifttums, neben Beschuldigte u. Zeugen...
- **[Judge=3]** `StPO – III. Steuerstrafverfahren – Rn. 25` — Direkt relevant zu § 136 StPO und Belehrungspflichten
  > Das nemo-tenetur-Prinzip (nemo tenetur se ipsum accusare und nemo tenetur se ipsum prodere) o. der Grundsatz der Selbstbelastungsfreiheit bedeutet, dass niemand verpflichtet ist, sich selbst anzuklage...

#### ours-mxbai-voyage — Top 3
- **[Judge=1]** `§ 500 StPO – F. Beispiele aus der Rspr – Rn. 9` — Behandelt Verteidigeranwesenheit, nicht § 136 StPO direkt
  > 9 III. Beschuldigtenvernehmung (Nr. 3). An der Beschuldigtenvernehmung (Nr. 3) darf der Verteidiger, abw. v. §§ 163a Abs. 3 S. 2, 168c Abs. 1 StPO, nicht teilnehmen, wenn die gem. § 31 Abs. 1 getroffe...
- **[Judge=3]** `§ 114b StPO – I. Abs – Rn. 5` — Direkt relevant: behandelt Belehrungspflichten nach § 136 StPO
  > 5 II. Abs. 2 S. 1 Nr. 2–4. Hier wird die auch nach § 136 Abs. 1 S. 2, 3 und § 163a Abs. 3 S. 2, 4 vor Beginn der ersten richterlichen bzw. staatsanwaltschaftlichen o. polizeilichen Vernehmung bestehen...
- **[Judge=2]** `§ 500 StPO – ILL. für das Strafverfahren und das Bußgeldverf` — Behandelt Beschuldigtenvernehmung, aber nicht § 136 StPO direkt
  > (4) Zeugen können zur Aufenthaltsermittlung ausgeschrieben werden.  (5) Für die internationale Fahndung nach Personen, einschließlich der Fahndung nach Personen im SIS und aufgrund eines Europäischen ...

### q16 — cross-reference

**Query:** Worin unterscheidet sich Betrug von Unterschlagung?

**Kontext:** Abgrenzung § 263 vs § 246 StGB

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours-mxbai | 0.83 | 80% | 67% | 1 | 5.9s |
| ours-mxbai-voyage | 0.71 | 60% | 67% | 0 | 4.6s |

#### ours-mxbai — Top 3
- **[Judge=1]** `§ 263 StGB – BT. Zweitundzwanzigster Abschnitt – Rn. 69` — Betrug-Details, aber keine Unterschlagungsabgrenzung
  > 69 Anders ist es, wenn der Verfügende seinerseits nur (gutgläubige) Hilfsperson eines bösgläubigen Dritten ist. Hier ist auf den Irrtum des Entscheidungsbefugten abzustellen: Erkennt dieser die Unrich...
- **[Judge=3]** `§ 263 StGB – I. Vermögensbegriff  – Rn. 263` — Enthält vollständigen Wortlaut des Betrugstatbestands § 263
  > 263 (1) Wer in der Absicht, sich oder einem Dritten einen rechtswidrigen Vermögensvorteil zu verschaffen, das Vermögen eines anderen dadurch beschädigt, daß er durch Vorspiegelung falscher oder durch ...
- **[Judge=2]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 76` — Behandelt Betrug, aber nicht Abgrenzung zur Unterschlagung
  > 4. Dreiecksbetrug. Da die Getäuschte und die verfügende, nicht aber die verfügende und die geschädigte Person identisch sein müssen, ist der Tatbestand des § 263 nur erfüllt, wenn die Vermögensverfügu...

#### ours-mxbai-voyage — Top 3
- **[Judge=0]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 263 (Tei` — Nur Literaturverzeichnis, keine inhaltliche Abgrenzung
  > Heghmanns, Strafbarkeit des „Phishing“ von Bankkontendaten und ihrer Verwertung, wistra 2007, 167; Hilgendorf, Tatsachenaussagen u. Werturteile im Strafrecht, 1998; Hillenkamp, Zum Schutz „deliktische...
- **[Judge=3]** `§ 263 StGB – BT. Zweitundzwanzigster Abschnitt – Rn. 69` — Definiert Betrug Tatbestandsmerkmale, direkt relevant für Abgrenzung
  > 69 Anders ist es, wenn der Verfügende seinerseits nur (gutgläubige) Hilfsperson eines bösgläubigen Dritten ist. Hier ist auf den Irrtum des Entscheidungsbefugten abzustellen: Erkennt dieser die Unrich...
- **[Judge=2]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 76` — Behandelt Betrug, aber nicht Abgrenzung zur Unterschlagung
  > 4. Dreiecksbetrug. Da die Getäuschte und die verfügende, nicht aber die verfügende und die geschädigte Person identisch sein müssen, ist der Tatbestand des § 263 nur erfüllt, wenn die Vermögensverfügu...

### q17 — cross-reference

**Query:** Was sind die Unterschiede zwischen Diebstahl und Raub?

**Kontext:** § 242 vs § 249 StGB — Abgrenzung durch Gewalt/Drohung

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours-mxbai | 1.00 | 80% | 100% | 3 | 5.8s |
| ours-mxbai-voyage | 0.92 | 60% | 100% | 2 | 6.1s |

#### ours-mxbai — Top 3
- **[Judge=3]** `§ 249 StGB` — Direkt relevant: Abgrenzung Raub/Erpressung, Wegnahme, Nötigungsmittel
  > NStZ 2023, 351). Danach ist § 249 gegenüber § 255 ein spezielles Delikt; in jedem Raub liegt eine räuberische Erpressung (aA die hM in der Literatur). Die Unterscheidung richtet sich nach dem äußeren ...
- **[Judge=3]** `§ 249 StGB – BT. Zwanzigster Abschnitt – Rn. 15` — Direkt relevant: behandelt subjektiven Tatbestand bei Raub vs Diebstahl
  > G. Subjektiver Tatbestand. Der Vorsatz muss entsprechend der Doppelnatur des Raubs sowohl Wegnahme (vgl. dazu → § 242 Rn. 29 ff.) als auch Nötigung (→ § 240 Rn. 53 f.) sowie deren Verknüpfung umfassen...
- **[Judge=3]** `§ 241a StGB – BT. Achtzchniter Abschnitt – Rn. 242` — Direkt relevant: Definition und Tatbestandsmerkmale von Diebstahl
  > 242 (1) Wer eine fremde bewegliche Sache einem anderen in der Absicht wegnimmt, die Sache sich oder einem Dritten rechtswidrig zuzueignen, wird mit Freiheitsstrafe bis zu fünf Jahren oder mit Geldstra...

#### ours-mxbai-voyage — Top 3
- **[Judge=2]** `§ 250 StGB` — Behandelt Raub-Konkurrenzen, nicht direkte Abgrenzung zu Diebstahl
  > I. Rechtsfolgen. Der (einfache) Raub ist Verbrechen. Für minder schwere Fälle (vgl. → § 12 Rn. 11; → § 46 Rn. 85 ff.) gilt Abs. 2; ein solcher kann zB vorliegen, wenn das Maß der Gewalt gering ist ode...
- **[Judge=2]** `§ 252 StGB – I. Sonstige Vorschriften – Rn. 252` — Räuberischer Diebstahl als Verbindungstatbestand, thematisch relevant
  > 252 Wer, bei einem Diebstahl auf frischer Tat betroffen, gegen eine Person Gewalt verübt oder Drohungen mit gegenwärtiger Gefahr für Leib oder Leben anwendet, um sich im Besitz des gestohlenen Gutes z...
- **[Judge=3]** `§ 249 StGB` — Direkt relevant: behandelt Raub § 249, Wegnahme, Nötigungsmittel
  > NStZ 2023, 351). Danach ist § 249 gegenüber § 255 ein spezielles Delikt; in jedem Raub liegt eine räuberische Erpressung (aA die hM in der Literatur). Die Unterscheidung richtet sich nach dem äußeren ...

### q18 — cross-reference

**Query:** Wann wird Betrug zu Computerbetrug und umgekehrt?

**Kontext:** § 263 vs § 263a StGB — Abgrenzung bei elektronischer Datenverarbeitung

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours-mxbai | 0.61 | 40% | 33% | 0 | 6.2s |
| ours-mxbai-voyage | 0.78 | 20% | 33% | 1 | 5.9s |

#### ours-mxbai — Top 3
- **[Judge=0]** `§ 263 StGB – BT. Zweitundzwanzigster Abschnitt – Rn. 69` — Behandelt Betrug intern, nicht Abgrenzung zu Computerbetrug
  > 69 Anders ist es, wenn der Verfügende seinerseits nur (gutgläubige) Hilfsperson eines bösgläubigen Dritten ist. Hier ist auf den Irrtum des Entscheidungsbefugten abzustellen: Erkennt dieser die Unrich...
- **[Judge=1]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 62` — Behandelt Betrug allgemein, nicht Abgrenzung zu Computerbetrug
  > Die Kausalität der Täuschung für den Irrtum und dessen Kausalität für die Vermögensverfügung müssen im Einzelfall festgestellt sein. Mitverursachung reicht aus. Dabei darf das Gericht auch bei Serien-...
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 58` — Direkte Abgrenzung § 263 vs § 263a bei EDV
  > 58 Im Geschäftsverkehr wird sich, wer die Berechtigung eines Leistungsverlangens oder -auftrags nicht zu prüfen hat, hierüber idR auch keine (richtigen oder falschen) Gedanken machen (NStZ 1997, 281; ...

#### ours-mxbai-voyage — Top 3
- **[Judge=1]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 263 (Tei` — Literaturverzeichnis zu Betrug, nicht Computerbetrug-Abgrenzung
  > Heghmanns, Strafbarkeit des „Phishing“ von Bankkontendaten und ihrer Verwertung, wistra 2007, 167; Hilgendorf, Tatsachenaussagen u. Werturteile im Strafrecht, 1998; Hillenkamp, Zum Schutz „deliktische...
- **[Judge=0]** `§ 263 StGB – I. Sonstige Vorschriften 239 – Rn. 263 (Teil 2)` — Nur Literaturverzeichnis, keine inhaltliche Abgrenzung
  > Hernandez Basuano, Täuschung und Opferschutzniveau beim Betrug (usw.), FS Tiedemann, 2008, 605; Bechtel, Der Schutz illegaler Betäubungsmittel durch die Vermögens- und Eigentumsdelikte – sinnvoll?, wi...
- **[Judge=2]** `§ 263 StGB – I. Vermögensbegriff  – Rn. 263` — Behandelt § 263 StGB, aber ohne Abgrenzung zu § 263a
  > 263 (1) Wer in der Absicht, sich oder einem Dritten einen rechtswidrigen Vermögensvorteil zu verschaffen, das Vermögen eines anderen dadurch beschädigt, daß er durch Vorspiegelung falscher oder durch ...