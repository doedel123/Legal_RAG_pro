# RAG Benchmark Report

_Generiert: 2026-04-21T23:30:41_


- Queries: **12**
- Top-K: **10**
- Systeme: ours-mxbai, pageindex

## Gesamtvergleich

| Metrik | ours-mxbai | pageindex |
|--------|--------|--------|
| nDCG@10 | 0.953 | 0.869 |
| Relevance@10 | 79.2% | 60.3% |
| Relevance@3 | 86.1% | 77.8% |
| Top-1-Score | 2.83 | 2.33 |
| Mean-Score | 2.32 | 1.81 |
| Latenz (s) | 5.23 | 3.14 |

## Nach Kategorie


### ermittlungsmass

| Metrik | ours-mxbai | pageindex |
|--------|--------|--------|
| nDCG@10 | 0.937 | 0.585 |
| Relevance@10 | 73.3% | 34.4% |
| Relevance@3 | 77.8% | 55.6% |

### fakten

| Metrik | ours-mxbai | pageindex |
|--------|--------|--------|
| nDCG@10 | 0.974 | 0.918 |
| Relevance@10 | 93.3% | 80.0% |
| Relevance@3 | 88.9% | 77.8% |

### juristisch

| Metrik | ours-mxbai | pageindex |
|--------|--------|--------|
| nDCG@10 | 0.930 | 0.990 |
| Relevance@10 | 80.0% | 86.7% |
| Relevance@3 | 77.8% | 100.0% |

### sachverhalt

| Metrik | ours-mxbai | pageindex |
|--------|--------|--------|
| nDCG@10 | 0.970 | 0.984 |
| Relevance@10 | 70.0% | 40.0% |
| Relevance@3 | 100.0% | 77.8% |

## Detail pro Query


### a01 — fakten

**Query:** Wer ist die Geschaedigte im Fall donkredito?

**Kontext:** Name, Geburtsdatum, Wohnort der Geschaedigten aus Anzeige und Vernehmung

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours-mxbai | 0.99 | 90% | 100% | 3 | 4.7s |
| pageindex | 0.94 | 60% | 67% | 3 | 2.9s |

#### ours-mxbai — Top 3
- **[Judge=3]** `?` — Nennt Geschädigte Zeynep Taya mit Wohnort Karlsruhe
  > ### a) Ursprung des Verfahrens und Vermögensschaden   Das Verfahren beruht auf einer Strafanzeige der Zeugin Zeynep Taya aus Karlsruhe vom 24.06.2020. Die Zeugin hatte nach eigenen Angaben am 20.05.20...
- **[Judge=3]** `?` — Günes, Hasan als Geschädigter mit Personaldaten identifiziert
  > ## Seite 17   Name Günes, Hasan, *10.09.1972 Aktenzeichen 240614-0943-069732  ☑ Ich bin/war mit der/dem Betroffenen/Beschuldigten nicht verheiratet, in Lebenspartnerschaft lebend, geschieden, verwandt...
- **[Judge=3]** `?` — Name und Geburtsdatum der Geschaedigten Dittmar
  > ## Seite 58   SA  |  Name Dittmar, Angelina, *27.09.1996 | Aktenzeichen 240620-0658-032830  | | --- | --- |  ☑ Ich bin/war mit der/dem Betroffenen/Beschuldigten **nicht** verheiratet, in Lebenspartner...

#### pageindex — Top 3
- **[Judge=3]** `GESCHÄDIGTE PERSON` — Direkt relevant: Name, Geburtsdatum, Wohnort der Geschaedigten
  > # GESCHÄDIGTE PERSON  Name Taya Geburtsname Taya Vorname Zeyneb Geburtsdatum 23.08.2001 Geburtsort/-land Karlsruhe Geschlecht weiblich Staatsangehörigkeit deutsch Anschrift 76133 Karlsruhe Kronenstraß...
- **[Judge=1]** `SACHVERHALT` — Sachverhalt ohne Namen, Geburtsdatum oder Wohnort
  > # SACHVERHALT  Die Geschädigte erhielt am 20.05.2020 von der Firma Payplus GmbH eine Rechnung in Höhe von 30,00 Euro für eine Bonitätsabrechnung, welche angeblich am 06.05.2020 vertraglich abgeschloss...
