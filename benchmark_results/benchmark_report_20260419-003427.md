# RAG Benchmark Report

_Generiert: 2026-04-19T00:34:27_


- Queries: **18**
- Top-K: **5**
- Systeme: ours-mxbai, ours-mxbai-voyage

## Gesamtvergleich

| Metrik | ours-mxbai | ours-mxbai-voyage |
|--------|--------|--------|
| nDCG@10 | 0.974 | 0.978 |
| Relevance@10 | 87.8% | 94.4% |
| Relevance@3 | 92.6% | 98.1% |
| Top-1-Score | 2.89 | 2.78 |
| Mean-Score | 2.48 | 2.71 |
| Latenz (s) | 5.59 | 5.43 |

## Nach Kategorie


### alltagssprache

| Metrik | ours-mxbai | ours-mxbai-voyage |
|--------|--------|--------|
| nDCG@10 | 0.998 | 1.000 |
| Relevance@10 | 100.0% | 100.0% |
| Relevance@3 | 100.0% | 100.0% |

### cross-reference

| Metrik | ours-mxbai | ours-mxbai-voyage |
|--------|--------|--------|
| nDCG@10 | 0.932 | 0.913 |
| Relevance@10 | 66.7% | 80.0% |
| Relevance@3 | 77.8% | 88.9% |

### exakte-paragraphen

| Metrik | ours-mxbai | ours-mxbai-voyage |
|--------|--------|--------|
| nDCG@10 | 0.987 | 0.992 |
| Relevance@10 | 95.0% | 100.0% |
| Relevance@3 | 100.0% | 100.0% |

### konzept

| Metrik | ours-mxbai | ours-mxbai-voyage |
|--------|--------|--------|
| nDCG@10 | 0.986 | 0.995 |
| Relevance@10 | 85.0% | 90.0% |
| Relevance@3 | 91.7% | 100.0% |

### stpo-prozess

| Metrik | ours-mxbai | ours-mxbai-voyage |
|--------|--------|--------|
| nDCG@10 | 0.952 | 0.969 |
| Relevance@10 | 86.7% | 100.0% |
| Relevance@3 | 88.9% | 100.0% |

## Detail pro Query


### q01 — exakte-paragraphen

**Query:** Welche Voraussetzungen hat der gewerbsmaessige Bandenbetrug nach § 263 Abs. 5 StGB?

**Kontext:** Qualifikationstatbestand des Bandenbetrugs im Fischer-Kommentar

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours-mxbai | 0.99 | 80% | 100% | 3 | 6.9s |
| ours-mxbai-voyage | 1.00 | 100% | 100% | 3 | 6.4s |

#### ours-mxbai — Top 3
- **[Judge=3]** `§ 263 StGB – BT. Zweriindzwanzigster Abschnitt – Rn. 225` — Direkt relevant: erklärt beide Qualifikationsvoraussetzungen detailliert
  > IV. Qualifikation (Abs. 5). Abs. 5 enthält einen Qualifikationstatbestand, der die Tat in Fällen kumulativ gewerbs- und bandenmäßiger Begehung zum Verbrechen macht. Die Qualifikation ist in die Urteil...
- **[Judge=3]** `§ 263 StGB – I. Vermögensbegriff  – Rn. 263` — Enthält direkt § 263 Abs. 5 mit allen Voraussetzungen
  > 263 (1) Wer in der Absicht, sich oder einem Dritten einen rechtswidrigen Vermögensvorteil zu verschaffen, das Vermögen eines anderen dadurch beschädigt, daß er durch Vorspiegelung falscher oder durch ...
- **[Judge=3]** `§ 263 StGB – BT. Zweijundzwanzigster Abschnitt – Rn. 213` — Direkt relevant zu Qualifikationstatbestand § 263 Abs. 5
  > 213 Sind beide Varianten erfüllt, ist eine Qualifikation nach Abs. 5 gegeben. Die Abgrenzung des Abs. 3 Nr. 1 zum Verbrechen nach Abs. 5 ist in Fällen bandenmäßiger Begehung schwierig, denn eine auf f...

#### ours-mxbai-voyage — Top 3
- **[Judge=3]** `§ 263 StGB – BT. Zweriindzwanzigster Abschnitt – Rn. 225` — Direkt relevant: behandelt explizit Abs. 5 Voraussetzungen
  > IV. Qualifikation (Abs. 5). Abs. 5 enthält einen Qualifikationstatbestand, der die Tat in Fällen kumulativ gewerbs- und bandenmäßiger Begehung zum Verbrechen macht. Die Qualifikation ist in die Urteil...
- **[Judge=3]** `§ 263 StGB – I. Vermögensbegriff  – Rn. 263` — Enthält vollständigen Wortlaut von § 263 Abs. 5 StGB
  > 263 (1) Wer in der Absicht, sich oder einem Dritten einen rechtswidrigen Vermögensvorteil zu verschaffen, das Vermögen eines anderen dadurch beschädigt, daß er durch Vorspiegelung falscher oder durch ...
- **[Judge=3]** `§ 263 StGB – BT. Zweijundzwanzigster Abschnitt – Rn. 211` — Direkt relevant: definiert bandenmäßige Begehung bei Betrug
  > 211 b) Bandenmäßigkeit. Bandenmäßige Begehung ist gegeben, wenn sich eine Bande (zum Begriff vgl. → § 244 Rn. 34 ff.) zur Begehung einer Mehrzahl von selbstständigen Taten der Urkundenfälschung oder d...

### q02 — exakte-paragraphen

**Query:** Was regelt § 112 StPO zur Untersuchungshaft?

**Kontext:** Anordnungsvoraussetzungen der U-Haft (dringender Tatverdacht, Haftgrund) im Schmitt/Koehler

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours-mxbai | 0.99 | 100% | 100% | 3 | 5.1s |
| ours-mxbai-voyage | 1.00 | 100% | 100% | 3 | 5.4s |

#### ours-mxbai — Top 3
- **[Judge=3]** `§ 112 StPO – Rn. 112` — Beantwortet Frage direkt mit Gesetzestext und Struktur
  > 112 (1) ¹ Die Untersuchungshaft darf gegen den Beschuldigten angeordnet werden, wenn er der Tat dringend verdächtig ist und ein Haftgrund besteht. ² Sie darf nicht angeordnet werden, wenn sie zu der B...
