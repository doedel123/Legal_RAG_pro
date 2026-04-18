# RAG Benchmark Report

_Generiert: 2026-04-18T13:33:40_


- Queries: **18**
- Top-K: **5**
- Systeme: vectara

## Gesamtvergleich

| Metrik | vectara |
|--------|--------|
| nDCG@10 | 0.863 |
| Relevance@10 | 41.1% |
| Relevance@3 | 44.4% |
| Top-1-Score | 1.50 |
| Mean-Score | 1.47 |
| Latenz (s) | 4.27 |

## Nach Kategorie


### alltagssprache

| Metrik | vectara |
|--------|--------|
| nDCG@10 | 0.728 |
| Relevance@10 | 25.0% |
| Relevance@3 | 33.3% |

### cross-reference

| Metrik | vectara |
|--------|--------|
| nDCG@10 | 0.946 |
| Relevance@10 | 66.7% |
| Relevance@3 | 88.9% |

### exakte-paragraphen

| Metrik | vectara |
|--------|--------|
| nDCG@10 | 0.861 |
| Relevance@10 | 35.0% |
| Relevance@3 | 25.0% |

### konzept

| Metrik | vectara |
|--------|--------|
| nDCG@10 | 0.929 |
| Relevance@10 | 40.0% |
| Relevance@3 | 41.7% |

### stpo-prozess

| Metrik | vectara |
|--------|--------|
| nDCG@10 | 0.874 |
| Relevance@10 | 46.7% |
| Relevance@3 | 44.4% |

## Detail pro Query


### q01 — exakte-paragraphen

**Query:** Welche Voraussetzungen hat der gewerbsmaessige Bandenbetrug nach § 263 Abs. 5 StGB?

**Kontext:** Qualifikationstatbestand des Bandenbetrugs im Fischer-Kommentar

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| vectara | 0.77 | 20% | 0% | 1 | 5.1s |

#### vectara — Top 3
- **[Judge=1]** `['Übersicht']` — Unvollständiger Text, nur Paragraphennennung ohne Inhalt
  > § 263 ist unter den Voraussetzungen von Abs....
- **[Judge=1]** `['97']` — Anderes Rechtsgebiet, aber ähnliche Bandenstruktur
  > aus der Abgabenordnung:a) Steuerhinterziehung unter den in § 370 Absatz 3 Satz 2 Nummer 1 genannten Voraussetzungen, sofern der Täter als Mitglied einer Bande, die sich zur fortgesetzten Begehung von ...
- **[Judge=1]** `['Neunzehnter Abschnitt. Diebstahl und Unterschlagun...']` — Nur Fundstellenverweise ohne inhaltliche Voraussetzungen
  > dazu BGHSt 47, 214 (216)); StraFo 2007, 78 (78 f.); NStZ 2002, 375 (377); 2007, 288 (289); 2008, 54 (Bandenbetrug; § 263 Abs....

### q02 — exakte-paragraphen

**Query:** Was regelt § 112 StPO zur Untersuchungshaft?

**Kontext:** Anordnungsvoraussetzungen der U-Haft (dringender Tatverdacht, Haftgrund) im Schmitt/Koehler

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| vectara | 0.81 | 60% | 33% | 1 | 3.0s |

#### vectara — Top 3
- **[Judge=1]** `['Übersicht']` — Nachbarparagraph zu U-Haft, aber andere Regelung
  > Verhaftung und vorläufige Festnahme § 116b StPO ckung von Untersuchungshaft vor, es sei denn, das Gericht trifft eine abweichende Entscheidung, weil der Zweck der Untersuchungshaft dies erfordert....
- **[Judge=3]** `['Einleitung']` — Direkt relevant für § 112 StPO Untersuchungshaft
  > → StPO Vor § 112 Rn....
- **[Judge=1]** `['Einleitung']` — Nur Verweis, keine inhaltliche Regelung zu § 112
  > 112): → StPO § 204 Rn....

### q03 — exakte-paragraphen

**Query:** Welche Haftgruende nennt § 112 Abs. 2 StPO?