- **[Judge=3]** `GESCHÄDIGTEN - VERNEHMUNG` — Direkte Antwort: Name, Geburtsdatum, Wohnort der Geschaedigten
  > # GESCHÄDIGTEN - VERNEHMUNG  Vernehmungsort Karlsruhe Prev. KA-Marktplatz Beginn 24.06.2020 18.08 Uhr  ## Zur Person  Name Taya Geburtsname Taya Vorname Zeyneb Geburtsdatum 23.08.2001 Geburtsort/-land...

### a02 — fakten

**Query:** Wer sind die Beschuldigten und welche Firmen leiten sie?

**Kontext:** Namen der Beschuldigten und deren Rollen bei Payplus, Clever Cards, Intaxx

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours-mxbai | 0.98 | 100% | 100% | 3 | 5.7s |
| pageindex | 0.98 | 90% | 100% | 3 | 3.8s |

#### ours-mxbai — Top 3
- **[Judge=3]** `?` — Nennt Beschuldigten Davies und seine Firmen
  > ## dd) Clever Cards B.V. und Intaxx B.V.   Geschäftsführer der Firmen Clever Cards B.V. und Intaxx B.V. (Bl. 71 ff. der Akten) ist der Zeuge Maurice Christiaan Davies, der als weiterer Beschuldigter i...
- **[Judge=3]** `?` — Beschuldigte Walter und Tanja Völl mit Firmendetails
  > ## Seite 147   Staatsanwaltschaft Aachen - 107 Js 1286/20 - Aachen, 07.07.2025 Seite 5 von 7 601  übernommen und mit dem vorliegenden Verfahren verbunden worden ist, ergeben sich aber keine Hinweise a...
- **[Judge=2]** `?` — Erwähnt relevante Firmen, keine direkten Beschuldigtennamen
  > ## Seite 161   615  - 8 -  18. Bestätigungsmail an die Zeugin Mohr (Bl. 27 VA 107 Js 2430/20), 19. Bestätigungsmail an den Zeugen Vent (Bl. 12 VA 107 Js 2473/20), 20. Bestätigungsmail an den Zeugen Ba...

#### pageindex — Top 3
- **[Judge=3]** `Anklageschrift > Seite 180` — Nennt Angeschuldigten Völl und Schweers mit Firmen
  > ## Seite 180  634  "huhu  anbei die AGB inklusive Widerrufsbelehrung für Credify.me und Schufaheld.  Also wir können hier zum 1.12. starten, müsste noch der Nummernkreis für die Nachnamen geändert wer...
- **[Judge=3]** `Anklageschrift > aa) PLUS CARDS LTD` — Nennt direkt Beschuldigte und deren Firmenrollen
  > ## aa) PLUS CARDS LTD  Geschäftsführer der PLUS CARDS LTD, eingetragener Geschäftssitz 20-22 Wenlock Road, London, England, N1 7GU, waren gemäß Register des Companies House die ursprünglich als Beschu...
- **[Judge=3]** `Anklageschrift > bb) payplus GmbH` — Nennt Beschuldigte und deren Rollen bei Payplus
  > ## bb) payplus GmbH  Die payplus GmbH wurde am 09.12.2009 gegründet. Gesellschafter mit einem Kapitalanteil in Höhe von jeweils 12.500,00 Euro waren ursprünglich die gesondert Verfolgten Dirk Pollex u...

### a03 — fakten

**Query:** Unter welchem Aktenzeichen wird der Fall gefuehrt?

**Kontext:** Aktenzeichen der Staatsanwaltschaft Aachen bzw. Karlsruhe

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours-mxbai | 0.95 | 90% | 67% | 3 | 5.5s |
| pageindex | 0.83 | 90% | 67% | 0 | 4.9s |

#### ours-mxbai — Top 3
- **[Judge=3]** `?` — Enthält beide Aktenzeichen: 107 Js 1286/20 (Aachen), NZS 9103 Js 18408/23 (Lüneburg)
  > ## Urschriftlich VAV   ☐ mit Beiakten  der / dem  ☐ Polizeibehörde ☑ Staatsanwaltschaft, Abtlg. z.Hd. Herrn Bodden 107 Js 1286/20 ☐ Amtsgericht in Aachen  ☐ mit der Bitte, den ☐ Beschuldigte/n ☐ Zeugi...
- **[Judge=3]** `?` — Aktenzeichen 201211-1121-027406 klar ersichtlich
  > ## Ermittlungsverfahren gegen Eduard Müller, geboren am 04.09.1971 in Rubcovsk, u. a.   Tatvorwurf: Gewerbsmäßiger Betrug als Mitglied einer Bande Ihr Zeichen: 201211-1121-027406  *denkaldo*  Um Rücks...
