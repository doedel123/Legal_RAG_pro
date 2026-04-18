# RAG Benchmark Report

_Generiert: 2026-04-19T00:47:51_


- Queries: **18**
- Top-K: **5**
- Systeme: ours, ours-cohere, ours-mxbai, ours-mxbai-voyage

## Gesamtvergleich

| Metrik | ours | ours-cohere | ours-mxbai | ours-mxbai-voyage |
|--------|--------|--------|--------|--------|
| nDCG@10 | 0.980 | 0.962 | 0.969 | 0.984 |
| Relevance@10 | 93.3% | 88.9% | 88.9% | 93.3% |
| Relevance@3 | 98.1% | 90.7% | 88.9% | 98.1% |
| Top-1-Score | 2.83 | 2.78 | 2.83 | 2.89 |
| Mean-Score | 2.68 | 2.54 | 2.57 | 2.69 |
| Latenz (s) | 5.58 | 5.71 | 5.60 | 5.65 |

## Nach Kategorie


### alltagssprache

| Metrik | ours | ours-cohere | ours-mxbai | ours-mxbai-voyage |
|--------|--------|--------|--------|--------|
| nDCG@10 | 0.981 | 0.976 | 0.993 | 0.999 |
| Relevance@10 | 100.0% | 95.0% | 95.0% | 100.0% |
| Relevance@3 | 100.0% | 100.0% | 91.7% | 100.0% |

### cross-reference

| Metrik | ours | ours-cohere | ours-mxbai | ours-mxbai-voyage |
|--------|--------|--------|--------|--------|
| nDCG@10 | 0.978 | 0.950 | 0.957 | 0.992 |
| Relevance@10 | 93.3% | 66.7% | 60.0% | 93.3% |
| Relevance@3 | 100.0% | 66.7% | 66.7% | 100.0% |

### exakte-paragraphen

| Metrik | ours | ours-cohere | ours-mxbai | ours-mxbai-voyage |
|--------|--------|--------|--------|--------|
| nDCG@10 | 0.987 | 0.997 | 0.988 | 0.995 |
| Relevance@10 | 95.0% | 100.0% | 100.0% | 95.0% |
| Relevance@3 | 100.0% | 100.0% | 100.0% | 100.0% |

### konzept

| Metrik | ours | ours-cohere | ours-mxbai | ours-mxbai-voyage |
|--------|--------|--------|--------|--------|
| nDCG@10 | 0.985 | 0.923 | 0.930 | 0.988 |
| Relevance@10 | 90.0% | 85.0% | 90.0% | 90.0% |
| Relevance@3 | 91.7% | 83.3% | 83.3% | 100.0% |

### stpo-prozess

| Metrik | ours | ours-cohere | ours-mxbai | ours-mxbai-voyage |
|--------|--------|--------|--------|--------|
| nDCG@10 | 0.964 | 0.961 | 0.977 | 0.933 |
| Relevance@10 | 86.7% | 93.3% | 93.3% | 86.7% |
| Relevance@3 | 100.0% | 100.0% | 100.0% | 88.9% |

## Detail pro Query


### q01 — exakte-paragraphen

**Query:** Welche Voraussetzungen hat der gewerbsmaessige Bandenbetrug nach § 263 Abs. 5 StGB?

**Kontext:** Qualifikationstatbestand des Bandenbetrugs im Fischer-Kommentar

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours | 0.99 | 100% | 100% | 3 | 6.4s |
| ours-cohere | 1.00 | 100% | 100% | 3 | 6.6s |
| ours-mxbai | 0.99 | 100% | 100% | 3 | 6.1s |
| ours-mxbai-voyage | 1.00 | 100% | 100% | 3 | 6.5s |

#### ours — Top 3
- **[Judge=3]** `§ 263 StGB – BT. Zweriindzwanzigster Abschnitt – Rn. 225` — Behandelt direkt § 263 Abs. 5 Voraussetzungen
  > IV. Qualifikation (Abs. 5). Abs. 5 enthält einen Qualifikationstatbestand, der die Tat in Fällen kumulativ gewerbs- und bandenmäßiger Begehung zum Verbrechen macht. Die Qualifikation ist in die Urteil...
- **[Judge=3]** `§ 263 StGB – BT. Zweijundzwanzigster Abschnitt – Rn. 213` — Direkt relevant: behandelt Qualifikationstatbestand § 263 Abs. 5
  > 213 Sind beide Varianten erfüllt, ist eine Qualifikation nach Abs. 5 gegeben. Die Abgrenzung des Abs. 3 Nr. 1 zum Verbrechen nach Abs. 5 ist in Fällen bandenmäßiger Begehung schwierig, denn eine auf f...
- **[Judge=2]** `§ 263 StGB – BT. Zweijundzwanzigster Abschnitt – Rn. 212` — Behandelt Bandenbetrug, aber fokussiert auf andere Paragraphen
  > 212 Der Begriff der Urkundenfälschung ist weit zu fassen; er umfasst neben Taten nach § 267 auch solche nach §§ 268–281 (LK-StGB/Kubiciel/Tiedemann Rn. 297; NK-StGB/Kindhäuser/Hoven Rn. 392). Entsprec...

#### ours-cohere — Top 3
- **[Judge=3]** `§ 263 StGB – BT. Zweijundzwanzigster Abschnitt – Rn. 213` — Direkt relevant für gewerbsmäßigen Bandenbetrug § 263 Abs. 5
  > 213 Sind beide Varianten erfüllt, ist eine Qualifikation nach Abs. 5 gegeben. Die Abgrenzung des Abs. 3 Nr. 1 zum Verbrechen nach Abs. 5 ist in Fällen bandenmäßiger Begehung schwierig, denn eine auf f...
- **[Judge=3]** `§ 263 StGB – BT. Zweriindzwanzigster Abschnitt – Rn. 225` — Behandelt direkt gewerbsmäßigen Bandenbetrug § 263 Abs. 5
  > IV. Qualifikation (Abs. 5). Abs. 5 enthält einen Qualifikationstatbestand, der die Tat in Fällen kumulativ gewerbs- und bandenmäßiger Begehung zum Verbrechen macht. Die Qualifikation ist in die Urteil...
- **[Judge=3]** `§ 263 StGB – I. Vermögensbegriff  – Rn. 263` — Enthält direkt § 263 Abs. 5 Bandenbetrug-Voraussetzungen
  > 263 (1) Wer in der Absicht, sich oder einem Dritten einen rechtswidrigen Vermögensvorteil zu verschaffen, das Vermögen eines anderen dadurch beschädigt, daß er durch Vorspiegelung falscher oder durch ...

#### ours-mxbai — Top 3
- **[Judge=3]** `§ 263 StGB – BT. Zweriindzwanzigster Abschnitt – Rn. 225` — Direkt relevant: Voraussetzungen Abs. 5 detailliert erklärt
  > IV. Qualifikation (Abs. 5). Abs. 5 enthält einen Qualifikationstatbestand, der die Tat in Fällen kumulativ gewerbs- und bandenmäßiger Begehung zum Verbrechen macht. Die Qualifikation ist in die Urteil...
- **[Judge=3]** `§ 263 StGB – BT. Zweijundzwanzigster Abschnitt – Rn. 213` — Direkt relevant zu Bandenbetrug Qualifikationstatbestand § 263 Abs. 5
  > 213 Sind beide Varianten erfüllt, ist eine Qualifikation nach Abs. 5 gegeben. Die Abgrenzung des Abs. 3 Nr. 1 zum Verbrechen nach Abs. 5 ist in Fällen bandenmäßiger Begehung schwierig, denn eine auf f...
- **[Judge=2]** `§ 263 StGB – BT. Zweijundzwanzigster Abschnitt – Rn. 212` — Behandelt Bandenbetrug, aber fokussiert auf Urkundenfälschung
  > 212 Der Begriff der Urkundenfälschung ist weit zu fassen; er umfasst neben Taten nach § 267 auch solche nach §§ 268–281 (LK-StGB/Kubiciel/Tiedemann Rn. 297; NK-StGB/Kindhäuser/Hoven Rn. 392). Entsprec...

#### ours-mxbai-voyage — Top 3
- **[Judge=3]** `§ 263 StGB – BT. Zweriindzwanzigster Abschnitt – Rn. 225` — Beantwortet direkt Voraussetzungen des gewerbsmäßigen Bandenbetrugs
  > IV. Qualifikation (Abs. 5). Abs. 5 enthält einen Qualifikationstatbestand, der die Tat in Fällen kumulativ gewerbs- und bandenmäßiger Begehung zum Verbrechen macht. Die Qualifikation ist in die Urteil...
- **[Judge=3]** `§ 263 StGB – I. Vermögensbegriff  – Rn. 263` — Direkt relevant: § 263 Abs. 5 vollständig enthalten
  > 263 (1) Wer in der Absicht, sich oder einem Dritten einen rechtswidrigen Vermögensvorteil zu verschaffen, das Vermögen eines anderen dadurch beschädigt, daß er durch Vorspiegelung falscher oder durch ...
- **[Judge=3]** `§ 263 StGB – BT. Zweijundzwanzigster Abschnitt – Rn. 211` — Definiert bandenmäßige Begehung bei Betrug direkt
  > 211 b) Bandenmäßigkeit. Bandenmäßige Begehung ist gegeben, wenn sich eine Bande (zum Begriff vgl. → § 244 Rn. 34 ff.) zur Begehung einer Mehrzahl von selbstständigen Taten der Urkundenfälschung oder d...

### q02 — exakte-paragraphen

**Query:** Was regelt § 112 StPO zur Untersuchungshaft?

**Kontext:** Anordnungsvoraussetzungen der U-Haft (dringender Tatverdacht, Haftgrund) im Schmitt/Koehler

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours | 0.99 | 100% | 100% | 3 | 5.0s |
| ours-cohere | 1.00 | 100% | 100% | 3 | 4.7s |
| ours-mxbai | 1.00 | 100% | 100% | 3 | 4.5s |
| ours-mxbai-voyage | 1.00 | 100% | 100% | 3 | 5.1s |

#### ours — Top 3
- **[Judge=3]** `§ 112 StPO – Rn. 112` — Direkt relevant: § 112 StPO Anordnungsvoraussetzungen der U-Haft
  > 112 (1) ¹ Die Untersuchungshaft darf gegen den Beschuldigten angeordnet werden, wenn er der Tat dringend verdächtig ist und ein Haftgrund besteht. ² Sie darf nicht angeordnet werden, wenn sie zu der B...
- **[Judge=3]** `§ 112 StPO – III. Flucht (Abs – Rn. 32 (Teil 2)` — Direkt relevant: behandelt Verdunkelungsgefahr als Haftgrund
  > Wenn die Verdunkelungshandlungen nicht geeignet sind, die Ermittlung der Wahrheit zu erschweren, darf UHaft nicht angeordnet werden. Der Haftgrund liegt daher nicht vor, wenn der Sachverhalt schon in ...