**Kontext:** Fluchtgefahr, Verdunkelungsgefahr, Flucht — im StPO-Kommentar

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| vectara | 0.98 | 0% | 0% | 1 | 2.9s |

#### vectara — Top 3
- **[Judge=1]** `['Vorbemerkung zu §§ 211–217']` — Nur Paragraphenverweis ohne Inhalt der Haftgruende
  > 2 Nr. 1 Buchst. h StPO; UHaft § 112 Abs....
- **[Judge=1]** `['Übersicht']` — Nur Paragraphenverweise ohne inhaltliche Erläuterung der Haftgründe
  > 5 S. 1, 148 Abs. 2 S. 1 StPO; § 112 Abs....
- **[Judge=1]** `['7. Untersuchungshaft, einstweilige Unterbringung u...']` — Erwähnt § 112 Abs. 2, aber keine Haftgründe
  > (4) Besteht in den Fällen des § 112 Absatz 3 und des § 112a Absatz 1 StPO auch ein Haftgrund nach § 112 Absatz 2 StPO, sind die Feststellungen hierüber aktenkundig zu machen....

### q04 — exakte-paragraphen

**Query:** Was regelt § 102 StPO zur Durchsuchung beim Beschuldigten?

**Kontext:** Durchsuchungsvoraussetzungen beim Verdaechtigen

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| vectara | 0.88 | 60% | 67% | 2 | 5.2s |

#### vectara — Top 3
- **[Judge=2]** `['Entschädigung für andere Strafverfolgungsmaßnahmen...']` — Erwähnt § 102 StPO, aber keine inhaltlichen Details
  > Durchsuchung iS Nr. 4 ist nur die nach §§ 102, 103 StPO, nicht die nach § 111 StPO (Meyer StrEG Rn....
- **[Judge=2]** `['Übersicht']` — Erwähnt § 102 StPO, aber nur fragmentarisch
  > 27); denn nach § 102 ist sogar die Durchsuchung zum Zweck der Ergreifung zulässig (→ § 102 Rn....
- **[Judge=1]** `['Herausgabepflicht']` — Erwähnt § 102 StPO nur tangential
  > 3; Burhoff StraFo 2021, 398 (400)); einschränkend bei vorhergehender Durchsuchung nach § 102 StPO MüKoStPO/Hausschild Rn....

### q05 — konzept

**Query:** Wann liegt eine konkludente Taeuschung im Sinne des § 263 StGB vor?

**Kontext:** Taeuschungshandlung durch schluessiges Verhalten

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| vectara | 0.76 | 20% | 33% | 1 | 9.0s |

#### vectara — Top 3
- **[Judge=1]** `['Übersicht']` — Nur Verweis auf § 263, keine konkludente Täuschung
  > → § 263 Rn. 193). Liegt auch Betrugsvorsatz vor, geht § 263 vor (→ Rn....
- **[Judge=1]** `['Übersicht', 'Besonders schwere Fälle der Bestechlichkeit und Be...']` — Behandelt § 263, aber besonders schwere Fälle
  > (2) Ein besonders schwerer Fall im Sinne des Absatzes 1 liegt in der Regel vor, wenn 1....
- **[Judge=3]** `['Übersicht']` — Direkt relevant: behandelt konkludente Täuschung bei § 263
  > 12a f.). Bei kollusivem Zusammenwirken zwischen Karteninhaber und Zahlungsannehmer (Vertragsunternehmen) liegt idR eine (konkludente) Täuschung des Ausstellers über die Voraussetzungen der Zahlungspfl...

### q06 — konzept

**Query:** Was ist eine Vermoegensverfuegung und welche Anforderungen stellt die Rechtsprechung?

**Kontext:** Tatbestandsmerkmal der Vermoegensverfuegung beim Betrug

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| vectara | 1.00 | 0% | 0% | 1 | 1.3s |

#### vectara — Top 3
- **[Judge=1]** `['Übersicht']` — Allgemeine Anforderungen, nicht spezifisch Vermoegensverfuegung
  > Maßgeblich sind die Anforderungen, welche die Rechtsordnung an jedermann stellt (BGHSt 43, 66 (77); NStZ-RR 1999, 295 (296); 2015, 137 (138))....