- **[Judge=0]** `?` — Asservatenliste ohne spezifische Aktenzeichen-Angaben
  > ## Seite 8   StrA übersenden  |  Asservatennu ID | Datum | Asservatenbezeichnung | Vorgangsnummer | zuet. Dat. / S | Anfrage StrA  | | --- | --- | --- | --- | --- | --- | |  A-22-1138 | 17328 | 08.08....

#### pageindex — Top 3
- **[Judge=0]** `Seite 1` — Keine Aktenzeichen der Staatsanwaltschaft erkennbar
  > ## Seite 1  Termine: 13  Landesjustizprüfungsamt ☐ Ja ☑ Nein Staatsarchiv: ☐ Ja ☑ Nein Unterschrift der Richterin / des Richterin der Staatsanwältin / des Staatsanwalts  Mitteilung nach Nrn. _________...
- **[Judge=3]** `Strafsache/Bußgeldsache` — Enthält das gesuchte Aktenzeichen 107 Js 1286/20
  > # Strafsache/Bußgeldsache  bei _______________  Verteidiger/in: Vollmacht: zur Pflichtverteidigerin/ zum Pflichtverteidiger bestellt:  RA. _______________ BI. _______________ BI. _______________  RA. ...
- **[Judge=3]** `Asservat` — Aktenzeichen 107 Js 1286/20 bei Staatsanwaltschaft Aachen
  > # Asservat  Erledigung siehe BI.  verbunden mit/zu:  Weggelegt 998AR 12/21 o.h.a. Aufzubewahren bis - dauernd - dankredito.com  6216s 54/21  AU 151 Strafsache / Bußgeld - gen. 08.2011 Justizvollzugsan...

### a04 — sachverhalt

**Query:** Wie lief die Betrugsmasche auf donkredito.com ab?

**Kontext:** Geschaeftsmodell der Website, wie Opfer zu Zahlungsverpflichtungen gelangten

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours-mxbai | 0.99 | 100% | 100% | 3 | 5.8s |
| pageindex | 0.97 | 80% | 100% | 3 | 3.2s |

#### ours-mxbai — Top 3
- **[Judge=3]** `?` — Direkter Bezug zu Betrugsmasche und Geschäftsmodell
  > # Anklageschrift   I. Walter Völl, geboren am 16.04.1974 in Düren, wohnhaft Vlijtingerweg 45, BE 3620 Lanaken, verheiratet, deutscher Staatsangehöriger,  - Verteidiger: Rechtsanwalt Bücken, Stolberger...
- **[Judge=3]** `?` — Direkte Beschreibung der Betrugsmasche und Opfererfahrungen
  > ## Seite 174   678  Der Zeuge Wundschittel wird angeben, davon ausgegangen zu sein, über die Seite www.donkredito.com eine Kreditkarte mit einem Kredit über 4.500,00 € mit einer monatlichen Rate i.H.v...
- **[Judge=3]** `?` — Beschreibt detailliert die Betrugsmasche der Website
  > ## Seite 155   609  - 2 -  wurden sowie der Euro Collect GmbH, die als Inkassodienstleister säumige Besteller in Anspruch nahm.  Die Programmierung der Seite https://donkredito.com war - wie dem Anges...

#### pageindex — Top 3
- **[Judge=3]** `Anklageschrift > Seite 155` — Detaillierte Beschreibung der Betrugsmasche auf donkredito.com
  > ## Seite 155  609  - 2 -  wurden sowie der Euro Collect GmbH, die als Inkassodienstleister säumige Besteller in Anspruch nahm.  Die Programmierung der Seite https://donkredito.com war - wie dem Angesc...
- **[Judge=3]** `Anklageschrift > Seite 156` — Direkte Beschreibung der Betrugsmasche auf donkredito.com
  > ## Seite 156  610  - 3 -  Besucher erst nach Scrollen über einen weiteren erst „Demnächst“ verfügbaren Tarif in kleinerer Schriftgröße angezeigt und lauteten: „* Diese Gebühren sind sofort und vor Kar...
- **[Judge=3]** `Anklageschrift > Seite 157` — Beschreibt detailliert die taeuscherische Website-Gestaltung von donkredito.com
  > ## Seite 157  611  Auswahlkästchen mussten sämtlich aktiviert werden, um den Vorgang fortsetzen zu können.  Bei Lektüre der AGB zum Dienst Schufaheld der Clever Cards BV konnte der Nutzer nach einer V...