- **[Judge=3]** `§ 112 StPO – Rn. 112` — Behandelt direkt § 112 StPO Untersuchungshaft-Voraussetzungen
  > Haftunfähigkeit des Beschuldigten schließt den Erlass des Haftbefehls nicht aus, sondern hindert nur seinen Vollzug (OLG Düsseldorf JZ 1984, 248; OLG Frankfurt a.M. NJW 1968, 2302; OLG Nürnberg OLGSt ...
- **[Judge=3]** `§ 112 StPO – III. Flucht (Abs – Rn. 23` — Direkt relevant zu § 112 StPO Haftgruenden
  > Bei einer besonders hohen Straferwartung braucht daher nur geprüft zu werden, ob Umstände vorhanden sind, die die hieraus herzuleitende Fluchtgefahr ausräumen können (KG StV 1996, 383; OLG München Str...

#### ours-mxbai-voyage — Top 3
- **[Judge=3]** `§ 112 StPO – Rn. 112` — Beantwortet Frage direkt mit allen Voraussetzungen
  > 112 (1) ¹ Die Untersuchungshaft darf gegen den Beschuldigten angeordnet werden, wenn er der Tat dringend verdächtig ist und ein Haftgrund besteht. ² Sie darf nicht angeordnet werden, wenn sie zu der B...
- **[Judge=3]** `§ 112 StPO – III. Flucht (Abs – Rn. 23` — Behandelt direkt Haftgruende der Untersuchungshaft nach § 112 StPO
  > Bei einer besonders hohen Straferwartung braucht daher nur geprüft zu werden, ob Umstände vorhanden sind, die die hieraus herzuleitende Fluchtgefahr ausräumen können (KG StV 1996, 383; OLG München Str...
- **[Judge=3]** `§ 112 StPO – Rn. 112` — Direkt relevant: § 112 StPO Haftvoraussetzungen erklärt
  > Haftunfähigkeit des Beschuldigten schließt den Erlass des Haftbefehls nicht aus, sondern hindert nur seinen Vollzug (OLG Düsseldorf JZ 1984, 248; OLG Frankfurt a.M. NJW 1968, 2302; OLG Nürnberg OLGSt ...

### q03 — exakte-paragraphen

**Query:** Welche Haftgruende nennt § 112 Abs. 2 StPO?

**Kontext:** Fluchtgefahr, Verdunkelungsgefahr, Flucht — im StPO-Kommentar

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours-mxbai | 0.99 | 100% | 100% | 3 | 5.0s |
| ours-mxbai-voyage | 1.00 | 100% | 100% | 3 | 5.0s |

#### ours-mxbai — Top 3
- **[Judge=3]** `§ 112 StPO – Rn. 112` — Vollständige Auflistung aller Haftgründe nach § 112 Abs. 2 StPO
  > 112 (1) ¹ Die Untersuchungshaft darf gegen den Beschuldigten angeordnet werden, wenn er der Tat dringend verdächtig ist und ein Haftgrund besteht. ² Sie darf nicht angeordnet werden, wenn sie zu der B...
- **[Judge=3]** `§ 112 StPO – III. Flucht (Abs – Rn. 23` — Behandelt direkt Haftgruende § 112 Abs. 2 StPO
  > Bei einer besonders hohen Straferwartung braucht daher nur geprüft zu werden, ob Umstände vorhanden sind, die die hieraus herzuleitende Fluchtgefahr ausräumen können (KG StV 1996, 383; OLG München Str...
- **[Judge=2]** `§ 112 StPO – III. Flucht (Abs – Rn. 32 (Teil 2)` — Behandelt Verdunkelungsgefahr als einen der drei Haftgruende
  > Wenn die Verdunkelungshandlungen nicht geeignet sind, die Ermittlung der Wahrheit zu erschweren, darf UHaft nicht angeordnet werden. Der Haftgrund liegt daher nicht vor, wenn der Sachverhalt schon in ...

#### ours-mxbai-voyage — Top 3
- **[Judge=3]** `§ 112 StPO – Rn. 112` — Enthält vollständige Aufzählung der Haftgründe nach § 112 Abs. 2 StPO
  > 112 (1) ¹ Die Untersuchungshaft darf gegen den Beschuldigten angeordnet werden, wenn er der Tat dringend verdächtig ist und ein Haftgrund besteht. ² Sie darf nicht angeordnet werden, wenn sie zu der B...
- **[Judge=3]** `§ 112 StPO – III. Flucht (Abs – Rn. 23` — Behandelt direkt Haftgruende nach § 112 Abs. 2 StPO
  > Bei einer besonders hohen Straferwartung braucht daher nur geprüft zu werden, ob Umstände vorhanden sind, die die hieraus herzuleitende Fluchtgefahr ausräumen können (KG StV 1996, 383; OLG München Str...
- **[Judge=3]** `§ 112 StPO – III. Flucht (Abs – Rn. 17 (Teil 1)` — Erläutert detailliert Fluchtgefahr nach § 112 Abs. 2 Nr. 2
  > 17 IV. Fluchtgefahr (Abs. 2 Nr. 2). Fluchtgefahr (Abs. 2 Nr. 2) besteht, wenn die Würdigung der Umstände des Falles es wahrscheinlicher macht, dass sich der Beschuldigte dem Strafverfahren entziehen, ...

### q04 — exakte-paragraphen

**Query:** Was regelt § 102 StPO zur Durchsuchung beim Beschuldigten?

**Kontext:** Durchsuchungsvoraussetzungen beim Verdaechtigen

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours-mxbai | 0.97 | 100% | 100% | 3 | 4.8s |
| ours-mxbai-voyage | 0.97 | 100% | 100% | 3 | 5.2s |

#### ours-mxbai — Top 3
- **[Judge=3]** `§ 102 StPO – Rn. 102` — Direkter § 102 StPO Text zu Durchsuchung beim Beschuldigten
  > 102 Bei dem, welcher als Täter oder Teilnehmer einer Straftat oder der Datenhehlerei, Begünstigung, Strafvereitelung oder Hehlerei  Köhler    Ermittlungsmaßnahmen  verdächtig ist, kann eine Durchsuchu...
- **[Judge=2]** `§ 102 StPO – Rn. 10` — Behandelt Durchsuchungsvoraussetzungen allgemein, nicht spezifisch § 102
  > II. Auffinden von Beweismitteln. Zu den Beweismitteln (→ § 94 Rn. 4 ff.) gehören auch die nur in § 103 erwähnten Spuren (SK-StPO/Jäger/Wohlers Rn. 21) u. Personen, die zu Beweiszwecken in Augenschein ...
- **[Judge=3]** `§ 102 StPO – Rn. 10` — Direkt relevant: Erläutert Sachen-Begriff bei § 102 StPO
  > 10 III. Sachen. Sachen sind Kleidungsstücke, die der Verdächtige bei sich führt, ohne sie zu tragen, u. seine sonstige bewegliche Habe, gleichgültig, ob sie sich in seinem Umkreis, zB in Gepäckstücken...

#### ours-mxbai-voyage — Top 3
- **[Judge=3]** `§ 102 StPO – Rn. 102` — Direkte Regelung § 102 StPO Durchsuchung Beschuldigter
  > 102 Bei dem, welcher als Täter oder Teilnehmer einer Straftat oder der Datenhehlerei, Begünstigung, Strafvereitelung oder Hehlerei  Köhler    Ermittlungsmaßnahmen  verdächtig ist, kann eine Durchsuchu...
- **[Judge=2]** `§ 102 StPO – Rn. 10` — Behandelt Durchsuchungsvoraussetzungen allgemein, nicht spezifisch § 102
  > II. Auffinden von Beweismitteln. Zu den Beweismitteln (→ § 94 Rn. 4 ff.) gehören auch die nur in § 103 erwähnten Spuren (SK-StPO/Jäger/Wohlers Rn. 21) u. Personen, die zu Beweiszwecken in Augenschein ...
- **[Judge=2]** `§ 102 StPO – Rn. 10` — Behandelt Durchsuchungsvoraussetzungen und Verhältnismäßigkeit, nicht spezifisch §102
  > Kohler     Erstes Buch. Achter Abschnitt  Aufklärung bislang ungeklärter Fälle“ einer Tatserie beitragen könne, scheint dies den besonderen Umständen des Einzelfalls geschuldet zu sein. Denn zum einen...

### q05 — konzept

**Query:** Wann liegt eine konkludente Taeuschung im Sinne des § 263 StGB vor?

**Kontext:** Taeuschungshandlung durch schluessiges Verhalten

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours-mxbai | 0.99 | 100% | 100% | 3 | 6.4s |
| ours-mxbai-voyage | 1.00 | 100% | 100% | 3 | 5.4s |

#### ours-mxbai — Top 3
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 21` — Definiert konkludente Taeuschung bei § 263 StGB direkt
  > 21 2. Konkludente Erklärungen. Auch durch eine schlüssige Handlung (konkludente Erklärung) kann vorspiegelt werden. Eine solche konkludente Erklärung durch aktives Tun ist von einer Erklärung durch Un...
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 14` — Behandelt direkt konkludente Taeuschung und Tatbestandsmerkmale
  > 14 II. Tathandlung. Der Begriff „Täuschen“ ist im Wortlaut des Abs. 1 nicht verwendet; er ergibt sich aus dem Zusammenhang zwischen der Beschreibung der Tathandlung (→ Rn. 18) und dem Irrtum als ihrem...
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 14` — Direkt relevant: behandelt konkludente Taeuschung nach § 263
  > Rspr. und hM bejahen darüber hinaus aber die Möglichkeit einer Täuschung durch Unterlassen auch ohne Erklärung gegenüber dem Irrenden (→ Rn. 38; vgl. BGHSt 39, 392 (398); BayObLG NJW 1987, 1654 (mAnm ...

#### ours-mxbai-voyage — Top 3
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 21` — Direkt relevant: definiert konkludente Taeuschung bei § 263
  > 21 2. Konkludente Erklärungen. Auch durch eine schlüssige Handlung (konkludente Erklärung) kann vorspiegelt werden. Eine solche konkludente Erklärung durch aktives Tun ist von einer Erklärung durch Un...
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 14` — Behandelt direkt konkludente Taeuschung und Abgrenzungsfragen
  > Rspr. und hM bejahen darüber hinaus aber die Möglichkeit einer Täuschung durch Unterlassen auch ohne Erklärung gegenüber dem Irrenden (→ Rn. 38; vgl. BGHSt 39, 392 (398); BayObLG NJW 1987, 1654 (mAnm ...
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 14` — Direkt relevant: behandelt konkludente Täuschungshandlungen bei § 263
  > 14 II. Tathandlung. Der Begriff „Täuschen“ ist im Wortlaut des Abs. 1 nicht verwendet; er ergibt sich aus dem Zusammenhang zwischen der Beschreibung der Tathandlung (→ Rn. 18) und dem Irrtum als ihrem...

### q06 — konzept

**Query:** Was ist eine Vermoegensverfuegung und welche Anforderungen stellt die Rechtsprechung?

**Kontext:** Tatbestandsmerkmal der Vermoegensverfuegung beim Betrug

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours-mxbai | 0.96 | 60% | 67% | 3 | 6.0s |
| ours-mxbai-voyage | 0.99 | 80% | 100% | 3 | 5.7s |

#### ours-mxbai — Top 3
- **[Judge=3]** `§ 263 StGB – BT. Zweitundzwanzigster Abschnitt – Rn. 69` — Direkt relevant: Definition und Anforderungen der Vermoegensverfuegung
  > 69 Anders ist es, wenn der Verfügende seinerseits nur (gutgläubige) Hilfsperson eines bösgläubigen Dritten ist. Hier ist auf den Irrtum des Entscheidungsbefugten abzustellen: Erkennt dieser die Unrich...
- **[Judge=2]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 87` — Behandelt Kausalität und Vermögensschaden, nicht Vermögensverfügung selbst
  > 87 5. Kausalität. Für die Vermögensverfügung muss der täuschungsbedingte Irrtum kausal sein (vgl. BGHSt 24, 257 (260); 24, 386 (389); NStZ 2003, 313 (314 f.); OLG Düsseldorf NJW 1987, 3145); Mitverurs...
- **[Judge=1]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 62` — Behandelt Kausalitaet beim Betrug, nicht Vermoegensverfuegung direkt
  > Die Kausalität der Täuschung für den Irrtum und dessen Kausalität für die Vermögensverfügung müssen im Einzelfall festgestellt sein. Mitverursachung reicht aus. Dabei darf das Gericht auch bei Serien-...

#### ours-mxbai-voyage — Top 3
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 76` — Direkt relevant: definiert Vermoegensverfuegung und Anforderungen
  > 76 3. Unmittelbarkeit der Verfügung. Neben der Freiwilligkeit ist das Merkmal der Unmittelbarkeit nach stRspr und hM das wichtigste Kriterium zur Beschränkung der § 263 unterfallenden Selbstschädigung...
- **[Judge=3]** `§ 263 StGB – BT. Zweitundzwanzigster Abschnitt – Rn. 69` — Definiert Vermögensverfügung beim Betrug direkt
  > 69 Anders ist es, wenn der Verfügende seinerseits nur (gutgläubige) Hilfsperson eines bösgläubigen Dritten ist. Hier ist auf den Irrtum des Entscheidungsbefugten abzustellen: Erkennt dieser die Unrich...
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 76` — Direkt relevant: definiert Vermoegensverfuegung beim Betrug
  > 4. Dreiecksbetrug. Da die Getäuschte und die verfügende, nicht aber die verfügende und die geschädigte Person identisch sein müssen, ist der Tatbestand des § 263 nur erfüllt, wenn die Vermögensverfügu...

### q07 — konzept

**Query:** Was versteht man unter einem Gefaehrdungsschaden beim Betrug?

**Kontext:** Schadensbegriff, schadensgleiche Vermoegensgefaehrdung

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours-mxbai | 1.00 | 100% | 100% | 3 | 5.2s |
| ours-mxbai-voyage | 1.00 | 80% | 100% | 3 | 4.8s |

#### ours-mxbai — Top 3
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 159` — Definiert direkt Gefährdungsschaden beim Betrug
  > 159 b) Voraussetzungen. aa) Ein Gefährdungsschaden ist gegeben, wenn die Wahrscheinlichkeit des endgültigen Verlusts eines Vermögensbestandteils zum Zeitpunkt der täuschungsbedingten Verfügung so groß...
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 182` — Behandelt direkt Gefährdungsschaden und Schadensvorsatz beim Betrug
  > 182 In Fällen des Gefährdungsschadens hat der BGH vielfach entschieden, die Kenntnis von Umständen, welche die Gefahr des Vermögensverlusts begründen, reiche oft, aber nicht in jedem Fall aus, um das ...
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 156` — Erklärt direkt schadensgleiche Vermögensgefährdung beim Betrug
  > 156 8. Schadensgleiche Vermögensgefährdung. Eine Ausweitung erfährt der Tatbestand durch die von stRspr (seit RGSt 16, 1) und hM bejahte Möglichkeit eines vollendeten Schadenseintritts durch konkrete ...

#### ours-mxbai-voyage — Top 3
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 159` — Definiert direkt Gefährdungsschaden beim Betrug
  > 159 b) Voraussetzungen. aa) Ein Gefährdungsschaden ist gegeben, wenn die Wahrscheinlichkeit des endgültigen Verlusts eines Vermögensbestandteils zum Zeitpunkt der täuschungsbedingten Verfügung so groß...
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 171` — Definiert und erklärt ausführlich den Gefährdungsschaden
  > Die täuschungsbedingte Herausgabe von EC-Karten, Kreditkarten und weiteren Zugangsdaten zu Bank-Guthaben (PINs, TANs; Passwörter), sei es infolge persönlicher Täuschung oder von „Phishing“-Manipulatio...
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 109` — Direkt relevant: Gefährdungsschaden wird explizit erwähnt
  > VI. Schaden. Vermögensschaden ist ein negativer Saldo zwischen dem Wert des Vermögens vor und nach der irrtumsbedingten Vermögensverfügung des Getäuschten (Prinzip der Gesamtsaldierung; stRspr; vgl. B...

### q08 — konzept

**Query:** Wie wird der Vorsatz beim Betrug bestimmt, insbesondere die Bereicherungsabsicht?

**Kontext:** Subjektiver Tatbestand § 263 StGB

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours-mxbai | 0.99 | 80% | 100% | 3 | 5.0s |
| ours-mxbai-voyage | 0.99 | 100% | 100% | 3 | 4.6s |

#### ours-mxbai — Top 3
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 176` — Behandelt direkt Vorsatz bei Betrug, relevante Voraussetzungen
  > D. Subjektiver Tatbestand. § 263 setzt Vorsatz voraus; darüber hinaus ist die Absicht rechtswidriger Bereicherung erforderlich.   I. Vorsatz. 1. Täuschungsvorsatz. Der Vorsatz (bedingter Vorsatz genüg...
- **[Judge=3]** `§ 263 StGB – I. Sonstige Vorschriften 239 – Rn. 263 (Teil 1)` — Behandelt direkt Bereicherungsabsicht und Vorsatz bei Betrug
  > 3. Einzelne Fallgruppen ... 92 4. Rechtlich missbilligte, sittenwidrige und gesetzeswidrige wirtschaftliche Werte ... 101 VI. Schaden ... 110 1. Grundsätze der Schadensermittlung ... 111 2. Vermögensm...
- **[Judge=2]** `§ 263 StGB – I. Vermögensbegriff  – Rn. 263` — Gesetzestext enthält Bereicherungsabsicht, aber keine Auslegung
  > 263 (1) Wer in der Absicht, sich oder einem Dritten einen rechtswidrigen Vermögensvorteil zu verschaffen, das Vermögen eines anderen dadurch beschädigt, daß er durch Vorspiegelung falscher oder durch ...

#### ours-mxbai-voyage — Top 3
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 176` — Direkt relevant: Vorsatz und Bereicherungsabsicht beim Betrug
  > D. Subjektiver Tatbestand. § 263 setzt Vorsatz voraus; darüber hinaus ist die Absicht rechtswidriger Bereicherung erforderlich.   I. Vorsatz. 1. Täuschungsvorsatz. Der Vorsatz (bedingter Vorsatz genüg...
- **[Judge=3]** `§ 263 StGB – BT. Zweijundzwanzigster Abschnitt – Rn. 194` — Direkt relevant: Vorsatz bei Bereicherungsabsicht, subjektiver Tatbestand
  > 194 4. Vorsatz hinsichtlich der Rechtswidrigkeit. Die Rechtswidrigkeit des angestrebten Vermögensvorteils muss vom Vorsatz umfasst sein; sie ist wie bei § 253 (vgl. dort 20) subjektives Tatbestandsmer...
- **[Judge=2]** `§ 263 StGB – I. Vermögensbegriff  – Rn. 263` — Gesetzestext mit Bereicherungsabsicht, aber keine Auslegung
  > 263 (1) Wer in der Absicht, sich oder einem Dritten einen rechtswidrigen Vermögensvorteil zu verschaffen, das Vermögen eines anderen dadurch beschädigt, daß er durch Vorspiegelung falscher oder durch ...

### q09 — alltagssprache

**Query:** Hat der Angeklagte die Kunden über das Internet betrogen?

**Kontext:** Abstrakte Frage zu Internetbetrug, sucht Taeuschungshandlung + Schaden

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours-mxbai | 0.99 | 100% | 100% | 3 | 5.5s |
| ours-mxbai-voyage | 1.00 | 100% | 100% | 3 | 4.9s |

#### ours-mxbai — Top 3
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 109` — Definiert Vermögensschaden bei Betrug direkt relevant
  > VI. Schaden. Vermögensschaden ist ein negativer Saldo zwischen dem Wert des Vermögens vor und nach der irrtumsbedingten Vermögensverfügung des Getäuschten (Prinzip der Gesamtsaldierung; stRspr; vgl. B...
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 5` — Definiert zentrale Merkmale des Betrugs direkt
  > 5 C. Grundtatbestand, Abs. 1. Tathandlung ist das Täuschen einer natürlichen Person (vgl. NStZ 2005, 213) über Tatsachen. Erfolg dieser Handlung muss ein Irrtum des Täuschungsadressaten sein; dieser m...
- **[Judge=2]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 263 (Tei` — Behandelt Betrug, aber nur Literaturverzeichnis ohne Inhalt
  > Heghmanns, Strafbarkeit des „Phishing“ von Bankkontendaten und ihrer Verwertung, wistra 2007, 167; Hilgendorf, Tatsachenaussagen u. Werturteile im Strafrecht, 1998; Hillenkamp, Zum Schutz „deliktische...

#### ours-mxbai-voyage — Top 3
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 5` — Definiert zentrale Tatbestandsmerkmale des Betrugs
  > 5 C. Grundtatbestand, Abs. 1. Tathandlung ist das Täuschen einer natürlichen Person (vgl. NStZ 2005, 213) über Tatsachen. Erfolg dieser Handlung muss ein Irrtum des Täuschungsadressaten sein; dieser m...
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 109` — Direkt relevant: zentrale Tatbestandsmerkmale Schaden bei Betrug
  > VI. Schaden. Vermögensschaden ist ein negativer Saldo zwischen dem Wert des Vermögens vor und nach der irrtumsbedingten Vermögensverfügung des Getäuschten (Prinzip der Gesamtsaldierung; stRspr; vgl. B...
- **[Judge=3]** `§ 263 StGB – I. Vermögensbegriff  – Rn. 263` — Zentrale Betrugsvorschrift mit allen Tatbestandsmerkmalen für Internetbetrug
  > 263 (1) Wer in der Absicht, sich oder einem Dritten einen rechtswidrigen Vermögensvorteil zu verschaffen, das Vermögen eines anderen dadurch beschädigt, daß er durch Vorspiegelung falscher oder durch ...

### q10 — alltagssprache

**Query:** Wann darf die Polizei bei jemandem zu Hause suchen?

**Kontext:** Durchsuchungsvoraussetzungen, §§ 102 ff. StPO

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours-mxbai | 1.00 | 100% | 100% | 3 | 5.6s |
| ours-mxbai-voyage | 1.00 | 100% | 100% | 3 | 5.8s |

#### ours-mxbai — Top 3
- **[Judge=3]** `§ 102 StPO – Rn. 102` — Direkt relevant: § 102 StPO Durchsuchungsvoraussetzungen
  > 102 Bei dem, welcher als Täter oder Teilnehmer einer Straftat oder der Datenhehlerei, Begünstigung, Strafvereitelung oder Hehlerei  Köhler    Ermittlungsmaßnahmen  verdächtig ist, kann eine Durchsuchu...
- **[Judge=3]** `§ 102 StPO – Rn. 3` — Direkt relevant: behandelt Durchsuchungsvoraussetzungen nach StPO
  > **Teilnehmer** nach §§ 25 ff. StGB, nicht die sog. notwendigen Teilnehmer (zum Begriff: Fischer/Fischer StGB Vor § 25 Rn. 7), stehen den Tatverdächtigen gleich. Bei jedem v. ihnen sowie bei den der Be...
- **[Judge=2]** `§ 102 StPO – Rn. 10` — Behandelt Durchsuchungsvoraussetzungen, aber nicht direkte Antwort
  > II. Auffinden von Beweismitteln. Zu den Beweismitteln (→ § 94 Rn. 4 ff.) gehören auch die nur in § 103 erwähnten Spuren (SK-StPO/Jäger/Wohlers Rn. 21) u. Personen, die zu Beweiszwecken in Augenschein ...

#### ours-mxbai-voyage — Top 3
- **[Judge=3]** `§ 102 StPO – Rn. 102` — Direkt relevant: Kern von § 102 StPO Durchsuchungsvoraussetzungen
  > 102 Bei dem, welcher als Täter oder Teilnehmer einer Straftat oder der Datenhehlerei, Begünstigung, Strafvereitelung oder Hehlerei  Köhler    Ermittlungsmaßnahmen  verdächtig ist, kann eine Durchsuchu...
- **[Judge=3]** `§ 102 StPO – Rn. 10` — Direkt relevant: Durchsuchungsvoraussetzungen und Verhältnismäßigkeitsgrundsatz
  > II. Auffinden von Beweismitteln. Zu den Beweismitteln (→ § 94 Rn. 4 ff.) gehören auch die nur in § 103 erwähnten Spuren (SK-StPO/Jäger/Wohlers Rn. 21) u. Personen, die zu Beweiszwecken in Augenschein ...
- **[Judge=3]** `§ 102 StPO – Rn. 3` — Direkt relevant: behandelt Durchsuchungsvoraussetzungen nach StPO
  > **Teilnehmer** nach §§ 25 ff. StGB, nicht die sog. notwendigen Teilnehmer (zum Begriff: Fischer/Fischer StGB Vor § 25 Rn. 7), stehen den Tatverdächtigen gleich. Bei jedem v. ihnen sowie bei den der Be...

### q11 — alltagssprache

**Query:** Was passiert wenn jemand luegt damit er Geld bekommt?

**Kontext:** Laienhafte Umschreibung des Betrugstatbestandes

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours-mxbai | 1.00 | 100% | 100% | 3 | 5.3s |
| ours-mxbai-voyage | 1.00 | 100% | 100% | 3 | 5.4s |

#### ours-mxbai — Top 3
- **[Judge=3]** `§ 263 StGB – I. Vermögensbegriff  – Rn. 263` — Definiert exakt Betrug durch Täuschung für Vermögensvorteil
  > 263 (1) Wer in der Absicht, sich oder einem Dritten einen rechtswidrigen Vermögensvorteil zu verschaffen, das Vermögen eines anderen dadurch beschädigt, daß er durch Vorspiegelung falscher oder durch ...
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 176` — Direkt relevant: Betrugstatbestand und Bereicherungsabsicht
  > D. Subjektiver Tatbestand. § 263 setzt Vorsatz voraus; darüber hinaus ist die Absicht rechtswidriger Bereicherung erforderlich.   I. Vorsatz. 1. Täuschungsvorsatz. Der Vorsatz (bedingter Vorsatz genüg...
- **[Judge=3]** `§ 263 StGB – BT. Zweitundzwanzigster Abschnitt – Rn. 69` — Direkt relevant: Betrugstatbestand mit Vermögensverfügung durch Irrtum
  > 69 Anders ist es, wenn der Verfügende seinerseits nur (gutgläubige) Hilfsperson eines bösgläubigen Dritten ist. Hier ist auf den Irrtum des Entscheidungsbefugten abzustellen: Erkennt dieser die Unrich...

#### ours-mxbai-voyage — Top 3
- **[Judge=3]** `§ 263 StGB – I. Vermögensbegriff  – Rn. 263` — Betrugstatbestand entspricht exakt der Suchanfrage
  > 263 (1) Wer in der Absicht, sich oder einem Dritten einen rechtswidrigen Vermögensvorteil zu verschaffen, das Vermögen eines anderen dadurch beschädigt, daß er durch Vorspiegelung falscher oder durch ...
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 176` — Direkt relevant: erklärt Vorsatz bei Betrug
  > D. Subjektiver Tatbestand. § 263 setzt Vorsatz voraus; darüber hinaus ist die Absicht rechtswidriger Bereicherung erforderlich.   I. Vorsatz. 1. Täuschungsvorsatz. Der Vorsatz (bedingter Vorsatz genüg...
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 5` — Direkt relevant: Betrugstatbestand mit Täuschen für Vermögensvorteil
  > 5 C. Grundtatbestand, Abs. 1. Tathandlung ist das Täuschen einer natürlichen Person (vgl. NStZ 2005, 213) über Tatsachen. Erfolg dieser Handlung muss ein Irrtum des Täuschungsadressaten sein; dieser m...

### q12 — alltagssprache

**Query:** Wann muss jemand ins Gefaengnis waehrend die Tat noch nicht bewiesen ist?

**Kontext:** Untersuchungshaft, §§ 112 ff. StPO

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours-mxbai | 1.00 | 100% | 100% | 3 | 5.7s |
| ours-mxbai-voyage | 1.00 | 100% | 100% | 3 | 5.7s |

#### ours-mxbai — Top 3
- **[Judge=3]** `§ 112 StPO – Rn. 112` — Beantwortet direkt Untersuchungshaft-Voraussetzungen ohne Beweis
  > 112 (1) ¹ Die Untersuchungshaft darf gegen den Beschuldigten angeordnet werden, wenn er der Tat dringend verdächtig ist und ein Haftgrund besteht. ² Sie darf nicht angeordnet werden, wenn sie zu der B...
- **[Judge=3]** `§ 112 StPO – III. Flucht (Abs – Rn. 23` — Behandelt direkt Haftgruende der Untersuchungshaft
  > Bei einer besonders hohen Straferwartung braucht daher nur geprüft zu werden, ob Umstände vorhanden sind, die die hieraus herzuleitende Fluchtgefahr ausräumen können (KG StV 1996, 383; OLG München Str...
- **[Judge=3]** `§ 112 StPO – Rn. 112` — Direkt relevant: Haftbefehl-Voraussetzungen, dringender Tatverdacht
  > Haftunfähigkeit des Beschuldigten schließt den Erlass des Haftbefehls nicht aus, sondern hindert nur seinen Vollzug (OLG Düsseldorf JZ 1984, 248; OLG Frankfurt a.M. NJW 1968, 2302; OLG Nürnberg OLGSt ...

#### ours-mxbai-voyage — Top 3
- **[Judge=3]** `§ 112 StPO – Rn. 112` — Beantwortet direkt Voraussetzungen für Untersuchungshaft
  > 112 (1) ¹ Die Untersuchungshaft darf gegen den Beschuldigten angeordnet werden, wenn er der Tat dringend verdächtig ist und ein Haftgrund besteht. ² Sie darf nicht angeordnet werden, wenn sie zu der B...
- **[Judge=3]** `§ 112 StPO – III. Flucht (Abs – Rn. 23` — Direkt relevant: behandelt Haftgründe der Untersuchungshaft
  > Bei einer besonders hohen Straferwartung braucht daher nur geprüft zu werden, ob Umstände vorhanden sind, die die hieraus herzuleitende Fluchtgefahr ausräumen können (KG StV 1996, 383; OLG München Str...
- **[Judge=3]** `§ 112 StPO – Rn. 112` — Erklärt direkt Haftbefehlsvoraussetzungen und dringenden Tatverdacht
  > Haftunfähigkeit des Beschuldigten schließt den Erlass des Haftbefehls nicht aus, sondern hindert nur seinen Vollzug (OLG Düsseldorf JZ 1984, 248; OLG Frankfurt a.M. NJW 1968, 2302; OLG Nürnberg OLGSt ...

### q13 — stpo-prozess

**Query:** Welche Voraussetzungen hat die Untersuchungshaft wegen Fluchtgefahr?

**Kontext:** § 112 Abs. 2 Nr. 2 StPO Fluchtgefahr

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours-mxbai | 0.94 | 60% | 67% | 3 | 4.8s |
| ours-mxbai-voyage | 1.00 | 100% | 100% | 3 | 6.9s |

#### ours-mxbai — Top 3
- **[Judge=3]** `§ 112 StPO – Rn. 112` — Enthält § 112 Abs. 2 Nr. 2 StPO Fluchtgefahr direkt
  > 112 (1) ¹ Die Untersuchungshaft darf gegen den Beschuldigten angeordnet werden, wenn er der Tat dringend verdächtig ist und ein Haftgrund besteht. ² Sie darf nicht angeordnet werden, wenn sie zu der B...
- **[Judge=1]** `§ 112 StPO – III. Flucht (Abs – Rn. 23` — Behandelt Verdunkelungsgefahr, nicht Fluchtgefahr
  > Bei einer besonders hohen Straferwartung braucht daher nur geprüft zu werden, ob Umstände vorhanden sind, die die hieraus herzuleitende Fluchtgefahr ausräumen können (KG StV 1996, 383; OLG München Str...
- **[Judge=3]** `§ 112 StPO – III. Flucht (Abs – Rn. 16` — Direkt relevant zu Fluchtgefahr nach § 112 Abs. 2 Nr. 2
  > 16 Bei Ergreifung des Beschuldigten aufgrund des nach Abs. 2 Nr. 1 erlassenen Haftbefehls entfällt der Haftgrund der Flucht. In der Regel wird die vorherige Flucht aber die Aufrechterhaltung des Haftb...

#### ours-mxbai-voyage — Top 3
- **[Judge=3]** `§ 112 StPO – Rn. 112` — Zentrale Norm für Fluchtgefahr-Voraussetzungen direkt enthalten
  > 112 (1) ¹ Die Untersuchungshaft darf gegen den Beschuldigten angeordnet werden, wenn er der Tat dringend verdächtig ist und ein Haftgrund besteht. ² Sie darf nicht angeordnet werden, wenn sie zu der B...
- **[Judge=3]** `§ 112 StPO – III. Flucht (Abs – Rn. 17 (Teil 1)` — Behandelt direkt Fluchtgefahr-Voraussetzungen nach § 112 Abs. 2 Nr. 2 StPO
  > 17 IV. Fluchtgefahr (Abs. 2 Nr. 2). Fluchtgefahr (Abs. 2 Nr. 2) besteht, wenn die Würdigung der Umstände des Falles es wahrscheinlicher macht, dass sich der Beschuldigte dem Strafverfahren entziehen, ...
- **[Judge=3]** `§ 112 StPO – III. Flucht (Abs – Rn. 17` — Direkt relevant: Fluchtgefahr-Voraussetzungen § 112 StPO
  > Die Beurteilung der Fluchtgefahr erfordert die Berücksichtigung aller Umstände des Falles, insbes. der Art der dem Beschuldigten vorgeworfenen Tat, der Persönlichkeit des Beschuldigten, seiner Lebensv...

### q14 — stpo-prozess

**Query:** Wie lange darf die Untersuchungshaft maximal dauern?

**Kontext:** § 121 StPO Sechs-Monats-Grenze, Haftpruefung OLG

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours-mxbai | 0.99 | 100% | 100% | 3 | 5.3s |
| ours-mxbai-voyage | 1.00 | 100% | 100% | 3 | 5.1s |

#### ours-mxbai — Top 3
- **[Judge=3]** `§ 121 StPO – Rn. 1` — Direkt relevant: behandelt Höchstgrenzen der Untersuchungshaft
  > Eine absolute Höchstgrenze für die Dauer v. UHaft sieht weder die StPO noch die EMRK vor (EGMR EuGRZ 1993, 384). Es kommt auf eine Abwägung aller Umstände des Einzelfalls an. Eine ein Jahr übersteigen...
- **[Judge=3]** `§ 121 StPO – Rn. 121` — Direkt relevant: regelt Sechs-Monats-Grenze der Untersuchungshaft
  > 121 (1) Solange kein Urteil ergangen ist, das auf Freiheitsstrafe oder eine freiheitsentziehende Maßregel der Besserung und Sicherung erkennt, darf der Vollzug der Untersuchungshaft wegen derselben Ta...
- **[Judge=2]** `§ 121 StPO – Rn. 8 (Teil 1)` — Behandelt Untersuchungshaft zeitliche Aspekte, nicht direkt maximale Dauer
  > 8 II. Zeitliche Geltung der Beschränkungen der UHaft. Bis zu einem auf Freiheitsentziehung lautenden Urteil (Freiheitsstrafe mit o. ohne Bewährung o. freiheitsentziehende Sicherungsmaßregeln) gelten d...

#### ours-mxbai-voyage — Top 3
- **[Judge=3]** `§ 121 StPO – Rn. 1` — Direkt relevant: behandelt 6-Monats-Grenze und OLG-Verlängerung
  > 1 A. Beschleunigungsgebot. Einen Anspruch auf beschleunigte Aburteilung hat der in UHaft (und einstweiliger Unterbringung) befindliche Beschuldigte nach Art. 5 Abs. 3 S. 2 EMRK (→ EMRK Art. 5 Rn. 10 f...
- **[Judge=3]** `§ 121 StPO – Rn. 121` — Direkt relevant: Maximaldauer Untersuchungshaft, zentrale Sechs-Monats-Grenze
  > 121 (1) Solange kein Urteil ergangen ist, das auf Freiheitsstrafe oder eine freiheitsentziehende Maßregel der Besserung und Sicherung erkennt, darf der Vollzug der Untersuchungshaft wegen derselben Ta...
- **[Judge=3]** `§ 121 StPO – Rn. 1` — Beantwortet direkt maximale Dauer der Untersuchungshaft
  > Eine absolute Höchstgrenze für die Dauer v. UHaft sieht weder die StPO noch die EMRK vor (EGMR EuGRZ 1993, 384). Es kommt auf eine Abwägung aller Umstände des Einzelfalls an. Eine ein Jahr übersteigen...

### q15 — stpo-prozess

**Query:** Was regelt § 136 StPO zur Beschuldigtenvernehmung?

**Kontext:** Belehrungspflichten, Recht auf Verteidiger

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours-mxbai | 0.92 | 100% | 100% | 2 | 4.7s |
| ours-mxbai-voyage | 0.91 | 100% | 100% | 2 | 5.0s |

#### ours-mxbai — Top 3
- **[Judge=2]** `§ 500 StPO – ILL. für das Strafverfahren und das Bußgeldverf` — Behandelt Beschuldigtenvernehmung, aber nicht § 136 StPO direkt
  > (4) Zeugen können zur Aufenthaltsermittlung ausgeschrieben werden.  (5) Für die internationale Fahndung nach Personen, einschließlich der Fahndung nach Personen im SIS und aufgrund eines Europäischen ...
- **[Judge=3]** `§ 114b StPO – I. Abs – Rn. 5` — Behandelt direkt § 136 StPO Belehrungspflichten und Verteidiger
  > 5 II. Abs. 2 S. 1 Nr. 2–4. Hier wird die auch nach § 136 Abs. 1 S. 2, 3 und § 163a Abs. 3 S. 2, 4 vor Beginn der ersten richterlichen bzw. staatsanwaltschaftlichen o. polizeilichen Vernehmung bestehen...
- **[Judge=2]** `StPO – III. Steuerstrafverfahren – Rn. 79` — Behandelt Belehrungspflichten nach § 136 StPO thematisch
  > 79 3. Die informatorische Befragung der Tatverdächtigen, die nach diesen Grundsätzen noch keine Beschuldigten sind, ist Zeugenvernehmung. Die Bestrebungen des Schrifttums, neben Beschuldigte u. Zeugen...

#### ours-mxbai-voyage — Top 3
- **[Judge=2]** `§ 500 StPO – ILL. für das Strafverfahren und das Bußgeldverf` — Behandelt Beschuldigtenvernehmung, aber nicht § 136 StPO direkt
  > (4) Zeugen können zur Aufenthaltsermittlung ausgeschrieben werden.  (5) Für die internationale Fahndung nach Personen, einschließlich der Fahndung nach Personen im SIS und aufgrund eines Europäischen ...
- **[Judge=2]** `§ 114b StPO – Rn. 6` — Behandelt Belehrungspflichten, aber bei Verhaftung, nicht Vernehmung
  > 6 D. Umfassende Geltung der Vorschrift. Nicht nur für Verhaftungen nach §§ 112 ff. gilt die Vorschr., sondern auch für solche nach § 230 Abs. 2, 236, 329 Abs. 4 S. 1 und § 412 S. 1. Sie ist auch auf b...
- **[Judge=3]** `§ 114b StPO – I. Abs – Rn. 5` — Direkt relevant: behandelt § 136 StPO Belehrungspflichten
  > 5 II. Abs. 2 S. 1 Nr. 2–4. Hier wird die auch nach § 136 Abs. 1 S. 2, 3 und § 163a Abs. 3 S. 2, 4 vor Beginn der ersten richterlichen bzw. staatsanwaltschaftlichen o. polizeilichen Vernehmung bestehen...

### q16 — cross-reference

**Query:** Worin unterscheidet sich Betrug von Unterschlagung?

**Kontext:** Abgrenzung § 263 vs § 246 StGB

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours-mxbai | 0.89 | 80% | 100% | 2 | 5.8s |
| ours-mxbai-voyage | 0.92 | 100% | 100% | 2 | 5.6s |

#### ours-mxbai — Top 3
- **[Judge=2]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 76` — Thematisch relevant, behandelt Betrugsabgrenzung aber nicht Unterschlagung
  > 4. Dreiecksbetrug. Da die Getäuschte und die verfügende, nicht aber die verfügende und die geschädigte Person identisch sein müssen, ist der Tatbestand des § 263 nur erfüllt, wenn die Vermögensverfügu...
- **[Judge=2]** `§ 263 StGB – BT. Zweitundzwanzigster Abschnitt – Rn. 69` — Behandelt Betrug, aber nicht Abgrenzung zur Unterschlagung
  > 69 Anders ist es, wenn der Verfügende seinerseits nur (gutgläubige) Hilfsperson eines bösgläubigen Dritten ist. Hier ist auf den Irrtum des Entscheidungsbefugten abzustellen: Erkennt dieser die Unrich...
- **[Judge=3]** `§ 263 StGB – I. Vermögensbegriff  – Rn. 263` — Vollständige Definition der Betrugsmerkmale gemäß § 263
  > 263 (1) Wer in der Absicht, sich oder einem Dritten einen rechtswidrigen Vermögensvorteil zu verschaffen, das Vermögen eines anderen dadurch beschädigt, daß er durch Vorspiegelung falscher oder durch ...

#### ours-mxbai-voyage — Top 3
- **[Judge=2]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 76` — Behandelt Betrug, aber nicht Unterschlagungsabgrenzung
  > 4. Dreiecksbetrug. Da die Getäuschte und die verfügende, nicht aber die verfügende und die geschädigte Person identisch sein müssen, ist der Tatbestand des § 263 nur erfüllt, wenn die Vermögensverfügu...
- **[Judge=3]** `§ 263 StGB – I. Vermögensbegriff  – Rn. 263` — Enthält vollständigen Betrug-Tatbestand für direkte Abgrenzung
  > 263 (1) Wer in der Absicht, sich oder einem Dritten einen rechtswidrigen Vermögensvorteil zu verschaffen, das Vermögen eines anderen dadurch beschädigt, daß er durch Vorspiegelung falscher oder durch ...
- **[Judge=2]** `§ 242 StGB – BT. Neunzehnter Abschnitt – Rn. 25` — Behandelt Abgrenzung Diebstahl/Betrug, nicht direkt Betrug/Unterschlagung
  > In Fällen des Trickdiebstahls ist die Wegnahme von einer (irrtums- oder nötigungsbedingten) Vermögensverfügung und daher Diebstahl von Betrug und Erpressung abzugrenzen; §§ 242 und 253, 263 schließen ...

### q17 — cross-reference

**Query:** Was sind die Unterschiede zwischen Diebstahl und Raub?

**Kontext:** § 242 vs § 249 StGB — Abgrenzung durch Gewalt/Drohung

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours-mxbai | 1.00 | 80% | 100% | 3 | 7.5s |
| ours-mxbai-voyage | 0.99 | 100% | 100% | 3 | 5.4s |

#### ours-mxbai — Top 3
- **[Judge=3]** `§ 249 StGB – BT. Zwanzigster Abschnitt – Rn. 15` — Direkter Vergleich Raub-Diebstahl, zentrale Abgrenzungskriterien
  > G. Subjektiver Tatbestand. Der Vorsatz muss entsprechend der Doppelnatur des Raubs sowohl Wegnahme (vgl. dazu → § 242 Rn. 29 ff.) als auch Nötigung (→ § 240 Rn. 53 f.) sowie deren Verknüpfung umfassen...
- **[Judge=3]** `§ 249 StGB` — Direkt relevant: Unterscheidung Raub/räuberische Erpressung, Wegnahme-Tatbestand
  > NStZ 2023, 351). Danach ist § 249 gegenüber § 255 ein spezielles Delikt; in jedem Raub liegt eine räuberische Erpressung (aA die hM in der Literatur). Die Unterscheidung richtet sich nach dem äußeren ...
- **[Judge=3]** `§ 241a StGB – BT. Achtzchniter Abschnitt – Rn. 242` — Definiert direkt Diebstahl-Tatbestand für Abgrenzung zum Raub
  > 242 (1) Wer eine fremde bewegliche Sache einem anderen in der Absicht wegnimmt, die Sache sich oder einem Dritten rechtswidrig zuzueignen, wird mit Freiheitsstrafe bis zu fünf Jahren oder mit Geldstra...

#### ours-mxbai-voyage — Top 3
- **[Judge=3]** `§ 249 StGB` — Direkt relevante Abgrenzung zwischen Raub und Erpressung
  > NStZ 2023, 351). Danach ist § 249 gegenüber § 255 ein spezielles Delikt; in jedem Raub liegt eine räuberische Erpressung (aA die hM in der Literatur). Die Unterscheidung richtet sich nach dem äußeren ...
- **[Judge=3]** `§ 248c StGB – G. Konkurrenzen – Rn. 249` — Definiert Raub direkt, zentral für Abgrenzung zu Diebstahl
  > 249 (1) Wer mit Gewalt gegen eine Person oder unter Anwendung von Drohungen mit gegenwärtiger Gefahr für Leib oder Leben eine fremde bewegliche Sache einem anderen in der Absicht wegnimmt, die Sache s...
- **[Judge=3]** `§ 249 StGB – BT. Zwanzigster Abschnitt – Rn. 15` — Direkt relevant: behandelt subjektiven Tatbestand Raub/Diebstahl-Abgrenzung
  > G. Subjektiver Tatbestand. Der Vorsatz muss entsprechend der Doppelnatur des Raubs sowohl Wegnahme (vgl. dazu → § 242 Rn. 29 ff.) als auch Nötigung (→ § 240 Rn. 53 f.) sowie deren Verknüpfung umfassen...

### q18 — cross-reference

**Query:** Wann wird Betrug zu Computerbetrug und umgekehrt?

**Kontext:** § 263 vs § 263a StGB — Abgrenzung bei elektronischer Datenverarbeitung

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours-mxbai | 0.91 | 40% | 33% | 3 | 6.0s |
| ours-mxbai-voyage | 0.82 | 40% | 67% | 1 | 5.5s |

#### ours-mxbai — Top 3
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 58` — Direkte Abgrenzung Betrug/Computerbetrug bei automatisierten Verfahren
  > 58 Im Geschäftsverkehr wird sich, wer die Berechtigung eines Leistungsverlangens oder -auftrags nicht zu prüfen hat, hierüber idR auch keine (richtigen oder falschen) Gedanken machen (NStZ 1997, 281; ...
- **[Judge=0]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 114` — Behandelt nur Vermögensschäden, nicht Abgrenzung 263/263a
  > 114 a) Quantifizierbarkeit der Vermögensminderung. Die Vermögensminderung muss quantifizierbar sein (RGSt 16, 4; 44, 249; BGHSt 16, 321). Grds. nicht ausreichend ist eine nicht quantifizierbare Einbuß...
- **[Judge=0]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 263 (Tei` — Nur Literaturverzeichnis, keine inhaltlichen Abgrenzungskriterien
  > Fischer/Lutz    Betrug und Untreue   schende Warnung": Eine Drohung?, FS Puppe, 2011, 1217; Kupper, Mengenbegriffe im Strafgesetzbuch, FS Kohlmann, 2003, 133; Lampe, Personales Unrecht im Betrug, FS O...

#### ours-mxbai-voyage — Top 3
- **[Judge=1]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 62` — Betrug allgemein, aber keine Abgrenzung zu Computerbetrug
  > Die Kausalität der Täuschung für den Irrtum und dessen Kausalität für die Vermögensverfügung müssen im Einzelfall festgestellt sein. Mitverursachung reicht aus. Dabei darf das Gericht auch bei Serien-...
- **[Judge=2]** `§ 263 StGB – I. Vermögensbegriff  – Rn. 263` — Betrug-Tatbestand relevant, aber keine Abgrenzung zu Computerbetrug
  > 263 (1) Wer in der Absicht, sich oder einem Dritten einen rechtswidrigen Vermögensvorteil zu verschaffen, das Vermögen eines anderen dadurch beschädigt, daß er durch Vorspiegelung falscher oder durch ...
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 58` — Direkte Abgrenzung § 263/§ 263a bei automatisierten Verfahren
  > 58 Im Geschäftsverkehr wird sich, wer die Berechtigung eines Leistungsverlangens oder -auftrags nicht zu prüfen hat, hierüber idR auch keine (richtigen oder falschen) Gedanken machen (NStZ 1997, 281; ...