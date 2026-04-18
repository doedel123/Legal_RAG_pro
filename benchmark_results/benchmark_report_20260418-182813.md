# RAG Benchmark Report

_Generiert: 2026-04-18T18:28:13_


- Queries: **18**
- Top-K: **5**
- Systeme: ours, ours-cohere

## Gesamtvergleich

| Metrik | ours | ours-cohere |
|--------|--------|--------|
| nDCG@10 | 0.963 | 0.975 |
| Relevance@10 | 81.1% | 85.6% |
| Relevance@3 | 87.0% | 90.7% |
| Top-1-Score | 2.61 | 2.78 |
| Mean-Score | 2.46 | 2.43 |
| Latenz (s) | 5.65 | 5.84 |

## Nach Kategorie


### alltagssprache

| Metrik | ours | ours-cohere |
|--------|--------|--------|
| nDCG@10 | 0.986 | 0.998 |
| Relevance@10 | 100.0% | 100.0% |
| Relevance@3 | 100.0% | 100.0% |

### cross-reference

| Metrik | ours | ours-cohere |
|--------|--------|--------|
| nDCG@10 | 0.913 | 0.942 |
| Relevance@10 | 66.7% | 60.0% |
| Relevance@3 | 88.9% | 66.7% |

### exakte-paragraphen

| Metrik | ours | ours-cohere |
|--------|--------|--------|
| nDCG@10 | 0.988 | 0.989 |
| Relevance@10 | 95.0% | 95.0% |
| Relevance@3 | 100.0% | 100.0% |

### konzept

| Metrik | ours | ours-cohere |
|--------|--------|--------|
| nDCG@10 | 0.969 | 0.979 |
| Relevance@10 | 85.0% | 80.0% |
| Relevance@3 | 83.3% | 91.7% |

### stpo-prozess

| Metrik | ours | ours-cohere |
|--------|--------|--------|
| nDCG@10 | 0.939 | 0.956 |
| Relevance@10 | 46.7% | 86.7% |
| Relevance@3 | 55.6% | 88.9% |

## Detail pro Query


### q01 — exakte-paragraphen

**Query:** Welche Voraussetzungen hat der gewerbsmaessige Bandenbetrug nach § 263 Abs. 5 StGB?

**Kontext:** Qualifikationstatbestand des Bandenbetrugs im Fischer-Kommentar

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours | 0.99 | 80% | 100% | 3 | 5.0s |
| ours-cohere | 0.98 | 80% | 100% | 3 | 5.4s |

#### ours — Top 3
- **[Judge=3]** `§ 263 StGB – BT. Zweijundzwanzigster Abschnitt – Rn. 213` — Direkt relevant: behandelt Voraussetzungen von Abs. 5
  > 213 Sind beide Varianten erfüllt, ist eine Qualifikation nach Abs. 5 gegeben. Die Abgrenzung des Abs. 3 Nr. 1 zum Verbrechen nach Abs. 5 ist in Fällen bandenmäßiger Begehung schwierig, denn eine auf f...
- **[Judge=3]** `§ 263 StGB – BT. Zweriindzwanzigster Abschnitt – Rn. 225` — Direkt relevant: behandelt exakt Bandenbetrug § 263 Abs. 5
  > IV. Qualifikation (Abs. 5). Abs. 5 enthält einen Qualifikationstatbestand, der die Tat in Fällen kumulativ gewerbs- und bandenmäßiger Begehung zum Verbrechen macht. Die Qualifikation ist in die Urteil...
- **[Judge=3]** `§ 263 StGB – BT. Zweijundzwanzigster Abschnitt – Rn. 212` — Direkt zu § 263 Abs. 5 Bandenbetrug
  > 212 Der Begriff der Urkundenfälschung ist weit zu fassen; er umfasst neben Taten nach § 267 auch solche nach §§ 268–281 (LK-StGB/Kubiciel/Tiedemann Rn. 297; NK-StGB/Kindhäuser/Hoven Rn. 392). Entsprec...

#### ours-cohere — Top 3
- **[Judge=3]** `§ 263 StGB – BT. Zweriindzwanzigster Abschnitt – Rn. 225` — Direkt relevant für gewerbsmäßigen Bandenbetrug § 263 Abs. 5
  > IV. Qualifikation (Abs. 5). Abs. 5 enthält einen Qualifikationstatbestand, der die Tat in Fällen kumulativ gewerbs- und bandenmäßiger Begehung zum Verbrechen macht. Die Qualifikation ist in die Urteil...
- **[Judge=3]** `§ 263 StGB – I. Vermögensbegriff  – Rn. 263` — Enthält vollständigen Wortlaut des § 263 Abs. 5
  > 263 (1) Wer in der Absicht, sich oder einem Dritten einen rechtswidrigen Vermögensvorteil zu verschaffen, das Vermögen eines anderen dadurch beschädigt, daß er durch Vorspiegelung falscher oder durch ...
- **[Judge=3]** `§ 263 StGB – BT. Zweijundzwanzigster Abschnitt – Rn. 213` — Direkt relevant für Qualifikationstatbestand nach § 263 Abs. 5
  > 213 Sind beide Varianten erfüllt, ist eine Qualifikation nach Abs. 5 gegeben. Die Abgrenzung des Abs. 3 Nr. 1 zum Verbrechen nach Abs. 5 ist in Fällen bandenmäßiger Begehung schwierig, denn eine auf f...

### q02 — exakte-paragraphen

**Query:** Was regelt § 112 StPO zur Untersuchungshaft?

**Kontext:** Anordnungsvoraussetzungen der U-Haft (dringender Tatverdacht, Haftgrund) im Schmitt/Koehler

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours | 1.00 | 100% | 100% | 3 | 5.8s |
| ours-cohere | 1.00 | 100% | 100% | 3 | 6.9s |

#### ours — Top 3
- **[Judge=3]** `§ 112 StPO – Rn. 112` — Direkt relevant: enthält den kompletten § 112 StPO
  > 112 (1) ¹ Die Untersuchungshaft darf gegen den Beschuldigten angeordnet werden, wenn er der Tat dringend verdächtig ist und ein Haftgrund besteht. ² Sie darf nicht angeordnet werden, wenn sie zu der B...
- **[Judge=3]** `§ 112 StPO – III. Flucht (Abs – Rn. 32 (Teil 2)` — Direkt relevant: Verdunkelungsgefahr als Haftgrund nach § 112 StPO
  > Wenn die Verdunkelungshandlungen nicht geeignet sind, die Ermittlung der Wahrheit zu erschweren, darf UHaft nicht angeordnet werden. Der Haftgrund liegt daher nicht vor, wenn der Sachverhalt schon in ...