- **[Judge=0]** `['Verlesung eines richterlichen Protokolls bei Gestä...']` — Verlesungsrecht, kein Bezug zu Vermoegensverfuegung
  > Verlesbar sind auch Erklärungen in einem anderen Strafverfahren u. in Zivil- u. Verwaltungsgerichtsverfahren (RGSt 56, 257; Schneidewin JR 1951, 485)), sofern die Voraussetzung für eine Verwertung im ...
- **[Judge=0]** `['Übersicht']` — Behandelt Einwilligung, nicht Vermoegensverfuegung beim Betrug
  > 1 S. 2). Damit die Einwilligung rechtswirksam ist, muss ihr eine Belehrung vorausgehen, welche den Anforderungen des Abs....

### q07 — konzept

**Query:** Was versteht man unter einem Gefaehrdungsschaden beim Betrug?

**Kontext:** Schadensbegriff, schadensgleiche Vermoegensgefaehrdung

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| vectara | 0.97 | 80% | 67% | 3 | 5.0s |

#### vectara — Top 3
- **[Judge=3]** `['Zweiundzwanzigster Abschnitt. Betrug und Untreue']` — Definiert direkt Gefährdungsschaden beim Betrug
  > einen vollendeten Betrug durch Entstehen eines Gefährdungsschadens an, wenn aufgrund tauschender Erklärungen dem Täter ein Überziehungskredit eingeräumt oder Karten mit Einlösungsgarantie ausgehändigt...
