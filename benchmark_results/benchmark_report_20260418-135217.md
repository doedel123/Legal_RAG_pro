# RAG Benchmark Report

_Generiert: 2026-04-18T13:52:17_


- Queries: **18**
- Top-K: **5**
- Systeme: ours, vectara

## Gesamtvergleich

| Metrik | ours | vectara |
|--------|--------|--------|
| nDCG@10 | 0.955 | 0.931 |
| Relevance@10 | 85.6% | 45.6% |
| Relevance@3 | 87.0% | 59.3% |
| Top-1-Score | 2.72 | 2.17 |
| Mean-Score | 2.54 | 1.51 |
| Latenz (s) | 10.99 | 1.99 |

## Nach Kategorie


### alltagssprache

| Metrik | ours | vectara |
|--------|--------|--------|
| nDCG@10 | 0.990 | 0.879 |
| Relevance@10 | 95.0% | 25.0% |
| Relevance@3 | 100.0% | 41.7% |

### cross-reference

| Metrik | ours | vectara |
|--------|--------|--------|
| nDCG@10 | 0.932 | 0.935 |
| Relevance@10 | 93.3% | 66.7% |
| Relevance@3 | 88.9% | 77.8% |

### exakte-paragraphen

| Metrik | ours | vectara |
|--------|--------|--------|
| nDCG@10 | 0.990 | 0.948 |
| Relevance@10 | 95.0% | 55.0% |
| Relevance@3 | 100.0% | 75.0% |

### konzept

| Metrik | ours | vectara |
|--------|--------|--------|
| nDCG@10 | 0.925 | 0.958 |
| Relevance@10 | 70.0% | 40.0% |
| Relevance@3 | 75.0% | 50.0% |

### stpo-prozess

| Metrik | ours | vectara |
|--------|--------|--------|
| nDCG@10 | 0.923 | 0.941 |
| Relevance@10 | 73.3% | 46.7% |
| Relevance@3 | 66.7% | 55.6% |

## Detail pro Query


### q01 — exakte-paragraphen

**Query:** Welche Voraussetzungen hat der gewerbsmaessige Bandenbetrug nach § 263 Abs. 5 StGB?

**Kontext:** Qualifikationstatbestand des Bandenbetrugs im Fischer-Kommentar

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours | 0.99 | 80% | 100% | 3 | 14.6s |
| vectara | 0.98 | 60% | 100% | 3 | 2.0s |

#### ours — Top 3
- **[Judge=3]** `§ 263 StGB – BT. Zweriindzwanzigster Abschnitt – Rn. 225` — Behandelt direkt die Voraussetzungen des § 263 Abs. 5
  > IV. Qualifikation (Abs. 5). Abs. 5 enthält einen Qualifikationstatbestand, der die Tat in Fällen kumulativ gewerbs- und bandenmäßiger Begehung zum Verbrechen macht. Die Qualifikation ist in die Urteil...
- **[Judge=3]** `§ 263 StGB – I. Vermögensbegriff  – Rn. 263` — Direkte Antwort: enthält § 263 Abs. 5
  > 263 (1) Wer in der Absicht, sich oder einem Dritten einen rechtswidrigen Vermögensvorteil zu verschaffen, das Vermögen eines anderen dadurch beschädigt, daß er durch Vorspiegelung falscher oder durch ...
- **[Judge=3]** `§ 263 StGB – BT. Zweijundzwanzigster Abschnitt – Rn. 213` — Direkt relevant: behandelt Abs. 5 Qualifikationsvoraussetzungen
  > 213 Sind beide Varianten erfüllt, ist eine Qualifikation nach Abs. 5 gegeben. Die Abgrenzung des Abs. 3 Nr. 1 zum Verbrechen nach Abs. 5 ist in Fällen bandenmäßiger Begehung schwierig, denn eine auf f...

#### vectara — Top 3
- **[Judge=3]** `['Übersicht']` — Direkt relevant: behandelt § 263 Abs. 5 Voraussetzungen
  > § 263 ist unter den Voraussetzungen von Abs....
- **[Judge=2]** `['Neunzehnter Abschnitt. Diebstahl und Unterschlagun...']` — Behandelt Bandenbetrug, aber nur Rechtsprechungsverweise
  > dazu BGHSt 47, 214 (216)); StraFo 2007, 78 (78 f.); NStZ 2002, 375 (377); 2007, 288 (289); 2008, 54 (Bandenbetrug; § 263 Abs....
- **[Judge=3]** `['Übersicht']` — Direkt relevanter Paragraph § 263 Abs. 5 StGB
  > 3 Nr. 5), weiterhin § 263 Abs....

### q02 — exakte-paragraphen

**Query:** Was regelt § 112 StPO zur Untersuchungshaft?

**Kontext:** Anordnungsvoraussetzungen der U-Haft (dringender Tatverdacht, Haftgrund) im Schmitt/Koehler

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours | 1.00 | 100% | 100% | 3 | 10.6s |
| vectara | 0.98 | 60% | 67% | 3 | 1.6s |

#### ours — Top 3
- **[Judge=3]** `§ 112 StPO – Rn. 112` — Direkt relevant: § 112 StPO Volltext mit Haftgruenden
  > 112 (1) ¹ Die Untersuchungshaft darf gegen den Beschuldigten angeordnet werden, wenn er der Tat dringend verdächtig ist und ein Haftgrund besteht. ² Sie darf nicht angeordnet werden, wenn sie zu der B...
- **[Judge=3]** `§ 112 StPO – III. Flucht (Abs – Rn. 32 (Teil 2)` — Direkt relevant zu Verdunkelungsgefahr als Haftgrund
  > Wenn die Verdunkelungshandlungen nicht geeignet sind, die Ermittlung der Wahrheit zu erschweren, darf UHaft nicht angeordnet werden. Der Haftgrund liegt daher nicht vor, wenn der Sachverhalt schon in ...
