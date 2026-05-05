# RAG Benchmark Report

_Generiert: 2026-05-05T21:39:42_


- Queries: **18**
- Top-K: **10**
- Systeme: azure-hybrid-exp, azure-semantic-exp, ours-api

## Gesamtvergleich

| Metrik | azure-hybrid-exp | azure-semantic-exp | ours-api |
|--------|--------|--------|--------|
| nDCG@10 | 0.955 | 0.918 | 0.982 |
| Relevance@10 | 80.0% | 60.0% | 86.7% |
| Relevance@3 | 90.7% | 79.6% | 96.3% |
| Top-1-Score | 2.83 | 2.44 | 3.00 |
| Mean-Score | 2.33 | 1.87 | 2.50 |
| Latenz (s) | 5.14 | 1.13 | 8.26 |

## Nach Kategorie


### alltagssprache

| Metrik | azure-hybrid-exp | azure-semantic-exp | ours-api |
|--------|--------|--------|--------|
| nDCG@10 | 0.979 | 0.854 | 0.999 |
| Relevance@10 | 92.5% | 52.5% | 95.0% |
| Relevance@3 | 91.7% | 66.7% | 100.0% |

### cross-reference

| Metrik | azure-hybrid-exp | azure-semantic-exp | ours-api |
|--------|--------|--------|--------|
| nDCG@10 | 0.964 | 0.924 | 0.975 |
| Relevance@10 | 83.3% | 56.7% | 90.0% |
| Relevance@3 | 88.9% | 77.8% | 100.0% |

### exakte-paragraphen

| Metrik | azure-hybrid-exp | azure-semantic-exp | ours-api |
|--------|--------|--------|--------|
| nDCG@10 | 0.951 | 0.924 | 0.986 |
| Relevance@10 | 80.0% | 65.0% | 85.0% |
| Relevance@3 | 100.0% | 75.0% | 100.0% |

### konzept

| Metrik | azure-hybrid-exp | azure-semantic-exp | ours-api |
|--------|--------|--------|--------|
| nDCG@10 | 0.956 | 0.956 | 0.966 |
| Relevance@10 | 72.5% | 72.5% | 80.0% |
| Relevance@3 | 91.7% | 91.7% | 83.3% |

### stpo-prozess

| Metrik | azure-hybrid-exp | azure-semantic-exp | ours-api |
|--------|--------|--------|--------|
| nDCG@10 | 0.916 | 0.937 | 0.981 |
| Relevance@10 | 70.0% | 50.0% | 83.3% |
| Relevance@3 | 77.8% | 88.9% | 100.0% |

## Detail pro Query


### q01 — exakte-paragraphen

**Query:** Welche Voraussetzungen hat der gewerbsmaessige Bandenbetrug nach § 263 Abs. 5 StGB?

**Kontext:** Qualifikationstatbestand des Bandenbetrugs im Fischer-Kommentar

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours-api | 0.99 | 60% | 100% | 3 | 24.0s |
| azure-hybrid-exp | 0.92 | 80% | 100% | 2 | 5.5s |
| azure-semantic-exp | 0.94 | 50% | 67% | 3 | 1.4s |

#### ours-api — Top 3
- **[Judge=3]** `§ 263 StGB – I. Vermögensbegriff  – Rn. 263` — Enthält direkt § 263 Abs. 5 Voraussetzungen
  > 263 (1) Wer in der Absicht, sich oder einem Dritten einen rechtswidrigen Vermögensvorteil zu verschaffen, das Vermögen eines anderen dadurch beschädigt, daß er durch Vorspiegelung falscher oder durch ...
- **[Judge=3]** `§ 263 StGB – BT. Zweriindzwanzigster Abschnitt – Rn. 225` — Direkt relevant: behandelt § 263 Abs. 5 Voraussetzungen
  > IV. Qualifikation (Abs. 5). Abs. 5 enthält einen Qualifikationstatbestand, der die Tat in Fällen kumulativ gewerbs- und bandenmäßiger Begehung zum Verbrechen macht. Die Qualifikation ist in die Urteil...
- **[Judge=3]** `§ 263 StGB – BT. Zweijundzwanzigster Abschnitt – Rn. 213` — Direkt relevant zu Abs. 5 Bandenbetrug-Voraussetzungen
  > 213 Sind beide Varianten erfüllt, ist eine Qualifikation nach Abs. 5 gegeben. Die Abgrenzung des Abs. 3 Nr. 1 zum Verbrechen nach Abs. 5 ist in Fällen bandenmäßiger Begehung schwierig, denn eine auf f...

#### azure-hybrid-exp — Top 3
- **[Judge=2]** `§ 263 StGB – BT. Zweijundzwanzigster Abschnitt – Rn. 201` — Behandelt Gewerbsmäßigkeit, aber nicht Bandenbetrug Abs. 5
  > Ein Gefährdungsschaden kann für die Strafzumessung nicht mit dem tatsächlich eingetretenen Schaden gleichgesetzt werden (wistra 1999, 185 (187); BGHSt 53, 71 (79) = NJW 2009, 528; 1. StS; aA aber BGHS...
- **[Judge=3]** `§ 263 StGB – BT. Zweijundzwanzigster Abschnitt – Rn. 211` — Definiert direkt Bandenmäßigkeit bei § 263 Abs. 5
  > 211 b) Bandenmäßigkeit. Bandenmäßige Begehung ist gegeben, wenn sich eine Bande (zum Begriff vgl. → § 244 Rn. 34 ff.) zur Begehung einer Mehrzahl von selbstständigen Taten der Urkundenfälschung oder d...
- **[Judge=2]** `§ 267 StGB – BT. Dreiundzwanzigster Abschnitt – Rn. 44` — Behandelt Bandenbetrug, aber nicht § 263 Abs. 5
  > I. Rechtsfolgen; besonders schwere Fälle (Abs. 3). Abs. 1 droht für den Grundfall Freiheitsstrafe bis zu 5 Jahren oder Geldstrafe an. Der besonders schwere Fall (Abs. 3) ist durch Regelbeispiele ausge...

#### azure-semantic-exp — Top 3
- **[Judge=3]** `§ 263 StGB – BT. Zweriindzwanzigster Abschnitt – Rn. 225` — Direkt relevant - erklärt Bandenbetrug § 263 Abs. 5
  > IV. Qualifikation (Abs. 5). Abs. 5 enthält einen Qualifikationstatbestand, der die Tat in Fällen kumulativ gewerbs- und bandenmäßiger Begehung zum Verbrechen macht. Die Qualifikation ist in die Urteil...
- **[Judge=3]** `§ 263 StGB – BT. Zweijundzwanzigster Abschnitt – Rn. 213` — Behandelt direkt Voraussetzungen von Abs. 5 Bandenbetrug
  > 213 Sind beide Varianten erfüllt, ist eine Qualifikation nach Abs. 5 gegeben. Die Abgrenzung des Abs. 3 Nr. 1 zum Verbrechen nach Abs. 5 ist in Fällen bandenmäßiger Begehung schwierig, denn eine auf f...
- **[Judge=0]** `§ 100a StPO – G. Zufallsfunde` — StPO-Text ueber Telekommunikationsueberwachung, nicht Betrug
  > 2. die Tat auch im Einzelfall schwer wiegt und 3. die Erforschung des Sachverhalts oder die Ermittlung des Aufenthaltsortes des Beschuldigten auf andere Weise wesentlich erschwert oder aussichtslos wä...

### q02 — exakte-paragraphen

**Query:** Was regelt § 112 StPO zur Untersuchungshaft?

**Kontext:** Anordnungsvoraussetzungen der U-Haft (dringender Tatverdacht, Haftgrund) im Schmitt/Koehler

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours-api | 0.99 | 100% | 100% | 3 | 21.7s |
| azure-hybrid-exp | 0.97 | 80% | 100% | 3 | 5.7s |
| azure-semantic-exp | 0.96 | 90% | 100% | 3 | 2.2s |

#### ours-api — Top 3
- **[Judge=3]** `§ 112 StPO – Rn. 112` — Direkt relevant: § 112 StPO Anordnungsvoraussetzungen Untersuchungshaft
  > 112 (1) ¹ Die Untersuchungshaft darf gegen den Beschuldigten angeordnet werden, wenn er der Tat dringend verdächtig ist und ein Haftgrund besteht. ² Sie darf nicht angeordnet werden, wenn sie zu der B...