- **[Judge=3]** `§ 112 StPO – Rn. 112` — Behandelt zentrale Voraussetzungen des § 112 StPO
  > Haftunfähigkeit des Beschuldigten schließt den Erlass des Haftbefehls nicht aus, sondern hindert nur seinen Vollzug (OLG Düsseldorf JZ 1984, 248; OLG Frankfurt a.M. NJW 1968, 2302; OLG Nürnberg OLGSt ...

#### ours-cohere — Top 3
- **[Judge=3]** `§ 112 StPO – Rn. 112` — Vollständiger Gesetzestext zu § 112 StPO
  > 112 (1) ¹ Die Untersuchungshaft darf gegen den Beschuldigten angeordnet werden, wenn er der Tat dringend verdächtig ist und ein Haftgrund besteht. ² Sie darf nicht angeordnet werden, wenn sie zu der B...
- **[Judge=3]** `§ 112 StPO – Rn. 112` — Direkt zu § 112 StPO Haftanordnungsvoraussetzungen
  > Haftunfähigkeit des Beschuldigten schließt den Erlass des Haftbefehls nicht aus, sondern hindert nur seinen Vollzug (OLG Düsseldorf JZ 1984, 248; OLG Frankfurt a.M. NJW 1968, 2302; OLG Nürnberg OLGSt ...
- **[Judge=3]** `§ 112 StPO – III. Flucht (Abs – Rn. 32 (Teil 2)` — Direkt relevant: Verdunkelungsgefahr als Haftgrund § 112 StPO
  > Wenn die Verdunkelungshandlungen nicht geeignet sind, die Ermittlung der Wahrheit zu erschweren, darf UHaft nicht angeordnet werden. Der Haftgrund liegt daher nicht vor, wenn der Sachverhalt schon in ...

### q03 — exakte-paragraphen

**Query:** Welche Haftgruende nennt § 112 Abs. 2 StPO?

**Kontext:** Fluchtgefahr, Verdunkelungsgefahr, Flucht — im StPO-Kommentar

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours | 0.99 | 100% | 100% | 3 | 4.7s |
| ours-cohere | 0.99 | 100% | 100% | 3 | 5.2s |

#### ours — Top 3
- **[Judge=3]** `§ 112 StPO – Rn. 112` — Direkt relevant: vollständige Aufzählung der Haftgründe
  > 112 (1) ¹ Die Untersuchungshaft darf gegen den Beschuldigten angeordnet werden, wenn er der Tat dringend verdächtig ist und ein Haftgrund besteht. ² Sie darf nicht angeordnet werden, wenn sie zu der B...
- **[Judge=3]** `§ 112 StPO – III. Flucht (Abs – Rn. 23` — Behandelt direkt die Haftgründe Flucht- und Verdunkelungsgefahr
  > Bei einer besonders hohen Straferwartung braucht daher nur geprüft zu werden, ob Umstände vorhanden sind, die die hieraus herzuleitende Fluchtgefahr ausräumen können (KG StV 1996, 383; OLG München Str...
- **[Judge=2]** `§ 112 StPO – III. Flucht (Abs – Rn. 32 (Teil 2)` — Behandelt Verdunkelungsgefahr als einen der Haftgruende
  > Wenn die Verdunkelungshandlungen nicht geeignet sind, die Ermittlung der Wahrheit zu erschweren, darf UHaft nicht angeordnet werden. Der Haftgrund liegt daher nicht vor, wenn der Sachverhalt schon in ...

#### ours-cohere — Top 3
- **[Judge=3]** `§ 112 StPO – Rn. 112` — Vollständige Auflistung aller Haftgründe des § 112 Abs. 2 StPO
  > 112 (1) ¹ Die Untersuchungshaft darf gegen den Beschuldigten angeordnet werden, wenn er der Tat dringend verdächtig ist und ein Haftgrund besteht. ² Sie darf nicht angeordnet werden, wenn sie zu der B...
- **[Judge=3]** `§ 112 StPO – III. Flucht (Abs – Rn. 23` — Behandelt direkt Haftgründe nach § 112 Abs. 2 StPO
  > Bei einer besonders hohen Straferwartung braucht daher nur geprüft zu werden, ob Umstände vorhanden sind, die die hieraus herzuleitende Fluchtgefahr ausräumen können (KG StV 1996, 383; OLG München Str...
- **[Judge=2]** `§ 112 StPO – III. Flucht (Abs – Rn. 32 (Teil 2)` — Behandelt Verdunkelungsgefahr, aber nicht alle Haftgruende
  > Wenn die Verdunkelungshandlungen nicht geeignet sind, die Ermittlung der Wahrheit zu erschweren, darf UHaft nicht angeordnet werden. Der Haftgrund liegt daher nicht vor, wenn der Sachverhalt schon in ...

### q04 — exakte-paragraphen

**Query:** Was regelt § 102 StPO zur Durchsuchung beim Beschuldigten?

**Kontext:** Durchsuchungsvoraussetzungen beim Verdaechtigen

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours | 0.97 | 100% | 100% | 3 | 5.1s |
| ours-cohere | 0.99 | 100% | 100% | 3 | 6.1s |

#### ours — Top 3
- **[Judge=3]** `§ 102 StPO – Rn. 102` — Volltext zu § 102 StPO Durchsuchungsvoraussetzungen
  > 102 Bei dem, welcher als Täter oder Teilnehmer einer Straftat oder der Datenhehlerei, Begünstigung, Strafvereitelung oder Hehlerei  Köhler    Ermittlungsmaßnahmen  verdächtig ist, kann eine Durchsuchu...
- **[Judge=2]** `§ 102 StPO – Rn. 10` — Thematisch relevant: Durchsuchungsvoraussetzungen und Beweismittelfindung
  > II. Auffinden von Beweismitteln. Zu den Beweismitteln (→ § 94 Rn. 4 ff.) gehören auch die nur in § 103 erwähnten Spuren (SK-StPO/Jäger/Wohlers Rn. 21) u. Personen, die zu Beweiszwecken in Augenschein ...
- **[Judge=3]** `§ 102 StPO – Rn. 10` — Erklärt § 102 StPO Durchsuchungsobjekte beim Beschuldigten
  > 10 III. Sachen. Sachen sind Kleidungsstücke, die der Verdächtige bei sich führt, ohne sie zu tragen, u. seine sonstige bewegliche Habe, gleichgültig, ob sie sich in seinem Umkreis, zB in Gepäckstücken...

#### ours-cohere — Top 3
- **[Judge=3]** `§ 102 StPO – Rn. 102` — Direkt relevant: Wortlaut und Voraussetzungen von § 102 StPO
  > 102 Bei dem, welcher als Täter oder Teilnehmer einer Straftat oder der Datenhehlerei, Begünstigung, Strafvereitelung oder Hehlerei  Köhler    Ermittlungsmaßnahmen  verdächtig ist, kann eine Durchsuchu...
- **[Judge=3]** `§ 102 StPO – Rn. 3` — Definiert direkt Durchsuchungsgegenstände des § 102 StPO
  > **Teilnehmer** nach §§ 25 ff. StGB, nicht die sog. notwendigen Teilnehmer (zum Begriff: Fischer/Fischer StGB Vor § 25 Rn. 7), stehen den Tatverdächtigen gleich. Bei jedem v. ihnen sowie bei den der Be...
- **[Judge=2]** `§ 102 StPO – Rn. 10` — Behandelt Durchsuchungsvoraussetzungen allgemein, nicht spezifisch § 102
  > II. Auffinden von Beweismitteln. Zu den Beweismitteln (→ § 94 Rn. 4 ff.) gehören auch die nur in § 103 erwähnten Spuren (SK-StPO/Jäger/Wohlers Rn. 21) u. Personen, die zu Beweiszwecken in Augenschein ...

### q05 — konzept

**Query:** Wann liegt eine konkludente Taeuschung im Sinne des § 263 StGB vor?

**Kontext:** Taeuschungshandlung durch schluessiges Verhalten

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours | 0.94 | 80% | 67% | 3 | 6.7s |
| ours-cohere | 0.91 | 100% | 100% | 2 | 5.8s |

#### ours — Top 3
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 14` — Behandelt direkt konkludente Täuschung bei § 263 StGB
  > Rspr. und hM bejahen darüber hinaus aber die Möglichkeit einer Täuschung durch Unterlassen auch ohne Erklärung gegenüber dem Irrenden (→ Rn. 38; vgl. BGHSt 39, 392 (398); BayObLG NJW 1987, 1654 (mAnm ...
- **[Judge=1]** `§ 263 StGB – I. Vermögensbegriff  – Rn. 263` — Gesetzestext ohne Erlaeuterung zur konkludenten Taeuschung
  > 263 (1) Wer in der Absicht, sich oder einem Dritten einen rechtswidrigen Vermögensvorteil zu verschaffen, das Vermögen eines anderen dadurch beschädigt, daß er durch Vorspiegelung falscher oder durch ...
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 21` — Definiert direkt konkludente Taeuschung nach § 263 StGB
  > 21 2. Konkludente Erklärungen. Auch durch eine schlüssige Handlung (konkludente Erklärung) kann vorspiegelt werden. Eine solche konkludente Erklärung durch aktives Tun ist von einer Erklärung durch Un...

#### ours-cohere — Top 3
- **[Judge=2]** `§ 263 StGB – I. Vermögensbegriff  – Rn. 263` — Enthält Betrug-Tatbestand, aber keine Details zu konkludenter Täuschung
  > 263 (1) Wer in der Absicht, sich oder einem Dritten einen rechtswidrigen Vermögensvorteil zu verschaffen, das Vermögen eines anderen dadurch beschädigt, daß er durch Vorspiegelung falscher oder durch ...
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 21` — Definiert direkt konkludente Taeuschung bei § 263 StGB
  > 21 2. Konkludente Erklärungen. Auch durch eine schlüssige Handlung (konkludente Erklärung) kann vorspiegelt werden. Eine solche konkludente Erklärung durch aktives Tun ist von einer Erklärung durch Un...
- **[Judge=2]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 263 (Tei` — Literaturliste zu Betrug, enthält konkludente Täuschung Referenzen
  > Heghmanns, Strafbarkeit des „Phishing“ von Bankkontendaten und ihrer Verwertung, wistra 2007, 167; Hilgendorf, Tatsachenaussagen u. Werturteile im Strafrecht, 1998; Hillenkamp, Zum Schutz „deliktische...

### q06 — konzept

**Query:** Was ist eine Vermoegensverfuegung und welche Anforderungen stellt die Rechtsprechung?

**Kontext:** Tatbestandsmerkmal der Vermoegensverfuegung beim Betrug

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours | 0.97 | 80% | 100% | 3 | 7.4s |
| ours-cohere | 1.00 | 40% | 67% | 3 | 6.0s |

#### ours — Top 3
- **[Judge=3]** `§ 263 StGB – BT. Zweitundzwanzigster Abschnitt – Rn. 69` — Definiert Vermoegensverfuegung und zentrale Anforderungen
  > 69 Anders ist es, wenn der Verfügende seinerseits nur (gutgläubige) Hilfsperson eines bösgläubigen Dritten ist. Hier ist auf den Irrtum des Entscheidungsbefugten abzustellen: Erkennt dieser die Unrich...
- **[Judge=2]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 87` — Behandelt Vermögensverfügung beim Betrug, aber nicht Definition/Anforderungen
  > 87 5. Kausalität. Für die Vermögensverfügung muss der täuschungsbedingte Irrtum kausal sein (vgl. BGHSt 24, 257 (260); 24, 386 (389); NStZ 2003, 313 (314 f.); OLG Düsseldorf NJW 1987, 3145); Mitverurs...
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 76` — Definiert Vermoegensverfuegung mit konkreten Rechtsprechungsanforderungen
  > 76 3. Unmittelbarkeit der Verfügung. Neben der Freiwilligkeit ist das Merkmal der Unmittelbarkeit nach stRspr und hM das wichtigste Kriterium zur Beschränkung der § 263 unterfallenden Selbstschädigung...

#### ours-cohere — Top 3
- **[Judge=3]** `§ 263 StGB – BT. Zweitundzwanzigster Abschnitt – Rn. 69` — Definiert Vermoegensverfuegung und rechtliche Anforderungen direkt
  > 69 Anders ist es, wenn der Verfügende seinerseits nur (gutgläubige) Hilfsperson eines bösgläubigen Dritten ist. Hier ist auf den Irrtum des Entscheidungsbefugten abzustellen: Erkennt dieser die Unrich...
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 76` — Definiert direkt Vermoegensverfuegung bei Betrug mit Rechtsprechungsanforderungen
  > 4. Dreiecksbetrug. Da die Getäuschte und die verfügende, nicht aber die verfügende und die geschädigte Person identisch sein müssen, ist der Tatbestand des § 263 nur erfüllt, wenn die Vermögensverfügu...
- **[Judge=1]** `§ 263 StGB – I. Vermögensbegriff  – Rn. 263` — Betrug-Grundtatbestand, aber keine Definition von Vermoegensverfuegung
  > 263 (1) Wer in der Absicht, sich oder einem Dritten einen rechtswidrigen Vermögensvorteil zu verschaffen, das Vermögen eines anderen dadurch beschädigt, daß er durch Vorspiegelung falscher oder durch ...

### q07 — konzept

**Query:** Was versteht man unter einem Gefaehrdungsschaden beim Betrug?

**Kontext:** Schadensbegriff, schadensgleiche Vermoegensgefaehrdung

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours | 0.99 | 100% | 100% | 3 | 4.9s |
| ours-cohere | 1.00 | 100% | 100% | 3 | 5.4s |

#### ours — Top 3
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 159` — Definiert direkt Gefaehrdungsschaden beim Betrug
  > 159 b) Voraussetzungen. aa) Ein Gefährdungsschaden ist gegeben, wenn die Wahrscheinlichkeit des endgültigen Verlusts eines Vermögensbestandteils zum Zeitpunkt der täuschungsbedingten Verfügung so groß...
- **[Judge=3]** `§ 263 StGB – BT. Zwei undzwanzigster Abschnitt – Rn. 263 (Te` — Direkt relevant: Gefährdungsschaden explizit behandelt
  > Fischer/Lutz    Betrug und Untreue   rechts für das Strafrecht, FS Weber, 2004, 271; Eisele/Bechtel, Der Schadensbegriff bei den Vermögensdelikten, JuS 2018, 97; Ellbogen/Wichmann, Zu Problemen des är...
- **[Judge=2]** `§ 263 StGB – BT. Zwei undzwanzigster Abschnitt – Rn. 263` — Thematisch relevant: Schadensmerkmal beim Betrug, aber spezielle Literatur
  > **Rechtsprechungsübersicht:** Scholz, Die Entwicklung des Berufs- und Vertragsarztrechts, medstra 2019, 331; 2021, 349; 2022, 355; 2023, 355; 2024, 351.  Weinrich/Wostry, Der Abrechnungsbetrug in der ...

#### ours-cohere — Top 3
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 109` — Direkt relevant: behandelt Gefaehrdungsschaden beim Betrug
  > VI. Schaden. Vermögensschaden ist ein negativer Saldo zwischen dem Wert des Vermögens vor und nach der irrtumsbedingten Vermögensverfügung des Getäuschten (Prinzip der Gesamtsaldierung; stRspr; vgl. B...
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 159` — Definiert direkt Gefaehrdungsschaden beim Betrug
  > 159 b) Voraussetzungen. aa) Ein Gefährdungsschaden ist gegeben, wenn die Wahrscheinlichkeit des endgültigen Verlusts eines Vermögensbestandteils zum Zeitpunkt der täuschungsbedingten Verfügung so groß...
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 171` — Direkt relevant: erklaert Gefaehrdungsschaden bei EC-/Kreditkarten ausfuehrlich
  > Die täuschungsbedingte Herausgabe von EC-Karten, Kreditkarten und weiteren Zugangsdaten zu Bank-Guthaben (PINs, TANs; Passwörter), sei es infolge persönlicher Täuschung oder von „Phishing“-Manipulatio...

### q08 — konzept

**Query:** Wie wird der Vorsatz beim Betrug bestimmt, insbesondere die Bereicherungsabsicht?

**Kontext:** Subjektiver Tatbestand § 263 StGB

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours | 0.97 | 80% | 67% | 3 | 6.4s |
| ours-cohere | 1.00 | 80% | 100% | 3 | 5.6s |

#### ours — Top 3
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 176` — Direkt relevant: behandelt Vorsatz und Bereicherungsabsicht § 263
  > D. Subjektiver Tatbestand. § 263 setzt Vorsatz voraus; darüber hinaus ist die Absicht rechtswidriger Bereicherung erforderlich.   I. Vorsatz. 1. Täuschungsvorsatz. Der Vorsatz (bedingter Vorsatz genüg...
- **[Judge=3]** `§ 263 StGB – I. Sonstige Vorschriften 239 – Rn. 263 (Teil 1)` — Behandelt direkt Bereicherungsabsicht und subjektiven Tatbestand
  > 3. Einzelne Fallgruppen ... 92 4. Rechtlich missbilligte, sittenwidrige und gesetzeswidrige wirtschaftliche Werte ... 101 VI. Schaden ... 110 1. Grundsätze der Schadensermittlung ... 111 2. Vermögensm...
- **[Judge=1]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 187 (Tei` — Stoffgleichheit bei Bereicherung, nicht Vorsatzbestimmung
  > 187 1. Stoffgleichheit. Der Vorteil muss die Kehrseite des Schadens und ihm „stoffgleich“ sein; er muss unmittelbare Folge der täuschungsbedingten Verfügung sein, welche den Schaden des Opfers herbeif...

#### ours-cohere — Top 3
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 176` — Direkt relevant: behandelt Vorsatz und Bereicherungsabsicht § 263
  > D. Subjektiver Tatbestand. § 263 setzt Vorsatz voraus; darüber hinaus ist die Absicht rechtswidriger Bereicherung erforderlich.   I. Vorsatz. 1. Täuschungsvorsatz. Der Vorsatz (bedingter Vorsatz genüg...
- **[Judge=3]** `§ 263 StGB – I. Sonstige Vorschriften 239 – Rn. 263 (Teil 1)` — Behandelt direkt Bereicherungsabsicht und subjektiven Tatbestand
  > 3. Einzelne Fallgruppen ... 92 4. Rechtlich missbilligte, sittenwidrige und gesetzeswidrige wirtschaftliche Werte ... 101 VI. Schaden ... 110 1. Grundsätze der Schadensermittlung ... 111 2. Vermögensm...
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 186` — Direkt relevant zur Bereicherungsabsicht beim Betrug
  > 186 II. Bereicherungsabsicht. Die Tat muss subjektiv auf die Erlangung eines rechtswidrigen Vermögensvorteils für den Täuschenden oder einen Dritten gerichtet sein. Vermögensvorteil ist die Erhöhung d...

### q09 — alltagssprache

**Query:** Hat der Angeklagte die Kunden über das Internet betrogen?

**Kontext:** Abstrakte Frage zu Internetbetrug, sucht Taeuschungshandlung + Schaden

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours | 0.97 | 100% | 100% | 3 | 5.7s |
| ours-cohere | 1.00 | 100% | 100% | 2 | 6.0s |

#### ours — Top 3
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 14` — Direkt relevant zu Internetbetrug-Taeuschungshandlungen, Phishing-Mails
  > Rspr. und hM bejahen darüber hinaus aber die Möglichkeit einer Täuschung durch Unterlassen auch ohne Erklärung gegenüber dem Irrenden (→ Rn. 38; vgl. BGHSt 39, 392 (398); BayObLG NJW 1987, 1654 (mAnm ...
- **[Judge=2]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 263 (Tei` — Phishing und Internetbetrug relevant, aber nur Literaturverzeichnis
  > Heghmanns, Strafbarkeit des „Phishing“ von Bankkontendaten und ihrer Verwertung, wistra 2007, 167; Hilgendorf, Tatsachenaussagen u. Werturteile im Strafrecht, 1998; Hillenkamp, Zum Schutz „deliktische...
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 62` — Direkt relevant: Betrug Täuschung-Irrtum-Kausalität bei Massenbetrug
  > Die Kausalität der Täuschung für den Irrtum und dessen Kausalität für die Vermögensverfügung müssen im Einzelfall festgestellt sein. Mitverursachung reicht aus. Dabei darf das Gericht auch bei Serien-...

#### ours-cohere — Top 3
- **[Judge=2]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 263 (Tei` — Thematisch relevant: Betrug, Internet, Phishing-Bezug
  > Heghmanns, Strafbarkeit des „Phishing“ von Bankkontendaten und ihrer Verwertung, wistra 2007, 167; Hilgendorf, Tatsachenaussagen u. Werturteile im Strafrecht, 1998; Hillenkamp, Zum Schutz „deliktische...
- **[Judge=2]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 182` — Vorsatz bei Vermögensschäden, relevant für Betrugsdelikte
  > 182 In Fällen des Gefährdungsschadens hat der BGH vielfach entschieden, die Kenntnis von Umständen, welche die Gefahr des Vermögensverlusts begründen, reiche oft, aber nicht in jedem Fall aus, um das ...
- **[Judge=2]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 176` — Subjektiver Tatbestand relevant für Internetbetrug-Bewertung
  > D. Subjektiver Tatbestand. § 263 setzt Vorsatz voraus; darüber hinaus ist die Absicht rechtswidriger Bereicherung erforderlich.   I. Vorsatz. 1. Täuschungsvorsatz. Der Vorsatz (bedingter Vorsatz genüg...

### q10 — alltagssprache

**Query:** Wann darf die Polizei bei jemandem zu Hause suchen?

**Kontext:** Durchsuchungsvoraussetzungen, §§ 102 ff. StPO

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours | 0.98 | 100% | 100% | 3 | 5.7s |
| ours-cohere | 0.99 | 100% | 100% | 3 | 5.7s |

#### ours — Top 3
- **[Judge=3]** `§ 102 StPO – Rn. 102` — Beantwortet direkt Durchsuchungsvoraussetzungen bei Wohnungen
  > 102 Bei dem, welcher als Täter oder Teilnehmer einer Straftat oder der Datenhehlerei, Begünstigung, Strafvereitelung oder Hehlerei  Köhler    Ermittlungsmaßnahmen  verdächtig ist, kann eine Durchsuchu...
- **[Judge=2]** `§ 102 StPO – Rn. 10` — Behandelt Durchsuchungsvoraussetzungen, aber keine grundlegenden Befugnisnormen
  > II. Auffinden von Beweismitteln. Zu den Beweismitteln (→ § 94 Rn. 4 ff.) gehören auch die nur in § 103 erwähnten Spuren (SK-StPO/Jäger/Wohlers Rn. 21) u. Personen, die zu Beweiszwecken in Augenschein ...
- **[Judge=3]** `§ 102 StPO – Rn. 3` — Direkt relevant für Durchsuchungsvoraussetzungen und Durchsuchungsgegenstände
  > **Teilnehmer** nach §§ 25 ff. StGB, nicht die sog. notwendigen Teilnehmer (zum Begriff: Fischer/Fischer StGB Vor § 25 Rn. 7), stehen den Tatverdächtigen gleich. Bei jedem v. ihnen sowie bei den der Be...

#### ours-cohere — Top 3
- **[Judge=3]** `§ 102 StPO – Rn. 102` — Direkt relevant: § 102 StPO Durchsuchungsvoraussetzungen
  > 102 Bei dem, welcher als Täter oder Teilnehmer einer Straftat oder der Datenhehlerei, Begünstigung, Strafvereitelung oder Hehlerei  Köhler    Ermittlungsmaßnahmen  verdächtig ist, kann eine Durchsuchu...
- **[Judge=3]** `§ 102 StPO – Rn. 10` — Direkt relevant: behandelt Durchsuchungsvoraussetzungen und Verhältnismäßigkeitsgrundsatz
  > II. Auffinden von Beweismitteln. Zu den Beweismitteln (→ § 94 Rn. 4 ff.) gehören auch die nur in § 103 erwähnten Spuren (SK-StPO/Jäger/Wohlers Rn. 21) u. Personen, die zu Beweiszwecken in Augenschein ...
- **[Judge=2]** `§ 102 StPO – Rn. 3` — Behandelt Durchsuchungsvoraussetzungen, aber spezielle Aspekte
  > **Teilnehmer** nach §§ 25 ff. StGB, nicht die sog. notwendigen Teilnehmer (zum Begriff: Fischer/Fischer StGB Vor § 25 Rn. 7), stehen den Tatverdächtigen gleich. Bei jedem v. ihnen sowie bei den der Be...

### q11 — alltagssprache

**Query:** Was passiert wenn jemand luegt damit er Geld bekommt?

**Kontext:** Laienhafte Umschreibung des Betrugstatbestandes

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours | 1.00 | 100% | 100% | 3 | 5.7s |
| ours-cohere | 1.00 | 100% | 100% | 3 | 5.0s |

#### ours — Top 3
- **[Judge=3]** `§ 263 StGB – I. Vermögensbegriff  – Rn. 263` — Beantwortet direkt die Frage zum Betrugstatbestand
  > 263 (1) Wer in der Absicht, sich oder einem Dritten einen rechtswidrigen Vermögensvorteil zu verschaffen, das Vermögen eines anderen dadurch beschädigt, daß er durch Vorspiegelung falscher oder durch ...
- **[Judge=3]** `§ 263 StGB – BT. Zweitundzwanzigster Abschnitt – Rn. 69` — Direkt relevant: behandelt Betrugstatbestand § 263 StGB
  > 69 Anders ist es, wenn der Verfügende seinerseits nur (gutgläubige) Hilfsperson eines bösgläubigen Dritten ist. Hier ist auf den Irrtum des Entscheidungsbefugten abzustellen: Erkennt dieser die Unrich...
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 176` — Direkt relevant: Subjektiver Tatbestand des Betrugs erklärt
  > D. Subjektiver Tatbestand. § 263 setzt Vorsatz voraus; darüber hinaus ist die Absicht rechtswidriger Bereicherung erforderlich.   I. Vorsatz. 1. Täuschungsvorsatz. Der Vorsatz (bedingter Vorsatz genüg...

#### ours-cohere — Top 3
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 5` — Direkt relevant: Betrugstatbestand mit Täuschung und Vermögensschaden
  > 5 C. Grundtatbestand, Abs. 1. Tathandlung ist das Täuschen einer natürlichen Person (vgl. NStZ 2005, 213) über Tatsachen. Erfolg dieser Handlung muss ein Irrtum des Täuschungsadressaten sein; dieser m...
- **[Judge=3]** `§ 263 StGB – I. Vermögensbegriff  – Rn. 263` — Definiert exakt Betrug durch Täuschung für Vermögensvorteil
  > 263 (1) Wer in der Absicht, sich oder einem Dritten einen rechtswidrigen Vermögensvorteil zu verschaffen, das Vermögen eines anderen dadurch beschädigt, daß er durch Vorspiegelung falscher oder durch ...
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 176` — Direkt relevant: subjektiver Tatbestand des Betrugsparagraphen
  > D. Subjektiver Tatbestand. § 263 setzt Vorsatz voraus; darüber hinaus ist die Absicht rechtswidriger Bereicherung erforderlich.   I. Vorsatz. 1. Täuschungsvorsatz. Der Vorsatz (bedingter Vorsatz genüg...

### q12 — alltagssprache

**Query:** Wann muss jemand ins Gefaengnis waehrend die Tat noch nicht bewiesen ist?

**Kontext:** Untersuchungshaft, §§ 112 ff. StPO

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours | 1.00 | 100% | 100% | 3 | 5.8s |
| ours-cohere | 1.00 | 100% | 100% | 3 | 5.7s |

#### ours — Top 3
- **[Judge=3]** `§ 112 StPO – Rn. 112` — Direkt relevant: definiert Untersuchungshaft ohne Beweis
  > 112 (1) ¹ Die Untersuchungshaft darf gegen den Beschuldigten angeordnet werden, wenn er der Tat dringend verdächtig ist und ein Haftgrund besteht. ² Sie darf nicht angeordnet werden, wenn sie zu der B...
- **[Judge=3]** `§ 112 StPO – Rn. 112` — Erklärt dringenden Tatverdacht für Untersuchungshaft
  > Haftunfähigkeit des Beschuldigten schließt den Erlass des Haftbefehls nicht aus, sondern hindert nur seinen Vollzug (OLG Düsseldorf JZ 1984, 248; OLG Frankfurt a.M. NJW 1968, 2302; OLG Nürnberg OLGSt ...
- **[Judge=3]** `§ 112 StPO – III. Flucht (Abs – Rn. 23` — Direkt relevant: erklärt Haftgründe bei Verdunkelungsgefahr
  > Bei einer besonders hohen Straferwartung braucht daher nur geprüft zu werden, ob Umstände vorhanden sind, die die hieraus herzuleitende Fluchtgefahr ausräumen können (KG StV 1996, 383; OLG München Str...

#### ours-cohere — Top 3
- **[Judge=3]** `§ 112 StPO – Rn. 112` — Direkt relevant: definiert Untersuchungshaft vor Tatbeweis
  > 112 (1) ¹ Die Untersuchungshaft darf gegen den Beschuldigten angeordnet werden, wenn er der Tat dringend verdächtig ist und ein Haftgrund besteht. ² Sie darf nicht angeordnet werden, wenn sie zu der B...
- **[Judge=3]** `§ 112 StPO – III. Flucht (Abs – Rn. 23` — Direkt relevant zu Haftgruenden der Untersuchungshaft
  > Bei einer besonders hohen Straferwartung braucht daher nur geprüft zu werden, ob Umstände vorhanden sind, die die hieraus herzuleitende Fluchtgefahr ausräumen können (KG StV 1996, 383; OLG München Str...
- **[Judge=3]** `§ 112 StPO – Rn. 112` — Erklaert direkt Voraussetzungen fuer Untersuchungshaft vor Verurteilung
  > Haftunfähigkeit des Beschuldigten schließt den Erlass des Haftbefehls nicht aus, sondern hindert nur seinen Vollzug (OLG Düsseldorf JZ 1984, 248; OLG Frankfurt a.M. NJW 1968, 2302; OLG Nürnberg OLGSt ...

### q13 — stpo-prozess

**Query:** Welche Voraussetzungen hat die Untersuchungshaft wegen Fluchtgefahr?

**Kontext:** § 112 Abs. 2 Nr. 2 StPO Fluchtgefahr

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours | 1.00 | 80% | 100% | 3 | 4.7s |
| ours-cohere | 0.99 | 80% | 100% | 3 | 4.9s |

#### ours — Top 3
- **[Judge=3]** `§ 112 StPO – Rn. 112` — Direkt relevant: § 112 Abs. 2 Nr. 2 Fluchtgefahr
  > 112 (1) ¹ Die Untersuchungshaft darf gegen den Beschuldigten angeordnet werden, wenn er der Tat dringend verdächtig ist und ein Haftgrund besteht. ² Sie darf nicht angeordnet werden, wenn sie zu der B...
- **[Judge=3]** `§ 112 StPO – III. Flucht (Abs – Rn. 17 (Teil 1)` — Definiert direkt Fluchtgefahr-Voraussetzungen nach § 112 Abs. 2 Nr. 2
  > 17 IV. Fluchtgefahr (Abs. 2 Nr. 2). Fluchtgefahr (Abs. 2 Nr. 2) besteht, wenn die Würdigung der Umstände des Falles es wahrscheinlicher macht, dass sich der Beschuldigte dem Strafverfahren entziehen, ...
- **[Judge=3]** `§ 112 StPO – III. Flucht (Abs – Rn. 16` — Direkt zu Fluchtgefahr nach § 112 Abs. 2 Nr. 2
  > 16 Bei Ergreifung des Beschuldigten aufgrund des nach Abs. 2 Nr. 1 erlassenen Haftbefehls entfällt der Haftgrund der Flucht. In der Regel wird die vorherige Flucht aber die Aufrechterhaltung des Haftb...

#### ours-cohere — Top 3
- **[Judge=3]** `§ 112 StPO – Rn. 112` — Enthält zentrale Voraussetzungen für Fluchtgefahr-Haftgrund direkt
  > 112 (1) ¹ Die Untersuchungshaft darf gegen den Beschuldigten angeordnet werden, wenn er der Tat dringend verdächtig ist und ein Haftgrund besteht. ² Sie darf nicht angeordnet werden, wenn sie zu der B...
- **[Judge=3]** `§ 112 StPO – III. Flucht (Abs – Rn. 16` — Direkt relevant: Fluchtgefahr nach § 112 Abs. 2 Nr. 2
  > 16 Bei Ergreifung des Beschuldigten aufgrund des nach Abs. 2 Nr. 1 erlassenen Haftbefehls entfällt der Haftgrund der Flucht. In der Regel wird die vorherige Flucht aber die Aufrechterhaltung des Haftb...
- **[Judge=3]** `§ 112 StPO – III. Flucht (Abs – Rn. 17` — Direkt relevant: Voraussetzungen Fluchtgefahr detailliert erklärt
  > Die Beurteilung der Fluchtgefahr erfordert die Berücksichtigung aller Umstände des Falles, insbes. der Art der dem Beschuldigten vorgeworfenen Tat, der Persönlichkeit des Beschuldigten, seiner Lebensv...

### q14 — stpo-prozess

**Query:** Wie lange darf die Untersuchungshaft maximal dauern?

**Kontext:** § 121 StPO Sechs-Monats-Grenze, Haftpruefung OLG

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours | 1.00 | 0% | 0% | 1 | 5.0s |
| ours-cohere | 0.98 | 100% | 100% | 3 | 5.7s |

#### ours — Top 3
- **[Judge=1]** `§ 117 StPO – Rn. 6` — Behandelt Haftbeschwerde, nicht Haftdauer
  > Die Entscheidung ergeht idR nach Aktenlage (zur Entsch. des Berufungs- o. Revisionsgerichts vgl. → § 114 Rn. 21); nach § 118 Abs. 2 kann aber auf Antrag des Beschuldigten o. vAw auch nach mündlicher V...
- **[Judge=1]** `§ 117 StPO – Rn. 117` — Haftprüfungsverfahren, aber nicht Höchstdauer
  > 117 (1) Solange der Beschuldigte in Untersuchungshaft ist, kann er jederzeit die gerichtliche Prüfung beantragen, ob der Haftbefehl aufzuheben oder dessen Vollzug nach § 116 auszusetzen ist (Haftprüfu...
- **[Judge=1]** `§ 117 StPO – Rn. 2` — Behandelt Haftprüfung, nicht maximale Haftdauer
  > 2 I. Haftprüfung auf Antrag des Beschuldigten (Abs. 1). Die Haftprüfung auf Antrag (Abs. 1) des Beschuldigten (wegen der Haftprüfung vAw vgl. → Rn. 16) verpflichtet den nach § 126 Abs. 1 zuständigen R...

#### ours-cohere — Top 3
- **[Judge=3]** `§ 121 StPO – Rn. 1` — Direkt zur Sechs-Monats-Grenze und maximalen UHaft-Dauer
  > 1 A. Beschleunigungsgebot. Einen Anspruch auf beschleunigte Aburteilung hat der in UHaft (und einstweiliger Unterbringung) befindliche Beschuldigte nach Art. 5 Abs. 3 S. 2 EMRK (→ EMRK Art. 5 Rn. 10 f...
- **[Judge=2]** `§ 121 StPO – Rn. 8 (Teil 1)` — Behandelt UHaft-Beschränkungen, aber nicht Sechs-Monats-Grenze
  > 8 II. Zeitliche Geltung der Beschränkungen der UHaft. Bis zu einem auf Freiheitsentziehung lautenden Urteil (Freiheitsstrafe mit o. ohne Bewährung o. freiheitsentziehende Sicherungsmaßregeln) gelten d...
- **[Judge=3]** `§ 121 StPO – Rn. 1` — Direkt relevant: Höchstgrenzen und Fristen der Untersuchungshaft
  > Eine absolute Höchstgrenze für die Dauer v. UHaft sieht weder die StPO noch die EMRK vor (EGMR EuGRZ 1993, 384). Es kommt auf eine Abwägung aller Umstände des Einzelfalls an. Eine ein Jahr übersteigen...

### q15 — stpo-prozess

**Query:** Was regelt § 136 StPO zur Beschuldigtenvernehmung?

**Kontext:** Belehrungspflichten, Recht auf Verteidiger

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours | 0.82 | 60% | 67% | 1 | 6.0s |
| ours-cohere | 0.90 | 80% | 67% | 2 | 6.7s |

#### ours — Top 3
- **[Judge=1]** `§ 110c StPO – Rn. 3` — Tangential: erwähnt § 136 Belehrungspflichten bei Verdeckten Ermittlern
  > 3 B. Sonstige Befugnisse. Als Beamter des Polizeidienstes hat der Verdeckte Ermittler die sich aus der StPO (zB §§ 102, 103, 127 Abs. 2 unter den dort jew. bezeichneten Voraussetzungen), den Polizeige...
- **[Judge=3]** `StPO – III. Steuerstrafverfahren – Rn. 25` — Behandelt direkt § 136 StPO und Belehrungspflichten
  > Das nemo-tenetur-Prinzip (nemo tenetur se ipsum accusare und nemo tenetur se ipsum prodere) o. der Grundsatz der Selbstbelastungsfreiheit bedeutet, dass niemand verpflichtet ist, sich selbst anzuklage...
- **[Judge=2]** `§ 500 StPO – ILL. für das Strafverfahren und das Bußgeldverf` — Behandelt Beschuldigtenvernehmung und Belehrung nach § 136
  > (4) Zeugen können zur Aufenthaltsermittlung ausgeschrieben werden.  (5) Für die internationale Fahndung nach Personen, einschließlich der Fahndung nach Personen im SIS und aufgrund eines Europäischen ...

#### ours-cohere — Top 3
- **[Judge=2]** `§ 500 StPO – ILL. für das Strafverfahren und das Bußgeldverf` — Behandelt Beschuldigtenvernehmung, aber nicht § 136 StPO direkt
  > (4) Zeugen können zur Aufenthaltsermittlung ausgeschrieben werden.  (5) Für die internationale Fahndung nach Personen, einschließlich der Fahndung nach Personen im SIS und aufgrund eines Europäischen ...
- **[Judge=3]** `§ 114b StPO – I. Abs – Rn. 5` — Direkter Bezug zu § 136 StPO Belehrungspflichten
  > 5 II. Abs. 2 S. 1 Nr. 2–4. Hier wird die auch nach § 136 Abs. 1 S. 2, 3 und § 163a Abs. 3 S. 2, 4 vor Beginn der ersten richterlichen bzw. staatsanwaltschaftlichen o. polizeilichen Vernehmung bestehen...
- **[Judge=1]** `§ 115 StPO – Rn. 5` — Behandelt Vorführung/Vernehmung, aber nicht § 136 StPO
  > 5 Am Tage nach der Ergreifung darf er nur vorgeführt werden, wenn eine frühere Vorführung nicht möglich ist. Spätestens an diesem Tage muss die Vorführung aber stattfinden, auch wenn er ein Sonnabend,...

### q16 — cross-reference

**Query:** Worin unterscheidet sich Betrug von Unterschlagung?

**Kontext:** Abgrenzung § 263 vs § 246 StGB

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours | 0.91 | 80% | 100% | 2 | 5.7s |
| ours-cohere | 0.88 | 60% | 67% | 2 | 5.6s |

#### ours — Top 3
- **[Judge=2]** `§ 263 StGB – BT. Zweitundzwanzigster Abschnitt – Rn. 69` — Behandelt Betrug, aber nicht Unterschlagungsabgrenzung
  > 69 Anders ist es, wenn der Verfügende seinerseits nur (gutgläubige) Hilfsperson eines bösgläubigen Dritten ist. Hier ist auf den Irrtum des Entscheidungsbefugten abzustellen: Erkennt dieser die Unrich...
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 76` — Behandelt Betrug direkt, zeigt Abgrenzung zur Wegnahme
  > 4. Dreiecksbetrug. Da die Getäuschte und die verfügende, nicht aber die verfügende und die geschädigte Person identisch sein müssen, ist der Tatbestand des § 263 nur erfüllt, wenn die Vermögensverfügu...
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 76` — Zentrale Abgrenzungskriterien Betrug: Verfügung und Unmittelbarkeit
  > 76 3. Unmittelbarkeit der Verfügung. Neben der Freiwilligkeit ist das Merkmal der Unmittelbarkeit nach stRspr und hM das wichtigste Kriterium zur Beschränkung der § 263 unterfallenden Selbstschädigung...

#### ours-cohere — Top 3
- **[Judge=2]** `§ 247 StGB – BT. Neunzehnter Abschnitt – Rn. 24` — Behandelt Abgrenzung § 246 zu § 263
  > 24 L. Konkurrenzen im Übrigen. Bei Manifestation des Zueignungswillens hinsichtlich mehrerer Sachen durch eine Ausführungshandlung liegt nur eine Tat vor (wistra 2006, 227 (227 f.)). Zur Abgrenzung vo...
- **[Judge=1]** `§ 263 StGB – BT. Zweitundzwanzigster Abschnitt – Rn. 69` — Behandelt Betrug, aber keine Unterschlagungsabgrenzung
  > 69 Anders ist es, wenn der Verfügende seinerseits nur (gutgläubige) Hilfsperson eines bösgläubigen Dritten ist. Hier ist auf den Irrtum des Entscheidungsbefugten abzustellen: Erkennt dieser die Unrich...
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 76` — Direkt relevant: Abgrenzung Betrug zu anderen Delikten
  > 4. Dreiecksbetrug. Da die Getäuschte und die verfügende, nicht aber die verfügende und die geschädigte Person identisch sein müssen, ist der Tatbestand des § 263 nur erfüllt, wenn die Vermögensverfügu...

### q17 — cross-reference

**Query:** Was sind die Unterschiede zwischen Diebstahl und Raub?

**Kontext:** § 242 vs § 249 StGB — Abgrenzung durch Gewalt/Drohung

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours | 1.00 | 60% | 100% | 3 | 6.1s |
| ours-cohere | 1.00 | 100% | 100% | 3 | 6.3s |

#### ours — Top 3
- **[Judge=3]** `§ 249 StGB` — Direkt relevant zu Raub-Tatbestandsmerkmalen und Abgrenzung
  > NStZ 2023, 351). Danach ist § 249 gegenüber § 255 ein spezielles Delikt; in jedem Raub liegt eine räuberische Erpressung (aA die hM in der Literatur). Die Unterscheidung richtet sich nach dem äußeren ...
- **[Judge=3]** `§ 249 StGB – BT. Zwanzigster Abschnitt – Rn. 15` — Direkt relevant: behandelt subjektiven Tatbestand bei Raub mit Bezug zu Diebstahl
  > G. Subjektiver Tatbestand. Der Vorsatz muss entsprechend der Doppelnatur des Raubs sowohl Wegnahme (vgl. dazu → § 242 Rn. 29 ff.) als auch Nötigung (→ § 240 Rn. 53 f.) sowie deren Verknüpfung umfassen...
- **[Judge=3]** `§ 241a StGB – BT. Achtzchniter Abschnitt – Rn. 242` — Diebstahlstatbestand direkt relevant für Abgrenzung
  > 242 (1) Wer eine fremde bewegliche Sache einem anderen in der Absicht wegnimmt, die Sache sich oder einem Dritten rechtswidrig zuzueignen, wird mit Freiheitsstrafe bis zu fünf Jahren oder mit Geldstra...

#### ours-cohere — Top 3
- **[Judge=3]** `§ 249 StGB` — Behandelt direkt Raub § 249 vs Diebstahl § 242
  > NStZ 2023, 351). Danach ist § 249 gegenüber § 255 ein spezielles Delikt; in jedem Raub liegt eine räuberische Erpressung (aA die hM in der Literatur). Die Unterscheidung richtet sich nach dem äußeren ...
- **[Judge=3]** `§ 249 StGB – BT. Zwanzigster Abschnitt – Rn. 15` — Direkt relevant: subjektive Tatbestandsmerkmale bei Raub vs Diebstahl
  > G. Subjektiver Tatbestand. Der Vorsatz muss entsprechend der Doppelnatur des Raubs sowohl Wegnahme (vgl. dazu → § 242 Rn. 29 ff.) als auch Nötigung (→ § 240 Rn. 53 f.) sowie deren Verknüpfung umfassen...
- **[Judge=3]** `§ 241a StGB – BT. Achtzchniter Abschnitt – Rn. 242` — Direkt relevant: definiert Diebstahl-Tatbestand vollständig
  > 242 (1) Wer eine fremde bewegliche Sache einem anderen in der Absicht wegnimmt, die Sache sich oder einem Dritten rechtswidrig zuzueignen, wird mit Freiheitsstrafe bis zu fünf Jahren oder mit Geldstra...

### q18 — cross-reference

**Query:** Wann wird Betrug zu Computerbetrug und umgekehrt?

**Kontext:** § 263 vs § 263a StGB — Abgrenzung bei elektronischer Datenverarbeitung

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours | 0.82 | 60% | 67% | 1 | 5.4s |
| ours-cohere | 0.94 | 20% | 33% | 3 | 7.0s |

#### ours — Top 3
- **[Judge=1]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 62` — Betrug allgemein, aber nicht Abgrenzung zu Computerbetrug
  > Die Kausalität der Täuschung für den Irrtum und dessen Kausalität für die Vermögensverfügung müssen im Einzelfall festgestellt sein. Mitverursachung reicht aus. Dabei darf das Gericht auch bei Serien-...
- **[Judge=2]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 14` — Täuschungshandlung bei Betrug, aber nicht spezifisch 263a
  > Rspr. und hM bejahen darüber hinaus aber die Möglichkeit einer Täuschung durch Unterlassen auch ohne Erklärung gegenüber dem Irrenden (→ Rn. 38; vgl. BGHSt 39, 392 (398); BayObLG NJW 1987, 1654 (mAnm ...
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 58` — Direkte Abgrenzung § 263/263a bei automatisierten Verfahren
  > 58 Im Geschäftsverkehr wird sich, wer die Berechtigung eines Leistungsverlangens oder -auftrags nicht zu prüfen hat, hierüber idR auch keine (richtigen oder falschen) Gedanken machen (NStZ 1997, 281; ...

#### ours-cohere — Top 3
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 58` — Direkte Abgrenzung § 263/§ 263a bei automatisierten Verfahren
  > 58 Im Geschäftsverkehr wird sich, wer die Berechtigung eines Leistungsverlangens oder -auftrags nicht zu prüfen hat, hierüber idR auch keine (richtigen oder falschen) Gedanken machen (NStZ 1997, 281; ...
- **[Judge=0]** `§ 263 StGB – BT. Zweriindzwanzigster Abschnitt – Rn. 234` — Behandelt Handlungseinheit/Tatmehrheit, nicht Betrug vs Computerbetrug
  > 234 II. Handlungseinheit. Wenn eine Mehrheit von Tathandlungen durch einen gemeinsamen Vorsatz verbunden sind und ein unmittelbarer zeitlicher und räumlicher Zusammenhang besteht, liegt nur eine Tat i...
- **[Judge=1]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 263 (Tei` — Literaturverzeichnis zu Betrug, keine Abgrenzung zu Computerbetrug
  > Fischer/Lutz    Betrug und Untreue   schende Warnung": Eine Drohung?, FS Puppe, 2011, 1217; Kupper, Mengenbegriffe im Strafgesetzbuch, FS Kohlmann, 2003, 133; Lampe, Personales Unrecht im Betrug, FS O...