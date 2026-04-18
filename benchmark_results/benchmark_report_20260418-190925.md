# RAG Benchmark Report

_Generiert: 2026-04-18T19:09:25_


- Queries: **18**
- Top-K: **5**
- Systeme: ours, ours-cohere, ours-mxbai

## Gesamtvergleich

| Metrik | ours | ours-cohere | ours-mxbai |
|--------|--------|--------|--------|
| nDCG@10 | 0.954 | 0.958 | 0.984 |
| Relevance@10 | 90.0% | 82.2% | 82.2% |
| Relevance@3 | 90.7% | 88.9% | 88.9% |
| Top-1-Score | 2.61 | 2.56 | 2.94 |
| Mean-Score | 2.57 | 2.43 | 2.42 |
| Latenz (s) | 5.61 | 5.92 | 5.59 |

## Nach Kategorie


### alltagssprache

| Metrik | ours | ours-cohere | ours-mxbai |
|--------|--------|--------|--------|
| nDCG@10 | 0.997 | 0.949 | 0.992 |
| Relevance@10 | 100.0% | 95.0% | 100.0% |
| Relevance@3 | 100.0% | 91.7% | 100.0% |

### cross-reference

| Metrik | ours | ours-cohere | ours-mxbai |
|--------|--------|--------|--------|
| nDCG@10 | 0.886 | 0.908 | 0.990 |
| Relevance@10 | 80.0% | 60.0% | 40.0% |
| Relevance@3 | 77.8% | 77.8% | 66.7% |

### exakte-paragraphen

| Metrik | ours | ours-cohere | ours-mxbai |
|--------|--------|--------|--------|
| nDCG@10 | 0.991 | 0.997 | 0.988 |
| Relevance@10 | 100.0% | 95.0% | 95.0% |
| Relevance@3 | 100.0% | 100.0% | 100.0% |

### konzept

| Metrik | ours | ours-cohere | ours-mxbai |
|--------|--------|--------|--------|
| nDCG@10 | 0.937 | 0.958 | 0.970 |
| Relevance@10 | 80.0% | 65.0% | 90.0% |
| Relevance@3 | 83.3% | 75.0% | 83.3% |

### stpo-prozess

| Metrik | ours | ours-cohere | ours-mxbai |
|--------|--------|--------|--------|
| nDCG@10 | 0.940 | 0.970 | 0.982 |
| Relevance@10 | 86.7% | 93.3% | 73.3% |
| Relevance@3 | 88.9% | 100.0% | 88.9% |

## Detail pro Query


### q01 — exakte-paragraphen

**Query:** Welche Voraussetzungen hat der gewerbsmaessige Bandenbetrug nach § 263 Abs. 5 StGB?

**Kontext:** Qualifikationstatbestand des Bandenbetrugs im Fischer-Kommentar

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours | 0.99 | 100% | 100% | 3 | 5.8s |
| ours-cohere | 1.00 | 80% | 100% | 3 | 5.9s |
| ours-mxbai | 0.99 | 80% | 100% | 3 | 6.1s |

#### ours — Top 3
- **[Judge=3]** `§ 263 StGB – BT. Zweriindzwanzigster Abschnitt – Rn. 225` — Behandelt direkt die gefragten Qualifikationsvoraussetzungen
  > IV. Qualifikation (Abs. 5). Abs. 5 enthält einen Qualifikationstatbestand, der die Tat in Fällen kumulativ gewerbs- und bandenmäßiger Begehung zum Verbrechen macht. Die Qualifikation ist in die Urteil...
- **[Judge=3]** `§ 263 StGB – BT. Zweijundzwanzigster Abschnitt – Rn. 213` — Behandelt direkt Bandenbetrug § 263 Abs. 5 StGB
  > 213 Sind beide Varianten erfüllt, ist eine Qualifikation nach Abs. 5 gegeben. Die Abgrenzung des Abs. 3 Nr. 1 zum Verbrechen nach Abs. 5 ist in Fällen bandenmäßiger Begehung schwierig, denn eine auf f...
- **[Judge=2]** `§ 263 StGB – I. Sonstige Vorschriften 239 – Rn. 263 (Teil 1)` — Inhaltsverzeichnis behandelt Betrug, aber nicht spezifisch Abs. 5
  > 3. Einzelne Fallgruppen ... 92 4. Rechtlich missbilligte, sittenwidrige und gesetzeswidrige wirtschaftliche Werte ... 101 VI. Schaden ... 110 1. Grundsätze der Schadensermittlung ... 111 2. Vermögensm...

#### ours-cohere — Top 3
- **[Judge=3]** `§ 263 StGB – BT. Zweriindzwanzigster Abschnitt – Rn. 225` — Direkt relevant: behandelt Voraussetzungen gewerbsmäßiger Bandenbetrug
  > IV. Qualifikation (Abs. 5). Abs. 5 enthält einen Qualifikationstatbestand, der die Tat in Fällen kumulativ gewerbs- und bandenmäßiger Begehung zum Verbrechen macht. Die Qualifikation ist in die Urteil...
- **[Judge=3]** `§ 263 StGB – BT. Zweijundzwanzigster Abschnitt – Rn. 213` — Behandelt direkt Voraussetzungen von § 263 Abs. 5
  > 213 Sind beide Varianten erfüllt, ist eine Qualifikation nach Abs. 5 gegeben. Die Abgrenzung des Abs. 3 Nr. 1 zum Verbrechen nach Abs. 5 ist in Fällen bandenmäßiger Begehung schwierig, denn eine auf f...
- **[Judge=3]** `§ 263 StGB – I. Vermögensbegriff  – Rn. 263` — Enthält vollständigen Wortlaut von § 263 Abs. 5 StGB
  > 263 (1) Wer in der Absicht, sich oder einem Dritten einen rechtswidrigen Vermögensvorteil zu verschaffen, das Vermögen eines anderen dadurch beschädigt, daß er durch Vorspiegelung falscher oder durch ...

#### ours-mxbai — Top 3
- **[Judge=3]** `§ 263 StGB – BT. Zweriindzwanzigster Abschnitt – Rn. 225` — Direkt relevant, erklaert § 263 Abs. 5 Voraussetzungen
  > IV. Qualifikation (Abs. 5). Abs. 5 enthält einen Qualifikationstatbestand, der die Tat in Fällen kumulativ gewerbs- und bandenmäßiger Begehung zum Verbrechen macht. Die Qualifikation ist in die Urteil...
- **[Judge=3]** `§ 263 StGB – BT. Zweijundzwanzigster Abschnitt – Rn. 213` — Direkt relevant: behandelt Qualifikationstatbestand § 263 Abs. 5
  > 213 Sind beide Varianten erfüllt, ist eine Qualifikation nach Abs. 5 gegeben. Die Abgrenzung des Abs. 3 Nr. 1 zum Verbrechen nach Abs. 5 ist in Fällen bandenmäßiger Begehung schwierig, denn eine auf f...
- **[Judge=2]** `§ 263 StGB – BT. Zweijundzwanzigster Abschnitt – Rn. 212` — Behandelt Bandenbetrug, aber andere Vorschrift (§ 244a)
  > 212 Der Begriff der Urkundenfälschung ist weit zu fassen; er umfasst neben Taten nach § 267 auch solche nach §§ 268–281 (LK-StGB/Kubiciel/Tiedemann Rn. 297; NK-StGB/Kindhäuser/Hoven Rn. 392). Entsprec...

### q02 — exakte-paragraphen

**Query:** Was regelt § 112 StPO zur Untersuchungshaft?

**Kontext:** Anordnungsvoraussetzungen der U-Haft (dringender Tatverdacht, Haftgrund) im Schmitt/Koehler

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours | 0.99 | 100% | 100% | 3 | 5.7s |
| ours-cohere | 1.00 | 100% | 100% | 3 | 5.7s |
| ours-mxbai | 1.00 | 100% | 100% | 3 | 5.7s |

#### ours — Top 3
- **[Judge=3]** `§ 112 StPO – Rn. 112` — Direkt relevant: vollständiger Gesetzestext zu § 112 StPO
  > 112 (1) ¹ Die Untersuchungshaft darf gegen den Beschuldigten angeordnet werden, wenn er der Tat dringend verdächtig ist und ein Haftgrund besteht. ² Sie darf nicht angeordnet werden, wenn sie zu der B...