### a05 — sachverhalt

**Query:** Welche Zahlungen wurden von der Geschaedigten gefordert und wann?

**Kontext:** Konkrete Rechnungen, Mahnungen, Betraege und Daten

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours-mxbai | 0.95 | 50% | 100% | 3 | 4.8s |
| pageindex | 0.98 | 30% | 100% | 3 | 5.6s |

#### ours-mxbai — Top 3
- **[Judge=3]** `?` — Enthält konkrete Zahlungsaufforderungen mit Beträgen und Daten
  > ### a) Ursprung des Verfahrens und Vermögensschaden   Das Verfahren beruht auf einer Strafanzeige der Zeugin Zeynep Taya aus Karlsruhe vom 24.06.2020. Die Zeugin hatte nach eigenen Angaben am 20.05.20...
- **[Judge=2]** `?` — Thematischer Kontext zu Forderungen und Zahlungen
  > ## Seite 174   678  Der Zeuge Wundschittel wird angeben, davon ausgegangen zu sein, über die Seite www.donkredito.com eine Kreditkarte mit einem Kredit über 4.500,00 € mit einer monatlichen Rate i.H.v...
- **[Judge=3]** `?` — Direkt relevant: konkrete Betraege und Zahlungsdaten
  > # Zur Sache   Am 20.05.2020 erhielt ich eine Rechnung durch die Firma Payplus GmbH über 30,00 Euro für eine Kreditkarte. Ich hatte zu keiner Zeit solch eine Kreditkarte bei diesem oder einem anderen U...

#### pageindex — Top 3
- **[Judge=3]** `ZAHLUNGSAUFFORDERUNG` — Konkrete Zahlungsaufforderung mit Betrag und Frist
  > # ZAHLUNGSAUFFORDERUNG  ## Rechnung CMP-2231278  ### Ihr Vertrag vom 06.05.2020 auf donkredito.com  Sehr geehrte Frau Taya,  vielen Dank für Ihr Vertrauen und, dass Sie uns am 06.05.2020 mit der **Ver...
- **[Judge=2]** `Eingang Zahlungserinne` — Enthält Zahlungsforderung aber unvollständige Informationen
  > # Eingang Zahlungserinne  ## Bearbeitungskosten  1 x Mahngebühr  Gesamt:  Bitte überweisen Sie die Forderung i.H. von 29,90 folgende folgende Bank unseres Finanzdienstleis  ---  ## Seite 24  Von meine...
- **[Judge=3]** `&lt; Eingang Zahlungserinne` — Direkte Zahlungsaufforderung mit Rechnungsdatum 20.05
  > # &lt; Eingang Zahlungserinne  leider haben Sie Ihre Seh- und entgegengenommen und wiederrufen. Dennoch sind wir für uns entstanden, welche unseren AGB`s, die Sie Bestellvorgang und mit Verifizierung ...

### a06 — sachverhalt

**Query:** Welche Rolle spielte Dominic Dietrich im Fall?

**Kontext:** Dominic Dietrich als Partner / Zeuge bei E-Mail-Marketing fuer donkredito

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours-mxbai | 0.96 | 60% | 100% | 3 | 4.6s |
| pageindex | 1.00 | 10% | 33% | 3 | 2.1s |

#### ours-mxbai — Top 3
- **[Judge=3]** `?` — Dominic Dietrich direkt als DD bei E-Mail-Marketing genannt
  > ## Seite 122   Name Aharroud, Mimount, *01.09.1976 Aktenzeichen 608000-054221-20/7  erinnere Bevigra (Bediamond), eine Mastercard (Veripay), Slimsticks (PayPlus GmbH) und ich meine das da auch Seitens...
- **[Judge=3]** `?` — Direkter Bezug zu Dominic Dietrich und Werbepartnerschaften
  > ## Seite 108   Name Völl. Walter, *16.04.1974 Aktenzeichen 608000-018798-19/8  Antwort:  Druck und Versand wurde durch payplus (Dirk Pollex) übernommen und das Mahnwesen durch Verify.  Wir wollten die...