- **[Judge=3]** `['Übersicht']` — Definiert direkt Gefährdungsschaden beim Betrug
  > 37 ff. ausdrücklich zwischen „Endschaden“ und „Gefährdungsschaden“ differenziert und dem Letzteren bei der Steuerhinterziehung („ähnlich wie beim Betrug“) ein nur halb so hohes Gewicht beigemessen (Gr...
- **[Judge=1]** `['Zweiundzwanzigster Abschnitt. Betrug und Untreue']` — Behandelt Schadensbegriff, aber nicht Gefaehrdungsschaden spezifisch
  > In Fällen, in denen der Zahlungsempfänger eine Leistung vorab erbringt und anschließend im Rahmen der Abrechnung über das Vorliegen tatsächlicher Anspruchsvoraussetzungen tauscht, ist grundsätzlich de...

### q08 — konzept

**Query:** Wie wird der Vorsatz beim Betrug bestimmt, insbesondere die Bereicherungsabsicht?

**Kontext:** Subjektiver Tatbestand § 263 StGB

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| vectara | 0.99 | 60% | 67% | 2 | 10.0s |

#### vectara — Top 3
- **[Judge=2]** `['Erpressung']` — Erwähnt Bereicherung beim Betrug, aber unvollständiger Kontext
  > Zwischen Schaden und (beabsichtigter) Bereicherung muss, wie beim Betrug (vgl....
- **[Judge=2]** `['Übersicht']` — Erwähnt Bereicherungsabsicht beim Betrug, aber oberflächlich
  > Otto JURA 1994, 143; dazu Kelker, Zur Legitimität von Gesinnungsmerkmalen im Strafrecht, 2007); weiterhin die über den Tatbestand hinausreichenden Absichten (zB Bereicherungsabsicht beim Betrug; Delik...
- **[Judge=1]** `['Zweiundzwanzigster Abschnitt. Betrug und Untreue']` — Nur bibliographische Angabe, keine inhaltliche Information
  > Rostock 2006); Harbort, Die Bedeutung der objektiven Zurechnung beim Betrug, 2010 (Diss....

### q09 — alltagssprache

**Query:** Hat der Angeklagte die Kunden über das Internet betrogen?

**Kontext:** Abstrakte Frage zu Internetbetrug, sucht Taeuschungshandlung + Schaden

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| vectara | 0.62 | 40% | 33% | 0 | 22.6s |

#### vectara — Top 3
- **[Judge=0]** `['Notwendige Auslagen des Nebenklägers']` — Unvollständiger Textauszug ohne erkennbaren Rechtsbezug
  > hat der Angeklagte die dadurch entstandenen bes....
- **[Judge=3]** `['Übersicht']` — Direkt relevant: Internetbetrug, Taeuschung, Kundenkonto
  > Der Tatbestand ist aber erfüllt bei Anlegen eines online-Kundenkontos unter Identitätstäuschung (aber nicht bei Bevollmächtigung des Dritten: BeckRS 2024, 11811), ebenso bei Verändern eines bestehende...
- **[Judge=0]** `['Revisionsbegründung']` — Unvollständiger Text, kein Bezug zu Internetbetrug
  > über eine angeklagte Tat abgesehen hat, denn dann ist das Verf....

### q10 — alltagssprache

**Query:** Wann darf die Polizei bei jemandem zu Hause suchen?

**Kontext:** Durchsuchungsvoraussetzungen, §§ 102 ff. StPO

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| vectara | 0.66 | 20% | 33% | 0 | 3.1s |

#### vectara — Top 3
- **[Judge=0]** `['Übersicht']` — Behandelt Notwehr/Nothilfe, nicht Durchsuchungsrecht
  > Die Polizei darf aber gerade nicht die Erschießung unschuldiger Personen anordnen, um Dritte zu retten....
- **[Judge=3]** `['Zuständigkeit für weitere gerichtliche Entscheidun...']` — Direkt relevant: Durchsuchungsvoraussetzungen für Wohnungen
  > 28 ff.). Die Wohnung des Verdächtigen darf durchsucht werden, wenn konkrete Anhaltspunkte dafür bestehen, dass er dort aufzufinden ist (Kaiser NJW 1980, 876)....
- **[Judge=0]** `['Teil 6 Behandlung von bevorrechtigten Personen bei...']` — Diplomatentransport, keine Durchsuchungsvoraussetzungen behandelt
  > Dann ist es zulässig, den Diplomaten zu seiner Mission oder nach Hause zu bringen....

### q11 — alltagssprache

**Query:** Was passiert wenn jemand luegt damit er Geld bekommt?

**Kontext:** Laienhafte Umschreibung des Betrugstatbestandes

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| vectara | 1.00 | 20% | 33% | 2 | 1.3s |

#### vectara — Top 3
- **[Judge=2]** `['Geldwäsche']` — Betrug thematisch relevant, aber spezifischer Aspekt Finanzagent
  > Für einen Finanzagenten kommt eine Beteiligung an der Vorrat des Betrugs in Betracht, wenn er den Hintermännern sein Bankkonto zur Verfügung stellt, damit die Geschädigten tatplankonform Geld darauf ü...
- **[Judge=0]** `['Geldfälschung']` — Geldfälschung, nicht Betrug durch Täuschung
  > Daher ist Geld „nachgemacht", wenn dem Täter die Legitimation zur Herstellung fehlt (vgl....
- **[Judge=0]** `['Gefährliche Eingriffe in den Bahn-, Schiffs- und L...', 'Gefährliche Eingriffe in den Straßenverkehr']` — Gefährdungsdelikt, nicht Betrug oder Vermögensschaden
  > einen ähnlichen, ebenso gefährlichen Eingriff vornimmt,und dadurch Leib oder Leben eines anderen Menschen oder fremde Sachen von bedeutendem Wert gefährdet, wird mit Freiheitsstrafe bis zu fünf Jahren...

### q12 — alltagssprache

**Query:** Wann muss jemand ins Gefaengnis waehrend die Tat noch nicht bewiesen ist?

**Kontext:** Untersuchungshaft, §§ 112 ff. StPO

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| vectara | 0.63 | 20% | 33% | 0 | 1.5s |

#### vectara — Top 3
- **[Judge=0]** `Strafgesetzbuch` — Behandelt Tatvollendung, nicht Untersuchungshaft
  > Var.). Wenn der Erfolg noch nicht eingetreten ist, muss er die Vollendung der Tat verhindern (3....
- **[Judge=2]** `['Übersicht']` — Thematisch relevant: Beweis und Untersuchungshaft
  > 16) noch nicht bewiesen (BGHSt 10, 276; OLG Köln StraFo 2005, 216)....
