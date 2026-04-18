# RAG Benchmark Report

_Generiert: 2026-04-18T14:45:40_


- Queries: **18**
- Top-K: **5**
- Systeme: openai, ours, ragie, vectara

## Gesamtvergleich

| Metrik | openai | ours | ragie | vectara |
|--------|--------|--------|--------|--------|
| nDCG@10 | 0.735 | 0.972 | 0.964 | 0.940 |
| Relevance@10 | 41.1% | 85.6% | 83.1% | 41.1% |
| Relevance@3 | 44.4% | 90.7% | 83.3% | 53.7% |
| Top-1-Score | 1.56 | 2.78 | 2.61 | 2.17 |
| Mean-Score | 1.29 | 2.49 | 2.44 | 1.44 |
| Latenz (s) | 1.73 | 5.83 | 1.92 | 1.10 |

## Nach Kategorie


### alltagssprache

| Metrik | openai | ours | ragie | vectara |
|--------|--------|--------|--------|--------|
| nDCG@10 | 0.493 | 0.993 | 0.958 | 0.879 |
| Relevance@10 | 25.0% | 100.0% | 83.8% | 25.0% |
| Relevance@3 | 25.0% | 100.0% | 83.3% | 41.7% |

### cross-reference

| Metrik | openai | ours | ragie | vectara |
|--------|--------|--------|--------|--------|
| nDCG@10 | 0.846 | 0.978 | 0.959 | 0.935 |
| Relevance@10 | 53.3% | 53.3% | 60.0% | 66.7% |
| Relevance@3 | 55.6% | 66.7% | 55.6% | 77.8% |

### exakte-paragraphen

| Metrik | openai | ours | ragie | vectara |
|--------|--------|--------|--------|--------|
| nDCG@10 | 0.905 | 0.989 | 0.947 | 0.995 |
| Relevance@10 | 45.0% | 95.0% | 75.4% | 40.0% |
| Relevance@3 | 58.3% | 100.0% | 75.0% | 58.3% |

### konzept

| Metrik | openai | ours | ragie | vectara |
|--------|--------|--------|--------|--------|
| nDCG@10 | 0.541 | 0.935 | 0.985 | 0.946 |
| Relevance@10 | 30.0% | 85.0% | 100.0% | 35.0% |
| Relevance@3 | 25.0% | 83.3% | 100.0% | 41.7% |

### stpo-prozess

| Metrik | openai | ours | ragie | vectara |
|--------|--------|--------|--------|--------|
| nDCG@10 | 0.982 | 0.968 | 0.972 | 0.944 |
| Relevance@10 | 60.0% | 86.7% | 93.3% | 46.7% |
| Relevance@3 | 66.7% | 100.0% | 100.0% | 55.6% |

## Detail pro Query


### q01 — exakte-paragraphen

**Query:** Welche Voraussetzungen hat der gewerbsmaessige Bandenbetrug nach § 263 Abs. 5 StGB?

**Kontext:** Qualifikationstatbestand des Bandenbetrugs im Fischer-Kommentar

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours | 0.99 | 100% | 100% | 3 | 5.3s |
| ragie | 1.00 | 100% | 100% | 3 | 2.0s |
| openai | 0.84 | 20% | 33% | 1 | 2.4s |
| vectara | 1.00 | 60% | 100% | 3 | 1.5s |

#### ours — Top 3
- **[Judge=3]** `§ 263 StGB – BT. Zweriindzwanzigster Abschnitt – Rn. 225` — Direkt relevant: behandelt Voraussetzungen § 263 Abs. 5
  > IV. Qualifikation (Abs. 5). Abs. 5 enthält einen Qualifikationstatbestand, der die Tat in Fällen kumulativ gewerbs- und bandenmäßiger Begehung zum Verbrechen macht. Die Qualifikation ist in die Urteil...
- **[Judge=3]** `§ 263 StGB – BT. Zweijundzwanzigster Abschnitt – Rn. 213` — Direkt relevant: behandelt Voraussetzungen des § 263 Abs. 5
  > 213 Sind beide Varianten erfüllt, ist eine Qualifikation nach Abs. 5 gegeben. Die Abgrenzung des Abs. 3 Nr. 1 zum Verbrechen nach Abs. 5 ist in Fällen bandenmäßiger Begehung schwierig, denn eine auf f...
- **[Judge=3]** `§ 263 StGB – I. Vermögensbegriff  – Rn. 263` — Enthält direkt § 263 Abs. 5 mit allen Voraussetzungen
  > 263 (1) Wer in der Absicht, sich oder einem Dritten einen rechtswidrigen Vermögensvorteil zu verschaffen, das Vermögen eines anderen dadurch beschädigt, daß er durch Vorspiegelung falscher oder durch ...

#### ragie — Top 3
- **[Judge=3]** `StGB_263_Betrug.md` — Direkt zu gewerbsmäßigem Bandenbetrug § 263 Abs. 5
  > StGB_263_Betrug.md 213 Sind beide Varianten erfüllt, ist eine Qualifikation nach Abs. 5 gegeben. Die Abgrenzung des Abs. 3 Nr. 1 zum Verbrechen nach Abs. 5 ist in Fällen bandenmäßiger Begehung schwier...
- **[Judge=3]** `StGB_Kommentar.md` — Direkt relevant: behandelt Bandenbetrug Abs. 5 Voraussetzungen
  > StGB_Kommentar.md 213 Sind beide Varianten erfüllt, ist eine Qualifikation nach Abs. 5 gegeben. Die Abgrenzung des Abs. 3 Nr. 1 zum Verbrechen nach Abs. 5 ist in Fällen bandenmäßiger Begehung schwieri...