- **[Judge=3]** `§ 112 StPO – III. Flucht (Abs – Rn. 23` — Direkt relevant: behandelt Haftgruende nach § 112 StPO
  > Bei einer besonders hohen Straferwartung braucht daher nur geprüft zu werden, ob Umstände vorhanden sind, die die hieraus herzuleitende Fluchtgefahr ausräumen können (KG StV 1996, 383; OLG München Str...
- **[Judge=3]** `§ 112 StPO – III. Flucht (Abs – Rn. 32 (Teil 2)` — Direkt relevant: behandelt Verdunkelungsgefahr als Haftgrund nach § 112 StPO
  > Wenn die Verdunkelungshandlungen nicht geeignet sind, die Ermittlung der Wahrheit zu erschweren, darf UHaft nicht angeordnet werden. Der Haftgrund liegt daher nicht vor, wenn der Sachverhalt schon in ...

#### azure-hybrid-exp — Top 3
- **[Judge=3]** `§ 112 StPO – Rn. 112` — Direkt relevant: komplette Regelung § 112 StPO
  > 112 (1) ¹ Die Untersuchungshaft darf gegen den Beschuldigten angeordnet werden, wenn er der Tat dringend verdächtig ist und ein Haftgrund besteht. ² Sie darf nicht angeordnet werden, wenn sie zu der B...
- **[Judge=3]** `§ 114 StPO – A. Erlass des Haftbefehls (Abs – Rn. 9` — Direkt relevante Ausführungen zu § 112 StPO Haftgründen
  > IV. Haftgrund (Nr. 3, 4). Der Haftgrund (Nr. 3, 4) als die prozessuale Grdl. des Haftbefehls ist ebenfalls zu bezeichnen. Dabei genügt die Kurzbezeichnung (Fluchtgefahr, Verdunkelungsgefahr, Wiederhol...
- **[Judge=2]** `§ 116 StPO – Rn. 116` — Behandelt Aussetzung der U-Haft, nicht Anordnungsvoraussetzungen
  > 116 (1) Der Richter setzt den Vollzug eines Haftbefehls, der lediglich wegen Fluchtgefahr gerechtfertigt ist, aus, wenn weniger einschneidende Maßnahmen die Erwartung hinreichend begründen, daß der Zw...

#### azure-semantic-exp — Top 3
- **[Judge=3]** `§ 112 StPO – Rn. 112` — Direkt relevant: § 112 StPO Anordnungsvoraussetzungen U-Haft
  > 112 (1) ¹ Die Untersuchungshaft darf gegen den Beschuldigten angeordnet werden, wenn er der Tat dringend verdächtig ist und ein Haftgrund besteht. ² Sie darf nicht angeordnet werden, wenn sie zu der B...
- **[Judge=3]** `§ 112 StPO – Rn. 112` — Behandelt direkt §112 StPO Haftbefehl-Voraussetzungen
  > Haftunfähigkeit des Beschuldigten schließt den Erlass des Haftbefehls nicht aus, sondern hindert nur seinen Vollzug (OLG Düsseldorf JZ 1984, 248; OLG Frankfurt a.M. NJW 1968, 2302; OLG Nürnberg OLGSt ...
- **[Judge=2]** `§ 112 StPO – Rn. 10` — Behandelt U-Haft Grundsätze, aber nicht § 112 StPO konkret
  > 10 UHaft darf daher nicht angeordnet werden, wenn der Beschuldigte freiwillige Beschränkungen (Ablieferung der Personalpapiere, freiwilliges Sich-Unterziehen einer Anstaltbehandlung; vgl. auch § 71 Ab...

### q03 — exakte-paragraphen

**Query:** Welche Haftgruende nennt § 112 Abs. 2 StPO?

**Kontext:** Fluchtgefahr, Verdunkelungsgefahr, Flucht — im StPO-Kommentar

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours-api | 0.99 | 100% | 100% | 3 | 5.3s |
| azure-hybrid-exp | 0.96 | 100% | 100% | 3 | 4.3s |
| azure-semantic-exp | 0.82 | 40% | 33% | 1 | 1.0s |

#### ours-api — Top 3
- **[Judge=3]** `§ 112 StPO – Rn. 112` — Direkte Antwort: listet alle drei Haftgruende auf
  > 112 (1) ¹ Die Untersuchungshaft darf gegen den Beschuldigten angeordnet werden, wenn er der Tat dringend verdächtig ist und ein Haftgrund besteht. ² Sie darf nicht angeordnet werden, wenn sie zu der B...
- **[Judge=3]** `§ 112 StPO – III. Flucht (Abs – Rn. 23` — Direkt relevant: Verdunkelungsgefahr als Haftgrund nach § 112 Abs. 2
  > Bei einer besonders hohen Straferwartung braucht daher nur geprüft zu werden, ob Umstände vorhanden sind, die die hieraus herzuleitende Fluchtgefahr ausräumen können (KG StV 1996, 383; OLG München Str...
- **[Judge=3]** `§ 112 StPO – III. Flucht (Abs – Rn. 17 (Teil 1)` — Direkt relevant: erklärt Fluchtgefahr als Haftgrund
  > 17 IV. Fluchtgefahr (Abs. 2 Nr. 2). Fluchtgefahr (Abs. 2 Nr. 2) besteht, wenn die Würdigung der Umstände des Falles es wahrscheinlicher macht, dass sich der Beschuldigte dem Strafverfahren entziehen, ...

#### azure-hybrid-exp — Top 3
- **[Judge=3]** `§ 112 StPO – III. Flucht (Abs – Rn. 23` — Behandelt direkt Haftgruende nach § 112 Abs. 2 StPO
  > Bei einer besonders hohen Straferwartung braucht daher nur geprüft zu werden, ob Umstände vorhanden sind, die die hieraus herzuleitende Fluchtgefahr ausräumen können (KG StV 1996, 383; OLG München Str...
- **[Judge=2]** `§ 112 StPO – III. Flucht (Abs – Rn. 32 (Teil 2)` — Behandelt Verdunkelungsgefahr als einen der Haftgruende
  > Wenn die Verdunkelungshandlungen nicht geeignet sind, die Ermittlung der Wahrheit zu erschweren, darf UHaft nicht angeordnet werden. Der Haftgrund liegt daher nicht vor, wenn der Sachverhalt schon in ...
- **[Judge=2]** `§ 112 StPO – III. Flucht (Abs – Rn. 17` — Behandelt Fluchtgefahr, aber nicht direkt die Haftgründe
  > Die Beurteilung der Fluchtgefahr erfordert die Berücksichtigung aller Umstände des Falles, insbes. der Art der dem Beschuldigten vorgeworfenen Tat, der Persönlichkeit des Beschuldigten, seiner Lebensv...

#### azure-semantic-exp — Top 3
- **[Judge=1]** `§ 112 StPO – Rn. 112` — Behandelt Haftbefehl allgemein, nicht spezifische Haftgründe § 112 Abs. 2
  > Haftunfähigkeit des Beschuldigten schließt den Erlass des Haftbefehls nicht aus, sondern hindert nur seinen Vollzug (OLG Düsseldorf JZ 1984, 248; OLG Frankfurt a.M. NJW 1968, 2302; OLG Nürnberg OLGSt ...
- **[Judge=3]** `§ 112 StPO – Rn. 112` — Enthaelt vollstaendig alle Haftgruende aus § 112 Abs. 2
  > 112 (1) ¹ Die Untersuchungshaft darf gegen den Beschuldigten angeordnet werden, wenn er der Tat dringend verdächtig ist und ein Haftgrund besteht. ² Sie darf nicht angeordnet werden, wenn sie zu der B...
- **[Judge=1]** `§ 112 StPO – Rn. 10` — Behandelt Untersuchungshaft allgemein, nicht konkrete Haftgruende
  > 10 UHaft darf daher nicht angeordnet werden, wenn der Beschuldigte freiwillige Beschränkungen (Ablieferung der Personalpapiere, freiwilliges Sich-Unterziehen einer Anstaltbehandlung; vgl. auch § 71 Ab...

### q04 — exakte-paragraphen

**Query:** Was regelt § 102 StPO zur Durchsuchung beim Beschuldigten?

**Kontext:** Durchsuchungsvoraussetzungen beim Verdaechtigen

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours-api | 0.97 | 80% | 100% | 3 | 5.7s |
| azure-hybrid-exp | 0.95 | 60% | 100% | 3 | 5.1s |
| azure-semantic-exp | 0.98 | 80% | 100% | 3 | 1.7s |

#### ours-api — Top 3
- **[Judge=3]** `§ 102 StPO – Rn. 102` — Regelt direkt § 102 StPO Durchsuchung beim Beschuldigten
  > 102 Bei dem, welcher als Täter oder Teilnehmer einer Straftat oder der Datenhehlerei, Begünstigung, Strafvereitelung oder Hehlerei  Köhler    Ermittlungsmaßnahmen  verdächtig ist, kann eine Durchsuchu...
- **[Judge=2]** `§ 102 StPO – Rn. 10` — Behandelt Durchsuchungsrecht, aber nicht spezifisch § 102 StPO
  > II. Auffinden von Beweismitteln. Zu den Beweismitteln (→ § 94 Rn. 4 ff.) gehören auch die nur in § 103 erwähnten Spuren (SK-StPO/Jäger/Wohlers Rn. 21) u. Personen, die zu Beweiszwecken in Augenschein ...
- **[Judge=3]** `§ 102 StPO – Rn. 3` — Behandelt direkt § 102 StPO Durchsuchung beim Verdächtigen
  > 3 C. Verdächtige. Der Verdächtige muss die Durchsuchung dulden. Er braucht noch nicht Beschuldigter (→ Einl. Rn. 76 ff.) zu sein; der Tatverdacht gegen ihn muss bei der Anordnung der Maßnahme nicht ei...

#### azure-hybrid-exp — Top 3
- **[Judge=3]** `§ 102 StPO – Rn. 102` — Direkter Gesetzestext und Kommentierung zu § 102 StPO
  > 102 Bei dem, welcher als Täter oder Teilnehmer einer Straftat oder der Datenhehlerei, Begünstigung, Strafvereitelung oder Hehlerei  Köhler    Ermittlungsmaßnahmen  verdächtig ist, kann eine Durchsuchu...
- **[Judge=2]** `§ 102 StPO – Rn. 10` — Behandelt Durchsuchungsvoraussetzungen, aber nicht spezifisch § 102
  > II. Auffinden von Beweismitteln. Zu den Beweismitteln (→ § 94 Rn. 4 ff.) gehören auch die nur in § 103 erwähnten Spuren (SK-StPO/Jäger/Wohlers Rn. 21) u. Personen, die zu Beweiszwecken in Augenschein ...
- **[Judge=3]** `§ 105 StPO – Rn. 5` — Direkt relevant: behandelt Verdachtsanforderungen bei Durchsuchung
  > Weitere Anforderungen: Die wesentlichen Verdachtsmomente sind darzulegen, also regelmäßig auch die Indiztatsachen, auf die der Verdacht gestützt wird (BGH NStZ-RR 2009, 142; BVerfG NJW 2015, 1585 (158...

#### azure-semantic-exp — Top 3
- **[Judge=3]** `§ 102 StPO – Rn. 3` — Direkt relevant zu § 102 StPO Durchsuchungsvoraussetzungen
  > 3 C. Verdächtige. Der Verdächtige muss die Durchsuchung dulden. Er braucht noch nicht Beschuldigter (→ Einl. Rn. 76 ff.) zu sein; der Tatverdacht gegen ihn muss bei der Anordnung der Maßnahme nicht ei...
- **[Judge=3]** `§ 102 StPO – Rn. 102` — Direkter Gesetzestext und vollständige Erklärung § 102 StPO
  > 102 Bei dem, welcher als Täter oder Teilnehmer einer Straftat oder der Datenhehlerei, Begünstigung, Strafvereitelung oder Hehlerei  Köhler    Ermittlungsmaßnahmen  verdächtig ist, kann eine Durchsuchu...
- **[Judge=2]** `§ 102 StPO – Rn. 10` — Behandelt Durchsuchungsvoraussetzungen, aber nicht spezifisch § 102
  > II. Auffinden von Beweismitteln. Zu den Beweismitteln (→ § 94 Rn. 4 ff.) gehören auch die nur in § 103 erwähnten Spuren (SK-StPO/Jäger/Wohlers Rn. 21) u. Personen, die zu Beweiszwecken in Augenschein ...

### q05 — konzept

**Query:** Wann liegt eine konkludente Taeuschung im Sinne des § 263 StGB vor?

**Kontext:** Taeuschungshandlung durch schluessiges Verhalten

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours-api | 0.99 | 100% | 100% | 3 | 6.1s |
| azure-hybrid-exp | 0.99 | 90% | 100% | 3 | 5.0s |
| azure-semantic-exp | 1.00 | 90% | 100% | 3 | 1.0s |

#### ours-api — Top 3
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 21` — Definiert direkt konkludente Taeuschung bei § 263 StGB
  > 21 2. Konkludente Erklärungen. Auch durch eine schlüssige Handlung (konkludente Erklärung) kann vorspiegelt werden. Eine solche konkludente Erklärung durch aktives Tun ist von einer Erklärung durch Un...
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 14` — Behandelt konkludente Täuschung und Abgrenzungskriterien direkt
  > Rspr. und hM bejahen darüber hinaus aber die Möglichkeit einer Täuschung durch Unterlassen auch ohne Erklärung gegenüber dem Irrenden (→ Rn. 38; vgl. BGHSt 39, 392 (398); BayObLG NJW 1987, 1654 (mAnm ...
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 14` — Erklärt konkludente Täuschung bei § 263 StGB detailliert
  > 14 II. Tathandlung. Der Begriff „Täuschen“ ist im Wortlaut des Abs. 1 nicht verwendet; er ergibt sich aus dem Zusammenhang zwischen der Beschreibung der Tathandlung (→ Rn. 18) und dem Irrtum als ihrem...

#### azure-hybrid-exp — Top 3
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 21` — Direkt relevant: Definition konkludente Täuschung § 263
  > 21 2. Konkludente Erklärungen. Auch durch eine schlüssige Handlung (konkludente Erklärung) kann vorspiegelt werden. Eine solche konkludente Erklärung durch aktives Tun ist von einer Erklärung durch Un...
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 14` — Direkte Definition konkludenter Täuschung durch schlüssiges Verhalten
  > Rspr. und hM bejahen darüber hinaus aber die Möglichkeit einer Täuschung durch Unterlassen auch ohne Erklärung gegenüber dem Irrenden (→ Rn. 38; vgl. BGHSt 39, 392 (398); BayObLG NJW 1987, 1654 (mAnm ...
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 23` — Direkte Beispiele konkludenter Taeuschung bei § 263
  > 23 Von besonderer praktischer Bedeutung sind hier Fälle, in denen die Ordnungsmäßigkeit einer vom Erklärungsempfänger unterstellten „Geschäftsgrundlage“ vorgetäuscht wird (krit. Kargl FS Lüderssen, 20...

#### azure-semantic-exp — Top 3
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 27` — Direkt relevant: konkrete Beispiele konkludenter Täuschungen
  > 27 b) Geltendmachen von Forderungen. Das Einfordern einer Leistung, auf die kein Anspruch besteht, ist eine Täuschung iSv § 263, wenn nicht allein eine Rechtsbehauptung aufgestellt, sondern ein Bezug ...
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 14` — Definiert direkt konkludente Täuschung bei § 263
  > Fischer/Lutz     BT. Zweiundzwanzigster Abschnitt.  Sinn verwendeten Wortbedeutungen (Arzt FS Hirsch, 1999, 446). Hier liegt idR entweder ein konkludentes Miterklären unwahrer oder ein Entstellen wahr...
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 21` — Definiert direkt konkludente Taeuschung nach § 263
  > 21 2. Konkludente Erklärungen. Auch durch eine schlüssige Handlung (konkludente Erklärung) kann vorspiegelt werden. Eine solche konkludente Erklärung durch aktives Tun ist von einer Erklärung durch Un...

### q06 — konzept

**Query:** Was ist eine Vermoegensverfuegung und welche Anforderungen stellt die Rechtsprechung?

**Kontext:** Tatbestandsmerkmal der Vermoegensverfuegung beim Betrug

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours-api | 0.94 | 60% | 67% | 3 | 7.1s |
| azure-hybrid-exp | 0.91 | 70% | 100% | 2 | 4.9s |
| azure-semantic-exp | 0.92 | 60% | 100% | 2 | 1.3s |

#### ours-api — Top 3
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 76` — Direkt relevant zu Vermoegensverfuegung beim Betrug
  > 76 3. Unmittelbarkeit der Verfügung. Neben der Freiwilligkeit ist das Merkmal der Unmittelbarkeit nach stRspr und hM das wichtigste Kriterium zur Beschränkung der § 263 unterfallenden Selbstschädigung...
- **[Judge=1]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 87` — Behandelt Betrug, aber Kausalität statt Verfügungsdefinition
  > 87 5. Kausalität. Für die Vermögensverfügung muss der täuschungsbedingte Irrtum kausal sein (vgl. BGHSt 24, 257 (260); 24, 386 (389); NStZ 2003, 313 (314 f.); OLG Düsseldorf NJW 1987, 3145); Mitverurs...
- **[Judge=3]** `§ 263 StGB – BT. Zweitundzwanzigster Abschnitt – Rn. 69` — Definiert Vermoegensverfuegung und nennt zentrale Anforderungen
  > 69 Anders ist es, wenn der Verfügende seinerseits nur (gutgläubige) Hilfsperson eines bösgläubigen Dritten ist. Hier ist auf den Irrtum des Entscheidungsbefugten abzustellen: Erkennt dieser die Unrich...

#### azure-hybrid-exp — Top 3
- **[Judge=2]** `§ 263 StGB – I. Vermögensbegriff  – Rn. 263` — Betrug-Grundtatbestand, aber keine Vermoegensverfuegung-Details
  > 263 (1) Wer in der Absicht, sich oder einem Dritten einen rechtswidrigen Vermögensvorteil zu verschaffen, das Vermögen eines anderen dadurch beschädigt, daß er durch Vorspiegelung falscher oder durch ...
- **[Judge=3]** `§ 263 StGB – BT. Zweitundzwanzigster Abschnitt – Rn. 69` — Direkt relevant: Definition und Anforderungen der Vermoegensverfuegung
  > 69 Anders ist es, wenn der Verfügende seinerseits nur (gutgläubige) Hilfsperson eines bösgläubigen Dritten ist. Hier ist auf den Irrtum des Entscheidungsbefugten abzustellen: Erkennt dieser die Unrich...
- **[Judge=2]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 87` — Thematisch relevant, behandelt Betrug und Verfügungskausalität
  > 87 5. Kausalität. Für die Vermögensverfügung muss der täuschungsbedingte Irrtum kausal sein (vgl. BGHSt 24, 257 (260); 24, 386 (389); NStZ 2003, 313 (314 f.); OLG Düsseldorf NJW 1987, 3145); Mitverurs...

#### azure-semantic-exp — Top 3
- **[Judge=2]** `§ 253 StGB – BT. Zwanzigster Abschnitt – Rn. 14` — Erpressung-Kontext, aber relevante Verfügungsdefinition
  > 14 I. Vermögensverfügung. Nach zutreffender Ansicht der Lit. muss das Verhalten des Genötigten eine Vermögensverfügung sein, das heißt eine willentliche Übertragung der faktischen Herrschaft über eine...
- **[Judge=3]** `§ 263 StGB – BT. Zweitundzwanzigster Abschnitt – Rn. 69` — Definiert Vermoegensverfuegung als ungeschriebenes Tatbestandsmerkmal direkt
  > 69 Anders ist es, wenn der Verfügende seinerseits nur (gutgläubige) Hilfsperson eines bösgläubigen Dritten ist. Hier ist auf den Irrtum des Entscheidungsbefugten abzustellen: Erkennt dieser die Unrich...
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 74` — Direkt relevant: definiert Vermögensverfügung und Rechtsprechungsanforderungen
  > 74 2. Verfügungsbewusstsein. Vermögensverfügungen sind nach hM grundsätzlich sowohl als bewusst als auch als unbewusst vermögensmindernde Handlungen möglich; eine aktuelle Vorstellung des Verfügenden ...

### q07 — konzept

**Query:** Was versteht man unter einem Gefaehrdungsschaden beim Betrug?

**Kontext:** Schadensbegriff, schadensgleiche Vermoegensgefaehrdung

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours-api | 1.00 | 100% | 100% | 3 | 6.3s |
| azure-hybrid-exp | 0.98 | 80% | 100% | 3 | 5.2s |
| azure-semantic-exp | 1.00 | 100% | 100% | 3 | 1.3s |

#### ours-api — Top 3
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 159` — Definiert exakt Gefährdungsschaden beim Betrug
  > 159 b) Voraussetzungen. aa) Ein Gefährdungsschaden ist gegeben, wenn die Wahrscheinlichkeit des endgültigen Verlusts eines Vermögensbestandteils zum Zeitpunkt der täuschungsbedingten Verfügung so groß...
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 171` — Direkt relevant: definiert Gefährdungsschaden beim Betrug
  > Die täuschungsbedingte Herausgabe von EC-Karten, Kreditkarten und weiteren Zugangsdaten zu Bank-Guthaben (PINs, TANs; Passwörter), sei es infolge persönlicher Täuschung oder von „Phishing“-Manipulatio...
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 163` — Direkt relevant: Definition und Beispiele von Gefaehrdungsschaeden
  > 163 c) Einzelfälle. Gefährdungsschäden sind zB bejaht worden in folgenden Fällen: BGHSt 3, 371 (373) (Erwerb eines unsicheren Pfandrechts); BGHSt 15, 83 (87 f.); wistra 2003, 230 (Prozessrisiko bei gu...

#### azure-hybrid-exp — Top 3
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 159` — Definiert direkt Gefährdungsschaden bei Betrug
  > 159 b) Voraussetzungen. aa) Ein Gefährdungsschaden ist gegeben, wenn die Wahrscheinlichkeit des endgültigen Verlusts eines Vermögensbestandteils zum Zeitpunkt der täuschungsbedingten Verfügung so groß...
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 164` — Direkt relevant: definiert und erklärt Gefährdungsschaden beim Betrug
  > 164 Es lassen sich im Übrigen Fallgruppen wie folgt unterscheiden:  aa) Der Abschluss eines unter Vorspiegelung von Leistungsfähigkeit und/oder Leistungswilligkeit erschlichenen Kaufvertrags kann eine...
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 171` — Direkt relevant: definiert Gefaehrdungsschaden beim Betrug
  > Die täuschungsbedingte Herausgabe von EC-Karten, Kreditkarten und weiteren Zugangsdaten zu Bank-Guthaben (PINs, TANs; Passwörter), sei es infolge persönlicher Täuschung oder von „Phishing“-Manipulatio...

#### azure-semantic-exp — Top 3
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 128` — Direkt relevant: behandelt explizit Gefährdungsschaden beim Betrug
  > 128 (4) BGHSt 51, 10 = NJW 2006, 1679 hat diese Grundsätze auf Fälle des Anlagebetrugs übertragen. Hier liegt ein Schaden vor, soweit die Zins- und Gewinnerwartungen des über das Risiko Getäuschten hi...
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 164` — Direkt relevant: erklaert Gefaehrdungsschaden beim Betrug konkret
  > 164 Es lassen sich im Übrigen Fallgruppen wie folgt unterscheiden:  aa) Der Abschluss eines unter Vorspiegelung von Leistungsfähigkeit und/oder Leistungswilligkeit erschlichenen Kaufvertrags kann eine...
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 159` — Definiert direkt Gefährdungsschaden beim Betrug
  > 159 b) Voraussetzungen. aa) Ein Gefährdungsschaden ist gegeben, wenn die Wahrscheinlichkeit des endgültigen Verlusts eines Vermögensbestandteils zum Zeitpunkt der täuschungsbedingten Verfügung so groß...

### q08 — konzept

**Query:** Wie wird der Vorsatz beim Betrug bestimmt, insbesondere die Bereicherungsabsicht?

**Kontext:** Subjektiver Tatbestand § 263 StGB

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours-api | 0.93 | 60% | 67% | 3 | 6.7s |
| azure-hybrid-exp | 0.95 | 50% | 67% | 3 | 4.1s |
| azure-semantic-exp | 0.91 | 40% | 67% | 3 | 1.0s |

#### ours-api — Top 3
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 176` — Beantwortet direkt Vorsatz und Bereicherungsabsicht beim Betrug
  > D. Subjektiver Tatbestand. § 263 setzt Vorsatz voraus; darüber hinaus ist die Absicht rechtswidriger Bereicherung erforderlich.   I. Vorsatz. 1. Täuschungsvorsatz. Der Vorsatz (bedingter Vorsatz genüg...
- **[Judge=1]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 187 (Tei` — Behandelt Stoffgleichheit, nicht Vorsatz/Bereicherungsabsicht
  > 187 1. Stoffgleichheit. Der Vorteil muss die Kehrseite des Schadens und ihm „stoffgleich“ sein; er muss unmittelbare Folge der täuschungsbedingten Verfügung sein, welche den Schaden des Opfers herbeif...
- **[Judge=2]** `§ 263 StGB – I. Vermögensbegriff  – Rn. 263` — Gesetzestext relevant, aber keine Vorsatzerläuterung
  > 263 (1) Wer in der Absicht, sich oder einem Dritten einen rechtswidrigen Vermögensvorteil zu verschaffen, das Vermögen eines anderen dadurch beschädigt, daß er durch Vorspiegelung falscher oder durch ...

#### azure-hybrid-exp — Top 3
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 176` — Direkt relevant: Vorsatz bei Betrug, subjektiver Tatbestand
  > D. Subjektiver Tatbestand. § 263 setzt Vorsatz voraus; darüber hinaus ist die Absicht rechtswidriger Bereicherung erforderlich.   I. Vorsatz. 1. Täuschungsvorsatz. Der Vorsatz (bedingter Vorsatz genüg...
- **[Judge=3]** `§ 263 StGB – BT. Zweijundzwanzigster Abschnitt – Rn. 194` — Direkt relevant zu Vorsatz und Bereicherungsabsicht bei Betrug
  > 194 4. Vorsatz hinsichtlich der Rechtswidrigkeit. Die Rechtswidrigkeit des angestrebten Vermögensvorteils muss vom Vorsatz umfasst sein; sie ist wie bei § 253 (vgl. dort 20) subjektives Tatbestandsmer...
- **[Judge=0]** `§ 244a StGB – E. Subjektiver Tatbestand` — Behandelt Diebstahl, nicht Betrug § 263
  > E. Subjektiver Tatbestand. Zum Vorsatz des Diebstahls unter den Voraussetzungen des § 243 Abs. 1 S. 2 vgl. dort; zum Vorsatz des Diebstahls mit Waffen (§ 244 Abs. 1 Nr. 1a, 1b) → § 244 Rn. 31.  Fische...

#### azure-semantic-exp — Top 3
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 176` — Behandelt direkt Vorsatz und Bereicherungsabsicht bei § 263
  > D. Subjektiver Tatbestand. § 263 setzt Vorsatz voraus; darüber hinaus ist die Absicht rechtswidriger Bereicherung erforderlich.   I. Vorsatz. 1. Täuschungsvorsatz. Der Vorsatz (bedingter Vorsatz genüg...
- **[Judge=1]** `§ 271 StGB – BT. Dreiundzwanzigster Abschnitt – Rn. 14` — Behandelt § 271, nicht § 263 Betrug
  > E. Subjektiver Tatbestand. § 271 setzt Vorsatz hinsichtlich der Unrichtigkeit der zu beurkundenden (Abs. 1) oder beurkundeten (Abs. 2) Tatsache und der anderen Tatbestandsmerkmale voraus; bedingter Vo...
- **[Judge=2]** `§ 259 StGB – BT. Einundzwanzigster Abschnitt – Rn. 18` — Behandelt Bereicherungsabsicht, aber bei Hehlerei nicht Betrug
  > Erfährt der Täter erst nach Erlangung des Gewahrsams von der Herkunft der Sache aus der Vortat, so kommt Hehlerei in Betracht, wenn der Täter den Gewahrsam zunächst zwar zu eigener Verfügungsgewalt, a...

### q09 — alltagssprache

**Query:** Hat der Angeklagte die Kunden über das Internet betrogen?

**Kontext:** Abstrakte Frage zu Internetbetrug, sucht Taeuschungshandlung + Schaden

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours-api | 1.00 | 100% | 100% | 3 | 6.5s |
| azure-hybrid-exp | 0.97 | 80% | 67% | 3 | 4.5s |
| azure-semantic-exp | 0.83 | 60% | 67% | 2 | 0.9s |

#### ours-api — Top 3
- **[Judge=3]** `§ 263 StGB – I. Vermögensbegriff  – Rn. 263` — Zentraler Betrugsparagraph mit allen relevanten Tatbestandsmerkmalen
  > 263 (1) Wer in der Absicht, sich oder einem Dritten einen rechtswidrigen Vermögensvorteil zu verschaffen, das Vermögen eines anderen dadurch beschädigt, daß er durch Vorspiegelung falscher oder durch ...
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 5` — Erklärt zentrale Tatbestandsmerkmale des Betrugs
  > 5 C. Grundtatbestand, Abs. 1. Tathandlung ist das Täuschen einer natürlichen Person (vgl. NStZ 2005, 213) über Tatsachen. Erfolg dieser Handlung muss ein Irrtum des Täuschungsadressaten sein; dieser m...
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 14` — Direkt relevant: Betrug, Täuschungshandlungen, Internet/E-Mail-Betrug
  > Rspr. und hM bejahen darüber hinaus aber die Möglichkeit einer Täuschung durch Unterlassen auch ohne Erklärung gegenüber dem Irrenden (→ Rn. 38; vgl. BGHSt 39, 392 (398); BayObLG NJW 1987, 1654 (mAnm ...

#### azure-hybrid-exp — Top 3
- **[Judge=3]** `§ 263 StGB – I. Vermögensbegriff  – Rn. 263` — Enthält komplette Betrugs-Tatbestandsmerkmale für Internetbetrug
  > 263 (1) Wer in der Absicht, sich oder einem Dritten einen rechtswidrigen Vermögensvorteil zu verschaffen, das Vermögen eines anderen dadurch beschädigt, daß er durch Vorspiegelung falscher oder durch ...
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 171` — Direkter Bezug zu Internetbetrug und Phishing-Täuschung
  > Die täuschungsbedingte Herausgabe von EC-Karten, Kreditkarten und weiteren Zugangsdaten zu Bank-Guthaben (PINs, TANs; Passwörter), sei es infolge persönlicher Täuschung oder von „Phishing“-Manipulatio...
- **[Judge=1]** `§ 263 StGB – I. Sonstige Vorschriften 239 – Rn. 263 (Teil 2)` — Literaturverzeichnis zu Betrug, keine konkreten Rechtsinhalte
  > Hernandez Basuano, Täuschung und Opferschutzniveau beim Betrug (usw.), FS Tiedemann, 2008, 605; Bechtel, Der Schutz illegaler Betäubungsmittel durch die Vermögens- und Eigentumsdelikte – sinnvoll?, wi...

#### azure-semantic-exp — Top 3
- **[Judge=2]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 263 (Tei` — Thematisch relevant: Internetbetrug-Literatur, gleiches Rechtsgebiet
  > Fischer/Lutz      BT. Zweiundzwanzigster Abschnitt. Fehlvorstellung beim Betrug, GA 2012, 354; Cornelius, Betrug durch verschleierte Kick-Back-Zahlungen bei Immobilienfinanzierungen?, NZWiSt 2012, 259...
- **[Judge=2]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 104` — Betrug-Tatbestand relevant, aber kein Internetbezug
  > 104 aa) Der Einsatz illegal oder sittenwidrig erworbener Gegenstände (einschließlich Geld) ist nach Rspr. und hM durch § 263 geschützt, wenn diese  Fischer/Lutz    Betrug und Untreue  Gegenstände eine...
- **[Judge=0]** `§ 247 StPO – G. Unterrichtung des Angeklagten (S – Rn. 12` — Verfahrensrecht Ausschluss Angeklagter, kein Betrug
  > F. Gerichtsbeschluss. Durch Gerichtsbeschluss, nicht durch Vfg. des Vorsitzenden allein, wird der vorübergehende Ausschluss des Angeklagten angeordnet (BGHSt 1, 346 (350); 15, 194 (196); 22, 18 (20); ...

### q10 — alltagssprache

**Query:** Wann darf die Polizei bei jemandem zu Hause suchen?

**Kontext:** Durchsuchungsvoraussetzungen, §§ 102 ff. StPO

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours-api | 1.00 | 80% | 100% | 3 | 6.0s |
| azure-hybrid-exp | 0.98 | 90% | 100% | 3 | 4.8s |
| azure-semantic-exp | 0.87 | 60% | 67% | 3 | 0.8s |

#### ours-api — Top 3
- **[Judge=3]** `§ 102 StPO – Rn. 102` — Direkt relevant: § 102 StPO Durchsuchungsvoraussetzungen
  > 102 Bei dem, welcher als Täter oder Teilnehmer einer Straftat oder der Datenhehlerei, Begünstigung, Strafvereitelung oder Hehlerei  Köhler    Ermittlungsmaßnahmen  verdächtig ist, kann eine Durchsuchu...
- **[Judge=3]** `§ 102 StPO – Rn. 10` — Direkt relevant zu Durchsuchungsvoraussetzungen und Verhältnismäßigkeit
  > II. Auffinden von Beweismitteln. Zu den Beweismitteln (→ § 94 Rn. 4 ff.) gehören auch die nur in § 103 erwähnten Spuren (SK-StPO/Jäger/Wohlers Rn. 21) u. Personen, die zu Beweiszwecken in Augenschein ...
- **[Judge=3]** `§ 102 StPO – Rn. 3` — Definiert Durchsuchungsgegenstände Wohnungen, direkt relevant
  > **Teilnehmer** nach §§ 25 ff. StGB, nicht die sog. notwendigen Teilnehmer (zum Begriff: Fischer/Fischer StGB Vor § 25 Rn. 7), stehen den Tatverdächtigen gleich. Bei jedem v. ihnen sowie bei den der Be...

#### azure-hybrid-exp — Top 3
- **[Judge=3]** `§ 105 StPO` — Regelt direkt Durchsuchungsanordnung und -verfahren
  > Beweise (BGH MDR 1964, 71). Eine willkürliche Annahme der Voraussetzungen kann bei der erforderlichen Abwägung → Einl. Rn. 55a) eine so hohes Gewicht erlangen, dass im Einzelfall ein Beweisverwertungs...
- **[Judge=3]** `§ 104 StPO – Rn. 104` — Behandelt direkt Durchsuchungsvoraussetzungen zur Nachtzeit
  > 104 (1) Zur Nachtzeit dürfen die Wohnung, die Geschäftsräume und das befriedete Besitztum nur in folgenden Fällen durchsucht werden:  1. bei Verfolgung auf frischer Tat, 2. bei Gefahr im Verzug, 3. we...
- **[Judge=2]** `§ 105 StPO – Rn. 13` — Behandelt Durchsetzung mit Zwang, nicht Voraussetzungen
  > 13 H. Unmittelbarer Zwang. Die Anordnung – auch die wegen Gefahr im Verzug (LG Trier NStZ 2024, 511) – berechtigt dazu, die Durchsuchung mit Zwangsmaßnahmen durchzusetzen (OLG Stuttgart MDR 1984, 249;...

#### azure-semantic-exp — Top 3
- **[Judge=3]** `§ 105 StPO – Rn. 13` — Direkt relevant: Zwangsmaßnahmen bei Wohnungsdurchsuchungen nach StPO
  > 13 H. Unmittelbarer Zwang. Die Anordnung – auch die wegen Gefahr im Verzug (LG Trier NStZ 2024, 511) – berechtigt dazu, die Durchsuchung mit Zwangsmaßnahmen durchzusetzen (OLG Stuttgart MDR 1984, 249;...
- **[Judge=0]** `§ 145d StGB – BT. Siebenter Abschnitt – Rn. 9` — Betrifft Täuschung bei Ermittlungen, nicht Durchsuchungsrecht
  > 9 In der zweiten Fallgruppe hat der Täuschende die Tat selbst begangen und versucht, den Verdacht von sich abzulenken. Erforderlich ist auch hier, dass er die Verfolgungstätigkeit in eine bestimmte fa...
- **[Judge=2]** `§ 127 StPO – IV. Zur Festnahme berechtigt – Rn. 20` — Thematisch relevant: Durchsuchung der Wohnung des Verdächtigen
  > 20 Zur Durchführung der vorl. Festnahme vgl. → Rn. 12 ff. Die Grenzen der Festnahmemittel werden für Polizeibeamte nach hM durch das Polizeirecht, insbes. die Landesgesetze über die Anwendung unmittel...

### q11 — alltagssprache

**Query:** Was passiert wenn jemand luegt damit er Geld bekommt?

**Kontext:** Laienhafte Umschreibung des Betrugstatbestandes

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours-api | 1.00 | 100% | 100% | 3 | 6.3s |
| azure-hybrid-exp | 1.00 | 100% | 100% | 3 | 5.7s |
| azure-semantic-exp | 0.79 | 50% | 67% | 1 | 1.0s |

#### ours-api — Top 3
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 5` — Definiert direkt den Betrugstatbestand mit Täuschung
  > 5 C. Grundtatbestand, Abs. 1. Tathandlung ist das Täuschen einer natürlichen Person (vgl. NStZ 2005, 213) über Tatsachen. Erfolg dieser Handlung muss ein Irrtum des Täuschungsadressaten sein; dieser m...
- **[Judge=3]** `§ 263 StGB – I. Vermögensbegriff  – Rn. 263` — Direkt relevant: Betrugstatbestand erfasst Luegen fuer Geld
  > 263 (1) Wer in der Absicht, sich oder einem Dritten einen rechtswidrigen Vermögensvorteil zu verschaffen, das Vermögen eines anderen dadurch beschädigt, daß er durch Vorspiegelung falscher oder durch ...
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 176` — Direkt relevant: subjektiver Tatbestand des Betrugs
  > D. Subjektiver Tatbestand. § 263 setzt Vorsatz voraus; darüber hinaus ist die Absicht rechtswidriger Bereicherung erforderlich.   I. Vorsatz. 1. Täuschungsvorsatz. Der Vorsatz (bedingter Vorsatz genüg...

#### azure-hybrid-exp — Top 3
- **[Judge=3]** `§ 263 StGB – I. Vermögensbegriff  – Rn. 263` — Direkter Betrugstatbestand: Lügen für Geld
  > 263 (1) Wer in der Absicht, sich oder einem Dritten einen rechtswidrigen Vermögensvorteil zu verschaffen, das Vermögen eines anderen dadurch beschädigt, daß er durch Vorspiegelung falscher oder durch ...
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 87` — Direkt relevant: behandelt Betrug § 263 StGB
  > 87 5. Kausalität. Für die Vermögensverfügung muss der täuschungsbedingte Irrtum kausal sein (vgl. BGHSt 24, 257 (260); 24, 386 (389); NStZ 2003, 313 (314 f.); OLG Düsseldorf NJW 1987, 3145); Mitverurs...
- **[Judge=3]** `§ 263 StGB – BT. Zweijundzwanzigster Abschnitt – Rn. 194` — Behandelt direkt Betrugsvorsatz und Rechtswidrigkeit des Vermögensvorteils
  > 194 4. Vorsatz hinsichtlich der Rechtswidrigkeit. Die Rechtswidrigkeit des angestrebten Vermögensvorteils muss vom Vorsatz umfasst sein; sie ist wie bei § 253 (vgl. dort 20) subjektives Tatbestandsmer...

#### azure-semantic-exp — Top 3
- **[Judge=1]** `§ 109d StGB – C. Subjektiver Tatbestand` — Behandelt Machenschaft bei Wehrpflichtentzug, nicht allgemeinen Betrug
  > Machenschaft ist mehr als eine bloße – einmalige – Lüge (hM; OLG Hamm NZWehrr 2014, 84); der Begriff setzt vielmehr ein methodisch berechnetes Gesamtverhalten voraus (vgl. BayObLGSt 1961, 222 (224); O...
- **[Judge=3]** `§ 263 StGB – I. Sonstige Vorschriften 239 – Rn. 263 (Teil 1)` — Direkt relevant: Betrug-Paragraf, alle Tatbestandsmerkmale behandelt
  > 3. Einzelne Fallgruppen ... 92 4. Rechtlich missbilligte, sittenwidrige und gesetzeswidrige wirtschaftliche Werte ... 101 VI. Schaden ... 110 1. Grundsätze der Schadensermittlung ... 111 2. Vermögensm...
- **[Judge=3]** `§ 263 StGB – I. Vermögensbegriff  – Rn. 263` — Definiert exakt Betrug durch Täuschung für Vermögensvorteil
  > 263 (1) Wer in der Absicht, sich oder einem Dritten einen rechtswidrigen Vermögensvorteil zu verschaffen, das Vermögen eines anderen dadurch beschädigt, daß er durch Vorspiegelung falscher oder durch ...

### q12 — alltagssprache

**Query:** Wann muss jemand ins Gefaengnis waehrend die Tat noch nicht bewiesen ist?

**Kontext:** Untersuchungshaft, §§ 112 ff. StPO

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours-api | 1.00 | 100% | 100% | 3 | 6.3s |
| azure-hybrid-exp | 0.97 | 100% | 100% | 3 | 5.9s |
| azure-semantic-exp | 0.93 | 40% | 67% | 3 | 1.0s |

#### ours-api — Top 3
- **[Judge=3]** `§ 112 StPO – Rn. 112` — Direkt relevant: § 112 StPO regelt Untersuchungshaft
  > 112 (1) ¹ Die Untersuchungshaft darf gegen den Beschuldigten angeordnet werden, wenn er der Tat dringend verdächtig ist und ein Haftgrund besteht. ² Sie darf nicht angeordnet werden, wenn sie zu der B...
- **[Judge=3]** `§ 112 StPO – III. Flucht (Abs – Rn. 23` — Direkt relevant zu Untersuchungshaft bei unbewiesen Taten
  > Bei einer besonders hohen Straferwartung braucht daher nur geprüft zu werden, ob Umstände vorhanden sind, die die hieraus herzuleitende Fluchtgefahr ausräumen können (KG StV 1996, 383; OLG München Str...
- **[Judge=3]** `§ 112 StPO – Rn. 112` — Direkter Bezug zu Untersuchungshaft und Voraussetzungen
  > Haftunfähigkeit des Beschuldigten schließt den Erlass des Haftbefehls nicht aus, sondern hindert nur seinen Vollzug (OLG Düsseldorf JZ 1984, 248; OLG Frankfurt a.M. NJW 1968, 2302; OLG Nürnberg OLGSt ...

#### azure-hybrid-exp — Top 3
- **[Judge=3]** `§ 112 StPO – Rn. 112` — Direkt relevant - beantwortet Untersuchungshaft-Voraussetzungen vollstaendig
  > 112 (1) ¹ Die Untersuchungshaft darf gegen den Beschuldigten angeordnet werden, wenn er der Tat dringend verdächtig ist und ein Haftgrund besteht. ² Sie darf nicht angeordnet werden, wenn sie zu der B...
- **[Judge=3]** `§ 112 StPO – Rn. 112` — Definiert dringenden Tatverdacht als Haftvoraussetzung
  > Haftunfähigkeit des Beschuldigten schließt den Erlass des Haftbefehls nicht aus, sondern hindert nur seinen Vollzug (OLG Düsseldorf JZ 1984, 248; OLG Frankfurt a.M. NJW 1968, 2302; OLG Nürnberg OLGSt ...
- **[Judge=2]** `§ 114 StPO – A. Erlass des Haftbefehls (Abs – Rn. 9` — Haftgründe und Begründung der Untersuchungshaft
  > IV. Haftgrund (Nr. 3, 4). Der Haftgrund (Nr. 3, 4) als die prozessuale Grdl. des Haftbefehls ist ebenfalls zu bezeichnen. Dabei genügt die Kurzbezeichnung (Fluchtgefahr, Verdunkelungsgefahr, Wiederhol...

#### azure-semantic-exp — Top 3
- **[Judge=3]** `§ 112a StPO – Rn. 39` — Direkt relevant: Untersuchungshaft bei dringendem Verdacht
  > B. Voraussetzung der Sicherungshaft (Abs. 1). Dringender Verdacht iSd § 112 Abs. 1 S. 1 (→ § 112 Rn. 5) muss bestehen hins. einer der in S. 1 Nr. 1 und 2 abschl. bezeichneten Straftaten (Anlasstaten),...
- **[Judge=3]** `§ 112 StPO – Rn. 112` — Erklaert Haftbefehl-Voraussetzungen bei dringendem Tatverdacht
  > Haftunfähigkeit des Beschuldigten schließt den Erlass des Haftbefehls nicht aus, sondern hindert nur seinen Vollzug (OLG Düsseldorf JZ 1984, 248; OLG Frankfurt a.M. NJW 1968, 2302; OLG Nürnberg OLGSt ...
- **[Judge=0]** `§ 96 StGB – D. Rechtfertigung – Rn. 36` — Behandelt Staatsgeheimnisse, nicht Untersuchungshaft
  > 36 (1) Wer sich ein Staatsgeheimnis verschafft, um es zu verraten (§ 94), wird mit Freiheitsstrafe von einem Jahr bis zu zehn Jahren bestraft.  (2) Wer sich ein Staatsgeheimnis, das von einer amtliche...

### q13 — stpo-prozess

**Query:** Welche Voraussetzungen hat die Untersuchungshaft wegen Fluchtgefahr?

**Kontext:** § 112 Abs. 2 Nr. 2 StPO Fluchtgefahr

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours-api | 0.97 | 70% | 100% | 3 | 5.8s |
| azure-hybrid-exp | 0.97 | 70% | 100% | 3 | 4.5s |
| azure-semantic-exp | 0.93 | 70% | 100% | 2 | 1.0s |

#### ours-api — Top 3
- **[Judge=3]** `§ 112 StPO – Rn. 112` — Enthält vollständigen Gesetzestext zu Fluchtgefahr
  > 112 (1) ¹ Die Untersuchungshaft darf gegen den Beschuldigten angeordnet werden, wenn er der Tat dringend verdächtig ist und ein Haftgrund besteht. ² Sie darf nicht angeordnet werden, wenn sie zu der B...
- **[Judge=3]** `§ 112 StPO – III. Flucht (Abs – Rn. 17 (Teil 1)` — Definiert direkt Fluchtgefahr-Voraussetzungen nach § 112 StPO
  > 17 IV. Fluchtgefahr (Abs. 2 Nr. 2). Fluchtgefahr (Abs. 2 Nr. 2) besteht, wenn die Würdigung der Umstände des Falles es wahrscheinlicher macht, dass sich der Beschuldigte dem Strafverfahren entziehen, ...
- **[Judge=3]** `§ 112 StPO – III. Flucht (Abs – Rn. 22` — Direkt relevant: Voraussetzungen der Fluchtgefahr nach § 112
  > 22 Die Fluchtgefahr darf nur aus bestimmten Tatsachen hergeleitet werden. Bloße Mutmaßungen u. Befürchtungen genügen nicht. Die Tatsachen brauchen aber nicht zur vollen Überzeugung des Gerichts festzu...

#### azure-hybrid-exp — Top 3
- **[Judge=3]** `§ 112 StPO – Rn. 112` — Enthält direkt die gesetzlichen Voraussetzungen der Fluchtgefahr
  > 112 (1) ¹ Die Untersuchungshaft darf gegen den Beschuldigten angeordnet werden, wenn er der Tat dringend verdächtig ist und ein Haftgrund besteht. ² Sie darf nicht angeordnet werden, wenn sie zu der B...
- **[Judge=3]** `§ 112 StPO – III. Flucht (Abs – Rn. 16` — Direkt relevant zu Fluchtgefahr nach § 112 Abs. 2 Nr. 2 StPO
  > 16 Bei Ergreifung des Beschuldigten aufgrund des nach Abs. 2 Nr. 1 erlassenen Haftbefehls entfällt der Haftgrund der Flucht. In der Regel wird die vorherige Flucht aber die Aufrechterhaltung des Haftb...
- **[Judge=3]** `§ 112 StPO – III. Flucht (Abs – Rn. 17` — Direkt relevant: Voraussetzungen und Kriterien der Fluchtgefahr
  > Die Beurteilung der Fluchtgefahr erfordert die Berücksichtigung aller Umstände des Falles, insbes. der Art der dem Beschuldigten vorgeworfenen Tat, der Persönlichkeit des Beschuldigten, seiner Lebensv...

#### azure-semantic-exp — Top 3
- **[Judge=2]** `§ 16a StPO – JGG. Anh – Rn. 15` — Behandelt Untersuchungshaft Fluchtgefahr, aber nur bei Jugendlichen
  > (2) Solange der Jugendliche das sechzehnte Lebensjahr noch nicht vollendet hat, ist die Verhängung von Untersuchungshaft wegen Fluchtgefahr nur zulässig, wenn er  1. sich dem Verfahren bereits entzoge...
- **[Judge=3]** `§ 113 StPO – Rn. 113` — Direkte Antwort zu Fluchtgefahr-Voraussetzungen nach § 113 StPO
  > 113 (1) Ist die Tat nur mit Freiheitsstrafe bis zu sechs Monaten oder mit Geldstrafe bis zu einhundertachtzig Tagessätzen bedroht, so darf die Untersuchungshaft wegen Verdunkelungsgefahr nicht angeord...
- **[Judge=3]** `§ 112 StPO – Rn. 112` — Direkt relevant: § 112 Abs. 2 Nr. 2 Fluchtgefahr
  > 112 (1) ¹ Die Untersuchungshaft darf gegen den Beschuldigten angeordnet werden, wenn er der Tat dringend verdächtig ist und ein Haftgrund besteht. ² Sie darf nicht angeordnet werden, wenn sie zu der B...

### q14 — stpo-prozess

**Query:** Wie lange darf die Untersuchungshaft maximal dauern?

**Kontext:** § 121 StPO Sechs-Monats-Grenze, Haftpruefung OLG

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours-api | 0.99 | 100% | 100% | 3 | 5.9s |
| azure-hybrid-exp | 0.93 | 80% | 67% | 3 | 5.0s |
| azure-semantic-exp | 0.92 | 50% | 100% | 3 | 1.0s |

#### ours-api — Top 3
- **[Judge=3]** `§ 121 StPO – Rn. 1` — Direkt zur Sechs-Monats-Grenze und OLG-Entscheidungen
  > 1 A. Beschleunigungsgebot. Einen Anspruch auf beschleunigte Aburteilung hat der in UHaft (und einstweiliger Unterbringung) befindliche Beschuldigte nach Art. 5 Abs. 3 S. 2 EMRK (→ EMRK Art. 5 Rn. 10 f...
- **[Judge=3]** `§ 121 StPO – Rn. 121` — Beantwortet direkt die Frage zur maximalen Untersuchungshaftdauer
  > 121 (1) Solange kein Urteil ergangen ist, das auf Freiheitsstrafe oder eine freiheitsentziehende Maßregel der Besserung und Sicherung erkennt, darf der Vollzug der Untersuchungshaft wegen derselben Ta...
- **[Judge=3]** `§ 121 StPO – Rn. 1` — Direkte Antwort zu Höchstgrenzen der Untersuchungshaft
  > Eine absolute Höchstgrenze für die Dauer v. UHaft sieht weder die StPO noch die EMRK vor (EGMR EuGRZ 1993, 384). Es kommt auf eine Abwägung aller Umstände des Einzelfalls an. Eine ein Jahr übersteigen...

#### azure-hybrid-exp — Top 3
- **[Judge=3]** `§ 121 StPO – Rn. 1` — Direkt relevant: behandelt Sechs-Monats-Grenze und OLG-Anordnung
  > 1 A. Beschleunigungsgebot. Einen Anspruch auf beschleunigte Aburteilung hat der in UHaft (und einstweiliger Unterbringung) befindliche Beschuldigte nach Art. 5 Abs. 3 S. 2 EMRK (→ EMRK Art. 5 Rn. 10 f...
- **[Judge=1]** `§ 120 StPO – Rn. 120 (Teil 1)` — Aufhebungsgruende, nicht maximale Haftdauer
  > 120 (1)¹ Der Haftbefehl ist aufzuheben, sobald die Voraussetzungen der Untersuchungshaft nicht mehr vorliegen oder sich ergibt, daß die weitere Untersuchungshaft zu der Bedeutung der Sache und der zu ...
- **[Judge=3]** `§ 121 StPO – Rn. 1` — Direkt relevant: behandelt maximale Dauer der Untersuchungshaft
  > Eine absolute Höchstgrenze für die Dauer v. UHaft sieht weder die StPO noch die EMRK vor (EGMR EuGRZ 1993, 384). Es kommt auf eine Abwägung aller Umstände des Einzelfalls an. Eine ein Jahr übersteigen...

#### azure-semantic-exp — Top 3
- **[Judge=3]** `§ 121 StPO – Rn. 121` — Beantwortet direkt die Frage zur maximalen Dauer
  > 121 (1) Solange kein Urteil ergangen ist, das auf Freiheitsstrafe oder eine freiheitsentziehende Maßregel der Besserung und Sicherung erkennt, darf der Vollzug der Untersuchungshaft wegen derselben Ta...
- **[Judge=2]** `§ 16a StPO – RL. für das Strafverfahren und das Bußgeldverfa` — Behandelt Haftfortdauer nach sechs Monaten, nicht Höchstdauer
  > (3) Haftprüfungen und Haftbeschwerden sollen den Fortgang der Ermittlungen nicht aufhalten.  55. Anordnung der Freilassung des Verhafteten. (1) ¹Hebt das Gericht den Haftbefehl auf, ordnet es zugleich...
- **[Judge=3]** `§ 122a StPO – G. Zuständigkeit des BGH (Abs` — Direkt relevant: Höchstdauer Untersuchungshaft bei Wiederholungsgefahr
  > G. Zuständigkeit des BGH (Abs. 7). Der BGH (Abs. 7) entscheidet über die Haftfortdauer, wenn für die Sache nach § 120 GVG ein OLG im 1. Rechtszug zuständig ist (vgl. § 121 Abs. 4 S. 2).  Höchstdauer d...

### q15 — stpo-prozess

**Query:** Was regelt § 136 StPO zur Beschuldigtenvernehmung?

**Kontext:** Belehrungspflichten, Recht auf Verteidiger

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours-api | 0.98 | 80% | 100% | 3 | 7.2s |
| azure-hybrid-exp | 0.85 | 60% | 67% | 2 | 4.9s |
| azure-semantic-exp | 0.96 | 30% | 67% | 2 | 0.9s |

#### ours-api — Top 3
- **[Judge=3]** `§ 135 OWiG – A. 2 StPO – Rn. 41` — Direkt relevant: behandelt § 136 StPO Belehrungspflichten
  > ## Abschnitt 9b Vorläufiges Berufsverbot  ## § 132a Anordnung und Aufhebung eines vorläufigen Berufsverbots nicht abgedruckt⁶⁵  ## Zehnter Abschnitt Vernehmung des Beschuldigten  ## § 133 Ladung⁶⁶ VB ...
- **[Judge=3]** `§ 399 AO – Rn. 8` — Behandelt direkt § 136 StPO Belehrungspflichten
  > 8 a) Vernehmung des Beschuldigten. Spätestens vor Abschluss der Ermittlungen ist der Beschuldigte zu vernehmen (§ 163a I 1 StPO). In einfachen Sachen genügt es, dass ihm Gelegenheit gegeben wird, sich...
- **[Judge=2]** `§ 16a StPO – ILL. für das Strafverfahren und das Bußgeldverf` — Belehrungspflichten bei Beschuldigtenvernehmung, aber nicht § 136
  > (4) Zeugen können zur Aufenthaltsermittlung ausgeschrieben werden.  (5) Für die internationale Fahndung nach Personen, einschließlich der Fahndung nach Personen im SIS und aufgrund eines Europäischen ...

#### azure-hybrid-exp — Top 3
- **[Judge=2]** `§ 16a StPO – ILL. für das Strafverfahren und das Bußgeldverf` — Behandelt Beschuldigtenvernehmung, aber nicht § 136 StPO direkt
  > (4) Zeugen können zur Aufenthaltsermittlung ausgeschrieben werden.  (5) Für die internationale Fahndung nach Personen, einschließlich der Fahndung nach Personen im SIS und aufgrund eines Europäischen ...
- **[Judge=3]** `§ 114b StPO – I. Abs – Rn. 5` — Direkt relevant zu § 136 StPO Belehrungspflichten
  > 5 II. Abs. 2 S. 1 Nr. 2–4. Hier wird die auch nach § 136 Abs. 1 S. 2, 3 und § 163a Abs. 3 S. 2, 4 vor Beginn der ersten richterlichen bzw. staatsanwaltschaftlichen o. polizeilichen Vernehmung bestehen...
- **[Judge=0]** `StPO – III. Sonstige Prozesshindernisse – Rn. 242` — Inhaltsverzeichnis ohne Regelungsinhalt zu § 136 StPO
  > Verwaltung beschlagnahmter oder gepfändeter Gegenstände 111m Herausgabe beweglicher Sachen 111n Verfahren bei der Herausgabe 111o Notveräußerung 111p Beschlagnahme von Verkörperungen eines Inhalts und...

#### azure-semantic-exp — Top 3
- **[Judge=2]** `StPO – III. Steuerstrafverfahren – Rn. 77` — Behandelt Beschuldigteneigenschaft, aber nicht § 136 direkt
  > 77 1. Tatverdacht allein begründet allerdings weder die Beschuldigteneigenschaft noch zwingt er ohne weiteres zur Einleitung v. Ermittlungen (BGHSt 64, 89 = NJW 2019, 2627 (2630)), auch nicht allein d...
- **[Judge=1]** `§ 78c StGB – AT. Fünfter Abschnitt – Rn. 7` — Erwähnt § 136 StPO nur beiläufig, behandelt Verjährung
  > 7 F. Unterbrechungshandlungen (Abs. 1 S. 1, Abs. 2). Abs. 1 S. 1 enthält einen abschließenden Katalog der Unterbrechungshandlungen (BGHSt 25, 6 (8)). Eine Analogie zu Ungunsten des Täters ist nicht zu...
- **[Judge=2]** `§ 16a StPO – ILL. für das Strafverfahren und das Bußgeldverf` — Behandelt Beschuldigtenvernehmung, aber nicht § 136 StPO direkt
  > (4) Zeugen können zur Aufenthaltsermittlung ausgeschrieben werden.  (5) Für die internationale Fahndung nach Personen, einschließlich der Fahndung nach Personen im SIS und aufgrund eines Europäischen ...

### q16 — cross-reference

**Query:** Worin unterscheidet sich Betrug von Unterschlagung?

**Kontext:** Abgrenzung § 263 vs § 246 StGB

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours-api | 0.97 | 80% | 100% | 3 | 7.2s |
| azure-hybrid-exp | 0.94 | 50% | 67% | 3 | 6.7s |
| azure-semantic-exp | 0.86 | 20% | 33% | 1 | 0.9s |

#### ours-api — Top 3
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 76` — Erläutert direkt Betrug-Abgrenzung zu anderen Delikten
  > 4. Dreiecksbetrug. Da die Getäuschte und die verfügende, nicht aber die verfügende und die geschädigte Person identisch sein müssen, ist der Tatbestand des § 263 nur erfüllt, wenn die Vermögensverfügu...
- **[Judge=3]** `§ 263 StGB – I. Vermögensbegriff  – Rn. 263` — Enthaelt vollstaendigen Wortlaut von § 263 StGB
  > 263 (1) Wer in der Absicht, sich oder einem Dritten einen rechtswidrigen Vermögensvorteil zu verschaffen, das Vermögen eines anderen dadurch beschädigt, daß er durch Vorspiegelung falscher oder durch ...
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 76` — Direkt relevant für Abgrenzung § 263 StGB
  > 76 3. Unmittelbarkeit der Verfügung. Neben der Freiwilligkeit ist das Merkmal der Unmittelbarkeit nach stRspr und hM das wichtigste Kriterium zur Beschränkung der § 263 unterfallenden Selbstschädigung...

#### azure-hybrid-exp — Top 3
- **[Judge=3]** `§ 263 StGB – I. Vermögensbegriff  – Rn. 263` — Vollständiger Betrug-Tatbestand für direkte Abgrenzung zur Unterschlagung
  > 263 (1) Wer in der Absicht, sich oder einem Dritten einen rechtswidrigen Vermögensvorteil zu verschaffen, das Vermögen eines anderen dadurch beschädigt, daß er durch Vorspiegelung falscher oder durch ...
- **[Judge=1]** `§ 246 StGB – BT. Neunzehnter Abschnitt – Rn. 20` — Unterschlagung behandelt, aber nicht Betrug-Abgrenzung
  > 20 H. Subjektiver Tatbestand. Der Vorsatz (bedingter Vorsatz genügt) besteht in dem Willen des Täters, sich oder einem Dritten rechtswidrig eine fremde,  Fischer    Diebstahl und Unterschlagung   bewe...
- **[Judge=2]** `§ 242 StGB – BT. Neunzehnter Abschnitt – Rn. 25` — Behandelt Abgrenzung Betrug/Diebstahl, nicht Betrug/Unterschlagung
  > In Fällen des Trickdiebstahls ist die Wegnahme von einer (irrtums- oder nötigungsbedingten) Vermögensverfügung und daher Diebstahl von Betrug und Erpressung abzugrenzen; §§ 242 und 253, 263 schließen ...

#### azure-semantic-exp — Top 3
- **[Judge=1]** `§ 253 StGB – BT. Zwanzigster Abschnitt – Rn. 2` — Erwähnt Betrug nur zur Abgrenzung zur Erpressung
  > 2 B. Systematik. Erpressung ist die Nötigung (§ 240) einer Person, durch die dem Vermögen der genötigten oder einer anderen (natürlichen oder juristischen) Person in der Absicht rechtswidriger Bereich...
- **[Judge=1]** `§ 248a StGB – E. Irrtum` — Behandelt Antragserfordernis, nicht Abgrenzung der Tatbestände
  > B. Anwendungsbereich. § 247 stellt, um bestimmte persönliche Beziehungen durch Eingreifen von Amts wegen nicht zu stören (BGHSt 10, 403; 18, 126; 29, 56), für Diebstahl und Unterschlagung in allen For...
- **[Judge=2]** `§ 266 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 191` — Behandelt Abgrenzung Untreue/Betrug, nicht Betrug/Unterschlagung direkt
  > Tateinheit ist möglich mit Diebstahl (Dallinger MDR 1954, 399), und zwar auch dann, wenn auch eine nicht in einem Treueverhältnis stehende Person den Diebstahl hätte begehen können (BGHSt 17, 360); mi...

### q17 — cross-reference

**Query:** Was sind die Unterschiede zwischen Diebstahl und Raub?

**Kontext:** § 242 vs § 249 StGB — Abgrenzung durch Gewalt/Drohung

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours-api | 0.96 | 100% | 100% | 3 | 6.6s |
| azure-hybrid-exp | 0.98 | 100% | 100% | 3 | 5.2s |
| azure-semantic-exp | 0.98 | 80% | 100% | 3 | 0.8s |

#### ours-api — Top 3
- **[Judge=3]** `§ 249 StGB` — Direkte Abgrenzung Raub zu Diebstahl und Erpressung
  > NStZ 2023, 351). Danach ist § 249 gegenüber § 255 ein spezielles Delikt; in jedem Raub liegt eine räuberische Erpressung (aA die hM in der Literatur). Die Unterscheidung richtet sich nach dem äußeren ...
- **[Judge=2]** `§ 252 StGB – I. Sonstige Vorschriften – Rn. 252` — Behandelt räuberischen Diebstahl, nicht direkte Abgrenzung
  > 252 Wer, bei einem Diebstahl auf frischer Tat betroffen, gegen eine Person Gewalt verübt oder Drohungen mit gegenwärtiger Gefahr für Leib oder Leben anwendet, um sich im Besitz des gestohlenen Gutes z...
- **[Judge=2]** `§ 250 StGB` — Behandelt Raub-Konkurrenzen, aber nicht direkte Abgrenzung
  > I. Rechtsfolgen. Der (einfache) Raub ist Verbrechen. Für minder schwere Fälle (vgl. → § 12 Rn. 11; → § 46 Rn. 85 ff.) gilt Abs. 2; ein solcher kann zB vorliegen, wenn das Maß der Gewalt gering ist ode...

#### azure-hybrid-exp — Top 3
- **[Judge=3]** `§ 249 StGB` — Direkt relevant: Raub-Wegnahme mit Nötigungsmitteln vs Diebstahl
  > NStZ 2023, 351). Danach ist § 249 gegenüber § 255 ein spezielles Delikt; in jedem Raub liegt eine räuberische Erpressung (aA die hM in der Literatur). Die Unterscheidung richtet sich nach dem äußeren ...
- **[Judge=3]** `§ 248c StGB – G. Konkurrenzen – Rn. 249` — Direkt relevant - zeigt Raubtatbestand mit Gewalt/Drohung
  > 249 (1) Wer mit Gewalt gegen eine Person oder unter Anwendung von Drohungen mit gegenwärtiger Gefahr für Leib oder Leben eine fremde bewegliche Sache einem anderen in der Absicht wegnimmt, die Sache s...
- **[Judge=3]** `§ 249 StGB – BT. Zwanzigster Abschnitt – Rn. 15` — Erklärt zentrale Abgrenzung: Drohung bei Raub
  > 15 Drohen setzt eine Handlung des Täters im Sinne einer ausdrücklichen oder konkludenten Gedankenäußerung voraus. Eine solche ist nicht schon dann gegeben, wenn der Täter die Furcht des Opfers vor (we...

#### azure-semantic-exp — Top 3
- **[Judge=3]** `§ 248c StGB – G. Konkurrenzen – Rn. 2` — Direkte Abgrenzung Raub-Diebstahl, systematische Stellung
  > 2 B. Systematische Stellung. Raub als selbstständiges Delikt (BGHSt 20, 235 (237 f.)) richtet sich gegen das Eigentum und die persönliche Freiheit (BGH NJW 1968, 1292). Die §§ 247, 248a sind unanwendb...
- **[Judge=3]** `§ 252 StGB – I. Sonstige Vorschriften – Rn. 252` — Behandelt direkt Abgrenzung Diebstahl-Raub durch räuberischen Diebstahl
  > 252 Wer, bei einem Diebstahl auf frischer Tat betroffen, gegen eine Person Gewalt verübt oder Drohungen mit gegenwärtiger Gefahr für Leib oder Leben anwendet, um sich im Besitz des gestohlenen Gutes z...
- **[Judge=2]** `§ 250 StGB` — Konkurrenzen zwischen Raub und Diebstahl, thematisch relevant
  > I. Rechtsfolgen. Der (einfache) Raub ist Verbrechen. Für minder schwere Fälle (vgl. → § 12 Rn. 11; → § 46 Rn. 85 ff.) gilt Abs. 2; ein solcher kann zB vorliegen, wenn das Maß der Gewalt gering ist ode...

### q18 — cross-reference

**Query:** Wann wird Betrug zu Computerbetrug und umgekehrt?

**Kontext:** § 263 vs § 263a StGB — Abgrenzung bei elektronischer Datenverarbeitung

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours-api | 0.99 | 90% | 100% | 3 | 7.9s |
| azure-hybrid-exp | 0.97 | 100% | 100% | 3 | 5.6s |
| azure-semantic-exp | 0.93 | 70% | 100% | 3 | 1.0s |

#### ours-api — Top 3
- **[Judge=3]** `§ 263a StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 23` — Direkte Abgrenzung zwischen § 263 und § 263a
  > 23 G. Subjektiver Tatbestand. Die Tat setzt (bedingten) Vorsatz voraus. Er muss sich auf alle Tatbestandsmerkmale, zu denen auch die Unbefugtheit (→ Rn. 10) gehört, dh auch auf die Voraussetzungen ers...
- **[Judge=3]** `§ 263a StGB – L. Konkurrenzen – Rn. 33` — Direkte Abgrenzung zwischen § 263 und § 263a
  > II. Verhältnis zu sonstigen Tatbeständen. § 263a und § 263 schließen sich aus, wenn derselbe Schaden sowohl durch die Manipulationsweisen des § 263a als auch durch Täuschung bewirkt wird. Mit § 263 is...
- **[Judge=3]** `§ 263a StGB – M. Sonstige Vorschriften 40 – Rn. 239` — Direkt relevante Abgrenzung zwischen § 263 und § 263a StGB
  > 239 I. Sonstige Vorschriften. FAufsicht §§ 263 Abs. 5, 68 Abs. 1. Zuständigkeit in Wirtschaftsstrafaschen § 74c Abs. 1 Nr. 6, § 74e Nr. 2 GVG iVm § 103 Abs. 2 JGG. TKÜ § 100a Abs. 2 Nr. 1 Buchst. n St...

#### azure-hybrid-exp — Top 3
- **[Judge=3]** `§ 263a StGB – M. Sonstige Vorschriften 40 – Rn. 239` — Definiert Computerbetrug § 263a vollständig, direkt relevant
  > 239 I. Sonstige Vorschriften. FAufsicht §§ 263 Abs. 5, 68 Abs. 1. Zuständigkeit in Wirtschaftsstrafaschen § 74c Abs. 1 Nr. 6, § 74e Nr. 2 GVG iVm § 103 Abs. 2 JGG. TKÜ § 100a Abs. 2 Nr. 1 Buchst. n St...
- **[Judge=2]** `§ 263 StGB – I. Vermögensbegriff  – Rn. 263` — Grundtatbestand § 263, aber keine Abgrenzung zu § 263a
  > 263 (1) Wer in der Absicht, sich oder einem Dritten einen rechtswidrigen Vermögensvorteil zu verschaffen, das Vermögen eines anderen dadurch beschädigt, daß er durch Vorspiegelung falscher oder durch ...
- **[Judge=3]** `§ 263a StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 23` — Direkte Abgrenzung zwischen § 263 und § 263a
  > 23 G. Subjektiver Tatbestand. Die Tat setzt (bedingten) Vorsatz voraus. Er muss sich auf alle Tatbestandsmerkmale, zu denen auch die Unbefugtheit (→ Rn. 10) gehört, dh auch auf die Voraussetzungen ers...

#### azure-semantic-exp — Top 3
- **[Judge=3]** `§ 263a StGB – M. Sonstige Vorschriften 40 – Rn. 239` — Direkter Gesetzestext und Struktur zu § 263a
  > 239 I. Sonstige Vorschriften. FAufsicht §§ 263 Abs. 5, 68 Abs. 1. Zuständigkeit in Wirtschaftsstrafaschen § 74c Abs. 1 Nr. 6, § 74e Nr. 2 GVG iVm § 103 Abs. 2 JGG. TKÜ § 100a Abs. 2 Nr. 1 Buchst. n St...
- **[Judge=2]** `§ 243 StGB – BT. Neunzehnter Abschnitt` — Erwähnt Computerbetrug-Abgrenzung bei Scheckkarten-Diebstahl
  > BT. Neunzehnter Abschnitt.  1979, 118); oder wenn sonst durch die Nachtat ein anderes Rechtsgut verletzt wird; in den letzteren Fällen ist Realkonkurrenz mit dem vorausgegangenen Diebstahl gegeben, se...
- **[Judge=2]** `§ 1 StGB – AT. Erster Abschnitt – Rn. 45` — Behandelt Abgrenzung Betrug/Computerbetrug bei Postpendenz
  > 45 4. Postpendenz. Als sog. Postpendenz werden Fälle bezeichnet, in denen eine nur einseitige Sachverhaltsungewissheit in dem Sinn besteht, dass von zwei Sachverhalten der zeitlich frühere möglicherwe...