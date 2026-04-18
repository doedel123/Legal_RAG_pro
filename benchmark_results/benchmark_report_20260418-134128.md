# RAG Benchmark Report

_Generiert: 2026-04-18T13:41:28_


- Queries: **18**
- Top-K: **5**
- Systeme: ours, vectara

## Gesamtvergleich

| Metrik | ours | vectara |
|--------|--------|--------|
| nDCG@10 | 0.961 | 0.874 |
| Relevance@10 | 85.6% | 42.2% |
| Relevance@3 | 85.2% | 46.3% |
| Top-1-Score | 2.83 | 1.56 |
| Mean-Score | 2.49 | 1.50 |
| Latenz (s) | 10.07 | 1.49 |

## Nach Kategorie


### alltagssprache

| Metrik | ours | vectara |
|--------|--------|--------|
| nDCG@10 | 0.975 | 0.728 |
| Relevance@10 | 100.0% | 25.0% |
| Relevance@3 | 100.0% | 33.3% |

### cross-reference

| Metrik | ours | vectara |
|--------|--------|--------|
| nDCG@10 | 0.929 | 0.946 |
| Relevance@10 | 66.7% | 66.7% |
| Relevance@3 | 55.6% | 88.9% |

### exakte-paragraphen

| Metrik | ours | vectara |
|--------|--------|--------|
| nDCG@10 | 0.987 | 0.883 |
| Relevance@10 | 100.0% | 40.0% |
| Relevance@3 | 100.0% | 33.3% |

### konzept

| Metrik | ours | vectara |
|--------|--------|--------|
| nDCG@10 | 0.965 | 0.950 |
| Relevance@10 | 75.0% | 40.0% |
| Relevance@3 | 83.3% | 41.7% |

### stpo-prozess

| Metrik | ours | vectara |
|--------|--------|--------|
| nDCG@10 | 0.937 | 0.883 |
| Relevance@10 | 80.0% | 46.7% |
| Relevance@3 | 77.8% | 44.4% |

## Detail pro Query


### q01 — exakte-paragraphen

**Query:** Welche Voraussetzungen hat der gewerbsmaessige Bandenbetrug nach § 263 Abs. 5 StGB?

**Kontext:** Qualifikationstatbestand des Bandenbetrugs im Fischer-Kommentar

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours | 0.99 | 100% | 100% | 3 | 8.9s |
| vectara | 0.94 | 60% | 67% | 3 | 2.0s |

#### ours — Top 3
- **[Judge=3]** `§ 263 StGB – I. Vermögensbegriff  – Rn. 263` — Enthält exakt § 263 Abs. 5 StGB mit allen Voraussetzungen
  > 263 (1) Wer in der Absicht, sich oder einem Dritten einen rechtswidrigen Vermögensvorteil zu verschaffen, das Vermögen eines anderen dadurch beschädigt, daß er durch Vorspiegelung falscher oder durch ...
- **[Judge=3]** `§ 263 StGB – BT. Zweriindzwanzigster Abschnitt – Rn. 225` — Direkt relevant: erklärt Voraussetzungen des § 263 Abs. 5
  > IV. Qualifikation (Abs. 5). Abs. 5 enthält einen Qualifikationstatbestand, der die Tat in Fällen kumulativ gewerbs- und bandenmäßiger Begehung zum Verbrechen macht. Die Qualifikation ist in die Urteil...
- **[Judge=3]** `§ 263 StGB – BT. Zweijundzwanzigster Abschnitt – Rn. 213` — Direkt relevant: behandelt Qualifikationstatbestand § 263 Abs. 5
  > 213 Sind beide Varianten erfüllt, ist eine Qualifikation nach Abs. 5 gegeben. Die Abgrenzung des Abs. 3 Nr. 1 zum Verbrechen nach Abs. 5 ist in Fällen bandenmäßiger Begehung schwierig, denn eine auf f...

#### vectara — Top 3
- **[Judge=3]** `['Übersicht']` — Direkt relevant für Bandenbetrug Qualifikationstatbestand
  > § 263 ist unter den Voraussetzungen von Abs....
- **[Judge=1]** `['97']` — Andere Straftaten, aber verwandte Bandenkriminalität
  > aus der Abgabenordnung:a) Steuerhinterziehung unter den in § 370 Absatz 3 Satz 2 Nummer 1 genannten Voraussetzungen, sofern der Täter als Mitglied einer Bande, die sich zur fortgesetzten Begehung von ...