- **[Judge=0]** `['Wirkung der Vollziehung des Vermögensarrestes']` — Insolvenzrecht, nicht Untersuchungshaft betreffend
  > 14 Die StA muss Insolvenzforderung u. Insolvenzgrund lediglich glaubhaft machen; bewiesen sein muss die Forderung nicht (Bittmann/Tschakert ZInsO 2017, Köhler ***...

### q13 — stpo-prozess

**Query:** Welche Voraussetzungen hat die Untersuchungshaft wegen Fluchtgefahr?

**Kontext:** § 112 Abs. 2 Nr. 2 StPO Fluchtgefahr

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| vectara | 0.91 | 60% | 33% | 3 | 1.0s |

#### vectara — Top 3
- **[Judge=3]** `['Haftgrund der Wiederholungsgefahr']` — Direkt relevant für Fluchtgefahr-Voraussetzungen nach § 112 StPO
  > (2) In diesen Fällen darf die Untersuchungshaft wegen Fluchtgefahr nur angeordnet werden, wenn der Beschuldigte 1....
- **[Judge=1]** `['Fünfter Unterabschnitt. Verfahren bei Aussetzung d...']` — Jugendstrafrecht, nicht allgemeine Fluchtgefahr-Voraussetzungen
  > (2) Solange der Jugendliche das sechzehnte Lebensjahr noch nicht vollendet hat, ist die Verhängung von Untersuchungshaft wegen Fluchtgefahr nur zulässig, wenn er 1....
- **[Judge=1]** `['7. Untersuchungshaft, einstweilige Unterbringung u...']` — Untersuchungshaft allgemein, aber nicht Fluchtgefahr
  > ² Entscheidend ist vielmehr, ob die Voraussetzungen für die Untersuchungshaft wegen der Krankheit weggefallen sind....

### q14 — stpo-prozess

**Query:** Wie lange darf die Untersuchungshaft maximal dauern?

**Kontext:** § 121 StPO Sechs-Monats-Grenze, Haftpruefung OLG

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| vectara | 0.80 | 40% | 33% | 1 | 1.4s |

#### vectara — Top 3
- **[Judge=1]** `['Nachträgliche Entscheidung über Strafaussetzung zu...']` — Behandelt Haftdauer, aber Sicherungshaft statt Untersuchungshaft
  > Länger als die bei Widerruf der Aussetzung zu verbüßende Strafe darf die Sicherungshaft nicht dauern....
- **[Judge=3]** `['Verfahren bei der Haftprüfung']` — Beantwortet direkt die Frage zur Haftdauer
  > 1 vgl. § 123. Fortdauer der Untersuchungshaft über sechs Monate RiStBV 56 121 (1) Solange kein Urteil ergangen ist, das auf Freiheitsstrafe oder eine freiheitsentziehende Maßregel der Besserung und Si...
- **[Judge=1]** `['Belehrung bei Strafaussetzung oder Verwarnung mit ...']` — Andere Haftart, nicht Untersuchungshaft
  > Länger als die bei Widerruf der Aussetzung zu verbüßende Strafe darf die Sicherungshaft nicht dauern....

### q15 — stpo-prozess

**Query:** Was regelt § 136 StPO zur Beschuldigtenvernehmung?

**Kontext:** Belehrungspflichten, Recht auf Verteidiger

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| vectara | 0.91 | 40% | 67% | 2 | 1.0s |

#### vectara — Top 3
- **[Judge=2]** `['Einleitung']` — Behandelt § 136 StPO aber ohne Belehrungspflichten
  > → StPO § 136 Rn. 3) als Beschuldigtenvernehmung fortzusetzen (BGHSt 22, 129 (132))....
- **[Judge=3]** `['Einleitung']` — Direkter Verweis auf gesuchten Paragraphen 136 StPO
  > dazu → StPO § 136 Rn....
