# RAG Benchmark Report

_Generiert: 2026-05-05T21:20:28_


- Queries: **18**
- Top-K: **10**
- Systeme: azure-hybrid, azure-semantic, ours-api

## Gesamtvergleich

| Metrik | azure-hybrid | azure-semantic | ours-api |
|--------|--------|--------|--------|
| nDCG@10 | 0.871 | 0.902 | 0.983 |
| Relevance@10 | 61.7% | 58.9% | 87.2% |
| Relevance@3 | 64.8% | 72.2% | 98.1% |
| Top-1-Score | 2.17 | 2.28 | 3.00 |
| Mean-Score | 1.88 | 1.84 | 2.52 |
| Latenz (s) | 1.59 | 1.61 | 9.41 |

## Nach Kategorie


### alltagssprache

| Metrik | azure-hybrid | azure-semantic | ours-api |
|--------|--------|--------|--------|
| nDCG@10 | 0.856 | 0.810 | 0.996 |
| Relevance@10 | 60.0% | 50.0% | 95.0% |
| Relevance@3 | 50.0% | 50.0% | 100.0% |

### cross-reference

| Metrik | azure-hybrid | azure-semantic | ours-api |
|--------|--------|--------|--------|
| nDCG@10 | 0.857 | 0.911 | 0.976 |
| Relevance@10 | 60.0% | 46.7% | 83.3% |
| Relevance@3 | 77.8% | 66.7% | 100.0% |

### exakte-paragraphen

| Metrik | azure-hybrid | azure-semantic | ours-api |
|--------|--------|--------|--------|
| nDCG@10 | 0.925 | 0.917 | 0.986 |
| Relevance@10 | 75.0% | 70.0% | 87.5% |
| Relevance@3 | 75.0% | 75.0% | 100.0% |

### konzept

| Metrik | azure-hybrid | azure-semantic | ours-api |
|--------|--------|--------|--------|
| nDCG@10 | 0.836 | 0.941 | 0.982 |
| Relevance@10 | 60.0% | 72.5% | 90.0% |
| Relevance@3 | 58.3% | 83.3% | 100.0% |

### stpo-prozess

| Metrik | azure-hybrid | azure-semantic | ours-api |
|--------|--------|--------|--------|
| nDCG@10 | 0.879 | 0.941 | 0.972 |
| Relevance@10 | 50.0% | 50.0% | 76.7% |
| Relevance@3 | 66.7% | 88.9% | 88.9% |

## Detail pro Query


### q01 — exakte-paragraphen

**Query:** Welche Voraussetzungen hat der gewerbsmaessige Bandenbetrug nach § 263 Abs. 5 StGB?

**Kontext:** Qualifikationstatbestand des Bandenbetrugs im Fischer-Kommentar

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours-api | 0.99 | 80% | 100% | 3 | 25.8s |
| azure-hybrid | 0.91 | 70% | 67% | 2 | 1.8s |
| azure-semantic | 0.90 | 60% | 67% | 3 | 1.8s |

#### ours-api — Top 3
- **[Judge=3]** `§ 263 StGB – I. Vermögensbegriff  – Rn. 263` — Enthält komplette Voraussetzungen des § 263 Abs. 5
  > 263 (1) Wer in der Absicht, sich oder einem Dritten einen rechtswidrigen Vermögensvorteil zu verschaffen, das Vermögen eines anderen dadurch beschädigt, daß er durch Vorspiegelung falscher oder durch ...
- **[Judge=3]** `§ 263 StGB – BT. Zweriindzwanzigster Abschnitt – Rn. 225` — Behandelt direkt § 263 Abs. 5 Voraussetzungen
  > IV. Qualifikation (Abs. 5). Abs. 5 enthält einen Qualifikationstatbestand, der die Tat in Fällen kumulativ gewerbs- und bandenmäßiger Begehung zum Verbrechen macht. Die Qualifikation ist in die Urteil...
- **[Judge=3]** `§ 263 StGB – BT. Zweijundzwanzigster Abschnitt – Rn. 213` — Direkt relevant: Qualifikationstatbestand § 263 Abs. 5
  > 213 Sind beide Varianten erfüllt, ist eine Qualifikation nach Abs. 5 gegeben. Die Abgrenzung des Abs. 3 Nr. 1 zum Verbrechen nach Abs. 5 ist in Fällen bandenmäßiger Begehung schwierig, denn eine auf f...

#### azure-hybrid — Top 3
- **[Judge=2]** `§ 263 StGB – BT. Zweijundzwanzigster Abschnitt – Rn. 201` — Behandelt Gewerbsmäßigkeit bei Betrug, aber nicht Bande
  > Ein Gefährdungsschaden kann für die Strafzumessung nicht mit dem tatsächlich eingetretenen Schaden gleichgesetzt werden (wistra 1999, 185 (187); BGHSt 53, 71 (79) = NJW 2009, 528; 1. StS; aA aber BGHS...
- **[Judge=3]** `§ 263 StGB – BT. Zweijundzwanzigster Abschnitt – Rn. 211` — Direkt zu Bandenbetrug § 263 Abs. 5 StGB
  > 211 b) Bandenmäßigkeit. Bandenmäßige Begehung ist gegeben, wenn sich eine Bande (zum Begriff vgl. → § 244 Rn. 34 ff.) zur Begehung einer Mehrzahl von selbstständigen Taten der Urkundenfälschung oder d...
- **[Judge=1]** `§ 267 StGB – BT. Dreiundzwanzigster Abschnitt – Rn. 44` — Behandelt § 267 Abs. 3, nicht § 263 Abs. 5
  > I. Rechtsfolgen; besonders schwere Fälle (Abs. 3). Abs. 1 droht für den Grundfall Freiheitsstrafe bis zu 5 Jahren oder Geldstrafe an. Der besonders schwere Fall (Abs. 3) ist durch Regelbeispiele ausge...

#### azure-semantic — Top 3
- **[Judge=3]** `§ 263 StGB – BT. Zweriindzwanzigster Abschnitt – Rn. 225` — Direkt relevant: behandelt exakt § 263 Abs. 5
  > IV. Qualifikation (Abs. 5). Abs. 5 enthält einen Qualifikationstatbestand, der die Tat in Fällen kumulativ gewerbs- und bandenmäßiger Begehung zum Verbrechen macht. Die Qualifikation ist in die Urteil...
- **[Judge=2]** `§ 263 StGB – BT. Zweijundzwanzigster Abschnitt – Rn. 213` — Behandelt Bandenbetrug, aber andere Qualifikationsmerkmale
  > 213 Sind beide Varianten erfüllt, ist eine Qualifikation nach Abs. 5 gegeben. Die Abgrenzung des Abs. 3 Nr. 1 zum Verbrechen nach Abs. 5 ist in Fällen bandenmäßiger Begehung schwierig, denn eine auf f...
- **[Judge=0]** `§ 100a StPO – G. Zufallsfunde` — StPO-Telekommunikationsueberwachung, nicht StGB § 263
  > 2. die Tat auch im Einzelfall schwer wiegt und 3. die Erforschung des Sachverhalts oder die Ermittlung des Aufenthaltsortes des Beschuldigten auf andere Weise wesentlich erschwert oder aussichtslos wä...

### q02 — exakte-paragraphen

**Query:** Was regelt § 112 StPO zur Untersuchungshaft?

**Kontext:** Anordnungsvoraussetzungen der U-Haft (dringender Tatverdacht, Haftgrund) im Schmitt/Koehler

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours-api | 1.00 | 100% | 100% | 3 | 10.9s |
| azure-hybrid | 0.91 | 60% | 67% | 3 | 1.6s |
| azure-semantic | 0.96 | 90% | 100% | 3 | 1.7s |

#### ours-api — Top 3
- **[Judge=3]** `§ 112 StPO – Rn. 112` — Direkt relevant: § 112 StPO mit vollständigen Anordnungsvoraussetzungen
  > 112 (1) ¹ Die Untersuchungshaft darf gegen den Beschuldigten angeordnet werden, wenn er der Tat dringend verdächtig ist und ein Haftgrund besteht. ² Sie darf nicht angeordnet werden, wenn sie zu der B...
