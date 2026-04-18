# RAG Benchmark Report

_Generiert: 2026-04-18T18:58:24_


- Queries: **18**
- Top-K: **5**
- Systeme: ours, ours-mxbai

## Gesamtvergleich

| Metrik | ours | ours-mxbai |
|--------|--------|--------|
| nDCG@10 | 0.960 | 0.979 |
| Relevance@10 | 85.6% | 84.4% |
| Relevance@3 | 87.0% | 94.4% |
| Top-1-Score | 2.72 | 2.83 |
| Mean-Score | 2.50 | 2.50 |
| Latenz (s) | 5.87 | 5.87 |

## Nach Kategorie


### alltagssprache

| Metrik | ours | ours-mxbai |
|--------|--------|--------|
| nDCG@10 | 0.983 | 0.994 |
| Relevance@10 | 100.0% | 95.0% |
| Relevance@3 | 100.0% | 100.0% |

### cross-reference

| Metrik | ours | ours-mxbai |
|--------|--------|--------|
| nDCG@10 | 0.920 | 0.979 |
| Relevance@10 | 66.7% | 86.7% |
| Relevance@3 | 66.7% | 100.0% |

### exakte-paragraphen

| Metrik | ours | ours-mxbai |
|--------|--------|--------|
| nDCG@10 | 0.988 | 1.000 |
| Relevance@10 | 100.0% | 90.0% |
| Relevance@3 | 100.0% | 100.0% |

### konzept

| Metrik | ours | ours-mxbai |
|--------|--------|--------|
| nDCG@10 | 0.938 | 0.959 |
| Relevance@10 | 75.0% | 65.0% |
| Relevance@3 | 66.7% | 75.0% |

### stpo-prozess

| Metrik | ours | ours-mxbai |
|--------|--------|--------|
| nDCG@10 | 0.962 | 0.960 |
| Relevance@10 | 80.0% | 86.7% |
| Relevance@3 | 100.0% | 100.0% |

## Detail pro Query


### q01 — exakte-paragraphen

**Query:** Welche Voraussetzungen hat der gewerbsmaessige Bandenbetrug nach § 263 Abs. 5 StGB?

**Kontext:** Qualifikationstatbestand des Bandenbetrugs im Fischer-Kommentar

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours | 0.99 | 100% | 100% | 3 | 7.4s |
| ours-mxbai | 1.00 | 80% | 100% | 3 | 6.2s |

#### ours — Top 3
- **[Judge=3]** `§ 263 StGB – BT. Zweijundzwanzigster Abschnitt – Rn. 213` — Direkt relevant, behandelt Qualifikationstatbestände § 263 Abs. 5
  > 213 Sind beide Varianten erfüllt, ist eine Qualifikation nach Abs. 5 gegeben. Die Abgrenzung des Abs. 3 Nr. 1 zum Verbrechen nach Abs. 5 ist in Fällen bandenmäßiger Begehung schwierig, denn eine auf f...
- **[Judge=3]** `§ 263 StGB – BT. Zweriindzwanzigster Abschnitt – Rn. 225` — Beantwortet direkt die Frage zu § 263 Abs. 5
  > IV. Qualifikation (Abs. 5). Abs. 5 enthält einen Qualifikationstatbestand, der die Tat in Fällen kumulativ gewerbs- und bandenmäßiger Begehung zum Verbrechen macht. Die Qualifikation ist in die Urteil...
- **[Judge=3]** `§ 263 StGB – I. Vermögensbegriff  – Rn. 263` — Enthält § 263 Abs. 5 mit allen Tatbestandsmerkmalen
  > 263 (1) Wer in der Absicht, sich oder einem Dritten einen rechtswidrigen Vermögensvorteil zu verschaffen, das Vermögen eines anderen dadurch beschädigt, daß er durch Vorspiegelung falscher oder durch ...

#### ours-mxbai — Top 3
- **[Judge=3]** `§ 263 StGB – I. Vermögensbegriff  – Rn. 263` — Enthält direkt § 263 Abs. 5 StGB Tatbestandsmerkmale
  > 263 (1) Wer in der Absicht, sich oder einem Dritten einen rechtswidrigen Vermögensvorteil zu verschaffen, das Vermögen eines anderen dadurch beschädigt, daß er durch Vorspiegelung falscher oder durch ...
- **[Judge=3]** `§ 263 StGB – BT. Zweriindzwanzigster Abschnitt – Rn. 225` — Direkt relevant: behandelt exakt § 263 Abs. 5 StGB Voraussetzungen
  > IV. Qualifikation (Abs. 5). Abs. 5 enthält einen Qualifikationstatbestand, der die Tat in Fällen kumulativ gewerbs- und bandenmäßiger Begehung zum Verbrechen macht. Die Qualifikation ist in die Urteil...
- **[Judge=3]** `§ 263 StGB – BT. Zweijundzwanzigster Abschnitt – Rn. 213` — Direkt relevant: behandelt Abs. 5 Qualifikationstatbestand
  > 213 Sind beide Varianten erfüllt, ist eine Qualifikation nach Abs. 5 gegeben. Die Abgrenzung des Abs. 3 Nr. 1 zum Verbrechen nach Abs. 5 ist in Fällen bandenmäßiger Begehung schwierig, denn eine auf f...

### q02 — exakte-paragraphen

**Query:** Was regelt § 112 StPO zur Untersuchungshaft?

**Kontext:** Anordnungsvoraussetzungen der U-Haft (dringender Tatverdacht, Haftgrund) im Schmitt/Koehler

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours | 0.99 | 100% | 100% | 3 | 4.7s |
| ours-mxbai | 1.00 | 100% | 100% | 3 | 4.7s |

#### ours — Top 3
- **[Judge=3]** `§ 112 StPO – Rn. 112` — Direkte Antwort: § 112 StPO Anordnungsvoraussetzungen U-Haft
  > 112 (1) ¹ Die Untersuchungshaft darf gegen den Beschuldigten angeordnet werden, wenn er der Tat dringend verdächtig ist und ein Haftgrund besteht. ² Sie darf nicht angeordnet werden, wenn sie zu der B...