- **[Judge=0]** `Beck'sche Kurz-Kommentare` — Behandelt Ausschreibung zur Festnahme, nicht Vernehmung
  > (1) ¹ In den Fällen des § 131 StPO veranlasst der Staatsanwalt die Ausschreibung des Beschuldigten zur Festnahme und die Niederlegung eines entsprechenden Suchvermerks im Bundeszentralregister....

### q16 — cross-reference

**Query:** Worin unterscheidet sich Betrug von Unterschlagung?

**Kontext:** Abgrenzung § 263 vs § 246 StGB

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| vectara | 0.84 | 60% | 67% | 1 | 0.9s |

#### vectara — Top 3
- **[Judge=1]** `['Erpressung']` — Behandelt Abgrenzung, aber zu Nötigung statt Unterschlagung
  > Vom Betrug unterscheidet sie sich im Mittel, das dort Täuschung, hier Nötigung ist....
- **[Judge=3]** `['Neunzehnter Abschnitt. Diebstahl und Unterschlagun...']` — Direkte Abgrenzung zwischen § 263 und § 246
  > Gegenüber § 263 tritt § 246 zurück, wenn die Zueignung durch Betrug geschieht; dagegen ist ein der Unterschlagung nachfolgender Sicherungsbetrug mitbestrafte Nachtat....
- **[Judge=2]** `['Zweiundzwanzigster Abschnitt. Betrug und Untreue']` — Behandelt Betrug, aber nicht Abgrenzung zur Unterschlagung
  > Ein (vollendeter) Betrug liegt vor, wenn zum Zeitpunkt des Abschlusses eines Verpflichtungsgeschäfts feststeht, dass der durch Täuschung erlangten Verpflichtung (= Vermögensverfügung) eine (irrtumsbed...

### q17 — cross-reference

**Query:** Was sind die Unterschiede zwischen Diebstahl und Raub?

**Kontext:** § 242 vs § 249 StGB — Abgrenzung durch Gewalt/Drohung

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| vectara | 1.00 | 60% | 100% | 3 | 1.8s |

#### vectara — Top 3
- **[Judge=3]** `['Erpressung']` — Direkt relevant: Abgrenzung Diebstahl und Raub
  > Zur Abgrenzung von (Diebstahl und) Raub vgl....
- **[Judge=3]** `['Zwanzigster Abschnitt. Raub und Erpressung']` — Direkt relevant: behandelt Raub-Diebstahl-Abgrenzung
  > Raub und Erpressung§ 249 nur Diebstahl (§ 243 Abs....
- **[Judge=2]** `['Zwanzigster Abschnitt. Raub und Erpressung']` — Thematisch relevant: Diebstahl-Raub-Verhältnis, aber Konkurrenzfragen
  > Tateinheit kann zwischen vollendetem Diebstahl und versuchtem Raub gegeben sein (BGHSt 21, 78; NStZ-RR 2005, 202 (203)); zwischen § 250 und § 249 im Fall unterschiedlicher Begehung gegenüber mehreren ...

### q18 — cross-reference

**Query:** Wann wird Betrug zu Computerbetrug und umgekehrt?

**Kontext:** § 263 vs § 263a StGB — Abgrenzung bei elektronischer Datenverarbeitung

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| vectara | 1.00 | 80% | 100% | 3 | 0.9s |

#### vectara — Top 3
- **[Judge=3]** `['Übersicht']` — Direkt relevant: Verhältnis Betrug zu Computerbetrug
  > Ebenso ist das Verhältnis zwischen (möglicher) Beteiligung am Betrug und (sicherem) späterem Computerbetrug hinsichtlich desselben Schadens zu behandeln (BGH NStZ 2008, 396 (396 f.))....
- **[Judge=3]** `['Zweiundzwanzigster Abschnitt. Betrug und Untreue']` — Direkt relevant: Abgrenzung Betrug vs Computerbetrug
  > (Teil 1), GA 2023, 615; (Teil 2) GA 2023, 675; Schuhr, Betrug vs. Computerbetrug....
- **[Judge=3]** `['Neunzehnter Abschnitt. Diebstahl und Unterschlagun...']` — Direkt relevant für Abgrenzung § 263/263a StGB
  > 4), Computerbetrug (§ 263a Abs....