- **[Judge=2]** `§ 112 StPO – Rn. 112` — Behandelt Haftbefehl und dringenden Tatverdacht, nicht direkt § 112
  > Haftunfähigkeit des Beschuldigten schließt den Erlass des Haftbefehls nicht aus, sondern hindert nur seinen Vollzug (OLG Düsseldorf JZ 1984, 248; OLG Frankfurt a.M. NJW 1968, 2302; OLG Nürnberg OLGSt ...

#### ours-cohere — Top 3
- **[Judge=3]** `§ 112 StPO – Rn. 112` — Beantwortet die Frage direkt und vollstaendig
  > 112 (1) ¹ Die Untersuchungshaft darf gegen den Beschuldigten angeordnet werden, wenn er der Tat dringend verdächtig ist und ein Haftgrund besteht. ² Sie darf nicht angeordnet werden, wenn sie zu der B...
- **[Judge=3]** `§ 112 StPO – Rn. 112` — Behandelt direkt § 112 StPO Haftbefehlsvoraussetzungen
  > Haftunfähigkeit des Beschuldigten schließt den Erlass des Haftbefehls nicht aus, sondern hindert nur seinen Vollzug (OLG Düsseldorf JZ 1984, 248; OLG Frankfurt a.M. NJW 1968, 2302; OLG Nürnberg OLGSt ...
- **[Judge=3]** `§ 112 StPO – III. Flucht (Abs – Rn. 32 (Teil 2)` — Direkt relevant: behandelt Verdunkelungsgefahr als Haftgrund
  > Wenn die Verdunkelungshandlungen nicht geeignet sind, die Ermittlung der Wahrheit zu erschweren, darf UHaft nicht angeordnet werden. Der Haftgrund liegt daher nicht vor, wenn der Sachverhalt schon in ...

#### ours-mxbai — Top 3
- **[Judge=3]** `§ 112 StPO – Rn. 112` — Direkter Gesetzestext zu § 112 StPO Untersuchungshaft
  > 112 (1) ¹ Die Untersuchungshaft darf gegen den Beschuldigten angeordnet werden, wenn er der Tat dringend verdächtig ist und ein Haftgrund besteht. ² Sie darf nicht angeordnet werden, wenn sie zu der B...
- **[Judge=3]** `§ 112 StPO – III. Flucht (Abs – Rn. 32 (Teil 2)` — Direkt relevant: behandelt Verdunkelungsgefahr nach § 112 StPO
  > Wenn die Verdunkelungshandlungen nicht geeignet sind, die Ermittlung der Wahrheit zu erschweren, darf UHaft nicht angeordnet werden. Der Haftgrund liegt daher nicht vor, wenn der Sachverhalt schon in ...
- **[Judge=3]** `§ 112 StPO – Rn. 112` — Erklärt direkt § 112 StPO Haftgründe und Voraussetzungen
  > Haftunfähigkeit des Beschuldigten schließt den Erlass des Haftbefehls nicht aus, sondern hindert nur seinen Vollzug (OLG Düsseldorf JZ 1984, 248; OLG Frankfurt a.M. NJW 1968, 2302; OLG Nürnberg OLGSt ...

#### ours-mxbai-voyage — Top 3
- **[Judge=3]** `§ 112 StPO – Rn. 112` — Beantwortet direkt § 112 StPO Anordnungsvoraussetzungen
  > 112 (1) ¹ Die Untersuchungshaft darf gegen den Beschuldigten angeordnet werden, wenn er der Tat dringend verdächtig ist und ein Haftgrund besteht. ² Sie darf nicht angeordnet werden, wenn sie zu der B...
- **[Judge=3]** `§ 112 StPO – Rn. 112` — Behandelt direkt § 112 StPO Haftbefehlsvoraussetzungen
  > Haftunfähigkeit des Beschuldigten schließt den Erlass des Haftbefehls nicht aus, sondern hindert nur seinen Vollzug (OLG Düsseldorf JZ 1984, 248; OLG Frankfurt a.M. NJW 1968, 2302; OLG Nürnberg OLGSt ...
- **[Judge=3]** `§ 112 StPO – III. Flucht (Abs – Rn. 23` — Erklaert direkt Haftgruende nach § 112 StPO
  > Bei einer besonders hohen Straferwartung braucht daher nur geprüft zu werden, ob Umstände vorhanden sind, die die hieraus herzuleitende Fluchtgefahr ausräumen können (KG StV 1996, 383; OLG München Str...

### q03 — exakte-paragraphen

**Query:** Welche Haftgruende nennt § 112 Abs. 2 StPO?

**Kontext:** Fluchtgefahr, Verdunkelungsgefahr, Flucht — im StPO-Kommentar

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours | 1.00 | 80% | 100% | 3 | 4.5s |
| ours-cohere | 1.00 | 100% | 100% | 3 | 4.6s |
| ours-mxbai | 0.99 | 100% | 100% | 3 | 4.5s |
| ours-mxbai-voyage | 1.00 | 100% | 100% | 3 | 4.8s |

#### ours — Top 3
- **[Judge=3]** `§ 112 StPO – Rn. 112` — Vollständige Auflistung aller Haftgründe nach § 112 Abs. 2 StPO
  > 112 (1) ¹ Die Untersuchungshaft darf gegen den Beschuldigten angeordnet werden, wenn er der Tat dringend verdächtig ist und ein Haftgrund besteht. ² Sie darf nicht angeordnet werden, wenn sie zu der B...
- **[Judge=3]** `§ 112 StPO – III. Flucht (Abs – Rn. 23` — Behandelt direkt Haftgruende nach § 112 Abs. 2 StPO
  > Bei einer besonders hohen Straferwartung braucht daher nur geprüft zu werden, ob Umstände vorhanden sind, die die hieraus herzuleitende Fluchtgefahr ausräumen können (KG StV 1996, 383; OLG München Str...
- **[Judge=3]** `§ 112 StPO – III. Flucht (Abs – Rn. 32 (Teil 2)` — Behandelt direkt Verdunkelungsgefahr als Haftgrund § 112 Abs. 2
  > Wenn die Verdunkelungshandlungen nicht geeignet sind, die Ermittlung der Wahrheit zu erschweren, darf UHaft nicht angeordnet werden. Der Haftgrund liegt daher nicht vor, wenn der Sachverhalt schon in ...

#### ours-cohere — Top 3
- **[Judge=3]** `§ 112 StPO – Rn. 112` — Enthält vollständigen Wortlaut von § 112 Abs. 2 StPO
  > 112 (1) ¹ Die Untersuchungshaft darf gegen den Beschuldigten angeordnet werden, wenn er der Tat dringend verdächtig ist und ein Haftgrund besteht. ² Sie darf nicht angeordnet werden, wenn sie zu der B...
- **[Judge=3]** `§ 112 StPO – III. Flucht (Abs – Rn. 23` — Behandelt direkt Haftgruende Flucht- und Verdunkelungsgefahr
  > Bei einer besonders hohen Straferwartung braucht daher nur geprüft zu werden, ob Umstände vorhanden sind, die die hieraus herzuleitende Fluchtgefahr ausräumen können (KG StV 1996, 383; OLG München Str...
- **[Judge=2]** `§ 112 StPO – III. Flucht (Abs – Rn. 32 (Teil 2)` — Behandelt Verdunkelungsgefahr als einen der Haftgruende
  > Wenn die Verdunkelungshandlungen nicht geeignet sind, die Ermittlung der Wahrheit zu erschweren, darf UHaft nicht angeordnet werden. Der Haftgrund liegt daher nicht vor, wenn der Sachverhalt schon in ...

#### ours-mxbai — Top 3
- **[Judge=3]** `§ 112 StPO – Rn. 112` — Beantwortet direkt die Frage nach Haftgruenden
  > 112 (1) ¹ Die Untersuchungshaft darf gegen den Beschuldigten angeordnet werden, wenn er der Tat dringend verdächtig ist und ein Haftgrund besteht. ² Sie darf nicht angeordnet werden, wenn sie zu der B...
- **[Judge=3]** `§ 112 StPO – III. Flucht (Abs – Rn. 23` — Behandelt direkt Haftgruende nach § 112 Abs. 2 StPO
  > Bei einer besonders hohen Straferwartung braucht daher nur geprüft zu werden, ob Umstände vorhanden sind, die die hieraus herzuleitende Fluchtgefahr ausräumen können (KG StV 1996, 383; OLG München Str...
- **[Judge=2]** `§ 112 StPO – III. Flucht (Abs – Rn. 32 (Teil 2)` — Behandelt Verdunkelungsgefahr als einen der drei Haftgruende
  > Wenn die Verdunkelungshandlungen nicht geeignet sind, die Ermittlung der Wahrheit zu erschweren, darf UHaft nicht angeordnet werden. Der Haftgrund liegt daher nicht vor, wenn der Sachverhalt schon in ...

#### ours-mxbai-voyage — Top 3
- **[Judge=3]** `§ 112 StPO – Rn. 112` — Direkter Wortlaut von § 112 Abs. 2 StPO
  > 112 (1) ¹ Die Untersuchungshaft darf gegen den Beschuldigten angeordnet werden, wenn er der Tat dringend verdächtig ist und ein Haftgrund besteht. ² Sie darf nicht angeordnet werden, wenn sie zu der B...
- **[Judge=3]** `§ 112 StPO – III. Flucht (Abs – Rn. 23` — Beantwortet direkt Frage nach Haftgründen § 112 II StPO
  > Bei einer besonders hohen Straferwartung braucht daher nur geprüft zu werden, ob Umstände vorhanden sind, die die hieraus herzuleitende Fluchtgefahr ausräumen können (KG StV 1996, 383; OLG München Str...
- **[Judge=3]** `§ 112 StPO – III. Flucht (Abs – Rn. 17 (Teil 1)` — Direkt relevant, behandelt Fluchtgefahr als Haftgrund
  > 17 IV. Fluchtgefahr (Abs. 2 Nr. 2). Fluchtgefahr (Abs. 2 Nr. 2) besteht, wenn die Würdigung der Umstände des Falles es wahrscheinlicher macht, dass sich der Beschuldigte dem Strafverfahren entziehen, ...

### q04 — exakte-paragraphen

**Query:** Was regelt § 102 StPO zur Durchsuchung beim Beschuldigten?

**Kontext:** Durchsuchungsvoraussetzungen beim Verdaechtigen

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours | 0.97 | 100% | 100% | 3 | 5.0s |
| ours-cohere | 0.99 | 100% | 100% | 3 | 5.3s |
| ours-mxbai | 0.97 | 100% | 100% | 3 | 5.0s |
| ours-mxbai-voyage | 0.98 | 80% | 100% | 3 | 5.1s |

#### ours — Top 3
- **[Judge=3]** `§ 102 StPO – Rn. 102` — Beantwortet direkt die Frage zu § 102 StPO
  > 102 Bei dem, welcher als Täter oder Teilnehmer einer Straftat oder der Datenhehlerei, Begünstigung, Strafvereitelung oder Hehlerei  Köhler    Ermittlungsmaßnahmen  verdächtig ist, kann eine Durchsuchu...
- **[Judge=2]** `§ 102 StPO – Rn. 10` — Behandelt Durchsuchungsvoraussetzungen, aber nicht spezifisch § 102
  > II. Auffinden von Beweismitteln. Zu den Beweismitteln (→ § 94 Rn. 4 ff.) gehören auch die nur in § 103 erwähnten Spuren (SK-StPO/Jäger/Wohlers Rn. 21) u. Personen, die zu Beweiszwecken in Augenschein ...
- **[Judge=3]** `§ 102 StPO – Rn. 3` — Direkt relevant: behandelt § 102 StPO Durchsuchungsgegenstände
  > **Teilnehmer** nach §§ 25 ff. StGB, nicht die sog. notwendigen Teilnehmer (zum Begriff: Fischer/Fischer StGB Vor § 25 Rn. 7), stehen den Tatverdächtigen gleich. Bei jedem v. ihnen sowie bei den der Be...

#### ours-cohere — Top 3
- **[Judge=3]** `§ 102 StPO – Rn. 102` — Direkter Wortlaut von § 102 StPO mit Durchsuchungsvoraussetzungen
  > 102 Bei dem, welcher als Täter oder Teilnehmer einer Straftat oder der Datenhehlerei, Begünstigung, Strafvereitelung oder Hehlerei  Köhler    Ermittlungsmaßnahmen  verdächtig ist, kann eine Durchsuchu...
- **[Judge=3]** `§ 102 StPO – Rn. 10` — Direkt relevant: behandelt Durchsuchung bei Verdächtigen nach § 102 StPO
  > 10 III. Sachen. Sachen sind Kleidungsstücke, die der Verdächtige bei sich führt, ohne sie zu tragen, u. seine sonstige bewegliche Habe, gleichgültig, ob sie sich in seinem Umkreis, zB in Gepäckstücken...
- **[Judge=2]** `§ 102 StPO – Rn. 10` — Behandelt Durchsuchungsvoraussetzungen allgemein, nicht spezifisch § 102
  > II. Auffinden von Beweismitteln. Zu den Beweismitteln (→ § 94 Rn. 4 ff.) gehören auch die nur in § 103 erwähnten Spuren (SK-StPO/Jäger/Wohlers Rn. 21) u. Personen, die zu Beweiszwecken in Augenschein ...

#### ours-mxbai — Top 3
- **[Judge=3]** `§ 102 StPO – Rn. 102` — Regelt exakt § 102 StPO Durchsuchungsvoraussetzungen
  > 102 Bei dem, welcher als Täter oder Teilnehmer einer Straftat oder der Datenhehlerei, Begünstigung, Strafvereitelung oder Hehlerei  Köhler    Ermittlungsmaßnahmen  verdächtig ist, kann eine Durchsuchu...
- **[Judge=2]** `§ 102 StPO – Rn. 10` — Behandelt Durchsuchungsvoraussetzungen allgemein, aber nicht spezifisch § 102
  > II. Auffinden von Beweismitteln. Zu den Beweismitteln (→ § 94 Rn. 4 ff.) gehören auch die nur in § 103 erwähnten Spuren (SK-StPO/Jäger/Wohlers Rn. 21) u. Personen, die zu Beweiszwecken in Augenschein ...
- **[Judge=3]** `§ 102 StPO – Rn. 3` — Erläutert direkt Durchsuchungsgegenstände und Wohnungsbegriff § 102
  > **Teilnehmer** nach §§ 25 ff. StGB, nicht die sog. notwendigen Teilnehmer (zum Begriff: Fischer/Fischer StGB Vor § 25 Rn. 7), stehen den Tatverdächtigen gleich. Bei jedem v. ihnen sowie bei den der Be...

#### ours-mxbai-voyage — Top 3
- **[Judge=3]** `§ 102 StPO – Rn. 102` — Beantwortet direkt § 102 StPO Durchsuchungsvoraussetzungen
  > 102 Bei dem, welcher als Täter oder Teilnehmer einer Straftat oder der Datenhehlerei, Begünstigung, Strafvereitelung oder Hehlerei  Köhler    Ermittlungsmaßnahmen  verdächtig ist, kann eine Durchsuchu...
- **[Judge=2]** `§ 102 StPO – Rn. 10` — Behandelt Durchsuchungsvoraussetzungen, aber nicht spezifisch § 102
  > II. Auffinden von Beweismitteln. Zu den Beweismitteln (→ § 94 Rn. 4 ff.) gehören auch die nur in § 103 erwähnten Spuren (SK-StPO/Jäger/Wohlers Rn. 21) u. Personen, die zu Beweiszwecken in Augenschein ...
- **[Judge=3]** `§ 102 StPO – Rn. 3` — Direkt zu § 102 StPO Durchsuchungsgegenstände
  > **Teilnehmer** nach §§ 25 ff. StGB, nicht die sog. notwendigen Teilnehmer (zum Begriff: Fischer/Fischer StGB Vor § 25 Rn. 7), stehen den Tatverdächtigen gleich. Bei jedem v. ihnen sowie bei den der Be...

### q05 — konzept

**Query:** Wann liegt eine konkludente Taeuschung im Sinne des § 263 StGB vor?

**Kontext:** Taeuschungshandlung durch schluessiges Verhalten

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours | 1.00 | 100% | 100% | 3 | 4.6s |
| ours-cohere | 0.70 | 60% | 33% | 1 | 5.0s |
| ours-mxbai | 0.75 | 60% | 33% | 1 | 5.0s |
| ours-mxbai-voyage | 1.00 | 80% | 100% | 3 | 4.7s |

#### ours — Top 3
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 14` — Behandelt direkt konkludente Täuschung bei § 263
  > Rspr. und hM bejahen darüber hinaus aber die Möglichkeit einer Täuschung durch Unterlassen auch ohne Erklärung gegenüber dem Irrenden (→ Rn. 38; vgl. BGHSt 39, 392 (398); BayObLG NJW 1987, 1654 (mAnm ...
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 21` — Direkt relevant: definiert konkludente Taeuschung bei § 263
  > 21 2. Konkludente Erklärungen. Auch durch eine schlüssige Handlung (konkludente Erklärung) kann vorspiegelt werden. Eine solche konkludente Erklärung durch aktives Tun ist von einer Erklärung durch Un...
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 33` — Erklaert direkt konkludente Taeuschung bei Zahlungsbereitschaft
  > 33 f) Vorspiegelung von Zahlungsbereitschaft. Die schlüssige Erklärung, bei Fälligkeit einer Forderung zahlen zu können und zu wollen, ist der häufigste Fall konkludenter Täuschung (vgl. zB BGHSt 15, ...

#### ours-cohere — Top 3
- **[Judge=1]** `§ 263 StGB – I. Vermögensbegriff  – Rn. 263` — Gesetzestext ohne Erläuterung zu konkludenter Täuschung
  > 263 (1) Wer in der Absicht, sich oder einem Dritten einen rechtswidrigen Vermögensvorteil zu verschaffen, das Vermögen eines anderen dadurch beschädigt, daß er durch Vorspiegelung falscher oder durch ...
- **[Judge=0]** `§ 263 StGB – BT. Zweitundzwanzigster Abschnitt – Rn. 69` — Behandelt Verfügung/Irrtum, nicht konkludente Täuschung
  > 69 Anders ist es, wenn der Verfügende seinerseits nur (gutgläubige) Hilfsperson eines bösgläubigen Dritten ist. Hier ist auf den Irrtum des Entscheidungsbefugten abzustellen: Erkennt dieser die Unrich...
- **[Judge=2]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 263 (Tei` — Literaturverzeichnis zu Betrug, enthält relevante Spezialliteratur
  > Heghmanns, Strafbarkeit des „Phishing“ von Bankkontendaten und ihrer Verwertung, wistra 2007, 167; Hilgendorf, Tatsachenaussagen u. Werturteile im Strafrecht, 1998; Hillenkamp, Zum Schutz „deliktische...

#### ours-mxbai — Top 3
- **[Judge=1]** `§ 263 StGB – I. Vermögensbegriff  – Rn. 263` — Gesetzestext ohne konkludente Täuschung Details
  > 263 (1) Wer in der Absicht, sich oder einem Dritten einen rechtswidrigen Vermögensvorteil zu verschaffen, das Vermögen eines anderen dadurch beschädigt, daß er durch Vorspiegelung falscher oder durch ...
- **[Judge=2]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 263 (Tei` — Literaturverzeichnis zu Betrug, enthält relevante Titel zu konkludenter Täuschung
  > Heghmanns, Strafbarkeit des „Phishing“ von Bankkontendaten und ihrer Verwertung, wistra 2007, 167; Hilgendorf, Tatsachenaussagen u. Werturteile im Strafrecht, 1998; Hillenkamp, Zum Schutz „deliktische...
- **[Judge=0]** `§ 263 StGB – BT. Zweitundzwanzigster Abschnitt – Rn. 69` — Behandelt Verfuegungshandlung, nicht Taeuschungshandlung
  > 69 Anders ist es, wenn der Verfügende seinerseits nur (gutgläubige) Hilfsperson eines bösgläubigen Dritten ist. Hier ist auf den Irrtum des Entscheidungsbefugten abzustellen: Erkennt dieser die Unrich...

#### ours-mxbai-voyage — Top 3
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 21` — Beantwortet direkt konkludente Taeuschung bei § 263
  > 21 2. Konkludente Erklärungen. Auch durch eine schlüssige Handlung (konkludente Erklärung) kann vorspiegelt werden. Eine solche konkludente Erklärung durch aktives Tun ist von einer Erklärung durch Un...
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 14` — Erklaert konkludente Taeuschung und ihre Voraussetzungen direkt
  > 14 II. Tathandlung. Der Begriff „Täuschen“ ist im Wortlaut des Abs. 1 nicht verwendet; er ergibt sich aus dem Zusammenhang zwischen der Beschreibung der Tathandlung (→ Rn. 18) und dem Irrtum als ihrem...
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 14` — Direkt relevant zu konkludenter Täuschung § 263
  > Rspr. und hM bejahen darüber hinaus aber die Möglichkeit einer Täuschung durch Unterlassen auch ohne Erklärung gegenüber dem Irrenden (→ Rn. 38; vgl. BGHSt 39, 392 (398); BayObLG NJW 1987, 1654 (mAnm ...

### q06 — konzept

**Query:** Was ist eine Vermoegensverfuegung und welche Anforderungen stellt die Rechtsprechung?

**Kontext:** Tatbestandsmerkmal der Vermoegensverfuegung beim Betrug

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours | 0.96 | 80% | 100% | 3 | 5.5s |
| ours-cohere | 0.99 | 80% | 100% | 3 | 5.6s |
| ours-mxbai | 0.99 | 100% | 100% | 3 | 8.9s |
| ours-mxbai-voyage | 0.98 | 80% | 100% | 3 | 5.7s |

#### ours — Top 3
- **[Judge=3]** `§ 263 StGB – BT. Zweitundzwanzigster Abschnitt – Rn. 69` — Definiert Vermoegensverfuegung direkt und umfassend
  > 69 Anders ist es, wenn der Verfügende seinerseits nur (gutgläubige) Hilfsperson eines bösgläubigen Dritten ist. Hier ist auf den Irrtum des Entscheidungsbefugten abzustellen: Erkennt dieser die Unrich...
- **[Judge=2]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 87` — Behandelt Kausalität und Vermögensschaden, nicht Definition Vermögensverfügung
  > 87 5. Kausalität. Für die Vermögensverfügung muss der täuschungsbedingte Irrtum kausal sein (vgl. BGHSt 24, 257 (260); 24, 386 (389); NStZ 2003, 313 (314 f.); OLG Düsseldorf NJW 1987, 3145); Mitverurs...
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 76` — Behandelt direkt Vermoegensverfuegung beim Betrug mit Anforderungen
  > 4. Dreiecksbetrug. Da die Getäuschte und die verfügende, nicht aber die verfügende und die geschädigte Person identisch sein müssen, ist der Tatbestand des § 263 nur erfüllt, wenn die Vermögensverfügu...

#### ours-cohere — Top 3
- **[Judge=3]** `§ 263 StGB – BT. Zweitundzwanzigster Abschnitt – Rn. 69` — Definiert Vermoegensverfuegung und behandelt Rechtsprechungsanforderungen direkt
  > 69 Anders ist es, wenn der Verfügende seinerseits nur (gutgläubige) Hilfsperson eines bösgläubigen Dritten ist. Hier ist auf den Irrtum des Entscheidungsbefugten abzustellen: Erkennt dieser die Unrich...
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 76` — Direkt relevant: definiert Unmittelbarkeit der Vermoegensverfuegung beim Betrug
  > 76 3. Unmittelbarkeit der Verfügung. Neben der Freiwilligkeit ist das Merkmal der Unmittelbarkeit nach stRspr und hM das wichtigste Kriterium zur Beschränkung der § 263 unterfallenden Selbstschädigung...
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 87` — Erklaert Kausalitaet der Vermoegensverfuegung direkt relevant
  > 87 5. Kausalität. Für die Vermögensverfügung muss der täuschungsbedingte Irrtum kausal sein (vgl. BGHSt 24, 257 (260); 24, 386 (389); NStZ 2003, 313 (314 f.); OLG Düsseldorf NJW 1987, 3145); Mitverurs...

#### ours-mxbai — Top 3
- **[Judge=3]** `§ 263 StGB – BT. Zweitundzwanzigster Abschnitt – Rn. 69` — Direkt relevant: Definition und Anforderungen der Vermoegensverfuegung
  > 69 Anders ist es, wenn der Verfügende seinerseits nur (gutgläubige) Hilfsperson eines bösgläubigen Dritten ist. Hier ist auf den Irrtum des Entscheidungsbefugten abzustellen: Erkennt dieser die Unrich...
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 76` — Definiert Unmittelbarkeit bei Vermoegensverfuegung beim Betrug
  > 76 3. Unmittelbarkeit der Verfügung. Neben der Freiwilligkeit ist das Merkmal der Unmittelbarkeit nach stRspr und hM das wichtigste Kriterium zur Beschränkung der § 263 unterfallenden Selbstschädigung...
- **[Judge=2]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 87` — Behandelt Kausalität bei Vermögensverfügung, aber nicht Definition
  > 87 5. Kausalität. Für die Vermögensverfügung muss der täuschungsbedingte Irrtum kausal sein (vgl. BGHSt 24, 257 (260); 24, 386 (389); NStZ 2003, 313 (314 f.); OLG Düsseldorf NJW 1987, 3145); Mitverurs...

#### ours-mxbai-voyage — Top 3
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 76` — Definiert unmittelbare Vermoegensverfuegung beim Betrug direkt
  > 76 3. Unmittelbarkeit der Verfügung. Neben der Freiwilligkeit ist das Merkmal der Unmittelbarkeit nach stRspr und hM das wichtigste Kriterium zur Beschränkung der § 263 unterfallenden Selbstschädigung...
- **[Judge=2]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 87` — Behandelt Kausalität bei Vermögensverfügung, nicht Definition
  > 87 5. Kausalität. Für die Vermögensverfügung muss der täuschungsbedingte Irrtum kausal sein (vgl. BGHSt 24, 257 (260); 24, 386 (389); NStZ 2003, 313 (314 f.); OLG Düsseldorf NJW 1987, 3145); Mitverurs...
- **[Judge=3]** `§ 263 StGB – BT. Zweitundzwanzigster Abschnitt – Rn. 69` — Direkt relevant, definiert Vermoegensverfuegung beim Betrug
  > 69 Anders ist es, wenn der Verfügende seinerseits nur (gutgläubige) Hilfsperson eines bösgläubigen Dritten ist. Hier ist auf den Irrtum des Entscheidungsbefugten abzustellen: Erkennt dieser die Unrich...

### q07 — konzept

**Query:** Was versteht man unter einem Gefaehrdungsschaden beim Betrug?

**Kontext:** Schadensbegriff, schadensgleiche Vermoegensgefaehrdung

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours | 1.00 | 100% | 100% | 3 | 6.1s |
| ours-cohere | 1.00 | 100% | 100% | 3 | 6.3s |
| ours-mxbai | 1.00 | 100% | 100% | 3 | 5.6s |
| ours-mxbai-voyage | 1.00 | 100% | 100% | 3 | 6.4s |

#### ours — Top 3
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 159` — Definiert direkt Gefährdungsschaden beim Betrug
  > 159 b) Voraussetzungen. aa) Ein Gefährdungsschaden ist gegeben, wenn die Wahrscheinlichkeit des endgültigen Verlusts eines Vermögensbestandteils zum Zeitpunkt der täuschungsbedingten Verfügung so groß...
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 171` — Definiert Gefährdungsschaden beim Betrug direkt und konkret
  > Die täuschungsbedingte Herausgabe von EC-Karten, Kreditkarten und weiteren Zugangsdaten zu Bank-Guthaben (PINs, TANs; Passwörter), sei es infolge persönlicher Täuschung oder von „Phishing“-Manipulatio...
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 182` — Definiert direkt Gefaehrdungsschaden und dessen Vorsatzproblematik
  > 182 In Fällen des Gefährdungsschadens hat der BGH vielfach entschieden, die Kenntnis von Umständen, welche die Gefahr des Vermögensverlusts begründen, reiche oft, aber nicht in jedem Fall aus, um das ...

#### ours-cohere — Top 3
- **[Judge=3]** `§ 263 StGB – BT. Zwei undzwanzigster Abschnitt – Rn. 263 (Te` — Direkte Behandlung des Gefaehrdungsschadens beim Betrug
  > Fischer/Lutz    Betrug und Untreue   rechts für das Strafrecht, FS Weber, 2004, 271; Eisele/Bechtel, Der Schadensbegriff bei den Vermögensdelikten, JuS 2018, 97; Ellbogen/Wichmann, Zu Problemen des är...
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 159` — Direkte Definition des Gefährdungsschadens beim Betrug
  > 159 b) Voraussetzungen. aa) Ein Gefährdungsschaden ist gegeben, wenn die Wahrscheinlichkeit des endgültigen Verlusts eines Vermögensbestandteils zum Zeitpunkt der täuschungsbedingten Verfügung so groß...
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 182` — Behandelt direkt Gefährdungsschaden und Vorsatzproblematik beim Betrug
  > 182 In Fällen des Gefährdungsschadens hat der BGH vielfach entschieden, die Kenntnis von Umständen, welche die Gefahr des Vermögensverlusts begründen, reiche oft, aber nicht in jedem Fall aus, um das ...

#### ours-mxbai — Top 3
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 159` — Direkt relevant: definiert und erklaert Gefaehrdungsschaden beim Betrug
  > 159 b) Voraussetzungen. aa) Ein Gefährdungsschaden ist gegeben, wenn die Wahrscheinlichkeit des endgültigen Verlusts eines Vermögensbestandteils zum Zeitpunkt der täuschungsbedingten Verfügung so groß...
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 109` — Direkter Bezug zu Gefaehrdungsschaden beim Betrug
  > VI. Schaden. Vermögensschaden ist ein negativer Saldo zwischen dem Wert des Vermögens vor und nach der irrtumsbedingten Vermögensverfügung des Getäuschten (Prinzip der Gesamtsaldierung; stRspr; vgl. B...
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 182` — Behandelt direkt Gefährdungsschaden und Vorsatzelemente beim Betrug
  > 182 In Fällen des Gefährdungsschadens hat der BGH vielfach entschieden, die Kenntnis von Umständen, welche die Gefahr des Vermögensverlusts begründen, reiche oft, aber nicht in jedem Fall aus, um das ...

#### ours-mxbai-voyage — Top 3
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 159` — Definiert direkt Gefährdungsschaden beim Betrug
  > 159 b) Voraussetzungen. aa) Ein Gefährdungsschaden ist gegeben, wenn die Wahrscheinlichkeit des endgültigen Verlusts eines Vermögensbestandteils zum Zeitpunkt der täuschungsbedingten Verfügung so groß...
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 171` — Direkt relevant: erklärt Gefährdungsschaden beim Betrug ausführlich
  > Die täuschungsbedingte Herausgabe von EC-Karten, Kreditkarten und weiteren Zugangsdaten zu Bank-Guthaben (PINs, TANs; Passwörter), sei es infolge persönlicher Täuschung oder von „Phishing“-Manipulatio...
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 176` — Erklaert direkt Gefaehrdungsschaden beim Betrug detailliert
  > 176 Für die Schadensfeststellung kommt es auf den Gesamt-Vermögensstand des Opfers vor und nach dem Vertragsschluss an (BGHSt 31, 115 (117); NStZ 2008, 96 (98) (Bespr. Rose wistra 2009, 289)); maßgebl...

### q08 — konzept

**Query:** Wie wird der Vorsatz beim Betrug bestimmt, insbesondere die Bereicherungsabsicht?

**Kontext:** Subjektiver Tatbestand § 263 StGB

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours | 0.98 | 80% | 67% | 3 | 6.0s |
| ours-cohere | 1.00 | 100% | 100% | 3 | 6.0s |
| ours-mxbai | 0.99 | 100% | 100% | 3 | 5.7s |
| ours-mxbai-voyage | 0.97 | 100% | 100% | 3 | 5.1s |

#### ours — Top 3
- **[Judge=3]** `§ 263 StGB – I. Sonstige Vorschriften 239 – Rn. 263 (Teil 1)` — Behandelt direkt Bereicherungsabsicht und Vorsatz beim Betrug
  > 3. Einzelne Fallgruppen ... 92 4. Rechtlich missbilligte, sittenwidrige und gesetzeswidrige wirtschaftliche Werte ... 101 VI. Schaden ... 110 1. Grundsätze der Schadensermittlung ... 111 2. Vermögensm...
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 176` — Behandelt direkt Vorsatz und Bereicherungsabsicht bei Betrug
  > D. Subjektiver Tatbestand. § 263 setzt Vorsatz voraus; darüber hinaus ist die Absicht rechtswidriger Bereicherung erforderlich.   I. Vorsatz. 1. Täuschungsvorsatz. Der Vorsatz (bedingter Vorsatz genüg...
- **[Judge=1]** `§ 263 StGB – BT. Zweitundzwanzigster Abschnitt – Rn. 69` — Tangential: Verfügung beim Betrug, nicht Vorsatz/Bereicherungsabsicht
  > 69 Anders ist es, wenn der Verfügende seinerseits nur (gutgläubige) Hilfsperson eines bösgläubigen Dritten ist. Hier ist auf den Irrtum des Entscheidungsbefugten abzustellen: Erkennt dieser die Unrich...

#### ours-cohere — Top 3
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 176` — Behandelt direkt Vorsatz bei Betrug § 263
  > D. Subjektiver Tatbestand. § 263 setzt Vorsatz voraus; darüber hinaus ist die Absicht rechtswidriger Bereicherung erforderlich.   I. Vorsatz. 1. Täuschungsvorsatz. Der Vorsatz (bedingter Vorsatz genüg...
- **[Judge=3]** `§ 263 StGB – BT. Zweijundzwanzigster Abschnitt – Rn. 194` — Behandelt direkt Vorsatz bei § 263 StGB
  > 194 4. Vorsatz hinsichtlich der Rechtswidrigkeit. Die Rechtswidrigkeit des angestrebten Vermögensvorteils muss vom Vorsatz umfasst sein; sie ist wie bei § 253 (vgl. dort 20) subjektives Tatbestandsmer...
- **[Judge=3]** `§ 263 StGB – I. Sonstige Vorschriften 239 – Rn. 263 (Teil 1)` — Behandelt direkt Bereicherungsabsicht und Vorsatz bei Betrug
  > 3. Einzelne Fallgruppen ... 92 4. Rechtlich missbilligte, sittenwidrige und gesetzeswidrige wirtschaftliche Werte ... 101 VI. Schaden ... 110 1. Grundsätze der Schadensermittlung ... 111 2. Vermögensm...

#### ours-mxbai — Top 3
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 176` — Direkt relevant, behandelt Vorsatz bei § 263 StGB
  > D. Subjektiver Tatbestand. § 263 setzt Vorsatz voraus; darüber hinaus ist die Absicht rechtswidriger Bereicherung erforderlich.   I. Vorsatz. 1. Täuschungsvorsatz. Der Vorsatz (bedingter Vorsatz genüg...
- **[Judge=3]** `§ 263 StGB – I. Sonstige Vorschriften 239 – Rn. 263 (Teil 1)` — Behandelt direkt Bereicherungsabsicht und Vorsatz beim Betrug
  > 3. Einzelne Fallgruppen ... 92 4. Rechtlich missbilligte, sittenwidrige und gesetzeswidrige wirtschaftliche Werte ... 101 VI. Schaden ... 110 1. Grundsätze der Schadensermittlung ... 111 2. Vermögensm...
- **[Judge=2]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 187 (Tei` — Stoffgleichheit relevant, aber nicht Vorsatz/Bereicherungsabsicht direkt
  > 187 1. Stoffgleichheit. Der Vorteil muss die Kehrseite des Schadens und ihm „stoffgleich“ sein; er muss unmittelbare Folge der täuschungsbedingten Verfügung sein, welche den Schaden des Opfers herbeif...

#### ours-mxbai-voyage — Top 3
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 176` — Direkt relevant: behandelt Vorsatz und Bereicherungsabsicht bei § 263 StGB
  > D. Subjektiver Tatbestand. § 263 setzt Vorsatz voraus; darüber hinaus ist die Absicht rechtswidriger Bereicherung erforderlich.   I. Vorsatz. 1. Täuschungsvorsatz. Der Vorsatz (bedingter Vorsatz genüg...
- **[Judge=2]** `§ 263 StGB – I. Vermögensbegriff  – Rn. 263` — Gesetzestext mit Bereicherungsabsicht, aber keine Vorsatzbestimmung
  > 263 (1) Wer in der Absicht, sich oder einem Dritten einen rechtswidrigen Vermögensvorteil zu verschaffen, das Vermögen eines anderen dadurch beschädigt, daß er durch Vorspiegelung falscher oder durch ...
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 186` — Direkt relevant: definiert Bereicherungsabsicht bei Betrug
  > 186 II. Bereicherungsabsicht. Die Tat muss subjektiv auf die Erlangung eines rechtswidrigen Vermögensvorteils für den Täuschenden oder einen Dritten gerichtet sein. Vermögensvorteil ist die Erhöhung d...

### q09 — alltagssprache

**Query:** Hat der Angeklagte die Kunden über das Internet betrogen?

**Kontext:** Abstrakte Frage zu Internetbetrug, sucht Taeuschungshandlung + Schaden

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours | 0.92 | 100% | 100% | 2 | 5.1s |
| ours-cohere | 0.93 | 100% | 100% | 2 | 5.6s |
| ours-mxbai | 0.97 | 80% | 67% | 3 | 5.1s |
| ours-mxbai-voyage | 1.00 | 100% | 100% | 3 | 5.2s |

#### ours — Top 3
- **[Judge=2]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 87` — Behandelt Betrugstatbestand, aber nicht spezifisch Internetbetrug
  > 87 5. Kausalität. Für die Vermögensverfügung muss der täuschungsbedingte Irrtum kausal sein (vgl. BGHSt 24, 257 (260); 24, 386 (389); NStZ 2003, 313 (314 f.); OLG Düsseldorf NJW 1987, 3145); Mitverurs...
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 109` — Direkt relevant: Schadenselement beim Betrug detailliert erklaert
  > VI. Schaden. Vermögensschaden ist ein negativer Saldo zwischen dem Wert des Vermögens vor und nach der irrtumsbedingten Vermögensverfügung des Getäuschten (Prinzip der Gesamtsaldierung; stRspr; vgl. B...
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 176` — Direkt relevant: subjektiver Tatbestand von Betrug
  > D. Subjektiver Tatbestand. § 263 setzt Vorsatz voraus; darüber hinaus ist die Absicht rechtswidriger Bereicherung erforderlich.   I. Vorsatz. 1. Täuschungsvorsatz. Der Vorsatz (bedingter Vorsatz genüg...

#### ours-cohere — Top 3
- **[Judge=2]** `§ 263 StGB – BT. Zweijundzwanzigster Abschnitt – Rn. 193` — Behandelt Betrug allgemein, nicht spezifisch Internetbetrug
  > 193 Hat der Täter oder der begünstigte Dritte einen fälligen und einredefreien Anspruch auf den Vermögensvorteil, ist dieser nicht rechtswidrig. Eine durch Täuschung erreichte Erfüllung eines materiel...
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 176` — Definiert zentrale Betrugsmerkmale: Vorsatz, Täuschung, Schaden
  > D. Subjektiver Tatbestand. § 263 setzt Vorsatz voraus; darüber hinaus ist die Absicht rechtswidriger Bereicherung erforderlich.   I. Vorsatz. 1. Täuschungsvorsatz. Der Vorsatz (bedingter Vorsatz genüg...
- **[Judge=3]** `§ 263 StGB – BT. Zweijundzwanzigster Abschnitt – Rn. 187` — Bereicherungsabsicht bei Betrug, direkt tatbestandsrelevant
  > 2. Absicht. Es muss dem Täter darauf ankommen, sich oder einem Dritten einen Vermögensvorteil zu verschaffen. Motiv oder letzter Zweck muss dies nicht sein (BGHSt 4, 107; 16. 1; BGHR § 263 I Täusch. 9...

#### ours-mxbai — Top 3
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 14` — Direkt relevant zu Betrug, Täuschungshandlungen im Internet
  > Rspr. und hM bejahen darüber hinaus aber die Möglichkeit einer Täuschung durch Unterlassen auch ohne Erklärung gegenüber dem Irrenden (→ Rn. 38; vgl. BGHSt 39, 392 (398); BayObLG NJW 1987, 1654 (mAnm ...
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 5` — Definiert zentrale Tatbestandsmerkmale des Betrugs
  > 5 C. Grundtatbestand, Abs. 1. Tathandlung ist das Täuschen einer natürlichen Person (vgl. NStZ 2005, 213) über Tatsachen. Erfolg dieser Handlung muss ein Irrtum des Täuschungsadressaten sein; dieser m...
- **[Judge=1]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 263 (Tei` — Allgemeine Betrugsliteratur, nicht internetspezifisch behandelt
  > Heghmanns, Strafbarkeit des „Phishing“ von Bankkontendaten und ihrer Verwertung, wistra 2007, 167; Hilgendorf, Tatsachenaussagen u. Werturteile im Strafrecht, 1998; Hillenkamp, Zum Schutz „deliktische...

#### ours-mxbai-voyage — Top 3
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 5` — Definiert zentrale Tatbestandsmerkmale des Betrugs
  > 5 C. Grundtatbestand, Abs. 1. Tathandlung ist das Täuschen einer natürlichen Person (vgl. NStZ 2005, 213) über Tatsachen. Erfolg dieser Handlung muss ein Irrtum des Täuschungsadressaten sein; dieser m...
- **[Judge=3]** `§ 263 StGB – I. Vermögensbegriff  – Rn. 263` — Betrugsparagraph 263 - direkt relevant für Internetbetrug
  > 263 (1) Wer in der Absicht, sich oder einem Dritten einen rechtswidrigen Vermögensvorteil zu verschaffen, das Vermögen eines anderen dadurch beschädigt, daß er durch Vorspiegelung falscher oder durch ...
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 28` — Direkt relevant: Internetbetrug durch taeuschendes Verhalten
  > 28 Solche Scheinrechnungen sind so formuliert, dass sie bei eiligen oder geschäftsunerfahrenen Empfängern den Eindruck der Zahlungspflicht zu erzeugen geeignet sind (vgl. auch Erb ZIS 2011, 354: „Sugg...

### q10 — alltagssprache

**Query:** Wann darf die Polizei bei jemandem zu Hause suchen?

**Kontext:** Durchsuchungsvoraussetzungen, §§ 102 ff. StPO

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours | 1.00 | 100% | 100% | 3 | 6.1s |
| ours-cohere | 0.98 | 80% | 100% | 3 | 6.1s |
| ours-mxbai | 1.00 | 100% | 100% | 3 | 5.7s |
| ours-mxbai-voyage | 1.00 | 100% | 100% | 3 | 5.6s |

#### ours — Top 3
- **[Judge=3]** `§ 102 StPO – Rn. 102` — Direkt relevant: behandelt zentrale Durchsuchungsvoraussetzungen nach § 102 StPO
  > 102 Bei dem, welcher als Täter oder Teilnehmer einer Straftat oder der Datenhehlerei, Begünstigung, Strafvereitelung oder Hehlerei  Köhler    Ermittlungsmaßnahmen  verdächtig ist, kann eine Durchsuchu...
- **[Judge=3]** `§ 102 StPO – Rn. 3` — Direkt relevant: Durchsuchungsvoraussetzungen bei Wohnungen
  > **Teilnehmer** nach §§ 25 ff. StGB, nicht die sog. notwendigen Teilnehmer (zum Begriff: Fischer/Fischer StGB Vor § 25 Rn. 7), stehen den Tatverdächtigen gleich. Bei jedem v. ihnen sowie bei den der Be...
- **[Judge=3]** `§ 102 StPO – Rn. 10` — Direkt relevant: behandelt Durchsuchungsvoraussetzungen und Beweismittelfindung
  > II. Auffinden von Beweismitteln. Zu den Beweismitteln (→ § 94 Rn. 4 ff.) gehören auch die nur in § 103 erwähnten Spuren (SK-StPO/Jäger/Wohlers Rn. 21) u. Personen, die zu Beweiszwecken in Augenschein ...

#### ours-cohere — Top 3
- **[Judge=3]** `§ 102 StPO – Rn. 102` — Direkt relevant: beantwortet Durchsuchungsvoraussetzungen bei Wohnungen
  > 102 Bei dem, welcher als Täter oder Teilnehmer einer Straftat oder der Datenhehlerei, Begünstigung, Strafvereitelung oder Hehlerei  Köhler    Ermittlungsmaßnahmen  verdächtig ist, kann eine Durchsuchu...
- **[Judge=2]** `§ 102 StPO – Rn. 3` — Durchsuchungsgegenstaende und spezielle Personengruppen, aber nicht Grundvoraussetzungen
  > **Teilnehmer** nach §§ 25 ff. StGB, nicht die sog. notwendigen Teilnehmer (zum Begriff: Fischer/Fischer StGB Vor § 25 Rn. 7), stehen den Tatverdächtigen gleich. Bei jedem v. ihnen sowie bei den der Be...
- **[Judge=3]** `§ 102 StPO – Rn. 10` — Direkt relevant zu Durchsuchungsvoraussetzungen nach §§ 102 ff. StPO
  > II. Auffinden von Beweismitteln. Zu den Beweismitteln (→ § 94 Rn. 4 ff.) gehören auch die nur in § 103 erwähnten Spuren (SK-StPO/Jäger/Wohlers Rn. 21) u. Personen, die zu Beweiszwecken in Augenschein ...

#### ours-mxbai — Top 3
- **[Judge=3]** `§ 102 StPO – Rn. 102` — Direkt relevant: § 102 StPO regelt Durchsuchungsvoraussetzungen
  > 102 Bei dem, welcher als Täter oder Teilnehmer einer Straftat oder der Datenhehlerei, Begünstigung, Strafvereitelung oder Hehlerei  Köhler    Ermittlungsmaßnahmen  verdächtig ist, kann eine Durchsuchu...
- **[Judge=3]** `§ 102 StPO – Rn. 10` — Direkt relevant zu Durchsuchungsvoraussetzungen und -zwecken
  > II. Auffinden von Beweismitteln. Zu den Beweismitteln (→ § 94 Rn. 4 ff.) gehören auch die nur in § 103 erwähnten Spuren (SK-StPO/Jäger/Wohlers Rn. 21) u. Personen, die zu Beweiszwecken in Augenschein ...
- **[Judge=3]** `§ 102 StPO – Rn. 3` — Behandelt direkt Durchsuchungsvoraussetzungen nach StPO
  > **Teilnehmer** nach §§ 25 ff. StGB, nicht die sog. notwendigen Teilnehmer (zum Begriff: Fischer/Fischer StGB Vor § 25 Rn. 7), stehen den Tatverdächtigen gleich. Bei jedem v. ihnen sowie bei den der Be...

#### ours-mxbai-voyage — Top 3
- **[Judge=3]** `§ 102 StPO – Rn. 102` — Direkt relevant: beantwortet Durchsuchungsvoraussetzungen bei Verdaechtigen
  > 102 Bei dem, welcher als Täter oder Teilnehmer einer Straftat oder der Datenhehlerei, Begünstigung, Strafvereitelung oder Hehlerei  Köhler    Ermittlungsmaßnahmen  verdächtig ist, kann eine Durchsuchu...
- **[Judge=3]** `§ 102 StPO – Rn. 102` — Behandelt direkt Tatverdacht für Wohnungsdurchsuchungen nach § 102
  > Köhler     Erstes Buch. Achter Abschnitt  Gesetz gebundenen Behörden u. Gremien ist nicht angezeigt (BGH JR 2019, 404 mAnm Löffelmann). Bei anonymen Hinweisen ist wegen der erhöhten Gefahr u. des nur ...
- **[Judge=2]** `§ 102 StPO – Rn. 10` — Thematisch relevant: Durchsuchungsvoraussetzungen und Verhältnismäßigkeitsprinzip
  > II. Auffinden von Beweismitteln. Zu den Beweismitteln (→ § 94 Rn. 4 ff.) gehören auch die nur in § 103 erwähnten Spuren (SK-StPO/Jäger/Wohlers Rn. 21) u. Personen, die zu Beweiszwecken in Augenschein ...

### q11 — alltagssprache

**Query:** Was passiert wenn jemand luegt damit er Geld bekommt?

**Kontext:** Laienhafte Umschreibung des Betrugstatbestandes

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours | 1.00 | 100% | 100% | 3 | 5.1s |
| ours-cohere | 1.00 | 100% | 100% | 3 | 5.1s |
| ours-mxbai | 1.00 | 100% | 100% | 3 | 5.1s |
| ours-mxbai-voyage | 1.00 | 100% | 100% | 3 | 5.8s |

#### ours — Top 3
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 5` — Definiert direkt den Betrugstatbestand mit Täuschung
  > 5 C. Grundtatbestand, Abs. 1. Tathandlung ist das Täuschen einer natürlichen Person (vgl. NStZ 2005, 213) über Tatsachen. Erfolg dieser Handlung muss ein Irrtum des Täuschungsadressaten sein; dieser m...
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 176` — Direkt relevant: erklärt subjektive Tatbestandsmerkmale beim Betrug
  > D. Subjektiver Tatbestand. § 263 setzt Vorsatz voraus; darüber hinaus ist die Absicht rechtswidriger Bereicherung erforderlich.   I. Vorsatz. 1. Täuschungsvorsatz. Der Vorsatz (bedingter Vorsatz genüg...
- **[Judge=3]** `§ 263 StGB – I. Vermögensbegriff  – Rn. 263` — Direkt relevant: Betrugstatbestand § 263 StGB
  > 263 (1) Wer in der Absicht, sich oder einem Dritten einen rechtswidrigen Vermögensvorteil zu verschaffen, das Vermögen eines anderen dadurch beschädigt, daß er durch Vorspiegelung falscher oder durch ...

#### ours-cohere — Top 3
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 5` — Definiert direkt Betrug: Täuschen für Vermögensschaden
  > 5 C. Grundtatbestand, Abs. 1. Tathandlung ist das Täuschen einer natürlichen Person (vgl. NStZ 2005, 213) über Tatsachen. Erfolg dieser Handlung muss ein Irrtum des Täuschungsadressaten sein; dieser m...
- **[Judge=3]** `§ 263 StGB – I. Vermögensbegriff  – Rn. 263` — Direkter Betrugstatbestand - exakt passende Rechtsnorm
  > 263 (1) Wer in der Absicht, sich oder einem Dritten einen rechtswidrigen Vermögensvorteil zu verschaffen, das Vermögen eines anderen dadurch beschädigt, daß er durch Vorspiegelung falscher oder durch ...
- **[Judge=3]** `§ 263 StGB – BT. Zweitundzwanzigster Abschnitt – Rn. 69` — Behandelt direkt Betrug § 263 mit Vermögensverfügung
  > 69 Anders ist es, wenn der Verfügende seinerseits nur (gutgläubige) Hilfsperson eines bösgläubigen Dritten ist. Hier ist auf den Irrtum des Entscheidungsbefugten abzustellen: Erkennt dieser die Unrich...

#### ours-mxbai — Top 3
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 5` — Direkt relevant: Betrugstatbestand mit Täuschung und Vermögensschaden
  > 5 C. Grundtatbestand, Abs. 1. Tathandlung ist das Täuschen einer natürlichen Person (vgl. NStZ 2005, 213) über Tatsachen. Erfolg dieser Handlung muss ein Irrtum des Täuschungsadressaten sein; dieser m...
- **[Judge=3]** `§ 263 StGB – I. Vermögensbegriff  – Rn. 263` — Betrug durch Täuschung zur Vermögensbereicherung - perfekte Übereinstimmung
  > 263 (1) Wer in der Absicht, sich oder einem Dritten einen rechtswidrigen Vermögensvorteil zu verschaffen, das Vermögen eines anderen dadurch beschädigt, daß er durch Vorspiegelung falscher oder durch ...
- **[Judge=3]** `§ 263 StGB – BT. Zweitundzwanzigster Abschnitt – Rn. 69` — Behandelt direkt Betrugstatbestand und dessen zentrale Merkmale
  > 69 Anders ist es, wenn der Verfügende seinerseits nur (gutgläubige) Hilfsperson eines bösgläubigen Dritten ist. Hier ist auf den Irrtum des Entscheidungsbefugten abzustellen: Erkennt dieser die Unrich...

#### ours-mxbai-voyage — Top 3
- **[Judge=3]** `§ 263 StGB – I. Vermögensbegriff  – Rn. 263` — Definiert exakt Betrug durch Täuschung für Vermögensvorteil
  > 263 (1) Wer in der Absicht, sich oder einem Dritten einen rechtswidrigen Vermögensvorteil zu verschaffen, das Vermögen eines anderen dadurch beschädigt, daß er durch Vorspiegelung falscher oder durch ...
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 5` — Direkt relevant: Betrug durch Täuschung für Vermögensvorteil
  > 5 C. Grundtatbestand, Abs. 1. Tathandlung ist das Täuschen einer natürlichen Person (vgl. NStZ 2005, 213) über Tatsachen. Erfolg dieser Handlung muss ein Irrtum des Täuschungsadressaten sein; dieser m...
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 176` — Direkt relevant für subjektiven Betrugstatbestand
  > D. Subjektiver Tatbestand. § 263 setzt Vorsatz voraus; darüber hinaus ist die Absicht rechtswidriger Bereicherung erforderlich.   I. Vorsatz. 1. Täuschungsvorsatz. Der Vorsatz (bedingter Vorsatz genüg...

### q12 — alltagssprache

**Query:** Wann muss jemand ins Gefaengnis waehrend die Tat noch nicht bewiesen ist?

**Kontext:** Untersuchungshaft, §§ 112 ff. StPO

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours | 1.00 | 100% | 100% | 3 | 5.4s |
| ours-cohere | 1.00 | 100% | 100% | 3 | 6.0s |
| ours-mxbai | 1.00 | 100% | 100% | 3 | 5.3s |
| ours-mxbai-voyage | 0.99 | 100% | 100% | 3 | 5.4s |

#### ours — Top 3
- **[Judge=3]** `§ 112 StPO – Rn. 112` — Direkt relevant: Untersuchungshaft vor Beweis der Tat
  > 112 (1) ¹ Die Untersuchungshaft darf gegen den Beschuldigten angeordnet werden, wenn er der Tat dringend verdächtig ist und ein Haftgrund besteht. ² Sie darf nicht angeordnet werden, wenn sie zu der B...
- **[Judge=3]** `§ 112 StPO – III. Flucht (Abs – Rn. 23` — Direkt relevant: Haftgruende Flucht- und Verdunkelungsgefahr
  > Bei einer besonders hohen Straferwartung braucht daher nur geprüft zu werden, ob Umstände vorhanden sind, die die hieraus herzuleitende Fluchtgefahr ausräumen können (KG StV 1996, 383; OLG München Str...
- **[Judge=3]** `§ 112 StPO – Rn. 112` — Erklaert dringenden Tatverdacht als zentrale Haftvoraussetzung
  > Haftunfähigkeit des Beschuldigten schließt den Erlass des Haftbefehls nicht aus, sondern hindert nur seinen Vollzug (OLG Düsseldorf JZ 1984, 248; OLG Frankfurt a.M. NJW 1968, 2302; OLG Nürnberg OLGSt ...

#### ours-cohere — Top 3
- **[Judge=3]** `§ 112 StPO – Rn. 112` — Beantwortet direkt die Frage zur Untersuchungshaft
  > 112 (1) ¹ Die Untersuchungshaft darf gegen den Beschuldigten angeordnet werden, wenn er der Tat dringend verdächtig ist und ein Haftgrund besteht. ² Sie darf nicht angeordnet werden, wenn sie zu der B...
- **[Judge=3]** `§ 112 StPO – III. Flucht (Abs – Rn. 23` — Direkt relevant zu Untersuchungshaft und Haftgruenden
  > Bei einer besonders hohen Straferwartung braucht daher nur geprüft zu werden, ob Umstände vorhanden sind, die die hieraus herzuleitende Fluchtgefahr ausräumen können (KG StV 1996, 383; OLG München Str...
- **[Judge=3]** `§ 112 StPO – III. Flucht (Abs – Rn. 32 (Teil 2)` — Direkt relevant: Untersuchungshaft trotz unbewiese Tat
  > Wenn die Verdunkelungshandlungen nicht geeignet sind, die Ermittlung der Wahrheit zu erschweren, darf UHaft nicht angeordnet werden. Der Haftgrund liegt daher nicht vor, wenn der Sachverhalt schon in ...

#### ours-mxbai — Top 3
- **[Judge=3]** `§ 112 StPO – Rn. 112` — Definiert exakt Voraussetzungen der Untersuchungshaft
  > 112 (1) ¹ Die Untersuchungshaft darf gegen den Beschuldigten angeordnet werden, wenn er der Tat dringend verdächtig ist und ein Haftgrund besteht. ² Sie darf nicht angeordnet werden, wenn sie zu der B...
- **[Judge=3]** `§ 112 StPO – III. Flucht (Abs – Rn. 23` — Behandelt direkt Haftgruende fuer Untersuchungshaft vor Beweis
  > Bei einer besonders hohen Straferwartung braucht daher nur geprüft zu werden, ob Umstände vorhanden sind, die die hieraus herzuleitende Fluchtgefahr ausräumen können (KG StV 1996, 383; OLG München Str...
- **[Judge=3]** `§ 112 StPO – Rn. 112` — Direkt relevant: dringender Tatverdacht als Untersuchungshaft-Voraussetzung
  > Haftunfähigkeit des Beschuldigten schließt den Erlass des Haftbefehls nicht aus, sondern hindert nur seinen Vollzug (OLG Düsseldorf JZ 1984, 248; OLG Frankfurt a.M. NJW 1968, 2302; OLG Nürnberg OLGSt ...

#### ours-mxbai-voyage — Top 3
- **[Judge=3]** `§ 112 StPO – Rn. 112` — Direkt relevant: regelt Untersuchungshaft vor Urteil
  > 112 (1) ¹ Die Untersuchungshaft darf gegen den Beschuldigten angeordnet werden, wenn er der Tat dringend verdächtig ist und ein Haftgrund besteht. ² Sie darf nicht angeordnet werden, wenn sie zu der B...
- **[Judge=3]** `§ 112 StPO – Rn. 112` — Erklaert zentrale Voraussetzungen der Untersuchungshaft
  > Haftunfähigkeit des Beschuldigten schließt den Erlass des Haftbefehls nicht aus, sondern hindert nur seinen Vollzug (OLG Düsseldorf JZ 1984, 248; OLG Frankfurt a.M. NJW 1968, 2302; OLG Nürnberg OLGSt ...
- **[Judge=3]** `§ 112 StPO – Rn. 11 (Teil 1)` — Direkt relevant: Verhältnismäßigkeit bei Untersuchungshaft
  > 11 Abzuwägen für die Beurteilung der Verhältnismäßigkeit sind die Schwere des Eingriffs in die Lebenssphäre des Beschuldigten, wobei auch sein Gesundheitszustand zu berücksichtigen ist (BGH StraFo 201...

### q13 — stpo-prozess

**Query:** Welche Voraussetzungen hat die Untersuchungshaft wegen Fluchtgefahr?

**Kontext:** § 112 Abs. 2 Nr. 2 StPO Fluchtgefahr

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours | 1.00 | 100% | 100% | 3 | 5.7s |
| ours-cohere | 0.99 | 100% | 100% | 3 | 5.9s |
| ours-mxbai | 1.00 | 100% | 100% | 3 | 5.7s |
| ours-mxbai-voyage | 1.00 | 100% | 100% | 3 | 5.8s |

#### ours — Top 3
- **[Judge=3]** `§ 112 StPO – Rn. 112` — Direkt relevant: § 112 Abs. 2 Nr. 2 Fluchtgefahr
  > 112 (1) ¹ Die Untersuchungshaft darf gegen den Beschuldigten angeordnet werden, wenn er der Tat dringend verdächtig ist und ein Haftgrund besteht. ² Sie darf nicht angeordnet werden, wenn sie zu der B...
- **[Judge=3]** `§ 112 StPO – III. Flucht (Abs – Rn. 17 (Teil 1)` — Direkt relevant: definiert Fluchtgefahr-Voraussetzungen
  > 17 IV. Fluchtgefahr (Abs. 2 Nr. 2). Fluchtgefahr (Abs. 2 Nr. 2) besteht, wenn die Würdigung der Umstände des Falles es wahrscheinlicher macht, dass sich der Beschuldigte dem Strafverfahren entziehen, ...
- **[Judge=3]** `§ 112 StPO – III. Flucht (Abs – Rn. 22` — Direkt relevant zu Fluchtgefahr-Voraussetzungen nach § 112
  > 22 Die Fluchtgefahr darf nur aus bestimmten Tatsachen hergeleitet werden. Bloße Mutmaßungen u. Befürchtungen genügen nicht. Die Tatsachen brauchen aber nicht zur vollen Überzeugung des Gerichts festzu...

#### ours-cohere — Top 3
- **[Judge=3]** `§ 112 StPO – Rn. 112` — Direkt relevante Vorschrift zu Untersuchungshaft und Fluchtgefahr
  > 112 (1) ¹ Die Untersuchungshaft darf gegen den Beschuldigten angeordnet werden, wenn er der Tat dringend verdächtig ist und ein Haftgrund besteht. ² Sie darf nicht angeordnet werden, wenn sie zu der B...
- **[Judge=3]** `§ 112 StPO – III. Flucht (Abs – Rn. 17 (Teil 1)` — Direkt relevant: definiert Fluchtgefahr-Voraussetzungen detailliert
  > 17 IV. Fluchtgefahr (Abs. 2 Nr. 2). Fluchtgefahr (Abs. 2 Nr. 2) besteht, wenn die Würdigung der Umstände des Falles es wahrscheinlicher macht, dass sich der Beschuldigte dem Strafverfahren entziehen, ...
- **[Judge=3]** `§ 112 StPO – III. Flucht (Abs – Rn. 16` — Direkt relevant zu Fluchtgefahr nach § 112 Abs. 2 Nr. 2
  > 16 Bei Ergreifung des Beschuldigten aufgrund des nach Abs. 2 Nr. 1 erlassenen Haftbefehls entfällt der Haftgrund der Flucht. In der Regel wird die vorherige Flucht aber die Aufrechterhaltung des Haftb...

#### ours-mxbai — Top 3
- **[Judge=3]** `§ 112 StPO – Rn. 112` — Direkte Antwort zu Fluchtgefahr-Voraussetzungen nach § 112
  > 112 (1) ¹ Die Untersuchungshaft darf gegen den Beschuldigten angeordnet werden, wenn er der Tat dringend verdächtig ist und ein Haftgrund besteht. ² Sie darf nicht angeordnet werden, wenn sie zu der B...
- **[Judge=3]** `§ 112 StPO – III. Flucht (Abs – Rn. 17` — Direkt relevant: behandelt Voraussetzungen der Fluchtgefahr
  > Die Beurteilung der Fluchtgefahr erfordert die Berücksichtigung aller Umstände des Falles, insbes. der Art der dem Beschuldigten vorgeworfenen Tat, der Persönlichkeit des Beschuldigten, seiner Lebensv...
- **[Judge=3]** `§ 112 StPO – III. Flucht (Abs – Rn. 17 (Teil 1)` — Direkt relevant: definiert Fluchtgefahr nach § 112 Abs. 2 Nr. 2
  > 17 IV. Fluchtgefahr (Abs. 2 Nr. 2). Fluchtgefahr (Abs. 2 Nr. 2) besteht, wenn die Würdigung der Umstände des Falles es wahrscheinlicher macht, dass sich der Beschuldigte dem Strafverfahren entziehen, ...

#### ours-mxbai-voyage — Top 3
- **[Judge=3]** `§ 112 StPO – Rn. 112` — Enthält zentrale Norm § 112 Abs. 2 Nr. 2 StPO
  > 112 (1) ¹ Die Untersuchungshaft darf gegen den Beschuldigten angeordnet werden, wenn er der Tat dringend verdächtig ist und ein Haftgrund besteht. ² Sie darf nicht angeordnet werden, wenn sie zu der B...
- **[Judge=3]** `§ 112 StPO – III. Flucht (Abs – Rn. 17 (Teil 1)` — Direkt relevant: Definition und Voraussetzungen der Fluchtgefahr
  > 17 IV. Fluchtgefahr (Abs. 2 Nr. 2). Fluchtgefahr (Abs. 2 Nr. 2) besteht, wenn die Würdigung der Umstände des Falles es wahrscheinlicher macht, dass sich der Beschuldigte dem Strafverfahren entziehen, ...
- **[Judge=3]** `§ 112 StPO – III. Flucht (Abs – Rn. 17` — Direkt relevant: Voraussetzungen und Kriterien der Fluchtgefahr
  > Die Beurteilung der Fluchtgefahr erfordert die Berücksichtigung aller Umstände des Falles, insbes. der Art der dem Beschuldigten vorgeworfenen Tat, der Persönlichkeit des Beschuldigten, seiner Lebensv...

### q14 — stpo-prozess

**Query:** Wie lange darf die Untersuchungshaft maximal dauern?

**Kontext:** § 121 StPO Sechs-Monats-Grenze, Haftpruefung OLG

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours | 0.99 | 80% | 100% | 3 | 4.9s |
| ours-cohere | 0.97 | 100% | 100% | 3 | 5.5s |
| ours-mxbai | 0.99 | 100% | 100% | 3 | 4.4s |
| ours-mxbai-voyage | 1.00 | 100% | 100% | 3 | 6.4s |

#### ours — Top 3
- **[Judge=3]** `§ 121 StPO – Rn. 121` — Beantwortet direkt die Frage zur Maximaldauer Untersuchungshaft
  > 121 (1) Solange kein Urteil ergangen ist, das auf Freiheitsstrafe oder eine freiheitsentziehende Maßregel der Besserung und Sicherung erkennt, darf der Vollzug der Untersuchungshaft wegen derselben Ta...
- **[Judge=3]** `§ 121 StPO – Rn. 1` — Behandelt direkt maximale Dauer der Untersuchungshaft
  > Eine absolute Höchstgrenze für die Dauer v. UHaft sieht weder die StPO noch die EMRK vor (EGMR EuGRZ 1993, 384). Es kommt auf eine Abwägung aller Umstände des Einzelfalls an. Eine ein Jahr übersteigen...
- **[Judge=3]** `§ 121 StPO – Rn. 1` — Direkt relevant zu Haftdauer und 6-Monats-Grenze
  > 1 A. Beschleunigungsgebot. Einen Anspruch auf beschleunigte Aburteilung hat der in UHaft (und einstweiliger Unterbringung) befindliche Beschuldigte nach Art. 5 Abs. 3 S. 2 EMRK (→ EMRK Art. 5 Rn. 10 f...

#### ours-cohere — Top 3
- **[Judge=3]** `§ 121 StPO – Rn. 13` — Direkt zur Sechs-Monats-Grenze bei Untersuchungshaft
  > 13 Das bedeutet: Wird UHaft vollzogen, so darf sie nicht aufgrund eines weiteren Haftbefehls, der bereits bei Erlass des 1. Haftbefehls bekannt gewesene Tatvorwürfe zum Gegenstand hat, über 6 Monate h...
- **[Judge=2]** `§ 121 StPO – Rn. 8 (Teil 1)` — Behandelt Haftdauer-Beschränkungen, aber nicht maximale Zeitgrenzen
  > 8 II. Zeitliche Geltung der Beschränkungen der UHaft. Bis zu einem auf Freiheitsentziehung lautenden Urteil (Freiheitsstrafe mit o. ohne Bewährung o. freiheitsentziehende Sicherungsmaßregeln) gelten d...
- **[Judge=3]** `§ 121 StPO – Rn. 121` — Beantwortet direkt die Frage zur maximalen Haftdauer
  > 121 (1) Solange kein Urteil ergangen ist, das auf Freiheitsstrafe oder eine freiheitsentziehende Maßregel der Besserung und Sicherung erkennt, darf der Vollzug der Untersuchungshaft wegen derselben Ta...

#### ours-mxbai — Top 3
- **[Judge=3]** `§ 121 StPO – Rn. 121` — Direkt relevant: beantwortet konkret die Frage zur Haftdauer
  > 121 (1) Solange kein Urteil ergangen ist, das auf Freiheitsstrafe oder eine freiheitsentziehende Maßregel der Besserung und Sicherung erkennt, darf der Vollzug der Untersuchungshaft wegen derselben Ta...
- **[Judge=3]** `§ 121 StPO – Rn. 1` — Direkt relevant, behandelt maximale Dauer der Untersuchungshaft
  > Eine absolute Höchstgrenze für die Dauer v. UHaft sieht weder die StPO noch die EMRK vor (EGMR EuGRZ 1993, 384). Es kommt auf eine Abwägung aller Umstände des Einzelfalls an. Eine ein Jahr übersteigen...
- **[Judge=2]** `§ 121 StPO – Rn. 8 (Teil 1)` — Behandelt UHaft-Beschränkungen, aber nicht maximale Dauer
  > 8 II. Zeitliche Geltung der Beschränkungen der UHaft. Bis zu einem auf Freiheitsentziehung lautenden Urteil (Freiheitsstrafe mit o. ohne Bewährung o. freiheitsentziehende Sicherungsmaßregeln) gelten d...

#### ours-mxbai-voyage — Top 3
- **[Judge=3]** `§ 121 StPO – Rn. 121` — Direkt relevant: behandelt exakt maximale Untersuchungshaftdauer
  > 121 (1) Solange kein Urteil ergangen ist, das auf Freiheitsstrafe oder eine freiheitsentziehende Maßregel der Besserung und Sicherung erkennt, darf der Vollzug der Untersuchungshaft wegen derselben Ta...
- **[Judge=3]** `§ 121 StPO – Rn. 1` — Behandelt direkt die Sechsmonatsfrist der Untersuchungshaft
  > 1 A. Beschleunigungsgebot. Einen Anspruch auf beschleunigte Aburteilung hat der in UHaft (und einstweiliger Unterbringung) befindliche Beschuldigte nach Art. 5 Abs. 3 S. 2 EMRK (→ EMRK Art. 5 Rn. 10 f...
- **[Judge=3]** `§ 121 StPO – Rn. 1` — Behandelt direkt die Höchstdauern der Untersuchungshaft
  > Eine absolute Höchstgrenze für die Dauer v. UHaft sieht weder die StPO noch die EMRK vor (EGMR EuGRZ 1993, 384). Es kommt auf eine Abwägung aller Umstände des Einzelfalls an. Eine ein Jahr übersteigen...

### q15 — stpo-prozess

**Query:** Was regelt § 136 StPO zur Beschuldigtenvernehmung?

**Kontext:** Belehrungspflichten, Recht auf Verteidiger

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours | 0.90 | 80% | 100% | 2 | 5.4s |
| ours-cohere | 0.92 | 80% | 100% | 2 | 5.8s |
| ours-mxbai | 0.94 | 80% | 100% | 2 | 5.3s |
| ours-mxbai-voyage | 0.80 | 60% | 67% | 1 | 5.5s |

#### ours — Top 3
- **[Judge=2]** `StPO – III. Steuerstrafverfahren – Rn. 79` — Behandelt Belehrungspflichten bei verschiedenen Vernehmungsarten, nicht direkt § 136
  > 79 3. Die informatorische Befragung der Tatverdächtigen, die nach diesen Grundsätzen noch keine Beschuldigten sind, ist Zeugenvernehmung. Die Bestrebungen des Schrifttums, neben Beschuldigte u. Zeugen...
- **[Judge=2]** `§ 500 StPO – ILL. für das Strafverfahren und das Bußgeldverf` — Behandelt Beschuldigtenvernehmung, aber nicht § 136 StPO direkt
  > (4) Zeugen können zur Aufenthaltsermittlung ausgeschrieben werden.  (5) Für die internationale Fahndung nach Personen, einschließlich der Fahndung nach Personen im SIS und aufgrund eines Europäischen ...
- **[Judge=2]** `StPO – III. Steuerstrafverfahren – Rn. 25` — Nemo-tenetur-Prinzip relevant für § 136 StPO Belehrungen
  > Das nemo-tenetur-Prinzip (nemo tenetur se ipsum accusare und nemo tenetur se ipsum prodere) o. der Grundsatz der Selbstbelastungsfreiheit bedeutet, dass niemand verpflichtet ist, sich selbst anzuklage...

#### ours-cohere — Top 3
- **[Judge=2]** `StPO – III. Steuerstrafverfahren – Rn. 79` — Behandelt Belehrungspflichten nach § 136 StPO, aber indirekt
  > 79 3. Die informatorische Befragung der Tatverdächtigen, die nach diesen Grundsätzen noch keine Beschuldigten sind, ist Zeugenvernehmung. Die Bestrebungen des Schrifttums, neben Beschuldigte u. Zeugen...
- **[Judge=2]** `§ 500 StPO – ILL. für das Strafverfahren und das Bußgeldverf` — Behandelt Beschuldigtenvernehmung, aber nicht § 136 StPO direkt
  > (4) Zeugen können zur Aufenthaltsermittlung ausgeschrieben werden.  (5) Für die internationale Fahndung nach Personen, einschließlich der Fahndung nach Personen im SIS und aufgrund eines Europäischen ...
- **[Judge=3]** `§ 114b StPO – I. Abs – Rn. 5` — Direkt relevant: behandelt § 136 Belehrungspflichten und Verteidigerrechte
  > 5 II. Abs. 2 S. 1 Nr. 2–4. Hier wird die auch nach § 136 Abs. 1 S. 2, 3 und § 163a Abs. 3 S. 2, 4 vor Beginn der ersten richterlichen bzw. staatsanwaltschaftlichen o. polizeilichen Vernehmung bestehen...

#### ours-mxbai — Top 3
- **[Judge=2]** `§ 500 StPO – ILL. für das Strafverfahren und das Bußgeldverf` — Behandelt Beschuldigtenvernehmung, aber nicht § 136 StPO direkt
  > (4) Zeugen können zur Aufenthaltsermittlung ausgeschrieben werden.  (5) Für die internationale Fahndung nach Personen, einschließlich der Fahndung nach Personen im SIS und aufgrund eines Europäischen ...
- **[Judge=3]** `§ 114b StPO – I. Abs – Rn. 5` — Direkt zu § 136 StPO Belehrungspflichten und Verteidiger
  > 5 II. Abs. 2 S. 1 Nr. 2–4. Hier wird die auch nach § 136 Abs. 1 S. 2, 3 und § 163a Abs. 3 S. 2, 4 vor Beginn der ersten richterlichen bzw. staatsanwaltschaftlichen o. polizeilichen Vernehmung bestehen...
- **[Judge=2]** `StPO – III. Steuerstrafverfahren – Rn. 79` — Behandelt Belehrungspflichten bei Vernehmungen, aber nicht § 136
  > 79 3. Die informatorische Befragung der Tatverdächtigen, die nach diesen Grundsätzen noch keine Beschuldigten sind, ist Zeugenvernehmung. Die Bestrebungen des Schrifttums, neben Beschuldigte u. Zeugen...

#### ours-mxbai-voyage — Top 3
- **[Judge=1]** `§ 115 StPO – Rn. 5` — Behandelt Vorführung/Vernehmung, nicht § 136 StPO-Belehrungen
  > 5 Am Tage nach der Ergreifung darf er nur vorgeführt werden, wenn eine frühere Vorführung nicht möglich ist. Spätestens an diesem Tage muss die Vorführung aber stattfinden, auch wenn er ein Sonnabend,...
- **[Judge=2]** `§ 500 StPO – ILL. für das Strafverfahren und das Bußgeldverf` — Behandelt Beschuldigtenvernehmung, aber nicht § 136 StPO direkt
  > (4) Zeugen können zur Aufenthaltsermittlung ausgeschrieben werden.  (5) Für die internationale Fahndung nach Personen, einschließlich der Fahndung nach Personen im SIS und aufgrund eines Europäischen ...
- **[Judge=3]** `§ 114b StPO – I. Abs – Rn. 5` — Direkt relevant: behandelt § 136 StPO Belehrungspflichten
  > 5 II. Abs. 2 S. 1 Nr. 2–4. Hier wird die auch nach § 136 Abs. 1 S. 2, 3 und § 163a Abs. 3 S. 2, 4 vor Beginn der ersten richterlichen bzw. staatsanwaltschaftlichen o. polizeilichen Vernehmung bestehen...

### q16 — cross-reference

**Query:** Worin unterscheidet sich Betrug von Unterschlagung?

**Kontext:** Abgrenzung § 263 vs § 246 StGB

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours | 0.93 | 100% | 100% | 2 | 6.4s |
| ours-cohere | 0.95 | 60% | 67% | 3 | 6.0s |
| ours-mxbai | 0.96 | 40% | 67% | 3 | 6.2s |
| ours-mxbai-voyage | 1.00 | 80% | 100% | 3 | 5.8s |

#### ours — Top 3
- **[Judge=2]** `§ 263 StGB – BT. Zweitundzwanzigster Abschnitt – Rn. 69` — Behandelt Betrug, aber nicht Abgrenzung zur Unterschlagung
  > 69 Anders ist es, wenn der Verfügende seinerseits nur (gutgläubige) Hilfsperson eines bösgläubigen Dritten ist. Hier ist auf den Irrtum des Entscheidungsbefugten abzustellen: Erkennt dieser die Unrich...
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 76` — Erklärt Dreiecksbetrug und Abgrenzung zu Wegnahme/Diebstahl
  > 4. Dreiecksbetrug. Da die Getäuschte und die verfügende, nicht aber die verfügende und die geschädigte Person identisch sein müssen, ist der Tatbestand des § 263 nur erfüllt, wenn die Vermögensverfügu...
- **[Judge=3]** `§ 263 StGB – I. Vermögensbegriff  – Rn. 263` — Direkt relevant: § 263 Betrug vollständiger Gesetzestext
  > 263 (1) Wer in der Absicht, sich oder einem Dritten einen rechtswidrigen Vermögensvorteil zu verschaffen, das Vermögen eines anderen dadurch beschädigt, daß er durch Vorspiegelung falscher oder durch ...

#### ours-cohere — Top 3
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 76` — Direkt relevant: zentrale Abgrenzung Betrug vs Diebstahl/Unterschlagung
  > 4. Dreiecksbetrug. Da die Getäuschte und die verfügende, nicht aber die verfügende und die geschädigte Person identisch sein müssen, ist der Tatbestand des § 263 nur erfüllt, wenn die Vermögensverfügu...
- **[Judge=1]** `§ 263 StGB – BT. Zweitundzwanzigster Abschnitt – Rn. 69` — Behandelt nur Betrug, nicht Abgrenzung zur Unterschlagung
  > 69 Anders ist es, wenn der Verfügende seinerseits nur (gutgläubige) Hilfsperson eines bösgläubigen Dritten ist. Hier ist auf den Irrtum des Entscheidungsbefugten abzustellen: Erkennt dieser die Unrich...
- **[Judge=3]** `§ 263 StGB – I. Vermögensbegriff  – Rn. 263` — Enthält vollständigen Wortlaut des Betrugsparagraphen 263 StGB
  > 263 (1) Wer in der Absicht, sich oder einem Dritten einen rechtswidrigen Vermögensvorteil zu verschaffen, das Vermögen eines anderen dadurch beschädigt, daß er durch Vorspiegelung falscher oder durch ...

#### ours-mxbai — Top 3
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 76` — Erklärt direkt Abgrenzung Betrug zu anderen Delikten
  > 4. Dreiecksbetrug. Da die Getäuschte und die verfügende, nicht aber die verfügende und die geschädigte Person identisch sein müssen, ist der Tatbestand des § 263 nur erfüllt, wenn die Vermögensverfügu...
- **[Judge=1]** `§ 263 StGB – BT. Zweitundzwanzigster Abschnitt – Rn. 69` — Betrug-Tatbestand, aber nicht Unterschlagungsabgrenzung
  > 69 Anders ist es, wenn der Verfügende seinerseits nur (gutgläubige) Hilfsperson eines bösgläubigen Dritten ist. Hier ist auf den Irrtum des Entscheidungsbefugten abzustellen: Erkennt dieser die Unrich...
- **[Judge=3]** `§ 263 StGB – I. Vermögensbegriff  – Rn. 263` — Direkt relevant: Definition und Tatbestandsmerkmale des Betrugs
  > 263 (1) Wer in der Absicht, sich oder einem Dritten einen rechtswidrigen Vermögensvorteil zu verschaffen, das Vermögen eines anderen dadurch beschädigt, daß er durch Vorspiegelung falscher oder durch ...

#### ours-mxbai-voyage — Top 3
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 76` — Direkte Abgrenzung Betrug vs andere Vermögensdelikte
  > 4. Dreiecksbetrug. Da die Getäuschte und die verfügende, nicht aber die verfügende und die geschädigte Person identisch sein müssen, ist der Tatbestand des § 263 nur erfüllt, wenn die Vermögensverfügu...
- **[Judge=3]** `§ 263 StGB – I. Vermögensbegriff  – Rn. 263` — Definiert zentrale Tatbestandsmerkmale des Betrugs
  > 263 (1) Wer in der Absicht, sich oder einem Dritten einen rechtswidrigen Vermögensvorteil zu verschaffen, das Vermögen eines anderen dadurch beschädigt, daß er durch Vorspiegelung falscher oder durch ...
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 76` — Direkt relevant: erklärt Verfügungsbegriff beim Betrug
  > 76 3. Unmittelbarkeit der Verfügung. Neben der Freiwilligkeit ist das Merkmal der Unmittelbarkeit nach stRspr und hM das wichtigste Kriterium zur Beschränkung der § 263 unterfallenden Selbstschädigung...

### q17 — cross-reference

**Query:** Was sind die Unterschiede zwischen Diebstahl und Raub?

**Kontext:** § 242 vs § 249 StGB — Abgrenzung durch Gewalt/Drohung

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours | 1.00 | 100% | 100% | 3 | 6.9s |
| ours-cohere | 0.99 | 100% | 100% | 3 | 6.6s |
| ours-mxbai | 1.00 | 100% | 100% | 3 | 6.6s |
| ours-mxbai-voyage | 0.98 | 100% | 100% | 3 | 6.3s |

#### ours — Top 3
- **[Judge=3]** `§ 249 StGB` — Erklärt direkt Raub-Tatbestandsmerkmale und Abgrenzung zu anderen Delikten
  > NStZ 2023, 351). Danach ist § 249 gegenüber § 255 ein spezielles Delikt; in jedem Raub liegt eine räuberische Erpressung (aA die hM in der Literatur). Die Unterscheidung richtet sich nach dem äußeren ...
- **[Judge=3]** `§ 249 StGB – BT. Zwanzigster Abschnitt – Rn. 15` — Behandelt direkt subjektiven Tatbestand bei Raub vs Diebstahl
  > G. Subjektiver Tatbestand. Der Vorsatz muss entsprechend der Doppelnatur des Raubs sowohl Wegnahme (vgl. dazu → § 242 Rn. 29 ff.) als auch Nötigung (→ § 240 Rn. 53 f.) sowie deren Verknüpfung umfassen...
- **[Judge=3]** `§ 241a StGB – BT. Achtzchniter Abschnitt – Rn. 242` — Direkt relevant: Definition und Tatbestandsmerkmale von Diebstahl
  > 242 (1) Wer eine fremde bewegliche Sache einem anderen in der Absicht wegnimmt, die Sache sich oder einem Dritten rechtswidrig zuzueignen, wird mit Freiheitsstrafe bis zu fünf Jahren oder mit Geldstra...

#### ours-cohere — Top 3
- **[Judge=3]** `§ 249 StGB` — Direkt relevant: behandelt Raub vs Erpressung Abgrenzung
  > NStZ 2023, 351). Danach ist § 249 gegenüber § 255 ein spezielles Delikt; in jedem Raub liegt eine räuberische Erpressung (aA die hM in der Literatur). Die Unterscheidung richtet sich nach dem äußeren ...
- **[Judge=3]** `§ 249 StGB – BT. Zwanzigster Abschnitt – Rn. 15` — Direkte Abgrenzung Diebstahl/Raub, behandelt beide Paragraphen
  > G. Subjektiver Tatbestand. Der Vorsatz muss entsprechend der Doppelnatur des Raubs sowohl Wegnahme (vgl. dazu → § 242 Rn. 29 ff.) als auch Nötigung (→ § 240 Rn. 53 f.) sowie deren Verknüpfung umfassen...
- **[Judge=3]** `§ 241a StGB – BT. Achtzchniter Abschnitt – Rn. 242` — Direkt relevant: § 242 Diebstahl Tatbestandsmerkmale
  > 242 (1) Wer eine fremde bewegliche Sache einem anderen in der Absicht wegnimmt, die Sache sich oder einem Dritten rechtswidrig zuzueignen, wird mit Freiheitsstrafe bis zu fünf Jahren oder mit Geldstra...

#### ours-mxbai — Top 3
- **[Judge=3]** `§ 249 StGB` — Direkte Abgrenzung Raub vs räuberische Erpressung, Wegnahme-Definition
  > NStZ 2023, 351). Danach ist § 249 gegenüber § 255 ein spezielles Delikt; in jedem Raub liegt eine räuberische Erpressung (aA die hM in der Literatur). Die Unterscheidung richtet sich nach dem äußeren ...
- **[Judge=3]** `§ 249 StGB – BT. Zwanzigster Abschnitt – Rn. 15` — Direkter Vergleich Raub-Diebstahl, erklärt subjektive Abgrenzungskriterien
  > G. Subjektiver Tatbestand. Der Vorsatz muss entsprechend der Doppelnatur des Raubs sowohl Wegnahme (vgl. dazu → § 242 Rn. 29 ff.) als auch Nötigung (→ § 240 Rn. 53 f.) sowie deren Verknüpfung umfassen...
- **[Judge=3]** `§ 241a StGB – BT. Achtzchniter Abschnitt – Rn. 242` — Zeigt Tatbestandsmerkmale des Diebstahls § 242, direkt relevant
  > 242 (1) Wer eine fremde bewegliche Sache einem anderen in der Absicht wegnimmt, die Sache sich oder einem Dritten rechtswidrig zuzueignen, wird mit Freiheitsstrafe bis zu fünf Jahren oder mit Geldstra...

#### ours-mxbai-voyage — Top 3
- **[Judge=3]** `§ 249 StGB` — Direkt relevant: Abgrenzung Raub/Erpressung, Wegnahme, Nötigungsmittel
  > NStZ 2023, 351). Danach ist § 249 gegenüber § 255 ein spezielles Delikt; in jedem Raub liegt eine räuberische Erpressung (aA die hM in der Literatur). Die Unterscheidung richtet sich nach dem äußeren ...
- **[Judge=2]** `§ 252 StGB – I. Sonstige Vorschriften – Rn. 252` — Behandelt räuberischen Diebstahl, thematisch relevant für Abgrenzung
  > 252 Wer, bei einem Diebstahl auf frischer Tat betroffen, gegen eine Person Gewalt verübt oder Drohungen mit gegenwärtiger Gefahr für Leib oder Leben anwendet, um sich im Besitz des gestohlenen Gutes z...
- **[Judge=3]** `§ 249 StGB – BT. Zwanzigster Abschnitt – Rn. 6` — Direkt relevant für Abgrenzung Diebstahl/Raub durch Gewaltmerkmal
  > 6 E. Finalzusammenhang zwischen Nötigung und Wegnahme. Gewalt oder Drohung müssen das (objektive und subjektive) Mittel zur Ermöglichung der Wegnahme (in Zueignungsabsicht) sein (BGHSt 4, 210 (211); 2...

### q18 — cross-reference

**Query:** Wann wird Betrug zu Computerbetrug und umgekehrt?

**Kontext:** § 263 vs § 263a StGB — Abgrenzung bei elektronischer Datenverarbeitung

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours | 1.00 | 80% | 100% | 3 | 6.6s |
| ours-cohere | 0.91 | 40% | 33% | 3 | 6.1s |
| ours-mxbai | 0.91 | 40% | 33% | 3 | 6.2s |
| ours-mxbai-voyage | 1.00 | 100% | 100% | 3 | 6.5s |

#### ours — Top 3
- **[Judge=3]** `§ 263a StGB – M. Sonstige Vorschriften 40 – Rn. 239` — Direkt relevant: enthält § 263a Definition und Abgrenzungskriterien
  > 239 I. Sonstige Vorschriften. FAufsicht §§ 263 Abs. 5, 68 Abs. 1. Zuständigkeit in Wirtschaftsstrafaschen § 74c Abs. 1 Nr. 6, § 74e Nr. 2 GVG iVm § 103 Abs. 2 JGG. TKÜ § 100a Abs. 2 Nr. 1 Buchst. n St...
- **[Judge=3]** `§ 263a StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 18` — Direkt relevant: Abgrenzung § 263/263a bei Automaten
  > Nicht nach § 263a zu beurteilen ist die Bedienung eines Geldspielautomaten mit Falschmünzen, und zwar auch dann, wenn der Automat mit einem elektronischen Münzprüfer ausgestattet ist (OLG Celle JR 199...
- **[Judge=3]** `§ 263a StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 23` — Direkte Abgrenzung § 263 vs § 263a bei Vorsatzproblemen
  > 23 G. Subjektiver Tatbestand. Die Tat setzt (bedingten) Vorsatz voraus. Er muss sich auf alle Tatbestandsmerkmale, zu denen auch die Unbefugtheit (→ Rn. 10) gehört, dh auch auf die Voraussetzungen ers...

#### ours-cohere — Top 3
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 58` — Direkte Abgrenzung zwischen § 263 und § 263a
  > 58 Im Geschäftsverkehr wird sich, wer die Berechtigung eines Leistungsverlangens oder -auftrags nicht zu prüfen hat, hierüber idR auch keine (richtigen oder falschen) Gedanken machen (NStZ 1997, 281; ...
- **[Judge=0]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 114` — Betrifft allgemeine Schadenslehre, nicht §263/263a-Abgrenzung
  > 114 a) Quantifizierbarkeit der Vermögensminderung. Die Vermögensminderung muss quantifizierbar sein (RGSt 16, 4; 44, 249; BGHSt 16, 321). Grds. nicht ausreichend ist eine nicht quantifizierbare Einbuß...
- **[Judge=1]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 62` — Betrug allgemein, nicht Computerbetrug-Abgrenzung
  > Die Kausalität der Täuschung für den Irrtum und dessen Kausalität für die Vermögensverfügung müssen im Einzelfall festgestellt sein. Mitverursachung reicht aus. Dabei darf das Gericht auch bei Serien-...

#### ours-mxbai — Top 3
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 58` — Direkte Abgrenzung zwischen § 263 und § 263a
  > 58 Im Geschäftsverkehr wird sich, wer die Berechtigung eines Leistungsverlangens oder -auftrags nicht zu prüfen hat, hierüber idR auch keine (richtigen oder falschen) Gedanken machen (NStZ 1997, 281; ...
- **[Judge=1]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 62` — Behandelt Betrug allgemein, nicht Abgrenzung zu Computerbetrug
  > Die Kausalität der Täuschung für den Irrtum und dessen Kausalität für die Vermögensverfügung müssen im Einzelfall festgestellt sein. Mitverursachung reicht aus. Dabei darf das Gericht auch bei Serien-...
- **[Judge=0]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 114` — Behandelt Vermögensschaden bei § 263, nicht Abgrenzung zu § 263a
  > 114 a) Quantifizierbarkeit der Vermögensminderung. Die Vermögensminderung muss quantifizierbar sein (RGSt 16, 4; 44, 249; BGHSt 16, 321). Grds. nicht ausreichend ist eine nicht quantifizierbare Einbuß...

#### ours-mxbai-voyage — Top 3
- **[Judge=3]** `§ 263a StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 23` — Direkt relevant: behandelt Abgrenzung § 263/263a
  > 23 G. Subjektiver Tatbestand. Die Tat setzt (bedingten) Vorsatz voraus. Er muss sich auf alle Tatbestandsmerkmale, zu denen auch die Unbefugtheit (→ Rn. 10) gehört, dh auch auf die Voraussetzungen ers...
- **[Judge=3]** `§ 263a StGB – M. Sonstige Vorschriften 40 – Rn. 239` — Direkter Text zu § 263a, zentral für Abgrenzungsfrage
  > 239 I. Sonstige Vorschriften. FAufsicht §§ 263 Abs. 5, 68 Abs. 1. Zuständigkeit in Wirtschaftsstrafaschen § 74c Abs. 1 Nr. 6, § 74e Nr. 2 GVG iVm § 103 Abs. 2 JGG. TKÜ § 100a Abs. 2 Nr. 1 Buchst. n St...
- **[Judge=3]** `§ 263a StGB – BT. Zweijundzwanzigster Abschnitt – Rn. 7` — Direkt relevant: Abgrenzung § 263/263a bei Datenmanipulation
  > 7 II. Var. 2: Verwenden unrichtiger oder unvollständiger Daten. Die Tatvariante erfasst Fälle, in denen eingegebene Daten in einen anderen Zusammenhang gebracht oder unterdrückt werden (RegE 20; Input...