- **[Judge=3]** `§ 112 StPO – Rn. 112` — Behandelt direkt § 112 StPO Haftbefehlsvoraussetzungen
  > Haftunfähigkeit des Beschuldigten schließt den Erlass des Haftbefehls nicht aus, sondern hindert nur seinen Vollzug (OLG Düsseldorf JZ 1984, 248; OLG Frankfurt a.M. NJW 1968, 2302; OLG Nürnberg OLGSt ...
- **[Judge=3]** `§ 112 StPO – III. Flucht (Abs – Rn. 23` — Direkt relevant: Haftgruende nach § 112 StPO
  > Bei einer besonders hohen Straferwartung braucht daher nur geprüft zu werden, ob Umstände vorhanden sind, die die hieraus herzuleitende Fluchtgefahr ausräumen können (KG StV 1996, 383; OLG München Str...

#### ours-mxbai — Top 3
- **[Judge=3]** `§ 112 StPO – Rn. 112` — Direkter Gesetzestext mit allen Anordnungsvoraussetzungen
  > 112 (1) ¹ Die Untersuchungshaft darf gegen den Beschuldigten angeordnet werden, wenn er der Tat dringend verdächtig ist und ein Haftgrund besteht. ² Sie darf nicht angeordnet werden, wenn sie zu der B...
- **[Judge=3]** `§ 112 StPO – Rn. 112` — Direkt relevant zu § 112 StPO Haftvoraussetzungen
  > Haftunfähigkeit des Beschuldigten schließt den Erlass des Haftbefehls nicht aus, sondern hindert nur seinen Vollzug (OLG Düsseldorf JZ 1984, 248; OLG Frankfurt a.M. NJW 1968, 2302; OLG Nürnberg OLGSt ...
- **[Judge=3]** `§ 112 StPO – III. Flucht (Abs – Rn. 23` — Direkt relevant: § 112 StPO Haftgründe Flucht-/Verdunkelungsgefahr
  > Bei einer besonders hohen Straferwartung braucht daher nur geprüft zu werden, ob Umstände vorhanden sind, die die hieraus herzuleitende Fluchtgefahr ausräumen können (KG StV 1996, 383; OLG München Str...

### q03 — exakte-paragraphen

**Query:** Welche Haftgruende nennt § 112 Abs. 2 StPO?

**Kontext:** Fluchtgefahr, Verdunkelungsgefahr, Flucht — im StPO-Kommentar

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours | 0.99 | 100% | 100% | 3 | 5.6s |
| ours-mxbai | 1.00 | 100% | 100% | 3 | 4.9s |

#### ours — Top 3
- **[Judge=3]** `§ 112 StPO – Rn. 112` — Beantwortet direkt die Frage zu Haftgruenden
  > 112 (1) ¹ Die Untersuchungshaft darf gegen den Beschuldigten angeordnet werden, wenn er der Tat dringend verdächtig ist und ein Haftgrund besteht. ² Sie darf nicht angeordnet werden, wenn sie zu der B...
- **[Judge=3]** `§ 112 StPO – III. Flucht (Abs – Rn. 23` — Behandelt direkt Haftgruende des § 112 Abs. 2 StPO
  > Bei einer besonders hohen Straferwartung braucht daher nur geprüft zu werden, ob Umstände vorhanden sind, die die hieraus herzuleitende Fluchtgefahr ausräumen können (KG StV 1996, 383; OLG München Str...
- **[Judge=2]** `§ 112 StPO – III. Flucht (Abs – Rn. 32 (Teil 2)` — Behandelt Verdunkelungsgefahr detailliert, aber keine vollständige Aufzählung
  > Wenn die Verdunkelungshandlungen nicht geeignet sind, die Ermittlung der Wahrheit zu erschweren, darf UHaft nicht angeordnet werden. Der Haftgrund liegt daher nicht vor, wenn der Sachverhalt schon in ...

#### ours-mxbai — Top 3
- **[Judge=3]** `§ 112 StPO – Rn. 112` — Beantwortet die Frage direkt und vollständig
  > 112 (1) ¹ Die Untersuchungshaft darf gegen den Beschuldigten angeordnet werden, wenn er der Tat dringend verdächtig ist und ein Haftgrund besteht. ² Sie darf nicht angeordnet werden, wenn sie zu der B...
- **[Judge=3]** `§ 112 StPO – III. Flucht (Abs – Rn. 23` — Direkte Antwort auf Haftgruende nach § 112 Abs. 2
  > Bei einer besonders hohen Straferwartung braucht daher nur geprüft zu werden, ob Umstände vorhanden sind, die die hieraus herzuleitende Fluchtgefahr ausräumen können (KG StV 1996, 383; OLG München Str...
- **[Judge=3]** `§ 112 StPO – III. Flucht (Abs – Rn. 32 (Teil 2)` — Behandelt direkt Verdunkelungsgefahr aus § 112 Abs. 2 StPO
  > Wenn die Verdunkelungshandlungen nicht geeignet sind, die Ermittlung der Wahrheit zu erschweren, darf UHaft nicht angeordnet werden. Der Haftgrund liegt daher nicht vor, wenn der Sachverhalt schon in ...

### q04 — exakte-paragraphen

**Query:** Was regelt § 102 StPO zur Durchsuchung beim Beschuldigten?

**Kontext:** Durchsuchungsvoraussetzungen beim Verdaechtigen

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours | 0.97 | 100% | 100% | 3 | 4.5s |
| ours-mxbai | 1.00 | 80% | 100% | 3 | 4.5s |

#### ours — Top 3
- **[Judge=3]** `§ 102 StPO – Rn. 102` — Direkt relevant: erklärt § 102 StPO Durchsuchungsvoraussetzungen
  > 102 Bei dem, welcher als Täter oder Teilnehmer einer Straftat oder der Datenhehlerei, Begünstigung, Strafvereitelung oder Hehlerei  Köhler    Ermittlungsmaßnahmen  verdächtig ist, kann eine Durchsuchu...
- **[Judge=2]** `§ 102 StPO – Rn. 10` — Behandelt Durchsuchungsvoraussetzungen, aber nicht spezifisch § 102
  > II. Auffinden von Beweismitteln. Zu den Beweismitteln (→ § 94 Rn. 4 ff.) gehören auch die nur in § 103 erwähnten Spuren (SK-StPO/Jäger/Wohlers Rn. 21) u. Personen, die zu Beweiszwecken in Augenschein ...
- **[Judge=3]** `§ 102 StPO – Rn. 10` — Direkt relevant zu § 102 StPO Durchsuchungsvoraussetzungen
  > 10 III. Sachen. Sachen sind Kleidungsstücke, die der Verdächtige bei sich führt, ohne sie zu tragen, u. seine sonstige bewegliche Habe, gleichgültig, ob sie sich in seinem Umkreis, zB in Gepäckstücken...

#### ours-mxbai — Top 3
- **[Judge=3]** `§ 102 StPO – Rn. 102` — Direkt zu § 102 StPO Durchsuchungsvoraussetzungen
  > 102 Bei dem, welcher als Täter oder Teilnehmer einer Straftat oder der Datenhehlerei, Begünstigung, Strafvereitelung oder Hehlerei  Köhler    Ermittlungsmaßnahmen  verdächtig ist, kann eine Durchsuchu...
- **[Judge=3]** `§ 102 StPO – Rn. 10` — Direkt relevant: behandelt Durchsuchung beim Verdächtigen nach § 102
  > 10 III. Sachen. Sachen sind Kleidungsstücke, die der Verdächtige bei sich führt, ohne sie zu tragen, u. seine sonstige bewegliche Habe, gleichgültig, ob sie sich in seinem Umkreis, zB in Gepäckstücken...
- **[Judge=3]** `§ 102 StPO – Rn. 3` — Regelt direkt § 102 StPO Durchsuchungsvoraussetzungen
  > 3 C. Verdächtige. Der Verdächtige muss die Durchsuchung dulden. Er braucht noch nicht Beschuldigter (→ Einl. Rn. 76 ff.) zu sein; der Tatverdacht gegen ihn muss bei der Anordnung der Maßnahme nicht ei...

### q05 — konzept

**Query:** Wann liegt eine konkludente Taeuschung im Sinne des § 263 StGB vor?

**Kontext:** Taeuschungshandlung durch schluessiges Verhalten

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours | 0.85 | 80% | 67% | 1 | 5.9s |
| ours-mxbai | 0.85 | 60% | 33% | 2 | 5.8s |

#### ours — Top 3
- **[Judge=1]** `§ 263 StGB – I. Vermögensbegriff  – Rn. 263` — Gesetzestext ohne Erläuterung zu konkludenter Täuschung
  > 263 (1) Wer in der Absicht, sich oder einem Dritten einen rechtswidrigen Vermögensvorteil zu verschaffen, das Vermögen eines anderen dadurch beschädigt, daß er durch Vorspiegelung falscher oder durch ...
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 14` — Direkt relevant: Definition konkludente Täuschung durch Verhalten
  > Rspr. und hM bejahen darüber hinaus aber die Möglichkeit einer Täuschung durch Unterlassen auch ohne Erklärung gegenüber dem Irrenden (→ Rn. 38; vgl. BGHSt 39, 392 (398); BayObLG NJW 1987, 1654 (mAnm ...
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 263 (Tei` — Erwähnt explizit konkludente Täuschung bei § 263 StGB
  > Heghmanns, Strafbarkeit des „Phishing“ von Bankkontendaten und ihrer Verwertung, wistra 2007, 167; Hilgendorf, Tatsachenaussagen u. Werturteile im Strafrecht, 1998; Hillenkamp, Zum Schutz „deliktische...

#### ours-mxbai — Top 3
- **[Judge=2]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 38` — Behandelt Taeuschung durch Unterlassen, nicht konkludente Taeuschung
  > 38 4. Täuschung durch Unterlassen. Eine Täuschung kann nach hM (aA Grünwald FS H. Mayer, 1966, 281; Kargl ZStW 119 (2007), 250 (287) mwN) auch durch Unterlassen begangen werden, wenn eine Garantenpfli...
- **[Judge=1]** `§ 263 StGB – I. Vermögensbegriff  – Rn. 263` — Gesetzestext ohne konkludente Taeuschung Details
  > 263 (1) Wer in der Absicht, sich oder einem Dritten einen rechtswidrigen Vermögensvorteil zu verschaffen, das Vermögen eines anderen dadurch beschädigt, daß er durch Vorspiegelung falscher oder durch ...
- **[Judge=1]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 176` — Subjektiver Tatbestand, nicht konkludente Taeuschung
  > D. Subjektiver Tatbestand. § 263 setzt Vorsatz voraus; darüber hinaus ist die Absicht rechtswidriger Bereicherung erforderlich.   I. Vorsatz. 1. Täuschungsvorsatz. Der Vorsatz (bedingter Vorsatz genüg...

### q06 — konzept

**Query:** Was ist eine Vermoegensverfuegung und welche Anforderungen stellt die Rechtsprechung?

**Kontext:** Tatbestandsmerkmal der Vermoegensverfuegung beim Betrug

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours | 0.92 | 60% | 33% | 3 | 5.6s |
| ours-mxbai | 1.00 | 60% | 100% | 3 | 6.3s |

#### ours — Top 3
- **[Judge=3]** `§ 263 StGB – BT. Zweitundzwanzigster Abschnitt – Rn. 69` — Direkt relevant: definiert Vermoegensverfuegung, zeigt Rechtsprechungsanforderungen
  > 69 Anders ist es, wenn der Verfügende seinerseits nur (gutgläubige) Hilfsperson eines bösgläubigen Dritten ist. Hier ist auf den Irrtum des Entscheidungsbefugten abzustellen: Erkennt dieser die Unrich...
- **[Judge=1]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 87` — Kausalität der Verfügung, nicht Definition der Verfügung
  > 87 5. Kausalität. Für die Vermögensverfügung muss der täuschungsbedingte Irrtum kausal sein (vgl. BGHSt 24, 257 (260); 24, 386 (389); NStZ 2003, 313 (314 f.); OLG Düsseldorf NJW 1987, 3145); Mitverurs...
- **[Judge=1]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 176` — Subjektiver Tatbestand, nicht Vermoegensverfuegung selbst
  > D. Subjektiver Tatbestand. § 263 setzt Vorsatz voraus; darüber hinaus ist die Absicht rechtswidriger Bereicherung erforderlich.   I. Vorsatz. 1. Täuschungsvorsatz. Der Vorsatz (bedingter Vorsatz genüg...

#### ours-mxbai — Top 3
- **[Judge=3]** `§ 263 StGB – BT. Zweitundzwanzigster Abschnitt – Rn. 69` — Definiert Vermoegensverfuegung und erlaeutert Rechtsprechungsanforderungen
  > 69 Anders ist es, wenn der Verfügende seinerseits nur (gutgläubige) Hilfsperson eines bösgläubigen Dritten ist. Hier ist auf den Irrtum des Entscheidungsbefugten abzustellen: Erkennt dieser die Unrich...
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 76` — Definiert unmittelbare Verfuegung beim Betrug, zentrale Tatbestandsmerkmale
  > 76 3. Unmittelbarkeit der Verfügung. Neben der Freiwilligkeit ist das Merkmal der Unmittelbarkeit nach stRspr und hM das wichtigste Kriterium zur Beschränkung der § 263 unterfallenden Selbstschädigung...
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 74` — Definiert Vermoegensverfuegung und Rechtsprechungsanforderungen direkt
  > 74 2. Verfügungsbewusstsein. Vermögensverfügungen sind nach hM grundsätzlich sowohl als bewusst als auch als unbewusst vermögensmindernde Handlungen möglich; eine aktuelle Vorstellung des Verfügenden ...

### q07 — konzept

**Query:** Was versteht man unter einem Gefaehrdungsschaden beim Betrug?

**Kontext:** Schadensbegriff, schadensgleiche Vermoegensgefaehrdung

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours | 1.00 | 100% | 100% | 3 | 5.2s |
| ours-mxbai | 1.00 | 80% | 100% | 3 | 4.4s |

#### ours — Top 3
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 159` — Direkte Definition des Gefaehrdungsschadens beim Betrug
  > 159 b) Voraussetzungen. aa) Ein Gefährdungsschaden ist gegeben, wenn die Wahrscheinlichkeit des endgültigen Verlusts eines Vermögensbestandteils zum Zeitpunkt der täuschungsbedingten Verfügung so groß...
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 109` — Behandelt direkt Gefaehrdungsschaden und Schadensbegriff beim Betrug
  > VI. Schaden. Vermögensschaden ist ein negativer Saldo zwischen dem Wert des Vermögens vor und nach der irrtumsbedingten Vermögensverfügung des Getäuschten (Prinzip der Gesamtsaldierung; stRspr; vgl. B...
- **[Judge=3]** `§ 263 StGB – BT. Zwei undzwanzigster Abschnitt – Rn. 263` — Direkter Bezug zu Gefaehrdungsschaden beim Betrug
  > **Rechtsprechungsübersicht:** Scholz, Die Entwicklung des Berufs- und Vertragsarztrechts, medstra 2019, 331; 2021, 349; 2022, 355; 2023, 355; 2024, 351.  Weinrich/Wostry, Der Abrechnungsbetrug in der ...

#### ours-mxbai — Top 3
- **[Judge=3]** `§ 263 StGB – BT. Zwei undzwanzigster Abschnitt – Rn. 263 (Te` — Direkt relevant: behandelt explizit Gefaehrdungsschaden beim Betrug
  > Fischer/Lutz    Betrug und Untreue   rechts für das Strafrecht, FS Weber, 2004, 271; Eisele/Bechtel, Der Schadensbegriff bei den Vermögensdelikten, JuS 2018, 97; Ellbogen/Wichmann, Zu Problemen des är...
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 159` — Definiert exakt Gefährdungsschaden beim Betrug
  > 159 b) Voraussetzungen. aa) Ein Gefährdungsschaden ist gegeben, wenn die Wahrscheinlichkeit des endgültigen Verlusts eines Vermögensbestandteils zum Zeitpunkt der täuschungsbedingten Verfügung so groß...
- **[Judge=3]** `§ 263 StGB – BT. Zwei undzwanzigster Abschnitt – Rn. 263` — Direkt relevant: behandelt explizit Gefaehrdungsschaden beim Betrug
  > **Rechtsprechungsübersicht:** Scholz, Die Entwicklung des Berufs- und Vertragsarztrechts, medstra 2019, 331; 2021, 349; 2022, 355; 2023, 355; 2024, 351.  Weinrich/Wostry, Der Abrechnungsbetrug in der ...

### q08 — konzept

**Query:** Wie wird der Vorsatz beim Betrug bestimmt, insbesondere die Bereicherungsabsicht?

**Kontext:** Subjektiver Tatbestand § 263 StGB

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours | 0.98 | 60% | 67% | 3 | 5.4s |
| ours-mxbai | 0.98 | 60% | 67% | 3 | 5.9s |

#### ours — Top 3
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 176` — Direkt relevant: behandelt Vorsatz und Bereicherungsabsicht bei Betrug
  > D. Subjektiver Tatbestand. § 263 setzt Vorsatz voraus; darüber hinaus ist die Absicht rechtswidriger Bereicherung erforderlich.   I. Vorsatz. 1. Täuschungsvorsatz. Der Vorsatz (bedingter Vorsatz genüg...
- **[Judge=3]** `§ 263 StGB – I. Sonstige Vorschriften 239 – Rn. 263 (Teil 1)` — Behandelt direkt Bereicherungsabsicht und subjektiven Tatbestand
  > 3. Einzelne Fallgruppen ... 92 4. Rechtlich missbilligte, sittenwidrige und gesetzeswidrige wirtschaftliche Werte ... 101 VI. Schaden ... 110 1. Grundsätze der Schadensermittlung ... 111 2. Vermögensm...
- **[Judge=1]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 187 (Tei` — Stoffgleichheit nicht Vorsatz/Bereicherungsabsicht
  > 187 1. Stoffgleichheit. Der Vorteil muss die Kehrseite des Schadens und ihm „stoffgleich“ sein; er muss unmittelbare Folge der täuschungsbedingten Verfügung sein, welche den Schaden des Opfers herbeif...

#### ours-mxbai — Top 3
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 176` — Direkt relevant: behandelt Vorsatz und Bereicherungsabsicht § 263
  > D. Subjektiver Tatbestand. § 263 setzt Vorsatz voraus; darüber hinaus ist die Absicht rechtswidriger Bereicherung erforderlich.   I. Vorsatz. 1. Täuschungsvorsatz. Der Vorsatz (bedingter Vorsatz genüg...
- **[Judge=3]** `§ 263 StGB – I. Sonstige Vorschriften 239 – Rn. 263 (Teil 1)` — Direkt relevant: behandelt Bereicherungsabsicht bei § 263
  > 3. Einzelne Fallgruppen ... 92 4. Rechtlich missbilligte, sittenwidrige und gesetzeswidrige wirtschaftliche Werte ... 101 VI. Schaden ... 110 1. Grundsätze der Schadensermittlung ... 111 2. Vermögensm...
- **[Judge=1]** `§ 263 StGB – BT. Zweitundzwanzigster Abschnitt – Rn. 69` — Behandelt Verfügung, nicht subjektiven Tatbestand/Vorsatz
  > 69 Anders ist es, wenn der Verfügende seinerseits nur (gutgläubige) Hilfsperson eines bösgläubigen Dritten ist. Hier ist auf den Irrtum des Entscheidungsbefugten abzustellen: Erkennt dieser die Unrich...

### q09 — alltagssprache

**Query:** Hat der Angeklagte die Kunden über das Internet betrogen?

**Kontext:** Abstrakte Frage zu Internetbetrug, sucht Taeuschungshandlung + Schaden

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours | 0.93 | 100% | 100% | 2 | 5.3s |
| ours-mxbai | 0.98 | 100% | 100% | 3 | 6.2s |

#### ours — Top 3
- **[Judge=2]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 263 (Tei` — Literaturverweise zu Betrug, auch Phishing erwähnt
  > Heghmanns, Strafbarkeit des „Phishing“ von Bankkontendaten und ihrer Verwertung, wistra 2007, 167; Hilgendorf, Tatsachenaussagen u. Werturteile im Strafrecht, 1998; Hillenkamp, Zum Schutz „deliktische...
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 109` — Behandelt Schadensmerkmal bei Betrug - zentral für Internetbetrug
  > VI. Schaden. Vermögensschaden ist ein negativer Saldo zwischen dem Wert des Vermögens vor und nach der irrtumsbedingten Vermögensverfügung des Getäuschten (Prinzip der Gesamtsaldierung; stRspr; vgl. B...
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 28` — Beschreibt konkret Internetbetrug durch taeuschende Scheinrechnungen
  > 28 Solche Scheinrechnungen sind so formuliert, dass sie bei eiligen oder geschäftsunerfahrenen Empfängern den Eindruck der Zahlungspflicht zu erzeugen geeignet sind (vgl. auch Erb ZIS 2011, 354: „Sugg...

#### ours-mxbai — Top 3
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 5` — Definiert zentrale Tatbestandsmerkmale des Betrugs
  > 5 C. Grundtatbestand, Abs. 1. Tathandlung ist das Täuschen einer natürlichen Person (vgl. NStZ 2005, 213) über Tatsachen. Erfolg dieser Handlung muss ein Irrtum des Täuschungsadressaten sein; dieser m...
- **[Judge=2]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 176` — Subjektiver Tatbestand § 263, thematisch relevant zu Betrug
  > D. Subjektiver Tatbestand. § 263 setzt Vorsatz voraus; darüber hinaus ist die Absicht rechtswidriger Bereicherung erforderlich.   I. Vorsatz. 1. Täuschungsvorsatz. Der Vorsatz (bedingter Vorsatz genüg...
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 62` — Zentrale Betrugsmerkmale Täuschung, Irrtum, Kausalität bei Massentaten
  > Die Kausalität der Täuschung für den Irrtum und dessen Kausalität für die Vermögensverfügung müssen im Einzelfall festgestellt sein. Mitverursachung reicht aus. Dabei darf das Gericht auch bei Serien-...

### q10 — alltagssprache

**Query:** Wann darf die Polizei bei jemandem zu Hause suchen?

**Kontext:** Durchsuchungsvoraussetzungen, §§ 102 ff. StPO

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours | 1.00 | 100% | 100% | 3 | 5.7s |
| ours-mxbai | 1.00 | 80% | 100% | 3 | 5.4s |

#### ours — Top 3
- **[Judge=3]** `§ 102 StPO – Rn. 102` — Direkt relevant: behandelt Durchsuchungsvoraussetzungen bei Verdächtigen
  > 102 Bei dem, welcher als Täter oder Teilnehmer einer Straftat oder der Datenhehlerei, Begünstigung, Strafvereitelung oder Hehlerei  Köhler    Ermittlungsmaßnahmen  verdächtig ist, kann eine Durchsuchu...
- **[Judge=3]** `§ 102 StPO – Rn. 10` — Direkt zu Durchsuchungsvoraussetzungen und Verhältnismäßigkeitsprinzip
  > II. Auffinden von Beweismitteln. Zu den Beweismitteln (→ § 94 Rn. 4 ff.) gehören auch die nur in § 103 erwähnten Spuren (SK-StPO/Jäger/Wohlers Rn. 21) u. Personen, die zu Beweiszwecken in Augenschein ...
- **[Judge=3]** `§ 102 StPO – Rn. 3` — Direkt relevant für Durchsuchungsvoraussetzungen und -gegenstände
  > **Teilnehmer** nach §§ 25 ff. StGB, nicht die sog. notwendigen Teilnehmer (zum Begriff: Fischer/Fischer StGB Vor § 25 Rn. 7), stehen den Tatverdächtigen gleich. Bei jedem v. ihnen sowie bei den der Be...

#### ours-mxbai — Top 3
- **[Judge=3]** `§ 102 StPO – Rn. 102` — Zentrale Voraussetzungen der polizeilichen Wohnungsdurchsuchung nach § 102 StPO
  > 102 Bei dem, welcher als Täter oder Teilnehmer einer Straftat oder der Datenhehlerei, Begünstigung, Strafvereitelung oder Hehlerei  Köhler    Ermittlungsmaßnahmen  verdächtig ist, kann eine Durchsuchu...
- **[Judge=3]** `§ 102 StPO – Rn. 3` — Direkt relevant: behandelt Durchsuchungsvoraussetzungen nach StPO
  > **Teilnehmer** nach §§ 25 ff. StGB, nicht die sog. notwendigen Teilnehmer (zum Begriff: Fischer/Fischer StGB Vor § 25 Rn. 7), stehen den Tatverdächtigen gleich. Bei jedem v. ihnen sowie bei den der Be...
- **[Judge=3]** `§ 102 StPO – Rn. 10` — Behandelt direkt Durchsuchungsvoraussetzungen und Verhältnismäßigkeitsgrundsatz
  > II. Auffinden von Beweismitteln. Zu den Beweismitteln (→ § 94 Rn. 4 ff.) gehören auch die nur in § 103 erwähnten Spuren (SK-StPO/Jäger/Wohlers Rn. 21) u. Personen, die zu Beweiszwecken in Augenschein ...

### q11 — alltagssprache

**Query:** Was passiert wenn jemand luegt damit er Geld bekommt?

**Kontext:** Laienhafte Umschreibung des Betrugstatbestandes

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours | 1.00 | 100% | 100% | 3 | 5.2s |
| ours-mxbai | 1.00 | 100% | 100% | 3 | 5.2s |

#### ours — Top 3
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 5` — Direkte Beschreibung des Betrugstatbestandes nach § 263 StGB
  > 5 C. Grundtatbestand, Abs. 1. Tathandlung ist das Täuschen einer natürlichen Person (vgl. NStZ 2005, 213) über Tatsachen. Erfolg dieser Handlung muss ein Irrtum des Täuschungsadressaten sein; dieser m...
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 176` — Behandelt direkt subjektiven Tatbestand bei Betrug
  > D. Subjektiver Tatbestand. § 263 setzt Vorsatz voraus; darüber hinaus ist die Absicht rechtswidriger Bereicherung erforderlich.   I. Vorsatz. 1. Täuschungsvorsatz. Der Vorsatz (bedingter Vorsatz genüg...
- **[Judge=3]** `§ 263 StGB – BT. Zweitundzwanzigster Abschnitt – Rn. 69` — Direkt relevant: Betrug § 263 durch Täuschung
  > 69 Anders ist es, wenn der Verfügende seinerseits nur (gutgläubige) Hilfsperson eines bösgläubigen Dritten ist. Hier ist auf den Irrtum des Entscheidungsbefugten abzustellen: Erkennt dieser die Unrich...

#### ours-mxbai — Top 3
- **[Judge=3]** `§ 263 StGB – I. Vermögensbegriff  – Rn. 263` — Direkt relevant: Definition des Betrugstatbestandes § 263
  > 263 (1) Wer in der Absicht, sich oder einem Dritten einen rechtswidrigen Vermögensvorteil zu verschaffen, das Vermögen eines anderen dadurch beschädigt, daß er durch Vorspiegelung falscher oder durch ...
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 5` — Definiert direkt Betrugstatbestand mit Täuschung und Vermögensschaden
  > 5 C. Grundtatbestand, Abs. 1. Tathandlung ist das Täuschen einer natürlichen Person (vgl. NStZ 2005, 213) über Tatsachen. Erfolg dieser Handlung muss ein Irrtum des Täuschungsadressaten sein; dieser m...
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 176` — Behandelt direkt den subjektiven Tatbestand des Betrugs
  > D. Subjektiver Tatbestand. § 263 setzt Vorsatz voraus; darüber hinaus ist die Absicht rechtswidriger Bereicherung erforderlich.   I. Vorsatz. 1. Täuschungsvorsatz. Der Vorsatz (bedingter Vorsatz genüg...

### q12 — alltagssprache

**Query:** Wann muss jemand ins Gefaengnis waehrend die Tat noch nicht bewiesen ist?

**Kontext:** Untersuchungshaft, §§ 112 ff. StPO

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours | 1.00 | 100% | 100% | 3 | 5.6s |
| ours-mxbai | 1.00 | 100% | 100% | 3 | 5.5s |

#### ours — Top 3
- **[Judge=3]** `§ 112 StPO – Rn. 112` — Direkt relevant: regelt Untersuchungshaft bei dringendem Verdacht
  > 112 (1) ¹ Die Untersuchungshaft darf gegen den Beschuldigten angeordnet werden, wenn er der Tat dringend verdächtig ist und ein Haftgrund besteht. ² Sie darf nicht angeordnet werden, wenn sie zu der B...
- **[Judge=3]** `§ 112 StPO – III. Flucht (Abs – Rn. 23` — Erklaert direkt Haftgruende vor Verurteilung
  > Bei einer besonders hohen Straferwartung braucht daher nur geprüft zu werden, ob Umstände vorhanden sind, die die hieraus herzuleitende Fluchtgefahr ausräumen können (KG StV 1996, 383; OLG München Str...
- **[Judge=3]** `§ 112 StPO – III. Flucht (Abs – Rn. 32 (Teil 2)` — Direkt relevant zu Untersuchungshaft und Verdunkelungsgefahr
  > Wenn die Verdunkelungshandlungen nicht geeignet sind, die Ermittlung der Wahrheit zu erschweren, darf UHaft nicht angeordnet werden. Der Haftgrund liegt daher nicht vor, wenn der Sachverhalt schon in ...

#### ours-mxbai — Top 3
- **[Judge=3]** `§ 112 StPO – Rn. 112` — Direkt relevant: Untersuchungshaft vor Verurteilung geregelt
  > 112 (1) ¹ Die Untersuchungshaft darf gegen den Beschuldigten angeordnet werden, wenn er der Tat dringend verdächtig ist und ein Haftgrund besteht. ² Sie darf nicht angeordnet werden, wenn sie zu der B...
- **[Judge=3]** `§ 112 StPO – Rn. 112` — Direkt relevant: Voraussetzungen fuer Untersuchungshaft, dringender Tatverdacht
  > Haftunfähigkeit des Beschuldigten schließt den Erlass des Haftbefehls nicht aus, sondern hindert nur seinen Vollzug (OLG Düsseldorf JZ 1984, 248; OLG Frankfurt a.M. NJW 1968, 2302; OLG Nürnberg OLGSt ...
- **[Judge=3]** `§ 112 StPO – III. Flucht (Abs – Rn. 23` — Direkt zu Untersuchungshaft, behandelt Flucht- und Verdunkelungsgefahr
  > Bei einer besonders hohen Straferwartung braucht daher nur geprüft zu werden, ob Umstände vorhanden sind, die die hieraus herzuleitende Fluchtgefahr ausräumen können (KG StV 1996, 383; OLG München Str...

### q13 — stpo-prozess

**Query:** Welche Voraussetzungen hat die Untersuchungshaft wegen Fluchtgefahr?

**Kontext:** § 112 Abs. 2 Nr. 2 StPO Fluchtgefahr

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours | 0.99 | 80% | 100% | 3 | 7.2s |
| ours-mxbai | 0.99 | 80% | 100% | 3 | 8.5s |

#### ours — Top 3
- **[Judge=3]** `§ 112 StPO – Rn. 112` — Enthält § 112 Abs. 2 Nr. 2 StPO Fluchtgefahr direkt
  > 112 (1) ¹ Die Untersuchungshaft darf gegen den Beschuldigten angeordnet werden, wenn er der Tat dringend verdächtig ist und ein Haftgrund besteht. ² Sie darf nicht angeordnet werden, wenn sie zu der B...
- **[Judge=3]** `§ 112 StPO – III. Flucht (Abs – Rn. 17 (Teil 1)` — Direkt relevant: definiert Fluchtgefahr-Voraussetzungen nach § 112
  > 17 IV. Fluchtgefahr (Abs. 2 Nr. 2). Fluchtgefahr (Abs. 2 Nr. 2) besteht, wenn die Würdigung der Umstände des Falles es wahrscheinlicher macht, dass sich der Beschuldigte dem Strafverfahren entziehen, ...
- **[Judge=3]** `§ 112 StPO – III. Flucht (Abs – Rn. 16` — Direkt relevant zu Fluchtgefahr nach § 112 Abs. 2 Nr. 2
  > 16 Bei Ergreifung des Beschuldigten aufgrund des nach Abs. 2 Nr. 1 erlassenen Haftbefehls entfällt der Haftgrund der Flucht. In der Regel wird die vorherige Flucht aber die Aufrechterhaltung des Haftb...

#### ours-mxbai — Top 3
- **[Judge=3]** `§ 112 StPO – Rn. 112` — Direkt relevant: § 112 Abs. 2 Nr. 2 StPO Fluchtgefahr
  > 112 (1) ¹ Die Untersuchungshaft darf gegen den Beschuldigten angeordnet werden, wenn er der Tat dringend verdächtig ist und ein Haftgrund besteht. ² Sie darf nicht angeordnet werden, wenn sie zu der B...
- **[Judge=3]** `§ 112 StPO – III. Flucht (Abs – Rn. 17 (Teil 1)` — Direkt relevant: Definition und Voraussetzungen der Fluchtgefahr
  > 17 IV. Fluchtgefahr (Abs. 2 Nr. 2). Fluchtgefahr (Abs. 2 Nr. 2) besteht, wenn die Würdigung der Umstände des Falles es wahrscheinlicher macht, dass sich der Beschuldigte dem Strafverfahren entziehen, ...
- **[Judge=3]** `§ 112 StPO – III. Flucht (Abs – Rn. 16` — Direkt relevant: behandelt Fluchtgefahr nach § 112 Abs. 2 Nr. 2
  > 16 Bei Ergreifung des Beschuldigten aufgrund des nach Abs. 2 Nr. 1 erlassenen Haftbefehls entfällt der Haftgrund der Flucht. In der Regel wird die vorherige Flucht aber die Aufrechterhaltung des Haftb...

### q14 — stpo-prozess

**Query:** Wie lange darf die Untersuchungshaft maximal dauern?

**Kontext:** § 121 StPO Sechs-Monats-Grenze, Haftpruefung OLG

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours | 0.97 | 100% | 100% | 3 | 5.2s |
| ours-mxbai | 0.97 | 100% | 100% | 3 | 5.0s |

#### ours — Top 3
- **[Judge=3]** `§ 121 StPO – Rn. 1` — Direkt relevant: behandelt maximale Dauer der Untersuchungshaft
  > Eine absolute Höchstgrenze für die Dauer v. UHaft sieht weder die StPO noch die EMRK vor (EGMR EuGRZ 1993, 384). Es kommt auf eine Abwägung aller Umstände des Einzelfalls an. Eine ein Jahr übersteigen...
- **[Judge=2]** `§ 121 StPO – Rn. 8 (Teil 1)` — Behandelt Untersuchungshaft zeitliche Beschränkungen, aber nicht direkt maximale Dauer
  > 8 II. Zeitliche Geltung der Beschränkungen der UHaft. Bis zu einem auf Freiheitsentziehung lautenden Urteil (Freiheitsstrafe mit o. ohne Bewährung o. freiheitsentziehende Sicherungsmaßregeln) gelten d...
- **[Judge=3]** `§ 121 StPO – Rn. 121` — Direkt relevant, behandelt exakt Sechs-Monats-Grenze der Untersuchungshaft
  > 121 (1) Solange kein Urteil ergangen ist, das auf Freiheitsstrafe oder eine freiheitsentziehende Maßregel der Besserung und Sicherung erkennt, darf der Vollzug der Untersuchungshaft wegen derselben Ta...

#### ours-mxbai — Top 3
- **[Judge=3]** `§ 121 StPO – Rn. 1` — Behandelt direkt maximale Untersuchungshaftdauer, Höchstgrenzen
  > Eine absolute Höchstgrenze für die Dauer v. UHaft sieht weder die StPO noch die EMRK vor (EGMR EuGRZ 1993, 384). Es kommt auf eine Abwägung aller Umstände des Einzelfalls an. Eine ein Jahr übersteigen...
- **[Judge=2]** `§ 121 StPO – Rn. 8 (Teil 1)` — Behandelt Haftbeschränkungen, nicht maximale Dauer
  > 8 II. Zeitliche Geltung der Beschränkungen der UHaft. Bis zu einem auf Freiheitsentziehung lautenden Urteil (Freiheitsstrafe mit o. ohne Bewährung o. freiheitsentziehende Sicherungsmaßregeln) gelten d...
- **[Judge=3]** `§ 121 StPO – Rn. 121` — Beantwortet direkt die Frage zur Haftdauer
  > 121 (1) Solange kein Urteil ergangen ist, das auf Freiheitsstrafe oder eine freiheitsentziehende Maßregel der Besserung und Sicherung erkennt, darf der Vollzug der Untersuchungshaft wegen derselben Ta...

### q15 — stpo-prozess

**Query:** Was regelt § 136 StPO zur Beschuldigtenvernehmung?

**Kontext:** Belehrungspflichten, Recht auf Verteidiger

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours | 0.93 | 60% | 100% | 2 | 6.6s |
| ours-mxbai | 0.92 | 80% | 100% | 2 | 6.6s |

#### ours — Top 3
- **[Judge=2]** `§ 500 StPO – ILL. für das Strafverfahren und das Bußgeldverf` — Behandelt Beschuldigtenvernehmung, aber nicht § 136 StPO direkt
  > (4) Zeugen können zur Aufenthaltsermittlung ausgeschrieben werden.  (5) Für die internationale Fahndung nach Personen, einschließlich der Fahndung nach Personen im SIS und aufgrund eines Europäischen ...
- **[Judge=3]** `§ 114b StPO – I. Abs – Rn. 5` — Behandelt direkt § 136 StPO Belehrungspflichten und Verteidiger
  > 5 II. Abs. 2 S. 1 Nr. 2–4. Hier wird die auch nach § 136 Abs. 1 S. 2, 3 und § 163a Abs. 3 S. 2, 4 vor Beginn der ersten richterlichen bzw. staatsanwaltschaftlichen o. polizeilichen Vernehmung bestehen...
- **[Judge=3]** `StPO – III. Steuerstrafverfahren – Rn. 25` — Erklärt nemo-tenetur-Prinzip, direkt zu § 136 StPO
  > Das nemo-tenetur-Prinzip (nemo tenetur se ipsum accusare und nemo tenetur se ipsum prodere) o. der Grundsatz der Selbstbelastungsfreiheit bedeutet, dass niemand verpflichtet ist, sich selbst anzuklage...

#### ours-mxbai — Top 3
- **[Judge=2]** `§ 500 StPO – ILL. für das Strafverfahren und das Bußgeldverf` — Belehrungspflicht nach § 136 Abs. 1 erwähnt
  > (4) Zeugen können zur Aufenthaltsermittlung ausgeschrieben werden.  (5) Für die internationale Fahndung nach Personen, einschließlich der Fahndung nach Personen im SIS und aufgrund eines Europäischen ...
- **[Judge=3]** `§ 114b StPO – I. Abs – Rn. 5` — Direkt relevant: behandelt Belehrungspflichten nach § 136 StPO
  > 5 II. Abs. 2 S. 1 Nr. 2–4. Hier wird die auch nach § 136 Abs. 1 S. 2, 3 und § 163a Abs. 3 S. 2, 4 vor Beginn der ersten richterlichen bzw. staatsanwaltschaftlichen o. polizeilichen Vernehmung bestehen...
- **[Judge=2]** `StPO – III. Steuerstrafverfahren – Rn. 79` — Behandelt Belehrungspflichten bei informatorischer Befragung vs. Beschuldigtenvernehmung
  > 79 3. Die informatorische Befragung der Tatverdächtigen, die nach diesen Grundsätzen noch keine Beschuldigten sind, ist Zeugenvernehmung. Die Bestrebungen des Schrifttums, neben Beschuldigte u. Zeugen...

### q16 — cross-reference

**Query:** Worin unterscheidet sich Betrug von Unterschlagung?

**Kontext:** Abgrenzung § 263 vs § 246 StGB

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours | 0.88 | 60% | 67% | 2 | 5.8s |
| ours-mxbai | 0.94 | 80% | 100% | 2 | 6.4s |

#### ours — Top 3
- **[Judge=2]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 186` — Behandelt Bereicherungsabsicht bei § 263, wichtiger Abgrenzungsaspekt
  > 186 II. Bereicherungsabsicht. Die Tat muss subjektiv auf die Erlangung eines rechtswidrigen Vermögensvorteils für den Täuschenden oder einen Dritten gerichtet sein. Vermögensvorteil ist die Erhöhung d...
- **[Judge=1]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 114` — Behandelt Betrug, aber nicht Unterschlagung oder Abgrenzung
  > 114 a) Quantifizierbarkeit der Vermögensminderung. Die Vermögensminderung muss quantifizierbar sein (RGSt 16, 4; 44, 249; BGHSt 16, 321). Grds. nicht ausreichend ist eine nicht quantifizierbare Einbuß...
- **[Judge=3]** `§ 263 StGB – I. Vermögensbegriff  – Rn. 263` — Vollständige Definition Betrug für Abgrenzung zu Unterschlagung
  > 263 (1) Wer in der Absicht, sich oder einem Dritten einen rechtswidrigen Vermögensvorteil zu verschaffen, das Vermögen eines anderen dadurch beschädigt, daß er durch Vorspiegelung falscher oder durch ...

#### ours-mxbai — Top 3
- **[Judge=2]** `§ 247 StGB – BT. Neunzehnter Abschnitt – Rn. 24` — Behandelt Konkurrenzen, erwähnt Abgrenzung § 246/263
  > 24 L. Konkurrenzen im Übrigen. Bei Manifestation des Zueignungswillens hinsichtlich mehrerer Sachen durch eine Ausführungshandlung liegt nur eine Tat vor (wistra 2006, 227 (227 f.)). Zur Abgrenzung vo...
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 76` — Direkt relevant: Abgrenzung Betrug vs Diebstahl/Unterschlagung
  > 4. Dreiecksbetrug. Da die Getäuschte und die verfügende, nicht aber die verfügende und die geschädigte Person identisch sein müssen, ist der Tatbestand des § 263 nur erfüllt, wenn die Vermögensverfügu...
- **[Judge=2]** `§ 263 StGB – BT. Zweitundzwanzigster Abschnitt – Rn. 69` — Behandelt Betrug detailliert, aber keine Unterschlagungsabgrenzung
  > 69 Anders ist es, wenn der Verfügende seinerseits nur (gutgläubige) Hilfsperson eines bösgläubigen Dritten ist. Hier ist auf den Irrtum des Entscheidungsbefugten abzustellen: Erkennt dieser die Unrich...

### q17 — cross-reference

**Query:** Was sind die Unterschiede zwischen Diebstahl und Raub?

**Kontext:** § 242 vs § 249 StGB — Abgrenzung durch Gewalt/Drohung

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours | 1.00 | 100% | 100% | 3 | 7.6s |
| ours-mxbai | 1.00 | 80% | 100% | 3 | 7.4s |

#### ours — Top 3
- **[Judge=3]** `§ 249 StGB` — Direkt relevant: Raub-Tatbestand mit Nötigungsmitteln und Wegnahme
  > NStZ 2023, 351). Danach ist § 249 gegenüber § 255 ein spezielles Delikt; in jedem Raub liegt eine räuberische Erpressung (aA die hM in der Literatur). Die Unterscheidung richtet sich nach dem äußeren ...
- **[Judge=3]** `§ 249 StGB – BT. Zwanzigster Abschnitt – Rn. 15` — Direkt relevant: Abgrenzung Diebstahl/Raub durch Vorsatzelemente
  > G. Subjektiver Tatbestand. Der Vorsatz muss entsprechend der Doppelnatur des Raubs sowohl Wegnahme (vgl. dazu → § 242 Rn. 29 ff.) als auch Nötigung (→ § 240 Rn. 53 f.) sowie deren Verknüpfung umfassen...
- **[Judge=3]** `§ 241a StGB – BT. Achtzchniter Abschnitt – Rn. 242` — Definiert Diebstahl-Tatbestand, direkt relevant für Abgrenzung
  > 242 (1) Wer eine fremde bewegliche Sache einem anderen in der Absicht wegnimmt, die Sache sich oder einem Dritten rechtswidrig zuzueignen, wird mit Freiheitsstrafe bis zu fünf Jahren oder mit Geldstra...

#### ours-mxbai — Top 3
- **[Judge=3]** `§ 249 StGB` — Direkt relevant: Abgrenzung Raub/räuberische Erpressung, Wegnahme, Nötigungsmittel
  > NStZ 2023, 351). Danach ist § 249 gegenüber § 255 ein spezielles Delikt; in jedem Raub liegt eine räuberische Erpressung (aA die hM in der Literatur). Die Unterscheidung richtet sich nach dem äußeren ...
- **[Judge=3]** `§ 249 StGB – BT. Zwanzigster Abschnitt – Rn. 15` — Erklärt subjektive Tatbestandsmerkmale bei Raub vs Diebstahl
  > G. Subjektiver Tatbestand. Der Vorsatz muss entsprechend der Doppelnatur des Raubs sowohl Wegnahme (vgl. dazu → § 242 Rn. 29 ff.) als auch Nötigung (→ § 240 Rn. 53 f.) sowie deren Verknüpfung umfassen...
- **[Judge=3]** `§ 241a StGB – BT. Achtzchniter Abschnitt – Rn. 242` — Zeigt direkten Tatbestand § 242 StGB Diebstahl
  > 242 (1) Wer eine fremde bewegliche Sache einem anderen in der Absicht wegnimmt, die Sache sich oder einem Dritten rechtswidrig zuzueignen, wird mit Freiheitsstrafe bis zu fünf Jahren oder mit Geldstra...

### q18 — cross-reference

**Query:** Wann wird Betrug zu Computerbetrug und umgekehrt?

**Kontext:** § 263 vs § 263a StGB — Abgrenzung bei elektronischer Datenverarbeitung

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours | 0.88 | 40% | 33% | 3 | 7.0s |
| ours-mxbai | 1.00 | 100% | 100% | 3 | 6.8s |

#### ours — Top 3
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 58` — Direkte Abgrenzung § 263/263a bei automatisierten Verfahren
  > 58 Im Geschäftsverkehr wird sich, wer die Berechtigung eines Leistungsverlangens oder -auftrags nicht zu prüfen hat, hierüber idR auch keine (richtigen oder falschen) Gedanken machen (NStZ 1997, 281; ...
- **[Judge=0]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 62` — Behandelt nur § 263, nicht Abgrenzung zu § 263a
  > Die Kausalität der Täuschung für den Irrtum und dessen Kausalität für die Vermögensverfügung müssen im Einzelfall festgestellt sein. Mitverursachung reicht aus. Dabei darf das Gericht auch bei Serien-...
- **[Judge=0]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 114` — Behandelt nur Vermögensschäden, nicht Abgrenzung Betrug/Computerbetrug
  > 114 a) Quantifizierbarkeit der Vermögensminderung. Die Vermögensminderung muss quantifizierbar sein (RGSt 16, 4; 44, 249; BGHSt 16, 321). Grds. nicht ausreichend ist eine nicht quantifizierbare Einbuß...

#### ours-mxbai — Top 3
- **[Judge=3]** `§ 263a StGB – M. Sonstige Vorschriften 40 – Rn. 239` — Direkt relevant: Computerbetrug Tatbestandsmerkmale und Abgrenzung
  > 239 I. Sonstige Vorschriften. FAufsicht §§ 263 Abs. 5, 68 Abs. 1. Zuständigkeit in Wirtschaftsstrafaschen § 74c Abs. 1 Nr. 6, § 74e Nr. 2 GVG iVm § 103 Abs. 2 JGG. TKÜ § 100a Abs. 2 Nr. 1 Buchst. n St...
- **[Judge=3]** `§ 263a StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 23` — Direkte Abgrenzung § 263 vs § 263a bei Vorsatzproblemen
  > 23 G. Subjektiver Tatbestand. Die Tat setzt (bedingten) Vorsatz voraus. Er muss sich auf alle Tatbestandsmerkmale, zu denen auch die Unbefugtheit (→ Rn. 10) gehört, dh auch auf die Voraussetzungen ers...
- **[Judge=3]** `§ 263a StGB – L. Konkurrenzen – Rn. 33` — Behandelt direkt Abgrenzung § 263/263a und Konkurrenzverhältnisse
  > II. Verhältnis zu sonstigen Tatbeständen. § 263a und § 263 schließen sich aus, wenn derselbe Schaden sowohl durch die Manipulationsweisen des § 263a als auch durch Täuschung bewirkt wird. Mit § 263 is...