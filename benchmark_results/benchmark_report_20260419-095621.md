# RAG Benchmark Report

_Generiert: 2026-04-19T09:56:21_


- Queries: **18**
- Top-K: **5**
- Systeme: ours-api, ours-mxbai-voyage

## Gesamtvergleich

| Metrik | ours-api | ours-mxbai-voyage |
|--------|--------|--------|
| nDCG@10 | 0.971 | 0.985 |
| Relevance@10 | 91.1% | 94.4% |
| Relevance@3 | 90.7% | 98.1% |
| Top-1-Score | 2.78 | 2.94 |
| Mean-Score | 2.56 | 2.68 |
| Latenz (s) | 6.89 | 5.54 |

## Nach Kategorie


### alltagssprache

| Metrik | ours-api | ours-mxbai-voyage |
|--------|--------|--------|
| nDCG@10 | 0.990 | 0.993 |
| Relevance@10 | 100.0% | 100.0% |
| Relevance@3 | 100.0% | 100.0% |

### cross-reference

| Metrik | ours-api | ours-mxbai-voyage |
|--------|--------|--------|
| nDCG@10 | 0.904 | 0.985 |
| Relevance@10 | 80.0% | 100.0% |
| Relevance@3 | 66.7% | 100.0% |

### exakte-paragraphen

| Metrik | ours-api | ours-mxbai-voyage |
|--------|--------|--------|
| nDCG@10 | 0.989 | 0.987 |
| Relevance@10 | 95.0% | 100.0% |
| Relevance@3 | 91.7% | 100.0% |

### konzept

| Metrik | ours-api | ours-mxbai-voyage |
|--------|--------|--------|
| nDCG@10 | 0.986 | 0.994 |
| Relevance@10 | 90.0% | 85.0% |
| Relevance@3 | 100.0% | 100.0% |

### stpo-prozess

| Metrik | ours-api | ours-mxbai-voyage |
|--------|--------|--------|
| nDCG@10 | 0.967 | 0.962 |
| Relevance@10 | 86.7% | 86.7% |
| Relevance@3 | 88.9% | 88.9% |

## Detail pro Query


### q01 — exakte-paragraphen

**Query:** Welche Voraussetzungen hat der gewerbsmaessige Bandenbetrug nach § 263 Abs. 5 StGB?

**Kontext:** Qualifikationstatbestand des Bandenbetrugs im Fischer-Kommentar

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours-mxbai-voyage | 1.00 | 100% | 100% | 3 | 5.6s |
| ours-api | 1.00 | 100% | 100% | 3 | 20.5s |

#### ours-mxbai-voyage — Top 3
- **[Judge=3]** `§ 263 StGB – I. Vermögensbegriff  – Rn. 263` — Enthält direkt § 263 Abs. 5 Voraussetzungen
  > 263 (1) Wer in der Absicht, sich oder einem Dritten einen rechtswidrigen Vermögensvorteil zu verschaffen, das Vermögen eines anderen dadurch beschädigt, daß er durch Vorspiegelung falscher oder durch ...
- **[Judge=3]** `§ 263 StGB – BT. Zweriindzwanzigster Abschnitt – Rn. 225` — Erklärt direkt alle Voraussetzungen des § 263 Abs. 5
  > IV. Qualifikation (Abs. 5). Abs. 5 enthält einen Qualifikationstatbestand, der die Tat in Fällen kumulativ gewerbs- und bandenmäßiger Begehung zum Verbrechen macht. Die Qualifikation ist in die Urteil...
- **[Judge=3]** `§ 263 StGB – BT. Zweijundzwanzigster Abschnitt – Rn. 213` — Erklaert direkt Abgrenzung und Voraussetzungen Bandenbetrug
  > 213 Sind beide Varianten erfüllt, ist eine Qualifikation nach Abs. 5 gegeben. Die Abgrenzung des Abs. 3 Nr. 1 zum Verbrechen nach Abs. 5 ist in Fällen bandenmäßiger Begehung schwierig, denn eine auf f...

#### ours-api — Top 3
- **[Judge=3]** `§ 263 StGB – I. Vermögensbegriff  – Rn. 263` — Enthält vollständigen Wortlaut von § 263 Abs. 5 StGB
  > 263 (1) Wer in der Absicht, sich oder einem Dritten einen rechtswidrigen Vermögensvorteil zu verschaffen, das Vermögen eines anderen dadurch beschädigt, daß er durch Vorspiegelung falscher oder durch ...
- **[Judge=3]** `§ 263 StGB – BT. Zweriindzwanzigster Abschnitt – Rn. 225` — Direkt relevant: erklärt Voraussetzungen des § 263 Abs. 5
  > IV. Qualifikation (Abs. 5). Abs. 5 enthält einen Qualifikationstatbestand, der die Tat in Fällen kumulativ gewerbs- und bandenmäßiger Begehung zum Verbrechen macht. Die Qualifikation ist in die Urteil...
- **[Judge=3]** `§ 263 StGB – BT. Zweijundzwanzigster Abschnitt – Rn. 213` — Direkt relevant: behandelt gewerbsmäßigen Bandenbetrug § 263 Abs. 5
  > 213 Sind beide Varianten erfüllt, ist eine Qualifikation nach Abs. 5 gegeben. Die Abgrenzung des Abs. 3 Nr. 1 zum Verbrechen nach Abs. 5 ist in Fällen bandenmäßiger Begehung schwierig, denn eine auf f...

### q02 — exakte-paragraphen

**Query:** Was regelt § 112 StPO zur Untersuchungshaft?

**Kontext:** Anordnungsvoraussetzungen der U-Haft (dringender Tatverdacht, Haftgrund) im Schmitt/Koehler

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours-mxbai-voyage | 0.99 | 100% | 100% | 3 | 4.7s |
| ours-api | 1.00 | 100% | 100% | 3 | 5.7s |

#### ours-mxbai-voyage — Top 3
- **[Judge=3]** `§ 112 StPO – Rn. 112` — Direkt relevant: § 112 StPO Volltext zu Untersuchungshaft
  > 112 (1) ¹ Die Untersuchungshaft darf gegen den Beschuldigten angeordnet werden, wenn er der Tat dringend verdächtig ist und ein Haftgrund besteht. ² Sie darf nicht angeordnet werden, wenn sie zu der B...