- **[Judge=3]** `§ 112 StPO – Rn. 112` — Direkt relevant: erläutert Haftbefehlsvoraussetzungen § 112 StPO
  > Haftunfähigkeit des Beschuldigten schließt den Erlass des Haftbefehls nicht aus, sondern hindert nur seinen Vollzug (OLG Düsseldorf JZ 1984, 248; OLG Frankfurt a.M. NJW 1968, 2302; OLG Nürnberg OLGSt ...
- **[Judge=3]** `§ 112 StPO – III. Flucht (Abs – Rn. 23` — Behandelt direkt Haftgruende nach § 112 StPO
  > Bei einer besonders hohen Straferwartung braucht daher nur geprüft zu werden, ob Umstände vorhanden sind, die die hieraus herzuleitende Fluchtgefahr ausräumen können (KG StV 1996, 383; OLG München Str...

#### azure-hybrid — Top 3
- **[Judge=3]** `§ 112 StPO – Rn. 112` — Direkt relevant: vollständiger Gesetzestext zu § 112 StPO
  > 112 (1) ¹ Die Untersuchungshaft darf gegen den Beschuldigten angeordnet werden, wenn er der Tat dringend verdächtig ist und ein Haftgrund besteht. ² Sie darf nicht angeordnet werden, wenn sie zu der B...
- **[Judge=1]** `§ 112 StPO – Rn. 15` — Bestand des Haftbefehls, nicht Anordnungsvoraussetzungen
  > 15 G. Bestand des Haftbefehls. Wird der Haftbefehl nicht aufgeh., bleibt er grds. in Kraft; er wird nicht durch Zeitablauf wirkungslos (OLG Hamm NStZ 2016, 304).  Voraussetzungen der Untersuchungshaft...
- **[Judge=3]** `§ 112 StPO – Rn. 112` — Erklärt zentrale Voraussetzungen des § 112 StPO
  > Haftunfähigkeit des Beschuldigten schließt den Erlass des Haftbefehls nicht aus, sondern hindert nur seinen Vollzug (OLG Düsseldorf JZ 1984, 248; OLG Frankfurt a.M. NJW 1968, 2302; OLG Nürnberg OLGSt ...

#### azure-semantic — Top 3
- **[Judge=3]** `§ 112 StPO – Rn. 112` — Direkt relevant: § 112 StPO Untersuchungshaft vollständig
  > 112 (1) ¹ Die Untersuchungshaft darf gegen den Beschuldigten angeordnet werden, wenn er der Tat dringend verdächtig ist und ein Haftgrund besteht. ² Sie darf nicht angeordnet werden, wenn sie zu der B...
- **[Judge=3]** `§ 112 StPO – Rn. 112` — Direkt relevant zu § 112 StPO Haftvoraussetzungen
  > Haftunfähigkeit des Beschuldigten schließt den Erlass des Haftbefehls nicht aus, sondern hindert nur seinen Vollzug (OLG Düsseldorf JZ 1984, 248; OLG Frankfurt a.M. NJW 1968, 2302; OLG Nürnberg OLGSt ...
- **[Judge=2]** `§ 112 StPO – Rn. 10` — Behandelt U-Haft Grundsätze, aber nicht konkret § 112
  > 10 UHaft darf daher nicht angeordnet werden, wenn der Beschuldigte freiwillige Beschränkungen (Ablieferung der Personalpapiere, freiwilliges Sich-Unterziehen einer Anstaltbehandlung; vgl. auch § 71 Ab...

### q03 — exakte-paragraphen

**Query:** Welche Haftgruende nennt § 112 Abs. 2 StPO?

**Kontext:** Fluchtgefahr, Verdunkelungsgefahr, Flucht — im StPO-Kommentar

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours-api | 0.98 | 100% | 100% | 3 | 6.3s |
| azure-hybrid | 0.89 | 80% | 67% | 2 | 1.7s |
| azure-semantic | 0.82 | 40% | 33% | 1 | 1.7s |

#### ours-api — Top 3
- **[Judge=3]** `§ 112 StPO – Rn. 112` — Listet alle Haftgruende des § 112 Abs. 2 StPO
  > 112 (1) ¹ Die Untersuchungshaft darf gegen den Beschuldigten angeordnet werden, wenn er der Tat dringend verdächtig ist und ein Haftgrund besteht. ² Sie darf nicht angeordnet werden, wenn sie zu der B...
- **[Judge=3]** `§ 112 StPO – III. Flucht (Abs – Rn. 23` — Behandelt direkt Haftgruende Flucht- und Verdunkelungsgefahr
  > Bei einer besonders hohen Straferwartung braucht daher nur geprüft zu werden, ob Umstände vorhanden sind, die die hieraus herzuleitende Fluchtgefahr ausräumen können (KG StV 1996, 383; OLG München Str...
- **[Judge=3]** `§ 112 StPO – III. Flucht (Abs – Rn. 17 (Teil 1)` — Behandelt direkt Fluchtgefahr nach § 112 Abs. 2 Nr. 2
  > 17 IV. Fluchtgefahr (Abs. 2 Nr. 2). Fluchtgefahr (Abs. 2 Nr. 2) besteht, wenn die Würdigung der Umstände des Falles es wahrscheinlicher macht, dass sich der Beschuldigte dem Strafverfahren entziehen, ...

#### azure-hybrid — Top 3
- **[Judge=2]** `§ 114 StPO – A. Erlass des Haftbefehls (Abs – Rn. 9` — Behandelt Haftgründe allgemein, nicht spezifisch § 112 Abs. 2
  > IV. Haftgrund (Nr. 3, 4). Der Haftgrund (Nr. 3, 4) als die prozessuale Grdl. des Haftbefehls ist ebenfalls zu bezeichnen. Dabei genügt die Kurzbezeichnung (Fluchtgefahr, Verdunkelungsgefahr, Wiederhol...
- **[Judge=3]** `§ 112 StPO – Rn. 112` — Nennt direkt alle Haftgruende des § 112 Abs. 2 StPO
  > 112 (1) ¹ Die Untersuchungshaft darf gegen den Beschuldigten angeordnet werden, wenn er der Tat dringend verdächtig ist und ein Haftgrund besteht. ² Sie darf nicht angeordnet werden, wenn sie zu der B...
- **[Judge=1]** `§ 112 StPO – Rn. 112` — Behandelt Haftvoraussetzungen allgemein, nicht spezifische Haftgruende
  > Haftunfähigkeit des Beschuldigten schließt den Erlass des Haftbefehls nicht aus, sondern hindert nur seinen Vollzug (OLG Düsseldorf JZ 1984, 248; OLG Frankfurt a.M. NJW 1968, 2302; OLG Nürnberg OLGSt ...

#### azure-semantic — Top 3
- **[Judge=1]** `§ 112 StPO – Rn. 112` — Behandelt Haftvoraussetzungen, nicht konkrete Haftgruende § 112 Abs. 2
  > Haftunfähigkeit des Beschuldigten schließt den Erlass des Haftbefehls nicht aus, sondern hindert nur seinen Vollzug (OLG Düsseldorf JZ 1984, 248; OLG Frankfurt a.M. NJW 1968, 2302; OLG Nürnberg OLGSt ...
- **[Judge=3]** `§ 112 StPO – Rn. 112` — Vollständige Auflistung aller Haftgründe des § 112 Abs. 2 StPO
  > 112 (1) ¹ Die Untersuchungshaft darf gegen den Beschuldigten angeordnet werden, wenn er der Tat dringend verdächtig ist und ein Haftgrund besteht. ² Sie darf nicht angeordnet werden, wenn sie zu der B...
- **[Judge=1]** `§ 112 StPO – Rn. 10` — Behandelt Untersuchungshaft, aber nicht die spezifischen Haftgründe
  > 10 UHaft darf daher nicht angeordnet werden, wenn der Beschuldigte freiwillige Beschränkungen (Ablieferung der Personalpapiere, freiwilliges Sich-Unterziehen einer Anstaltbehandlung; vgl. auch § 71 Ab...

### q04 — exakte-paragraphen

**Query:** Was regelt § 102 StPO zur Durchsuchung beim Beschuldigten?

**Kontext:** Durchsuchungsvoraussetzungen beim Verdaechtigen

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours-api | 0.97 | 70% | 100% | 3 | 8.1s |
| azure-hybrid | 0.99 | 90% | 100% | 3 | 1.3s |
| azure-semantic | 0.99 | 90% | 100% | 3 | 1.4s |

#### ours-api — Top 3
- **[Judge=3]** `§ 102 StPO – Rn. 102` — Direkte Regelung des § 102 StPO zur Beschuldigtendurchsuchung
  > 102 Bei dem, welcher als Täter oder Teilnehmer einer Straftat oder der Datenhehlerei, Begünstigung, Strafvereitelung oder Hehlerei  Köhler    Ermittlungsmaßnahmen  verdächtig ist, kann eine Durchsuchu...
- **[Judge=2]** `§ 102 StPO – Rn. 10` — Thematisch relevant, behandelt allgemeine Durchsuchungsvoraussetzungen
  > II. Auffinden von Beweismitteln. Zu den Beweismitteln (→ § 94 Rn. 4 ff.) gehören auch die nur in § 103 erwähnten Spuren (SK-StPO/Jäger/Wohlers Rn. 21) u. Personen, die zu Beweiszwecken in Augenschein ...
- **[Judge=3]** `§ 102 StPO – Rn. 3` — Behandelt direkt § 102 StPO Durchsuchung bei Verdächtigen
  > 3 C. Verdächtige. Der Verdächtige muss die Durchsuchung dulden. Er braucht noch nicht Beschuldigter (→ Einl. Rn. 76 ff.) zu sein; der Tatverdacht gegen ihn muss bei der Anordnung der Maßnahme nicht ei...

#### azure-hybrid — Top 3
- **[Judge=3]** `§ 102 StPO – Rn. 10` — Direkt zu § 102 StPO Durchsuchung beim Beschuldigten
  > 10 III. Sachen. Sachen sind Kleidungsstücke, die der Verdächtige bei sich führt, ohne sie zu tragen, u. seine sonstige bewegliche Habe, gleichgültig, ob sie sich in seinem Umkreis, zB in Gepäckstücken...
- **[Judge=3]** `§ 102 StPO – Rn. 102` — Direkt relevant: vollständiger Wortlaut § 102 StPO
  > 102 Bei dem, welcher als Täter oder Teilnehmer einer Straftat oder der Datenhehlerei, Begünstigung, Strafvereitelung oder Hehlerei  Köhler    Ermittlungsmaßnahmen  verdächtig ist, kann eine Durchsuchu...
- **[Judge=2]** `§ 102 StPO – Rn. 10` — Thematisch relevant: Durchsuchungskontext, aber nicht § 102 spezifisch
  > II. Auffinden von Beweismitteln. Zu den Beweismitteln (→ § 94 Rn. 4 ff.) gehören auch die nur in § 103 erwähnten Spuren (SK-StPO/Jäger/Wohlers Rn. 21) u. Personen, die zu Beweiszwecken in Augenschein ...

#### azure-semantic — Top 3
- **[Judge=3]** `§ 102 StPO – Rn. 3` — Direkt relevant: behandelt § 102 StPO Durchsuchungsvoraussetzungen
  > 3 C. Verdächtige. Der Verdächtige muss die Durchsuchung dulden. Er braucht noch nicht Beschuldigter (→ Einl. Rn. 76 ff.) zu sein; der Tatverdacht gegen ihn muss bei der Anordnung der Maßnahme nicht ei...
- **[Judge=3]** `§ 102 StPO – Rn. 102` — Direkt § 102 StPO mit vollständigem Wortlaut
  > 102 Bei dem, welcher als Täter oder Teilnehmer einer Straftat oder der Datenhehlerei, Begünstigung, Strafvereitelung oder Hehlerei  Köhler    Ermittlungsmaßnahmen  verdächtig ist, kann eine Durchsuchu...
- **[Judge=2]** `§ 102 StPO – Rn. 10` — Behandelt Durchsuchungsvoraussetzungen, aber nicht spezifisch § 102
  > II. Auffinden von Beweismitteln. Zu den Beweismitteln (→ § 94 Rn. 4 ff.) gehören auch die nur in § 103 erwähnten Spuren (SK-StPO/Jäger/Wohlers Rn. 21) u. Personen, die zu Beweiszwecken in Augenschein ...

### q05 — konzept

**Query:** Wann liegt eine konkludente Taeuschung im Sinne des § 263 StGB vor?

**Kontext:** Taeuschungshandlung durch schluessiges Verhalten

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours-api | 0.97 | 90% | 100% | 3 | 5.8s |
| azure-hybrid | 0.99 | 90% | 100% | 3 | 1.7s |
| azure-semantic | 1.00 | 90% | 100% | 3 | 1.8s |

#### ours-api — Top 3
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 21` — Beantwortet direkt konkludente Taeuschung bei § 263 StGB
  > 21 2. Konkludente Erklärungen. Auch durch eine schlüssige Handlung (konkludente Erklärung) kann vorspiegelt werden. Eine solche konkludente Erklärung durch aktives Tun ist von einer Erklärung durch Un...
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 14` — Direkt relevant: konkludente Täuschung bei § 263 StGB
  > Rspr. und hM bejahen darüber hinaus aber die Möglichkeit einer Täuschung durch Unterlassen auch ohne Erklärung gegenüber dem Irrenden (→ Rn. 38; vgl. BGHSt 39, 392 (398); BayObLG NJW 1987, 1654 (mAnm ...
- **[Judge=2]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 38` — Behandelt Täuschung durch Unterlassen, nicht konkludente Täuschung
  > 38 4. Täuschung durch Unterlassen. Eine Täuschung kann nach hM (aA Grünwald FS H. Mayer, 1966, 281; Kargl ZStW 119 (2007), 250 (287) mwN) auch durch Unterlassen begangen werden, wenn eine Garantenpfli...

#### azure-hybrid — Top 3
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 33` — Direkt relevante Definition und Beispiele konkludenter Täuschung
  > 33 f) Vorspiegelung von Zahlungsbereitschaft. Die schlüssige Erklärung, bei Fälligkeit einer Forderung zahlen zu können und zu wollen, ist der häufigste Fall konkludenter Täuschung (vgl. zB BGHSt 15, ...
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 21` — Direkt relevante Definition konkludenter Taeuschung § 263
  > 21 2. Konkludente Erklärungen. Auch durch eine schlüssige Handlung (konkludente Erklärung) kann vorspiegelt werden. Eine solche konkludente Erklärung durch aktives Tun ist von einer Erklärung durch Un...
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 22` — Direkt zur konkludenten Taeuschung bei § 263
  > 22 Sowohl ausdrücklichen Erklärungen als auch tatsächlichen Handeln kann ein konkludenter Erklärungswert zukommen. Aus der bloßen Feststellung eines Irrtums kann aber nicht schon auf eine (konkludente...

#### azure-semantic — Top 3
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 27` — Direkt relevant: konkrete Beispiele konkludenter Taeuschung
  > 27 b) Geltendmachen von Forderungen. Das Einfordern einer Leistung, auf die kein Anspruch besteht, ist eine Täuschung iSv § 263, wenn nicht allein eine Rechtsbehauptung aufgestellt, sondern ein Bezug ...
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 14` — Definiert konkludente Täuschung bei § 263 direkt
  > Fischer/Lutz     BT. Zweiundzwanzigster Abschnitt.  Sinn verwendeten Wortbedeutungen (Arzt FS Hirsch, 1999, 446). Hier liegt idR entweder ein konkludentes Miterklären unwahrer oder ein Entstellen wahr...
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 21` — Direkt relevant - definiert konkludente Taeuschung bei 263
  > 21 2. Konkludente Erklärungen. Auch durch eine schlüssige Handlung (konkludente Erklärung) kann vorspiegelt werden. Eine solche konkludente Erklärung durch aktives Tun ist von einer Erklärung durch Un...

### q06 — konzept

**Query:** Was ist eine Vermoegensverfuegung und welche Anforderungen stellt die Rechtsprechung?

**Kontext:** Tatbestandsmerkmal der Vermoegensverfuegung beim Betrug

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours-api | 0.98 | 90% | 100% | 3 | 7.2s |
| azure-hybrid | 0.48 | 10% | 0% | 0 | 1.6s |
| azure-semantic | 0.93 | 70% | 100% | 2 | 1.6s |

#### ours-api — Top 3
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 76` — Direkt relevant: Definition und Anforderungen der Vermögensverfügung
  > 76 3. Unmittelbarkeit der Verfügung. Neben der Freiwilligkeit ist das Merkmal der Unmittelbarkeit nach stRspr und hM das wichtigste Kriterium zur Beschränkung der § 263 unterfallenden Selbstschädigung...
- **[Judge=3]** `§ 263 StGB – BT. Zweitundzwanzigster Abschnitt – Rn. 69` — Definiert Vermoegensverfuegung und erklaert Anforderungen detailliert
  > 69 Anders ist es, wenn der Verfügende seinerseits nur (gutgläubige) Hilfsperson eines bösgläubigen Dritten ist. Hier ist auf den Irrtum des Entscheidungsbefugten abzustellen: Erkennt dieser die Unrich...
- **[Judge=2]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 87` — Behandelt Betrug-Kausalität, nicht Definition der Vermögensverfügung
  > 87 5. Kausalität. Für die Vermögensverfügung muss der täuschungsbedingte Irrtum kausal sein (vgl. BGHSt 24, 257 (260); 24, 386 (389); NStZ 2003, 313 (314 f.); OLG Düsseldorf NJW 1987, 3145); Mitverurs...

#### azure-hybrid — Top 3
- **[Judge=0]** `§ 206 StGB – BT. Sechzehnter Abschnitt – Rn. 67` — Behandelt Patientenverfügungen, nicht strafrechtliche Vermögensverfügung
  > 67 An die Feststellung des tatsächlichen oder mutmaßlichen Willens der betroffenen Person (vgl. auch → § 223 Rn. 15) sind nach stRspr „strenge Anforderungen“ zu stellen (vgl. schon BGHSt 40, 257 (256 ...
- **[Judge=0]** `§ 206 StGB – BT. Sechzehnter Abschnitt – Rn. 43` — Behandelt Patientenverfügungen, nicht Vermögensverfügung beim Betrug
  > Eine Reichweitenbegrenzung (zB auf „irreversible tödliche Erkrankungen“; vgl. Enquete-Kommission (→ Rn. 73) 38 ff.) hat der 66. DJT mit großer Mehrheit zu Recht abgelehnt (Tagungsbericht Kaspar JZ 200...
- **[Judge=1]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 87` — Vermoegensbegriff relevant, aber nicht Vermoegensverfuegung
  > Vorherrschend ist heute auf der Basis eines „wirtschaftlichen“ Ansatzes (der kein „faktischer“, sondern wie jeder Vermögensbegriff ein normativer ist) ein sog. ökonomisch-juristischer Vermögensbegriff...

#### azure-semantic — Top 3
- **[Judge=2]** `§ 253 StGB – BT. Zwanzigster Abschnitt – Rn. 14` — Erpressung-Kontext, aber gleiche Verfügungsdefinition wie Betrug
  > 14 I. Vermögensverfügung. Nach zutreffender Ansicht der Lit. muss das Verhalten des Genötigten eine Vermögensverfügung sein, das heißt eine willentliche Übertragung der faktischen Herrschaft über eine...
- **[Judge=3]** `§ 263 StGB – BT. Zweitundzwanzigster Abschnitt – Rn. 69` — Definiert Vermoegensverfuegung beim Betrug direkt
  > 69 Anders ist es, wenn der Verfügende seinerseits nur (gutgläubige) Hilfsperson eines bösgläubigen Dritten ist. Hier ist auf den Irrtum des Entscheidungsbefugten abzustellen: Erkennt dieser die Unrich...
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 74` — Definiert Vermoegensverfuegung und Rechtsprechungsanforderungen direkt
  > 74 2. Verfügungsbewusstsein. Vermögensverfügungen sind nach hM grundsätzlich sowohl als bewusst als auch als unbewusst vermögensmindernde Handlungen möglich; eine aktuelle Vorstellung des Verfügenden ...

### q07 — konzept

**Query:** Was versteht man unter einem Gefaehrdungsschaden beim Betrug?

**Kontext:** Schadensbegriff, schadensgleiche Vermoegensgefaehrdung

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours-api | 0.98 | 100% | 100% | 3 | 6.6s |
| azure-hybrid | 0.92 | 80% | 67% | 3 | 1.8s |
| azure-semantic | 0.95 | 100% | 100% | 2 | 1.6s |

#### ours-api — Top 3
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 159` — Definiert direkt Gefährdungsschaden beim Betrug
  > 159 b) Voraussetzungen. aa) Ein Gefährdungsschaden ist gegeben, wenn die Wahrscheinlichkeit des endgültigen Verlusts eines Vermögensbestandteils zum Zeitpunkt der täuschungsbedingten Verfügung so groß...
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 109` — Direkt relevant: behandelt explizit Gefährdungsschaden beim Betrug
  > VI. Schaden. Vermögensschaden ist ein negativer Saldo zwischen dem Wert des Vermögens vor und nach der irrtumsbedingten Vermögensverfügung des Getäuschten (Prinzip der Gesamtsaldierung; stRspr; vgl. B...
- **[Judge=2]** `§ 263 StGB – I. Vermögensbegriff  – Rn. 263` — Betrug-Grundnorm, aber kein spezifischer Gefaehrdungsschaden-Bezug
  > 263 (1) Wer in der Absicht, sich oder einem Dritten einen rechtswidrigen Vermögensvorteil zu verschaffen, das Vermögen eines anderen dadurch beschädigt, daß er durch Vorspiegelung falscher oder durch ...

#### azure-hybrid — Top 3
- **[Judge=3]** `§ 263 StGB – BT. Zwei undzwanzigster Abschnitt – Rn. 263 (Te` — Direkt relevant zu Gefährdungsschaden beim Betrug
  > Weber, Rücktritt vom vermögensgefährdenden Betrug, FS Tiedemann, 2008, 637; Wolf, Der Betrugsschaden beim Erwerb von Dieselfahrzeugen mit illegalen Abschalteinrichtungen, NStZ 2023, 263; Zebisch/Kubik...
- **[Judge=2]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 124` — Anlagebetrug-Kontext, aber nicht spezifisch Gefährdungsschaden
  > 124 ee) Beim Anlagebetrug liegt ein Schaden insbes. vor bei Wertlosigkeit oder Minderwertigkeit der Anlage....
- **[Judge=0]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 121 (Tei` — Behandelt konkreten Schadensbegriff, nicht Gefaehrdungsschaden
  > 121 bb) Beim Gattungskauf liegt ein Schaden insbes. bei Lieferung eines minderwertigen aliud vor (zB NJW 1995, 2933 (Wein; abl. Samson StV 1996, 93); BGHSt 12, 347 (Butter); BGHSt 36, 373 (Milchpulver...

#### azure-semantic — Top 3
- **[Judge=2]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 128` — Behandelt Schadensbegriff, aber nicht spezifisch Gefaehrdungsschaden
  > 128 (4) BGHSt 51, 10 = NJW 2006, 1679 hat diese Grundsätze auf Fälle des Anlagebetrugs übertragen. Hier liegt ein Schaden vor, soweit die Zins- und Gewinnerwartungen des über das Risiko Getäuschten hi...
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 164` — Direkt relevant: definiert konkret Gefährdungsschaden beim Betrug
  > 164 Es lassen sich im Übrigen Fallgruppen wie folgt unterscheiden:  aa) Der Abschluss eines unter Vorspiegelung von Leistungsfähigkeit und/oder Leistungswilligkeit erschlichenen Kaufvertrags kann eine...
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 159` — Definiert direkt den Gefaehrdungsschaden beim Betrug
  > 159 b) Voraussetzungen. aa) Ein Gefährdungsschaden ist gegeben, wenn die Wahrscheinlichkeit des endgültigen Verlusts eines Vermögensbestandteils zum Zeitpunkt der täuschungsbedingten Verfügung so groß...

### q08 — konzept

**Query:** Wie wird der Vorsatz beim Betrug bestimmt, insbesondere die Bereicherungsabsicht?

**Kontext:** Subjektiver Tatbestand § 263 StGB

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours-api | 1.00 | 80% | 100% | 3 | 7.1s |
| azure-hybrid | 0.95 | 60% | 67% | 3 | 1.4s |
| azure-semantic | 0.89 | 30% | 33% | 3 | 1.6s |

#### ours-api — Top 3
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 176` — Direkt relevant: behandelt Vorsatz und Bereicherungsabsicht § 263
  > D. Subjektiver Tatbestand. § 263 setzt Vorsatz voraus; darüber hinaus ist die Absicht rechtswidriger Bereicherung erforderlich.   I. Vorsatz. 1. Täuschungsvorsatz. Der Vorsatz (bedingter Vorsatz genüg...
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 186` — Direkt relevant zu Bereicherungsabsicht bei Betrug
  > 186 II. Bereicherungsabsicht. Die Tat muss subjektiv auf die Erlangung eines rechtswidrigen Vermögensvorteils für den Täuschenden oder einen Dritten gerichtet sein. Vermögensvorteil ist die Erhöhung d...
- **[Judge=3]** `§ 263 StGB – BT. Zweijundzwanzigster Abschnitt – Rn. 194` — Direkt relevant zu Vorsatz bei Bereicherungsabsicht
  > 194 4. Vorsatz hinsichtlich der Rechtswidrigkeit. Die Rechtswidrigkeit des angestrebten Vermögensvorteils muss vom Vorsatz umfasst sein; sie ist wie bei § 253 (vgl. dort 20) subjektives Tatbestandsmer...

#### azure-hybrid — Top 3
- **[Judge=3]** `§ 263 StGB – I. Sonstige Vorschriften 239 – Rn. 263 (Teil 1)` — Direkt relevant: behandelt Bereicherungsabsicht bei § 263
  > 3. Einzelne Fallgruppen ... 92 4. Rechtlich missbilligte, sittenwidrige und gesetzeswidrige wirtschaftliche Werte ... 101 VI. Schaden ... 110 1. Grundsätze der Schadensermittlung ... 111 2. Vermögensm...
- **[Judge=3]** `§ 263 StGB – BT. Zweijundzwanzigster Abschnitt – Rn. 194` — Direkt relevant zu Vorsatz bei Bereicherungsabsicht
  > 194 4. Vorsatz hinsichtlich der Rechtswidrigkeit. Die Rechtswidrigkeit des angestrebten Vermögensvorteils muss vom Vorsatz umfasst sein; sie ist wie bei § 253 (vgl. dort 20) subjektives Tatbestandsmer...
- **[Judge=1]** `§ 271 StGB – BT. Dreiundzwanzigster Abschnitt – Rn. 14` — Behandelt § 271, nicht § 263 Betrug
  > E. Subjektiver Tatbestand. § 271 setzt Vorsatz hinsichtlich der Unrichtigkeit der zu beurkundenden (Abs. 1) oder beurkundeten (Abs. 2) Tatsache und der anderen Tatbestandsmerkmale voraus; bedingter Vo...

#### azure-semantic — Top 3
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 176` — Direkt relevant: Vorsatz beim Betrug detailliert erklaert
  > D. Subjektiver Tatbestand. § 263 setzt Vorsatz voraus; darüber hinaus ist die Absicht rechtswidriger Bereicherung erforderlich.   I. Vorsatz. 1. Täuschungsvorsatz. Der Vorsatz (bedingter Vorsatz genüg...
- **[Judge=1]** `§ 271 StGB – BT. Dreiundzwanzigster Abschnitt – Rn. 14` — § 271 StGB, nicht § 263 Betrug
  > E. Subjektiver Tatbestand. § 271 setzt Vorsatz hinsichtlich der Unrichtigkeit der zu beurkundenden (Abs. 1) oder beurkundeten (Abs. 2) Tatsache und der anderen Tatbestandsmerkmale voraus; bedingter Vo...
- **[Judge=1]** `§ 259 StGB – BT. Einundzwanzigster Abschnitt – Rn. 18` — Behandelt Hehlerei statt Betrug, andere Bereicherungsabsicht
  > Erfährt der Täter erst nach Erlangung des Gewahrsams von der Herkunft der Sache aus der Vortat, so kommt Hehlerei in Betracht, wenn der Täter den Gewahrsam zunächst zwar zu eigener Verfügungsgewalt, a...

### q09 — alltagssprache

**Query:** Hat der Angeklagte die Kunden über das Internet betrogen?

**Kontext:** Abstrakte Frage zu Internetbetrug, sucht Taeuschungshandlung + Schaden

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours-api | 0.98 | 100% | 100% | 3 | 6.9s |
| azure-hybrid | 0.96 | 70% | 67% | 3 | 1.3s |
| azure-semantic | 0.71 | 50% | 0% | 1 | 1.3s |

#### ours-api — Top 3
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 5` — Definiert zentrale Tatbestandsmerkmale des Betrugs
  > 5 C. Grundtatbestand, Abs. 1. Tathandlung ist das Täuschen einer natürlichen Person (vgl. NStZ 2005, 213) über Tatsachen. Erfolg dieser Handlung muss ein Irrtum des Täuschungsadressaten sein; dieser m...
- **[Judge=3]** `§ 263 StGB – I. Vermögensbegriff  – Rn. 263` — Zentrale Betrugsnorm mit allen relevanten Tatbestandsmerkmalen
  > 263 (1) Wer in der Absicht, sich oder einem Dritten einen rechtswidrigen Vermögensvorteil zu verschaffen, das Vermögen eines anderen dadurch beschädigt, daß er durch Vorspiegelung falscher oder durch ...
- **[Judge=2]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 176` — Subjektiver Tatbestand bei Betrug, aber nicht internetspezifisch
  > D. Subjektiver Tatbestand. § 263 setzt Vorsatz voraus; darüber hinaus ist die Absicht rechtswidriger Bereicherung erforderlich.   I. Vorsatz. 1. Täuschungsvorsatz. Der Vorsatz (bedingter Vorsatz genüg...

#### azure-hybrid — Top 3
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 28` — Direkt relevant: Internetbetrug, Täuschungshandlung über Scheinrechnungen
  > 28 Solche Scheinrechnungen sind so formuliert, dass sie bei eiligen oder geschäftsunerfahrenen Empfängern den Eindruck der Zahlungspflicht zu erzeugen geeignet sind (vgl. auch Erb ZIS 2011, 354: „Sugg...
- **[Judge=3]** `§ 269 StGB – BT. Dreiundzwanzigster Abschnitt – Rn. 5` — Direkt relevant: Internetbetrug und Täuschungshandlungen
  > Ob falsche Absender-Angaben in E-Mails mit rechtlich erheblichem Inhalt dem Tatbestand unterfallen (so im Grds. Buggisch NJW 2004, 3519 (3521 f.); Heghmanns wistra 2007, 167; Goeckenjan wistra 2008, 1...
- **[Judge=1]** `§ 263 StGB – BT. Zweijundzwanzigster Abschnitt – Rn. 109` — Behandelt Betrug allgemein, nicht spezifisch Internetbetrug
  > 109 Dass nach Geschäften zwischen BtM-Händlern der Käufer berechtigt sein soll, sich sein „gutes Geld“ durch Täuschung oder Drohung (§ 253) wieder zu beschaffen, wenn er betrogen wurde (NStZ 2003, 151...

#### azure-semantic — Top 3
- **[Judge=1]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 263 (Tei` — Literaturverzeichnis zu Betrug, keine konkreten Tatbestandsmerkmale
  > Fischer/Lutz      BT. Zweiundzwanzigster Abschnitt. Fehlvorstellung beim Betrug, GA 2012, 354; Cornelius, Betrug durch verschleierte Kick-Back-Zahlungen bei Immobilienfinanzierungen?, NZWiSt 2012, 259...
- **[Judge=1]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 104` — Behandelt Betrug allgemein, nicht spezifisch Internetbetrug
  > 104 aa) Der Einsatz illegal oder sittenwidrig erworbener Gegenstände (einschließlich Geld) ist nach Rspr. und hM durch § 263 geschützt, wenn diese  Fischer/Lutz    Betrug und Untreue  Gegenstände eine...
- **[Judge=0]** `§ 247 StPO – G. Unterrichtung des Angeklagten (S – Rn. 12` — Verfahrensrecht Ausschluss Angeklagter, nicht Internetbetrug
  > F. Gerichtsbeschluss. Durch Gerichtsbeschluss, nicht durch Vfg. des Vorsitzenden allein, wird der vorübergehende Ausschluss des Angeklagten angeordnet (BGHSt 1, 346 (350); 15, 194 (196); 22, 18 (20); ...

### q10 — alltagssprache

**Query:** Wann darf die Polizei bei jemandem zu Hause suchen?

**Kontext:** Durchsuchungsvoraussetzungen, §§ 102 ff. StPO

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours-api | 1.00 | 80% | 100% | 3 | 8.7s |
| azure-hybrid | 0.94 | 70% | 67% | 3 | 1.5s |
| azure-semantic | 0.80 | 60% | 67% | 2 | 1.6s |

#### ours-api — Top 3
- **[Judge=3]** `§ 102 StPO – Rn. 102` — Direkt relevant: § 102 StPO Durchsuchungsvoraussetzungen
  > 102 Bei dem, welcher als Täter oder Teilnehmer einer Straftat oder der Datenhehlerei, Begünstigung, Strafvereitelung oder Hehlerei  Köhler    Ermittlungsmaßnahmen  verdächtig ist, kann eine Durchsuchu...
- **[Judge=3]** `§ 102 StPO – Rn. 10` — Direkt relevant: Durchsuchungsvoraussetzungen und Verhältnismäßigkeitsgrundsatz
  > II. Auffinden von Beweismitteln. Zu den Beweismitteln (→ § 94 Rn. 4 ff.) gehören auch die nur in § 103 erwähnten Spuren (SK-StPO/Jäger/Wohlers Rn. 21) u. Personen, die zu Beweiszwecken in Augenschein ...
- **[Judge=2]** `§ 102 StPO – Rn. 3` — Behandelt Durchsuchungsvoraussetzungen bei besonderen Personengruppen
  > **Teilnehmer** nach §§ 25 ff. StGB, nicht die sog. notwendigen Teilnehmer (zum Begriff: Fischer/Fischer StGB Vor § 25 Rn. 7), stehen den Tatverdächtigen gleich. Bei jedem v. ihnen sowie bei den der Be...

#### azure-hybrid — Top 3
- **[Judge=3]** `§ 104 StPO – Rn. 104` — Zentrale Durchsuchungsvoraussetzungen, direkt zur Frage relevant
  > 104 (1) Zur Nachtzeit dürfen die Wohnung, die Geschäftsräume und das befriedete Besitztum nur in folgenden Fällen durchsucht werden:  1. bei Verfolgung auf frischer Tat, 2. bei Gefahr im Verzug, 3. we...
- **[Judge=2]** `§ 104 StPO – Rn. 14` — Spezielle Durchsuchung nach §103, nicht allgemeine Voraussetzungen
  > 14 III. Durchsuchungszweck. Durchsuchungszweck darf nur die Ergreifung des Beschuldigten sein, nicht die Auffindung v. Spuren u. Beweismitteln. Werben für eine terroristische Vereinigung o. deren geri...
- **[Judge=1]** `§ 127 StPO – IV. Zur Festnahme berechtigt – Rn. 20` — Behandelt Festnahme, nicht Wohnungsdurchsuchung
  > 20 Zur Durchführung der vorl. Festnahme vgl. → Rn. 12 ff. Die Grenzen der Festnahmemittel werden für Polizeibeamte nach hM durch das Polizeirecht, insbes. die Landesgesetze über die Anwendung unmittel...

#### azure-semantic — Top 3
- **[Judge=2]** `§ 105 StPO – Rn. 13` — Behandelt Zwangsmittel bei Durchsuchung, aber nicht Voraussetzungen
  > 13 H. Unmittelbarer Zwang. Die Anordnung – auch die wegen Gefahr im Verzug (LG Trier NStZ 2024, 511) – berechtigt dazu, die Durchsuchung mit Zwangsmaßnahmen durchzusetzen (OLG Stuttgart MDR 1984, 249;...
- **[Judge=0]** `§ 145d StGB – BT. Siebenter Abschnitt – Rn. 9` — Behandelt Vortäuschung von Straftaten, nicht Durchsuchungsrecht
  > 9 In der zweiten Fallgruppe hat der Täuschende die Tat selbst begangen und versucht, den Verdacht von sich abzulenken. Erforderlich ist auch hier, dass er die Verfolgungstätigkeit in eine bestimmte fa...
- **[Judge=2]** `§ 127 StPO – IV. Zur Festnahme berechtigt – Rn. 20` — Behandelt Durchsuchung, aber fokussiert auf Festnahme
  > 20 Zur Durchführung der vorl. Festnahme vgl. → Rn. 12 ff. Die Grenzen der Festnahmemittel werden für Polizeibeamte nach hM durch das Polizeirecht, insbes. die Landesgesetze über die Anwendung unmittel...

### q11 — alltagssprache

**Query:** Was passiert wenn jemand luegt damit er Geld bekommt?

**Kontext:** Laienhafte Umschreibung des Betrugstatbestandes

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours-api | 1.00 | 100% | 100% | 3 | 6.7s |
| azure-hybrid | 0.76 | 50% | 33% | 1 | 1.5s |
| azure-semantic | 0.80 | 50% | 67% | 1 | 1.7s |

#### ours-api — Top 3
- **[Judge=3]** `§ 263 StGB – I. Vermögensbegriff  – Rn. 263` — Direkt relevant: Betrugstatbestand entspricht exakt der Suchanfrage
  > 263 (1) Wer in der Absicht, sich oder einem Dritten einen rechtswidrigen Vermögensvorteil zu verschaffen, das Vermögen eines anderen dadurch beschädigt, daß er durch Vorspiegelung falscher oder durch ...
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 5` — Direkt relevant für Betrugstatbestand
  > 5 C. Grundtatbestand, Abs. 1. Tathandlung ist das Täuschen einer natürlichen Person (vgl. NStZ 2005, 213) über Tatsachen. Erfolg dieser Handlung muss ein Irrtum des Täuschungsadressaten sein; dieser m...
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 176` — Beantwortet direkt Betrugstatbestand und subjektive Tatbestandsmerkmale
  > D. Subjektiver Tatbestand. § 263 setzt Vorsatz voraus; darüber hinaus ist die Absicht rechtswidriger Bereicherung erforderlich.   I. Vorsatz. 1. Täuschungsvorsatz. Der Vorsatz (bedingter Vorsatz genüg...

#### azure-hybrid — Top 3
- **[Judge=1]** `§ 160 StGB – BT. Neunter Abschnitt – Rn. 160` — Falscheid-Verleitung, nicht Betrug um Geld
  > 160 (1) Wer einen anderen zur Ableistung eines falschen Eides verleitet, wird mit Freiheitsstrafe bis zu zwei Jahren oder mit Geldstrafe bestraft; wer einen anderen zur Ableistung einer falschen Versi...
- **[Judge=3]** `§ 263 StGB – I. Vermögensbegriff  – Rn. 263` — Direkt relevant: kompletter Betrugstatbestand § 263
  > 263 (1) Wer in der Absicht, sich oder einem Dritten einen rechtswidrigen Vermögensvorteil zu verschaffen, das Vermögen eines anderen dadurch beschädigt, daß er durch Vorspiegelung falscher oder durch ...
- **[Judge=0]** `§ 53 StGB – E. Geldstrafe (Abs` — Gesamtstrafe bei Tatmehrheit, nicht Betrug
  > die Strafe nach allgemeinen Grundsätzen (§§ 46, 47) zuzumessen; dabei kann die Verletzung der anderen Gesetze strafschärfend verwertet werden (stRspr).  Aus Abs. 2 S. 2 ergibt sich auch, dass auf eine...

#### azure-semantic — Top 3
- **[Judge=1]** `§ 109d StGB – C. Subjektiver Tatbestand` — Tangential - anderer Straftatbestand, nicht Betrug
  > Machenschaft ist mehr als eine bloße – einmalige – Lüge (hM; OLG Hamm NZWehrr 2014, 84); der Begriff setzt vielmehr ein methodisch berechnetes Gesamtverhalten voraus (vgl. BayObLGSt 1961, 222 (224); O...
- **[Judge=3]** `§ 263 StGB – I. Sonstige Vorschriften 239 – Rn. 263 (Teil 1)` — Inhaltsverzeichnis zu § 263 StGB - Betrug direkt relevant
  > 3. Einzelne Fallgruppen ... 92 4. Rechtlich missbilligte, sittenwidrige und gesetzeswidrige wirtschaftliche Werte ... 101 VI. Schaden ... 110 1. Grundsätze der Schadensermittlung ... 111 2. Vermögensm...
- **[Judge=3]** `§ 263 StGB – I. Vermögensbegriff  – Rn. 263` — Definiert exakt Betrug durch Luegen fuer Geld
  > 263 (1) Wer in der Absicht, sich oder einem Dritten einen rechtswidrigen Vermögensvorteil zu verschaffen, das Vermögen eines anderen dadurch beschädigt, daß er durch Vorspiegelung falscher oder durch ...

### q12 — alltagssprache

**Query:** Wann muss jemand ins Gefaengnis waehrend die Tat noch nicht bewiesen ist?

**Kontext:** Untersuchungshaft, §§ 112 ff. StPO

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours-api | 1.00 | 100% | 100% | 3 | 7.6s |
| azure-hybrid | 0.77 | 50% | 33% | 1 | 1.6s |
| azure-semantic | 0.93 | 40% | 67% | 3 | 1.5s |

#### ours-api — Top 3
- **[Judge=3]** `§ 112 StPO – Rn. 112` — Direkt relevant - definiert Untersuchungshaft-Voraussetzungen
  > 112 (1) ¹ Die Untersuchungshaft darf gegen den Beschuldigten angeordnet werden, wenn er der Tat dringend verdächtig ist und ein Haftgrund besteht. ² Sie darf nicht angeordnet werden, wenn sie zu der B...
- **[Judge=3]** `§ 112 StPO – III. Flucht (Abs – Rn. 23` — Behandelt direkt Haftgruende bei Untersuchungshaft
  > Bei einer besonders hohen Straferwartung braucht daher nur geprüft zu werden, ob Umstände vorhanden sind, die die hieraus herzuleitende Fluchtgefahr ausräumen können (KG StV 1996, 383; OLG München Str...
- **[Judge=3]** `§ 112 StPO – III. Flucht (Abs – Rn. 17` — Direkt relevant: Fluchtgefahr als Haftgrund behandelt
  > Die Beurteilung der Fluchtgefahr erfordert die Berücksichtigung aller Umstände des Falles, insbes. der Art der dem Beschuldigten vorgeworfenen Tat, der Persönlichkeit des Beschuldigten, seiner Lebensv...

#### azure-hybrid — Top 3
- **[Judge=1]** `§ 345 StGB` — Behandelt Verfolgung Unschuldiger, nicht Untersuchungshaft
  > diesem Sinne Unschuldigen zu verfolgen, auch wenn er keine sichere Kenntnis von dessen Unschuld hat (BT-Drs. 7/550, 279; LK-StGB/Zieschang Rn. 10; aA Herzberg JR 1986, 8; krit. auch Schroeder FS Rudol...
- **[Judge=3]** `§ 112 StPO – Rn. 112` — Direkt relevant: Voraussetzungen für Untersuchungshaft, dringender Tatverdacht
  > Haftunfähigkeit des Beschuldigten schließt den Erlass des Haftbefehls nicht aus, sondern hindert nur seinen Vollzug (OLG Düsseldorf JZ 1984, 248; OLG Frankfurt a.M. NJW 1968, 2302; OLG Nürnberg OLGSt ...
- **[Judge=0]** `§ 315c StGB – C. Tathandlung von Nr – Rn. 1` — Behandelt Verkehrsstraftaten, nicht Untersuchungshaft
  > Literatur zur Fahrlässigkeits-Strafbarkeit bei Schäden durch autonome Maschinen (autonomes Fahren) vgl. → Vor § 13 Rn. 50b.  B. Systematik. Die Tat nach § 315c ist konkretes Gefährdungsdelikt. § 315c ...

#### azure-semantic — Top 3
- **[Judge=3]** `§ 112a StPO – Rn. 39` — Direkt relevant zu Untersuchungshaft-Voraussetzungen
  > B. Voraussetzung der Sicherungshaft (Abs. 1). Dringender Verdacht iSd § 112 Abs. 1 S. 1 (→ § 112 Rn. 5) muss bestehen hins. einer der in S. 1 Nr. 1 und 2 abschl. bezeichneten Straftaten (Anlasstaten),...
- **[Judge=3]** `§ 112 StPO – Rn. 112` — Erklärt dringenden Tatverdacht für Untersuchungshaft direkt
  > Haftunfähigkeit des Beschuldigten schließt den Erlass des Haftbefehls nicht aus, sondern hindert nur seinen Vollzug (OLG Düsseldorf JZ 1984, 248; OLG Frankfurt a.M. NJW 1968, 2302; OLG Nürnberg OLGSt ...
- **[Judge=0]** `§ 96 StGB – D. Rechtfertigung – Rn. 36` — Behandelt Staatsgeheimnisse, nicht Untersuchungshaft
  > 36 (1) Wer sich ein Staatsgeheimnis verschafft, um es zu verraten (§ 94), wird mit Freiheitsstrafe von einem Jahr bis zu zehn Jahren bestraft.  (2) Wer sich ein Staatsgeheimnis, das von einer amtliche...

### q13 — stpo-prozess

**Query:** Welche Voraussetzungen hat die Untersuchungshaft wegen Fluchtgefahr?

**Kontext:** § 112 Abs. 2 Nr. 2 StPO Fluchtgefahr

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours-api | 0.96 | 60% | 100% | 3 | 25.4s |
| azure-hybrid | 0.97 | 50% | 100% | 3 | 1.7s |
| azure-semantic | 0.91 | 80% | 100% | 2 | 1.8s |

#### ours-api — Top 3
- **[Judge=3]** `§ 112 StPO – Rn. 112` — Direkt relevant: § 112 Abs. 2 Nr. 2 StPO Fluchtgefahr
  > 112 (1) ¹ Die Untersuchungshaft darf gegen den Beschuldigten angeordnet werden, wenn er der Tat dringend verdächtig ist und ein Haftgrund besteht. ² Sie darf nicht angeordnet werden, wenn sie zu der B...
- **[Judge=2]** `§ 112 StPO – III. Flucht (Abs – Rn. 23` — Thematisch relevant, behandelt Haftgruende aber Verdunkelungsgefahr
  > Bei einer besonders hohen Straferwartung braucht daher nur geprüft zu werden, ob Umstände vorhanden sind, die die hieraus herzuleitende Fluchtgefahr ausräumen können (KG StV 1996, 383; OLG München Str...
- **[Judge=3]** `§ 112 StPO – III. Flucht (Abs – Rn. 17 (Teil 1)` — Direkt relevant: zentrale Voraussetzungen der Fluchtgefahr detailliert erklaert
  > 17 IV. Fluchtgefahr (Abs. 2 Nr. 2). Fluchtgefahr (Abs. 2 Nr. 2) besteht, wenn die Würdigung der Umstände des Falles es wahrscheinlicher macht, dass sich der Beschuldigte dem Strafverfahren entziehen, ...

#### azure-hybrid — Top 3
- **[Judge=3]** `§ 112 StPO – III. Flucht (Abs – Rn. 17` — Direkt relevant: konkrete Voraussetzungen der Fluchtgefahr
  > Die Beurteilung der Fluchtgefahr erfordert die Berücksichtigung aller Umstände des Falles, insbes. der Art der dem Beschuldigten vorgeworfenen Tat, der Persönlichkeit des Beschuldigten, seiner Lebensv...
- **[Judge=3]** `§ 112 StPO – III. Flucht (Abs – Rn. 17 (Teil 1)` — Direkt relevant: definiert Fluchtgefahr-Voraussetzungen detailliert
  > 17 IV. Fluchtgefahr (Abs. 2 Nr. 2). Fluchtgefahr (Abs. 2 Nr. 2) besteht, wenn die Würdigung der Umstände des Falles es wahrscheinlicher macht, dass sich der Beschuldigte dem Strafverfahren entziehen, ...
- **[Judge=3]** `§ 112 StPO – III. Flucht (Abs – Rn. 23` — Direkt relevant: Fluchtgefahr, Straferwartung, Verhältnismäßigkeit bei UHaft
  > 23 Bei der Straferwartung hat eine schematische Beurteilung anhand genereller Maßstäbe zu unterbleiben; insbes. ist die Annahme unzulässig, dass bei einer Straferwartung in bestimmter Höhe stets (o. a...

#### azure-semantic — Top 3
- **[Judge=2]** `§ 16a StPO – JGG. Anh – Rn. 15` — Behandelt Untersuchungshaft bei Jugendlichen, aber nicht allgemeine Fluchtgefahr
  > (2) Solange der Jugendliche das sechzehnte Lebensjahr noch nicht vollendet hat, ist die Verhängung von Untersuchungshaft wegen Fluchtgefahr nur zulässig, wenn er  1. sich dem Verfahren bereits entzoge...
- **[Judge=2]** `§ 113 StPO – Rn. 113` — Behandelt Fluchtgefahr, aber nur bei leichten Delikten
  > 113 (1) Ist die Tat nur mit Freiheitsstrafe bis zu sechs Monaten oder mit Geldstrafe bis zu einhundertachtzig Tagessätzen bedroht, so darf die Untersuchungshaft wegen Verdunkelungsgefahr nicht angeord...
- **[Judge=3]** `§ 112 StPO – Rn. 112` — Direkte Antwort zu Fluchtgefahr-Voraussetzungen nach § 112 Abs. 2 Nr. 2
  > 112 (1) ¹ Die Untersuchungshaft darf gegen den Beschuldigten angeordnet werden, wenn er der Tat dringend verdächtig ist und ein Haftgrund besteht. ² Sie darf nicht angeordnet werden, wenn sie zu der B...

### q14 — stpo-prozess

**Query:** Wie lange darf die Untersuchungshaft maximal dauern?

**Kontext:** § 121 StPO Sechs-Monats-Grenze, Haftpruefung OLG

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours-api | 1.00 | 100% | 100% | 3 | 7.5s |
| azure-hybrid | 0.84 | 70% | 67% | 2 | 1.7s |
| azure-semantic | 0.94 | 50% | 100% | 3 | 1.8s |

#### ours-api — Top 3
- **[Judge=3]** `§ 121 StPO – Rn. 1` — Beantwortet direkt Sechs-Monats-Grenze und OLG-Regelung
  > 1 A. Beschleunigungsgebot. Einen Anspruch auf beschleunigte Aburteilung hat der in UHaft (und einstweiliger Unterbringung) befindliche Beschuldigte nach Art. 5 Abs. 3 S. 2 EMRK (→ EMRK Art. 5 Rn. 10 f...
- **[Judge=3]** `§ 121 StPO – Rn. 1` — Direkt relevant, behandelt maximale Untersuchungshaftdauer
  > Eine absolute Höchstgrenze für die Dauer v. UHaft sieht weder die StPO noch die EMRK vor (EGMR EuGRZ 1993, 384). Es kommt auf eine Abwägung aller Umstände des Einzelfalls an. Eine ein Jahr übersteigen...
- **[Judge=3]** `§ 121 StPO – Rn. 121` — Beantwortet direkt die Frage zur Haftdauer-Begrenzung
  > 121 (1) Solange kein Urteil ergangen ist, das auf Freiheitsstrafe oder eine freiheitsentziehende Maßregel der Besserung und Sicherung erkennt, darf der Vollzug der Untersuchungshaft wegen derselben Ta...

#### azure-hybrid — Top 3
- **[Judge=2]** `§ 122a StPO – G. Zuständigkeit des BGH (Abs` — Behandelt Haftdauer, aber speziell bei Wiederholungsgefahr
  > G. Zuständigkeit des BGH (Abs. 7). Der BGH (Abs. 7) entscheidet über die Haftfortdauer, wenn für die Sache nach § 120 GVG ein OLG im 1. Rechtszug zuständig ist (vgl. § 121 Abs. 4 S. 2).  Höchstdauer d...
- **[Judge=0]** `§ 456a StPO – Rn. 6` — Behandelt Strafaufschub, nicht Untersuchungshaft
  > 6 B. Maximale Dauer (Abs. 2). Nicht länger als 4 Monate (Abs. 2) darf der Strafaufschub dauern. Die nach § 43 zu bestimmende Frist beginnt nach jetzt ganz hM an dem Tag, zu dem der Verurteilte zum Str...
- **[Judge=3]** `§ 121 StPO – Rn. 1` — Direkt relevant: Höchstgrenzen und Zeitbegrenzungen der Untersuchungshaft
  > Eine absolute Höchstgrenze für die Dauer v. UHaft sieht weder die StPO noch die EMRK vor (EGMR EuGRZ 1993, 384). Es kommt auf eine Abwägung aller Umstände des Einzelfalls an. Eine ein Jahr übersteigen...

#### azure-semantic — Top 3
- **[Judge=3]** `§ 121 StPO – Rn. 121` — Direkter Gesetzestext zur Sechsmonatsfrist der Untersuchungshaft
  > 121 (1) Solange kein Urteil ergangen ist, das auf Freiheitsstrafe oder eine freiheitsentziehende Maßregel der Besserung und Sicherung erkennt, darf der Vollzug der Untersuchungshaft wegen derselben Ta...
- **[Judge=3]** `§ 16a StPO – RL. für das Strafverfahren und das Bußgeldverfa` — Direkt relevant zu Untersuchungshaft über sechs Monate
  > (3) Haftprüfungen und Haftbeschwerden sollen den Fortgang der Ermittlungen nicht aufhalten.  55. Anordnung der Freilassung des Verhafteten. (1) ¹Hebt das Gericht den Haftbefehl auf, ordnet es zugleich...
- **[Judge=3]** `§ 122a StPO – G. Zuständigkeit des BGH (Abs` — Direkt relevant: behandelt Höchstdauer der Untersuchungshaft
  > G. Zuständigkeit des BGH (Abs. 7). Der BGH (Abs. 7) entscheidet über die Haftfortdauer, wenn für die Sache nach § 120 GVG ein OLG im 1. Rechtszug zuständig ist (vgl. § 121 Abs. 4 S. 2).  Höchstdauer d...

### q15 — stpo-prozess

**Query:** Was regelt § 136 StPO zur Beschuldigtenvernehmung?

**Kontext:** Belehrungspflichten, Recht auf Verteidiger

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours-api | 0.96 | 70% | 67% | 3 | 7.9s |
| azure-hybrid | 0.83 | 30% | 33% | 1 | 1.4s |
| azure-semantic | 0.97 | 20% | 67% | 2 | 1.4s |

#### ours-api — Top 3
- **[Judge=3]** `§ 135 OWiG – A. 2 StPO – Rn. 41` — Direkt relevant: regelt Belehrungspflichten bei Beschuldigtenvernehmung
  > ## Abschnitt 9b Vorläufiges Berufsverbot  ## § 132a Anordnung und Aufhebung eines vorläufigen Berufsverbots nicht abgedruckt⁶⁵  ## Zehnter Abschnitt Vernehmung des Beschuldigten  ## § 133 Ladung⁶⁶ VB ...
- **[Judge=3]** `§ 399 AO – Rn. 8` — Behandelt direkt § 136 StPO und Belehrungspflichten
  > 8 a) Vernehmung des Beschuldigten. Spätestens vor Abschluss der Ermittlungen ist der Beschuldigte zu vernehmen (§ 163a I 1 StPO). In einfachen Sachen genügt es, dass ihm Gelegenheit gegeben wird, sich...
- **[Judge=1]** `§ 135 OWiG – A. 2 StPO – Rn. 41` — Regelt Verhaftung, nicht § 136 StPO Vernehmung
  > (1) ¹ Der verhaftete Beschuldigte ist unverzüglich und schriftlich in einer für ihn verständlichen Sprache über seine Rechte zu belehren. ² Ist eine schriftliche Belehrung erkennbar nicht ausreichend,...

#### azure-hybrid — Top 3
- **[Judge=1]** `§ 34 StPO – Rn. 9` — Behandelt Verteidiger bei Vernehmung, nicht § 136
  > 9 III. Beschuldigtenvernehmung (Nr. 3). An der Beschuldigtenvernehmung (Nr. 3) darf der Verteidiger, abw. v. §§ 163a Abs. 3 S. 2, 168c Abs. 1 StPO, nicht teilnehmen, wenn die gem. § 31 Abs. 1 getroffe...
- **[Judge=2]** `StPO – III. Steuerstrafverfahren – Rn. 77` — Thematischer Bezug zu § 136 StPO und Beschuldigtenstatus
  > 77 1. Tatverdacht allein begründet allerdings weder die Beschuldigteneigenschaft noch zwingt er ohne weiteres zur Einleitung v. Ermittlungen (BGHSt 64, 89 = NJW 2019, 2627 (2630)), auch nicht allein d...
- **[Judge=0]** `§ 69 StPO – Rn. 16` — Behandelt Zeugenvernehmung statt Beschuldigtenvernehmung
  > 16 Nach Abs. 3 S. 2 sind die Entscheidungen nach Abs. 1 S. 3 und Abs. 2 S. 1 **aktenkundig** zu machen, wobei nicht nur die Entsch. als solche, sondern auch ihre Gründe festzuhalten sind (Abs. 3 S. 2)...

#### azure-semantic — Top 3
- **[Judge=2]** `StPO – III. Steuerstrafverfahren – Rn. 77` — Behandelt Beschuldigteneigenschaft und Vernehmungsregeln, aber nicht § 136
  > 77 1. Tatverdacht allein begründet allerdings weder die Beschuldigteneigenschaft noch zwingt er ohne weiteres zur Einleitung v. Ermittlungen (BGHSt 64, 89 = NJW 2019, 2627 (2630)), auch nicht allein d...
- **[Judge=1]** `§ 78c StGB – AT. Fünfter Abschnitt – Rn. 7` — Erwähnt § 136 StPO, aber behandelt Verjährungsunterbrechung
  > 7 F. Unterbrechungshandlungen (Abs. 1 S. 1, Abs. 2). Abs. 1 S. 1 enthält einen abschließenden Katalog der Unterbrechungshandlungen (BGHSt 25, 6 (8)). Eine Analogie zu Ungunsten des Täters ist nicht zu...
- **[Judge=2]** `§ 16a StPO – ILL. für das Strafverfahren und das Bußgeldverf` — Belehrung nach § 136 StPO, aber nicht Kerninhalt
  > (4) Zeugen können zur Aufenthaltsermittlung ausgeschrieben werden.  (5) Für die internationale Fahndung nach Personen, einschließlich der Fahndung nach Personen im SIS und aufgrund eines Europäischen ...

### q16 — cross-reference

**Query:** Worin unterscheidet sich Betrug von Unterschlagung?

**Kontext:** Abgrenzung § 263 vs § 246 StGB

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours-api | 0.98 | 70% | 100% | 3 | 6.8s |
| azure-hybrid | 0.80 | 30% | 33% | 2 | 2.3s |
| azure-semantic | 0.86 | 20% | 33% | 1 | 2.3s |

#### ours-api — Top 3
- **[Judge=3]** `§ 263 StGB – I. Vermögensbegriff  – Rn. 263` — Enthält vollständigen Betrug-Tatbestand für direkte Abgrenzung
  > 263 (1) Wer in der Absicht, sich oder einem Dritten einen rechtswidrigen Vermögensvorteil zu verschaffen, das Vermögen eines anderen dadurch beschädigt, daß er durch Vorspiegelung falscher oder durch ...
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 76` — Direkte Abgrenzung Betrug, behandelt Dreiecksbetrug vs Wegnahme
  > 4. Dreiecksbetrug. Da die Getäuschte und die verfügende, nicht aber die verfügende und die geschädigte Person identisch sein müssen, ist der Tatbestand des § 263 nur erfüllt, wenn die Vermögensverfügu...
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 62` — Direkt relevant für Betrug-Tatbestandsmerkmale bei Abgrenzung
  > Die Kausalität der Täuschung für den Irrtum und dessen Kausalität für die Vermögensverfügung müssen im Einzelfall festgestellt sein. Mitverursachung reicht aus. Dabei darf das Gericht auch bei Serien-...

#### azure-hybrid — Top 3
- **[Judge=2]** `§ 247 StGB – BT. Neunzehnter Abschnitt – Rn. 24` — Behandelt Verhältnis § 246 zu § 263, aber nicht Abgrenzungskriterien
  > 24 L. Konkurrenzen im Übrigen. Bei Manifestation des Zueignungswillens hinsichtlich mehrerer Sachen durch eine Ausführungshandlung liegt nur eine Tat vor (wistra 2006, 227 (227 f.)). Zur Abgrenzung vo...
- **[Judge=1]** `§ 242 StGB – BT. Neunzehnter Abschnitt – Rn. 18` — Behandelt Diebstahl vs Betrug, aber andere Abgrenzungsproblematik
  > 18 1. Selbstbedienungsladen. Im Selbstbedienungsladen erlangt Gewahrsam, wer Waren in die Tasche steckt (BGHSt 16, 273; 17, 209; 26, 24; NJW 1981, 997), zum Verkauf angebotene Lebens- oder Genussmitte...
- **[Judge=1]** `§ 246 StGB – BT. Neunzehnter Abschnitt – Rn. 16` — Behandelt nur Unterschlagung, nicht Abgrenzung zu Betrug
  > 16 G. Veruntreuende Unterschlagung (Abs. 2). Abs. 2 regelt die Veruntreuung als qualifizierten Fall der Unterschlagung. Sie liegt vor, wenn die Sache dem Täter anvertraut ist, sei es vom Eigentümer od...

#### azure-semantic — Top 3
- **[Judge=1]** `§ 253 StGB – BT. Zwanzigster Abschnitt – Rn. 2` — Behandelt Erpressung vs Betrug, nicht Unterschlagung
  > 2 B. Systematik. Erpressung ist die Nötigung (§ 240) einer Person, durch die dem Vermögen der genötigten oder einer anderen (natürlichen oder juristischen) Person in der Absicht rechtswidriger Bereich...
- **[Judge=1]** `§ 248a StGB – E. Irrtum` — Behandelt Antragserfordernis, nicht materielle Abgrenzung
  > B. Anwendungsbereich. § 247 stellt, um bestimmte persönliche Beziehungen durch Eingreifen von Amts wegen nicht zu stören (BGHSt 10, 403; 18, 126; 29, 56), für Diebstahl und Unterschlagung in allen For...
- **[Judge=2]** `§ 266 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 191` — Behandelt Abgrenzung Unterschlagung/Untreue, nicht Betrug/Unterschlagung
  > Tateinheit ist möglich mit Diebstahl (Dallinger MDR 1954, 399), und zwar auch dann, wenn auch eine nicht in einem Treueverhältnis stehende Person den Diebstahl hätte begehen können (BGHSt 17, 360); mi...

### q17 — cross-reference

**Query:** Was sind die Unterschiede zwischen Diebstahl und Raub?

**Kontext:** § 242 vs § 249 StGB — Abgrenzung durch Gewalt/Drohung

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours-api | 0.96 | 100% | 100% | 3 | 7.4s |
| azure-hybrid | 0.90 | 90% | 100% | 2 | 1.5s |
| azure-semantic | 0.94 | 60% | 67% | 3 | 1.0s |

#### ours-api — Top 3
- **[Judge=3]** `§ 249 StGB` — Direkt relevant: Abgrenzung Raub vs Erpressung mit Gewaltmerkmal
  > NStZ 2023, 351). Danach ist § 249 gegenüber § 255 ein spezielles Delikt; in jedem Raub liegt eine räuberische Erpressung (aA die hM in der Literatur). Die Unterscheidung richtet sich nach dem äußeren ...
- **[Judge=2]** `§ 252 StGB – I. Sonstige Vorschriften – Rn. 252` — Behandelt räuberischen Diebstahl, nicht direkte Abgrenzung Diebstahl/Raub
  > 252 Wer, bei einem Diebstahl auf frischer Tat betroffen, gegen eine Person Gewalt verübt oder Drohungen mit gegenwärtiger Gefahr für Leib oder Leben anwendet, um sich im Besitz des gestohlenen Gutes z...
- **[Judge=3]** `§ 249 StGB – BT. Zwanzigster Abschnitt – Rn. 6` — Erklärt zentrale Abgrenzung Diebstahl/Raub durch Gewalt-Wegnahme-Zusammenhang
  > 6 E. Finalzusammenhang zwischen Nötigung und Wegnahme. Gewalt oder Drohung müssen das (objektive und subjektive) Mittel zur Ermöglichung der Wegnahme (in Zueignungsabsicht) sein (BGHSt 4, 210 (211); 2...

#### azure-hybrid — Top 3
- **[Judge=2]** `§ 250 StGB` — Behandelt Raub-Konkurrenzen, aber nicht direkte Abgrenzung Diebstahl-Raub
  > I. Rechtsfolgen. Der (einfache) Raub ist Verbrechen. Für minder schwere Fälle (vgl. → § 12 Rn. 11; → § 46 Rn. 85 ff.) gilt Abs. 2; ein solcher kann zB vorliegen, wenn das Maß der Gewalt gering ist ode...
- **[Judge=2]** `§ 252 StGB – I. Sonstige Vorschriften – Rn. 252` — Behandelt räuberischen Diebstahl, Übergangsbereich zwischen Diebstahl/Raub
  > 252 Wer, bei einem Diebstahl auf frischer Tat betroffen, gegen eine Person Gewalt verübt oder Drohungen mit gegenwärtiger Gefahr für Leib oder Leben anwendet, um sich im Besitz des gestohlenen Gutes z...
- **[Judge=3]** `§ 248c StGB – G. Konkurrenzen – Rn. 2` — Direkt relevante Abgrenzung Raub-Diebstahl durch systematische Stellung
  > 2 B. Systematische Stellung. Raub als selbstständiges Delikt (BGHSt 20, 235 (237 f.)) richtet sich gegen das Eigentum und die persönliche Freiheit (BGH NJW 1968, 1292). Die §§ 247, 248a sind unanwendb...

#### azure-semantic — Top 3
- **[Judge=3]** `§ 248c StGB – G. Konkurrenzen – Rn. 2` — Direkte Abgrenzung Raub-Diebstahl, zentrale Rechtsbegriffe behandelt
  > 2 B. Systematische Stellung. Raub als selbstständiges Delikt (BGHSt 20, 235 (237 f.)) richtet sich gegen das Eigentum und die persönliche Freiheit (BGH NJW 1968, 1292). Die §§ 247, 248a sind unanwendb...
- **[Judge=2]** `§ 252 StGB – I. Sonstige Vorschriften – Rn. 252` — Behandelt räuberischen Diebstahl, nicht direkte Abgrenzung Diebstahl/Raub
  > 252 Wer, bei einem Diebstahl auf frischer Tat betroffen, gegen eine Person Gewalt verübt oder Drohungen mit gegenwärtiger Gefahr für Leib oder Leben anwendet, um sich im Besitz des gestohlenen Gutes z...
- **[Judge=1]** `§ 250 StGB` — Konkurrenzen zwischen Raub/Diebstahl, aber nicht Abgrenzungskriterien
  > I. Rechtsfolgen. Der (einfache) Raub ist Verbrechen. Für minder schwere Fälle (vgl. → § 12 Rn. 11; → § 46 Rn. 85 ff.) gilt Abs. 2; ein solcher kann zB vorliegen, wenn das Maß der Gewalt gering ist ode...

### q18 — cross-reference

**Query:** Wann wird Betrug zu Computerbetrug und umgekehrt?

**Kontext:** § 263 vs § 263a StGB — Abgrenzung bei elektronischer Datenverarbeitung

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours-api | 0.99 | 80% | 100% | 3 | 6.9s |
| azure-hybrid | 0.87 | 60% | 100% | 2 | 1.1s |
| azure-semantic | 0.93 | 60% | 100% | 3 | 1.3s |

#### ours-api — Top 3
- **[Judge=3]** `§ 263a StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 23` — Direkte Abgrenzung zwischen § 263 und § 263a
  > 23 G. Subjektiver Tatbestand. Die Tat setzt (bedingten) Vorsatz voraus. Er muss sich auf alle Tatbestandsmerkmale, zu denen auch die Unbefugtheit (→ Rn. 10) gehört, dh auch auf die Voraussetzungen ers...
- **[Judge=3]** `§ 263a StGB – M. Sonstige Vorschriften 40 – Rn. 239` — Definiert Computerbetrug direkt, zentral fuer Abgrenzung
  > 239 I. Sonstige Vorschriften. FAufsicht §§ 263 Abs. 5, 68 Abs. 1. Zuständigkeit in Wirtschaftsstrafaschen § 74c Abs. 1 Nr. 6, § 74e Nr. 2 GVG iVm § 103 Abs. 2 JGG. TKÜ § 100a Abs. 2 Nr. 1 Buchst. n St...
- **[Judge=3]** `§ 263a StGB – L. Konkurrenzen – Rn. 33` — Direkte Abgrenzung zwischen § 263 und § 263a
  > II. Verhältnis zu sonstigen Tatbeständen. § 263a und § 263 schließen sich aus, wenn derselbe Schaden sowohl durch die Manipulationsweisen des § 263a als auch durch Täuschung bewirkt wird. Mit § 263 is...

#### azure-hybrid — Top 3
- **[Judge=2]** `§ 263 StGB – I. Vermögensbegriff  – Rn. 263` — Betrug-Definition, aber fehlt Computerbetrug-Abgrenzung
  > 263 (1) Wer in der Absicht, sich oder einem Dritten einen rechtswidrigen Vermögensvorteil zu verschaffen, das Vermögen eines anderen dadurch beschädigt, daß er durch Vorspiegelung falscher oder durch ...
- **[Judge=2]** `§ 263a StGB – L. Konkurrenzen – Rn. 33` — Behandelt Computerbetrug, aber nicht die Abgrenzung
  > 33 III. Tathandlungen des Abs. 3. Die Tathandlungen des Abs. 3 entsprechen § 149 Abs. 1 (vgl. auch § 152a Abs. 1 Nr. 2). Herstellen eines Programms ist kein Tätigkeitsdelikt; Abs. 3 setzt, wie sich au...
- **[Judge=3]** `§ 263a StGB – BT. Zweijundzwanzigster Abschnitt – Rn. 239` — Direkt relevant für Abgrenzung Betrug/Computerbetrug
  > Neuere Literatur (Auswahl): Achenbach, Strukturen des § 263a StGB, FS Gössel, 2002, 481; Altenhain, Der strafbare Missbrauch kartengestützter elektronischer Zahlungssysteme, JZ 1997, 752; Arloth, Comp...

#### azure-semantic — Top 3
- **[Judge=3]** `§ 263a StGB – M. Sonstige Vorschriften 40 – Rn. 239` — Behandelt direkt § 263a Tatbestandsmerkmale und Abgrenzung
  > 239 I. Sonstige Vorschriften. FAufsicht §§ 263 Abs. 5, 68 Abs. 1. Zuständigkeit in Wirtschaftsstrafaschen § 74c Abs. 1 Nr. 6, § 74e Nr. 2 GVG iVm § 103 Abs. 2 JGG. TKÜ § 100a Abs. 2 Nr. 1 Buchst. n St...
- **[Judge=2]** `§ 243 StGB – BT. Neunzehnter Abschnitt` — Erwähnt Abgrenzung Diebstahl zu Computerbetrug, nicht Betrug
  > BT. Neunzehnter Abschnitt.  1979, 118); oder wenn sonst durch die Nachtat ein anderes Rechtsgut verletzt wird; in den letzteren Fällen ist Realkonkurrenz mit dem vorausgegangenen Diebstahl gegeben, se...
- **[Judge=2]** `§ 1 StGB – AT. Erster Abschnitt – Rn. 45` — Behandelt Betrug-Computerbetrug-Verhältnis bei Postpendenz, nicht Abgrenzungskriterien
  > 45 4. Postpendenz. Als sog. Postpendenz werden Fälle bezeichnet, in denen eine nur einseitige Sachverhaltsungewissheit in dem Sinn besteht, dass von zwei Sachverhalten der zeitlich frühere möglicherwe...