- **[Judge=3]** `§ 112 StPO – Rn. 112` — Direkt relevante Erläuterung der Haftbefehlsvoraussetzungen nach § 112 StPO
  > Haftunfähigkeit des Beschuldigten schließt den Erlass des Haftbefehls nicht aus, sondern hindert nur seinen Vollzug (OLG Düsseldorf JZ 1984, 248; OLG Frankfurt a.M. NJW 1968, 2302; OLG Nürnberg OLGSt ...

#### vectara — Top 3
- **[Judge=3]** `['Notveräußerung']` — Direkt relevant - behandelt exakt § 112 StPO
  > StPO § 112 Erstes Buch....
- **[Judge=3]** `['Notveräußerung']` — Direkt relevanter Paragraph zu Untersuchungshaft-Anordnungsvoraussetzungen
  > StPO § 112 Erstes Buch....
- **[Judge=1]** `['Übersicht']` — Nachbarparagraph, behandelt Haftlockerung statt Anordnungsvoraussetzungen
  > Verhaftung und vorläufige Festnahme § 116b StPO ckung von Untersuchungshaft vor, es sei denn, das Gericht trifft eine abweichende Entscheidung, weil der Zweck der Untersuchungshaft dies erfordert....

### q03 — exakte-paragraphen

**Query:** Welche Haftgruende nennt § 112 Abs. 2 StPO?

**Kontext:** Fluchtgefahr, Verdunkelungsgefahr, Flucht — im StPO-Kommentar

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours | 1.00 | 100% | 100% | 3 | 6.9s |
| vectara | 0.90 | 20% | 33% | 1 | 1.4s |

#### ours — Top 3
- **[Judge=3]** `§ 112 StPO – Rn. 112` — Direkt relevant: vollständige Aufzählung aller Haftgründe
  > 112 (1) ¹ Die Untersuchungshaft darf gegen den Beschuldigten angeordnet werden, wenn er der Tat dringend verdächtig ist und ein Haftgrund besteht. ² Sie darf nicht angeordnet werden, wenn sie zu der B...
- **[Judge=3]** `§ 112 StPO – III. Flucht (Abs – Rn. 23` — Behandelt direkt die Haftgruende des § 112 Abs. 2 StPO
  > Bei einer besonders hohen Straferwartung braucht daher nur geprüft zu werden, ob Umstände vorhanden sind, die die hieraus herzuleitende Fluchtgefahr ausräumen können (KG StV 1996, 383; OLG München Str...
- **[Judge=3]** `§ 112 StPO – III. Flucht (Abs – Rn. 32 (Teil 2)` — Direkte Erläuterung Verdunkelungsgefahr aus § 112 Abs. 2
  > Wenn die Verdunkelungshandlungen nicht geeignet sind, die Ermittlung der Wahrheit zu erschweren, darf UHaft nicht angeordnet werden. Der Haftgrund liegt daher nicht vor, wenn der Sachverhalt schon in ...

#### vectara — Top 3
- **[Judge=1]** `['Vorbemerkung zu §§ 211–217']` — Erwähnt § 112 Abs., aber ohne Haftgründe-Details
  > 2 Nr. 1 Buchst. h StPO; UHaft § 112 Abs....
- **[Judge=2]** `['7. Untersuchungshaft, einstweilige Unterbringung u...']` — Verweist auf § 112 Abs. 2, aber nennt keine Haftgründe
  > (4) Besteht in den Fällen des § 112 Absatz 3 und des § 112a Absatz 1 StPO auch ein Haftgrund nach § 112 Absatz 2 StPO, sind die Feststellungen hierüber aktenkundig zu machen....
- **[Judge=1]** `['Verfahren bei der Haftprüfung']` — Erwähnt § 112, aber keine Haftgründe selbst
  > 17) auch auf einen Haftgrund nach § 112 gestützt, so findet § 122a keine Anwendung (KK-StPO/Gericke Rn....

### q04 — exakte-paragraphen

**Query:** Was regelt § 102 StPO zur Durchsuchung beim Beschuldigten?

**Kontext:** Durchsuchungsvoraussetzungen beim Verdaechtigen

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours | 0.97 | 100% | 100% | 3 | 10.4s |
| vectara | 0.94 | 80% | 100% | 2 | 1.5s |

#### ours — Top 3
- **[Judge=3]** `§ 102 StPO – Rn. 102` — Direkter Wortlaut und Kommentierung zu § 102 StPO
  > 102 Bei dem, welcher als Täter oder Teilnehmer einer Straftat oder der Datenhehlerei, Begünstigung, Strafvereitelung oder Hehlerei  Köhler    Ermittlungsmaßnahmen  verdächtig ist, kann eine Durchsuchu...
- **[Judge=2]** `§ 102 StPO – Rn. 10` — Behandelt Durchsuchungsvoraussetzungen, aber nicht spezifisch § 102
  > II. Auffinden von Beweismitteln. Zu den Beweismitteln (→ § 94 Rn. 4 ff.) gehören auch die nur in § 103 erwähnten Spuren (SK-StPO/Jäger/Wohlers Rn. 21) u. Personen, die zu Beweiszwecken in Augenschein ...
- **[Judge=3]** `§ 102 StPO – Rn. 10` — Direkt zu § 102 StPO Durchsuchungsgegenstand beim Beschuldigten
  > 10 III. Sachen. Sachen sind Kleidungsstücke, die der Verdächtige bei sich führt, ohne sie zu tragen, u. seine sonstige bewegliche Habe, gleichgültig, ob sie sich in seinem Umkreis, zB in Gepäckstücken...

#### vectara — Top 3
- **[Judge=2]** `['Übersicht']` — Erwähnt § 102 StPO, aber nur fragmentarisch
  > 27); denn nach § 102 ist sogar die Durchsuchung zum Zweck der Ergreifung zulässig (→ § 102 Rn....
- **[Judge=3]** `['Durchsuchung bei anderen Personen']` — Behandelt direkt § 102 StPO und Durchsuchungszweck
  > 2 stattfindet. Wenn dadurch der Untersuchungserfolg nicht gefährdet wird, sollte der Durchsuchungszweck auch im Fall des § 102 dem Verdächtigen bekanntgegeben werden (KK-StPO/Henrichs/Weingast Rn....
- **[Judge=2]** `['Entschädigung für andere Strafverfolgungsmaßnahmen...']` — Erwähnt § 102 StPO aber ohne inhaltliche Details
  > Durchsuchung iS Nr. 4 ist nur die nach §§ 102, 103 StPO, nicht die nach § 111 StPO (Meyer StrEG Rn....

### q05 — konzept

**Query:** Wann liegt eine konkludente Taeuschung im Sinne des § 263 StGB vor?

**Kontext:** Taeuschungshandlung durch schluessiges Verhalten

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours | 0.77 | 60% | 33% | 1 | 12.2s |
| vectara | 0.95 | 20% | 33% | 3 | 3.4s |

#### ours — Top 3
- **[Judge=1]** `§ 263 StGB – I. Vermögensbegriff  – Rn. 263` — Gesetzestext ohne konkludente Taeuschung Erklaerung
  > 263 (1) Wer in der Absicht, sich oder einem Dritten einen rechtswidrigen Vermögensvorteil zu verschaffen, das Vermögen eines anderen dadurch beschädigt, daß er durch Vorspiegelung falscher oder durch ...
- **[Judge=1]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 38` — Behandelt Betrug § 263, aber Täuschung durch Unterlassen
  > 38 4. Täuschung durch Unterlassen. Eine Täuschung kann nach hM (aA Grünwald FS H. Mayer, 1966, 281; Kargl ZStW 119 (2007), 250 (287) mwN) auch durch Unterlassen begangen werden, wenn eine Garantenpfli...
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 14` — Direkt relevant: behandelt konkludente Taeuschung bei § 263
  > Rspr. und hM bejahen darüber hinaus aber die Möglichkeit einer Täuschung durch Unterlassen auch ohne Erklärung gegenüber dem Irrenden (→ Rn. 38; vgl. BGHSt 39, 392 (398); BayObLG NJW 1987, 1654 (mAnm ...

#### vectara — Top 3
- **[Judge=3]** `['Übersicht']` — Definiert konkludente Taeuschung bei Kartenmissbrauch direkt
  > 12a f.). Bei kollusivem Zusammenwirken zwischen Karteninhaber und Zahlungsannehmer (Vertragsunternehmen) liegt idR eine (konkludente) Täuschung des Ausstellers über die Voraussetzungen der Zahlungspfl...
- **[Judge=0]** `['Vorführung einer aufgezeichneten Zeugenvernehmung']` — Behandelt Tateinheit bei anderen Delikten
  > Tateinheit u. eine Tat im prozessualen Sinne liegt etwa bei Zusammen treffen v. Betäubungsmitteldelikten und Verstößen nach dem WaffG vor, Schmitt 1467 ***...
- **[Judge=1]** `['Übersicht']` — Behandelt § 263, aber nicht konkludente Täuschung
  > → § 263 Rn. 193). Liegt auch Betrugsvorsatz vor, geht § 263 vor (→ Rn....

### q06 — konzept

**Query:** Was ist eine Vermoegensverfuegung und welche Anforderungen stellt die Rechtsprechung?

**Kontext:** Tatbestandsmerkmal der Vermoegensverfuegung beim Betrug

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours | 0.93 | 60% | 67% | 3 | 16.6s |
| vectara | 1.00 | 0% | 0% | 1 | 2.8s |

#### ours — Top 3
- **[Judge=3]** `§ 263 StGB – BT. Zweitundzwanzigster Abschnitt – Rn. 69` — Definiert Vermoegensverfuegung und zentrale Anforderungen direkt
  > 69 Anders ist es, wenn der Verfügende seinerseits nur (gutgläubige) Hilfsperson eines bösgläubigen Dritten ist. Hier ist auf den Irrtum des Entscheidungsbefugten abzustellen: Erkennt dieser die Unrich...
- **[Judge=1]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 87` — Kausalität und Vermögensschaden, nicht Verfügungsbegriff selbst
  > 87 5. Kausalität. Für die Vermögensverfügung muss der täuschungsbedingte Irrtum kausal sein (vgl. BGHSt 24, 257 (260); 24, 386 (389); NStZ 2003, 313 (314 f.); OLG Düsseldorf NJW 1987, 3145); Mitverurs...
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 74` — Definiert Vermoegensverfuegung und zentrale Rechtsprechungsanforderungen
  > 74 2. Verfügungsbewusstsein. Vermögensverfügungen sind nach hM grundsätzlich sowohl als bewusst als auch als unbewusst vermögensmindernde Handlungen möglich; eine aktuelle Vorstellung des Verfügenden ...

#### vectara — Top 3
- **[Judge=1]** `['Übersicht']` — Allgemeine Anforderungen, nicht spezifisch zu Vermoegensverfuegung
  > Maßgeblich sind die Anforderungen, welche die Rechtsordnung an jedermann stellt (BGHSt 43, 66 (77); NStZ-RR 1999, 295 (296); 2015, 137 (138))....
- **[Judge=0]** `['Vorführung bei vorläufiger Festnahme']` — Beweisrecht, nicht Betrug oder Vermoegensverfuegung
  > Gerichtsbeschlusses vortragen; denn an die Aufklärungsrüge können nicht geringere Anforderungen gestellt werden als an die Rüge fehlerhafter Ablehnung eines Beweisantrags (BGH NStZ 1984, 329; 2015, 54...
- **[Judge=0]** `['Übersicht']` — Behandelt Einwilligung, nicht Vermoegensverfuegung beim Betrug
  > 1 S. 2). Damit die Einwilligung rechtswirksam ist, muss ihr eine Belehrung vorausgehen, welche den Anforderungen des Abs....

### q07 — konzept

**Query:** Was versteht man unter einem Gefaehrdungsschaden beim Betrug?

**Kontext:** Schadensbegriff, schadensgleiche Vermoegensgefaehrdung

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours | 1.00 | 100% | 100% | 3 | 11.2s |
| vectara | 1.00 | 80% | 100% | 3 | 2.8s |

#### ours — Top 3
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 159` — Definiert direkt den Gefährdungsschaden beim Betrug
  > 159 b) Voraussetzungen. aa) Ein Gefährdungsschaden ist gegeben, wenn die Wahrscheinlichkeit des endgültigen Verlusts eines Vermögensbestandteils zum Zeitpunkt der täuschungsbedingten Verfügung so groß...
- **[Judge=3]** `§ 263 StGB – BT. Zwei undzwanzigster Abschnitt – Rn. 263 (Te` — Direkt relevant: behandelt Gefährdungsschaden beim Betrug
  > Fischer/Lutz    Betrug und Untreue   rechts für das Strafrecht, FS Weber, 2004, 271; Eisele/Bechtel, Der Schadensbegriff bei den Vermögensdelikten, JuS 2018, 97; Ellbogen/Wichmann, Zu Problemen des är...
- **[Judge=3]** `§ 263 StGB – BT. Zwei undzwanzigster Abschnitt – Rn. 263` — Behandelt direkt Gefährdungsschaden bei Betrug
  > **Rechtsprechungsübersicht:** Scholz, Die Entwicklung des Berufs- und Vertragsarztrechts, medstra 2019, 331; 2021, 349; 2022, 355; 2023, 355; 2024, 351.  Weinrich/Wostry, Der Abrechnungsbetrug in der ...

#### vectara — Top 3
- **[Judge=3]** `['Zweiundzwanzigster Abschnitt. Betrug und Untreue']` — Definiert direkt Gefährdungsschaden beim Betrug mit BGH-Beispielen
  > einen vollendeten Betrug durch Entstehen eines Gefährdungsschadens an, wenn aufgrund tauschender Erklärungen dem Täter ein Überziehungskredit eingeräumt oder Karten mit Einlösungsgarantie ausgehändigt...
- **[Judge=3]** `['Zweiundzwanzigster Abschnitt. Betrug und Untreue']` — Definiert direkt den Begriff Gefaehrdungsschaden
  > Vollendung. Vollendet ist der Betrug mit dem zumindest teilweisen Eintritt des Vermögensschadens (auch als Gefährdungsschaden iSv → Rn....
- **[Judge=3]** `['Zweiundzwanzigster Abschnitt. Betrug und Untreue']` — Definiert Gefährdungsschaden bei Betrug konkret
  > StS entschieden, der Vollendung eines (Eingehungs-)Betrugs stehe auch bei täuschendem Abschluss von Lebensversicherungen (zur Geldbeschaffung durch Vortäuschung des Versicherungsfalls) nicht entgegen,...

### q08 — konzept

**Query:** Wie wird der Vorsatz beim Betrug bestimmt, insbesondere die Bereicherungsabsicht?

**Kontext:** Subjektiver Tatbestand § 263 StGB

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours | 1.00 | 60% | 100% | 3 | 8.7s |
| vectara | 0.88 | 60% | 67% | 1 | 1.9s |

#### ours — Top 3
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 176` — Behandelt direkt Vorsatz bei Betrug inklusive Bereicherungsabsicht
  > D. Subjektiver Tatbestand. § 263 setzt Vorsatz voraus; darüber hinaus ist die Absicht rechtswidriger Bereicherung erforderlich.   I. Vorsatz. 1. Täuschungsvorsatz. Der Vorsatz (bedingter Vorsatz genüg...
- **[Judge=3]** `§ 263 StGB – I. Sonstige Vorschriften 239 – Rn. 263 (Teil 1)` — Behandelt direkt Bereicherungsabsicht und Vorsatz bei Betrug
  > 3. Einzelne Fallgruppen ... 92 4. Rechtlich missbilligte, sittenwidrige und gesetzeswidrige wirtschaftliche Werte ... 101 VI. Schaden ... 110 1. Grundsätze der Schadensermittlung ... 111 2. Vermögensm...
- **[Judge=3]** `§ 263 StGB – BT. Zweijundzwanzigster Abschnitt – Rn. 194` — Behandelt direkt Vorsatz bei Bereicherungsabsicht § 263
  > 194 4. Vorsatz hinsichtlich der Rechtswidrigkeit. Die Rechtswidrigkeit des angestrebten Vermögensvorteils muss vom Vorsatz umfasst sein; sie ist wie bei § 253 (vgl. dort 20) subjektives Tatbestandsmer...

#### vectara — Top 3
- **[Judge=1]** `['Zweiundzwanzigster Abschnitt. Betrug und Untreue']` — Versicherungsbetrug spezifisch, nicht allgemeine Vorsatzbestimmung
  > Der Vortäter muss Vorsatz auch hinsichtlich des späteren Versicherungsbetrugs gehabt haben; wenn der Täter die Vortat nur betrügerisch ausnutzt, liegt nur Abs....
- **[Judge=2]** `['Erpressung']` — Erwähnt Bereicherung bei Betrug, aber unvollständiger Kontext
  > Zwischen Schaden und (beabsichtigter) Bereicherung muss, wie beim Betrug (vgl....
- **[Judge=2]** `['Zweiundzwanzigster Abschnitt. Betrug und Untreue']` — Behandelt Bereicherungsabsicht, aber nur bei Gewerbsmäßigkeit
  > Gewerbsmäßigkeit setzt eigennütziges Handeln voraus; fremdnütziger Betrug reicht daher nur aus, wenn die Bereicherung dem Täter zumindest mittelbar zugutekommen soll (NStZ 2008, 282 (282 f.); wistra 2...

### q09 — alltagssprache

**Query:** Hat der Angeklagte die Kunden über das Internet betrogen?

**Kontext:** Abstrakte Frage zu Internetbetrug, sucht Taeuschungshandlung + Schaden

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours | 0.99 | 100% | 100% | 3 | 9.0s |
| vectara | 0.69 | 40% | 67% | 0 | 1.0s |

#### ours — Top 3
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 176` — Direkt relevant: Vorsatz bei Betrug, Täuschungs- und Schadensvorsatz
  > D. Subjektiver Tatbestand. § 263 setzt Vorsatz voraus; darüber hinaus ist die Absicht rechtswidriger Bereicherung erforderlich.   I. Vorsatz. 1. Täuschungsvorsatz. Der Vorsatz (bedingter Vorsatz genüg...
- **[Judge=3]** `§ 263 StGB – I. Vermögensbegriff  – Rn. 263` — Betrug-Grundtatbestand, direkt relevant für Internetbetrug
  > 263 (1) Wer in der Absicht, sich oder einem Dritten einen rechtswidrigen Vermögensvorteil zu verschaffen, das Vermögen eines anderen dadurch beschädigt, daß er durch Vorspiegelung falscher oder durch ...
- **[Judge=2]** `§ 263 StGB – BT. Zweitundzwanzigster Abschnitt – Rn. 69` — Behandelt Betrug allgemein, aber nicht speziell Internetbetrug
  > 69 Anders ist es, wenn der Verfügende seinerseits nur (gutgläubige) Hilfsperson eines bösgläubigen Dritten ist. Hier ist auf den Irrtum des Entscheidungsbefugten abzustellen: Erkennt dieser die Unrich...

#### vectara — Top 3
- **[Judge=0]** `['Notwendige Auslagen des Nebenklägers']` — Fragment ohne erkennbaren Bezug zu Internetbetrug
  > hat der Angeklagte die dadurch entstandenen bes....
- **[Judge=3]** `['Übersicht']` — Direkt relevant zu Internetbetrug und Taeuschungshandlungen online
  > Der Tatbestand ist aber erfüllt bei Anlegen eines online-Kundenkontos unter Identitätstäuschung (aber nicht bei Bevollmächtigung des Dritten: BeckRS 2024, 11811), ebenso bei Verändern eines bestehende...
- **[Judge=3]** `['Übersicht']` — Direkt relevant: Internetbetrug und Täuschungshandlung
  > Wird ein Online-Kundenkonto unter fremdem Namen zum Zwecke des nachfolgenden Betrugs angelegt, hat dies zur Folge, dass alle nachfolgenden betrügerischen Vorgänge mittels dieses Kundenkontos in Tatein...

### q10 — alltagssprache

**Query:** Wann darf die Polizei bei jemandem zu Hause suchen?

**Kontext:** Durchsuchungsvoraussetzungen, §§ 102 ff. StPO

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours | 0.97 | 80% | 100% | 3 | 7.1s |
| vectara | 0.82 | 20% | 33% | 1 | 1.4s |

#### ours — Top 3
- **[Judge=3]** `§ 102 StPO – Rn. 102` — Direkt relevant für Durchsuchungsvoraussetzungen der Wohnung
  > 102 Bei dem, welcher als Täter oder Teilnehmer einer Straftat oder der Datenhehlerei, Begünstigung, Strafvereitelung oder Hehlerei  Köhler    Ermittlungsmaßnahmen  verdächtig ist, kann eine Durchsuchu...
- **[Judge=2]** `§ 102 StPO – Rn. 10` — Behandelt Durchsuchungsvoraussetzungen, aber fokussiert auf Beweismittel
  > II. Auffinden von Beweismitteln. Zu den Beweismitteln (→ § 94 Rn. 4 ff.) gehören auch die nur in § 103 erwähnten Spuren (SK-StPO/Jäger/Wohlers Rn. 21) u. Personen, die zu Beweiszwecken in Augenschein ...
- **[Judge=3]** `§ 102 StPO – Rn. 3` — Definiert zentrale Durchsuchungsvoraussetzungen und -gegenstände
  > **Teilnehmer** nach §§ 25 ff. StGB, nicht die sog. notwendigen Teilnehmer (zum Begriff: Fischer/Fischer StGB Vor § 25 Rn. 7), stehen den Tatverdächtigen gleich. Bei jedem v. ihnen sowie bei den der Be...

#### vectara — Top 3
- **[Judge=1]** `Beck'sche Kurz-Kommentare` — Behandelt Fahndung, nicht Durchsuchungsvoraussetzungen
  > auch Nummer 43), wenn der Haftbefehl (Unterbringungsbefehl) zur Auslösung einer gezielten Fahndung der für den mutmaßlichen Wohnsitz des Gesuchten zuständigen Polizeidienststelle übersandt wird....
- **[Judge=3]** `['Zuständigkeit für weitere gerichtliche Entscheidun...']` — Direkt relevant: Durchsuchung Wohnung des Verdächtigen
  > 28 ff.). Die Wohnung des Verdächtigen darf durchsucht werden, wenn konkrete Anhaltspunkte dafür bestehen, dass er dort aufzufinden ist (Kaiser NJW 1980, 876)....
- **[Judge=1]** `['Durchsuchung bei anderen Personen']` — Personendurchsuchung, nicht Wohnungsdurchsuchung behandelt
  > Bei der Personendurchsuchung darf körperlicher Zwang angewendet werden; falls geboten, zB falls konkrete Verdunkelungsmaßnahmen drohen, darf der Betroffene auch kurzfristig festgenommen u. auf der Pol...

### q11 — alltagssprache

**Query:** Was passiert wenn jemand luegt damit er Geld bekommt?

**Kontext:** Laienhafte Umschreibung des Betrugstatbestandes

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours | 1.00 | 100% | 100% | 3 | 8.3s |
| vectara | 1.00 | 20% | 33% | 2 | 1.0s |

#### ours — Top 3
- **[Judge=3]** `§ 263 StGB – I. Vermögensbegriff  – Rn. 263` — Direkt relevanter Betrugstatbestand § 263 StGB
  > 263 (1) Wer in der Absicht, sich oder einem Dritten einen rechtswidrigen Vermögensvorteil zu verschaffen, das Vermögen eines anderen dadurch beschädigt, daß er durch Vorspiegelung falscher oder durch ...
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 5` — Direkt relevant: Betrugstatbestand mit Täuschung für Vermögensvorteil
  > 5 C. Grundtatbestand, Abs. 1. Tathandlung ist das Täuschen einer natürlichen Person (vgl. NStZ 2005, 213) über Tatsachen. Erfolg dieser Handlung muss ein Irrtum des Täuschungsadressaten sein; dieser m...
- **[Judge=3]** `§ 263 StGB – BT. Zweitundzwanzigster Abschnitt – Rn. 69` — Direkt relevant: Betrug §263, Vermögensverfügung durch Täuschung
  > 69 Anders ist es, wenn der Verfügende seinerseits nur (gutgläubige) Hilfsperson eines bösgläubigen Dritten ist. Hier ist auf den Irrtum des Entscheidungsbefugten abzustellen: Erkennt dieser die Unrich...

#### vectara — Top 3
- **[Judge=2]** `['Geldwäsche']` — Betrug-Kontext, aber spezieller Teilaspekt der Beteiligung
  > Für einen Finanzagenten kommt eine Beteiligung an der Vorrat des Betrugs in Betracht, wenn er den Hintermännern sein Bankkonto zur Verfügung stellt, damit die Geschädigten tatplankonform Geld darauf ü...
- **[Judge=0]** `['Übersicht']` — Fragment ohne Bezug zu Betrug oder Täuschung
  > Was er damit iErg bezweckt (Flucht, Vermeidung des Arbeitszwangs usw.)...
- **[Judge=0]** `['Geldfälschung']` — Geldfälschung, nicht Betrug durch Lügen
  > Daher ist Geld „nachgemacht", wenn dem Täter die Legitimation zur Herstellung fehlt (vgl....

### q12 — alltagssprache

**Query:** Wann muss jemand ins Gefaengnis waehrend die Tat noch nicht bewiesen ist?

**Kontext:** Untersuchungshaft, §§ 112 ff. StPO

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours | 1.00 | 100% | 100% | 3 | 12.5s |
| vectara | 1.00 | 20% | 33% | 3 | 2.2s |

#### ours — Top 3
- **[Judge=3]** `§ 112 StPO – Rn. 112` — Definiert Untersuchungshaft-Voraussetzungen vor Verurteilung komplett
  > 112 (1) ¹ Die Untersuchungshaft darf gegen den Beschuldigten angeordnet werden, wenn er der Tat dringend verdächtig ist und ein Haftgrund besteht. ² Sie darf nicht angeordnet werden, wenn sie zu der B...
- **[Judge=3]** `§ 112 StPO – III. Flucht (Abs – Rn. 23` — Direkt relevant: behandelt Haftgruende der Untersuchungshaft
  > Bei einer besonders hohen Straferwartung braucht daher nur geprüft zu werden, ob Umstände vorhanden sind, die die hieraus herzuleitende Fluchtgefahr ausräumen können (KG StV 1996, 383; OLG München Str...
- **[Judge=3]** `§ 112 StPO – Rn. 112` — Direkt relevant: Haftbefehl-Voraussetzungen bei Untersuchungshaft
  > Haftunfähigkeit des Beschuldigten schließt den Erlass des Haftbefehls nicht aus, sondern hindert nur seinen Vollzug (OLG Düsseldorf JZ 1984, 248; OLG Frankfurt a.M. NJW 1968, 2302; OLG Nürnberg OLGSt ...

#### vectara — Top 3
- **[Judge=3]** `['Übersicht']` — Direkt relevant: behandelt 'noch nicht bewiesen' Begriff
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
| ours | 0.93 | 60% | 67% | 3 | 13.3s |
| vectara | 0.94 | 60% | 67% | 3 | 2.0s |

#### ours — Top 3
- **[Judge=3]** `§ 112 StPO – Rn. 112` — Direkt relevant, zeigt konkrete Fluchtgefahr-Voraussetzungen in § 112
  > 112 (1) ¹ Die Untersuchungshaft darf gegen den Beschuldigten angeordnet werden, wenn er der Tat dringend verdächtig ist und ein Haftgrund besteht. ² Sie darf nicht angeordnet werden, wenn sie zu der B...
- **[Judge=1]** `§ 112 StPO – III. Flucht (Abs – Rn. 23` — Behandelt Verdunkelungsgefahr statt Fluchtgefahr
  > Bei einer besonders hohen Straferwartung braucht daher nur geprüft zu werden, ob Umstände vorhanden sind, die die hieraus herzuleitende Fluchtgefahr ausräumen können (KG StV 1996, 383; OLG München Str...
- **[Judge=3]** `§ 112 StPO – III. Flucht (Abs – Rn. 17 (Teil 1)` — Definiert direkt Fluchtgefahr nach § 112 Abs. 2 Nr. 2 StPO
  > 17 IV. Fluchtgefahr (Abs. 2 Nr. 2). Fluchtgefahr (Abs. 2 Nr. 2) besteht, wenn die Würdigung der Umstände des Falles es wahrscheinlicher macht, dass sich der Beschuldigte dem Strafverfahren entziehen, ...

#### vectara — Top 3
- **[Judge=3]** `['Haftgrund der Wiederholungsgefahr']` — Direkt relevante Voraussetzungen für Fluchtgefahr-Untersuchungshaft
  > (2) In diesen Fällen darf die Untersuchungshaft wegen Fluchtgefahr nur angeordnet werden, wenn der Beschuldigte 1....
- **[Judge=1]** `['Fünfter Unterabschnitt. Verfahren bei Aussetzung d...']` — Jugendstrafrecht, nicht allgemeine Fluchtgefahr-Voraussetzungen
  > (2) Solange der Jugendliche das sechzehnte Lebensjahr noch nicht vollendet hat, ist die Verhängung von Untersuchungshaft wegen Fluchtgefahr nur zulässig, wenn er 1....
- **[Judge=3]** `['Haftgrund der Wiederholungsgefahr']` — Direkt relevante Voraussetzungen für Fluchtgefahr-Untersuchungshaft
  > 4 Anordnung wegen Fluchtgefahr nur, wenn außer den Voraussetzungen des § 112 Abs....

### q14 — stpo-prozess

**Query:** Wie lange darf die Untersuchungshaft maximal dauern?

**Kontext:** § 121 StPO Sechs-Monats-Grenze, Haftpruefung OLG

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours | 0.94 | 80% | 67% | 3 | 14.7s |
| vectara | 0.95 | 40% | 67% | 3 | 4.0s |

#### ours — Top 3
- **[Judge=3]** `§ 121 StPO – Rn. 1` — Behandelt direkt maximale Dauer der Untersuchungshaft
  > Eine absolute Höchstgrenze für die Dauer v. UHaft sieht weder die StPO noch die EMRK vor (EGMR EuGRZ 1993, 384). Es kommt auf eine Abwägung aller Umstände des Einzelfalls an. Eine ein Jahr übersteigen...
- **[Judge=1]** `§ 121 StPO` — Behandelt Aufhebung/Übergang, nicht maximale Haftdauer
  > aufheben. An den Antrag, ihn außer Vollzug zu setzen, ist das Gericht nicht gebunden (OLG Celle NStZ 2021, 637 mwN; OLG Düsseldorf StV 2001, 462; KMR-StPO/Winkel Rn. 7; Löwe/Rosenberg/Hilger Rn. 40; a...
- **[Judge=3]** `§ 121 StPO – Rn. 121` — Direkt relevant: beantwortet Frage zur maximalen Haftdauer
  > 121 (1) Solange kein Urteil ergangen ist, das auf Freiheitsstrafe oder eine freiheitsentziehende Maßregel der Besserung und Sicherung erkennt, darf der Vollzug der Untersuchungshaft wegen derselben Ta...

#### vectara — Top 3
- **[Judge=3]** `['Verfahren bei der Haftprüfung']` — Beantwortet direkt die Sechs-Monats-Grenze der Untersuchungshaft
  > 1 vgl. § 123. Fortdauer der Untersuchungshaft über sechs Monate RiStBV 56 121 (1) Solange kein Urteil ergangen ist, das auf Freiheitsstrafe oder eine freiheitsentziehende Maßregel der Besserung und Si...
- **[Judge=1]** `['Haftgrund der Wiederholungsgefahr']` — Sicherungshaft, nicht Untersuchungshaft - anderer Hafttyp
  > Die Höchstdauer der Sicherungshaft beträgt 1 Jahr (§ 122a)....
- **[Judge=3]** `['Verfahren bei der Haftprüfung']` — Direkt relevant: Höchstdauer der Untersuchungshaft
  > 4 S. 2). Höchstdauer der Untersuchungshaft bei Wiederholungsgefahr 122a In den Fällen des § 121 Abs....

### q15 — stpo-prozess

**Query:** Was regelt § 136 StPO zur Beschuldigtenvernehmung?

**Kontext:** Belehrungspflichten, Recht auf Verteidiger

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours | 0.90 | 80% | 67% | 2 | 10.6s |
| vectara | 0.93 | 40% | 33% | 3 | 3.1s |

#### ours — Top 3
- **[Judge=2]** `StPO – III. Steuerstrafverfahren – Rn. 79` — Behandelt informatorische Befragung und Belehrungspflichten nach § 136
  > 79 3. Die informatorische Befragung der Tatverdächtigen, die nach diesen Grundsätzen noch keine Beschuldigten sind, ist Zeugenvernehmung. Die Bestrebungen des Schrifttums, neben Beschuldigte u. Zeugen...
- **[Judge=2]** `§ 500 StPO – ILL. für das Strafverfahren und das Bußgeldverf` — Thematisch relevant: Beschuldigtenvernehmung, aber nicht § 136 StPO
  > (4) Zeugen können zur Aufenthaltsermittlung ausgeschrieben werden.  (5) Für die internationale Fahndung nach Personen, einschließlich der Fahndung nach Personen im SIS und aufgrund eines Europäischen ...
- **[Judge=1]** `§ 55 StPO` — Zeugenauskunftsverweigerung, nicht Beschuldigtenvernehmung nach § 136 StPO
  > Erstes Buch. Sechster Abschnitt  # Auskunftsverweigerungsrecht  RiStBV 65  § 5 (1) Jeder Zeuge kann die Auskunft auf solche Fragen verweigern, deren Beantwortung ihm selbst oder einem der in § 52 Abs....

#### vectara — Top 3
- **[Judge=3]** `['Einleitung']` — Direkt relevant zu § 136 StPO Beschuldigtenvernehmung
  > → StPO § 136 Rn. 3) als Beschuldigtenvernehmung fortzusetzen (BGHSt 22, 129 (132))....
- **[Judge=1]** `Beck'sche Kurz-Kommentare` — Erwähnt § 136 StPO, aber nur Aufzeichnungsaspekt
  > (3) ¹ Hinsichtlich der Möglichkeit und gegebenenfalls Pflicht zur Aufzeichnung der Vernehmung des Beschuldigten in Bild und Ton sind § 136 Absatz 4 StPO bzw....
- **[Judge=1]** `['Einleitung']` — Nur Verweis auf §136, keine inhaltliche Regelung
  > StPO), ferner die Aussagen der Beschuldigten (§§ 136, 163a Abs....

### q16 — cross-reference

**Query:** Worin unterscheidet sich Betrug von Unterschlagung?

**Kontext:** Abgrenzung § 263 vs § 246 StGB

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours | 0.80 | 80% | 67% | 1 | 9.2s |
| vectara | 0.85 | 60% | 67% | 1 | 2.0s |

#### ours — Top 3
- **[Judge=1]** `§ 263 StGB – BT. Zweitundzwanzigster Abschnitt – Rn. 69` — Behandelt nur Betrug, nicht Unterschlagung oder Abgrenzung
  > 69 Anders ist es, wenn der Verfügende seinerseits nur (gutgläubige) Hilfsperson eines bösgläubigen Dritten ist. Hier ist auf den Irrtum des Entscheidungsbefugten abzustellen: Erkennt dieser die Unrich...
- **[Judge=2]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 76` — Behandelt Betrug-Tatbestand, aber nicht direkte Abgrenzung zur Unterschlagung
  > 4. Dreiecksbetrug. Da die Getäuschte und die verfügende, nicht aber die verfügende und die geschädigte Person identisch sein müssen, ist der Tatbestand des § 263 nur erfüllt, wenn die Vermögensverfügu...
- **[Judge=2]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 114` — Betrug-Vermögensschaden relevant, aber keine direkte Abgrenzung
  > 114 a) Quantifizierbarkeit der Vermögensminderung. Die Vermögensminderung muss quantifizierbar sein (RGSt 16, 4; 44, 249; BGHSt 16, 321). Grds. nicht ausreichend ist eine nicht quantifizierbare Einbuß...

#### vectara — Top 3
- **[Judge=1]** `['Erpressung']` — Behandelt Nötigung statt Unterschlagung-Betrug-Abgrenzung
  > Vom Betrug unterscheidet sie sich im Mittel, das dort Täuschung, hier Nötigung ist....
- **[Judge=3]** `['Neunzehnter Abschnitt. Diebstahl und Unterschlagun...']` — Direkte Abgrenzung § 263 vs § 246
  > Gegenüber § 263 tritt § 246 zurück, wenn die Zueignung durch Betrug geschieht; dagegen ist ein der Unterschlagung nachfolgender Sicherungsbetrug mitbestrafte Nachtat....
- **[Judge=2]** `['Zweiundzwanzigster Abschnitt. Betrug und Untreue']` — Behandelt Betrug, aber nicht Abgrenzung zur Unterschlagung
  > Ein (vollendeter) Betrug liegt vor, wenn zum Zeitpunkt des Abschlusses eines Verpflichtungsgeschäfts feststeht, dass der durch Täuschung erlangten Verpflichtung (= Vermögensverfügung) eine (irrtumsbed...

### q17 — cross-reference

**Query:** Was sind die Unterschiede zwischen Diebstahl und Raub?

**Kontext:** § 242 vs § 249 StGB — Abgrenzung durch Gewalt/Drohung

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours | 0.99 | 100% | 100% | 3 | 11.6s |
| vectara | 0.96 | 60% | 67% | 3 | 0.9s |

#### ours — Top 3
- **[Judge=3]** `§ 249 StGB` — Direkt relevant: Raub-Tatbestandsmerkmale, Abgrenzung zu Diebstahl/Erpressung
  > NStZ 2023, 351). Danach ist § 249 gegenüber § 255 ein spezielles Delikt; in jedem Raub liegt eine räuberische Erpressung (aA die hM in der Literatur). Die Unterscheidung richtet sich nach dem äußeren ...
- **[Judge=3]** `§ 249 StGB – BT. Zwanzigster Abschnitt – Rn. 15` — Direkte Abgrenzung Raub-Diebstahl durch Gewalt/Drohung
  > 15 Drohen setzt eine Handlung des Täters im Sinne einer ausdrücklichen oder konkludenten Gedankenäußerung voraus. Eine solche ist nicht schon dann gegeben, wenn der Täter die Furcht des Opfers vor (we...
- **[Judge=3]** `§ 249 StGB – BT. Zwanzigster Abschnitt – Rn. 15` — Direkt relevant: erklärt subjektive Abgrenzung Diebstahl/Raub
  > G. Subjektiver Tatbestand. Der Vorsatz muss entsprechend der Doppelnatur des Raubs sowohl Wegnahme (vgl. dazu → § 242 Rn. 29 ff.) als auch Nötigung (→ § 240 Rn. 53 f.) sowie deren Verknüpfung umfassen...

#### vectara — Top 3
- **[Judge=3]** `['Erpressung']` — Direkt relevant für Abgrenzung Diebstahl/Raub
  > Zur Abgrenzung von (Diebstahl und) Raub vgl....
- **[Judge=2]** `['Zwanzigster Abschnitt. Raub und Erpressung']` — Behandelt Konkurrenzen zwischen Diebstahl und Raub
  > Tateinheit kann zwischen vollendetem Diebstahl und versuchtem Raub gegeben sein (BGHSt 21, 78; NStZ-RR 2005, 202 (203)); zwischen § 250 und § 249 im Fall unterschiedlicher Begehung gegenüber mehreren ...
- **[Judge=1]** `Strafgesetzbuch` — Nur Paragraphenübersicht ohne inhaltliche Abgrenzungskriterien
  > Raub ... § 249Schwerer Raub ... § 250Raub mit Todesfolge ... § 251Räuberischer Diebstahl ... § 252Erpressung ... § 253(weggefallen) ... § 254Räuberische Erpressung ... § 255Führungsaufsicht ... § 256...

### q18 — cross-reference

**Query:** Wann wird Betrug zu Computerbetrug und umgekehrt?

**Kontext:** § 263 vs § 263a StGB — Abgrenzung bei elektronischer Datenverarbeitung

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours | 1.00 | 100% | 100% | 3 | 10.4s |
| vectara | 1.00 | 80% | 100% | 3 | 1.0s |

#### ours — Top 3
- **[Judge=3]** `§ 263a StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 23` — Direkt relevante Abgrenzung § 263 vs § 263a
  > 23 G. Subjektiver Tatbestand. Die Tat setzt (bedingten) Vorsatz voraus. Er muss sich auf alle Tatbestandsmerkmale, zu denen auch die Unbefugtheit (→ Rn. 10) gehört, dh auch auf die Voraussetzungen ers...
- **[Judge=3]** `§ 263a StGB – M. Sonstige Vorschriften 40 – Rn. 239` — Definiert § 263a direkt, zentral für Abgrenzungsfrage
  > 239 I. Sonstige Vorschriften. FAufsicht §§ 263 Abs. 5, 68 Abs. 1. Zuständigkeit in Wirtschaftsstrafaschen § 74c Abs. 1 Nr. 6, § 74e Nr. 2 GVG iVm § 103 Abs. 2 JGG. TKÜ § 100a Abs. 2 Nr. 1 Buchst. n St...
- **[Judge=3]** `§ 263a StGB – L. Konkurrenzen – Rn. 33` — Direkt relevant: Abgrenzung § 263/263a bei gleichen Schäden
  > II. Verhältnis zu sonstigen Tatbeständen. § 263a und § 263 schließen sich aus, wenn derselbe Schaden sowohl durch die Manipulationsweisen des § 263a als auch durch Täuschung bewirkt wird. Mit § 263 is...

#### vectara — Top 3
- **[Judge=3]** `['Übersicht']` — Direkte Abgrenzung Betrug zu Computerbetrug
  > Ebenso ist das Verhältnis zwischen (möglicher) Beteiligung am Betrug und (sicherem) späterem Computerbetrug hinsichtlich desselben Schadens zu behandeln (BGH NStZ 2008, 396 (396 f.))....
- **[Judge=3]** `['Neunzehnter Abschnitt. Diebstahl und Unterschlagun...']` — Direkt relevant - behandelt § 263a Computerbetrug
  > 4), Computerbetrug (§ 263a Abs....
- **[Judge=3]** `['Zweiundzwanzigster Abschnitt. Betrug und Untreue']` — Direkt relevant - behandelt Abgrenzung Betrug/Computerbetrug
  > (Teil 1), GA 2023, 615; (Teil 2) GA 2023, 675; Schuhr, Betrug vs. Computerbetrug....