- **[Judge=3]** `§ 112 StPO – III. Flucht (Abs – Rn. 23` — Direkt relevant zu § 112 StPO Haftgründen
  > Bei einer besonders hohen Straferwartung braucht daher nur geprüft zu werden, ob Umstände vorhanden sind, die die hieraus herzuleitende Fluchtgefahr ausräumen können (KG StV 1996, 383; OLG München Str...
- **[Judge=2]** `§ 112 StPO – Rn. 112` — Behandelt Haftbefehlsvoraussetzungen, aber nicht § 112 direkt
  > Haftunfähigkeit des Beschuldigten schließt den Erlass des Haftbefehls nicht aus, sondern hindert nur seinen Vollzug (OLG Düsseldorf JZ 1984, 248; OLG Frankfurt a.M. NJW 1968, 2302; OLG Nürnberg OLGSt ...

#### ours-api — Top 3
- **[Judge=3]** `§ 112 StPO – Rn. 112` — Direkt relevant: Gesetzestext und Gliederung zu § 112 StPO
  > 112 (1) ¹ Die Untersuchungshaft darf gegen den Beschuldigten angeordnet werden, wenn er der Tat dringend verdächtig ist und ein Haftgrund besteht. ² Sie darf nicht angeordnet werden, wenn sie zu der B...
- **[Judge=3]** `§ 112 StPO – III. Flucht (Abs – Rn. 23` — Behandelt direkt Haftgruende des § 112 StPO
  > Bei einer besonders hohen Straferwartung braucht daher nur geprüft zu werden, ob Umstände vorhanden sind, die die hieraus herzuleitende Fluchtgefahr ausräumen können (KG StV 1996, 383; OLG München Str...
- **[Judge=3]** `§ 112 StPO – III. Flucht (Abs – Rn. 32 (Teil 2)` — Direkt relevant zu Verdunkelungsgefahr als Haftgrund nach § 112 StPO
  > Wenn die Verdunkelungshandlungen nicht geeignet sind, die Ermittlung der Wahrheit zu erschweren, darf UHaft nicht angeordnet werden. Der Haftgrund liegt daher nicht vor, wenn der Sachverhalt schon in ...

### q03 — exakte-paragraphen

**Query:** Welche Haftgruende nennt § 112 Abs. 2 StPO?

**Kontext:** Fluchtgefahr, Verdunkelungsgefahr, Flucht — im StPO-Kommentar

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours-mxbai-voyage | 1.00 | 100% | 100% | 3 | 4.8s |
| ours-api | 1.00 | 100% | 100% | 3 | 5.6s |

#### ours-mxbai-voyage — Top 3
- **[Judge=3]** `§ 112 StPO – Rn. 112` — Nennt direkt alle Haftgruende des § 112 Abs. 2 StPO
  > 112 (1) ¹ Die Untersuchungshaft darf gegen den Beschuldigten angeordnet werden, wenn er der Tat dringend verdächtig ist und ein Haftgrund besteht. ² Sie darf nicht angeordnet werden, wenn sie zu der B...
- **[Judge=3]** `§ 112 StPO – III. Flucht (Abs – Rn. 23` — Behandelt direkt § 112 Abs. 2 StPO Haftgründe
  > Bei einer besonders hohen Straferwartung braucht daher nur geprüft zu werden, ob Umstände vorhanden sind, die die hieraus herzuleitende Fluchtgefahr ausräumen können (KG StV 1996, 383; OLG München Str...
- **[Judge=3]** `§ 112 StPO – III. Flucht (Abs – Rn. 17 (Teil 1)` — Behandelt direkt Fluchtgefahr aus § 112 Abs. 2 StPO
  > 17 IV. Fluchtgefahr (Abs. 2 Nr. 2). Fluchtgefahr (Abs. 2 Nr. 2) besteht, wenn die Würdigung der Umstände des Falles es wahrscheinlicher macht, dass sich der Beschuldigte dem Strafverfahren entziehen, ...

#### ours-api — Top 3
- **[Judge=3]** `§ 112 StPO – Rn. 112` — Direkter Volltext von § 112 Abs. 2 StPO
  > 112 (1) ¹ Die Untersuchungshaft darf gegen den Beschuldigten angeordnet werden, wenn er der Tat dringend verdächtig ist und ein Haftgrund besteht. ² Sie darf nicht angeordnet werden, wenn sie zu der B...
- **[Judge=3]** `§ 112 StPO – III. Flucht (Abs – Rn. 23` — Definiert direkt Verdunkelungsgefahr nach § 112 Abs. 2 Nr. 3
  > Bei einer besonders hohen Straferwartung braucht daher nur geprüft zu werden, ob Umstände vorhanden sind, die die hieraus herzuleitende Fluchtgefahr ausräumen können (KG StV 1996, 383; OLG München Str...
- **[Judge=3]** `§ 112 StPO – III. Flucht (Abs – Rn. 17 (Teil 1)` — Behandelt direkt Fluchtgefahr nach § 112 Abs. 2 Nr. 2
  > 17 IV. Fluchtgefahr (Abs. 2 Nr. 2). Fluchtgefahr (Abs. 2 Nr. 2) besteht, wenn die Würdigung der Umstände des Falles es wahrscheinlicher macht, dass sich der Beschuldigte dem Strafverfahren entziehen, ...

### q04 — exakte-paragraphen

**Query:** Was regelt § 102 StPO zur Durchsuchung beim Beschuldigten?

**Kontext:** Durchsuchungsvoraussetzungen beim Verdaechtigen

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours-mxbai-voyage | 0.96 | 100% | 100% | 3 | 4.7s |
| ours-api | 0.96 | 80% | 67% | 3 | 5.1s |

#### ours-mxbai-voyage — Top 3
- **[Judge=3]** `§ 102 StPO – Rn. 102` — Definiert direkt § 102 StPO und dessen Voraussetzungen
  > 102 Bei dem, welcher als Täter oder Teilnehmer einer Straftat oder der Datenhehlerei, Begünstigung, Strafvereitelung oder Hehlerei  Köhler    Ermittlungsmaßnahmen  verdächtig ist, kann eine Durchsuchu...
- **[Judge=2]** `§ 102 StPO – Rn. 10` — Thematisch relevant, behandelt Durchsuchungsvoraussetzungen allgemein
  > II. Auffinden von Beweismitteln. Zu den Beweismitteln (→ § 94 Rn. 4 ff.) gehören auch die nur in § 103 erwähnten Spuren (SK-StPO/Jäger/Wohlers Rn. 21) u. Personen, die zu Beweiszwecken in Augenschein ...
- **[Judge=2]** `§ 102 StPO – Rn. 10` — Durchsuchung allgemein, aber nicht spezifisch § 102
  > Kohler     Erstes Buch. Achter Abschnitt  Aufklärung bislang ungeklärter Fälle“ einer Tatserie beitragen könne, scheint dies den besonderen Umständen des Einzelfalls geschuldet zu sein. Denn zum einen...

#### ours-api — Top 3
- **[Judge=3]** `§ 102 StPO – Rn. 102` — Direkter Wortlaut § 102 StPO mit Durchsuchungsvoraussetzungen
  > 102 Bei dem, welcher als Täter oder Teilnehmer einer Straftat oder der Datenhehlerei, Begünstigung, Strafvereitelung oder Hehlerei  Köhler    Ermittlungsmaßnahmen  verdächtig ist, kann eine Durchsuchu...
- **[Judge=2]** `§ 102 StPO – Rn. 10` — Behandelt Durchsuchungsvoraussetzungen, aber nicht speziell § 102
  > II. Auffinden von Beweismitteln. Zu den Beweismitteln (→ § 94 Rn. 4 ff.) gehören auch die nur in § 103 erwähnten Spuren (SK-StPO/Jäger/Wohlers Rn. 21) u. Personen, die zu Beweiszwecken in Augenschein ...
- **[Judge=1]** `§ 102 StPO – Rn. 10` — Behandelt allgemeine Durchsuchungsvoraussetzungen, nicht spezifisch § 102
  > Kohler     Erstes Buch. Achter Abschnitt  Aufklärung bislang ungeklärter Fälle“ einer Tatserie beitragen könne, scheint dies den besonderen Umständen des Einzelfalls geschuldet zu sein. Denn zum einen...

### q05 — konzept

**Query:** Wann liegt eine konkludente Taeuschung im Sinne des § 263 StGB vor?

**Kontext:** Taeuschungshandlung durch schluessiges Verhalten

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours-mxbai-voyage | 0.99 | 100% | 100% | 3 | 5.5s |
| ours-api | 0.98 | 80% | 100% | 3 | 5.9s |

#### ours-mxbai-voyage — Top 3
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 21` — Definiert konkludente Taeuschung bei § 263 StGB direkt
  > 21 2. Konkludente Erklärungen. Auch durch eine schlüssige Handlung (konkludente Erklärung) kann vorspiegelt werden. Eine solche konkludente Erklärung durch aktives Tun ist von einer Erklärung durch Un...
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 14` — Direkt relevant: behandelt konkludente Tatsachenbehauptungen bei Täuschung
  > 14 II. Tathandlung. Der Begriff „Täuschen“ ist im Wortlaut des Abs. 1 nicht verwendet; er ergibt sich aus dem Zusammenhang zwischen der Beschreibung der Tathandlung (→ Rn. 18) und dem Irrtum als ihrem...
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 14` — Direkt relevant: behandelt konkludente Taeuschung bei § 263
  > Rspr. und hM bejahen darüber hinaus aber die Möglichkeit einer Täuschung durch Unterlassen auch ohne Erklärung gegenüber dem Irrenden (→ Rn. 38; vgl. BGHSt 39, 392 (398); BayObLG NJW 1987, 1654 (mAnm ...

#### ours-api — Top 3
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 14` — Definiert konkludente Täuschung bei § 263 StGB direkt
  > Rspr. und hM bejahen darüber hinaus aber die Möglichkeit einer Täuschung durch Unterlassen auch ohne Erklärung gegenüber dem Irrenden (→ Rn. 38; vgl. BGHSt 39, 392 (398); BayObLG NJW 1987, 1654 (mAnm ...
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 21` — Direkt relevant: definiert konkludente Taeuschung bei § 263
  > 21 2. Konkludente Erklärungen. Auch durch eine schlüssige Handlung (konkludente Erklärung) kann vorspiegelt werden. Eine solche konkludente Erklärung durch aktives Tun ist von einer Erklärung durch Un...
- **[Judge=2]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 38` — Behandelt Betrug § 263, aber fokussiert Unterlassen statt Konkludenz
  > 38 4. Täuschung durch Unterlassen. Eine Täuschung kann nach hM (aA Grünwald FS H. Mayer, 1966, 281; Kargl ZStW 119 (2007), 250 (287) mwN) auch durch Unterlassen begangen werden, wenn eine Garantenpfli...

### q06 — konzept

**Query:** Was ist eine Vermoegensverfuegung und welche Anforderungen stellt die Rechtsprechung?

**Kontext:** Tatbestandsmerkmal der Vermoegensverfuegung beim Betrug

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours-mxbai-voyage | 0.99 | 80% | 100% | 3 | 5.3s |
| ours-api | 0.99 | 100% | 100% | 3 | 6.3s |

#### ours-mxbai-voyage — Top 3
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 76` — Direkt relevant zur Vermoegensverfuegung beim Betrug
  > 76 3. Unmittelbarkeit der Verfügung. Neben der Freiwilligkeit ist das Merkmal der Unmittelbarkeit nach stRspr und hM das wichtigste Kriterium zur Beschränkung der § 263 unterfallenden Selbstschädigung...
- **[Judge=3]** `§ 263 StGB – BT. Zweitundzwanzigster Abschnitt – Rn. 69` — Definiert Vermoegensverfuegung als ungeschriebenes Tatbestandsmerkmal beim Betrug
  > 69 Anders ist es, wenn der Verfügende seinerseits nur (gutgläubige) Hilfsperson eines bösgläubigen Dritten ist. Hier ist auf den Irrtum des Entscheidungsbefugten abzustellen: Erkennt dieser die Unrich...
- **[Judge=2]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 87` — Behandelt Kausalität und Schaden, nicht Verfügungsdefinition
  > 87 5. Kausalität. Für die Vermögensverfügung muss der täuschungsbedingte Irrtum kausal sein (vgl. BGHSt 24, 257 (260); 24, 386 (389); NStZ 2003, 313 (314 f.); OLG Düsseldorf NJW 1987, 3145); Mitverurs...

#### ours-api — Top 3
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 76` — Direkt relevant: Definition und Unmittelbarkeitskriterium der Vermoegensverfuegung
  > 76 3. Unmittelbarkeit der Verfügung. Neben der Freiwilligkeit ist das Merkmal der Unmittelbarkeit nach stRspr und hM das wichtigste Kriterium zur Beschränkung der § 263 unterfallenden Selbstschädigung...
- **[Judge=3]** `§ 263 StGB – BT. Zweitundzwanzigster Abschnitt – Rn. 69` — Definiert direkt Vermoegensverfuegung und enthält Rechtsprechungsanforderungen
  > 69 Anders ist es, wenn der Verfügende seinerseits nur (gutgläubige) Hilfsperson eines bösgläubigen Dritten ist. Hier ist auf den Irrtum des Entscheidungsbefugten abzustellen: Erkennt dieser die Unrich...
- **[Judge=2]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 87` — Behandelt Kausalität und Vermögensschadens-Kontext, aber nicht Vermögensverfügungsdefinition
  > 87 5. Kausalität. Für die Vermögensverfügung muss der täuschungsbedingte Irrtum kausal sein (vgl. BGHSt 24, 257 (260); 24, 386 (389); NStZ 2003, 313 (314 f.); OLG Düsseldorf NJW 1987, 3145); Mitverurs...

### q07 — konzept

**Query:** Was versteht man unter einem Gefaehrdungsschaden beim Betrug?

**Kontext:** Schadensbegriff, schadensgleiche Vermoegensgefaehrdung

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours-mxbai-voyage | 0.99 | 80% | 100% | 3 | 5.4s |
| ours-api | 1.00 | 100% | 100% | 3 | 5.9s |

#### ours-mxbai-voyage — Top 3
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 159` — Definiert direkt Gefährdungsschaden beim Betrug
  > 159 b) Voraussetzungen. aa) Ein Gefährdungsschaden ist gegeben, wenn die Wahrscheinlichkeit des endgültigen Verlusts eines Vermögensbestandteils zum Zeitpunkt der täuschungsbedingten Verfügung so groß...
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 171` — Definiert direkt Gefährdungsschaden beim Betrug mit Beispielen
  > Die täuschungsbedingte Herausgabe von EC-Karten, Kreditkarten und weiteren Zugangsdaten zu Bank-Guthaben (PINs, TANs; Passwörter), sei es infolge persönlicher Täuschung oder von „Phishing“-Manipulatio...
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 163` — Direkt relevant: Definition und Beispiele für Gefährdungsschäden
  > 163 c) Einzelfälle. Gefährdungsschäden sind zB bejaht worden in folgenden Fällen: BGHSt 3, 371 (373) (Erwerb eines unsicheren Pfandrechts); BGHSt 15, 83 (87 f.); wistra 2003, 230 (Prozessrisiko bei gu...

#### ours-api — Top 3
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 159` — Definiert direkt Gefaehrdungsschaden beim Betrug
  > 159 b) Voraussetzungen. aa) Ein Gefährdungsschaden ist gegeben, wenn die Wahrscheinlichkeit des endgültigen Verlusts eines Vermögensbestandteils zum Zeitpunkt der täuschungsbedingten Verfügung so groß...
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 171` — Definiert direkt Gefährdungsschaden beim Betrug
  > Die täuschungsbedingte Herausgabe von EC-Karten, Kreditkarten und weiteren Zugangsdaten zu Bank-Guthaben (PINs, TANs; Passwörter), sei es infolge persönlicher Täuschung oder von „Phishing“-Manipulatio...
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 109` — Direkt relevant: erwähnt explizit Gefährdungsschaden und Schadensermittlung
  > VI. Schaden. Vermögensschaden ist ein negativer Saldo zwischen dem Wert des Vermögens vor und nach der irrtumsbedingten Vermögensverfügung des Getäuschten (Prinzip der Gesamtsaldierung; stRspr; vgl. B...

### q08 — konzept

**Query:** Wie wird der Vorsatz beim Betrug bestimmt, insbesondere die Bereicherungsabsicht?

**Kontext:** Subjektiver Tatbestand § 263 StGB

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours-mxbai-voyage | 1.00 | 80% | 100% | 3 | 5.8s |
| ours-api | 0.97 | 80% | 100% | 3 | 5.8s |

#### ours-mxbai-voyage — Top 3
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 176` — Direkt relevant: behandelt Vorsatz und Bereicherungsabsicht bei Betrug
  > D. Subjektiver Tatbestand. § 263 setzt Vorsatz voraus; darüber hinaus ist die Absicht rechtswidriger Bereicherung erforderlich.   I. Vorsatz. 1. Täuschungsvorsatz. Der Vorsatz (bedingter Vorsatz genüg...
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 186` — Direkt relevant: erklärt Bereicherungsabsicht bei § 263 StGB
  > 186 II. Bereicherungsabsicht. Die Tat muss subjektiv auf die Erlangung eines rechtswidrigen Vermögensvorteils für den Täuschenden oder einen Dritten gerichtet sein. Vermögensvorteil ist die Erhöhung d...
- **[Judge=3]** `§ 263 StGB – BT. Zweijundzwanzigster Abschnitt – Rn. 194` — Direkt relevant: behandelt Vorsatz bei Bereicherungsabsicht
  > 194 4. Vorsatz hinsichtlich der Rechtswidrigkeit. Die Rechtswidrigkeit des angestrebten Vermögensvorteils muss vom Vorsatz umfasst sein; sie ist wie bei § 253 (vgl. dort 20) subjektives Tatbestandsmer...

#### ours-api — Top 3
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 176` — Direkt relevant: behandelt Vorsatz und Bereicherungsabsicht bei Betrug
  > D. Subjektiver Tatbestand. § 263 setzt Vorsatz voraus; darüber hinaus ist die Absicht rechtswidriger Bereicherung erforderlich.   I. Vorsatz. 1. Täuschungsvorsatz. Der Vorsatz (bedingter Vorsatz genüg...
- **[Judge=2]** `§ 263 StGB – I. Vermögensbegriff  – Rn. 263` — Enthält Bereicherungsabsicht-Tatbestand, aber keine Vorsatzbestimmung
  > 263 (1) Wer in der Absicht, sich oder einem Dritten einen rechtswidrigen Vermögensvorteil zu verschaffen, das Vermögen eines anderen dadurch beschädigt, daß er durch Vorspiegelung falscher oder durch ...
- **[Judge=3]** `§ 263 StGB – BT. Zweijundzwanzigster Abschnitt – Rn. 194` — Direkt relevant für Vorsatz bei Bereicherungsabsicht
  > 194 4. Vorsatz hinsichtlich der Rechtswidrigkeit. Die Rechtswidrigkeit des angestrebten Vermögensvorteils muss vom Vorsatz umfasst sein; sie ist wie bei § 253 (vgl. dort 20) subjektives Tatbestandsmer...

### q09 — alltagssprache

**Query:** Hat der Angeklagte die Kunden über das Internet betrogen?

**Kontext:** Abstrakte Frage zu Internetbetrug, sucht Taeuschungshandlung + Schaden

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours-mxbai-voyage | 1.00 | 100% | 100% | 3 | 5.1s |
| ours-api | 0.99 | 100% | 100% | 3 | 7.1s |

#### ours-mxbai-voyage — Top 3
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 171` — Behandelt direkt Internetbetrug durch Phishing-Manipulationen
  > Die täuschungsbedingte Herausgabe von EC-Karten, Kreditkarten und weiteren Zugangsdaten zu Bank-Guthaben (PINs, TANs; Passwörter), sei es infolge persönlicher Täuschung oder von „Phishing“-Manipulatio...
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 28` — Direkt relevant: Täuschungshandlungen bei Internetbetrug
  > 28 Solche Scheinrechnungen sind so formuliert, dass sie bei eiligen oder geschäftsunerfahrenen Empfängern den Eindruck der Zahlungspflicht zu erzeugen geeignet sind (vgl. auch Erb ZIS 2011, 354: „Sugg...
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 28` — Direkt relevant: Internetbetrug, Täuschung, konkrete Fallgruppen
  > In Fällen sog. „Kostenfallen“ im Internet (vgl. dazu Eisele NStZ 2010, 193), bei denen unerfahrene Verbraucher durch (wahre) Versprechen besonders günstiger Angebote zum Abschluss von Verträgen gebrac...

#### ours-api — Top 3
- **[Judge=3]** `§ 263 StGB – I. Vermögensbegriff  – Rn. 263` — Betrug-Tatbestand direkt relevant für Internetbetrug
  > 263 (1) Wer in der Absicht, sich oder einem Dritten einen rechtswidrigen Vermögensvorteil zu verschaffen, das Vermögen eines anderen dadurch beschädigt, daß er durch Vorspiegelung falscher oder durch ...
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 5` — Direkt relevant: zentrale Tatbestandsmerkmale des Betrugs
  > 5 C. Grundtatbestand, Abs. 1. Tathandlung ist das Täuschen einer natürlichen Person (vgl. NStZ 2005, 213) über Tatsachen. Erfolg dieser Handlung muss ein Irrtum des Täuschungsadressaten sein; dieser m...
- **[Judge=2]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 176` — Subjektiver Tatbestand bei Betrug, thematisch relevant
  > D. Subjektiver Tatbestand. § 263 setzt Vorsatz voraus; darüber hinaus ist die Absicht rechtswidriger Bereicherung erforderlich.   I. Vorsatz. 1. Täuschungsvorsatz. Der Vorsatz (bedingter Vorsatz genüg...

### q10 — alltagssprache

**Query:** Wann darf die Polizei bei jemandem zu Hause suchen?

**Kontext:** Durchsuchungsvoraussetzungen, §§ 102 ff. StPO

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours-mxbai-voyage | 0.97 | 100% | 100% | 3 | 5.7s |
| ours-api | 0.97 | 100% | 100% | 3 | 6.4s |

#### ours-mxbai-voyage — Top 3
- **[Judge=3]** `§ 102 StPO – Rn. 102` — Beantwortet direkt Durchsuchungsvoraussetzungen der Wohnung
  > 102 Bei dem, welcher als Täter oder Teilnehmer einer Straftat oder der Datenhehlerei, Begünstigung, Strafvereitelung oder Hehlerei  Köhler    Ermittlungsmaßnahmen  verdächtig ist, kann eine Durchsuchu...
- **[Judge=2]** `§ 102 StPO – Rn. 10` — Behandelt Durchsuchungsvoraussetzungen, aber fokussiert auf Beweismittel
  > II. Auffinden von Beweismitteln. Zu den Beweismitteln (→ § 94 Rn. 4 ff.) gehören auch die nur in § 103 erwähnten Spuren (SK-StPO/Jäger/Wohlers Rn. 21) u. Personen, die zu Beweiszwecken in Augenschein ...
- **[Judge=2]** `§ 102 StPO – Rn. 3` — Behandelt Durchsuchungsvoraussetzungen, aber spezifische Aspekte
  > **Teilnehmer** nach §§ 25 ff. StGB, nicht die sog. notwendigen Teilnehmer (zum Begriff: Fischer/Fischer StGB Vor § 25 Rn. 7), stehen den Tatverdächtigen gleich. Bei jedem v. ihnen sowie bei den der Be...

#### ours-api — Top 3
- **[Judge=3]** `§ 102 StPO – Rn. 102` — Direkt relevant: § 102 StPO Durchsuchungsvoraussetzungen
  > 102 Bei dem, welcher als Täter oder Teilnehmer einer Straftat oder der Datenhehlerei, Begünstigung, Strafvereitelung oder Hehlerei  Köhler    Ermittlungsmaßnahmen  verdächtig ist, kann eine Durchsuchu...
- **[Judge=2]** `§ 102 StPO – Rn. 10` — Behandelt Durchsuchungsvoraussetzungen, aber nicht direkt Wohnungsdurchsuchungen
  > II. Auffinden von Beweismitteln. Zu den Beweismitteln (→ § 94 Rn. 4 ff.) gehören auch die nur in § 103 erwähnten Spuren (SK-StPO/Jäger/Wohlers Rn. 21) u. Personen, die zu Beweiszwecken in Augenschein ...
- **[Judge=2]** `§ 102 StPO – Rn. 3` — Behandelt Durchsuchung, aber nicht grundlegende Voraussetzungen
  > **Teilnehmer** nach §§ 25 ff. StGB, nicht die sog. notwendigen Teilnehmer (zum Begriff: Fischer/Fischer StGB Vor § 25 Rn. 7), stehen den Tatverdächtigen gleich. Bei jedem v. ihnen sowie bei den der Be...

### q11 — alltagssprache

**Query:** Was passiert wenn jemand luegt damit er Geld bekommt?

**Kontext:** Laienhafte Umschreibung des Betrugstatbestandes

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours-mxbai-voyage | 1.00 | 100% | 100% | 3 | 5.1s |
| ours-api | 1.00 | 100% | 100% | 3 | 6.3s |

#### ours-mxbai-voyage — Top 3
- **[Judge=3]** `§ 263 StGB – I. Vermögensbegriff  – Rn. 263` — Direkt relevant: definiert Betrug durch Täuschung
  > 263 (1) Wer in der Absicht, sich oder einem Dritten einen rechtswidrigen Vermögensvorteil zu verschaffen, das Vermögen eines anderen dadurch beschädigt, daß er durch Vorspiegelung falscher oder durch ...
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 5` — Direkt relevanter Betrugstatbestand - Täuschung für Vermögensvorteil
  > 5 C. Grundtatbestand, Abs. 1. Tathandlung ist das Täuschen einer natürlichen Person (vgl. NStZ 2005, 213) über Tatsachen. Erfolg dieser Handlung muss ein Irrtum des Täuschungsadressaten sein; dieser m...
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 176` — Erklärt subjektiven Tatbestand des Betrugs direkt
  > D. Subjektiver Tatbestand. § 263 setzt Vorsatz voraus; darüber hinaus ist die Absicht rechtswidriger Bereicherung erforderlich.   I. Vorsatz. 1. Täuschungsvorsatz. Der Vorsatz (bedingter Vorsatz genüg...

#### ours-api — Top 3
- **[Judge=3]** `§ 263 StGB – I. Vermögensbegriff  – Rn. 263` — Betrug § 263: direkte Antwort auf Lügen für Geld
  > 263 (1) Wer in der Absicht, sich oder einem Dritten einen rechtswidrigen Vermögensvorteil zu verschaffen, das Vermögen eines anderen dadurch beschädigt, daß er durch Vorspiegelung falscher oder durch ...
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 5` — Definiert direkt Betrug durch Täuschung für Vermögensvorteil
  > 5 C. Grundtatbestand, Abs. 1. Tathandlung ist das Täuschen einer natürlichen Person (vgl. NStZ 2005, 213) über Tatsachen. Erfolg dieser Handlung muss ein Irrtum des Täuschungsadressaten sein; dieser m...
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 176` — Erklärt subjektiven Tatbestand bei Betrug durch Täuschung
  > D. Subjektiver Tatbestand. § 263 setzt Vorsatz voraus; darüber hinaus ist die Absicht rechtswidriger Bereicherung erforderlich.   I. Vorsatz. 1. Täuschungsvorsatz. Der Vorsatz (bedingter Vorsatz genüg...

### q12 — alltagssprache

**Query:** Wann muss jemand ins Gefaengnis waehrend die Tat noch nicht bewiesen ist?

**Kontext:** Untersuchungshaft, §§ 112 ff. StPO

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours-mxbai-voyage | 1.00 | 100% | 100% | 3 | 5.3s |
| ours-api | 1.00 | 100% | 100% | 3 | 5.7s |

#### ours-mxbai-voyage — Top 3
- **[Judge=3]** `§ 112 StPO – Rn. 112` — Direkt relevant: § 112 StPO regelt Untersuchungshaft
  > 112 (1) ¹ Die Untersuchungshaft darf gegen den Beschuldigten angeordnet werden, wenn er der Tat dringend verdächtig ist und ein Haftgrund besteht. ² Sie darf nicht angeordnet werden, wenn sie zu der B...
- **[Judge=3]** `§ 112 StPO – III. Flucht (Abs – Rn. 23` — Direkt relevant: Verdunkelungsgefahr als Haftgrund nach StPO
  > Bei einer besonders hohen Straferwartung braucht daher nur geprüft zu werden, ob Umstände vorhanden sind, die die hieraus herzuleitende Fluchtgefahr ausräumen können (KG StV 1996, 383; OLG München Str...
- **[Judge=3]** `§ 112 StPO – Rn. 112` — Direkt relevant: definiert dringenden Tatverdacht für Untersuchungshaft
  > Haftunfähigkeit des Beschuldigten schließt den Erlass des Haftbefehls nicht aus, sondern hindert nur seinen Vollzug (OLG Düsseldorf JZ 1984, 248; OLG Frankfurt a.M. NJW 1968, 2302; OLG Nürnberg OLGSt ...

#### ours-api — Top 3
- **[Judge=3]** `§ 112 StPO – Rn. 112` — Direkt relevant: regelt Untersuchungshaft vor Urteil
  > 112 (1) ¹ Die Untersuchungshaft darf gegen den Beschuldigten angeordnet werden, wenn er der Tat dringend verdächtig ist und ein Haftgrund besteht. ² Sie darf nicht angeordnet werden, wenn sie zu der B...
- **[Judge=3]** `§ 112 StPO – III. Flucht (Abs – Rn. 23` — Direkt relevant: Haftgruende bei Untersuchungshaft
  > Bei einer besonders hohen Straferwartung braucht daher nur geprüft zu werden, ob Umstände vorhanden sind, die die hieraus herzuleitende Fluchtgefahr ausräumen können (KG StV 1996, 383; OLG München Str...
- **[Judge=3]** `§ 112 StPO – Rn. 112` — Definiert dringenden Tatverdacht für Haftbefehl direkt
  > Haftunfähigkeit des Beschuldigten schließt den Erlass des Haftbefehls nicht aus, sondern hindert nur seinen Vollzug (OLG Düsseldorf JZ 1984, 248; OLG Frankfurt a.M. NJW 1968, 2302; OLG Nürnberg OLGSt ...

### q13 — stpo-prozess

**Query:** Welche Voraussetzungen hat die Untersuchungshaft wegen Fluchtgefahr?

**Kontext:** § 112 Abs. 2 Nr. 2 StPO Fluchtgefahr

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours-mxbai-voyage | 1.00 | 80% | 100% | 3 | 5.1s |
| ours-api | 1.00 | 80% | 100% | 3 | 5.9s |

#### ours-mxbai-voyage — Top 3
- **[Judge=3]** `§ 112 StPO – Rn. 112` — Direkt relevant: enthält exakte Tatbestandsmerkmale für Fluchtgefahr
  > 112 (1) ¹ Die Untersuchungshaft darf gegen den Beschuldigten angeordnet werden, wenn er der Tat dringend verdächtig ist und ein Haftgrund besteht. ² Sie darf nicht angeordnet werden, wenn sie zu der B...
- **[Judge=3]** `§ 112 StPO – III. Flucht (Abs – Rn. 17 (Teil 1)` — Direkt relevant: definiert Fluchtgefahr nach § 112 Abs. 2 Nr. 2
  > 17 IV. Fluchtgefahr (Abs. 2 Nr. 2). Fluchtgefahr (Abs. 2 Nr. 2) besteht, wenn die Würdigung der Umstände des Falles es wahrscheinlicher macht, dass sich der Beschuldigte dem Strafverfahren entziehen, ...
- **[Judge=3]** `§ 112 StPO – III. Flucht (Abs – Rn. 17` — Definiert direkt Voraussetzungen und Indizien für Fluchtgefahr
  > Die Beurteilung der Fluchtgefahr erfordert die Berücksichtigung aller Umstände des Falles, insbes. der Art der dem Beschuldigten vorgeworfenen Tat, der Persönlichkeit des Beschuldigten, seiner Lebensv...

#### ours-api — Top 3
- **[Judge=3]** `§ 112 StPO – Rn. 112` — Direkt relevant: § 112 Abs. 2 Nr. 2 Fluchtgefahr
  > 112 (1) ¹ Die Untersuchungshaft darf gegen den Beschuldigten angeordnet werden, wenn er der Tat dringend verdächtig ist und ein Haftgrund besteht. ² Sie darf nicht angeordnet werden, wenn sie zu der B...
- **[Judge=3]** `§ 112 StPO – III. Flucht (Abs – Rn. 17` — Direkt relevant: behandelt Voraussetzungen der Fluchtgefahr
  > Die Beurteilung der Fluchtgefahr erfordert die Berücksichtigung aller Umstände des Falles, insbes. der Art der dem Beschuldigten vorgeworfenen Tat, der Persönlichkeit des Beschuldigten, seiner Lebensv...
- **[Judge=3]** `§ 112 StPO – III. Flucht (Abs – Rn. 17 (Teil 1)` — Direkt relevant: definiert Fluchtgefahr nach § 112 Abs. 2 Nr. 2
  > 17 IV. Fluchtgefahr (Abs. 2 Nr. 2). Fluchtgefahr (Abs. 2 Nr. 2) besteht, wenn die Würdigung der Umstände des Falles es wahrscheinlicher macht, dass sich der Beschuldigte dem Strafverfahren entziehen, ...

### q14 — stpo-prozess

**Query:** Wie lange darf die Untersuchungshaft maximal dauern?

**Kontext:** § 121 StPO Sechs-Monats-Grenze, Haftpruefung OLG

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours-mxbai-voyage | 1.00 | 100% | 100% | 3 | 5.4s |
| ours-api | 0.99 | 100% | 100% | 3 | 6.3s |

#### ours-mxbai-voyage — Top 3
- **[Judge=3]** `§ 121 StPO – Rn. 121` — Direkter § 121 StPO Text, beantwortet Frage vollständig
  > 121 (1) Solange kein Urteil ergangen ist, das auf Freiheitsstrafe oder eine freiheitsentziehende Maßregel der Besserung und Sicherung erkennt, darf der Vollzug der Untersuchungshaft wegen derselben Ta...
- **[Judge=3]** `§ 121 StPO – Rn. 1` — Beantwortet direkt die Frage zur maximalen UHaft-Dauer
  > 1 A. Beschleunigungsgebot. Einen Anspruch auf beschleunigte Aburteilung hat der in UHaft (und einstweiliger Unterbringung) befindliche Beschuldigte nach Art. 5 Abs. 3 S. 2 EMRK (→ EMRK Art. 5 Rn. 10 f...
- **[Judge=3]** `§ 121 StPO – Rn. 1` — Beantwortet direkt Höchstdauer der Untersuchungshaft
  > Eine absolute Höchstgrenze für die Dauer v. UHaft sieht weder die StPO noch die EMRK vor (EGMR EuGRZ 1993, 384). Es kommt auf eine Abwägung aller Umstände des Einzelfalls an. Eine ein Jahr übersteigen...

#### ours-api — Top 3
- **[Judge=3]** `§ 121 StPO – Rn. 1` — Direkt relevant: behandelt 6-Monats-Grenze und Haftdauer
  > 1 A. Beschleunigungsgebot. Einen Anspruch auf beschleunigte Aburteilung hat der in UHaft (und einstweiliger Unterbringung) befindliche Beschuldigte nach Art. 5 Abs. 3 S. 2 EMRK (→ EMRK Art. 5 Rn. 10 f...
- **[Judge=3]** `§ 121 StPO – Rn. 121` — Beantwortet direkt die Frage zur Höchstdauer Untersuchungshaft
  > 121 (1) Solange kein Urteil ergangen ist, das auf Freiheitsstrafe oder eine freiheitsentziehende Maßregel der Besserung und Sicherung erkennt, darf der Vollzug der Untersuchungshaft wegen derselben Ta...
- **[Judge=3]** `§ 121 StPO – Rn. 1` — Direkt relevant: behandelt Höchstdauer der Untersuchungshaft
  > Eine absolute Höchstgrenze für die Dauer v. UHaft sieht weder die StPO noch die EMRK vor (EGMR EuGRZ 1993, 384). Es kommt auf eine Abwägung aller Umstände des Einzelfalls an. Eine ein Jahr übersteigen...

### q15 — stpo-prozess

**Query:** Was regelt § 136 StPO zur Beschuldigtenvernehmung?

**Kontext:** Belehrungspflichten, Recht auf Verteidiger

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours-mxbai-voyage | 0.89 | 80% | 67% | 2 | 4.9s |
| ours-api | 0.90 | 80% | 67% | 2 | 6.1s |

#### ours-mxbai-voyage — Top 3
- **[Judge=2]** `§ 500 StPO – ILL. für das Strafverfahren und das Bußgeldverf` — Behandelt Beschuldigtenvernehmung, aber nicht § 136 StPO direkt
  > (4) Zeugen können zur Aufenthaltsermittlung ausgeschrieben werden.  (5) Für die internationale Fahndung nach Personen, einschließlich der Fahndung nach Personen im SIS und aufgrund eines Europäischen ...
- **[Judge=1]** `§ 114b StPO – Rn. 6` — Behandelt Belehrungspflichten, aber bei Verhaftung statt Vernehmung
  > 6 D. Umfassende Geltung der Vorschrift. Nicht nur für Verhaftungen nach §§ 112 ff. gilt die Vorschr., sondern auch für solche nach § 230 Abs. 2, 236, 329 Abs. 4 S. 1 und § 412 S. 1. Sie ist auch auf b...
- **[Judge=3]** `§ 114b StPO – I. Abs – Rn. 5` — Direkt relevant: behandelt Belehrungspflichten nach § 136 StPO
  > 5 II. Abs. 2 S. 1 Nr. 2–4. Hier wird die auch nach § 136 Abs. 1 S. 2, 3 und § 163a Abs. 3 S. 2, 4 vor Beginn der ersten richterlichen bzw. staatsanwaltschaftlichen o. polizeilichen Vernehmung bestehen...

#### ours-api — Top 3
- **[Judge=2]** `§ 500 StPO – ILL. für das Strafverfahren und das Bußgeldverf` — Behandelt Belehrung nach §136, aber nicht §136 selbst
  > (4) Zeugen können zur Aufenthaltsermittlung ausgeschrieben werden.  (5) Für die internationale Fahndung nach Personen, einschließlich der Fahndung nach Personen im SIS und aufgrund eines Europäischen ...
- **[Judge=0]** `§ 52 StPO – J. Revision 33 – Rn. 26` — Behandelt Zeugenvernehmung, nicht Beschuldigtenvernehmung nach § 136
  > 26 H. Belehrung (Abs. 3 S. 1). Die Belehrung (Abs. 3 S. 1) muss in allen Fällen, nicht nur in denen des Abs. 2, dem Zeugen eine genügende Vorstellung v. der Bedeutung des Zeugnisverweigerungsrechts zu...
- **[Judge=2]** `§ 114b StPO – Rn. 6` — Belehrungspflichten bei Verhaftung, nicht Vernehmung nach § 136
  > 6 D. Umfassende Geltung der Vorschrift. Nicht nur für Verhaftungen nach §§ 112 ff. gilt die Vorschr., sondern auch für solche nach § 230 Abs. 2, 236, 329 Abs. 4 S. 1 und § 412 S. 1. Sie ist auch auf b...

### q16 — cross-reference

**Query:** Worin unterscheidet sich Betrug von Unterschlagung?

**Kontext:** Abgrenzung § 263 vs § 246 StGB

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours-mxbai-voyage | 0.98 | 100% | 100% | 3 | 5.8s |
| ours-api | 0.93 | 80% | 67% | 2 | 6.6s |

#### ours-mxbai-voyage — Top 3
- **[Judge=3]** `§ 263 StGB – I. Vermögensbegriff  – Rn. 263` — Vollständiger Betrugs-Tatbestand für direkte Abgrenzung zur Unterschlagung
  > 263 (1) Wer in der Absicht, sich oder einem Dritten einen rechtswidrigen Vermögensvorteil zu verschaffen, das Vermögen eines anderen dadurch beschädigt, daß er durch Vorspiegelung falscher oder durch ...
- **[Judge=2]** `§ 247 StGB – BT. Neunzehnter Abschnitt – Rn. 24` — Behandelt Abgrenzung § 246 zu § 263
  > 24 L. Konkurrenzen im Übrigen. Bei Manifestation des Zueignungswillens hinsichtlich mehrerer Sachen durch eine Ausführungshandlung liegt nur eine Tat vor (wistra 2006, 227 (227 f.)). Zur Abgrenzung vo...
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 76` — Direkt relevant: Unmittelbarkeit der Verfügung bei Betrug
  > 76 3. Unmittelbarkeit der Verfügung. Neben der Freiwilligkeit ist das Merkmal der Unmittelbarkeit nach stRspr und hM das wichtigste Kriterium zur Beschränkung der § 263 unterfallenden Selbstschädigung...

#### ours-api — Top 3
- **[Judge=2]** `§ 247 StGB – BT. Neunzehnter Abschnitt – Rn. 24` — Behandelt Abgrenzung § 246 zu § 263
  > 24 L. Konkurrenzen im Übrigen. Bei Manifestation des Zueignungswillens hinsichtlich mehrerer Sachen durch eine Ausführungshandlung liegt nur eine Tat vor (wistra 2006, 227 (227 f.)). Zur Abgrenzung vo...
- **[Judge=3]** `§ 263 StGB – I. Vermögensbegriff  – Rn. 263` — Vollständiger Betrugs-Tatbestand für direkte Abgrenzung zur Unterschlagung
  > 263 (1) Wer in der Absicht, sich oder einem Dritten einen rechtswidrigen Vermögensvorteil zu verschaffen, das Vermögen eines anderen dadurch beschädigt, daß er durch Vorspiegelung falscher oder durch ...
- **[Judge=1]** `§ 242 StGB – BT. Neunzehnter Abschnitt – Rn. 31` — Behandelt Diebstahl, nicht Betrug-Unterschlagung-Abgrenzung
  > 31 Bedingter Vorsatz reicht grds. aus. Das betrifft namentlich die Merkmale des Sachbegriffs, der Fremdheit und der Wegnahme. Hinsichtlich des normativen Merkmals der Fremdheit kommt es hierbei auf ei...

### q17 — cross-reference

**Query:** Was sind die Unterschiede zwischen Diebstahl und Raub?

**Kontext:** § 242 vs § 249 StGB — Abgrenzung durch Gewalt/Drohung

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours-mxbai-voyage | 0.99 | 100% | 100% | 3 | 9.4s |
| ours-api | 1.00 | 100% | 100% | 3 | 6.9s |

#### ours-mxbai-voyage — Top 3
- **[Judge=3]** `§ 249 StGB` — Behandelt direkt Raub vs räuberische Erpressung, Wegnahme-Kriterien
  > NStZ 2023, 351). Danach ist § 249 gegenüber § 255 ein spezielles Delikt; in jedem Raub liegt eine räuberische Erpressung (aA die hM in der Literatur). Die Unterscheidung richtet sich nach dem äußeren ...
- **[Judge=3]** `§ 249 StGB – BT. Zwanzigster Abschnitt – Rn. 15` — Direkt relevant: erklärt subjektive Unterschiede Diebstahl/Raub
  > G. Subjektiver Tatbestand. Der Vorsatz muss entsprechend der Doppelnatur des Raubs sowohl Wegnahme (vgl. dazu → § 242 Rn. 29 ff.) als auch Nötigung (→ § 240 Rn. 53 f.) sowie deren Verknüpfung umfassen...
- **[Judge=2]** `§ 252 StGB – I. Sonstige Vorschriften – Rn. 252` — Behandelt räuberischen Diebstahl, nicht direkte Abgrenzung Diebstahl/Raub
  > 252 Wer, bei einem Diebstahl auf frischer Tat betroffen, gegen eine Person Gewalt verübt oder Drohungen mit gegenwärtiger Gefahr für Leib oder Leben anwendet, um sich im Besitz des gestohlenen Gutes z...

#### ours-api — Top 3
- **[Judge=3]** `§ 249 StGB` — Behandelt direkt Raub-Tatbestand und Abgrenzung zu anderen Delikten
  > NStZ 2023, 351). Danach ist § 249 gegenüber § 255 ein spezielles Delikt; in jedem Raub liegt eine räuberische Erpressung (aA die hM in der Literatur). Die Unterscheidung richtet sich nach dem äußeren ...
- **[Judge=3]** `§ 249 StGB – BT. Zwanzigster Abschnitt – Rn. 15` — Behandelt direkt subjektiven Tatbestand bei Raub vs Diebstahl
  > G. Subjektiver Tatbestand. Der Vorsatz muss entsprechend der Doppelnatur des Raubs sowohl Wegnahme (vgl. dazu → § 242 Rn. 29 ff.) als auch Nötigung (→ § 240 Rn. 53 f.) sowie deren Verknüpfung umfassen...
- **[Judge=3]** `§ 249 StGB – BT. Zwanzigster Abschnitt – Rn. 6` — Direkt relevant: Finalzusammenhang zwischen Nötigung und Wegnahme
  > 6 E. Finalzusammenhang zwischen Nötigung und Wegnahme. Gewalt oder Drohung müssen das (objektive und subjektive) Mittel zur Ermöglichung der Wegnahme (in Zueignungsabsicht) sein (BGHSt 4, 210 (211); 2...

### q18 — cross-reference

**Query:** Wann wird Betrug zu Computerbetrug und umgekehrt?

**Kontext:** § 263 vs § 263a StGB — Abgrenzung bei elektronischer Datenverarbeitung

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours-mxbai-voyage | 0.99 | 100% | 100% | 3 | 6.3s |
| ours-api | 0.79 | 60% | 33% | 1 | 5.9s |

#### ours-mxbai-voyage — Top 3
- **[Judge=3]** `§ 263a StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 23` — Direkte Abgrenzung § 263 vs § 263a bei Vorsatzproblemen
  > 23 G. Subjektiver Tatbestand. Die Tat setzt (bedingten) Vorsatz voraus. Er muss sich auf alle Tatbestandsmerkmale, zu denen auch die Unbefugtheit (→ Rn. 10) gehört, dh auch auf die Voraussetzungen ers...
- **[Judge=3]** `§ 263a StGB – M. Sonstige Vorschriften 40 – Rn. 239` — Definiert § 263a Tatbestandsmerkmale, direkt relevant für Abgrenzung
  > 239 I. Sonstige Vorschriften. FAufsicht §§ 263 Abs. 5, 68 Abs. 1. Zuständigkeit in Wirtschaftsstrafaschen § 74c Abs. 1 Nr. 6, § 74e Nr. 2 GVG iVm § 103 Abs. 2 JGG. TKÜ § 100a Abs. 2 Nr. 1 Buchst. n St...
- **[Judge=3]** `§ 263a StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 10` — Direkte Abgrenzung § 263/263a bei unbefugter Datenverwendung
  > Eine unbefugte Verwendung liegt insbes. vor bei Eingabe von Zugangscodes (PIN, TAN, usw.) gegen den (erkennbaren) Willen des Berechtigten; etwa nachdem mit Methoden des Phishing geheime Zugangsdaten e...

#### ours-api — Top 3
- **[Judge=1]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 62` — Betrug allgemein, aber nicht Abgrenzung zu Computerbetrug
  > Die Kausalität der Täuschung für den Irrtum und dessen Kausalität für die Vermögensverfügung müssen im Einzelfall festgestellt sein. Mitverursachung reicht aus. Dabei darf das Gericht auch bei Serien-...
- **[Judge=2]** `§ 263 StGB – I. Vermögensbegriff  – Rn. 263` — Enthält § 263 Grundtatbestand, fehlt § 263a Abgrenzung
  > 263 (1) Wer in der Absicht, sich oder einem Dritten einen rechtswidrigen Vermögensvorteil zu verschaffen, das Vermögen eines anderen dadurch beschädigt, daß er durch Vorspiegelung falscher oder durch ...
- **[Judge=1]** `§ 263 StGB – BT. Zweijundzwanzigster Abschnitt – Rn. 212` — Behandelt Betrug allgemein, nicht spezifisch § 263a Abgrenzung
  > 212 Der Begriff der Urkundenfälschung ist weit zu fassen; er umfasst neben Taten nach § 267 auch solche nach §§ 268–281 (LK-StGB/Kubiciel/Tiedemann Rn. 297; NK-StGB/Kindhäuser/Hoven Rn. 392). Entsprec...