- **[Judge=2]** `['Neunzehnter Abschnitt. Diebstahl und Unterschlagun...']` — Thematisch relevant, behandelt Bandenbetrug § 263
  > dazu BGHSt 47, 214 (216)); StraFo 2007, 78 (78 f.); NStZ 2002, 375 (377); 2007, 288 (289); 2008, 54 (Bandenbetrug; § 263 Abs....

### q02 — exakte-paragraphen

**Query:** Was regelt § 112 StPO zur Untersuchungshaft?

**Kontext:** Anordnungsvoraussetzungen der U-Haft (dringender Tatverdacht, Haftgrund) im Schmitt/Koehler

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours | 0.99 | 100% | 100% | 3 | 6.3s |
| vectara | 0.81 | 60% | 33% | 1 | 3.4s |

#### ours — Top 3
- **[Judge=3]** `§ 112 StPO – Rn. 112` — Direkt § 112 StPO zu Untersuchungshaft-Voraussetzungen
  > 112 (1) ¹ Die Untersuchungshaft darf gegen den Beschuldigten angeordnet werden, wenn er der Tat dringend verdächtig ist und ein Haftgrund besteht. ² Sie darf nicht angeordnet werden, wenn sie zu der B...
- **[Judge=3]** `§ 112 StPO – Rn. 112` — Behandelt direkt Voraussetzungen des Haftbefehls nach § 112
  > Haftunfähigkeit des Beschuldigten schließt den Erlass des Haftbefehls nicht aus, sondern hindert nur seinen Vollzug (OLG Düsseldorf JZ 1984, 248; OLG Frankfurt a.M. NJW 1968, 2302; OLG Nürnberg OLGSt ...
- **[Judge=3]** `§ 112 StPO – III. Flucht (Abs – Rn. 23` — Direkt relevant: behandelt Haftgründe nach § 112 StPO
  > Bei einer besonders hohen Straferwartung braucht daher nur geprüft zu werden, ob Umstände vorhanden sind, die die hieraus herzuleitende Fluchtgefahr ausräumen können (KG StV 1996, 383; OLG München Str...

#### vectara — Top 3
- **[Judge=1]** `['Übersicht']` — Nachbarparagraph zu U-Haft, aber nicht Anordnungsvoraussetzungen
  > Verhaftung und vorläufige Festnahme § 116b StPO ckung von Untersuchungshaft vor, es sei denn, das Gericht trifft eine abweichende Entscheidung, weil der Zweck der Untersuchungshaft dies erfordert....
- **[Judge=3]** `['Einleitung']` — Direkt relevant: behandelt Anordnungsvoraussetzungen der Untersuchungshaft
  > → StPO Vor § 112 Rn....
- **[Judge=1]** `['Einleitung']` — Nur Verweis, keine Inhalte zu § 112 StPO
  > 112): → StPO § 204 Rn....

### q03 — exakte-paragraphen

**Query:** Welche Haftgruende nennt § 112 Abs. 2 StPO?

**Kontext:** Fluchtgefahr, Verdunkelungsgefahr, Flucht — im StPO-Kommentar

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours | 0.99 | 100% | 100% | 3 | 7.0s |
| vectara | 1.00 | 0% | 0% | 1 | 1.2s |

#### ours — Top 3
- **[Judge=3]** `§ 112 StPO – Rn. 112` — Enthält vollständigen Wortlaut von § 112 Abs. 2 StPO
  > 112 (1) ¹ Die Untersuchungshaft darf gegen den Beschuldigten angeordnet werden, wenn er der Tat dringend verdächtig ist und ein Haftgrund besteht. ² Sie darf nicht angeordnet werden, wenn sie zu der B...
- **[Judge=3]** `§ 112 StPO – III. Flucht (Abs – Rn. 23` — Nennt direkt Haftgruende Flucht- und Verdunkelungsgefahr aus § 112 Abs. 2 StPO
  > Bei einer besonders hohen Straferwartung braucht daher nur geprüft zu werden, ob Umstände vorhanden sind, die die hieraus herzuleitende Fluchtgefahr ausräumen können (KG StV 1996, 383; OLG München Str...
- **[Judge=2]** `§ 112 StPO – III. Flucht (Abs – Rn. 32 (Teil 2)` — Behandelt Verdunkelungsgefahr aus § 112 Abs. 2 StPO
  > Wenn die Verdunkelungshandlungen nicht geeignet sind, die Ermittlung der Wahrheit zu erschweren, darf UHaft nicht angeordnet werden. Der Haftgrund liegt daher nicht vor, wenn der Sachverhalt schon in ...

#### vectara — Top 3
- **[Judge=1]** `['Vorbemerkung zu §§ 211–217']` — Nur Paragraphenreferenz, keine Haftgruende genannt
  > 2 Nr. 1 Buchst. h StPO; UHaft § 112 Abs....
- **[Judge=1]** `['Übersicht']` — Nur Paragraphennennung ohne Inhalte zu Haftgruenden
  > 5 S. 1, 148 Abs. 2 S. 1 StPO; § 112 Abs....
- **[Judge=1]** `['7. Untersuchungshaft, einstweilige Unterbringung u...']` — Verweist auf § 112 Abs. 2, nennt aber nicht die Haftgründe
  > (4) Besteht in den Fällen des § 112 Absatz 3 und des § 112a Absatz 1 StPO auch ein Haftgrund nach § 112 Absatz 2 StPO, sind die Feststellungen hierüber aktenkundig zu machen....

### q04 — exakte-paragraphen

**Query:** Was regelt § 102 StPO zur Durchsuchung beim Beschuldigten?

**Kontext:** Durchsuchungsvoraussetzungen beim Verdaechtigen

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours | 0.97 | 100% | 100% | 3 | 5.8s |
| vectara | 0.78 | 40% | 33% | 1 | 1.0s |

#### ours — Top 3
- **[Judge=3]** `§ 102 StPO – Rn. 102` — Direkt relevant: erklärt § 102 StPO Durchsuchungsvoraussetzungen
  > 102 Bei dem, welcher als Täter oder Teilnehmer einer Straftat oder der Datenhehlerei, Begünstigung, Strafvereitelung oder Hehlerei  Köhler    Ermittlungsmaßnahmen  verdächtig ist, kann eine Durchsuchu...
- **[Judge=2]** `§ 102 StPO – Rn. 10` — Behandelt Durchsuchungsvoraussetzungen, aber nicht spezifisch § 102
  > II. Auffinden von Beweismitteln. Zu den Beweismitteln (→ § 94 Rn. 4 ff.) gehören auch die nur in § 103 erwähnten Spuren (SK-StPO/Jäger/Wohlers Rn. 21) u. Personen, die zu Beweiszwecken in Augenschein ...
- **[Judge=3]** `§ 102 StPO – Rn. 10` — Direkt relevant - erklärt Durchsuchungsgegenstand bei § 102 StPO
  > 10 III. Sachen. Sachen sind Kleidungsstücke, die der Verdächtige bei sich führt, ohne sie zu tragen, u. seine sonstige bewegliche Habe, gleichgültig, ob sie sich in seinem Umkreis, zB in Gepäckstücken...

#### vectara — Top 3
- **[Judge=1]** `['Entschädigung für andere Strafverfolgungsmaßnahmen...']` — Erwähnt § 102 StPO, aber ohne Regelungsinhalt
  > Durchsuchung iS Nr. 4 ist nur die nach §§ 102, 103 StPO, nicht die nach § 111 StPO (Meyer StrEG Rn....
- **[Judge=2]** `['Übersicht']` — Erwähnt § 102 StPO, aber nur fragmentarisch
  > 27); denn nach § 102 ist sogar die Durchsuchung zum Zweck der Ergreifung zulässig (→ § 102 Rn....
- **[Judge=1]** `['Herausgabepflicht']` — Erwähnt § 102 StPO nur beiläufig ohne Regelungsinhalt
  > 3; Burhoff StraFo 2021, 398 (400)); einschränkend bei vorhergehender Durchsuchung nach § 102 StPO MüKoStPO/Hausschild Rn....

### q05 — konzept

**Query:** Wann liegt eine konkludente Taeuschung im Sinne des § 263 StGB vor?

**Kontext:** Taeuschungshandlung durch schluessiges Verhalten

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours | 0.90 | 80% | 67% | 2 | 8.5s |
| vectara | 0.84 | 20% | 33% | 1 | 1.3s |

#### ours — Top 3
- **[Judge=2]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 263 (Tei` — Literaturverzeichnis zu Betrug, enthält relevante Aufsätze zu konkludenter Täuschung
  > Heghmanns, Strafbarkeit des „Phishing“ von Bankkontendaten und ihrer Verwertung, wistra 2007, 167; Hilgendorf, Tatsachenaussagen u. Werturteile im Strafrecht, 1998; Hillenkamp, Zum Schutz „deliktische...
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 14` — Direkt relevant zu konkludenten Täuschungen § 263
  > Rspr. und hM bejahen darüber hinaus aber die Möglichkeit einer Täuschung durch Unterlassen auch ohne Erklärung gegenüber dem Irrenden (→ Rn. 38; vgl. BGHSt 39, 392 (398); BayObLG NJW 1987, 1654 (mAnm ...
- **[Judge=1]** `§ 263 StGB – I. Vermögensbegriff  – Rn. 263` — Gesetzestext ohne konkludente Taeuschung Details
  > 263 (1) Wer in der Absicht, sich oder einem Dritten einen rechtswidrigen Vermögensvorteil zu verschaffen, das Vermögen eines anderen dadurch beschädigt, daß er durch Vorspiegelung falscher oder durch ...

#### vectara — Top 3
- **[Judge=1]** `['Übersicht']` — Nur Verweis auf Betrug, keine konkludente Täuschung
  > → § 263 Rn. 193). Liegt auch Betrugsvorsatz vor, geht § 263 vor (→ Rn....
- **[Judge=1]** `['Übersicht', 'Besonders schwere Fälle der Bestechlichkeit und Be...']` — Behandelt § 263 StGB, aber qualifizierte Tatbestände
  > (2) Ein besonders schwerer Fall im Sinne des Absatzes 1 liegt in der Regel vor, wenn 1....
- **[Judge=2]** `['Übersicht']` — Erwähnt konkludente Täuschung, aber spezifischer Anwendungsfall
  > 12a f.). Bei kollusivem Zusammenwirken zwischen Karteninhaber und Zahlungsannehmer (Vertragsunternehmen) liegt idR eine (konkludente) Täuschung des Ausstellers über die Voraussetzungen der Zahlungspfl...

### q06 — konzept

**Query:** Was ist eine Vermoegensverfuegung und welche Anforderungen stellt die Rechtsprechung?

**Kontext:** Tatbestandsmerkmal der Vermoegensverfuegung beim Betrug

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours | 0.98 | 60% | 67% | 3 | 14.0s |
| vectara | 1.00 | 0% | 0% | 1 | 0.8s |

#### ours — Top 3
- **[Judge=3]** `§ 263 StGB – BT. Zweitundzwanzigster Abschnitt – Rn. 69` — Direkt relevant: definiert Vermoegensverfuegung mit Rechtsprechungsanforderungen
  > 69 Anders ist es, wenn der Verfügende seinerseits nur (gutgläubige) Hilfsperson eines bösgläubigen Dritten ist. Hier ist auf den Irrtum des Entscheidungsbefugten abzustellen: Erkennt dieser die Unrich...
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 76` — Definiert Unmittelbarkeit als zentrales Merkmal der Vermoegensverfuegung
  > 76 3. Unmittelbarkeit der Verfügung. Neben der Freiwilligkeit ist das Merkmal der Unmittelbarkeit nach stRspr und hM das wichtigste Kriterium zur Beschränkung der § 263 unterfallenden Selbstschädigung...
- **[Judge=1]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 87` — Behandelt Kausalitaet, nicht Definition der Vermoegensverfuegung
  > 87 5. Kausalität. Für die Vermögensverfügung muss der täuschungsbedingte Irrtum kausal sein (vgl. BGHSt 24, 257 (260); 24, 386 (389); NStZ 2003, 313 (314 f.); OLG Düsseldorf NJW 1987, 3145); Mitverurs...

#### vectara — Top 3
- **[Judge=1]** `['Übersicht']` — Allgemeine Anforderungen, nicht spezifisch zu Vermoegensverfuegung
  > Maßgeblich sind die Anforderungen, welche die Rechtsordnung an jedermann stellt (BGHSt 43, 66 (77); NStZ-RR 1999, 295 (296); 2015, 137 (138))....
- **[Judge=0]** `['Verlesung eines richterlichen Protokolls bei Gestä...']` — Verfahrensrecht, nicht Vermoegensverfuegung beim Betrug
  > Verlesbar sind auch Erklärungen in einem anderen Strafverfahren u. in Zivil- u. Verwaltungsgerichtsverfahren (RGSt 56, 257; Schneidewin JR 1951, 485)), sofern die Voraussetzung für eine Verwertung im ...
- **[Judge=0]** `['Übersicht']` — Fragment über Einwilligung, nicht Vermögensverfügung
  > 1 S. 2). Damit die Einwilligung rechtswirksam ist, muss ihr eine Belehrung vorausgehen, welche den Anforderungen des Abs....

### q07 — konzept

**Query:** Was versteht man unter einem Gefaehrdungsschaden beim Betrug?

**Kontext:** Schadensbegriff, schadensgleiche Vermoegensgefaehrdung

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours | 0.98 | 80% | 100% | 3 | 11.1s |
| vectara | 0.97 | 80% | 67% | 3 | 1.2s |

#### ours — Top 3
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 159` — Direkt relevant: definiert Gefährdungsschaden beim Betrug
  > 159 b) Voraussetzungen. aa) Ein Gefährdungsschaden ist gegeben, wenn die Wahrscheinlichkeit des endgültigen Verlusts eines Vermögensbestandteils zum Zeitpunkt der täuschungsbedingten Verfügung so groß...
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 109` — Behandelt direkt Gefaehrdungsschaden bei Betrug
  > VI. Schaden. Vermögensschaden ist ein negativer Saldo zwischen dem Wert des Vermögens vor und nach der irrtumsbedingten Vermögensverfügung des Getäuschten (Prinzip der Gesamtsaldierung; stRspr; vgl. B...
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 171` — Definiert Gefährdungsschaden bei Betrug, zentral relevant
  > Die täuschungsbedingte Herausgabe von EC-Karten, Kreditkarten und weiteren Zugangsdaten zu Bank-Guthaben (PINs, TANs; Passwörter), sei es infolge persönlicher Täuschung oder von „Phishing“-Manipulatio...

#### vectara — Top 3
- **[Judge=3]** `['Zweiundzwanzigster Abschnitt. Betrug und Untreue']` — Definiert direkt Gefaehrdungsschaden beim Betrug mit Beispielen
  > einen vollendeten Betrug durch Entstehen eines Gefährdungsschadens an, wenn aufgrund tauschender Erklärungen dem Täter ein Überziehungskredit eingeräumt oder Karten mit Einlösungsgarantie ausgehändigt...
- **[Judge=3]** `['Übersicht']` — Definiert explizit Gefaehrdungsschaden beim Betrug
  > 37 ff. ausdrücklich zwischen „Endschaden“ und „Gefährdungsschaden“ differenziert und dem Letzteren bei der Steuerhinterziehung („ähnlich wie beim Betrug“) ein nur halb so hohes Gewicht beigemessen (Gr...
- **[Judge=1]** `['Zweiundzwanzigster Abschnitt. Betrug und Untreue']` — Schadensbegriff beim Betrug, aber nicht Gefaehrdungsschaden
  > In Fällen, in denen der Zahlungsempfänger eine Leistung vorab erbringt und anschließend im Rahmen der Abrechnung über das Vorliegen tatsächlicher Anspruchsvoraussetzungen tauscht, ist grundsätzlich de...

### q08 — konzept

**Query:** Wie wird der Vorsatz beim Betrug bestimmt, insbesondere die Bereicherungsabsicht?

**Kontext:** Subjektiver Tatbestand § 263 StGB

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours | 1.00 | 80% | 100% | 3 | 12.3s |
| vectara | 0.99 | 60% | 67% | 2 | 0.9s |

#### ours — Top 3
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 176` — Beantwortet direkt Vorsatz und Bereicherungsabsicht bei Betrug
  > D. Subjektiver Tatbestand. § 263 setzt Vorsatz voraus; darüber hinaus ist die Absicht rechtswidriger Bereicherung erforderlich.   I. Vorsatz. 1. Täuschungsvorsatz. Der Vorsatz (bedingter Vorsatz genüg...
- **[Judge=3]** `§ 263 StGB – I. Sonstige Vorschriften 239 – Rn. 263 (Teil 1)` — Direkt relevant: behandelt Bereicherungsabsicht bei § 263
  > 3. Einzelne Fallgruppen ... 92 4. Rechtlich missbilligte, sittenwidrige und gesetzeswidrige wirtschaftliche Werte ... 101 VI. Schaden ... 110 1. Grundsätze der Schadensermittlung ... 111 2. Vermögensm...
- **[Judge=3]** `§ 263 StGB – BT. Zweijundzwanzigster Abschnitt – Rn. 187` — Direkt relevant: behandelt Bereicherungsabsicht bei Betrug
  > 2. Absicht. Es muss dem Täter darauf ankommen, sich oder einem Dritten einen Vermögensvorteil zu verschaffen. Motiv oder letzter Zweck muss dies nicht sein (BGHSt 4, 107; 16. 1; BGHR § 263 I Täusch. 9...

#### vectara — Top 3
- **[Judge=2]** `['Erpressung']` — Erwähnt Bereicherung bei Betrug, aber unvollständiger Kontext
  > Zwischen Schaden und (beabsichtigter) Bereicherung muss, wie beim Betrug (vgl....
- **[Judge=2]** `['Übersicht']` — Erwähnt Bereicherungsabsicht beim Betrug, aber keine Details
  > Otto JURA 1994, 143; dazu Kelker, Zur Legitimität von Gesinnungsmerkmalen im Strafrecht, 2007); weiterhin die über den Tatbestand hinausreichenden Absichten (zB Bereicherungsabsicht beim Betrug; Delik...
- **[Judge=1]** `['Zweiundzwanzigster Abschnitt. Betrug und Untreue']` — Nur bibliographische Angabe ohne Rechtsinhalte
  > Rostock 2006); Harbort, Die Bedeutung der objektiven Zurechnung beim Betrug, 2010 (Diss....

### q09 — alltagssprache

**Query:** Hat der Angeklagte die Kunden über das Internet betrogen?

**Kontext:** Abstrakte Frage zu Internetbetrug, sucht Taeuschungshandlung + Schaden

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours | 0.92 | 100% | 100% | 2 | 10.0s |
| vectara | 0.62 | 40% | 33% | 0 | 0.8s |

#### ours — Top 3
- **[Judge=2]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 263 (Tei` — Literaturverzeichnis zu Betrug, enthält Phishing-Verweis
  > Heghmanns, Strafbarkeit des „Phishing“ von Bankkontendaten und ihrer Verwertung, wistra 2007, 167; Hilgendorf, Tatsachenaussagen u. Werturteile im Strafrecht, 1998; Hillenkamp, Zum Schutz „deliktische...
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 28` — Direkt relevant: Internetbetrug durch Taeuschungshandlungen im Detail
  > 28 Solche Scheinrechnungen sind so formuliert, dass sie bei eiligen oder geschäftsunerfahrenen Empfängern den Eindruck der Zahlungspflicht zu erzeugen geeignet sind (vgl. auch Erb ZIS 2011, 354: „Sugg...
- **[Judge=2]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 176` — Behandelt subjektive Tatbestandsmerkmale des Betrugs, relevant für Internetbetrug
  > D. Subjektiver Tatbestand. § 263 setzt Vorsatz voraus; darüber hinaus ist die Absicht rechtswidriger Bereicherung erforderlich.   I. Vorsatz. 1. Täuschungsvorsatz. Der Vorsatz (bedingter Vorsatz genüg...

#### vectara — Top 3
- **[Judge=0]** `['Notwendige Auslagen des Nebenklägers']` — Fragment ohne Kontext, nicht bewertbar
  > hat der Angeklagte die dadurch entstandenen bes....
- **[Judge=3]** `['Übersicht']` — Direkt relevant zu Internetbetrug durch Identitätstäuschung
  > Der Tatbestand ist aber erfüllt bei Anlegen eines online-Kundenkontos unter Identitätstäuschung (aber nicht bei Bevollmächtigung des Dritten: BeckRS 2024, 11811), ebenso bei Verändern eines bestehende...
- **[Judge=0]** `['Revisionsbegründung']` — Fragment ohne rechtlichen Inhalt zu Betrug
  > über eine angeklagte Tat abgesehen hat, denn dann ist das Verf....

### q10 — alltagssprache

**Query:** Wann darf die Polizei bei jemandem zu Hause suchen?

**Kontext:** Durchsuchungsvoraussetzungen, §§ 102 ff. StPO

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours | 0.98 | 100% | 100% | 3 | 6.8s |
| vectara | 0.66 | 20% | 33% | 0 | 1.1s |

#### ours — Top 3
- **[Judge=3]** `§ 102 StPO – Rn. 102` — Beantwortet direkt die Durchsuchungsvoraussetzungen nach § 102 StPO
  > 102 Bei dem, welcher als Täter oder Teilnehmer einer Straftat oder der Datenhehlerei, Begünstigung, Strafvereitelung oder Hehlerei  Köhler    Ermittlungsmaßnahmen  verdächtig ist, kann eine Durchsuchu...
- **[Judge=2]** `§ 102 StPO – Rn. 10` — Behandelt Durchsuchungsvoraussetzungen, aber fokussiert auf Beweismittel
  > II. Auffinden von Beweismitteln. Zu den Beweismitteln (→ § 94 Rn. 4 ff.) gehören auch die nur in § 103 erwähnten Spuren (SK-StPO/Jäger/Wohlers Rn. 21) u. Personen, die zu Beweiszwecken in Augenschein ...
- **[Judge=3]** `§ 102 StPO – Rn. 3` — Direkt relevant: behandelt Durchsuchungsvoraussetzungen und Wohnungsschutz
  > **Teilnehmer** nach §§ 25 ff. StGB, nicht die sog. notwendigen Teilnehmer (zum Begriff: Fischer/Fischer StGB Vor § 25 Rn. 7), stehen den Tatverdächtigen gleich. Bei jedem v. ihnen sowie bei den der Be...

#### vectara — Top 3
- **[Judge=0]** `['Übersicht']` — Behandelt Notwehr/Notstand, nicht Durchsuchungsrecht
  > Die Polizei darf aber gerade nicht die Erschießung unschuldiger Personen anordnen, um Dritte zu retten....
- **[Judge=3]** `['Zuständigkeit für weitere gerichtliche Entscheidun...']` — Direkte Antwort zu Wohnungsdurchsuchung und Voraussetzungen
  > 28 ff.). Die Wohnung des Verdächtigen darf durchsucht werden, wenn konkrete Anhaltspunkte dafür bestehen, dass er dort aufzufinden ist (Kaiser NJW 1980, 876)....
- **[Judge=0]** `['Teil 6 Behandlung von bevorrechtigten Personen bei...']` — Diplomatischer Transport, keine Durchsuchungsregelungen
  > Dann ist es zulässig, den Diplomaten zu seiner Mission oder nach Hause zu bringen....

### q11 — alltagssprache

**Query:** Was passiert wenn jemand luegt damit er Geld bekommt?

**Kontext:** Laienhafte Umschreibung des Betrugstatbestandes

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours | 1.00 | 100% | 100% | 3 | 11.5s |
| vectara | 1.00 | 20% | 33% | 2 | 1.2s |

#### ours — Top 3
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 5` — Direkt relevant: beschreibt Betrug durch Täuschung für Vermögensvorteil
  > 5 C. Grundtatbestand, Abs. 1. Tathandlung ist das Täuschen einer natürlichen Person (vgl. NStZ 2005, 213) über Tatsachen. Erfolg dieser Handlung muss ein Irrtum des Täuschungsadressaten sein; dieser m...
- **[Judge=3]** `§ 263 StGB – I. Vermögensbegriff  – Rn. 263` — Direkter Betrugstatbestand, zentrale Rechtsnorm
  > 263 (1) Wer in der Absicht, sich oder einem Dritten einen rechtswidrigen Vermögensvorteil zu verschaffen, das Vermögen eines anderen dadurch beschädigt, daß er durch Vorspiegelung falscher oder durch ...
- **[Judge=3]** `§ 263 StGB – BT. Zweitundzwanzigster Abschnitt – Rn. 69` — Direkt relevant: behandelt Betrugstatbestand § 263
  > 69 Anders ist es, wenn der Verfügende seinerseits nur (gutgläubige) Hilfsperson eines bösgläubigen Dritten ist. Hier ist auf den Irrtum des Entscheidungsbefugten abzustellen: Erkennt dieser die Unrich...

#### vectara — Top 3
- **[Judge=2]** `['Geldwäsche']` — Betrug thematisch relevant, aber nur Teilaspekt
  > Für einen Finanzagenten kommt eine Beteiligung an der Vorrat des Betrugs in Betracht, wenn er den Hintermännern sein Bankkonto zur Verfügung stellt, damit die Geschädigten tatplankonform Geld darauf ü...
- **[Judge=0]** `['Geldfälschung']` — Geldfälschung, nicht Betrug durch Lügen
  > Daher ist Geld „nachgemacht", wenn dem Täter die Legitimation zur Herstellung fehlt (vgl....
- **[Judge=0]** `['Gefährliche Eingriffe in den Bahn-, Schiffs- und L...', 'Gefährliche Eingriffe in den Straßenverkehr']` — Gefährdungsdelikt, nicht Betrug oder Vermögensschaden
  > einen ähnlichen, ebenso gefährlichen Eingriff vornimmt,und dadurch Leib oder Leben eines anderen Menschen oder fremde Sachen von bedeutendem Wert gefährdet, wird mit Freiheitsstrafe bis zu fünf Jahren...

### q12 — alltagssprache

**Query:** Wann muss jemand ins Gefaengnis waehrend die Tat noch nicht bewiesen ist?

**Kontext:** Untersuchungshaft, §§ 112 ff. StPO

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours | 1.00 | 100% | 100% | 3 | 8.2s |
| vectara | 0.63 | 20% | 33% | 0 | 0.9s |

#### ours — Top 3
- **[Judge=3]** `§ 112 StPO – Rn. 112` — Beantwortet direkt Untersuchungshaft-Voraussetzungen ohne Tatbeweis
  > 112 (1) ¹ Die Untersuchungshaft darf gegen den Beschuldigten angeordnet werden, wenn er der Tat dringend verdächtig ist und ein Haftgrund besteht. ² Sie darf nicht angeordnet werden, wenn sie zu der B...
- **[Judge=3]** `§ 112 StPO – III. Flucht (Abs – Rn. 23` — Direkt relevant: Haftgruende Flucht- und Verdunkelungsgefahr
  > Bei einer besonders hohen Straferwartung braucht daher nur geprüft zu werden, ob Umstände vorhanden sind, die die hieraus herzuleitende Fluchtgefahr ausräumen können (KG StV 1996, 383; OLG München Str...
- **[Judge=3]** `§ 112 StPO – Rn. 112` — Direkt relevant: Untersuchungshaft, dringender Tatverdacht, Haftbefehls-Voraussetzungen
  > Haftunfähigkeit des Beschuldigten schließt den Erlass des Haftbefehls nicht aus, sondern hindert nur seinen Vollzug (OLG Düsseldorf JZ 1984, 248; OLG Frankfurt a.M. NJW 1968, 2302; OLG Nürnberg OLGSt ...

#### vectara — Top 3
- **[Judge=0]** `Strafgesetzbuch` — Behandelt Tatverhinderung, nicht Untersuchungshaft
  > Var.). Wenn der Erfolg noch nicht eingetreten ist, muss er die Vollendung der Tat verhindern (3....
- **[Judge=2]** `['Übersicht']` — Thematisch relevant: behandelt Beweis vor Verurteilung
  > 16) noch nicht bewiesen (BGHSt 10, 276; OLG Köln StraFo 2005, 216)....
- **[Judge=0]** `['Wirkung der Vollziehung des Vermögensarrestes']` — Insolvenzrecht, nicht Untersuchungshaft
  > 14 Die StA muss Insolvenzforderung u. Insolvenzgrund lediglich glaubhaft machen; bewiesen sein muss die Forderung nicht (Bittmann/Tschakert ZInsO 2017, Köhler ***...

### q13 — stpo-prozess

**Query:** Welche Voraussetzungen hat die Untersuchungshaft wegen Fluchtgefahr?

**Kontext:** § 112 Abs. 2 Nr. 2 StPO Fluchtgefahr

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours | 0.94 | 80% | 67% | 3 | 7.8s |
| vectara | 0.91 | 60% | 33% | 3 | 1.1s |

#### ours — Top 3
- **[Judge=3]** `§ 112 StPO – Rn. 112` — Behandelt direkt § 112 Abs. 2 Nr. 2 Fluchtgefahr
  > 112 (1) ¹ Die Untersuchungshaft darf gegen den Beschuldigten angeordnet werden, wenn er der Tat dringend verdächtig ist und ein Haftgrund besteht. ² Sie darf nicht angeordnet werden, wenn sie zu der B...
- **[Judge=1]** `§ 112 StPO – Rn. 112` — Allgemeine Haftbefehlsvoraussetzungen, nicht spezifisch Fluchtgefahr
  > Haftunfähigkeit des Beschuldigten schließt den Erlass des Haftbefehls nicht aus, sondern hindert nur seinen Vollzug (OLG Düsseldorf JZ 1984, 248; OLG Frankfurt a.M. NJW 1968, 2302; OLG Nürnberg OLGSt ...
- **[Judge=3]** `§ 112 StPO – III. Flucht (Abs – Rn. 16` — Behandelt direkt Fluchtgefahr nach § 112 Abs. 2 Nr. 2
  > 16 Bei Ergreifung des Beschuldigten aufgrund des nach Abs. 2 Nr. 1 erlassenen Haftbefehls entfällt der Haftgrund der Flucht. In der Regel wird die vorherige Flucht aber die Aufrechterhaltung des Haftb...

#### vectara — Top 3
- **[Judge=3]** `['Haftgrund der Wiederholungsgefahr']` — Direkt relevant: betrifft Voraussetzungen der Untersuchungshaft wegen Fluchtgefahr
  > (2) In diesen Fällen darf die Untersuchungshaft wegen Fluchtgefahr nur angeordnet werden, wenn der Beschuldigte 1....
- **[Judge=1]** `['Fünfter Unterabschnitt. Verfahren bei Aussetzung d...']` — Jugendstrafrecht, nicht allgemeine Untersuchungshaft-Voraussetzungen
  > (2) Solange der Jugendliche das sechzehnte Lebensjahr noch nicht vollendet hat, ist die Verhängung von Untersuchungshaft wegen Fluchtgefahr nur zulässig, wenn er 1....
- **[Judge=1]** `['7. Untersuchungshaft, einstweilige Unterbringung u...']` — Behandelt Untersuchungshaft, aber nicht Fluchtgefahr
  > ² Entscheidend ist vielmehr, ob die Voraussetzungen für die Untersuchungshaft wegen der Krankheit weggefallen sind....

### q14 — stpo-prozess

**Query:** Wie lange darf die Untersuchungshaft maximal dauern?

**Kontext:** § 121 StPO Sechs-Monats-Grenze, Haftpruefung OLG

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours | 0.99 | 100% | 100% | 3 | 13.6s |
| vectara | 0.80 | 40% | 33% | 1 | 2.5s |

#### ours — Top 3
- **[Judge=3]** `§ 121 StPO – Rn. 13` — Direkt relevant zu 6-Monats-Grenze und Fortsetzung UHaft
  > 13 Das bedeutet: Wird UHaft vollzogen, so darf sie nicht aufgrund eines weiteren Haftbefehls, der bereits bei Erlass des 1. Haftbefehls bekannt gewesene Tatvorwürfe zum Gegenstand hat, über 6 Monate h...
- **[Judge=3]** `§ 121 StPO – Rn. 1` — Direkt relevant: § 121 StPO Sechs-Monats-Grenze erläutert
  > 1 A. Beschleunigungsgebot. Einen Anspruch auf beschleunigte Aburteilung hat der in UHaft (und einstweiliger Unterbringung) befindliche Beschuldigte nach Art. 5 Abs. 3 S. 2 EMRK (→ EMRK Art. 5 Rn. 10 f...
- **[Judge=2]** `§ 121 StPO – Rn. 8 (Teil 1)` — Thematisch relevant, behandelt Untersuchungshaft-Beschränkungen aber nicht maximale Dauer
  > 8 II. Zeitliche Geltung der Beschränkungen der UHaft. Bis zu einem auf Freiheitsentziehung lautenden Urteil (Freiheitsstrafe mit o. ohne Bewährung o. freiheitsentziehende Sicherungsmaßregeln) gelten d...

#### vectara — Top 3
- **[Judge=1]** `['Nachträgliche Entscheidung über Strafaussetzung zu...']` — Sicherungshaft, nicht Untersuchungshaft - anderer Hafttyp
  > Länger als die bei Widerruf der Aussetzung zu verbüßende Strafe darf die Sicherungshaft nicht dauern....
- **[Judge=3]** `['Verfahren bei der Haftprüfung']` — Direkte Antwort auf Maximaldauer der Untersuchungshaft
  > 1 vgl. § 123. Fortdauer der Untersuchungshaft über sechs Monate RiStBV 56 121 (1) Solange kein Urteil ergangen ist, das auf Freiheitsstrafe oder eine freiheitsentziehende Maßregel der Besserung und Si...
- **[Judge=1]** `['Belehrung bei Strafaussetzung oder Verwarnung mit ...']` — Behandelt Haftdauer, aber Sicherungshaft statt Untersuchungshaft
  > Länger als die bei Widerruf der Aussetzung zu verbüßende Strafe darf die Sicherungshaft nicht dauern....

### q15 — stpo-prozess

**Query:** Was regelt § 136 StPO zur Beschuldigtenvernehmung?

**Kontext:** Belehrungspflichten, Recht auf Verteidiger

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours | 0.88 | 60% | 67% | 3 | 14.6s |
| vectara | 0.93 | 40% | 67% | 2 | 2.1s |

#### ours — Top 3
- **[Judge=3]** `§ 114b StPO – I. Abs – Rn. 5` — Direkt relevant: § 136 StPO Belehrungspflichten und Verteidigerwahl
  > 5 II. Abs. 2 S. 1 Nr. 2–4. Hier wird die auch nach § 136 Abs. 1 S. 2, 3 und § 163a Abs. 3 S. 2, 4 vor Beginn der ersten richterlichen bzw. staatsanwaltschaftlichen o. polizeilichen Vernehmung bestehen...
- **[Judge=0]** `§ 115 StPO – Rn. 5` — Behandelt § 115 StPO Vorführung, nicht § 136
  > 5 Am Tage nach der Ergreifung darf er nur vorgeführt werden, wenn eine frühere Vorführung nicht möglich ist. Spätestens an diesem Tage muss die Vorführung aber stattfinden, auch wenn er ein Sonnabend,...
- **[Judge=2]** `§ 500 StPO – ILL. für das Strafverfahren und das Bußgeldverf` — Behandelt Beschuldigtenvernehmung, aber nicht § 136 StPO direkt
  > (4) Zeugen können zur Aufenthaltsermittlung ausgeschrieben werden.  (5) Für die internationale Fahndung nach Personen, einschließlich der Fahndung nach Personen im SIS und aufgrund eines Europäischen ...

#### vectara — Top 3
- **[Judge=2]** `['Einleitung']` — Behandelt § 136 StPO, aber nur kurzer Verweis
  > → StPO § 136 Rn. 3) als Beschuldigtenvernehmung fortzusetzen (BGHSt 22, 129 (132))....
- **[Judge=3]** `['Einleitung']` — Direkter Verweis auf gesuchten Paragraphen
  > dazu → StPO § 136 Rn....
- **[Judge=1]** `Beck'sche Kurz-Kommentare` — Anderer Paragraph, gleiches Verfahrensrecht
  > (1) ¹ In den Fällen des § 131 StPO veranlasst der Staatsanwalt die Ausschreibung des Beschuldigten zur Festnahme und die Niederlegung eines entsprechenden Suchvermerks im Bundeszentralregister....

### q16 — cross-reference

**Query:** Worin unterscheidet sich Betrug von Unterschlagung?

**Kontext:** Abgrenzung § 263 vs § 246 StGB

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours | 0.85 | 60% | 33% | 2 | 17.2s |
| vectara | 0.84 | 60% | 67% | 1 | 2.6s |

#### ours — Top 3
- **[Judge=2]** `§ 247 StGB – BT. Neunzehnter Abschnitt – Rn. 24` — Behandelt Konkurrenzen zwischen § 246 und § 263
  > 24 L. Konkurrenzen im Übrigen. Bei Manifestation des Zueignungswillens hinsichtlich mehrerer Sachen durch eine Ausführungshandlung liegt nur eine Tat vor (wistra 2006, 227 (227 f.)). Zur Abgrenzung vo...
- **[Judge=1]** `§ 263 StGB – BT. Zweitundzwanzigster Abschnitt – Rn. 69` — Behandelt Betrug, aber nicht Abgrenzung zu Unterschlagung
  > 69 Anders ist es, wenn der Verfügende seinerseits nur (gutgläubige) Hilfsperson eines bösgläubigen Dritten ist. Hier ist auf den Irrtum des Entscheidungsbefugten abzustellen: Erkennt dieser die Unrich...
- **[Judge=1]** `§ 353 StGB – BT. Dreißigster Abschnitt – Rn. 353` — Konkurrenzen erwähnt, aber zu § 353, nicht Abgrenzung
  > 5. D. Abs. 2. Nach Abs. 2 ist ein Amtsträger strafbar, der bei amtlicher Ausgabe von Geld oder Naturalien dem Empfänger vorsätzlich und rechtswidrig Abzüge macht und außerdem die Ausgabe als vollständ...

#### vectara — Top 3
- **[Judge=1]** `['Erpressung']` — Behandelt Abgrenzung, aber zu Nötigung statt Unterschlagung
  > Vom Betrug unterscheidet sie sich im Mittel, das dort Täuschung, hier Nötigung ist....
- **[Judge=3]** `['Neunzehnter Abschnitt. Diebstahl und Unterschlagun...']` — Direkte Abgrenzung zwischen Betrug und Unterschlagung
  > Gegenüber § 263 tritt § 246 zurück, wenn die Zueignung durch Betrug geschieht; dagegen ist ein der Unterschlagung nachfolgender Sicherungsbetrug mitbestrafte Nachtat....
- **[Judge=2]** `['Zweiundzwanzigster Abschnitt. Betrug und Untreue']` — Behandelt Betrug, aber nicht Abgrenzung zur Unterschlagung
  > Ein (vollendeter) Betrug liegt vor, wenn zum Zeitpunkt des Abschlusses eines Verpflichtungsgeschäfts feststeht, dass der durch Täuschung erlangten Verpflichtung (= Vermögensverfügung) eine (irrtumsbed...

### q17 — cross-reference

**Query:** Was sind die Unterschiede zwischen Diebstahl und Raub?

**Kontext:** § 242 vs § 249 StGB — Abgrenzung durch Gewalt/Drohung

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours | 0.97 | 100% | 100% | 3 | 9.1s |
| vectara | 1.00 | 60% | 100% | 3 | 1.0s |

#### ours — Top 3
- **[Judge=3]** `§ 249 StGB` — Direkt relevant: Abgrenzung Raub zu anderen Delikten
  > NStZ 2023, 351). Danach ist § 249 gegenüber § 255 ein spezielles Delikt; in jedem Raub liegt eine räuberische Erpressung (aA die hM in der Literatur). Die Unterscheidung richtet sich nach dem äußeren ...
- **[Judge=2]** `§ 252 StGB – BT. Zwanzigster Abschnitt – Rn. 12` — Behandelt Konkurrenzen zwischen Raub- und Diebstahlsdelikten
  > 12 I. Konkurrenzen. Gesetzeseinheit besteht mit §§ 242, 244 sowie mit § 240 (diff. NK-StGB/Kindhäuser Rn. 28). § 249 verdrängt § 252, wenn Raubmittel zunächst zur Wegnahme und später zur Sicherung des...
- **[Judge=3]** `§ 249 StGB – BT. Zwanzigster Abschnitt – Rn. 15` — Direkt relevant - erklärt subjektive Tatbestandsmerkmale beider Delikte
  > G. Subjektiver Tatbestand. Der Vorsatz muss entsprechend der Doppelnatur des Raubs sowohl Wegnahme (vgl. dazu → § 242 Rn. 29 ff.) als auch Nötigung (→ § 240 Rn. 53 f.) sowie deren Verknüpfung umfassen...

#### vectara — Top 3
- **[Judge=3]** `['Erpressung']` — Direkt relevant: behandelt exakt die gefragte Abgrenzung
  > Zur Abgrenzung von (Diebstahl und) Raub vgl....
- **[Judge=3]** `['Zwanzigster Abschnitt. Raub und Erpressung']` — Direkt relevant: behandelt Raub § 249 und Diebstahl
  > Raub und Erpressung§ 249 nur Diebstahl (§ 243 Abs....
- **[Judge=2]** `['Zwanzigster Abschnitt. Raub und Erpressung']` — Behandelt Diebstahl-Raub-Verhältnis, aber fokussiert Konkurrenzfragen
  > Tateinheit kann zwischen vollendetem Diebstahl und versuchtem Raub gegeben sein (BGHSt 21, 78; NStZ-RR 2005, 202 (203)); zwischen § 250 und § 249 im Fall unterschiedlicher Begehung gegenüber mehreren ...

### q18 — cross-reference

**Query:** Wann wird Betrug zu Computerbetrug und umgekehrt?

**Kontext:** § 263 vs § 263a StGB — Abgrenzung bei elektronischer Datenverarbeitung

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours | 0.96 | 40% | 33% | 3 | 8.5s |
| vectara | 1.00 | 80% | 100% | 3 | 1.5s |

#### ours — Top 3
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 58` — Direkte Abgrenzung Betrug/Computerbetrug bei automatisierten Verfahren
  > 58 Im Geschäftsverkehr wird sich, wer die Berechtigung eines Leistungsverlangens oder -auftrags nicht zu prüfen hat, hierüber idR auch keine (richtigen oder falschen) Gedanken machen (NStZ 1997, 281; ...
- **[Judge=1]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 62` — Betrug allgemein, nicht spezifisch Abgrenzung 263/263a
  > Die Kausalität der Täuschung für den Irrtum und dessen Kausalität für die Vermögensverfügung müssen im Einzelfall festgestellt sein. Mitverursachung reicht aus. Dabei darf das Gericht auch bei Serien-...
- **[Judge=1]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 263 (Tei` — Literaturverzeichnis zu § 263, behandelt nicht § 263a Abgrenzung
  > Fischer/Lutz    Betrug und Untreue   schende Warnung": Eine Drohung?, FS Puppe, 2011, 1217; Kupper, Mengenbegriffe im Strafgesetzbuch, FS Kohlmann, 2003, 133; Lampe, Personales Unrecht im Betrug, FS O...

#### vectara — Top 3
- **[Judge=3]** `['Übersicht']` — Behandelt direkt Abgrenzung Betrug/Computerbetrug bei identischem Schaden
  > Ebenso ist das Verhältnis zwischen (möglicher) Beteiligung am Betrug und (sicherem) späterem Computerbetrug hinsichtlich desselben Schadens zu behandeln (BGH NStZ 2008, 396 (396 f.))....
- **[Judge=3]** `['Zweiundzwanzigster Abschnitt. Betrug und Untreue']` — Direkt zur Abgrenzung Betrug vs Computerbetrug relevant
  > (Teil 1), GA 2023, 615; (Teil 2) GA 2023, 675; Schuhr, Betrug vs. Computerbetrug....
- **[Judge=3]** `['Neunzehnter Abschnitt. Diebstahl und Unterschlagun...']` — Direkt relevant: behandelt Computerbetrug-Paragraph zur Abgrenzung
  > 4), Computerbetrug (§ 263a Abs....