- **[Judge=2]** `?` — Bedenken zu Dietrich wegen Geldwäsche-Nachfragen erwähnt
  > ## Seite 106   Name Völl, Walter, *16.04.1974 Abbezeichen 608000-018798-19/8 98  Antwort:  Nur aus dem Partnerprogramm, nicht persönlich.  Daten habe ich nicht dabei.  Es ist ein öffentlich einsehbare...

#### pageindex — Top 3
- **[Judge=3]** `Anklageschrift > Seite 181` — Zeigt Dietrichs direkte Rolle als E-Mail-Marketing-Partner
  > ## Seite 181  635  Am 27.03.18 um 16:12 Uhr schrieb Dominik Dietrich (a.dietrich@plpverlag.de) an Walter Völl (w.v.@payplus.de) [Hervorhebung Fettdruck durch Unterzeichner, Bl. 107 SH I]:  „Servus Wal...
- **[Judge=1]** `Anklageschrift > Seite 182` — Namensvariation Dominik statt Dominic, E-Mail-Marketing Kontext
  > ## Seite 182  636  Hoffe das sagt zu?  LG  Walter  Am 12.04.2018 um 9:25 Uhr schrieb Walter Völl Bl. 103 SH I:  „Hi Dominik,  ich würde sagen wir machen das genauso. Das sieht sehr geil aus. Wir heben...
- **[Judge=0]** `Anklageschrift > b) Zu den Gesellschaften` — Keine Informationen zu Dominic Dietrich enthalten
  > ## b) Zu den Gesellschaften...

### a07 — ermittlungsmass

**Query:** Wurde eine Europaeische Ermittlungsanordnung erlassen?

**Kontext:** EEA nach Richtlinie 2014/41/EU fuer grenzueberschreitende Ermittlungen

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours-mxbai | 1.00 | 100% | 100% | 3 | 5.5s |
| pageindex | 0.93 | 70% | 100% | 3 | 2.2s |

#### ours-mxbai — Top 3
- **[Judge=3]** `?` — Direkter Nachweis einer erlassenen EEA nach Richtlinie 2014/41/EU
  > # EUROPÄISCHE ERMITTLUNGSANORDNUNG (EEA)   Diese EEA wurde von einer zuständigen Behörde angeordnet. Die Anordnungsbehörde bescheinigt, dass der Erlass dieser EEA für die Zwecke des darin angegebenen ...
- **[Judge=3]** `?` — Direkter Nachweis der erlassenen EEA nach Richtlinie 2014/41/EU
  > # Vfg.   1. Europ. Ermittlungsanordnung (EEA) mit Dienstsiegel versehen (unter Abschnitt K, wenn EEA von StA, unter Abschnitt L – Dienstsiegel – wenn lediglich validiert) 2. Frau AL’in IX o. V. [Handw...
- **[Judge=3]** `?` — Direkte Antwort: EEA wurde erlassen
  > # EUROPÄISCHE ERMITTLUNGSANORDNUNG (EEA)   Diese EEA wurde von einer zuständigen Behörde angeordnet. Die Anordnungsbehörde bescheinigt, dass der Erlass dieser EEA für die Zwecke des darin angegebenen ...

#### pageindex — Top 3
- **[Judge=3]** `Europäische Ermittlungsanordnung nach Richtlinie 2014/41/EU` — Direkte Bestätigung: EEA wurde erlassen und übermittelt
  > # Europäische Ermittlungsanordnung nach Richtlinie 2014/41/EU  Sehr geehrte Damen und Herren Kollegen,  meine Behörde führt gegen die serbische Staatsangehörige Dobrila Bigovic, geboren im September 1...
- **[Judge=3]** `EUROPÄISCHE ERMITTLUNGSANORDNUNG (EEA)` — Direkte Antwort: EEA wurde von Deutschland erlassen
  > # EUROPÄISCHE ERMITTLUNGSANORDNUNG (EEA)  Diese EEA wurde von einer zuständigen Behörde angeordnet. Die Anordnungsbehörde bescheinigt, dass der Erlass dieser EEA für die Zwecke des darin angegebenen V...
- **[Judge=3]** `ABSCHNITT G: Gründe für den Erlass der EEA:` — EEA-Formular mit Sachverhalt und Ermittlungsgruenden
  > # ABSCHNITT G: Gründe für den Erlass der EEA:  ## 1. Zusammenfassung des Sachverhalts  Legen Sie die Gründe dafür dar, weshalb die EEA erlassen wird, einschließlich einer Zusammenfassung des zugrunde ...

### a08 — ermittlungsmass

**Query:** Was ergaben die Whois- und VPN-Recherchen?