- **[Judge=3]** `§ 112 StPO – Rn. 112` — Erklaert direkt Haftbefehl-Voraussetzungen nach § 112 StPO
  > Haftunfähigkeit des Beschuldigten schließt den Erlass des Haftbefehls nicht aus, sondern hindert nur seinen Vollzug (OLG Düsseldorf JZ 1984, 248; OLG Frankfurt a.M. NJW 1968, 2302; OLG Nürnberg OLGSt ...
- **[Judge=3]** `§ 112 StPO – III. Flucht (Abs – Rn. 23` — Direkt relevant zu § 112 StPO Haftgründen
  > Bei einer besonders hohen Straferwartung braucht daher nur geprüft zu werden, ob Umstände vorhanden sind, die die hieraus herzuleitende Fluchtgefahr ausräumen können (KG StV 1996, 383; OLG München Str...

#### ours-cohere — Top 3
- **[Judge=3]** `§ 112 StPO – Rn. 112` — Direkt relevant: § 112 StPO Wortlaut und Systematik
  > 112 (1) ¹ Die Untersuchungshaft darf gegen den Beschuldigten angeordnet werden, wenn er der Tat dringend verdächtig ist und ein Haftgrund besteht. ² Sie darf nicht angeordnet werden, wenn sie zu der B...
- **[Judge=3]** `§ 112 StPO – Rn. 112` — Behandelt direkt § 112 StPO Haftbefehl-Voraussetzungen
  > Haftunfähigkeit des Beschuldigten schließt den Erlass des Haftbefehls nicht aus, sondern hindert nur seinen Vollzug (OLG Düsseldorf JZ 1984, 248; OLG Frankfurt a.M. NJW 1968, 2302; OLG Nürnberg OLGSt ...
- **[Judge=3]** `§ 112 StPO – III. Flucht (Abs – Rn. 32 (Teil 2)` — Behandelt direkt Verdunkelungsgefahr als Haftgrund nach § 112 StPO
  > Wenn die Verdunkelungshandlungen nicht geeignet sind, die Ermittlung der Wahrheit zu erschweren, darf UHaft nicht angeordnet werden. Der Haftgrund liegt daher nicht vor, wenn der Sachverhalt schon in ...

#### ours-mxbai — Top 3
- **[Judge=3]** `§ 112 StPO – Rn. 112` — Vollständiger Gesetzestext und Struktur zu § 112 StPO
  > 112 (1) ¹ Die Untersuchungshaft darf gegen den Beschuldigten angeordnet werden, wenn er der Tat dringend verdächtig ist und ein Haftgrund besteht. ² Sie darf nicht angeordnet werden, wenn sie zu der B...
- **[Judge=3]** `§ 112 StPO – Rn. 112` — Behandelt direkt § 112 StPO Voraussetzungen Untersuchungshaft
  > Haftunfähigkeit des Beschuldigten schließt den Erlass des Haftbefehls nicht aus, sondern hindert nur seinen Vollzug (OLG Düsseldorf JZ 1984, 248; OLG Frankfurt a.M. NJW 1968, 2302; OLG Nürnberg OLGSt ...
- **[Judge=3]** `§ 112 StPO – III. Flucht (Abs – Rn. 23` — Behandelt direkt Haftgruende nach § 112 StPO
  > Bei einer besonders hohen Straferwartung braucht daher nur geprüft zu werden, ob Umstände vorhanden sind, die die hieraus herzuleitende Fluchtgefahr ausräumen können (KG StV 1996, 383; OLG München Str...

### q03 — exakte-paragraphen

**Query:** Welche Haftgruende nennt § 112 Abs. 2 StPO?

**Kontext:** Fluchtgefahr, Verdunkelungsgefahr, Flucht — im StPO-Kommentar

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours | 0.99 | 100% | 100% | 3 | 4.5s |
| ours-cohere | 1.00 | 100% | 100% | 3 | 4.5s |
| ours-mxbai | 1.00 | 100% | 100% | 3 | 4.4s |

#### ours — Top 3
- **[Judge=3]** `§ 112 StPO – Rn. 112` — Beantwortet die Frage direkt und vollstaendig
  > 112 (1) ¹ Die Untersuchungshaft darf gegen den Beschuldigten angeordnet werden, wenn er der Tat dringend verdächtig ist und ein Haftgrund besteht. ² Sie darf nicht angeordnet werden, wenn sie zu der B...
- **[Judge=3]** `§ 112 StPO – III. Flucht (Abs – Rn. 23` — Direkter Bezug zu § 112 Abs. 2 StPO Haftgründen
  > Bei einer besonders hohen Straferwartung braucht daher nur geprüft zu werden, ob Umstände vorhanden sind, die die hieraus herzuleitende Fluchtgefahr ausräumen können (KG StV 1996, 383; OLG München Str...
- **[Judge=2]** `§ 112 StPO – III. Flucht (Abs – Rn. 32 (Teil 2)` — Behandelt Verdunkelungsgefahr detailliert, aber nicht Haftgruende allgemein
  > Wenn die Verdunkelungshandlungen nicht geeignet sind, die Ermittlung der Wahrheit zu erschweren, darf UHaft nicht angeordnet werden. Der Haftgrund liegt daher nicht vor, wenn der Sachverhalt schon in ...

#### ours-cohere — Top 3
- **[Judge=3]** `§ 112 StPO – Rn. 112` — Vollständige Auflistung aller Haftgründe nach § 112 Abs. 2 StPO
  > 112 (1) ¹ Die Untersuchungshaft darf gegen den Beschuldigten angeordnet werden, wenn er der Tat dringend verdächtig ist und ein Haftgrund besteht. ² Sie darf nicht angeordnet werden, wenn sie zu der B...
- **[Judge=3]** `§ 112 StPO – III. Flucht (Abs – Rn. 23` — Erklärt direkt Haftgründe § 112 Abs. 2 StPO
  > Bei einer besonders hohen Straferwartung braucht daher nur geprüft zu werden, ob Umstände vorhanden sind, die die hieraus herzuleitende Fluchtgefahr ausräumen können (KG StV 1996, 383; OLG München Str...
- **[Judge=3]** `§ 112 StPO – III. Flucht (Abs – Rn. 32 (Teil 2)` — Erläutert direkt Haftgrund Verdunkelungsgefahr aus § 112 Abs. 2
  > Wenn die Verdunkelungshandlungen nicht geeignet sind, die Ermittlung der Wahrheit zu erschweren, darf UHaft nicht angeordnet werden. Der Haftgrund liegt daher nicht vor, wenn der Sachverhalt schon in ...

#### ours-mxbai — Top 3
- **[Judge=3]** `§ 112 StPO – Rn. 112` — Direkter Wortlaut von § 112 Abs. 2 StPO
  > 112 (1) ¹ Die Untersuchungshaft darf gegen den Beschuldigten angeordnet werden, wenn er der Tat dringend verdächtig ist und ein Haftgrund besteht. ² Sie darf nicht angeordnet werden, wenn sie zu der B...
- **[Judge=3]** `§ 112 StPO – III. Flucht (Abs – Rn. 23` — Erklärt direkt Haftgrund Verdunkelungsgefahr nach § 112 Abs. 2 Nr. 3
  > Bei einer besonders hohen Straferwartung braucht daher nur geprüft zu werden, ob Umstände vorhanden sind, die die hieraus herzuleitende Fluchtgefahr ausräumen können (KG StV 1996, 383; OLG München Str...
- **[Judge=3]** `§ 112 StPO – III. Flucht (Abs – Rn. 32 (Teil 2)` — Behandelt direkt Verdunkelungsgefahr als Haftgrund nach § 112 StPO
  > Wenn die Verdunkelungshandlungen nicht geeignet sind, die Ermittlung der Wahrheit zu erschweren, darf UHaft nicht angeordnet werden. Der Haftgrund liegt daher nicht vor, wenn der Sachverhalt schon in ...

### q04 — exakte-paragraphen

**Query:** Was regelt § 102 StPO zur Durchsuchung beim Beschuldigten?

**Kontext:** Durchsuchungsvoraussetzungen beim Verdaechtigen

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours | 0.99 | 100% | 100% | 3 | 5.5s |
| ours-cohere | 0.99 | 100% | 100% | 3 | 7.2s |
| ours-mxbai | 0.96 | 100% | 100% | 3 | 5.1s |

#### ours — Top 3
- **[Judge=3]** `§ 102 StPO – Rn. 102` — Direkt relevanter § 102 StPO Text zu Durchsuchungsvoraussetzungen
  > 102 Bei dem, welcher als Täter oder Teilnehmer einer Straftat oder der Datenhehlerei, Begünstigung, Strafvereitelung oder Hehlerei  Köhler    Ermittlungsmaßnahmen  verdächtig ist, kann eine Durchsuchu...
- **[Judge=3]** `§ 102 StPO – Rn. 10` — Direkt relevant: behandelt Durchsuchungsvoraussetzungen bei § 102
  > 10 III. Sachen. Sachen sind Kleidungsstücke, die der Verdächtige bei sich führt, ohne sie zu tragen, u. seine sonstige bewegliche Habe, gleichgültig, ob sie sich in seinem Umkreis, zB in Gepäckstücken...
- **[Judge=2]** `§ 102 StPO – Rn. 10` — Thematisch relevant: Durchsuchungsrecht, aber nicht § 102 direkt
  > II. Auffinden von Beweismitteln. Zu den Beweismitteln (→ § 94 Rn. 4 ff.) gehören auch die nur in § 103 erwähnten Spuren (SK-StPO/Jäger/Wohlers Rn. 21) u. Personen, die zu Beweiszwecken in Augenschein ...

#### ours-cohere — Top 3
- **[Judge=3]** `§ 102 StPO – Rn. 102` — Direkte Relevanz: § 102 StPO Durchsuchung Beschuldigter
  > 102 Bei dem, welcher als Täter oder Teilnehmer einer Straftat oder der Datenhehlerei, Begünstigung, Strafvereitelung oder Hehlerei  Köhler    Ermittlungsmaßnahmen  verdächtig ist, kann eine Durchsuchu...
- **[Judge=3]** `§ 102 StPO – Rn. 10` — Direkt relevant: behandelt § 102 StPO Sachendurchsuchung
  > 10 III. Sachen. Sachen sind Kleidungsstücke, die der Verdächtige bei sich führt, ohne sie zu tragen, u. seine sonstige bewegliche Habe, gleichgültig, ob sie sich in seinem Umkreis, zB in Gepäckstücken...
- **[Judge=2]** `§ 102 StPO – Rn. 10` — Behandelt Durchsuchungsvoraussetzungen und Verhaeltnismaessigkeit, aber nicht spezifisch § 102
  > II. Auffinden von Beweismitteln. Zu den Beweismitteln (→ § 94 Rn. 4 ff.) gehören auch die nur in § 103 erwähnten Spuren (SK-StPO/Jäger/Wohlers Rn. 21) u. Personen, die zu Beweiszwecken in Augenschein ...

#### ours-mxbai — Top 3
- **[Judge=3]** `§ 102 StPO – Rn. 102` — Vollständige Erläuterung des § 102 StPO Durchsuchungsrechts
  > 102 Bei dem, welcher als Täter oder Teilnehmer einer Straftat oder der Datenhehlerei, Begünstigung, Strafvereitelung oder Hehlerei  Köhler    Ermittlungsmaßnahmen  verdächtig ist, kann eine Durchsuchu...
- **[Judge=2]** `§ 102 StPO – Rn. 10` — Behandelt Durchsuchungsvoraussetzungen, aber nicht spezifisch §102
  > II. Auffinden von Beweismitteln. Zu den Beweismitteln (→ § 94 Rn. 4 ff.) gehören auch die nur in § 103 erwähnten Spuren (SK-StPO/Jäger/Wohlers Rn. 21) u. Personen, die zu Beweiszwecken in Augenschein ...
- **[Judge=2]** `§ 102 StPO – Rn. 10` — Behandelt Durchsuchungsverhaeltnismaessigkeit, aber nicht § 102 StPO
  > Kohler     Erstes Buch. Achter Abschnitt  Aufklärung bislang ungeklärter Fälle“ einer Tatserie beitragen könne, scheint dies den besonderen Umständen des Einzelfalls geschuldet zu sein. Denn zum einen...

### q05 — konzept

**Query:** Wann liegt eine konkludente Taeuschung im Sinne des § 263 StGB vor?

**Kontext:** Taeuschungshandlung durch schluessiges Verhalten

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours | 0.83 | 80% | 67% | 1 | 5.9s |
| ours-cohere | 0.83 | 60% | 67% | 1 | 6.3s |
| ours-mxbai | 0.94 | 80% | 67% | 3 | 6.6s |

#### ours — Top 3
- **[Judge=1]** `§ 263 StGB – I. Vermögensbegriff  – Rn. 263` — Nur Gesetzestext, keine Erklaerung konkludenter Taeuschung
  > 263 (1) Wer in der Absicht, sich oder einem Dritten einen rechtswidrigen Vermögensvorteil zu verschaffen, das Vermögen eines anderen dadurch beschädigt, daß er durch Vorspiegelung falscher oder durch ...
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 21` — Direkt relevant: erklaert konkludente Taeuschung bei § 263 StGB
  > 21 2. Konkludente Erklärungen. Auch durch eine schlüssige Handlung (konkludente Erklärung) kann vorspiegelt werden. Eine solche konkludente Erklärung durch aktives Tun ist von einer Erklärung durch Un...
- **[Judge=2]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 263 (Tei` — Literaturnachweise zu konkludenter Taeuschung, aber keine Inhalte
  > Heghmanns, Strafbarkeit des „Phishing“ von Bankkontendaten und ihrer Verwertung, wistra 2007, 167; Hilgendorf, Tatsachenaussagen u. Werturteile im Strafrecht, 1998; Hillenkamp, Zum Schutz „deliktische...

#### ours-cohere — Top 3
- **[Judge=1]** `§ 263 StGB – I. Vermögensbegriff  – Rn. 263` — Nennt nur Tatbestandsmerkmale, keine konkludente Taeuschung
  > 263 (1) Wer in der Absicht, sich oder einem Dritten einen rechtswidrigen Vermögensvorteil zu verschaffen, das Vermögen eines anderen dadurch beschädigt, daß er durch Vorspiegelung falscher oder durch ...
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 14` — Behandelt direkt konkludente Täuschung bei § 263 StGB
  > Rspr. und hM bejahen darüber hinaus aber die Möglichkeit einer Täuschung durch Unterlassen auch ohne Erklärung gegenüber dem Irrenden (→ Rn. 38; vgl. BGHSt 39, 392 (398); BayObLG NJW 1987, 1654 (mAnm ...
- **[Judge=2]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 263 (Tei` — Literaturverzeichnis zu Betrug, erwähnt konkludente Täuschung tangential
  > Heghmanns, Strafbarkeit des „Phishing“ von Bankkontendaten und ihrer Verwertung, wistra 2007, 167; Hilgendorf, Tatsachenaussagen u. Werturteile im Strafrecht, 1998; Hillenkamp, Zum Schutz „deliktische...

#### ours-mxbai — Top 3
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 14` — Direkt relevant: behandelt konkludente Täuschung bei § 263
  > Rspr. und hM bejahen darüber hinaus aber die Möglichkeit einer Täuschung durch Unterlassen auch ohne Erklärung gegenüber dem Irrenden (→ Rn. 38; vgl. BGHSt 39, 392 (398); BayObLG NJW 1987, 1654 (mAnm ...
- **[Judge=1]** `§ 263 StGB – I. Vermögensbegriff  – Rn. 263` — Gesetzestext ohne Erklärung konkludenter Täuschung
  > 263 (1) Wer in der Absicht, sich oder einem Dritten einen rechtswidrigen Vermögensvorteil zu verschaffen, das Vermögen eines anderen dadurch beschädigt, daß er durch Vorspiegelung falscher oder durch ...
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 14` — Behandelt direkt konkludente Taeuschung bei § 263
  > 14 II. Tathandlung. Der Begriff „Täuschen“ ist im Wortlaut des Abs. 1 nicht verwendet; er ergibt sich aus dem Zusammenhang zwischen der Beschreibung der Tathandlung (→ Rn. 18) und dem Irrtum als ihrem...

### q06 — konzept

**Query:** Was ist eine Vermoegensverfuegung und welche Anforderungen stellt die Rechtsprechung?

**Kontext:** Tatbestandsmerkmal der Vermoegensverfuegung beim Betrug

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours | 0.93 | 60% | 67% | 3 | 5.9s |
| ours-cohere | 1.00 | 20% | 33% | 3 | 5.5s |
| ours-mxbai | 0.98 | 100% | 100% | 3 | 5.8s |

#### ours — Top 3
- **[Judge=3]** `§ 263 StGB – BT. Zweitundzwanzigster Abschnitt – Rn. 69` — Definiert Vermoegensverfuegung und nennt Rechtsprechungsanforderungen direkt
  > 69 Anders ist es, wenn der Verfügende seinerseits nur (gutgläubige) Hilfsperson eines bösgläubigen Dritten ist. Hier ist auf den Irrtum des Entscheidungsbefugten abzustellen: Erkennt dieser die Unrich...
- **[Judge=1]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 176` — Subjektiver Tatbestand, nicht Vermoegensverfuegung selbst
  > D. Subjektiver Tatbestand. § 263 setzt Vorsatz voraus; darüber hinaus ist die Absicht rechtswidriger Bereicherung erforderlich.   I. Vorsatz. 1. Täuschungsvorsatz. Der Vorsatz (bedingter Vorsatz genüg...
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 76` — Behandelt direkt Vermoegensverfuegung und deren Anforderungen
  > 4. Dreiecksbetrug. Da die Getäuschte und die verfügende, nicht aber die verfügende und die geschädigte Person identisch sein müssen, ist der Tatbestand des § 263 nur erfüllt, wenn die Vermögensverfügu...

#### ours-cohere — Top 3
- **[Judge=3]** `§ 263 StGB – BT. Zweitundzwanzigster Abschnitt – Rn. 69` — Direkt relevant: definiert Vermoegensverfuegung und Rechtsprechungsanforderungen
  > 69 Anders ist es, wenn der Verfügende seinerseits nur (gutgläubige) Hilfsperson eines bösgläubigen Dritten ist. Hier ist auf den Irrtum des Entscheidungsbefugten abzustellen: Erkennt dieser die Unrich...
- **[Judge=1]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 87` — Behandelt Kausalität und Schaden, nicht Verfügungsbegriff selbst
  > 87 5. Kausalität. Für die Vermögensverfügung muss der täuschungsbedingte Irrtum kausal sein (vgl. BGHSt 24, 257 (260); 24, 386 (389); NStZ 2003, 313 (314 f.); OLG Düsseldorf NJW 1987, 3145); Mitverurs...
- **[Judge=1]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 176` — Behandelt subjektiven Tatbestand, nicht Vermoegensverfuegung
  > D. Subjektiver Tatbestand. § 263 setzt Vorsatz voraus; darüber hinaus ist die Absicht rechtswidriger Bereicherung erforderlich.   I. Vorsatz. 1. Täuschungsvorsatz. Der Vorsatz (bedingter Vorsatz genüg...

#### ours-mxbai — Top 3
- **[Judge=3]** `§ 263 StGB – BT. Zweitundzwanzigster Abschnitt – Rn. 69` — Definiert Vermoegensverfuegung als ungeschriebenes Tatbestandsmerkmal mit Anforderungen
  > 69 Anders ist es, wenn der Verfügende seinerseits nur (gutgläubige) Hilfsperson eines bösgläubigen Dritten ist. Hier ist auf den Irrtum des Entscheidungsbefugten abzustellen: Erkennt dieser die Unrich...
- **[Judge=2]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 87` — Kausalität bei Vermögensverfügung, nicht Definition selbst
  > 87 5. Kausalität. Für die Vermögensverfügung muss der täuschungsbedingte Irrtum kausal sein (vgl. BGHSt 24, 257 (260); 24, 386 (389); NStZ 2003, 313 (314 f.); OLG Düsseldorf NJW 1987, 3145); Mitverurs...
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 74` — Definiert Vermoegensverfuegung und Verfügungsbewusstsein direkt
  > 74 2. Verfügungsbewusstsein. Vermögensverfügungen sind nach hM grundsätzlich sowohl als bewusst als auch als unbewusst vermögensmindernde Handlungen möglich; eine aktuelle Vorstellung des Verfügenden ...

### q07 — konzept

**Query:** Was versteht man unter einem Gefaehrdungsschaden beim Betrug?

**Kontext:** Schadensbegriff, schadensgleiche Vermoegensgefaehrdung

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours | 0.99 | 100% | 100% | 3 | 5.8s |
| ours-cohere | 1.00 | 100% | 100% | 3 | 6.2s |
| ours-mxbai | 1.00 | 100% | 100% | 3 | 5.2s |

#### ours — Top 3
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 159` — Definiert direkt den Gefährdungsschaden beim Betrug
  > 159 b) Voraussetzungen. aa) Ein Gefährdungsschaden ist gegeben, wenn die Wahrscheinlichkeit des endgültigen Verlusts eines Vermögensbestandteils zum Zeitpunkt der täuschungsbedingten Verfügung so groß...
- **[Judge=3]** `§ 263 StGB – BT. Zwei undzwanzigster Abschnitt – Rn. 263 (Te` — Direkt relevant: Gefährdungsschaden wird explizit thematisiert
  > Fischer/Lutz    Betrug und Untreue   rechts für das Strafrecht, FS Weber, 2004, 271; Eisele/Bechtel, Der Schadensbegriff bei den Vermögensdelikten, JuS 2018, 97; Ellbogen/Wichmann, Zu Problemen des är...
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 156` — Direkt relevant: erklaert schadensgleiche Vermoegensgefaehrdung beim Betrug
  > 156 8. Schadensgleiche Vermögensgefährdung. Eine Ausweitung erfährt der Tatbestand durch die von stRspr (seit RGSt 16, 1) und hM bejahte Möglichkeit eines vollendeten Schadenseintritts durch konkrete ...

#### ours-cohere — Top 3
- **[Judge=3]** `§ 263 StGB – BT. Zwei undzwanzigster Abschnitt – Rn. 263` — Behandelt direkt Gefährdungsschaden beim Betrug
  > **Rechtsprechungsübersicht:** Scholz, Die Entwicklung des Berufs- und Vertragsarztrechts, medstra 2019, 331; 2021, 349; 2022, 355; 2023, 355; 2024, 351.  Weinrich/Wostry, Der Abrechnungsbetrug in der ...
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 109` — Direkt relevant: definiert Gefährdungsschaden beim Betrug
  > VI. Schaden. Vermögensschaden ist ein negativer Saldo zwischen dem Wert des Vermögens vor und nach der irrtumsbedingten Vermögensverfügung des Getäuschten (Prinzip der Gesamtsaldierung; stRspr; vgl. B...
- **[Judge=3]** `§ 263 StGB – BT. Zwei undzwanzigster Abschnitt – Rn. 263 (Te` — Direkt relevant: Gefährdungsschaden beim Betrug behandelt
  > Fischer/Lutz    Betrug und Untreue   rechts für das Strafrecht, FS Weber, 2004, 271; Eisele/Bechtel, Der Schadensbegriff bei den Vermögensdelikten, JuS 2018, 97; Ellbogen/Wichmann, Zu Problemen des är...

#### ours-mxbai — Top 3
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 159` — Direkte Definition und Voraussetzungen des Gefaehrdungsschadens
  > 159 b) Voraussetzungen. aa) Ein Gefährdungsschaden ist gegeben, wenn die Wahrscheinlichkeit des endgültigen Verlusts eines Vermögensbestandteils zum Zeitpunkt der täuschungsbedingten Verfügung so groß...
- **[Judge=3]** `§ 263 StGB – BT. Zwei undzwanzigster Abschnitt – Rn. 263 (Te` — Behandelt direkt Gefährdungsschaden bei Vermögensdelikten
  > Fischer/Lutz    Betrug und Untreue   rechts für das Strafrecht, FS Weber, 2004, 271; Eisele/Bechtel, Der Schadensbegriff bei den Vermögensdelikten, JuS 2018, 97; Ellbogen/Wichmann, Zu Problemen des är...
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 109` — Definiert Gefaehrdungsschaden direkt im Betrugsstrafrecht
  > VI. Schaden. Vermögensschaden ist ein negativer Saldo zwischen dem Wert des Vermögens vor und nach der irrtumsbedingten Vermögensverfügung des Getäuschten (Prinzip der Gesamtsaldierung; stRspr; vgl. B...

### q08 — konzept

**Query:** Wie wird der Vorsatz beim Betrug bestimmt, insbesondere die Bereicherungsabsicht?

**Kontext:** Subjektiver Tatbestand § 263 StGB

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours | 0.99 | 80% | 100% | 3 | 5.9s |
| ours-cohere | 1.00 | 80% | 100% | 3 | 6.4s |
| ours-mxbai | 0.97 | 80% | 67% | 3 | 5.7s |

#### ours — Top 3
- **[Judge=3]** `§ 263 StGB – I. Sonstige Vorschriften 239 – Rn. 263 (Teil 1)` — Direkt relevant: behandelt Bereicherungsabsicht beim Betrug
  > 3. Einzelne Fallgruppen ... 92 4. Rechtlich missbilligte, sittenwidrige und gesetzeswidrige wirtschaftliche Werte ... 101 VI. Schaden ... 110 1. Grundsätze der Schadensermittlung ... 111 2. Vermögensm...
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 176` — Direkt relevant: behandelt Vorsatz und Bereicherungsabsicht beim Betrug
  > D. Subjektiver Tatbestand. § 263 setzt Vorsatz voraus; darüber hinaus ist die Absicht rechtswidriger Bereicherung erforderlich.   I. Vorsatz. 1. Täuschungsvorsatz. Der Vorsatz (bedingter Vorsatz genüg...
- **[Judge=2]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 187 (Tei` — Objektiver Tatbestand, nicht Vorsatz/Bereicherungsabsicht
  > 187 1. Stoffgleichheit. Der Vorteil muss die Kehrseite des Schadens und ihm „stoffgleich“ sein; er muss unmittelbare Folge der täuschungsbedingten Verfügung sein, welche den Schaden des Opfers herbeif...

#### ours-cohere — Top 3
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 176` — Direkt relevant: behandelt Vorsatz und Bereicherungsabsicht bei Betrug
  > D. Subjektiver Tatbestand. § 263 setzt Vorsatz voraus; darüber hinaus ist die Absicht rechtswidriger Bereicherung erforderlich.   I. Vorsatz. 1. Täuschungsvorsatz. Der Vorsatz (bedingter Vorsatz genüg...
- **[Judge=3]** `§ 263 StGB – I. Sonstige Vorschriften 239 – Rn. 263 (Teil 1)` — Direkt relevant - behandelt Bereicherungsabsicht bei Betrug
  > 3. Einzelne Fallgruppen ... 92 4. Rechtlich missbilligte, sittenwidrige und gesetzeswidrige wirtschaftliche Werte ... 101 VI. Schaden ... 110 1. Grundsätze der Schadensermittlung ... 111 2. Vermögensm...
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 186` — Definiert direkt Bereicherungsabsicht beim Betrug
  > 186 II. Bereicherungsabsicht. Die Tat muss subjektiv auf die Erlangung eines rechtswidrigen Vermögensvorteils für den Täuschenden oder einen Dritten gerichtet sein. Vermögensvorteil ist die Erhöhung d...

#### ours-mxbai — Top 3
- **[Judge=3]** `§ 263 StGB – I. Sonstige Vorschriften 239 – Rn. 263 (Teil 1)` — Direkt relevant: behandelt Bereicherungsabsicht bei Betrug
  > 3. Einzelne Fallgruppen ... 92 4. Rechtlich missbilligte, sittenwidrige und gesetzeswidrige wirtschaftliche Werte ... 101 VI. Schaden ... 110 1. Grundsätze der Schadensermittlung ... 111 2. Vermögensm...
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 176` — Direkt relevant: Vorsatz und Bereicherungsabsicht beim Betrug
  > D. Subjektiver Tatbestand. § 263 setzt Vorsatz voraus; darüber hinaus ist die Absicht rechtswidriger Bereicherung erforderlich.   I. Vorsatz. 1. Täuschungsvorsatz. Der Vorsatz (bedingter Vorsatz genüg...
- **[Judge=1]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 187 (Tei` — Behandelt Stoffgleichheit, nicht Vorsatz/Bereicherungsabsicht
  > 187 1. Stoffgleichheit. Der Vorteil muss die Kehrseite des Schadens und ihm „stoffgleich“ sein; er muss unmittelbare Folge der täuschungsbedingten Verfügung sein, welche den Schaden des Opfers herbeif...

### q09 — alltagssprache

**Query:** Hat der Angeklagte die Kunden über das Internet betrogen?

**Kontext:** Abstrakte Frage zu Internetbetrug, sucht Taeuschungshandlung + Schaden

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours | 0.99 | 100% | 100% | 3 | 5.6s |
| ours-cohere | 0.84 | 80% | 67% | 1 | 5.9s |
| ours-mxbai | 1.00 | 100% | 100% | 3 | 5.6s |

#### ours — Top 3
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 28` — Direkt relevant: Internetbetrug, Täuschungshandlungen bei Kostenfallen
  > In Fällen sog. „Kostenfallen“ im Internet (vgl. dazu Eisele NStZ 2010, 193), bei denen unerfahrene Verbraucher durch (wahre) Versprechen besonders günstiger Angebote zum Abschluss von Verträgen gebrac...
- **[Judge=3]** `§ 263 StGB – I. Vermögensbegriff  – Rn. 263` — Zentrale Betrugsvorschrift mit allen relevanten Tatbestandsmerkmalen
  > 263 (1) Wer in der Absicht, sich oder einem Dritten einen rechtswidrigen Vermögensvorteil zu verschaffen, das Vermögen eines anderen dadurch beschädigt, daß er durch Vorspiegelung falscher oder durch ...
- **[Judge=2]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 263 (Tei` — Behandelt Betrug und Internet-Phishing, aber nur Literaturverweise
  > Heghmanns, Strafbarkeit des „Phishing“ von Bankkontendaten und ihrer Verwertung, wistra 2007, 167; Hilgendorf, Tatsachenaussagen u. Werturteile im Strafrecht, 1998; Hillenkamp, Zum Schutz „deliktische...

#### ours-cohere — Top 3
- **[Judge=1]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 263 (Tei` — Literaturverzeichnis zu Betrug, aber keine konkreten Inhalte
  > Heghmanns, Strafbarkeit des „Phishing“ von Bankkontendaten und ihrer Verwertung, wistra 2007, 167; Hilgendorf, Tatsachenaussagen u. Werturteile im Strafrecht, 1998; Hillenkamp, Zum Schutz „deliktische...
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 5` — Definiert zentrale Tatbestandsmerkmale des Betrugs
  > 5 C. Grundtatbestand, Abs. 1. Tathandlung ist das Täuschen einer natürlichen Person (vgl. NStZ 2005, 213) über Tatsachen. Erfolg dieser Handlung muss ein Irrtum des Täuschungsadressaten sein; dieser m...
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 14` — Direkt relevant: Täuschungshandlungen und Internetbetrug (SPAM/Phishing)
  > Rspr. und hM bejahen darüber hinaus aber die Möglichkeit einer Täuschung durch Unterlassen auch ohne Erklärung gegenüber dem Irrenden (→ Rn. 38; vgl. BGHSt 39, 392 (398); BayObLG NJW 1987, 1654 (mAnm ...

#### ours-mxbai — Top 3
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 109` — Direkt relevant: zentrale Schadensdefinition bei Betrug
  > VI. Schaden. Vermögensschaden ist ein negativer Saldo zwischen dem Wert des Vermögens vor und nach der irrtumsbedingten Vermögensverfügung des Getäuschten (Prinzip der Gesamtsaldierung; stRspr; vgl. B...
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 5` — Definiert Betrug: Täuschung, Irrtum, Vermögensschaden
  > 5 C. Grundtatbestand, Abs. 1. Tathandlung ist das Täuschen einer natürlichen Person (vgl. NStZ 2005, 213) über Tatsachen. Erfolg dieser Handlung muss ein Irrtum des Täuschungsadressaten sein; dieser m...
- **[Judge=2]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 263 (Tei` — Betrugsliteratur mit Internetbezug, thematisch relevant aber oberflächlich
  > Heghmanns, Strafbarkeit des „Phishing“ von Bankkontendaten und ihrer Verwertung, wistra 2007, 167; Hilgendorf, Tatsachenaussagen u. Werturteile im Strafrecht, 1998; Hillenkamp, Zum Schutz „deliktische...

### q10 — alltagssprache

**Query:** Wann darf die Polizei bei jemandem zu Hause suchen?

**Kontext:** Durchsuchungsvoraussetzungen, §§ 102 ff. StPO

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours | 1.00 | 100% | 100% | 3 | 5.6s |
| ours-cohere | 0.98 | 100% | 100% | 3 | 5.2s |
| ours-mxbai | 0.97 | 100% | 100% | 3 | 4.8s |

#### ours — Top 3
- **[Judge=3]** `§ 102 StPO – Rn. 102` — Direkt relevant: zentrale Durchsuchungsvoraussetzungen nach § 102 StPO
  > 102 Bei dem, welcher als Täter oder Teilnehmer einer Straftat oder der Datenhehlerei, Begünstigung, Strafvereitelung oder Hehlerei  Köhler    Ermittlungsmaßnahmen  verdächtig ist, kann eine Durchsuchu...
- **[Judge=3]** `§ 102 StPO – Rn. 10` — Behandelt direkt Durchsuchungsvoraussetzungen nach StPO
  > II. Auffinden von Beweismitteln. Zu den Beweismitteln (→ § 94 Rn. 4 ff.) gehören auch die nur in § 103 erwähnten Spuren (SK-StPO/Jäger/Wohlers Rn. 21) u. Personen, die zu Beweiszwecken in Augenschein ...
- **[Judge=3]** `§ 102 StPO – Rn. 102` — Behandelt direkt Tatverdacht für Wohnungsdurchsuchungen nach § 102
  > Köhler     Erstes Buch. Achter Abschnitt  Gesetz gebundenen Behörden u. Gremien ist nicht angezeigt (BGH JR 2019, 404 mAnm Löffelmann). Bei anonymen Hinweisen ist wegen der erhöhten Gefahr u. des nur ...

#### ours-cohere — Top 3
- **[Judge=3]** `§ 102 StPO – Rn. 102` — Direkt relevant: § 102 StPO Durchsuchungsvoraussetzungen
  > 102 Bei dem, welcher als Täter oder Teilnehmer einer Straftat oder der Datenhehlerei, Begünstigung, Strafvereitelung oder Hehlerei  Köhler    Ermittlungsmaßnahmen  verdächtig ist, kann eine Durchsuchu...
- **[Judge=2]** `§ 102 StPO – Rn. 10` — Behandelt Durchsuchungsvoraussetzungen, aber fokussiert auf Beweismittel/Verhältnismäßigkeit
  > II. Auffinden von Beweismitteln. Zu den Beweismitteln (→ § 94 Rn. 4 ff.) gehören auch die nur in § 103 erwähnten Spuren (SK-StPO/Jäger/Wohlers Rn. 21) u. Personen, die zu Beweiszwecken in Augenschein ...
- **[Judge=3]** `§ 102 StPO – Rn. 3` — Direkt relevant zu Durchsuchungsvoraussetzungen und Wohnungen
  > **Teilnehmer** nach §§ 25 ff. StGB, nicht die sog. notwendigen Teilnehmer (zum Begriff: Fischer/Fischer StGB Vor § 25 Rn. 7), stehen den Tatverdächtigen gleich. Bei jedem v. ihnen sowie bei den der Be...

#### ours-mxbai — Top 3
- **[Judge=3]** `§ 102 StPO – Rn. 102` — Direkt relevant: Durchsuchungsvoraussetzungen bei Verdächtigen
  > 102 Bei dem, welcher als Täter oder Teilnehmer einer Straftat oder der Datenhehlerei, Begünstigung, Strafvereitelung oder Hehlerei  Köhler    Ermittlungsmaßnahmen  verdächtig ist, kann eine Durchsuchu...
- **[Judge=2]** `§ 102 StPO – Rn. 10` — Behandelt Durchsuchungsvoraussetzungen, aber nicht direkt polizeiliche Hausdurchsuchung
  > II. Auffinden von Beweismitteln. Zu den Beweismitteln (→ § 94 Rn. 4 ff.) gehören auch die nur in § 103 erwähnten Spuren (SK-StPO/Jäger/Wohlers Rn. 21) u. Personen, die zu Beweiszwecken in Augenschein ...
- **[Judge=3]** `§ 102 StPO – Rn. 3` — Direkt relevant zu Durchsuchungsvoraussetzungen und -gegenständen
  > **Teilnehmer** nach §§ 25 ff. StGB, nicht die sog. notwendigen Teilnehmer (zum Begriff: Fischer/Fischer StGB Vor § 25 Rn. 7), stehen den Tatverdächtigen gleich. Bei jedem v. ihnen sowie bei den der Be...

### q11 — alltagssprache

**Query:** Was passiert wenn jemand luegt damit er Geld bekommt?

**Kontext:** Laienhafte Umschreibung des Betrugstatbestandes

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours | 1.00 | 100% | 100% | 3 | 5.7s |
| ours-cohere | 0.99 | 100% | 100% | 3 | 7.1s |
| ours-mxbai | 1.00 | 100% | 100% | 3 | 5.6s |

#### ours — Top 3
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 5` — Direkt relevant: beschreibt exakt den Betrugstatbestand
  > 5 C. Grundtatbestand, Abs. 1. Tathandlung ist das Täuschen einer natürlichen Person (vgl. NStZ 2005, 213) über Tatsachen. Erfolg dieser Handlung muss ein Irrtum des Täuschungsadressaten sein; dieser m...
- **[Judge=3]** `§ 263 StGB – BT. Zweitundzwanzigster Abschnitt – Rn. 69` — Direkt relevant: Betrugstatbestand mit Vermögensverfügung
  > 69 Anders ist es, wenn der Verfügende seinerseits nur (gutgläubige) Hilfsperson eines bösgläubigen Dritten ist. Hier ist auf den Irrtum des Entscheidungsbefugten abzustellen: Erkennt dieser die Unrich...
- **[Judge=3]** `§ 263 StGB – I. Vermögensbegriff  – Rn. 263` — Direkt relevant: Betrugstatbestand § 263 StGB
  > 263 (1) Wer in der Absicht, sich oder einem Dritten einen rechtswidrigen Vermögensvorteil zu verschaffen, das Vermögen eines anderen dadurch beschädigt, daß er durch Vorspiegelung falscher oder durch ...

#### ours-cohere — Top 3
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 5` — Direkt relevant: Betrug durch Täuschung um Vermögensvorteil
  > 5 C. Grundtatbestand, Abs. 1. Tathandlung ist das Täuschen einer natürlichen Person (vgl. NStZ 2005, 213) über Tatsachen. Erfolg dieser Handlung muss ein Irrtum des Täuschungsadressaten sein; dieser m...
- **[Judge=3]** `§ 263 StGB – I. Vermögensbegriff  – Rn. 263` — Direkt relevant: Definition des Betrugstatbestandes § 263
  > 263 (1) Wer in der Absicht, sich oder einem Dritten einen rechtswidrigen Vermögensvorteil zu verschaffen, das Vermögen eines anderen dadurch beschädigt, daß er durch Vorspiegelung falscher oder durch ...
- **[Judge=2]** `§ 263 StGB – BT. Zweitundzwanzigster Abschnitt – Rn. 69` — Behandelt Betrug, aber komplexe Spezialproblem-Konstellation statt Grundtatbestand
  > 69 Anders ist es, wenn der Verfügende seinerseits nur (gutgläubige) Hilfsperson eines bösgläubigen Dritten ist. Hier ist auf den Irrtum des Entscheidungsbefugten abzustellen: Erkennt dieser die Unrich...

#### ours-mxbai — Top 3
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 186` — Erklaert Bereicherungsabsicht beim Betrug direkt relevant
  > 186 II. Bereicherungsabsicht. Die Tat muss subjektiv auf die Erlangung eines rechtswidrigen Vermögensvorteils für den Täuschenden oder einen Dritten gerichtet sein. Vermögensvorteil ist die Erhöhung d...
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 5` — Definiert direkt den Betrugstatbestand mit Täuschung
  > 5 C. Grundtatbestand, Abs. 1. Tathandlung ist das Täuschen einer natürlichen Person (vgl. NStZ 2005, 213) über Tatsachen. Erfolg dieser Handlung muss ein Irrtum des Täuschungsadressaten sein; dieser m...
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 176` — Direkt relevant: behandelt Betrugstatbestand mit Bereicherungsabsicht
  > D. Subjektiver Tatbestand. § 263 setzt Vorsatz voraus; darüber hinaus ist die Absicht rechtswidriger Bereicherung erforderlich.   I. Vorsatz. 1. Täuschungsvorsatz. Der Vorsatz (bedingter Vorsatz genüg...

### q12 — alltagssprache

**Query:** Wann muss jemand ins Gefaengnis waehrend die Tat noch nicht bewiesen ist?

**Kontext:** Untersuchungshaft, §§ 112 ff. StPO

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours | 1.00 | 100% | 100% | 3 | 5.3s |
| ours-cohere | 0.99 | 100% | 100% | 3 | 6.1s |
| ours-mxbai | 1.00 | 100% | 100% | 3 | 4.9s |

#### ours — Top 3
- **[Judge=3]** `§ 112 StPO – Rn. 112` — Beantwortet direkt Voraussetzungen der Untersuchungshaft
  > 112 (1) ¹ Die Untersuchungshaft darf gegen den Beschuldigten angeordnet werden, wenn er der Tat dringend verdächtig ist und ein Haftgrund besteht. ² Sie darf nicht angeordnet werden, wenn sie zu der B...
- **[Judge=3]** `§ 112 StPO – III. Flucht (Abs – Rn. 23` — Behandelt direkt Haftgruende fuer Untersuchungshaft
  > Bei einer besonders hohen Straferwartung braucht daher nur geprüft zu werden, ob Umstände vorhanden sind, die die hieraus herzuleitende Fluchtgefahr ausräumen können (KG StV 1996, 383; OLG München Str...
- **[Judge=3]** `§ 112 StPO – Rn. 112` — Erklärt dringenden Tatverdacht als zentrale UHaft-Voraussetzung
  > Haftunfähigkeit des Beschuldigten schließt den Erlass des Haftbefehls nicht aus, sondern hindert nur seinen Vollzug (OLG Düsseldorf JZ 1984, 248; OLG Frankfurt a.M. NJW 1968, 2302; OLG Nürnberg OLGSt ...

#### ours-cohere — Top 3
- **[Judge=3]** `§ 112 StPO – Rn. 112` — Direkt relevant: zentrale Norm zur Untersuchungshaft
  > 112 (1) ¹ Die Untersuchungshaft darf gegen den Beschuldigten angeordnet werden, wenn er der Tat dringend verdächtig ist und ein Haftgrund besteht. ² Sie darf nicht angeordnet werden, wenn sie zu der B...
- **[Judge=3]** `§ 112 StPO – III. Flucht (Abs – Rn. 23` — Direkt relevant: Fluchtgefahr und Verdunkelungsgefahr als Haftgruende
  > Bei einer besonders hohen Straferwartung braucht daher nur geprüft zu werden, ob Umstände vorhanden sind, die die hieraus herzuleitende Fluchtgefahr ausräumen können (KG StV 1996, 383; OLG München Str...
- **[Judge=3]** `§ 112 StPO – III. Flucht (Abs – Rn. 32 (Teil 2)` — Direkt relevant zu Untersuchungshaft und Verdunkelungsgefahr
  > Wenn die Verdunkelungshandlungen nicht geeignet sind, die Ermittlung der Wahrheit zu erschweren, darf UHaft nicht angeordnet werden. Der Haftgrund liegt daher nicht vor, wenn der Sachverhalt schon in ...

#### ours-mxbai — Top 3
- **[Judge=3]** `§ 112 StPO – Rn. 112` — Beantwortet direkt Untersuchungshaft-Voraussetzungen
  > 112 (1) ¹ Die Untersuchungshaft darf gegen den Beschuldigten angeordnet werden, wenn er der Tat dringend verdächtig ist und ein Haftgrund besteht. ² Sie darf nicht angeordnet werden, wenn sie zu der B...
- **[Judge=3]** `§ 112 StPO – III. Flucht (Abs – Rn. 23` — Direkt relevant zu Untersuchungshaft und Haftgruenden
  > Bei einer besonders hohen Straferwartung braucht daher nur geprüft zu werden, ob Umstände vorhanden sind, die die hieraus herzuleitende Fluchtgefahr ausräumen können (KG StV 1996, 383; OLG München Str...
- **[Judge=3]** `§ 112 StPO – Rn. 112` — Direkt relevant: behandelt Untersuchungshaft-Voraussetzungen dringender Tatverdacht
  > Haftunfähigkeit des Beschuldigten schließt den Erlass des Haftbefehls nicht aus, sondern hindert nur seinen Vollzug (OLG Düsseldorf JZ 1984, 248; OLG Frankfurt a.M. NJW 1968, 2302; OLG Nürnberg OLGSt ...

### q13 — stpo-prozess

**Query:** Welche Voraussetzungen hat die Untersuchungshaft wegen Fluchtgefahr?

**Kontext:** § 112 Abs. 2 Nr. 2 StPO Fluchtgefahr

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours | 0.94 | 80% | 67% | 3 | 5.2s |
| ours-cohere | 1.00 | 80% | 100% | 3 | 5.2s |
| ours-mxbai | 0.99 | 80% | 100% | 3 | 4.9s |

#### ours — Top 3
- **[Judge=3]** `§ 112 StPO – Rn. 112` — Direkt relevante Rechtsgrundlage zu Fluchtgefahr-Voraussetzungen
  > 112 (1) ¹ Die Untersuchungshaft darf gegen den Beschuldigten angeordnet werden, wenn er der Tat dringend verdächtig ist und ein Haftgrund besteht. ² Sie darf nicht angeordnet werden, wenn sie zu der B...
- **[Judge=1]** `§ 112 StPO – Rn. 112` — Behandelt allgemeine Haftvoraussetzungen, nicht spezifisch Fluchtgefahr
  > Haftunfähigkeit des Beschuldigten schließt den Erlass des Haftbefehls nicht aus, sondern hindert nur seinen Vollzug (OLG Düsseldorf JZ 1984, 248; OLG Frankfurt a.M. NJW 1968, 2302; OLG Nürnberg OLGSt ...
- **[Judge=3]** `§ 112 StPO – III. Flucht (Abs – Rn. 22` — Behandelt direkt Tatsachenerfordernisse bei Fluchtgefahr
  > 22 Die Fluchtgefahr darf nur aus bestimmten Tatsachen hergeleitet werden. Bloße Mutmaßungen u. Befürchtungen genügen nicht. Die Tatsachen brauchen aber nicht zur vollen Überzeugung des Gerichts festzu...

#### ours-cohere — Top 3
- **[Judge=3]** `§ 112 StPO – Rn. 112` — Enthaelt direkt § 112 Abs. 2 Nr. 2 Fluchtgefahr
  > 112 (1) ¹ Die Untersuchungshaft darf gegen den Beschuldigten angeordnet werden, wenn er der Tat dringend verdächtig ist und ein Haftgrund besteht. ² Sie darf nicht angeordnet werden, wenn sie zu der B...
- **[Judge=3]** `§ 112 StPO – III. Flucht (Abs – Rn. 17 (Teil 1)` — Direkt relevant: definiert Fluchtgefahr-Voraussetzungen nach § 112
  > 17 IV. Fluchtgefahr (Abs. 2 Nr. 2). Fluchtgefahr (Abs. 2 Nr. 2) besteht, wenn die Würdigung der Umstände des Falles es wahrscheinlicher macht, dass sich der Beschuldigte dem Strafverfahren entziehen, ...
- **[Judge=3]** `§ 112 StPO – III. Flucht (Abs – Rn. 17` — Direkt relevant - definiert konkrete Fluchtgefahr-Kriterien
  > Die Beurteilung der Fluchtgefahr erfordert die Berücksichtigung aller Umstände des Falles, insbes. der Art der dem Beschuldigten vorgeworfenen Tat, der Persönlichkeit des Beschuldigten, seiner Lebensv...

#### ours-mxbai — Top 3
- **[Judge=3]** `§ 112 StPO – Rn. 112` — Zentrale Vorschrift zu Fluchtgefahr-Voraussetzungen
  > 112 (1) ¹ Die Untersuchungshaft darf gegen den Beschuldigten angeordnet werden, wenn er der Tat dringend verdächtig ist und ein Haftgrund besteht. ² Sie darf nicht angeordnet werden, wenn sie zu der B...
- **[Judge=3]** `§ 112 StPO – III. Flucht (Abs – Rn. 16` — Direkt zu Fluchtgefahr § 112 Abs. 2 Nr. 2
  > 16 Bei Ergreifung des Beschuldigten aufgrund des nach Abs. 2 Nr. 1 erlassenen Haftbefehls entfällt der Haftgrund der Flucht. In der Regel wird die vorherige Flucht aber die Aufrechterhaltung des Haftb...
- **[Judge=3]** `§ 112 StPO – III. Flucht (Abs – Rn. 17` — Direkt relevant: zentrale Voraussetzungen der Fluchtgefahr detailliert
  > Die Beurteilung der Fluchtgefahr erfordert die Berücksichtigung aller Umstände des Falles, insbes. der Art der dem Beschuldigten vorgeworfenen Tat, der Persönlichkeit des Beschuldigten, seiner Lebensv...

### q14 — stpo-prozess

**Query:** Wie lange darf die Untersuchungshaft maximal dauern?

**Kontext:** § 121 StPO Sechs-Monats-Grenze, Haftpruefung OLG

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours | 0.97 | 100% | 100% | 3 | 5.4s |
| ours-cohere | 1.00 | 100% | 100% | 3 | 5.4s |
| ours-mxbai | 0.99 | 80% | 100% | 3 | 5.4s |

#### ours — Top 3
- **[Judge=3]** `§ 121 StPO – Rn. 1` — Direkt relevant zur maximalen Dauer der Untersuchungshaft
  > Eine absolute Höchstgrenze für die Dauer v. UHaft sieht weder die StPO noch die EMRK vor (EGMR EuGRZ 1993, 384). Es kommt auf eine Abwägung aller Umstände des Einzelfalls an. Eine ein Jahr übersteigen...
- **[Judge=2]** `§ 121 StPO – Rn. 8 (Teil 1)` — Behandelt UHaft-Beschränkungen, aber nicht konkrete Höchstdauer
  > 8 II. Zeitliche Geltung der Beschränkungen der UHaft. Bis zu einem auf Freiheitsentziehung lautenden Urteil (Freiheitsstrafe mit o. ohne Bewährung o. freiheitsentziehende Sicherungsmaßregeln) gelten d...
- **[Judge=3]** `§ 121 StPO – Rn. 121` — Beantwortet direkt die Frage zur Sechsmonatsfrist
  > 121 (1) Solange kein Urteil ergangen ist, das auf Freiheitsstrafe oder eine freiheitsentziehende Maßregel der Besserung und Sicherung erkennt, darf der Vollzug der Untersuchungshaft wegen derselben Ta...

#### ours-cohere — Top 3
- **[Judge=3]** `§ 121 StPO – Rn. 1` — Direkt relevant: behandelt Höchstgrenzen der Untersuchungshaft detailliert
  > Eine absolute Höchstgrenze für die Dauer v. UHaft sieht weder die StPO noch die EMRK vor (EGMR EuGRZ 1993, 384). Es kommt auf eine Abwägung aller Umstände des Einzelfalls an. Eine ein Jahr übersteigen...
- **[Judge=3]** `§ 121 StPO – Rn. 1` — Direkt relevant: behandelt maximale Dauer Untersuchungshaft
  > 1 A. Beschleunigungsgebot. Einen Anspruch auf beschleunigte Aburteilung hat der in UHaft (und einstweiliger Unterbringung) befindliche Beschuldigte nach Art. 5 Abs. 3 S. 2 EMRK (→ EMRK Art. 5 Rn. 10 f...
- **[Judge=3]** `§ 121 StPO – Rn. 16` — Behandelt direkt § 121 StPO Sechs-Monats-Grenze
  > 16 IV. Unmöglichkeit des Urteilserlasses innerhalb der 6-Monats-Frist. 1. Die besondere Schwierigkeit oder der besondere Umfang der Ermittlungen führen nur dann zur Aufrechterhaltung der UHaft, wenn d...

#### ours-mxbai — Top 3
- **[Judge=3]** `§ 121 StPO – Rn. 1` — Direkt relevant: Behandelt Höchstgrenzen der Untersuchungshaft detailliert
  > Eine absolute Höchstgrenze für die Dauer v. UHaft sieht weder die StPO noch die EMRK vor (EGMR EuGRZ 1993, 384). Es kommt auf eine Abwägung aller Umstände des Einzelfalls an. Eine ein Jahr übersteigen...
- **[Judge=3]** `§ 121 StPO – Rn. 1` — Direkte Antwort zur Sechs-Monats-Grenze und Überschreitung durch OLG
  > 1 A. Beschleunigungsgebot. Einen Anspruch auf beschleunigte Aburteilung hat der in UHaft (und einstweiliger Unterbringung) befindliche Beschuldigte nach Art. 5 Abs. 3 S. 2 EMRK (→ EMRK Art. 5 Rn. 10 f...
- **[Judge=2]** `§ 121 StPO – Rn. 8 (Teil 1)` — Behandelt UHaft-Beschränkungen, aber nicht konkrete Höchstdauer
  > 8 II. Zeitliche Geltung der Beschränkungen der UHaft. Bis zu einem auf Freiheitsentziehung lautenden Urteil (Freiheitsstrafe mit o. ohne Bewährung o. freiheitsentziehende Sicherungsmaßregeln) gelten d...

### q15 — stpo-prozess

**Query:** Was regelt § 136 StPO zur Beschuldigtenvernehmung?

**Kontext:** Belehrungspflichten, Recht auf Verteidiger

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours | 0.91 | 80% | 100% | 2 | 5.1s |
| ours-cohere | 0.91 | 100% | 100% | 2 | 5.0s |
| ours-mxbai | 0.96 | 60% | 67% | 3 | 5.0s |

#### ours — Top 3
- **[Judge=2]** `§ 500 StPO – ILL. für das Strafverfahren und das Bußgeldverf` — Behandelt Beschuldigtenvernehmung und Belehrungspflichten, aber nicht § 136 StPO direkt
  > (4) Zeugen können zur Aufenthaltsermittlung ausgeschrieben werden.  (5) Für die internationale Fahndung nach Personen, einschließlich der Fahndung nach Personen im SIS und aufgrund eines Europäischen ...
- **[Judge=3]** `§ 114b StPO – I. Abs – Rn. 5` — Direkt relevant: behandelt Belehrungspflichten nach § 136 StPO
  > 5 II. Abs. 2 S. 1 Nr. 2–4. Hier wird die auch nach § 136 Abs. 1 S. 2, 3 und § 163a Abs. 3 S. 2, 4 vor Beginn der ersten richterlichen bzw. staatsanwaltschaftlichen o. polizeilichen Vernehmung bestehen...
- **[Judge=2]** `§ 114c StPO` — Behandelt Belehrungspflichten, aber spezifisch für Ausländer
  > GVG) u. RiVASt 135 vorgeschrieben. Der Ausländer ist danach zu belehren, dass er die (unverzügliche) Benachrichtigung seiner konsularischen Vertretung v. der Festnahme verlangen darf. Dies gilt auch f...

#### ours-cohere — Top 3
- **[Judge=2]** `§ 114c StPO` — Behandelt Belehrungspflichten, aber konsularischen Beistand statt § 136
  > GVG) u. RiVASt 135 vorgeschrieben. Der Ausländer ist danach zu belehren, dass er die (unverzügliche) Benachrichtigung seiner konsularischen Vertretung v. der Festnahme verlangen darf. Dies gilt auch f...
- **[Judge=2]** `§ 500 StPO – ILL. für das Strafverfahren und das Bußgeldverf` — Thematisch relevant: Belehrung nach § 136 erwähnt
  > (4) Zeugen können zur Aufenthaltsermittlung ausgeschrieben werden.  (5) Für die internationale Fahndung nach Personen, einschließlich der Fahndung nach Personen im SIS und aufgrund eines Europäischen ...
- **[Judge=2]** `StPO – III. Steuerstrafverfahren – Rn. 79` — Behandelt Belehrungspflichten bei informatorischer Befragung vs Beschuldigtenvernehmung
  > 79 3. Die informatorische Befragung der Tatverdächtigen, die nach diesen Grundsätzen noch keine Beschuldigten sind, ist Zeugenvernehmung. Die Bestrebungen des Schrifttums, neben Beschuldigte u. Zeugen...

#### ours-mxbai — Top 3
- **[Judge=3]** `§ 114b StPO – I. Abs – Rn. 5` — Direkt relevant: behandelt Belehrungspflichten nach § 136 StPO
  > 5 II. Abs. 2 S. 1 Nr. 2–4. Hier wird die auch nach § 136 Abs. 1 S. 2, 3 und § 163a Abs. 3 S. 2, 4 vor Beginn der ersten richterlichen bzw. staatsanwaltschaftlichen o. polizeilichen Vernehmung bestehen...
- **[Judge=1]** `§ 115 StPO – Rn. 5` — Behandelt Vorführung/Vernehmung, nicht § 136 StPO Belehrungspflichten
  > 5 Am Tage nach der Ergreifung darf er nur vorgeführt werden, wenn eine frühere Vorführung nicht möglich ist. Spätestens an diesem Tage muss die Vorführung aber stattfinden, auch wenn er ein Sonnabend,...
- **[Judge=2]** `§ 500 StPO – ILL. für das Strafverfahren und das Bußgeldverf` — Behandelt Beschuldigtenvernehmung, aber nicht § 136 StPO direkt
  > (4) Zeugen können zur Aufenthaltsermittlung ausgeschrieben werden.  (5) Für die internationale Fahndung nach Personen, einschließlich der Fahndung nach Personen im SIS und aufgrund eines Europäischen ...

### q16 — cross-reference

**Query:** Worin unterscheidet sich Betrug von Unterschlagung?

**Kontext:** Abgrenzung § 263 vs § 246 StGB

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours | 0.93 | 100% | 100% | 2 | 6.0s |
| ours-cohere | 0.94 | 60% | 67% | 3 | 6.5s |
| ours-mxbai | 0.97 | 40% | 67% | 2 | 6.5s |

#### ours — Top 3
- **[Judge=2]** `§ 247 StGB – BT. Neunzehnter Abschnitt – Rn. 24` — Konkurrenzregelung zwischen § 263 und § 246
  > 24 L. Konkurrenzen im Übrigen. Bei Manifestation des Zueignungswillens hinsichtlich mehrerer Sachen durch eine Ausführungshandlung liegt nur eine Tat vor (wistra 2006, 227 (227 f.)). Zur Abgrenzung vo...
- **[Judge=2]** `§ 263 StGB – BT. Zweitundzwanzigster Abschnitt – Rn. 69` — Betrug relevant, aber keine direkte Abgrenzung zur Unterschlagung
  > 69 Anders ist es, wenn der Verfügende seinerseits nur (gutgläubige) Hilfsperson eines bösgläubigen Dritten ist. Hier ist auf den Irrtum des Entscheidungsbefugten abzustellen: Erkennt dieser die Unrich...
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 76` — Betrifft direkt Abgrenzung Betrug zu anderen Vermögensdelikten
  > 4. Dreiecksbetrug. Da die Getäuschte und die verfügende, nicht aber die verfügende und die geschädigte Person identisch sein müssen, ist der Tatbestand des § 263 nur erfüllt, wenn die Vermögensverfügu...

#### ours-cohere — Top 3
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 76` — Zentral für Abgrenzung Betrug vs Unterschlagung
  > 4. Dreiecksbetrug. Da die Getäuschte und die verfügende, nicht aber die verfügende und die geschädigte Person identisch sein müssen, ist der Tatbestand des § 263 nur erfüllt, wenn die Vermögensverfügu...
- **[Judge=1]** `§ 263 StGB – BT. Zweitundzwanzigster Abschnitt – Rn. 69` — Behandelt Betrug, aber nicht Abgrenzung zur Unterschlagung
  > 69 Anders ist es, wenn der Verfügende seinerseits nur (gutgläubige) Hilfsperson eines bösgläubigen Dritten ist. Hier ist auf den Irrtum des Entscheidungsbefugten abzustellen: Erkennt dieser die Unrich...
- **[Judge=3]** `§ 263 StGB – I. Vermögensbegriff  – Rn. 263` — Enthält vollständigen Tatbestand § 263 für Abgrenzung
  > 263 (1) Wer in der Absicht, sich oder einem Dritten einen rechtswidrigen Vermögensvorteil zu verschaffen, das Vermögen eines anderen dadurch beschädigt, daß er durch Vorspiegelung falscher oder durch ...

#### ours-mxbai — Top 3
- **[Judge=2]** `§ 247 StGB – BT. Neunzehnter Abschnitt – Rn. 24` — Behandelt Abgrenzung § 246 zu § 263
  > 24 L. Konkurrenzen im Übrigen. Bei Manifestation des Zueignungswillens hinsichtlich mehrerer Sachen durch eine Ausführungshandlung liegt nur eine Tat vor (wistra 2006, 227 (227 f.)). Zur Abgrenzung vo...
- **[Judge=1]** `§ 263a StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 23` — Behandelt Betrug vs Computerbetrug, nicht vs Unterschlagung
  > 23 G. Subjektiver Tatbestand. Die Tat setzt (bedingten) Vorsatz voraus. Er muss sich auf alle Tatbestandsmerkmale, zu denen auch die Unbefugtheit (→ Rn. 10) gehört, dh auch auf die Voraussetzungen ers...
- **[Judge=2]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 76` — Betrug-Kontext relevant, aber keine direkte Unterschlagungsabgrenzung
  > 4. Dreiecksbetrug. Da die Getäuschte und die verfügende, nicht aber die verfügende und die geschädigte Person identisch sein müssen, ist der Tatbestand des § 263 nur erfüllt, wenn die Vermögensverfügu...

### q17 — cross-reference

**Query:** Was sind die Unterschiede zwischen Diebstahl und Raub?

**Kontext:** § 242 vs § 249 StGB — Abgrenzung durch Gewalt/Drohung

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours | 0.91 | 100% | 100% | 2 | 6.2s |
| ours-cohere | 0.89 | 80% | 100% | 2 | 6.4s |
| ours-mxbai | 1.00 | 60% | 100% | 3 | 6.8s |

#### ours — Top 3
- **[Judge=2]** `§ 242 StGB – BT. Neunzehnter Abschnitt – Rn. 31` — Behandelt nur Diebstahl, nicht Raub-Abgrenzung
  > 31 Bedingter Vorsatz reicht grds. aus. Das betrifft namentlich die Merkmale des Sachbegriffs, der Fremdheit und der Wegnahme. Hinsichtlich des normativen Merkmals der Fremdheit kommt es hierbei auf ei...
- **[Judge=3]** `§ 242 StGB – BT. Neunzehnter Abschnitt – Rn. 41` — Direkt relevant für Diebstahl-Tatbestand § 242
  > 41 2. Absicht. § 242 verlangt die Absicht der Zueignung im Zeitpunkt der Wegnahme (→ Rn. 43). Das bedeutet nach hM, dass es dem Täter auf die Herstellung einer eigentümerähnlichen Verfügungsgewalt ank...
- **[Judge=2]** `§ 242 StGB – BT. Neunzehnter Abschnitt – Rn. 55` — Thematisch relevant: behandelt Diebstahl (§242), aber nicht Raub-Abgrenzung
  > **Vorbereitung** ist gegeben bei Handlungen, die erst bei Eintritt weiterer Bedingungen oder Hinzutritt weiterer Handlungen zur Wegnahme führen sollen; etwa bei Anfertigen von Nachschlüsseln (vgl. BGH...

#### ours-cohere — Top 3
- **[Judge=2]** `§ 242 StGB – BT. Neunzehnter Abschnitt – Rn. 48` — Behandelt § 242 Diebstahl, aber nicht Raub-Abgrenzung
  > Die Absicht fehlt zB, wenn der Täter (im Fall der Drittzueignung der Dritte) ein gesetzliches Aneignungsrecht oder einen fälligen Anspruch auf Übereignung bestimmter Sachen (Stückschuld) hat (BGHSt 17...
- **[Judge=2]** `§ 242 StGB – BT. Neunzehnter Abschnitt – Rn. 31` — Behandelt Diebstahl-Vorsatz, aber nicht Raub-Abgrenzung
  > 31 Bedingter Vorsatz reicht grds. aus. Das betrifft namentlich die Merkmale des Sachbegriffs, der Fremdheit und der Wegnahme. Hinsichtlich des normativen Merkmals der Fremdheit kommt es hierbei auf ei...
- **[Judge=3]** `§ 242 StGB – BT. Neunzehnter Abschnitt – Rn. 7` — Erklaert zentrale Tatbestandsmerkmale des Diebstahls (Wegnahme, Gewahrsam)
  > 4. Anwartschaftsrecht. Ein Anspruch auf Eigentumsverschaffung, sei er rein schuldrechtlich oder dinglich gesichert (Anwartschaftsrecht), ändert nichts an der Fremdheit der Sache, so dass der Vorbehalt...

#### ours-mxbai — Top 3
- **[Judge=3]** `§ 249 StGB` — Erklärt Raub-Tatbestand und Abgrenzung zu anderen Delikten
  > NStZ 2023, 351). Danach ist § 249 gegenüber § 255 ein spezielles Delikt; in jedem Raub liegt eine räuberische Erpressung (aA die hM in der Literatur). Die Unterscheidung richtet sich nach dem äußeren ...
- **[Judge=3]** `§ 249 StGB – BT. Zwanzigster Abschnitt – Rn. 15` — Direkt relevant: erklärt subjektive Tatbestandsmerkmale beider Delikte
  > G. Subjektiver Tatbestand. Der Vorsatz muss entsprechend der Doppelnatur des Raubs sowohl Wegnahme (vgl. dazu → § 242 Rn. 29 ff.) als auch Nötigung (→ § 240 Rn. 53 f.) sowie deren Verknüpfung umfassen...
- **[Judge=3]** `§ 241a StGB – BT. Achtzchniter Abschnitt – Rn. 242` — Direkt relevant - Diebstahl-Definition und Tatbestandsmerkmale
  > 242 (1) Wer eine fremde bewegliche Sache einem anderen in der Absicht wegnimmt, die Sache sich oder einem Dritten rechtswidrig zuzueignen, wird mit Freiheitsstrafe bis zu fünf Jahren oder mit Geldstra...

### q18 — cross-reference

**Query:** Wann wird Betrug zu Computerbetrug und umgekehrt?

**Kontext:** § 263 vs § 263a StGB — Abgrenzung bei elektronischer Datenverarbeitung

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours | 0.82 | 40% | 33% | 1 | 5.9s |
| ours-cohere | 0.89 | 40% | 67% | 1 | 6.0s |
| ours-mxbai | 1.00 | 20% | 33% | 3 | 6.4s |

#### ours — Top 3
- **[Judge=1]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 62` — Betrug allgemein, aber nicht Computerbetrug-Abgrenzung
  > Die Kausalität der Täuschung für den Irrtum und dessen Kausalität für die Vermögensverfügung müssen im Einzelfall festgestellt sein. Mitverursachung reicht aus. Dabei darf das Gericht auch bei Serien-...
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 58` — Direkte Abgrenzung § 263/263a bei automatisierter Verarbeitung
  > 58 Im Geschäftsverkehr wird sich, wer die Berechtigung eines Leistungsverlangens oder -auftrags nicht zu prüfen hat, hierüber idR auch keine (richtigen oder falschen) Gedanken machen (NStZ 1997, 281; ...
- **[Judge=1]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 57` — Irrtumslehre bei Betrug, nicht Abgrenzung zu Computerbetrug
  > 57 2. Abgrenzung fehlerhafter von fehlenden Vorstellungen. Das gänzliche Fehlen einer Vorstellung, also die Unkenntnis relevanter Tatsachen, begründet für sich allein nach hM keinen Irrtum (BGHSt 2, 3...

#### ours-cohere — Top 3
- **[Judge=1]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 62` — Behandelt § 263, aber nicht Abgrenzung zu § 263a
  > Die Kausalität der Täuschung für den Irrtum und dessen Kausalität für die Vermögensverfügung müssen im Einzelfall festgestellt sein. Mitverursachung reicht aus. Dabei darf das Gericht auch bei Serien-...
- **[Judge=2]** `§ 263 StGB – BT. Zweriindzwanzigster Abschnitt – Rn. 234` — Behandelt § 263 Konkurrenzfragen, erwähnt § 263a kurz
  > Mit § 266 ist Tateinheit möglich, wenn im Rahmen einer schon bestehenden Vermögensbetreuungspflicht die Nachteilszufügung durch eine Täuschungshandlung bewirkt wird (BGH NStZ 2008, 340; wistra 2009, 1...
- **[Judge=2]** `§ 263 StGB – I. Vermögensbegriff  – Rn. 263` — Betrug-Grundtatbestand, aber ohne Abgrenzung zu Computerbetrug
  > 263 (1) Wer in der Absicht, sich oder einem Dritten einen rechtswidrigen Vermögensvorteil zu verschaffen, das Vermögen eines anderen dadurch beschädigt, daß er durch Vorspiegelung falscher oder durch ...

#### ours-mxbai — Top 3
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 58` — Direkte Abgrenzung § 263/263a bei automatisierten Verfahren
  > 58 Im Geschäftsverkehr wird sich, wer die Berechtigung eines Leistungsverlangens oder -auftrags nicht zu prüfen hat, hierüber idR auch keine (richtigen oder falschen) Gedanken machen (NStZ 1997, 281; ...
- **[Judge=1]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 62` — Allgemeiner Betrug, keine Abgrenzung zu Computerbetrug
  > Die Kausalität der Täuschung für den Irrtum und dessen Kausalität für die Vermögensverfügung müssen im Einzelfall festgestellt sein. Mitverursachung reicht aus. Dabei darf das Gericht auch bei Serien-...
- **[Judge=1]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 263 (Tei` — Literaturverzeichnis zu Betrug, keine Abgrenzungsregeln zu Computerbetrug
  > Fischer/Lutz    Betrug und Untreue   schende Warnung": Eine Drohung?, FS Puppe, 2011, 1217; Kupper, Mengenbegriffe im Strafgesetzbuch, FS Kohlmann, 2003, 133; Lampe, Personales Unrecht im Betrug, FS O...