- **[Judge=3]** `StGB_263_Betrug.md` — Direkt relevante Voraussetzungen für gewerbsmäßigen Bandenbetrug
  > StGB_263_Betrug.md 212 Der Begriff der Urkundenfälschung ist weit zu fassen; er umfasst neben Taten nach § 267 auch solche nach §§ 268–281 (LK-StGB/Kubiciel/Tiedemann Rn. 297; NK-StGB/Kindhäuser/Hoven...

#### openai — Top 3
- **[Judge=1]** `analyses_findings.md` — Erwähnt Bandenbetrug, aber behandelt Schadensberechnung statt Tatbestandsvoraussetzungen
  > **Zusammenhang im Detail:**  1. **Kein Verkaufsverbot** → Die Angeklagten durften darauf vertrauen, dass ihre Produkte legal sind → **Kein Vorsatz** (§ 16 StGB) oder zumindest **Verbotsirrtum** (§ 17 ...
- **[Judge=3]** `StGB_Kommentar.md` — Behandelt direkt § 263 Abs. 5 Bandenbetrug-Voraussetzungen
  > 212 Der Begriff der Urkundenfälschung ist weit zu fassen; er umfasst neben Taten nach § 267 auch solche nach §§ 268–281 (LK-StGB/Kubiciel/Tiedemann Rn. 297; NK-StGB/Kindhäuser/Hoven Rn. 392). Entsprec...
- **[Judge=1]** `Probenheld-KOMPLETT.md` — Praxisfall Bandenbetrug, aber keine Voraussetzungen erläutert
  > Das Projekt "Probenheld" war im Partnerprogramm und wurde von VERIPAY BV in HEERLEN (NL) betrieben und hierüber wurden die Bestellungen im Rahmen des Partnerprogramms "Platinum-Partner" über mehr als ...

#### vectara — Top 3
- **[Judge=3]** `['Übersicht']` — Direkt relevant für gewerbsmäßigen Bandenbetrug § 263 Abs. 5
  > § 263 ist unter den Voraussetzungen von Abs....
- **[Judge=2]** `['Neunzehnter Abschnitt. Diebstahl und Unterschlagun...']` — Erwähnt Bandenbetrug § 263 Abs., aber keine Voraussetzungen
  > dazu BGHSt 47, 214 (216)); StraFo 2007, 78 (78 f.); NStZ 2002, 375 (377); 2007, 288 (289); 2008, 54 (Bandenbetrug; § 263 Abs....
- **[Judge=2]** `['Übersicht']` — Paragraphenverweis relevant, aber unvollständiger Textauszug
  > 3 Nr. 5), weiterhin § 263 Abs....

### q02 — exakte-paragraphen

**Query:** Was regelt § 112 StPO zur Untersuchungshaft?

**Kontext:** Anordnungsvoraussetzungen der U-Haft (dringender Tatverdacht, Haftgrund) im Schmitt/Koehler

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours | 0.99 | 100% | 100% | 3 | 8.9s |
| ragie | 0.98 | 75% | 67% | 3 | 1.8s |
| openai | 1.00 | 80% | 100% | 3 | 1.6s |
| vectara | 0.98 | 60% | 67% | 3 | 1.3s |

#### ours — Top 3
- **[Judge=3]** `§ 112 StPO – Rn. 112` — Direkter Gesetzestext zu § 112 StPO Untersuchungshaft
  > 112 (1) ¹ Die Untersuchungshaft darf gegen den Beschuldigten angeordnet werden, wenn er der Tat dringend verdächtig ist und ein Haftgrund besteht. ² Sie darf nicht angeordnet werden, wenn sie zu der B...
- **[Judge=3]** `§ 112 StPO – Rn. 112` — Erklärt zentrale Voraussetzungen der Untersuchungshaft nach § 112
  > Haftunfähigkeit des Beschuldigten schließt den Erlass des Haftbefehls nicht aus, sondern hindert nur seinen Vollzug (OLG Düsseldorf JZ 1984, 248; OLG Frankfurt a.M. NJW 1968, 2302; OLG Nürnberg OLGSt ...
- **[Judge=3]** `§ 112 StPO – III. Flucht (Abs – Rn. 23` — Erklärt § 112 StPO Haftgründe direkt relevant
  > Bei einer besonders hohen Straferwartung braucht daher nur geprüft zu werden, ob Umstände vorhanden sind, die die hieraus herzuleitende Fluchtgefahr ausräumen können (KG StV 1996, 383; OLG München Str...

#### ragie — Top 3
- **[Judge=3]** `Strafprozessordnung.md` — Direkt relevant: § 112 StPO Anordnungsvoraussetzungen U-Haft
  > Strafprozessordnung.md Werden mehrere Haftbefehle in verschiedenen Sachen erlassen, so kann nur einer v. ihnen vollzogen werden. Eine „Doppelhaft“ ist ausgeschlossen (Münchhalffen/Gatzweiler Untersuch...
- **[Judge=3]** `Strafprozessordnung.md` — Behandelt direkt § 112 StPO Anordnungsvoraussetzungen
  > Strafprozessordnung.md a) der dringende Tatverdacht, b) der Haftgrund  ergeben.  ---  ## Seite 2435  Anh. 3 RiStBV  RL für das Strafverfahren und das Bußgeldverfahren  (2) Wenn die Anwendung des § 112...
- **[Judge=1]** `Strafprozessordnung.md` — Jugendstrafrecht, nicht allgemeine StPO § 112
  > Strafprozessordnung.md § 72 Untersuchungshaft. (1) ¹ Untersuchungshaft darf nur verhängt und vollstreckt werden, wenn ihr Zweck nicht durch eine vorläufige Anordnung über die Erziehung oder durch ande...

#### openai — Top 3
- **[Judge=3]** `Strafprozessordnung.md` — Direkt relevant: § 112 StPO Untersuchungshaft-Voraussetzungen
  > Schmitt  ---  ## Seite 722  StPO § 112  Erstes Buch. Neunter Abschnitt  wenn Überhaft notiert ist, weil der Beschuldigte sich noch in anderer Sache in Strafhaft befindet. Zur Haftbeschwerde bei Überha...
- **[Judge=3]** `Strafprozessordnung.md` — Direkt relevant: behandelt § 112 StPO Untersuchungshaftvoraussetzungen
  > 3, Abs. 2 schließt auch aus, den auf § 112 gestützten Haftbefehl hilfsweise auf den Haftgrund der Wiederholungsgefahr zu stützen; denn auch dann handelt es sich um eine Anwendung dieses Haftgrundes (L...
- **[Judge=3]** `Strafprozessordnung.md` — Direkt relevant: behandelt § 112 StPO Anordnungsvoraussetzungen
  > # 7. Untersuchungshaft, einstweilige Unterbringung und sonstige Maßnahmen zur Sicherstellung der Strafverfolgung und der Strafvollstreckung  46. Begründung der Anträge in Haftsachen. (1) Der Staatsanw...

#### vectara — Top 3
- **[Judge=3]** `['Notveräußerung']` — Direkter Bezug zu § 112 StPO Untersuchungshaft
  > StPO § 112 Erstes Buch....
- **[Judge=3]** `['Notveräußerung']` — Direkt relevant - § 112 StPO regelt Untersuchungshaft
  > StPO § 112 Erstes Buch....
- **[Judge=1]** `['Übersicht']` — Nachbarparagraph, behandelt Haftlockerung statt Anordnungsvoraussetzungen
  > Verhaftung und vorläufige Festnahme § 116b StPO ckung von Untersuchungshaft vor, es sei denn, das Gericht trifft eine abweichende Entscheidung, weil der Zweck der Untersuchungshaft dies erfordert....

### q03 — exakte-paragraphen

**Query:** Welche Haftgruende nennt § 112 Abs. 2 StPO?

**Kontext:** Fluchtgefahr, Verdunkelungsgefahr, Flucht — im StPO-Kommentar

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours | 0.99 | 100% | 100% | 3 | 5.0s |
| ragie | 0.97 | 67% | 67% | 2 | 1.8s |
| openai | 1.00 | 40% | 67% | 3 | 1.5s |
| vectara | 1.00 | 0% | 0% | 1 | 1.1s |

#### ours — Top 3
- **[Judge=3]** `§ 112 StPO – Rn. 112` — Listet vollständig alle Haftgründe des § 112 Abs. 2 StPO
  > 112 (1) ¹ Die Untersuchungshaft darf gegen den Beschuldigten angeordnet werden, wenn er der Tat dringend verdächtig ist und ein Haftgrund besteht. ² Sie darf nicht angeordnet werden, wenn sie zu der B...
- **[Judge=3]** `§ 112 StPO – III. Flucht (Abs – Rn. 23` — Behandelt direkt Haftgruende nach § 112 Abs. 2 StPO
  > Bei einer besonders hohen Straferwartung braucht daher nur geprüft zu werden, ob Umstände vorhanden sind, die die hieraus herzuleitende Fluchtgefahr ausräumen können (KG StV 1996, 383; OLG München Str...
- **[Judge=2]** `§ 112 StPO – III. Flucht (Abs – Rn. 32 (Teil 2)` — Behandelt Verdunkelungsgefahr als einen der Haftgruende detailliert
  > Wenn die Verdunkelungshandlungen nicht geeignet sind, die Ermittlung der Wahrheit zu erschweren, darf UHaft nicht angeordnet werden. Der Haftgrund liegt daher nicht vor, wenn der Sachverhalt schon in ...

#### ragie — Top 3
- **[Judge=2]** `Strafprozessordnung.md` — Behandelt Haftgruende, aber fokussiert auf Abs. 3
  > Strafprozessordnung.md 38 Die Vorschr. begründet bei dieser Auslegung weder eine Vermutung der Haftgründe (aM OLG Düsseldorf MDR 1983, 152; offenbar auch OLG Bremen StV 1983, 288), noch findet eine „U...
- **[Judge=1]** `Strafprozessordnung.md` — Erwähnt § 112 Abs. 2 StPO, keine konkreten Haftgründe
  > Strafprozessordnung.md (3) ¹ Hinsichtlich der Möglichkeit und gegebenenfalls Pflicht zur Aufzeichnung der Vernehmung des Beschuldigten in Bild und Ton sind § 136 Absatz 4 StPO bzw. § 70c Absatz 2 Satz...
- **[Judge=2]** `Strafprozessordnung.md` — Thematisch relevant, behandelt Haftgründe aber nicht § 112 Abs. 2
  > Strafprozessordnung.md Soweit die Staatssicherheit gefährdet wurde, kann v. der Begründung des dringenden Tatverdachts abgesehen werden (dazu Creifelds NJW 1965, 949); das muss in dem Haftbefehl zum A...

#### openai — Top 3
- **[Judge=3]** `Strafprozessordnung.md` — Beantwortet die Frage zu § 112 Abs. 2 StPO direkt
  > 1 A. Einschränkung der UHaft. Eine Einschränkung der UHaft bei Straftaten mit geringer Strafandrohung bestimmt die Vorschrift. Ihr ist zu entnehmen, dass UHaft auch angeordnet werden darf, wenn nur ei...
- **[Judge=2]** `Strafprozessordnung.md` — Behandelt Verdunkelungsgefahr, nicht alle Haftgruende des § 112 Abs. 2
  > 33).  30 Es genügt, dass andere Beweisanzeichen für die Verdunkelungsgefahr vorhanden sind, zB die frühere Verurteilung des Beschuldigten wegen Meineids o. Vortäuschung einer Straftat (Dahs NJW 1965, ...
- **[Judge=1]** `Strafprozessordnung.md` — Erwähnt Haftgründe, aber nennt sie nicht konkret
  > # 7. Untersuchungshaft, einstweilige Unterbringung und sonstige Maßnahmen zur Sicherstellung der Strafverfolgung und der Strafvollstreckung  46. Begründung der Anträge in Haftsachen. (1) Der Staatsanw...

#### vectara — Top 3
- **[Judge=1]** `['Vorbemerkung zu §§ 211–217']` — Nur Paragraphenverweis, keine inhaltlichen Haftgruende genannt
  > 2 Nr. 1 Buchst. h StPO; UHaft § 112 Abs....
- **[Judge=1]** `['7. Untersuchungshaft, einstweilige Unterbringung u...']` — Erwähnt § 112 Abs. 2, aber keine Aufzählung
  > (4) Besteht in den Fällen des § 112 Absatz 3 und des § 112a Absatz 1 StPO auch ein Haftgrund nach § 112 Absatz 2 StPO, sind die Feststellungen hierüber aktenkundig zu machen....
- **[Judge=1]** `['Verfahren bei der Haftprüfung']` — Erwähnt § 112 aber nicht die konkreten Haftgründe
  > 17) auch auf einen Haftgrund nach § 112 gestützt, so findet § 122a keine Anwendung (KK-StPO/Gericke Rn....

### q04 — exakte-paragraphen

**Query:** Was regelt § 102 StPO zur Durchsuchung beim Beschuldigten?

**Kontext:** Durchsuchungsvoraussetzungen beim Verdaechtigen

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours | 0.97 | 80% | 100% | 3 | 5.7s |
| ragie | 0.84 | 60% | 67% | 1 | 1.8s |
| openai | 0.78 | 40% | 33% | 1 | 1.6s |
| vectara | 1.00 | 40% | 67% | 3 | 1.3s |

#### ours — Top 3
- **[Judge=3]** `§ 102 StPO – Rn. 102` — Behandelt direkt § 102 StPO Durchsuchungsregelungen
  > 102 Bei dem, welcher als Täter oder Teilnehmer einer Straftat oder der Datenhehlerei, Begünstigung, Strafvereitelung oder Hehlerei  Köhler    Ermittlungsmaßnahmen  verdächtig ist, kann eine Durchsuchu...
- **[Judge=2]** `§ 102 StPO – Rn. 10` — Behandelt Durchsuchungsvoraussetzungen, aber nicht spezifisch § 102
  > II. Auffinden von Beweismitteln. Zu den Beweismitteln (→ § 94 Rn. 4 ff.) gehören auch die nur in § 103 erwähnten Spuren (SK-StPO/Jäger/Wohlers Rn. 21) u. Personen, die zu Beweiszwecken in Augenschein ...
- **[Judge=3]** `§ 102 StPO – Rn. 10` — Erläutert direkt § 102 StPO Durchsuchungsgegenstand Sachen
  > 10 III. Sachen. Sachen sind Kleidungsstücke, die der Verdächtige bei sich führt, ohne sie zu tragen, u. seine sonstige bewegliche Habe, gleichgültig, ob sie sich in seinem Umkreis, zB in Gepäckstücken...

#### ragie — Top 3
- **[Judge=1]** `Strafprozessordnung.md` — Behandelt § 103 StPO, nicht direkt § 102
  > Strafprozessordnung.md 3 B. Durchsuchungsgegenstände. Durchsuchungsgegenstände können die Wohnung u. Räume des Unverdächtigen (→ § 102 Rn. 7) sowie seine Person (→ § 102 Rn. 9) u. die ihm gehörenden S...
- **[Judge=3]** `Strafprozessordnung.md` — Direkter Gesetzestext und vollstaendige Durchsuchungsregelung
  > Strafprozessordnung.md Durchsuchung bei Beschuldigten RiStBV 73a  102 Bei dem, welcher als Täter oder Teilnehmer einer Straftat oder der Datenhehlerei, Begünstigung, Strafvereitelung oder Hehlerei  Kö...
- **[Judge=3]** `Strafprozessordnung.md` — Direkter Volltext zu § 102 StPO Durchsuchungsregelung
  > Strafprozessordnung.md 102 Bei dem, welcher als Täter oder Teilnehmer einer Straftat oder der Datenhehlerei, Begünstigung, Strafvereitelung oder Hehlerei  Köhler  ---  ## Seite 613  Ermittlungsmaßnahm...

#### openai — Top 3
- **[Judge=1]** `Strafprozessordnung.md` — Behandelt § 103 StPO, nicht § 102 StPO
  > 14 III. Durchsuchungszweck. Durchsuchungszweck darf nur die Ergreifung des Beschuldigten sein, nicht die Auffindung v. Spuren u. Beweismitteln. Werben für eine terroristische Vereinigung o. deren geri...
- **[Judge=2]** `Strafprozessordnung.md` — Behandelt § 103 StPO, vergleicht mit § 102
  > Rn. 76). Wie im Fall des § 102 (→ § 102 Rn. 12) steht dem Beschuldigten der rkr. Verurteilte gleich. Anders als dort (→ § 102 Rn. 2) ist die Durchsuchung aber nur zulässig, wenn aus aufgrund Zeugenbek...
- **[Judge=1]** `Strafprozessordnung.md` — Behandelt § 103 StPO, nicht § 102
  > Die Pflicht zur Herausgabe amtlich verwahrter Akten u. Unterlagen darf mit Blick auf § 96 nicht nach § 103 erzwungen werden (→ § 96 Rn. 2). Um der Behörde die Prüfung der Abgabe einer Sperrerklarung n...

#### vectara — Top 3
- **[Judge=3]** `['Übersicht']` — Direkt relevant: behandelt § 102 StPO Durchsuchung
  > 27); denn nach § 102 ist sogar die Durchsuchung zum Zweck der Ergreifung zulässig (→ § 102 Rn....
- **[Judge=3]** `['Durchsuchung bei anderen Personen']` — Behandelt direkt § 102 StPO zur Durchsuchung
  > 2 stattfindet. Wenn dadurch der Untersuchungserfolg nicht gefährdet wird, sollte der Durchsuchungszweck auch im Fall des § 102 dem Verdächtigen bekanntgegeben werden (KK-StPO/Henrichs/Weingast Rn....
- **[Judge=1]** `['Entschädigung für andere Strafverfolgungsmaßnahmen...']` — Erwähnt § 102 StPO, aber erklärt ihn nicht
  > Durchsuchung iS Nr. 4 ist nur die nach §§ 102, 103 StPO, nicht die nach § 111 StPO (Meyer StrEG Rn....

### q05 — konzept

**Query:** Wann liegt eine konkludente Taeuschung im Sinne des § 263 StGB vor?

**Kontext:** Taeuschungshandlung durch schluessiges Verhalten

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours | 0.81 | 80% | 67% | 1 | 4.5s |
| ragie | 0.97 | 100% | 100% | 3 | 1.8s |
| openai | 0.92 | 60% | 67% | 3 | 1.5s |
| vectara | 0.95 | 20% | 33% | 3 | 1.2s |

#### ours — Top 3
- **[Judge=1]** `§ 263 StGB – I. Vermögensbegriff  – Rn. 263` — Gesetzestext ohne konkludente Täuschung spezifiziert
  > 263 (1) Wer in der Absicht, sich oder einem Dritten einen rechtswidrigen Vermögensvorteil zu verschaffen, das Vermögen eines anderen dadurch beschädigt, daß er durch Vorspiegelung falscher oder durch ...
- **[Judge=2]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 263 (Tei` — Literaturliste zu Betrug, aber ohne konkreten Inhalt
  > Heghmanns, Strafbarkeit des „Phishing“ von Bankkontendaten und ihrer Verwertung, wistra 2007, 167; Hilgendorf, Tatsachenaussagen u. Werturteile im Strafrecht, 1998; Hillenkamp, Zum Schutz „deliktische...
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 21` — Direkt zur konkludenten Taeuschung bei § 263
  > 21 2. Konkludente Erklärungen. Auch durch eine schlüssige Handlung (konkludente Erklärung) kann vorspiegelt werden. Eine solche konkludente Erklärung durch aktives Tun ist von einer Erklärung durch Un...

#### ragie — Top 3
- **[Judge=3]** `StGB_263_Betrug.md` — Direkte Antwort zur konkludenten Taeuschung § 263
  > StGB_263_Betrug.md 21 2. Konkludente Erklärungen. Auch durch eine schlüssige Handlung (konkludente Erklärung) kann vorspiegelt werden. Eine solche konkludente Erklärung durch aktives Tun ist von einer...
- **[Judge=2]** `StGB_Kommentar.md` — Behandelt konkludente Täuschung, aber bei Scheck-/Kreditkarten
  > StGB_Kommentar.md E. Vollendung, Versuch. Die Tat ist mit dem Eintritt des Schadens vollendet und idR auch beendet iSv § 78a. Der Versuch ist nicht strafbar. Die (vom Gesetzgeber des 2. WiKG verworfen...
- **[Judge=3]** `StGB_263_Betrug.md` — Beantwortet direkt konkludente Taeuschung bei § 263 StGB
  > StGB_263_Betrug.md 22 Sowohl ausdrücklichen Erklärungen als auch tatsächlichen Handeln kann ein konkludenter Erklärungswert zukommen. Aus der bloßen Feststellung eines Irrtums kann aber nicht schon au...

#### openai — Top 3
- **[Judge=3]** `StGB_Kommentar.md` — Direkt relevant: behandelt konkludente Taeuschung bei § 263
  > Es kann im Einzelfall auch mit Aussagen zu wahren Tatsachen (nicht: über solche) getäuscht werden, wenn der Täter es darauf anlegt, gerade hierdurch Missverständnis und Irrtum hinsichtl. anderer Tatsa...
- **[Judge=2]** `StGB_Kommentar.md` — Behandelt konkludente Täuschung bei Kartenmissbrauch, § 263 relevant
  > F. Täterschaft und Teilnahme. Die Tat ist ein Sonderdelikt (BT-Drs. 10/5058, 32; NStZ 1992, 279; OLG Stuttgart NJW 1988, 981 (981 f.)); für Teilnehmer gilt § 28 Abs. 1 (hM; aA TK-StGB/Perron Rn. 13). ...
- **[Judge=0]** `StGB_Kommentar.md` — Behandelt Scheckkartenmissbrauch, nicht konkludente Taeuschung allgemein
  > Ein Irrtum wird sich – trotz der verbreiteten Praxis von Banken, Überziehungen weit über einen alsbald rückführbaren Rahmen hinaus zu dulden und den Kontoausgleich durch Ratenkreditverträge anzubieten...

#### vectara — Top 3
- **[Judge=3]** `['Übersicht']` — Direkt relevant: konkludente Taeuschung bei Betrug
  > 12a f.). Bei kollusivem Zusammenwirken zwischen Karteninhaber und Zahlungsannehmer (Vertragsunternehmen) liegt idR eine (konkludente) Täuschung des Ausstellers über die Voraussetzungen der Zahlungspfl...
- **[Judge=0]** `['Vorführung einer aufgezeichneten Zeugenvernehmung']` — Betäubungsmittel/Waffen, nicht Betrug/Täuschung
  > Tateinheit u. eine Tat im prozessualen Sinne liegt etwa bei Zusammen treffen v. Betäubungsmitteldelikten und Verstößen nach dem WaffG vor, Schmitt 1467 ***...
- **[Judge=1]** `['Übersicht']` — Erwähnt § 263, aber keine konkludente Täuschung
  > → § 263 Rn. 193). Liegt auch Betrugsvorsatz vor, geht § 263 vor (→ Rn....

### q06 — konzept

**Query:** Was ist eine Vermoegensverfuegung und welche Anforderungen stellt die Rechtsprechung?

**Kontext:** Tatbestandsmerkmal der Vermoegensverfuegung beim Betrug

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours | 0.94 | 80% | 67% | 3 | 6.3s |
| ragie | 1.00 | 100% | 100% | 3 | 2.0s |
| openai | 0.43 | 0% | 0% | 0 | 1.4s |
| vectara | 1.00 | 0% | 0% | 1 | 1.0s |

#### ours — Top 3
- **[Judge=3]** `§ 263 StGB – BT. Zweitundzwanzigster Abschnitt – Rn. 69` — Definiert Vermoegensverfuegung als ungeschriebenes Tatbestandsmerkmal direkt
  > 69 Anders ist es, wenn der Verfügende seinerseits nur (gutgläubige) Hilfsperson eines bösgläubigen Dritten ist. Hier ist auf den Irrtum des Entscheidungsbefugten abzustellen: Erkennt dieser die Unrich...
- **[Judge=1]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 87` — Kausalität bei Verfügungen, nicht Definition der Vermögensverfügung
  > 87 5. Kausalität. Für die Vermögensverfügung muss der täuschungsbedingte Irrtum kausal sein (vgl. BGHSt 24, 257 (260); 24, 386 (389); NStZ 2003, 313 (314 f.); OLG Düsseldorf NJW 1987, 3145); Mitverurs...
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 76` — Erklaert direkt Vermoegensverfuegung und deren Zurechnung
  > 4. Dreiecksbetrug. Da die Getäuschte und die verfügende, nicht aber die verfügende und die geschädigte Person identisch sein müssen, ist der Tatbestand des § 263 nur erfüllt, wenn die Vermögensverfügu...

#### ragie — Top 3
- **[Judge=3]** `StGB_Kommentar.md` — Definiert Vermoegensverfuegung mit konkreten Rechtsprechungsbeispielen direkt
  > StGB_Kommentar.md a) Einzelfälle. Als Verfügungen sind zB angesehen worden: Veranlassung oder Vornahme einer Überweisung (wistra 1987, 257; NStZ 1999, 558); Herausgabe fremder Sachen: Bewilligung von ...
- **[Judge=3]** `StGB_Kommentar.md` — Direkte Definition und Anforderungen der Vermoegensverfuegung
  > StGB_Kommentar.md 1. Verfügungshandlung. Die Anzahl möglicher vermögensmindernder Handlungen ist grds. unbeschränkt; sie sind meist den Fallgruppen des Eingehens oder des Erfüllens einer Verbindlichke...

#### openai — Top 3
- **[Judge=0]** `StGB_Kommentar.md` — Behandelt Schuldunfaehigkeit, nicht Vermoegensverfuegung beim Betrug
  > (77); 49, 45 (53); NStZ-RR 2010, 73; 2023, 72 stRspr). Auf die Rechtsfrage, ob eine (festgestellte; vgl. → § 20 Rn. 44a) Störung erheblich ist, ist daher auch der Zweifelssatz im Grundsatz nicht anwen...
- **[Judge=0]** `StGB_Kommentar.md` — Behandelt Schuldminderung bei psychischen Störungen, nicht Vermögensverfügung
  > 9; → § 20 Rn. 46b). Dabei ist die Beziehung zwischen Entstehungsgeschichte, Motivation und Verlauf der Tat und den konkreten Auswirkungen der psychischen Störung zu betrachten; einzubeziehen ist auch ...
- **[Judge=0]** `StGB_Kommentar.md` — Behandelt Sexualstraftaten, nicht Vermoegensverfuegung beim Betrug
  > Nicht vorausgesetzt ist auch, dass die Sexualstraftat gerade gegen diejenige Person begangen wird, die von der Gruppe „bedrängt“ wird. Vielmehr ist auch die Möglichkeit umfasst, dass die Tat nach § 17...

#### vectara — Top 3
- **[Judge=1]** `['Übersicht']` — Allgemeine Anforderungen, nicht spezifisch Vermoegensverfuegung
  > Maßgeblich sind die Anforderungen, welche die Rechtsordnung an jedermann stellt (BGHSt 43, 66 (77); NStZ-RR 1999, 295 (296); 2015, 137 (138))....
- **[Judge=0]** `['Vorführung bei vorläufiger Festnahme']` — Verfahrensrecht Aufklaerungsruege, nicht Betrug Vermoegensverfuegung
  > Gerichtsbeschlusses vortragen; denn an die Aufklärungsrüge können nicht geringere Anforderungen gestellt werden als an die Rüge fehlerhafter Ablehnung eines Beweisantrags (BGH NStZ 1984, 329; 2015, 54...
- **[Judge=0]** `['Übersicht']` — Behandelt Einwilligung, nicht Vermoegensverfuegung beim Betrug
  > 1 S. 2). Damit die Einwilligung rechtswirksam ist, muss ihr eine Belehrung vorausgehen, welche den Anforderungen des Abs....

### q07 — konzept

**Query:** Was versteht man unter einem Gefaehrdungsschaden beim Betrug?

**Kontext:** Schadensbegriff, schadensgleiche Vermoegensgefaehrdung

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours | 0.99 | 80% | 100% | 3 | 4.7s |
| ragie | 1.00 | 100% | 100% | 3 | 2.9s |
| openai | 0.00 | 0% | 0% | 0 | 1.8s |
| vectara | 1.00 | 80% | 100% | 3 | 1.0s |

#### ours — Top 3
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 159` — Definiert Gefährdungsschaden beim Betrug vollständig
  > 159 b) Voraussetzungen. aa) Ein Gefährdungsschaden ist gegeben, wenn die Wahrscheinlichkeit des endgültigen Verlusts eines Vermögensbestandteils zum Zeitpunkt der täuschungsbedingten Verfügung so groß...
- **[Judge=3]** `§ 263 StGB – BT. Zwei undzwanzigster Abschnitt – Rn. 263 (Te` — Direkt relevant: Gefährdungsschaden bei Betrug explizit behandelt
  > Fischer/Lutz    Betrug und Untreue   rechts für das Strafrecht, FS Weber, 2004, 271; Eisele/Bechtel, Der Schadensbegriff bei den Vermögensdelikten, JuS 2018, 97; Ellbogen/Wichmann, Zu Problemen des är...
- **[Judge=2]** `§ 263 StGB – BT. Zwei undzwanzigster Abschnitt – Rn. 263` — Thematisch relevant: Betrugsschadensmerkmal, aber nur Literaturverweise
  > **Rechtsprechungsübersicht:** Scholz, Die Entwicklung des Berufs- und Vertragsarztrechts, medstra 2019, 331; 2021, 349; 2022, 355; 2023, 355; 2024, 351.  Weinrich/Wostry, Der Abrechnungsbetrug in der ...

#### ragie — Top 3
- **[Judge=3]** `StGB_263_Betrug.md` — Direkte Definition und Voraussetzungen des Gefaehrdungsschadens
  > StGB_263_Betrug.md 159 b) Voraussetzungen. aa) Ein Gefährdungsschaden ist gegeben, wenn die Wahrscheinlichkeit des endgültigen Verlusts eines Vermögensbestandteils zum Zeitpunkt der täuschungsbedingte...
- **[Judge=3]** `StGB_263_Betrug.md` — Direkt relevant: Definition und Voraussetzungen des Gefaehrdungsschadens
  > StGB_263_Betrug.md 158 Der 3. StS hat in BGHSt 54, 69 (122 ff.) (Anm. Joecks wistra 2010, 179; vgl. → Rn. 8; → Rn. 176) sowohl der Sache nach als auch begrifflich am „Gefährdungsschaden“ festgehalten ...
- **[Judge=3]** `StGB_Kommentar.md` — Direkt relevant: definiert und erklaert Gefaehrdungsschaden beim Betrug
  > StGB_Kommentar.md Die täuschungsbedingte Herausgabe von EC-Karten, Kreditkarten und weiteren Zugangsdaten zu Bank-Guthaben (PINs, TANs; Passwörter), sei es infolge persönlicher Täuschung oder von „Phi...

#### openai — Top 3
- **[Judge=0]** `StGB_Kommentar.md` — Behandelt Täterschaft/Teilnahme, nicht Betrugsschaden
  > Die Abgrenzung hängt nach der Rspr. davon ab, ob das betreffende Merkmal im Schwergewicht die Tat oder die Persönlichkeit des Täters kennzeichnet. Umstände, die eine besondere Gefährlichkeit des Täter...
- **[Judge=0]** `StGB_Kommentar.md` — Text behandelt Schuldfaehigkeit, nicht Betrug oder Gefaehrdungsschaden
  > 29 f.). Die als Kriterien eines Vorverschuldens herangezogenen Umstände sind durchweg solche, die in anderem Gewand schon auf der tatsächlichen Ebene gegen die Feststellung einer („tiefgreifenden“) Be...
- **[Judge=0]** `Probenheld-KOMPLETT.md` — Praktische Faelle, keine Schadensbegriff-Definition
  > Ich bin allerdings letztes Jahr mal angerufen worden. Wie diese Firma hieß, weiß ich nicht. Da hat man mir eine Mastercard in Verbindung mit einem Sofortkredit angeboten. Ich habe da aber ausdrücklich...

#### vectara — Top 3
- **[Judge=3]** `['Zweiundzwanzigster Abschnitt. Betrug und Untreue']` — Direkt relevant: definiert Gefährdungsschaden beim Betrug
  > einen vollendeten Betrug durch Entstehen eines Gefährdungsschadens an, wenn aufgrund tauschender Erklärungen dem Täter ein Überziehungskredit eingeräumt oder Karten mit Einlösungsgarantie ausgehändigt...
- **[Judge=3]** `['Zweiundzwanzigster Abschnitt. Betrug und Untreue']` — Definiert direkt den gesuchten Gefaehrdungsschaden-Begriff
  > Vollendung. Vollendet ist der Betrug mit dem zumindest teilweisen Eintritt des Vermögensschadens (auch als Gefährdungsschaden iSv → Rn....
- **[Judge=3]** `['Zweiundzwanzigster Abschnitt. Betrug und Untreue']` — Erklaert Gefaehrdungsschaden bei Betrug direkt
  > StS entschieden, der Vollendung eines (Eingehungs-)Betrugs stehe auch bei täuschendem Abschluss von Lebensversicherungen (zur Geldbeschaffung durch Vortäuschung des Versicherungsfalls) nicht entgegen,...

### q08 — konzept

**Query:** Wie wird der Vorsatz beim Betrug bestimmt, insbesondere die Bereicherungsabsicht?

**Kontext:** Subjektiver Tatbestand § 263 StGB

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours | 1.00 | 100% | 100% | 3 | 6.3s |
| ragie | 0.97 | 100% | 100% | 3 | 2.1s |
| openai | 0.81 | 60% | 33% | 1 | 1.8s |
| vectara | 0.83 | 40% | 33% | 1 | 1.0s |

#### ours — Top 3
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 176` — Direkt relevant: behandelt Vorsatz und Bereicherungsabsicht bei Betrug
  > D. Subjektiver Tatbestand. § 263 setzt Vorsatz voraus; darüber hinaus ist die Absicht rechtswidriger Bereicherung erforderlich.   I. Vorsatz. 1. Täuschungsvorsatz. Der Vorsatz (bedingter Vorsatz genüg...
- **[Judge=3]** `§ 263 StGB – I. Sonstige Vorschriften 239 – Rn. 263 (Teil 1)` — Direkt relevant: behandelt Bereicherungsabsicht beim subjektiven Tatbestand
  > 3. Einzelne Fallgruppen ... 92 4. Rechtlich missbilligte, sittenwidrige und gesetzeswidrige wirtschaftliche Werte ... 101 VI. Schaden ... 110 1. Grundsätze der Schadensermittlung ... 111 2. Vermögensm...
- **[Judge=3]** `§ 263 StGB – BT. Zweijundzwanzigster Abschnitt – Rn. 187` — Direkt zur Bereicherungsabsicht beim Betrug relevant
  > 2. Absicht. Es muss dem Täter darauf ankommen, sich oder einem Dritten einen Vermögensvorteil zu verschaffen. Motiv oder letzter Zweck muss dies nicht sein (BGHSt 4, 107; 16. 1; BGHR § 263 I Täusch. 9...

#### ragie — Top 3
- **[Judge=3]** `StGB_263_Betrug.md` — Direkt relevant: definiert Bereicherungsabsicht bei Betrug
  > StGB_263_Betrug.md 183–185 Diese Rspr. setzt einerseits konkrete Gefährdung und (endgültigen) Schadens- erfolg gleich (vgl. BGHSt 48, 331 (347)); andererseits sieht sie die Kenntnis der Gefahr nur als...
- **[Judge=2]** `StGB_Kommentar.md` — Erwähnt Bereicherungsabsicht beim Betrug als subjektives Element
  > StGB_Kommentar.md II. Tatbestandsmerkmale unechten Unterlassens. Für unechte Unterlassungsdelikte hat der GrSen (BGHSt 16, 155) entschieden, dass nur die Umstände, welche die Rechtspflicht begründen (...
- **[Judge=3]** `StGB_263_Betrug.md` — Direkt relevant: behandelt Vorsatz und Bereicherungsabsicht bei Betrug
  > StGB_263_Betrug.md D. Subjektiver Tatbestand. § 263 setzt Vorsatz voraus; darüber hinaus ist die Absicht rechtswidriger Bereicherung erforderlich.  179  I. Vorsatz. 1. Täuschungsvorsatz. Der Vorsatz (...

#### openai — Top 3
- **[Judge=1]** `StGB_Kommentar.md` — Behandelt Bereicherungsabsicht bei Erpressung, nicht Betrug
  > 36 I. Vorsatz. Für die Nötigung gilt das in → § 240 Rn. 53 ff. Gesagte, auch bezüglich der Kenntnis der Empfindlichkeit des Übels und der Rechtswidrigkeit der Tat.  37 II. Bereicherungsabsicht. Der Tä...
- **[Judge=3]** `StGB_Kommentar.md` — Behandelt direkt Bereicherungsabsicht beim Betrug
  > Erforderlich ist weiterhin der Vorsatz, eine der Tathandlungen (→ Rn. 9 ff.) zu begehen und dadurch die rechtswidrige Vermögenslage aufrechtzuerhalten. Auch insoweit reicht bedingter Vorsatz aus. Nimm...
- **[Judge=1]** `StGB_Kommentar.md` — Raub, nicht Betrug - anderer Paragraph
  > G. Subjektiver Tatbestand. Der Vorsatz muss entsprechend der Doppelnatur des Raubs sowohl Wegnahme (vgl. dazu → § 242 Rn. 29 ff.) als auch Nötigung (→ § 240 Rn. 53 f.) sowie deren Verknüpfung umfassen...

#### vectara — Top 3
- **[Judge=1]** `['Zweiundzwanzigster Abschnitt. Betrug und Untreue']` — Vorsatz erwähnt, aber Versicherungsbetrug nicht Bereicherungsabsicht
  > Der Vortäter muss Vorsatz auch hinsichtlich des späteren Versicherungsbetrugs gehabt haben; wenn der Täter die Vortat nur betrügerisch ausnutzt, liegt nur Abs....
- **[Judge=1]** `['Erpressung']` — Erwähnt Bereicherung, aber ohne Details zu Vorsatzbestimmung
  > Zwischen Schaden und (beabsichtigter) Bereicherung muss, wie beim Betrug (vgl....
- **[Judge=2]** `['Zweiundzwanzigster Abschnitt. Betrug und Untreue']` — Gewerbsmäßigkeit beim Betrug, nicht direkt Bereicherungsabsicht allgemein
  > Gewerbsmäßigkeit setzt eigennütziges Handeln voraus; fremdnütziger Betrug reicht daher nur aus, wenn die Bereicherung dem Täter zumindest mittelbar zugutekommen soll (NStZ 2008, 282 (282 f.); wistra 2...

### q09 — alltagssprache

**Query:** Hat der Angeklagte die Kunden über das Internet betrogen?

**Kontext:** Abstrakte Frage zu Internetbetrug, sucht Taeuschungshandlung + Schaden

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours | 0.97 | 100% | 100% | 3 | 6.2s |
| ragie | 1.00 | 100% | 100% | 3 | 1.5s |
| openai | 0.97 | 80% | 67% | 3 | 1.6s |
| vectara | 0.69 | 40% | 67% | 0 | 0.8s |

#### ours — Top 3
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 176` — Beantwortet zentrale Betrugsmerkmale: Vorsatz, Täuschung, Schaden
  > D. Subjektiver Tatbestand. § 263 setzt Vorsatz voraus; darüber hinaus ist die Absicht rechtswidriger Bereicherung erforderlich.   I. Vorsatz. 1. Täuschungsvorsatz. Der Vorsatz (bedingter Vorsatz genüg...
- **[Judge=2]** `§ 263 StGB – BT. Zweitundzwanzigster Abschnitt – Rn. 69` — Behandelt Betrug-Tatbestandsmerkmale, aber nicht Internet-spezifische Aspekte
  > 69 Anders ist es, wenn der Verfügende seinerseits nur (gutgläubige) Hilfsperson eines bösgläubigen Dritten ist. Hier ist auf den Irrtum des Entscheidungsbefugten abzustellen: Erkennt dieser die Unrich...
- **[Judge=3]** `§ 263 StGB – I. Vermögensbegriff  – Rn. 263` — Grundtatbestand Betrug - direkt relevant für Internetbetrug
  > 263 (1) Wer in der Absicht, sich oder einem Dritten einen rechtswidrigen Vermögensvorteil zu verschaffen, das Vermögen eines anderen dadurch beschädigt, daß er durch Vorspiegelung falscher oder durch ...

#### ragie — Top 3
- **[Judge=3]** `StGB_263_Betrug.md` — Behandelt direkt Internetbetrug mit Täuschungshandlungen
  > StGB_263_Betrug.md Entsprechendes gilt auch für sog. Abofallen im Internet (dazu NJW 2014, 2595; Routenplaner). Dies sind scheinbar unentgeltliche Informationsangebote (Wetterberichte; Routenplaner; B...
- **[Judge=3]** `StGB_263_Betrug.md` — Direkt relevant zu Internetbetrug mit Taeuschungshandlungen
  > StGB_263_Betrug.md In Fällen sog. „Kostenfallen“ im Internet (vgl. dazu Eisele NStZ 2010, 193), bei denen unerfahrene Verbraucher durch (wahre) Versprechen besonders günstiger Angebote zum Abschluss v...
- **[Judge=2]** `StGB_263_Betrug.md` — Behandelt Betrug im Internet, aber nur Literaturverweise
  > StGB_263_Betrug.md Fehlvorstellung beim Betrug, GA 2012, 354; Cornelius, Betrug durch verschleierte Kick-Back-Zahlungen bei Immobilienfinanzierungen?, NZWiSt 2012, 259; Cramer, Zur Strafbarkeit von Pr...

#### openai — Top 3
- **[Judge=3]** `Probenheld-KOMPLETT.md` — Direkt relevant: Internetbetrug durch Täuschung über kostenlose Proben
  > ## 3. Zusammenhänge  Aufgrund der IP-Adressen der Webseiten, des Registranten der Webseiten, der Hoster, der Anschriften und der Hotlines scheinen hier alle Firmen im Zusammenhang zustehen.  Die zentr...
- **[Judge=3]** `Probenheld-KOMPLETT.md` — Ermittlungsvorgang zu Internetbetrug mit konkreter Taeuschungshandlung
  > Polizeiinspektion Salzgitter, 19.07.2018  KRUCK, Polizeioberkommissar  ## Antwort DENIC Domainauskunft Slimsticks.de - 19. Juli 2018  **Von:** DENIC Whois <noreply@denic.de> **An:** Kruck, Detlef (PI ...
- **[Judge=1]** `Probenheld-KOMPLETT.md` — Konkreter Betrugsfall, aber keine allgemeinen Tatbestandsmerkmale
  > Aktuell informiert uns ein Nichtkunde unserer Sparkasse mit dem im Anhang beigefügten E-Mail-Verkehr, dass er sich durch die Firma Payplus GmbH betrogen fühle. Darüber hinaus liegen uns zwischenzeitli...

#### vectara — Top 3
- **[Judge=0]** `['Notwendige Auslagen des Nebenklägers']` — Unvollständiger Textauszug ohne erkennbaren Rechtsbezug
  > hat der Angeklagte die dadurch entstandenen bes....
- **[Judge=3]** `['Übersicht']` — Direkt relevant zu Internetbetrug und Taeuschungshandlungen
  > Der Tatbestand ist aber erfüllt bei Anlegen eines online-Kundenkontos unter Identitätstäuschung (aber nicht bei Bevollmächtigung des Dritten: BeckRS 2024, 11811), ebenso bei Verändern eines bestehende...
- **[Judge=3]** `['Übersicht']` — Direkt relevant: Online-Betrug und betrügerische Vorgänge
  > Wird ein Online-Kundenkonto unter fremdem Namen zum Zwecke des nachfolgenden Betrugs angelegt, hat dies zur Folge, dass alle nachfolgenden betrügerischen Vorgänge mittels dieses Kundenkontos in Tatein...

### q10 — alltagssprache

**Query:** Wann darf die Polizei bei jemandem zu Hause suchen?

**Kontext:** Durchsuchungsvoraussetzungen, §§ 102 ff. StPO

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours | 1.00 | 100% | 100% | 3 | 5.5s |
| ragie | 0.97 | 75% | 67% | 3 | 1.7s |
| openai | 0.00 | 0% | 0% | 0 | 1.6s |
| vectara | 0.82 | 20% | 33% | 1 | 0.8s |

#### ours — Top 3
- **[Judge=3]** `§ 102 StPO – Rn. 102` — Direkt relevant: zentrale Voraussetzungen für Wohnungsdurchsuchung
  > 102 Bei dem, welcher als Täter oder Teilnehmer einer Straftat oder der Datenhehlerei, Begünstigung, Strafvereitelung oder Hehlerei  Köhler    Ermittlungsmaßnahmen  verdächtig ist, kann eine Durchsuchu...
- **[Judge=3]** `§ 102 StPO – Rn. 10` — Direkt relevant: behandelt Durchsuchungsvoraussetzungen nach §§ 102 ff. StPO
  > II. Auffinden von Beweismitteln. Zu den Beweismitteln (→ § 94 Rn. 4 ff.) gehören auch die nur in § 103 erwähnten Spuren (SK-StPO/Jäger/Wohlers Rn. 21) u. Personen, die zu Beweiszwecken in Augenschein ...
- **[Judge=3]** `§ 102 StPO – Rn. 3` — Definiert zentrale Durchsuchungsvoraussetzungen bei Wohnungen
  > **Teilnehmer** nach §§ 25 ff. StGB, nicht die sog. notwendigen Teilnehmer (zum Begriff: Fischer/Fischer StGB Vor § 25 Rn. 7), stehen den Tatverdächtigen gleich. Bei jedem v. ihnen sowie bei den der Be...

#### ragie — Top 3
- **[Judge=3]** `Strafprozessordnung.md` — Direkt relevant: zentrale Durchsuchungsvoraussetzungen nach § 102 StPO
  > Strafprozessordnung.md 102 Bei dem, welcher als Täter oder Teilnehmer einer Straftat oder der Datenhehlerei, Begünstigung, Strafvereitelung oder Hehlerei  Köhler  ---  ## Seite 613  Ermittlungsmaßnahm...
- **[Judge=3]** `Strafprozessordnung.md` — Direkt relevant: Durchsuchungsvoraussetzungen nach StPO
  > Strafprozessordnung.md 15 E. Raumdurchsuchung bei Ergreifung oder Verfolgung des Beschuldigten (Abs. 2). Wird der Beschuldigte, auch der aus der Strafhaft entflohene Verurteilte (BayObLGSt 2020, 152),...
- **[Judge=0]** `Strafprozessordnung.md` — Behandelt Beweisrecht in Hauptverhandlung, nicht Durchsuchungsvoraussetzungen
  > Strafprozessordnung.md Schmitt  ---  ## Seite 917  Hauptverhandlung § 252 StPO  der Wohnungstür geklingelt hat, ihr Mann sei nicht zu Hause (OLG Stuttgart Justiz 1972, 322), nicht aber die Angabe, er ...

#### openai — Top 3
- **[Judge=0]** `Strafprozessordnung.md` — Behandelt Zeugnisverweigerungsrecht, nicht Durchsuchung
  > 26 H. Belehrung (Abs. 3 S. 1). Die Belehrung (Abs. 3 S. 1) muss in allen Fällen, nicht nur in denen des Abs. 2, dem Zeugen eine genügende Vorstellung v. der Bedeutung des Zeugnisverweigerungsrechts zu...
- **[Judge=0]** `StGB_Kommentar.md` — Straftat gegen öffentliche Ordnung, nicht Durchsuchungsrecht
  > Fischer  ---  ## Seite 1190  Straftaten gegen die öffentliche Ordnung  § 145d  auf einen anderen lenkt, für den die Handlung nicht strafbar wäre (BGHSt 19, 305; OLG Köln NJW 1953, 596; OLG Hamm NJW 19...
- **[Judge=0]** `Probenheld-KOMPLETT.md` — Bankauskunftsersuchen, nicht Durchsuchung von Wohnungen
  > Sehr geehrte Damen und Herren, in dem genannten Ermittlungsverfahren ist über folgende Tatsachen und Fragen Beweis zu erheben:  - Kontostände auf d. oben genannte Konto/Konten - Wann bzw. durch wen er...

#### vectara — Top 3
- **[Judge=1]** `Beck'sche Kurz-Kommentare` — Fahndung, aber nicht Durchsuchungsvoraussetzungen
  > auch Nummer 43), wenn der Haftbefehl (Unterbringungsbefehl) zur Auslösung einer gezielten Fahndung der für den mutmaßlichen Wohnsitz des Gesuchten zuständigen Polizeidienststelle übersandt wird....
- **[Judge=3]** `['Zuständigkeit für weitere gerichtliche Entscheidun...']` — Direkt relevant: Durchsuchungsvoraussetzungen Wohnung des Verdächtigen
  > 28 ff.). Die Wohnung des Verdächtigen darf durchsucht werden, wenn konkrete Anhaltspunkte dafür bestehen, dass er dort aufzufinden ist (Kaiser NJW 1980, 876)....
- **[Judge=1]** `['Durchsuchung bei anderen Personen']` — Personendurchsuchung, nicht Wohnungsdurchsuchung behandelt
  > Bei der Personendurchsuchung darf körperlicher Zwang angewendet werden; falls geboten, zB falls konkrete Verdunkelungsmaßnahmen drohen, darf der Betroffene auch kurzfristig festgenommen u. auf der Pol...

### q11 — alltagssprache

**Query:** Was passiert wenn jemand luegt damit er Geld bekommt?

**Kontext:** Laienhafte Umschreibung des Betrugstatbestandes

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours | 1.00 | 100% | 100% | 3 | 6.2s |
| ragie | 0.98 | 100% | 100% | 3 | 1.8s |
| openai | 1.00 | 20% | 33% | 3 | 1.7s |
| vectara | 1.00 | 20% | 33% | 2 | 2.5s |

#### ours — Top 3
- **[Judge=3]** `§ 263 StGB – I. Vermögensbegriff  – Rn. 263` — Definiert exakt Betrug durch Täuschung für Vermögensvorteil
  > 263 (1) Wer in der Absicht, sich oder einem Dritten einen rechtswidrigen Vermögensvorteil zu verschaffen, das Vermögen eines anderen dadurch beschädigt, daß er durch Vorspiegelung falscher oder durch ...
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 5` — Direkt relevant: Betrugstatbestand mit Täuschung und Vermögensschaden
  > 5 C. Grundtatbestand, Abs. 1. Tathandlung ist das Täuschen einer natürlichen Person (vgl. NStZ 2005, 213) über Tatsachen. Erfolg dieser Handlung muss ein Irrtum des Täuschungsadressaten sein; dieser m...
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 176` — Direkt relevant: Vorsatz bei Bereicherungsabsicht beim Betrug
  > D. Subjektiver Tatbestand. § 263 setzt Vorsatz voraus; darüber hinaus ist die Absicht rechtswidriger Bereicherung erforderlich.   I. Vorsatz. 1. Täuschungsvorsatz. Der Vorsatz (bedingter Vorsatz genüg...

#### ragie — Top 3
- **[Judge=3]** `StGB_263_Betrug.md` — Direkt relevant für Betrugstatbestand durch Lügen
  > StGB_263_Betrug.md Schwieriger ist die Abgrenzung bei zeitlich gestrecktem Fälligkeitstermin 34 (Mietzins; Ratenzahlungsverpflichtung; Arbeitsentgelt); auch hinsichtlich der Anforderungen an die konkl...
- **[Judge=2]** `StGB_263_Betrug.md` — Behandelt Betrug, aber spezielle Anstellungssituationen
  > StGB_263_Betrug.md durch Verschweigen von Vermögensdelikten eines Bauleiters; zw.); NJW 1978, 2042 (Vermögensdelikt bei Einkäufer)). Bei Täuschung über eine frühere MfS-Mitarbeit war ein Schaden nur g...
- **[Judge=3]** `StGB_263_Betrug.md` — Direkt relevante Norm für Betrug durch Lügen
  > StGB_263_Betrug.md Betrug  RiStBV 236–238  263 (1) Wer in der Absicht, sich oder einem Dritten einen rechtswidrigen Vermögensvorteil zu verschaffen, das Vermögen eines anderen dadurch beschädigt, daß ...

#### openai — Top 3
- **[Judge=3]** `Probenheld-KOMPLETT.md` — Beschreibt konkreten Betrugsfall mit Taeuschung fuer Geld
  > Durch einen Bekannten bekommt der GS nun den Hinweis, dass es sich um eine Betrugsmasche handelt, bei der lediglich weitere Papiere per Nachnahme zugesandt werden, man am Ende noch einige hundert Euro...
- **[Judge=1]** `analyses_findings.md` — Fallakten zu Internetbetrug, aber keine Tatbestandsmerkmale erklärt
  > ### 107Js198620 d (107Js198620 d.md) - Seitenbesuch: Seitenkontakt geschildert | Z.995: Er gab an, dass er im Internet auf eine Werbung geklickt hatte, bei der ihm versprochen wurde, dass er 7000 € be...
- **[Judge=1]** `Probenheld-KOMPLETT.md` — Verfahrensdokument zu Betrug, aber keine Rechtsnormen
  > | Anzeigenaufnahme am | 30.04.2019 13:36 h | | :-- | :-- |  ## Personalbogen / Vernehmung - Zeuge/Zeugin  **Polizeipräsidium Rheinpfalz Kriminalinspektion Neustadt/W.**  Datum 30.04.2019 VN 509016/300...

#### vectara — Top 3
- **[Judge=2]** `['Geldwäsche']` — Behandelt Betrug, aber spezifischen Teilaspekt der Beihilfe
  > Für einen Finanzagenten kommt eine Beteiligung an der Vorrat des Betrugs in Betracht, wenn er den Hintermännern sein Bankkonto zur Verfügung stellt, damit die Geschädigten tatplankonform Geld darauf ü...
- **[Judge=0]** `['Übersicht']` — Fragment ohne Bezug zu Betrug oder Täuschung
  > Was er damit iErg bezweckt (Flucht, Vermeidung des Arbeitszwangs usw.)...
- **[Judge=0]** `['Geldfälschung']` — Falschgeld, nicht Betrug durch Täuschung
  > Daher ist Geld „nachgemacht", wenn dem Täter die Legitimation zur Herstellung fehlt (vgl....

### q12 — alltagssprache

**Query:** Wann muss jemand ins Gefaengnis waehrend die Tat noch nicht bewiesen ist?

**Kontext:** Untersuchungshaft, §§ 112 ff. StPO

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours | 1.00 | 100% | 100% | 3 | 5.5s |
| ragie | 0.89 | 60% | 67% | 3 | 1.9s |
| openai | 0.00 | 0% | 0% | 0 | 1.8s |
| vectara | 1.00 | 20% | 33% | 2 | 0.7s |

#### ours — Top 3
- **[Judge=3]** `§ 112 StPO – Rn. 112` — Direkt relevant: Beantwortet Frage zur Untersuchungshaft vollständig
  > 112 (1) ¹ Die Untersuchungshaft darf gegen den Beschuldigten angeordnet werden, wenn er der Tat dringend verdächtig ist und ein Haftgrund besteht. ² Sie darf nicht angeordnet werden, wenn sie zu der B...
- **[Judge=3]** `§ 112 StPO – III. Flucht (Abs – Rn. 23` — Direkt relevant zu Untersuchungshaft und deren Voraussetzungen
  > Bei einer besonders hohen Straferwartung braucht daher nur geprüft zu werden, ob Umstände vorhanden sind, die die hieraus herzuleitende Fluchtgefahr ausräumen können (KG StV 1996, 383; OLG München Str...
- **[Judge=3]** `§ 112 StPO – III. Flucht (Abs – Rn. 32 (Teil 2)` — Behandelt direkt Untersuchungshaft und Verdunkelungsgefahr
  > Wenn die Verdunkelungshandlungen nicht geeignet sind, die Ermittlung der Wahrheit zu erschweren, darf UHaft nicht angeordnet werden. Der Haftgrund liegt daher nicht vor, wenn der Sachverhalt schon in ...

#### ragie — Top 3
- **[Judge=3]** `Strafprozessordnung.md` — Direkt relevant zu Untersuchungshaft vor Verurteilung
  > Strafprozessordnung.md A. UHaft. Die UHaft nach §§ 112 ff., §§ 72, 72a JGG, dh die Inhaftierung eines noch nicht (o. noch nkr) verurteilten Beschuldigten, lässt sich mit der Unschuldsvermutung des Art...
- **[Judge=0]** `StGB_Kommentar.md` — Behandelt Vollstreckungsvereitelung, nicht Untersuchungshaft
  > StGB_Kommentar.md Fischer/Lutz  1941  ---  ## Seite 682  § 258  BT. Einundzwanzigster Abschnitt.  über für die Bewertung maßgebliche Umstände bewusst unterdrückt oder verschweigt. Dasselbe gilt entspr...
- **[Judge=3]** `Strafprozessordnung.md` — Behandelt direkt Haftgruende bei Untersuchungshaft
  > Strafprozessordnung.md 2 Freiheitsstrafe iSv Abs. 1 ist auch der Strafarrest nach § 9 WStG, nicht aber der Jugendarrest nach § 16 JGG (Löwe/Rosenberg/Hilger Rn. 3), auch wenn dieser neben Jugendstrafe...

#### openai — Top 3
- **[Judge=0]** `Strafprozessordnung.md` — Behandelt Teilfreispruch, nicht Untersuchungshaft
  > Tatmehrheit: Wird nicht wegen aller Delikte verurteilt, die nach der Anklage in Tatmehrheit (§ 53 StGB) begangen worden sein sollen, so muss insoweit freigesprochen werden (BGH NStZ-RR 2008, 287 mwN; ...
- **[Judge=0]** `StGB_Kommentar.md` — Behandelt Vollstreckungsvereitelung, nicht Untersuchungshaft
  > 29 D. Vollstreckungsvereitelung (Abs. 2). Voraussetzung der Vollstreckungsvereitelung ist, dass eine gegen eine andere Person rechtskräftig (§ 449 StPO) verhängte Strafe (→ Rn. 5f.) oder Maßnahme (→ R...
- **[Judge=0]** `Strafprozessordnung.md` — Behandelt Beweisverwertung, nicht Untersuchungshaft
  > Der Verwertung steht auch nicht entgegen, wenn sich wegen einer **Änderung der rechtlichen Beurteilung** der Tat während des Verfahrens diese sich im Urteilszeitpunkt aus tatsächlichen oder rechtliche...

#### vectara — Top 3
- **[Judge=2]** `['Übersicht']` — Thematisch relevant, behandelt Beweiswuerdigung vor Verurteilung
  > 16) noch nicht bewiesen (BGHSt 10, 276; OLG Köln StraFo 2005, 216)....
- **[Judge=0]** `Strafgesetzbuch` — Behandelt Tatbestandsvollendung, nicht Untersuchungshaft
  > Var.). Wenn der Erfolg noch nicht eingetreten ist, muss er die Vollendung der Tat verhindern (3....
- **[Judge=0]** `['Zehnter Abschnitt. Falsche Verdächtigung']` — Behandelt Verdächtigung, nicht Untersuchungshaft
  > , auch wenn der Verdächtigende dies nicht weiß (Langer JZ 1987, 810); oder wenn schon nach dem Inhalt der Äußerung die objektiven oder subjektiven Voraussetzungen einer angeblich begangenen Straftat o...

### q13 — stpo-prozess

**Query:** Welche Voraussetzungen hat die Untersuchungshaft wegen Fluchtgefahr?

**Kontext:** § 112 Abs. 2 Nr. 2 StPO Fluchtgefahr

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours | 0.99 | 80% | 100% | 3 | 5.6s |
| ragie | 0.99 | 80% | 100% | 3 | 1.6s |
| openai | 0.95 | 100% | 100% | 2 | 1.6s |
| vectara | 0.94 | 60% | 67% | 3 | 1.1s |

#### ours — Top 3
- **[Judge=3]** `§ 112 StPO – Rn. 112` — Behandelt direkt § 112 Abs. 2 Nr. 2 StPO Fluchtgefahr
  > 112 (1) ¹ Die Untersuchungshaft darf gegen den Beschuldigten angeordnet werden, wenn er der Tat dringend verdächtig ist und ein Haftgrund besteht. ² Sie darf nicht angeordnet werden, wenn sie zu der B...
- **[Judge=3]** `§ 112 StPO – III. Flucht (Abs – Rn. 17 (Teil 1)` — Definiert direkt Fluchtgefahr nach § 112 Abs. 2 Nr. 2 StPO
  > 17 IV. Fluchtgefahr (Abs. 2 Nr. 2). Fluchtgefahr (Abs. 2 Nr. 2) besteht, wenn die Würdigung der Umstände des Falles es wahrscheinlicher macht, dass sich der Beschuldigte dem Strafverfahren entziehen, ...
- **[Judge=3]** `§ 112 StPO – III. Flucht (Abs – Rn. 16` — Direkt zu Fluchtgefahr nach § 112 Abs. 2 Nr. 2 StPO
  > 16 Bei Ergreifung des Beschuldigten aufgrund des nach Abs. 2 Nr. 1 erlassenen Haftbefehls entfällt der Haftgrund der Flucht. In der Regel wird die vorherige Flucht aber die Aufrechterhaltung des Haftb...

#### ragie — Top 3
- **[Judge=3]** `Strafprozessordnung.md` — Direkt relevant: behandelt Fluchtgefahr-Voraussetzungen bei UHaft
  > Strafprozessordnung.md ## Untersuchungshaft bei leichteren Taten  113 (1) Ist die Tat nur mit Freiheitsstrafe bis zu sechs Monaten oder mit Geldstrafe bis zu einhundertachtzig Tagessätzen bedroht, so ...
- **[Judge=3]** `Strafprozessordnung.md` — Direkt relevant: detaillierte Kriterien für Fluchtgefahr-Beurteilung
  > Strafprozessordnung.md Die Beurteilung der Fluchtgefahr erfordert die Berücksichtigung aller Umstände des Falles, insbes. der Art der dem Beschuldigten vorgeworfenen Tat, der Persönlichkeit des Beschu...
- **[Judge=3]** `Strafprozessordnung.md` — Direkt zu Fluchtgefahr § 112 Abs. 2 Nr. 2 StPO
  > Strafprozessordnung.md 21 Gegen die Fluchtgefahr sprechen idR starke familiäre o. berufliche Bindungen (OLG Hamm StV 2003, 509), dass der Beschuldigte sich dem Verf. über einen längeren Zeitraum geste...

#### openai — Top 3
- **[Judge=2]** `Strafprozessordnung.md` — Behandelt Fluchtgefahr, aber nur bei leichteren Taten
  > 3, Abs. 2 schließt auch aus, den auf § 112 gestützten Haftbefehl hilfsweise auf den Haftgrund der Wiederholungsgefahr zu stützen; denn auch dann handelt es sich um eine Anwendung dieses Haftgrundes (L...
- **[Judge=3]** `Strafprozessordnung.md` — Direkt relevant - § 112 Abs. 2 Nr. 2 Fluchtgefahr
  > 15 G. Bestand des Haftbefehls. Wird der Haftbefehl nicht aufgeh., bleibt er grds. in Kraft; er wird nicht durch Zeitablauf wirkungslos (OLG Hamm NStZ 2016, 304).  Voraussetzungen der Untersuchungshaft...
- **[Judge=2]** `Strafprozessordnung.md` — Behandelt Alternativen zur Untersuchungshaft bei Fluchtgefahr
  > ## Aussetzung des Vollzugs des Haftbefehls RiStBV 54, 57  116 (1) Der Richter setzt den Vollzug eines Haftbefehls, der lediglich wegen Fluchtgefahr gerechtfertigt ist, aus, wenn weniger einschneidende...

#### vectara — Top 3
- **[Judge=3]** `['Haftgrund der Wiederholungsgefahr']` — Direkt relevanter Text zu § 112 Abs. 2 Fluchtgefahr
  > (2) In diesen Fällen darf die Untersuchungshaft wegen Fluchtgefahr nur angeordnet werden, wenn der Beschuldigte 1....
- **[Judge=1]** `['Fünfter Unterabschnitt. Verfahren bei Aussetzung d...']` — Jugendstrafrecht, nicht allgemeine Fluchtgefahr-Voraussetzungen
  > (2) Solange der Jugendliche das sechzehnte Lebensjahr noch nicht vollendet hat, ist die Verhängung von Untersuchungshaft wegen Fluchtgefahr nur zulässig, wenn er 1....
- **[Judge=3]** `['Haftgrund der Wiederholungsgefahr']` — Direkt relevant: behandelt Fluchtgefahr-Voraussetzungen
  > 4 Anordnung wegen Fluchtgefahr nur, wenn außer den Voraussetzungen des § 112 Abs....

### q14 — stpo-prozess

**Query:** Wie lange darf die Untersuchungshaft maximal dauern?

**Kontext:** § 121 StPO Sechs-Monats-Grenze, Haftpruefung OLG

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours | 0.99 | 100% | 100% | 3 | 5.3s |
| ragie | 1.00 | 100% | 100% | 3 | 1.7s |
| openai | 1.00 | 0% | 0% | 1 | 2.0s |
| vectara | 0.96 | 40% | 67% | 3 | 1.0s |

#### ours — Top 3
- **[Judge=3]** `§ 121 StPO – Rn. 121` — Beantwortet direkt Sechs-Monats-Grenze der Untersuchungshaft
  > 121 (1) Solange kein Urteil ergangen ist, das auf Freiheitsstrafe oder eine freiheitsentziehende Maßregel der Besserung und Sicherung erkennt, darf der Vollzug der Untersuchungshaft wegen derselben Ta...
- **[Judge=3]** `§ 121 StPO – Rn. 1` — Direkt relevant: behandelt maximale Dauer der Untersuchungshaft
  > Eine absolute Höchstgrenze für die Dauer v. UHaft sieht weder die StPO noch die EMRK vor (EGMR EuGRZ 1993, 384). Es kommt auf eine Abwägung aller Umstände des Einzelfalls an. Eine ein Jahr übersteigen...
- **[Judge=2]** `§ 121 StPO – Rn. 8 (Teil 1)` — Behandelt UHaft-Beschränkungen, aber nicht Sechs-Monats-Grenze
  > 8 II. Zeitliche Geltung der Beschränkungen der UHaft. Bis zu einem auf Freiheitsentziehung lautenden Urteil (Freiheitsstrafe mit o. ohne Bewährung o. freiheitsentziehende Sicherungsmaßregeln) gelten d...

#### ragie — Top 3
- **[Judge=3]** `Strafprozessordnung.md` — Behandelt direkt maximale Dauer der Untersuchungshaft
  > Strafprozessordnung.md die 6 Monate überschritten werden (Abs. 2), eine UHaft v. mehr als 1 Jahr bis zum Beginn der HV kann nur in ganz bes. Ausnahmefällen gerechtfertigt sein (BVerfG NJW 2018, 2948; ...
- **[Judge=3]** `Strafprozessordnung.md` — Direkt relevant, regelt die Sechs-Monats-Grenze der Untersuchungshaft
  > Strafprozessordnung.md Der Haftbefehl wird gegenstandslos (BVerfGE 9, 160; KG NStZ 2012, 230; OLG Düsseldorf Rpfleger 1984, 73; OLG Hamm StraFo 2002, 100; OLG Stuttgart Justiz 1984, 213). Dies soll we...
- **[Judge=3]** `Strafprozessordnung.md` — Direkt relevant: behandelt Sechs-Monats-Grenze des § 121 StPO
  > Strafprozessordnung.md Die zeitliche Begrenzung der UHaft nach Abs. 1 gilt nicht, wenn der Haftbefehl nach § 230 Abs. 2 (→ § 230 Rn. 10), § 236 oder § 329 Abs. 4 S. 1 (→ § 329 Rn. 45) ergangen ist, au...

#### openai — Top 3
- **[Judge=1]** `Strafprozessordnung.md` — JGG-Vorschriften, andere Aspekte als allgemeine Haftdauer
  > (5) Befindet sich ein Jugendlicher in Untersuchungshaft, so ist das Verfahren mit besonderer Beschleunigung durchzuführen.  (6) Die richterlichen Entscheidungen, welche die Untersuchungshaft betreffen...
- **[Judge=1]** `Strafprozessordnung.md` — Jugendstrafrecht, nicht allgemeine Haftdauer-Bestimmungen
  > 2667  ---  ## Seite 2392  Anh. 1 JGG Jugendgerichtsgesetz  die zugrundeliegenden tatsächlichen Feststellungen letztmals geprüft werden konnten.² Wird die Vollstreckung des Restes der lebenslangen Frei...
- **[Judge=1]** `StGB_Kommentar.md` — JGG Untersuchungshaft, aber nicht zur Maximaldauer
  > (3) In den Fällen des Absatzes 1 gilt § 85 Abs. 6 entsprechend mit der Maßgabe, daß der Vollstreckungsleiter die Vollstreckung der Jugendstrafe abgeben kann, wenn der Verurteilte das einundzwanzigste ...

#### vectara — Top 3
- **[Judge=3]** `['Verfahren bei der Haftprüfung']` — Beantwortet direkt die Sechs-Monats-Grenze der Untersuchungshaft
  > 1 vgl. § 123. Fortdauer der Untersuchungshaft über sechs Monate RiStBV 56 121 (1) Solange kein Urteil ergangen ist, das auf Freiheitsstrafe oder eine freiheitsentziehende Maßregel der Besserung und Si...
- **[Judge=1]** `['Haftgrund der Wiederholungsgefahr']` — Sicherungshaft, nicht Untersuchungshaft - anderer Hafttyp
  > Die Höchstdauer der Sicherungshaft beträgt 1 Jahr (§ 122a)....
- **[Judge=3]** `['Verfahren bei der Haftprüfung']` — Behandelt direkt Höchstdauer der Untersuchungshaft
  > 4 S. 2). Höchstdauer der Untersuchungshaft bei Wiederholungsgefahr 122a In den Fällen des § 121 Abs....

### q15 — stpo-prozess

**Query:** Was regelt § 136 StPO zur Beschuldigtenvernehmung?

**Kontext:** Belehrungspflichten, Recht auf Verteidiger

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours | 0.92 | 80% | 100% | 2 | 5.7s |
| ragie | 0.93 | 100% | 100% | 2 | 2.1s |
| openai | 1.00 | 80% | 100% | 2 | 2.0s |
| vectara | 0.93 | 40% | 33% | 3 | 0.9s |

#### ours — Top 3
- **[Judge=2]** `§ 500 StPO – ILL. für das Strafverfahren und das Bußgeldverf` — Behandelt Beschuldigtenvernehmung, aber nicht § 136 StPO direkt
  > (4) Zeugen können zur Aufenthaltsermittlung ausgeschrieben werden.  (5) Für die internationale Fahndung nach Personen, einschließlich der Fahndung nach Personen im SIS und aufgrund eines Europäischen ...
- **[Judge=3]** `§ 114b StPO – I. Abs – Rn. 5` — Direkt relevant: behandelt Belehrungspflichten nach § 136 StPO
  > 5 II. Abs. 2 S. 1 Nr. 2–4. Hier wird die auch nach § 136 Abs. 1 S. 2, 3 und § 163a Abs. 3 S. 2, 4 vor Beginn der ersten richterlichen bzw. staatsanwaltschaftlichen o. polizeilichen Vernehmung bestehen...
- **[Judge=3]** `StPO – III. Steuerstrafverfahren – Rn. 25` — Direkt relevant: behandelt § 136 StPO und Grundsätze
  > Das nemo-tenetur-Prinzip (nemo tenetur se ipsum accusare und nemo tenetur se ipsum prodere) o. der Grundsatz der Selbstbelastungsfreiheit bedeutet, dass niemand verpflichtet ist, sich selbst anzuklage...

#### ragie — Top 3
- **[Judge=2]** `Strafprozessordnung.md` — Behandelt Belehrungspflichten bei Beschuldigtenvernehmung, aber nicht § 136 StPO direkt
  > Strafprozessordnung.md 77a Der Verfolgungsbehörde steht insoweit ein – objektiv zu bestimmender – Beurteilungsspielraum zu (BGHSt 38, 214 (228); BGHSt 64, 89; StraFo 2005, 27; erg. → StPO § 163a Rn. 4...
- **[Judge=2]** `Strafprozessordnung.md` — Behandelt Vernehmungsverfahren, aber nicht § 136 direkt
  > Strafprozessordnung.md (2) In der Ladung zu einer richterlichen oder staatsanwaltschaftlichen Vernehmung sollen Zwangsmaßnahmen für den Fall des Ausbleibens nur angedroht werden, wenn sie gegen den un...
- **[Judge=3]** `Strafprozessordnung.md` — Direkt relevant: regelt Belehrung nach § 136 StPO
  > Strafprozessordnung.md 45. Form der Vernehmung und Niederschrift. (1) ¹ Die Belehrung des Beschuldigten vor seiner Vernehmung nach § 136 Absatz 1, § 163a Absatz 3 Satz 2 StPO ist aktenkundig zu machen...

#### openai — Top 3
- **[Judge=2]** `Strafprozessordnung.md` — Behandelt Belehrungspflichten und Beschuldigtenvernehmung, aber nicht § 136
  > aber auch BayObLGSt 2004, 141). Ist die Einleitung eines Ermittlungsverfahrens geboten, weil der Vernehmungsbeamte den Verdächtigen als Täter überführen will, dann darf dieser nicht als Zeuge vernomme...
- **[Judge=2]** `Strafprozessordnung.md` — Behandelt Beschuldigtenstatus und Vernehmungsarten, nicht direkt § 136
  > 77 1. Tatverdacht allein begründet allerdings weder die Beschuldigteneigenschaft noch zwingt er ohne weiteres zur Einleitung v. Ermittlungen (BGHSt 64, 89 = NJW 2019, 2627 (2630)), auch nicht allein d...
- **[Judge=2]** `StGB_Kommentar.md` — Behandelt § 136 StPO, aber zu Verjährungsunterbrechung
  > Abs. 2 enthält eine Bestimmung des Unterbrechungszeitpunkts, wenn dieser eine schriftliche Anordnung oder Entscheidung voraussetzt. Die Regelung ist durch G vom 15.6.2021 (BGBl. I 2099) geändert worde...

#### vectara — Top 3
- **[Judge=3]** `['Einleitung']` — Direkt relevant - behandelt § 136 StPO Beschuldigtenvernehmung
  > → StPO § 136 Rn. 3) als Beschuldigtenvernehmung fortzusetzen (BGHSt 22, 129 (132))....
- **[Judge=1]** `Beck'sche Kurz-Kommentare` — Erwähnt § 136 StPO, aber nur Aufzeichnungspflicht
  > (3) ¹ Hinsichtlich der Möglichkeit und gegebenenfalls Pflicht zur Aufzeichnung der Vernehmung des Beschuldigten in Bild und Ton sind § 136 Absatz 4 StPO bzw....
- **[Judge=1]** `['Einleitung']` — Nur Verweis auf Paragraph, keine Regelungsinhalte
  > StPO), ferner die Aussagen der Beschuldigten (§§ 136, 163a Abs....

### q16 — cross-reference

**Query:** Worin unterscheidet sich Betrug von Unterschlagung?

**Kontext:** Abgrenzung § 263 vs § 246 StGB

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours | 0.93 | 40% | 67% | 2 | 5.5s |
| ragie | 1.00 | 0% | 0% | 1 | 1.8s |
| openai | 0.98 | 60% | 67% | 3 | 1.6s |
| vectara | 0.85 | 60% | 67% | 1 | 0.7s |

#### ours — Top 3
- **[Judge=2]** `§ 266 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 191` — Behandelt Tateinheit zwischen Betrug und Unterschlagung
  > Tateinheit ist möglich mit Diebstahl (Dallinger MDR 1954, 399), und zwar auch dann, wenn auch eine nicht in einem Treueverhältnis stehende Person den Diebstahl hätte begehen können (BGHSt 17, 360); mi...
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 76` — Direkt relevant: Abgrenzung Betrug-Diebstahl, zentrale Tatbestandsmerkmale
  > 4. Dreiecksbetrug. Da die Getäuschte und die verfügende, nicht aber die verfügende und die geschädigte Person identisch sein müssen, ist der Tatbestand des § 263 nur erfüllt, wenn die Vermögensverfügu...
- **[Judge=1]** `§ 263 StGB – BT. Zweitundzwanzigster Abschnitt – Rn. 69` — Behandelt Betrug, aber nicht Unterschlagungsabgrenzung
  > 69 Anders ist es, wenn der Verfügende seinerseits nur (gutgläubige) Hilfsperson eines bösgläubigen Dritten ist. Hier ist auf den Irrtum des Entscheidungsbefugten abzustellen: Erkennt dieser die Unrich...

#### ragie — Top 3
- **[Judge=1]** `StGB_Kommentar.md` — Nennt beide Delikte, keine Abgrenzungskriterien erklärt
  > StGB_Kommentar.md 3. Einzelfälle. a) Zulässig sind Wahlfeststellungen nach hM (umfassende Dokumentation bei Wolter (→ Rn. 38) S. 174 ff.) zwischen:  Diebstahl und Hehlerei (BGHSt 1, 302; 12, 386; 15, ...
- **[Judge=1]** `StGB_Kommentar.md` — Inhaltsverzeichnis ohne inhaltliche Abgrenzung der Delikte
  > StGB_Kommentar.md # Neunzehnter Abschnitt. Diebstahl und Unterschlagung  Diebstahl ... § 242 Besonders schwerer Fall des Diebstahls ... § 243 Diebstahl mit Waffen; Bandendiebstahl; Wohnungseinbruchdie...

#### openai — Top 3
- **[Judge=3]** `StGB_Kommentar.md` — Direkte Abgrenzung § 263 vs § 246 behandelt
  > Für den Vortäter kann die Unterschlagung mit Drittzueignungswillen zugleich Beihilfe zur Hehlerei sein; in diesem Fall dürfte die Beteiligung an § 259 ebenso zurücktreten wie im Fall einer real konkur...
- **[Judge=2]** `StGB_Kommentar.md` — Behandelt Konkurrenz § 246/§ 263, aber keine Abgrenzungsmerkmale
  > Für Fälle des Abs. 2 ist für den Vergleich der Strafdrohungen auf den Strafrahmen der (tatbestandlichen) Qualifikation abzustellen. Daraus ergeben sich zufällig erscheinende Konkurrenz-Folgen.  23d Pr...
- **[Judge=1]** `Probenheld-KOMPLETT.md` — Behandelt nur Betrug, nicht Abgrenzung zur Unterschlagung
  > Vermögensschaden trotz fehlender Zahlung: Die Gerichte werten auch die bloße Berechnung einer Forderung als schadensbegründend; der fehlende Zahlungswille des Kunden verhindert nicht die Strafbarkeit....

#### vectara — Top 3
- **[Judge=1]** `['Erpressung']` — Abgrenzung zu anderem Delikt, nicht Betrug vs Unterschlagung
  > Vom Betrug unterscheidet sie sich im Mittel, das dort Täuschung, hier Nötigung ist....
- **[Judge=3]** `['Neunzehnter Abschnitt. Diebstahl und Unterschlagun...']` — Direkte Abgrenzung zwischen Betrug und Unterschlagung
  > Gegenüber § 263 tritt § 246 zurück, wenn die Zueignung durch Betrug geschieht; dagegen ist ein der Unterschlagung nachfolgender Sicherungsbetrug mitbestrafte Nachtat....
- **[Judge=2]** `['Zweiundzwanzigster Abschnitt. Betrug und Untreue']` — Betrug-Definition, aber keine direkte Abgrenzung zur Unterschlagung
  > Ein (vollendeter) Betrug liegt vor, wenn zum Zeitpunkt des Abschlusses eines Verpflichtungsgeschäfts feststeht, dass der durch Täuschung erlangten Verpflichtung (= Vermögensverfügung) eine (irrtumsbed...

### q17 — cross-reference

**Query:** Was sind die Unterschiede zwischen Diebstahl und Raub?

**Kontext:** § 242 vs § 249 StGB — Abgrenzung durch Gewalt/Drohung

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours | 1.00 | 100% | 100% | 3 | 6.0s |
| ragie | 1.00 | 100% | 100% | 3 | 2.0s |
| openai | 0.89 | 80% | 67% | 2 | 1.8s |
| vectara | 0.96 | 60% | 67% | 3 | 0.8s |

#### ours — Top 3
- **[Judge=3]** `§ 249 StGB` — Direkt relevant: erklärt Raub-Tatbestand und Abgrenzung zur Erpressung
  > NStZ 2023, 351). Danach ist § 249 gegenüber § 255 ein spezielles Delikt; in jedem Raub liegt eine räuberische Erpressung (aA die hM in der Literatur). Die Unterscheidung richtet sich nach dem äußeren ...
- **[Judge=3]** `§ 249 StGB – BT. Zwanzigster Abschnitt – Rn. 15` — Direkt relevant: erklärt subjektiven Tatbestand Raub vs Diebstahl
  > G. Subjektiver Tatbestand. Der Vorsatz muss entsprechend der Doppelnatur des Raubs sowohl Wegnahme (vgl. dazu → § 242 Rn. 29 ff.) als auch Nötigung (→ § 240 Rn. 53 f.) sowie deren Verknüpfung umfassen...
- **[Judge=3]** `§ 248c StGB – G. Konkurrenzen – Rn. 249` — Direkt relevant: Raubtatbestand mit Gewalt/Drohung-Abgrenzung
  > 249 (1) Wer mit Gewalt gegen eine Person oder unter Anwendung von Drohungen mit gegenwärtiger Gefahr für Leib oder Leben eine fremde bewegliche Sache einem anderen in der Absicht wegnimmt, die Sache s...

#### ragie — Top 3
- **[Judge=3]** `StGB_Kommentar.md` — Direkte Abgrenzung Diebstahl/Raub mit systematischer Stellung
  > StGB_Kommentar.md Rechtsprechungsübersichten: Maier/Percic NStZ-RR 2010, 129; Maier NStZ-RR 2012, 297; 2013, 329 (364); 2015, 33; 2017, 1, 2018, 33; 2025, 129; 2025, 161.  2 B. Systematische Stellung....
- **[Judge=3]** `StGB_Kommentar.md` — Direkte Abgrenzung Raub zu Diebstahl, Konkurrenzen
  > StGB_Kommentar.md J. Konkurrenzen. Gesetzeseinheit liegt zwischen § 249 und §§ 242, 243, 244, 244a vor, die von § 249 verdrängt werden (vgl. BGHSt 20, 235 (237 f.); NStZ-RR 2005, 202 (203)). Entsprech...
- **[Judge=3]** `StGB_Kommentar.md` — Direkt relevant: enthält Raubdefinition mit Gewaltkriterium
  > StGB_Kommentar.md E. Strafantrag. Abs. 3 regelt ein Antragserfordernis entspr. §§ 247, 248a (vgl. → § 247 Rn. 1 ff., → § 248a Rn. 1 ff.).  F. Abs. 4. Nach Abs. 4 wird milder bestraft, wer ohne Zueignu...

#### openai — Top 3
- **[Judge=2]** `StGB_Kommentar.md` — Konkurrenzen zwischen Raub/Diebstahl, aber nicht grundlegende Unterschiede
  > 12 I. Konkurrenzen. Gesetzeseinheit besteht mit §§ 242, 244 sowie mit § 240 (diff. NK-StGB/Kindhäuser Rn. 28). § 249 verdrängt § 252, wenn Raubmittel zunächst zur Wegnahme und später zur Sicherung des...
- **[Judge=1]** `StGB_Kommentar.md` — Behandelt schweren Raub, nicht Grundabgrenzung Diebstahl/Raub
  > 1); zwischen § 249 und § 255, wenn neben der vom Tatopfer herausgegebenen Sache noch eine weitere gewaltsam weggenommen wird (BGH NStZ 2025, 40); mit § 223 (BGH NStZ-RR 1999, 173; NK-StGB/Kindhäuser R...
- **[Judge=3]** `StGB_Kommentar.md` — Direkte Abgrenzung Diebstahl/Raub durch Konkurrenzen
  > J. Konkurrenzen. Gesetzeseinheit liegt zwischen § 249 und §§ 242, 243, 244, 244a vor, die von § 249 verdrängt werden (vgl. BGHSt 20, 235 (237 f.); NStZ-RR 2005, 202 (203)). Entsprechendes gilt zwische...

#### vectara — Top 3
- **[Judge=3]** `['Erpressung']` — Direkt zur Abgrenzung Diebstahl/Raub relevant
  > Zur Abgrenzung von (Diebstahl und) Raub vgl....
- **[Judge=2]** `['Zwanzigster Abschnitt. Raub und Erpressung']` — Tateinheit Diebstahl-Raub, aber keine Abgrenzungskriterien
  > Tateinheit kann zwischen vollendetem Diebstahl und versuchtem Raub gegeben sein (BGHSt 21, 78; NStZ-RR 2005, 202 (203)); zwischen § 250 und § 249 im Fall unterschiedlicher Begehung gegenüber mehreren ...
- **[Judge=1]** `Strafgesetzbuch` — Nur Paragraphenübersicht ohne inhaltliche Abgrenzungskriterien
  > Raub ... § 249Schwerer Raub ... § 250Raub mit Todesfolge ... § 251Räuberischer Diebstahl ... § 252Erpressung ... § 253(weggefallen) ... § 254Räuberische Erpressung ... § 255Führungsaufsicht ... § 256...

### q18 — cross-reference

**Query:** Wann wird Betrug zu Computerbetrug und umgekehrt?

**Kontext:** § 263 vs § 263a StGB — Abgrenzung bei elektronischer Datenverarbeitung

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours | 1.00 | 20% | 33% | 3 | 6.6s |
| ragie | 0.88 | 80% | 67% | 2 | 2.2s |
| openai | 0.67 | 20% | 33% | 0 | 2.2s |
| vectara | 1.00 | 80% | 100% | 3 | 0.9s |

#### ours — Top 3
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 58` — Direkte Abgrenzung zwischen § 263 und § 263a
  > 58 Im Geschäftsverkehr wird sich, wer die Berechtigung eines Leistungsverlangens oder -auftrags nicht zu prüfen hat, hierüber idR auch keine (richtigen oder falschen) Gedanken machen (NStZ 1997, 281; ...
- **[Judge=1]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 62` — Behandelt nur § 263 Betrug, nicht Abgrenzung zu § 263a
  > Die Kausalität der Täuschung für den Irrtum und dessen Kausalität für die Vermögensverfügung müssen im Einzelfall festgestellt sein. Mitverursachung reicht aus. Dabei darf das Gericht auch bei Serien-...
- **[Judge=1]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 114` — Behandelt Vermögensschaden bei § 263, nicht Abgrenzung zu § 263a
  > 114 a) Quantifizierbarkeit der Vermögensminderung. Die Vermögensminderung muss quantifizierbar sein (RGSt 16, 4; 44, 249; BGHSt 16, 321). Grds. nicht ausreichend ist eine nicht quantifizierbare Einbuß...

#### ragie — Top 3
- **[Judge=2]** `StGB_Kommentar.md` — Behandelt Computerbetrug, aber nicht Abgrenzung zu normalem Betrug
  > StGB_Kommentar.md Fischer/Lutz  ---  ## Seite 799  Betrug und Untreue § 263a  IV. Subjektiver Tatbestand. In subjektiver Hinsicht ist (mindestens bedingter) Vorsatz hinsichtlich der Merkmale des Compu...
- **[Judge=3]** `StGB_Kommentar.md` — Direkt relevante Norm § 263a zur Abgrenzung
  > StGB_Kommentar.md ## Computerbetrug  263a (1) Wer in der Absicht, sich oder einem Dritten einen rechtswidrigen Vermögensvorteil zu verschaffen, das Vermögen eines anderen dadurch beschädigt, daß er da...
- **[Judge=0]** `StGB_Kommentar.md` — Text behandelt Tateinheit/Nachbardelikte, nicht Abgrenzung Betrug/Computerbetrug
  > StGB_Kommentar.md 237b § 266a wird von § 263 verdrängt, wenn hinsichtlich einer Verkürzung des Gesamtversicherungsbeitrags eine Betrugshandlung vorliegt (NJW 2003, 1821 (1823)).  238 Tateinheit ist mö...

#### openai — Top 3
- **[Judge=0]** `Probenheld-KOMPLETT.md` — Aktenverzeichnis ohne Abgrenzungskriterien zwischen Paragraphen
  > | § 263 StGB Betrug | Vg / 281492 / 2019 | Bezikakriminalinapek Iron Kiel, <br> Fachinapektion 1, <br> Kommissariat 14 | Uda Mark, (8575) | 0431/180-3183 | StA M.Öpiglt: 56/2/19 <br> StA Kiel: 596 UJa...
- **[Judge=2]** `Probenheld-KOMPLETT.md` — Behandelt § 263a, aber keine Abgrenzung zu § 263
  > **Betrug** **101109** **(1)**  ## Weggelegt  **Aufzubewahren bis**  - dauernd -  **Aktenzeichen:** **107 Js 1871/19** **Datum:** **12.12.2019**  **Verfahrensgegenstand nach der Justizstatistik**  | Sc...
- **[Judge=1]** `Probenheld-KOMPLETT.md` — Praktischer Fall, aber ohne Abgrenzungskriterien § 263/263a
  > Das vorliegende Verfahren wird abgeschlossen und der STA Cottbus mit der Bitte um Kenntnisnahme und zur weiteren Entscheidung übersandt.  ## ABSCHLIEßENDER BERICHT  Polizeipräsidium Polizeidirektion S...

#### vectara — Top 3
- **[Judge=3]** `['Übersicht']` — Direkte Abgrenzung Betrug zu Computerbetrug behandelt
  > Ebenso ist das Verhältnis zwischen (möglicher) Beteiligung am Betrug und (sicherem) späterem Computerbetrug hinsichtlich desselben Schadens zu behandeln (BGH NStZ 2008, 396 (396 f.))....
- **[Judge=3]** `['Neunzehnter Abschnitt. Diebstahl und Unterschlagun...']` — Direkt relevant - behandelt gesuchte Abgrenzung § 263/263a
  > 4), Computerbetrug (§ 263a Abs....
- **[Judge=3]** `['Zweiundzwanzigster Abschnitt. Betrug und Untreue']` — Direkt relevant: behandelt exakt Betrug vs Computerbetrug
  > (Teil 1), GA 2023, 615; (Teil 2) GA 2023, 675; Schuhr, Betrug vs. Computerbetrug....