**Kontext:** IP-Adresse 185.51.8.84, Whois-Daten, VPN-Anbieter Whoer

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours-mxbai | 0.85 | 30% | 33% | 3 | 5.8s |
| pageindex | 0.83 | 33% | 67% | 1 | 2.3s |

#### ours-mxbai — Top 3
- **[Judge=3]** `?` — Zeigt konkrete Whois-Recherche zur gesuchten IP-Adresse
  > ## Seite 84   Staatsanwaltschaft Aachen - 107 Js 1286/20 - Aachen, 04.11.2020 Seite 3 von 3  3. Die Verfahren  |  107 Js 1551/20 | 107 Js 1866/20 | 107 Js 2049/20  | | --- | --- | --- | |  107 Js 1675...
- **[Judge=0]** `?` — Formular zu Rechtshilfeersuchen, keine Whois/VPN-Rechercheergebnisse
  > ## Seite 99   91  Wird um derartige Ermittlungsmaßnahmen ersucht, so geben Sie bitte die Gründe dafür an, weshalb die Informationen, um die ersucht wird, Ihres Erachtens für die Zwecke des Strafverfah...
- **[Judge=0]** `?` — Formular-Template ohne konkrete Whois-/VPN-Ergebnisse
  > ## Seite 56   234  |  ☐ Informationen über Bankgeschäfte  | | --- | |  ☐ Informationen über sonstige Finanzgeschäfte  | |  Geben Sie bitte die betreffenden Zeiträume und die entsprechenden Konten an: ...

#### pageindex — Top 3
- **[Judge=1]** `Whois IP` — Allgemeine Whois-Info, nicht spezifisch zur gesuchten IP
  > # Whois IP  Whois suchen nach domain und IP  https://donkredito.com  Überprüfen  Whois-Service ist ein Service, der erlaubt, Informationen über den Standort der IP-Adressen, der Sie abzurufen. Sie kön...
- **[Judge=3]** `IP-Adresse: 185.51.8.84` — Direkte Antwort auf Whois-Recherche zur gesuchten IP
  > # IP-Adresse: 185.51.8.84  Standort: Austria (AT), Europe  Region: Niederösterreich  Stadt: Obritzberg  PLZ: 3123  Hostname: web19.easyname.com → 185.51.8.84  IP-Bereich: 185.51.8.0 - 185.51.10.255  I...
- **[Judge=3]** `Whois IP` — Direkt relevante Whois-Daten zur IP 185.51.8.84
  > # Whois IP  Whois suchen nach domain und IP  https://donkredito.com  Überprüfen  Whois-Service ist ein Service, der erlaubt, Informationen über den Standort der IP-Adressen, der Server und der Webseit...

### a09 — ermittlungsmass

**Query:** Welche Asservate wurden sichergestellt?

**Kontext:** Asservatenliste, Asservatennummern, beschlagnahmte Gegenstaende

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours-mxbai | 0.96 | 90% | 100% | 3 | 5.0s |
| pageindex | 0.00 | 0% | 0% | 0 | 2.2s |

#### ours-mxbai — Top 3
- **[Judge=3]** `?` — Direkte Asservatenliste mit Nummern und Gegenstaenden
  > ## Seite 5   Staatsanwaltschaft  Aachen, 16.03.2023  107 Js 1286/20  Lagerort: Hauptraum  Ass.-Listen Nr.: 2689/23  bei Abgabe an das Gericht:  ges. Aufbew.Nr.:  Ass.Listen Nr.dort:  Verw.B.Nr.:  List...
- **[Judge=2]** `?` — Erwähnt Asservate und Aufbereitung, keine konkrete Liste
  > ## 01   Der Auftrag zwecks weiterer Aufbereitung des Festplatte HD870 wurde am 16.12. 2022 an die IT-Unterstützung des KK 22 weitergeleitet.  Durch den Sondereinsatz Lützerath über den gesamten Januar...
- **[Judge=3]** `?` — Asservatenliste mit konkreten Gegenstaenden und Nummern
  > # Anlage   QCRM-M21-027406  zur Durchsuchung/Sicherstellung vom: 30.3.2022  Betroffener: Firma kayplus  Ermittlungsverfahren: STA AC 107 y5 1286/20  |  1 f d. Nr. | Menge | Gegenstand / Zustand | letz...

#### pageindex — Top 3

### a10 — juristisch

**Query:** Welcher Tatvorwurf wird in der Anklageschrift erhoben?

**Kontext:** §§ aus der Anklageschrift, vorgeworfene Straftaten (z.B. Betrug, Bandenbetrug)

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours-mxbai | 0.79 | 40% | 33% | 1 | 4.7s |
| pageindex | 0.98 | 60% | 100% | 3 | 2.2s |

#### ours-mxbai — Top 3
- **[Judge=1]** `?` — Kontext zu Ermittlungen, keine konkreten Tatvorwürfe
  > ## dd) Clever Cards B.V. und Intaxx B.V.   Geschäftsführer der Firmen Clever Cards B.V. und Intaxx B.V. (Bl. 71 ff. der Akten) ist der Zeuge Maurice Christiaan Davies, der als weiterer Beschuldigter i...
- **[Judge=3]** `?` — Direkter Tatvorwurf: gewerbsmäßiger Betrug mit Vermögensschädigung
  > # Anklageschrift   I. Walter Völl, geboren am 16.04.1974 in Düren, wohnhaft Vlijtingerweg 45, BE 3620 Lanaken, verheiratet, deutscher Staatsangehöriger,  - Verteidiger: Rechtsanwalt Bücken, Stolberger...
- **[Judge=1]** `?` — Nur Zeugenliste, keine Tatvorwürfe genannt
  > # Zeugenliste   Die ladungsfähigen Anschriften der im vorliegenden Verfahren in der Anklageschrift vom 25.06.2025 benannten Zeugen, auch soweit von der Benennung der vollständigen Anschriften gem. § 2...

#### pageindex — Top 3
- **[Judge=3]** `Anklageschrift` — Direkt relevante Tatvorwürfe: Betrug, gewerbsmäßig, bandenförmig
  > # Anklageschrift  I. Walter Völl, geboren am 16.04.1974 in Düren, wohnhaft Vlijtingerweg 45, BE 3620 Lanaken, verheiratet, deutscher Staatsangehöriger,  - Verteidiger: Rechtsanwalt Bücken, Stolberger ...
- **[Judge=3]** `Anklageschrift > Seite 155` — Beschreibt detailliert Täuschungshandlungen der Anklageschrift
  > ## Seite 155  609  - 2 -  wurden sowie der Euro Collect GmbH, die als Inkassodienstleister säumige Besteller in Anspruch nahm.  Die Programmierung der Seite https://donkredito.com war - wie dem Angesc...
- **[Judge=3]** `Anklageschrift > Seite 156` — Beschreibt detailliert den angeklagten Tatmodus operandi
  > ## Seite 156  610  - 3 -  Besucher erst nach Scrollen über einen weiteren erst „Demnächst“ verfügbaren Tarif in kleinerer Schriftgröße angezeigt und lauteten: „* Diese Gebühren sind sofort und vor Kar...

### a11 — juristisch

**Query:** Welche Durchsuchungen wurden angeordnet und wo fanden sie statt?

**Kontext:** Durchsuchungsbeschluesse, Orte (z.B. Heinsberg), Zeitpunkte

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours-mxbai | 1.00 | 100% | 100% | 3 | 5.9s |
| pageindex | 1.00 | 100% | 100% | 3 | 2.4s |

#### ours-mxbai — Top 3
- **[Judge=3]** `?` — Durchsuchungsbeschluss mit konkreten Anordnungen und Zielen
  > ## Beschluss   In dem Ermittlungsverfahren  gegen 1. Patrick Schweers, geboren am 13. Mai 1986 in Oldenburg, wohnhaft Am Acker 1 A, 27243 Beckeln  2. Kai Kröger, geboren am 04. September 1988, wohnhaf...
- **[Judge=3]** `?` — Durchsuchungsbeschluss mit konkreten Orten und Anordnung
  > ## Beschluss   In dem Ermittlungsverfahren  gegen Maurice Christiaan Davies, geboren am 13. Dezember 1994 in Emmerich, deutscher Staatsangehöriger, ledig wohnhaft Mittelstraße 6, 52538 Gangelt,  wegen...
- **[Judge=3]** `?` — Direkt relevant: Durchsuchungsbeschluss mit genauem Ort
  > ## Beschluss   In dem Ermittlungsverfahren  gegen: Patrick Schweers, geboren am 13. Mai 1986 in Oldenburg, wohnhaft Am Acker 1 A, 27243 Beckeln u.a.  wegen des Verdachts des Bandenbetrugs  Gemäß §§ 10...

#### pageindex — Top 3
- **[Judge=3]** `Durchsuchungs-/Sicherstellungsprotokoll` — Durchsuchungsprotokoll mit Ort und Zeitpunkt
  > # Durchsuchungs-/Sicherstellungsprotokoll  |  Angesordnet durch: (Name Beamtin/Beamter mit Dienststelle oder anerkannte Stelle mit Anlehr-/Geschäftszeichen) Als, Hallo, Beadluss 021 GS 1955/21 (107 Js...
- **[Judge=3]** `Durchsuchungs-/Sicherstellungsprotokoll` — Durchsuchungsprotokoll mit Datum, Ort, sichergestellten Gegenstaenden
  > # Durchsuchungs-/Sicherstellungsprotokoll  Verzeichnis der sichergestellten/beschlagnahmten Gegenstände  35ta  vom 20.2.2022 Betroffene/Betroffener Fa. Payplus  |  Ifd. Nr. | Menge | Gegenstand (Art/B...
- **[Judge=3]** `Durchsuchungsbericht` — Durchsuchungsbeschluss mit konkreter Person und Adresse
  > # Durchsuchungsbericht  Der Beschluss richtet sich gegen  Maurice Christiaan Davis  *13.12.1994 Emmerich  Mittelstraße 6  52538 Gangelt  wegen des Verdachts des gewerbsmäßigen Bandenbetruges....

### a12 — juristisch

**Query:** Welche Zeugen wurden vernommen und zu welchen Themen?

**Kontext:** Zeugenvernehmungen, Namen der Zeugen, Inhalt der Aussagen

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours-mxbai | 1.00 | 100% | 100% | 3 | 4.7s |
| pageindex | 0.99 | 100% | 100% | 3 | 4.0s |

#### ours-mxbai — Top 3
- **[Judge=3]** `?` — Direkt relevant: Name und Daten einer Zeugin
  > # Zeugenvernehmung   |  Beginn der Vernehmung (Datum, Uhrzeit) 10.07.2024, 10:45 Uhr | Ort der Vernehmung Eschweiler  | | --- | --- | |  Mir wurde eröffnet, zu welcher Sache ich gehört werden soll.  |...
- **[Judge=3]** `?` — Zeigt Zeugin Sabrina Meeßen, Vernehmung am 05.07.2024
  > # Zeugenvernehmung   |  Beginn der Vernehmung (Datum, Uhrzeit) 05.07.2024, 11:39 Uhr | Ort der Vernehmung KK13  | | --- | --- | |  Mir wurde eröffnet, zu welcher Sache ich gehört werden soll.  |   | |...
- **[Judge=3]** `?` — Zeuge Ralph Hauser vernommen zu Bandenbetrug probenheld.de
  > # Zeugenvernehmung   |  Beginn der Vernehmung (Datum, Uhrzeit) 03.09.2020, 08:27 Uhr | Ort der Vernehmung Aachen  | | --- | --- | |  Mir wurde eröffnet, zu welcher Sache ich gehört werden soll.  |   |...

#### pageindex — Top 3
- **[Judge=3]** `Zeugenvernehmung` — Zeuge Ingo-Ludwig Bolz identifiziert, Betrugs-Kontext gegeben
  > # Zeugenvernehmung  |  Beginn der Vernehmung (Datum, Uhrzeit) 01.09.2020, 12:29 Uhr | Ort der Vernehmung Aachen  | | --- | --- | |  Mir wurde eröffnet, zu welcher Sache ich gehört werden soll.  |   | ...
- **[Judge=3]** `Zeugenvernehmung` — Zeuge Ralph Hauser vernommen zu Betrugsvorwurf
  > # Zeugenvernehmung  |  Beginn der Vernehmung (Datum, Uhrzeit) 03.09.2020, 08:27 Uhr | Ort der Vernehmung Aachen  | | --- | --- | |  Mir wurde eröffnet, zu welcher Sache ich gehört werden soll.  |   | ...
- **[Judge=3]** `Zeugenvernehmung` — Zeugenvernehmung mit Namen und Verfahrensdetails dokumentiert
  > # Zeugenvernehmung  |  Beginn der Vernehmung (Datum, Uhrzeit) 28.10.2020, 10:08 Uhr | Ort der Vernehmung Aachen  | | --- | --- | |  Mir wurde eröffnet, zu welcher Sache ich gehört werden soll.  |   | ...