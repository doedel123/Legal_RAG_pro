# RAG Benchmark Report

_Generiert: 2026-04-16T09:50:29_


- Queries: **18**
- Top-K: **10**
- Systeme: openai, ours, ragie

## Gesamtvergleich

| Metrik | openai | ours | ragie |
|--------|--------|--------|--------|
| nDCG@10 | 0.718 | 0.975 | 0.945 |
| Relevance@10 | 34.4% | 82.8% | 84.6% |
| Relevance@3 | 48.1% | 96.3% | 87.0% |
| Top-1-Score | 1.67 | 2.89 | 2.61 |
| Mean-Score | 1.13 | 2.42 | 2.45 |
| Latenz (s) | 1.68 | 6.48 | 2.24 |

## Nach Kategorie


### alltagssprache

| Metrik | openai | ours | ragie |
|--------|--------|--------|--------|
| nDCG@10 | 0.537 | 0.979 | 0.948 |
| Relevance@10 | 25.0% | 92.5% | 80.6% |
| Relevance@3 | 33.3% | 100.0% | 83.3% |

### cross-reference

| Metrik | openai | ours | ragie |
|--------|--------|--------|--------|
| nDCG@10 | 0.854 | 0.963 | 0.923 |
| Relevance@10 | 26.7% | 80.0% | 81.5% |
| Relevance@3 | 44.4% | 88.9% | 88.9% |

### exakte-paragraphen

| Metrik | openai | ours | ragie |
|--------|--------|--------|--------|
| nDCG@10 | 0.887 | 0.987 | 0.916 |
| Relevance@10 | 37.5% | 87.5% | 81.3% |
| Relevance@3 | 66.7% | 100.0% | 75.0% |

### konzept

| Metrik | openai | ours | ragie |
|--------|--------|--------|--------|
| nDCG@10 | 0.442 | 0.991 | 0.982 |
| Relevance@10 | 35.0% | 80.0% | 91.7% |
| Relevance@3 | 25.0% | 100.0% | 91.7% |

### stpo-prozess

| Metrik | openai | ours | ragie |
|--------|--------|--------|--------|
| nDCG@10 | 0.966 | 0.945 | 0.949 |
| Relevance@10 | 50.0% | 70.0% | 88.3% |
| Relevance@3 | 77.8% | 88.9% | 100.0% |

## Detail pro Query


### q01 — exakte-paragraphen

**Query:** Welche Voraussetzungen hat der gewerbsmaessige Bandenbetrug nach § 263 Abs. 5 StGB?

**Kontext:** Qualifikationstatbestand des Bandenbetrugs im Fischer-Kommentar

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours | 1.00 | 80% | 100% | 3 | 6.2s |
| ragie | 1.00 | 90% | 100% | 3 | 2.7s |
| openai | 0.79 | 20% | 33% | 1 | 2.4s |

#### ours — Top 3
- **[Judge=3]** `§ 263 StGB – BT. Zweijundzwanzigster Abschnitt – Rn. 213` — Direkte Erläuterung zu § 263 Abs. 5 StGB
  > 213 Sind beide Varianten erfüllt, ist eine Qualifikation nach Abs. 5 gegeben. Die Abgrenzung des Abs. 3 Nr. 1 zum Verbrechen nach Abs. 5 ist in Fällen bandenmäßiger Begehung schwierig, denn eine auf f...
- **[Judge=3]** `§ 263 StGB – BT. Zweriindzwanzigster Abschnitt – Rn. 225` — Direkt relevante Erklärung der Voraussetzungen § 263 Abs. 5
  > IV. Qualifikation (Abs. 5). Abs. 5 enthält einen Qualifikationstatbestand, der die Tat in Fällen kumulativ gewerbs- und bandenmäßiger Begehung zum Verbrechen macht. Die Qualifikation ist in die Urteil...
- **[Judge=3]** `§ 263 StGB – I. Vermögensbegriff  – Rn. 263` — Enthält direkt § 263 Abs. 5 mit allen Voraussetzungen
  > 263 (1) Wer in der Absicht, sich oder einem Dritten einen rechtswidrigen Vermögensvorteil zu verschaffen, das Vermögen eines anderen dadurch beschädigt, daß er durch Vorspiegelung falscher oder durch ...

#### ragie — Top 3
- **[Judge=3]** `StGB_263_Betrug.md` — Direkt relevant: Bandenbetrug Abs. 5 Qualifikation erläutert
  > StGB_263_Betrug.md 213 Sind beide Varianten erfüllt, ist eine Qualifikation nach Abs. 5 gegeben. Die Abgrenzung des Abs. 3 Nr. 1 zum Verbrechen nach Abs. 5 ist in Fällen bandenmäßiger Begehung schwier...
- **[Judge=3]** `StGB_Kommentar.md` — Direkt relevant zu Bandenbetrug Abs. 5 Voraussetzungen
  > StGB_Kommentar.md 213 Sind beide Varianten erfüllt, ist eine Qualifikation nach Abs. 5 gegeben. Die Abgrenzung des Abs. 3 Nr. 1 zum Verbrechen nach Abs. 5 ist in Fällen bandenmäßiger Begehung schwieri...
- **[Judge=3]** `StGB_263_Betrug.md` — Direkt relevant für gewerbsmäßigen Bandenbetrug § 263 Abs. 5
  > StGB_263_Betrug.md IV. Qualifikation (Abs. 5). Abs. 5 enthält einen Qualifikationstatbestand, der die Tat in Fällen kumulativ gewerbs- und bandenmäßiger Begehung zum Verbrechen macht. Die Qualifikatio...

#### openai — Top 3
- **[Judge=1]** `analyses_findings.md` — Erwähnt Bandenbetrug, aber behandelt andere Rechtsfragen
  > **Zusammenhang im Detail:**  1. **Kein Verkaufsverbot** → Die Angeklagten durften darauf vertrauen, dass ihre Produkte legal sind → **Kein Vorsatz** (§ 16 StGB) oder zumindest **Verbotsirrtum** (§ 17 ...
- **[Judge=3]** `StGB_Kommentar.md` — Direkt relevant - behandelt Bandenbetrug § 263 Abs. 5
  > 212 Der Begriff der Urkundenfälschung ist weit zu fassen; er umfasst neben Taten nach § 267 auch solche nach §§ 268–281 (LK-StGB/Kubiciel/Tiedemann Rn. 297; NK-StGB/Kindhäuser/Hoven Rn. 392). Entsprec...
- **[Judge=0]** `Probenheld-KOMPLETT.md` — Verfahrensfragen zu konkretem Fall, keine Tatbestandsmerkmale
  > Das Projekt "Probenheld" war im Partnerprogramm und wurde von VERIPAY BV in HEERLEN (NL) betrieben und hierüber wurden die Bestellungen im Rahmen des Partnerprogramms "Platinum-Partner" über mehr als ...

### q02 — exakte-paragraphen

**Query:** Was regelt § 112 StPO zur Untersuchungshaft?

**Kontext:** Anordnungsvoraussetzungen der U-Haft (dringender Tatverdacht, Haftgrund) im Schmitt/Koehler

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours | 1.00 | 100% | 100% | 3 | 4.8s |
| ragie | 0.96 | 75% | 67% | 3 | 3.7s |
| openai | 0.96 | 60% | 100% | 3 | 1.5s |

#### ours — Top 3
- **[Judge=3]** `§ 112 StPO – Rn. 112` — Direkter Gesetzestext zu § 112 StPO Untersuchungshaft
  > 112 (1) ¹ Die Untersuchungshaft darf gegen den Beschuldigten angeordnet werden, wenn er der Tat dringend verdächtig ist und ein Haftgrund besteht. ² Sie darf nicht angeordnet werden, wenn sie zu der B...
- **[Judge=3]** `§ 112 StPO – III. Flucht (Abs – Rn. 32 (Teil 2)` — Behandelt direkt Verdunkelungsgefahr als Haftgrund nach § 112 StPO
  > Wenn die Verdunkelungshandlungen nicht geeignet sind, die Ermittlung der Wahrheit zu erschweren, darf UHaft nicht angeordnet werden. Der Haftgrund liegt daher nicht vor, wenn der Sachverhalt schon in ...
- **[Judge=3]** `§ 112 StPO – Rn. 112` — Direkt relevant: erklärt Voraussetzungen § 112 StPO
  > Haftunfähigkeit des Beschuldigten schließt den Erlass des Haftbefehls nicht aus, sondern hindert nur seinen Vollzug (OLG Düsseldorf JZ 1984, 248; OLG Frankfurt a.M. NJW 1968, 2302; OLG Nürnberg OLGSt ...

#### ragie — Top 3
- **[Judge=3]** `Strafprozessordnung.md` — Direkt relevant: § 112 Anordnungsvoraussetzungen U-Haft
  > Strafprozessordnung.md Werden mehrere Haftbefehle in verschiedenen Sachen erlassen, so kann nur einer v. ihnen vollzogen werden. Eine „Doppelhaft“ ist ausgeschlossen (Münchhalffen/Gatzweiler Untersuch...
- **[Judge=3]** `Strafprozessordnung.md` — Direkt relevant: § 112 StPO Anordnungsvoraussetzungen behandelt
  > Strafprozessordnung.md a) der dringende Tatverdacht, b) der Haftgrund  ergeben.  ---  ## Seite 2435  Anh. 3 RiStBV  RL für das Strafverfahren und das Bußgeldverfahren  (2) Wenn die Anwendung des § 112...
- **[Judge=1]** `Strafprozessordnung.md` — Jugendstrafrecht, nicht allgemeine StPO-Voraussetzungen
  > Strafprozessordnung.md § 72 Untersuchungshaft. (1) ¹ Untersuchungshaft darf nur verhängt und vollstreckt werden, wenn ihr Zweck nicht durch eine vorläufige Anordnung über die Erziehung oder durch ande...

#### openai — Top 3
- **[Judge=3]** `Strafprozessordnung.md` — Direkte Regelung der Anordnungsvoraussetzungen für U-Haft
  > Schmitt  ---  ## Seite 722  StPO § 112  Erstes Buch. Neunter Abschnitt  wenn Überhaft notiert ist, weil der Beschuldigte sich noch in anderer Sache in Strafhaft befindet. Zur Haftbeschwerde bei Überha...
- **[Judge=3]** `Strafprozessordnung.md` — Behandelt direkt Haftgründe und Voraussetzungen von § 112 StPO
  > 3, Abs. 2 schließt auch aus, den auf § 112 gestützten Haftbefehl hilfsweise auf den Haftgrund der Wiederholungsgefahr zu stützen; denn auch dann handelt es sich um eine Anwendung dieses Haftgrundes (L...
- **[Judge=3]** `Strafprozessordnung.md` — Direkt relevant: Anordnungsvoraussetzungen der U-Haft nach § 112 StPO
  > # 7. Untersuchungshaft, einstweilige Unterbringung und sonstige Maßnahmen zur Sicherstellung der Strafverfolgung und der Strafvollstreckung  46. Begründung der Anträge in Haftsachen. (1) Der Staatsanw...

### q03 — exakte-paragraphen

**Query:** Welche Haftgruende nennt § 112 Abs. 2 StPO?

**Kontext:** Fluchtgefahr, Verdunkelungsgefahr, Flucht — im StPO-Kommentar

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours | 0.99 | 90% | 100% | 3 | 4.9s |
| ragie | 0.86 | 71% | 67% | 2 | 2.0s |
| openai | 0.85 | 20% | 33% | 2 | 1.7s |

#### ours — Top 3
- **[Judge=3]** `§ 112 StPO – Rn. 112` — Beantwortet direkt die Frage zu Haftgruenden
  > 112 (1) ¹ Die Untersuchungshaft darf gegen den Beschuldigten angeordnet werden, wenn er der Tat dringend verdächtig ist und ein Haftgrund besteht. ² Sie darf nicht angeordnet werden, wenn sie zu der B...
- **[Judge=3]** `§ 112 StPO – III. Flucht (Abs – Rn. 23` — Direkt relevant: behandelt Verdunkelungsgefahr § 112 Abs. 2
  > Bei einer besonders hohen Straferwartung braucht daher nur geprüft zu werden, ob Umstände vorhanden sind, die die hieraus herzuleitende Fluchtgefahr ausräumen können (KG StV 1996, 383; OLG München Str...
- **[Judge=3]** `§ 112 StPO – III. Flucht (Abs – Rn. 32 (Teil 2)` — Behandelt direkt Verdunkelungsgefahr als Haftgrund § 112 StPO
  > Wenn die Verdunkelungshandlungen nicht geeignet sind, die Ermittlung der Wahrheit zu erschweren, darf UHaft nicht angeordnet werden. Der Haftgrund liegt daher nicht vor, wenn der Sachverhalt schon in ...

#### ragie — Top 3
- **[Judge=2]** `Strafprozessordnung.md` — Behandelt Haftgründe, aber fokussiert auf Abs. 3
  > Strafprozessordnung.md 38 Die Vorschr. begründet bei dieser Auslegung weder eine Vermutung der Haftgründe (aM OLG Düsseldorf MDR 1983, 152; offenbar auch OLG Bremen StV 1983, 288), noch findet eine „U...
- **[Judge=1]** `Strafprozessordnung.md` — Erwähnt Haftgründe, aber nennt sie nicht konkret
  > Strafprozessordnung.md (3) ¹ Hinsichtlich der Möglichkeit und gegebenenfalls Pflicht zur Aufzeichnung der Vernehmung des Beschuldigten in Bild und Ton sind § 136 Absatz 4 StPO bzw. § 70c Absatz 2 Satz...
- **[Judge=2]** `Strafprozessordnung.md` — Behandelt Haftgruende allgemein, nicht spezifisch Abs. 2
  > Strafprozessordnung.md Soweit die Staatssicherheit gefährdet wurde, kann v. der Begründung des dringenden Tatverdachts abgesehen werden (dazu Creifelds NJW 1965, 949); das muss in dem Haftbefehl zum A...

#### openai — Top 3
- **[Judge=2]** `Strafprozessordnung.md` — Behandelt Haftgründe des § 112, aber nicht vollständig
  > 1 A. Einschränkung der UHaft. Eine Einschränkung der UHaft bei Straftaten mit geringer Strafandrohung bestimmt die Vorschrift. Ihr ist zu entnehmen, dass UHaft auch angeordnet werden darf, wenn nur ei...
- **[Judge=1]** `Strafprozessordnung.md` — Erwähnt Haftgründe, aber nennt sie nicht konkret
  > # 7. Untersuchungshaft, einstweilige Unterbringung und sonstige Maßnahmen zur Sicherstellung der Strafverfolgung und der Strafvollstreckung  46. Begründung der Anträge in Haftsachen. (1) Der Staatsanw...
- **[Judge=1]** `Strafprozessordnung.md` — Behandelt Sicherungshaft nach § 112a, nicht Haftgründe § 112 Abs. 2
  > (2) Absatz 1 findet keine Anwendung, wenn die Voraussetzungen für den Erlaß eines Haftbefehls nach § 112 vorliegen und die Voraussetzungen für die Aussetzung des Vollzugs des Haftbefehls nach § 116 Ab...

### q04 — exakte-paragraphen

**Query:** Was regelt § 102 StPO zur Durchsuchung beim Beschuldigten?

**Kontext:** Durchsuchungsvoraussetzungen beim Verdaechtigen

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours | 0.97 | 80% | 100% | 3 | 5.2s |
| ragie | 0.85 | 89% | 67% | 1 | 2.2s |
| openai | 0.94 | 50% | 100% | 3 | 1.7s |

#### ours — Top 3
- **[Judge=3]** `§ 102 StPO – Rn. 102` — Direkter Wortlaut und Struktur von § 102 StPO
  > 102 Bei dem, welcher als Täter oder Teilnehmer einer Straftat oder der Datenhehlerei, Begünstigung, Strafvereitelung oder Hehlerei  Köhler    Ermittlungsmaßnahmen  verdächtig ist, kann eine Durchsuchu...
- **[Judge=2]** `§ 102 StPO – Rn. 10` — Behandelt Durchsuchungsvoraussetzungen, aber nicht § 102 spezifisch
  > II. Auffinden von Beweismitteln. Zu den Beweismitteln (→ § 94 Rn. 4 ff.) gehören auch die nur in § 103 erwähnten Spuren (SK-StPO/Jäger/Wohlers Rn. 21) u. Personen, die zu Beweiszwecken in Augenschein ...
- **[Judge=3]** `§ 102 StPO – Rn. 3` — Definiert zentrale Begriffe und Durchsuchungsgegenstände § 102 StPO
  > **Teilnehmer** nach §§ 25 ff. StGB, nicht die sog. notwendigen Teilnehmer (zum Begriff: Fischer/Fischer StGB Vor § 25 Rn. 7), stehen den Tatverdächtigen gleich. Bei jedem v. ihnen sowie bei den der Be...

#### ragie — Top 3
- **[Judge=1]** `Strafprozessordnung.md` — Behandelt § 103 statt gefragten § 102 StPO
  > Strafprozessordnung.md 3 B. Durchsuchungsgegenstände. Durchsuchungsgegenstände können die Wohnung u. Räume des Unverdächtigen (→ § 102 Rn. 7) sowie seine Person (→ § 102 Rn. 9) u. die ihm gehörenden S...
- **[Judge=3]** `Strafprozessordnung.md` — Direkt relevant: Wortlaut und Struktur von § 102 StPO
  > Strafprozessordnung.md Durchsuchung bei Beschuldigten RiStBV 73a  102 Bei dem, welcher als Täter oder Teilnehmer einer Straftat oder der Datenhehlerei, Begünstigung, Strafvereitelung oder Hehlerei  Kö...
- **[Judge=2]** `Strafprozessordnung.md` — Behandelt Durchsuchung Unverdaechtiger, nicht Beschuldigter direkt
  > Strafprozessordnung.md 2 Auch Dienstgebäude u. -räume v. Behörden dürfen nur durchsucht werden (vgl. § 105 Abs. 3 S. 3), wenn dies erforderlich, um den Beschuldigten zu ergreifen oder Beweismittel auf...

#### openai — Top 3
- **[Judge=3]** `Strafprozessordnung.md` — Direkter Paragraph 102 StPO zur Durchsuchung beim Beschuldigten
  > 3 C. Inhalt. Der Inhalt der Berichte ist für die einzelnen Maßnahmen in Abs. 2 jew. iE vorgeschrieben worden (Abs. 2 für § 100a, Abs. 3 für § 100b, Abs. 4 für § 100c und Abs. 5 für § 100g sowie Abs. 6...
- **[Judge=2]** `Strafprozessordnung.md` — Behandelt Durchsuchung, aber speziell § 103 StPO
  > 14 III. Durchsuchungszweck. Durchsuchungszweck darf nur die Ergreifung des Beschuldigten sein, nicht die Auffindung v. Spuren u. Beweismitteln. Werben für eine terroristische Vereinigung o. deren geri...
- **[Judge=2]** `Strafprozessordnung.md` — Behandelt § 103 StPO, nicht direkt § 102
  > Rn. 76). Wie im Fall des § 102 (→ § 102 Rn. 12) steht dem Beschuldigten der rkr. Verurteilte gleich. Anders als dort (→ § 102 Rn. 2) ist die Durchsuchung aber nur zulässig, wenn aus aufgrund Zeugenbek...

### q05 — konzept

**Query:** Wann liegt eine konkludente Taeuschung im Sinne des § 263 StGB vor?

**Kontext:** Taeuschungshandlung durch schluessiges Verhalten

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours | 0.99 | 100% | 100% | 3 | 5.7s |
| ragie | 0.95 | 89% | 67% | 3 | 3.0s |
| openai | 0.94 | 80% | 67% | 3 | 1.7s |

#### ours — Top 3
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 14` — Behandelt direkt konkludente Täuschung bei § 263
  > Rspr. und hM bejahen darüber hinaus aber die Möglichkeit einer Täuschung durch Unterlassen auch ohne Erklärung gegenüber dem Irrenden (→ Rn. 38; vgl. BGHSt 39, 392 (398); BayObLG NJW 1987, 1654 (mAnm ...
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 21` — Direkt relevant: erklärt konkludente Täuschung bei § 263
  > 21 2. Konkludente Erklärungen. Auch durch eine schlüssige Handlung (konkludente Erklärung) kann vorspiegelt werden. Eine solche konkludente Erklärung durch aktives Tun ist von einer Erklärung durch Un...
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 14` — Erklaert konkludente Taeusching direkt und praezise
  > 14 II. Tathandlung. Der Begriff „Täuschen“ ist im Wortlaut des Abs. 1 nicht verwendet; er ergibt sich aus dem Zusammenhang zwischen der Beschreibung der Tathandlung (→ Rn. 18) und dem Irrtum als ihrem...

#### ragie — Top 3
- **[Judge=3]** `StGB_263_Betrug.md` — Beantwortet direkt konkludente Taeuschung bei § 263
  > StGB_263_Betrug.md 21 2. Konkludente Erklärungen. Auch durch eine schlüssige Handlung (konkludente Erklärung) kann vorspiegelt werden. Eine solche konkludente Erklärung durch aktives Tun ist von einer...
- **[Judge=1]** `StGB_Kommentar.md` — Behandelt Scheckkarten-Missbrauch, nicht allgemeine konkludente Taeuschung
  > StGB_Kommentar.md E. Vollendung, Versuch. Die Tat ist mit dem Eintritt des Schadens vollendet und idR auch beendet iSv § 78a. Der Versuch ist nicht strafbar. Die (vom Gesetzgeber des 2. WiKG verworfen...
- **[Judge=3]** `StGB_263_Betrug.md` — Behandelt direkt konkludente Täuschung bei § 263
  > StGB_263_Betrug.md 22 Sowohl ausdrücklichen Erklärungen als auch tatsächlichen Handeln kann ein konkludenter Erklärungswert zukommen. Aus der bloßen Feststellung eines Irrtums kann aber nicht schon au...

#### openai — Top 3
- **[Judge=3]** `StGB_Kommentar.md` — Behandelt direkt konkludente Taeuschung bei § 263
  > Es kann im Einzelfall auch mit Aussagen zu wahren Tatsachen (nicht: über solche) getäuscht werden, wenn der Täter es darauf anlegt, gerade hierdurch Missverständnis und Irrtum hinsichtl. anderer Tatsa...
- **[Judge=2]** `StGB_Kommentar.md` — Behandelt konkludente Täuschung bei § 263, aber spezifisch Kartenmissbrauch
  > F. Täterschaft und Teilnahme. Die Tat ist ein Sonderdelikt (BT-Drs. 10/5058, 32; NStZ 1992, 279; OLG Stuttgart NJW 1988, 981 (981 f.)); für Teilnehmer gilt § 28 Abs. 1 (hM; aA TK-StGB/Perron Rn. 13). ...
- **[Judge=1]** `StGB_Kommentar.md` — Behandelt Kartenmissbrauch, nicht allgemeine konkludente Taeuschung
  > Ein Irrtum wird sich – trotz der verbreiteten Praxis von Banken, Überziehungen weit über einen alsbald rückführbaren Rahmen hinaus zu dulden und den Kontoausgleich durch Ratenkreditverträge anzubieten...

### q06 — konzept

**Query:** Was ist eine Vermoegensverfuegung und welche Anforderungen stellt die Rechtsprechung?

**Kontext:** Tatbestandsmerkmal der Vermoegensverfuegung beim Betrug

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours | 0.99 | 50% | 100% | 3 | 6.2s |
| ragie | 1.00 | 100% | 100% | 3 | 2.2s |
| openai | 0.00 | 0% | 0% | 0 | 1.6s |

#### ours — Top 3
- **[Judge=3]** `§ 263 StGB – BT. Zweitundzwanzigster Abschnitt – Rn. 69` — Definiert Vermoegensverfuegung und deren rechtliche Anforderungen direkt
  > 69 Anders ist es, wenn der Verfügende seinerseits nur (gutgläubige) Hilfsperson eines bösgläubigen Dritten ist. Hier ist auf den Irrtum des Entscheidungsbefugten abzustellen: Erkennt dieser die Unrich...
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 76` — Definiert Unmittelbarkeit als zentrales Kriterium der Vermoegensverfuegung
  > 76 3. Unmittelbarkeit der Verfügung. Neben der Freiwilligkeit ist das Merkmal der Unmittelbarkeit nach stRspr und hM das wichtigste Kriterium zur Beschränkung der § 263 unterfallenden Selbstschädigung...
- **[Judge=2]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 87` — Behandelt Kausalität bei Vermögensverfügung, nicht Definition
  > 87 5. Kausalität. Für die Vermögensverfügung muss der täuschungsbedingte Irrtum kausal sein (vgl. BGHSt 24, 257 (260); 24, 386 (389); NStZ 2003, 313 (314 f.); OLG Düsseldorf NJW 1987, 3145); Mitverurs...

#### ragie — Top 3
- **[Judge=3]** `StGB_Kommentar.md` — Definiert Vermoegensverfuegung mit konkreten Rechtsprechungsbeispielen
  > StGB_Kommentar.md a) Einzelfälle. Als Verfügungen sind zB angesehen worden: Veranlassung oder Vornahme einer Überweisung (wistra 1987, 257; NStZ 1999, 558); Herausgabe fremder Sachen: Bewilligung von ...
- **[Judge=3]** `StGB_Kommentar.md` — Direkt relevant: Definition und Rechtsprechung zu Vermoegensverfuegung
  > StGB_Kommentar.md 1. Verfügungshandlung. Die Anzahl möglicher vermögensmindernder Handlungen ist grds. unbeschränkt; sie sind meist den Fallgruppen des Eingehens oder des Erfüllens einer Verbindlichke...
- **[Judge=2]** `StGB_Kommentar.md` — Behandelt Vermögensschaden, nicht Vermögensverfügung direkt
  > StGB_Kommentar.md 113 2. Vermögensminderung. Erforderlich ist eine durch die Vermögensverfügung kausal verursachte Minderung des Vermögenswerts durch den Verlust oder die Wertminderung von Aktiva oder...

#### openai — Top 3
- **[Judge=0]** `StGB_Kommentar.md` — Behandelt psychische Störungen, nicht Vermögensverfügung
  > (77); 49, 45 (53); NStZ-RR 2010, 73; 2023, 72 stRspr). Auf die Rechtsfrage, ob eine (festgestellte; vgl. → § 20 Rn. 44a) Störung erheblich ist, ist daher auch der Zweifelssatz im Grundsatz nicht anwen...
- **[Judge=0]** `StGB_Kommentar.md` — Behandelt Schuldunfaehigkeit, nicht Vermoegensverfuegung beim Betrug
  > 9; → § 20 Rn. 46b). Dabei ist die Beziehung zwischen Entstehungsgeschichte, Motivation und Verlauf der Tat und den konkreten Auswirkungen der psychischen Störung zu betrachten; einzubeziehen ist auch ...
- **[Judge=0]** `StGB_Kommentar.md` — Behandelt Sexualstraftaten, nicht Betrug oder Vermögensverfügung
  > Nicht vorausgesetzt ist auch, dass die Sexualstraftat gerade gegen diejenige Person begangen wird, die von der Gruppe „bedrängt“ wird. Vielmehr ist auch die Möglichkeit umfasst, dass die Tat nach § 17...

### q07 — konzept

**Query:** Was versteht man unter einem Gefaehrdungsschaden beim Betrug?

**Kontext:** Schadensbegriff, schadensgleiche Vermoegensgefaehrdung

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours | 1.00 | 100% | 100% | 3 | 6.1s |
| ragie | 1.00 | 100% | 100% | 3 | 2.0s |
| openai | 0.00 | 0% | 0% | 0 | 1.6s |

#### ours — Top 3
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 159` — Definiert direkt Gefährdungsschaden beim Betrug
  > 159 b) Voraussetzungen. aa) Ein Gefährdungsschaden ist gegeben, wenn die Wahrscheinlichkeit des endgültigen Verlusts eines Vermögensbestandteils zum Zeitpunkt der täuschungsbedingten Verfügung so groß...
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 109` — Definiert direkt den Gefährdungsschaden beim Betrug
  > VI. Schaden. Vermögensschaden ist ein negativer Saldo zwischen dem Wert des Vermögens vor und nach der irrtumsbedingten Vermögensverfügung des Getäuschten (Prinzip der Gesamtsaldierung; stRspr; vgl. B...
- **[Judge=3]** `§ 263 StGB – BT. Zwei undzwanzigster Abschnitt – Rn. 263 (Te` — Direkt relevant - Literaturverzeichnis zu Gefährdungsschäden
  > Fischer/Lutz    Betrug und Untreue   rechts für das Strafrecht, FS Weber, 2004, 271; Eisele/Bechtel, Der Schadensbegriff bei den Vermögensdelikten, JuS 2018, 97; Ellbogen/Wichmann, Zu Problemen des är...

#### ragie — Top 3
- **[Judge=3]** `StGB_263_Betrug.md` — Definiert direkt Gefaehrdungsschaden beim Betrug
  > StGB_263_Betrug.md 159 b) Voraussetzungen. aa) Ein Gefährdungsschaden ist gegeben, wenn die Wahrscheinlichkeit des endgültigen Verlusts eines Vermögensbestandteils zum Zeitpunkt der täuschungsbedingte...
- **[Judge=3]** `StGB_263_Betrug.md` — Direkte Definition und Voraussetzungen des Gefährdungsschadens
  > StGB_263_Betrug.md 158 Der 3. StS hat in BGHSt 54, 69 (122 ff.) (Anm. Joecks wistra 2010, 179; vgl. → Rn. 8; → Rn. 176) sowohl der Sache nach als auch begrifflich am „Gefährdungsschaden“ festgehalten ...
- **[Judge=3]** `StGB_Kommentar.md` — Definiert direkt Gefährdungsschaden beim Betrug mit Beispielen
  > StGB_Kommentar.md Die täuschungsbedingte Herausgabe von EC-Karten, Kreditkarten und weiteren Zugangsdaten zu Bank-Guthaben (PINs, TANs; Passwörter), sei es infolge persönlicher Täuschung oder von „Phi...

#### openai — Top 3
- **[Judge=0]** `StGB_Kommentar.md` — Behandelt Täterschaft/Teilnahme, nicht Betrugsschaden oder Gefährdungsschaden
  > Die Abgrenzung hängt nach der Rspr. davon ab, ob das betreffende Merkmal im Schwergewicht die Tat oder die Persönlichkeit des Täters kennzeichnet. Umstände, die eine besondere Gefährlichkeit des Täter...
- **[Judge=0]** `StGB_Kommentar.md` — Betrifft Schuldunfaehigkeit, nicht Betrug oder Vermoegensgefaehrdung
  > 29 f.). Die als Kriterien eines Vorverschuldens herangezogenen Umstände sind durchweg solche, die in anderem Gewand schon auf der tatsächlichen Ebene gegen die Feststellung einer („tiefgreifenden“) Be...
- **[Judge=0]** `Probenheld-KOMPLETT.md` — Polizeianzeigen, nicht Gefaehrdungsschaden-Definition
  > Ich bin allerdings letztes Jahr mal angerufen worden. Wie diese Firma hieß, weiß ich nicht. Da hat man mir eine Mastercard in Verbindung mit einem Sofortkredit angeboten. Ich habe da aber ausdrücklich...

### q08 — konzept

**Query:** Wie wird der Vorsatz beim Betrug bestimmt, insbesondere die Bereicherungsabsicht?

**Kontext:** Subjektiver Tatbestand § 263 StGB

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours | 0.99 | 70% | 100% | 3 | 5.3s |
| ragie | 0.98 | 78% | 100% | 3 | 1.7s |
| openai | 0.83 | 60% | 33% | 1 | 1.7s |

#### ours — Top 3
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 176` — Direkt relevant: Vorsatz und Bereicherungsabsicht beim Betrug
  > D. Subjektiver Tatbestand. § 263 setzt Vorsatz voraus; darüber hinaus ist die Absicht rechtswidriger Bereicherung erforderlich.   I. Vorsatz. 1. Täuschungsvorsatz. Der Vorsatz (bedingter Vorsatz genüg...
- **[Judge=3]** `§ 263 StGB – I. Sonstige Vorschriften 239 – Rn. 263 (Teil 1)` — Direkt relevant: Bereicherungsabsicht und Vorsatz beim Betrug
  > 3. Einzelne Fallgruppen ... 92 4. Rechtlich missbilligte, sittenwidrige und gesetzeswidrige wirtschaftliche Werte ... 101 VI. Schaden ... 110 1. Grundsätze der Schadensermittlung ... 111 2. Vermögensm...
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 186` — Definiert direkt Bereicherungsabsicht bei § 263 StGB
  > 186 II. Bereicherungsabsicht. Die Tat muss subjektiv auf die Erlangung eines rechtswidrigen Vermögensvorteils für den Täuschenden oder einen Dritten gerichtet sein. Vermögensvorteil ist die Erhöhung d...

#### ragie — Top 3
- **[Judge=3]** `StGB_263_Betrug.md` — Direkt relevant: Bereicherungsabsicht und Vorsatz beim Betrug
  > StGB_263_Betrug.md 186 II. Bereicherungsabsicht. Die Tat muss subjektiv auf die Erlangung eines rechtswidrigen Vermögensvorteils für den Täuschenden oder einen Dritten gerichtet sein. Vermögensvorteil...
- **[Judge=3]** `StGB_263_Betrug.md` — Direkt zur Bereicherungsabsicht und deren Bestimmung
  > StGB_263_Betrug.md 183–185 Diese Rspr. setzt einerseits konkrete Gefährdung und (endgültigen) Schadens- erfolg gleich (vgl. BGHSt 48, 331 (347)); andererseits sieht sie die Kenntnis der Gefahr nur als...
- **[Judge=2]** `StGB_Kommentar.md` — Behandelt Bereicherungsabsicht als ueberschießende Innentendenz, aber nicht spezifisch
  > StGB_Kommentar.md II. Tatbestandsmerkmale unechten Unterlassens. Für unechte Unterlassungsdelikte hat der GrSen (BGHSt 16, 155) entschieden, dass nur die Umstände, welche die Rechtspflicht begründen (...

#### openai — Top 3
- **[Judge=1]** `StGB_Kommentar.md` — Erpressung § 253, nicht Betrug § 263
  > 36 I. Vorsatz. Für die Nötigung gilt das in → § 240 Rn. 53 ff. Gesagte, auch bezüglich der Kenntnis der Empfindlichkeit des Übels und der Rechtswidrigkeit der Tat.  37 II. Bereicherungsabsicht. Der Tä...
- **[Judge=3]** `StGB_Kommentar.md` — Behandelt direkt Bereicherungsabsicht bei Vorsatz § 263
  > Erforderlich ist weiterhin der Vorsatz, eine der Tathandlungen (→ Rn. 9 ff.) zu begehen und dadurch die rechtswidrige Vermögenslage aufrechtzuerhalten. Auch insoweit reicht bedingter Vorsatz aus. Nimm...
- **[Judge=1]** `StGB_Kommentar.md` — Raub-Kommentar, nicht Betrug-spezifisch zur Bereicherungsabsicht
  > G. Subjektiver Tatbestand. Der Vorsatz muss entsprechend der Doppelnatur des Raubs sowohl Wegnahme (vgl. dazu → § 242 Rn. 29 ff.) als auch Nötigung (→ § 240 Rn. 53 f.) sowie deren Verknüpfung umfassen...

### q09 — alltagssprache

**Query:** Hat der Angeklagte die Kunden über das Internet betrogen?

**Kontext:** Abstrakte Frage zu Internetbetrug, sucht Taeuschungshandlung + Schaden

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours | 0.93 | 100% | 100% | 2 | 5.7s |
| ragie | 0.99 | 100% | 100% | 3 | 1.8s |
| openai | 0.98 | 80% | 100% | 3 | 1.8s |

#### ours — Top 3
- **[Judge=2]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 263 (Tei` — Literaturverzeichnis zu Betrug, thematisch relevant aber nicht konkret
  > Heghmanns, Strafbarkeit des „Phishing“ von Bankkontendaten und ihrer Verwertung, wistra 2007, 167; Hilgendorf, Tatsachenaussagen u. Werturteile im Strafrecht, 1998; Hillenkamp, Zum Schutz „deliktische...
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 62` — Direkt relevant: Betrug Täuschung Irrtum Kausalität
  > Die Kausalität der Täuschung für den Irrtum und dessen Kausalität für die Vermögensverfügung müssen im Einzelfall festgestellt sein. Mitverursachung reicht aus. Dabei darf das Gericht auch bei Serien-...
- **[Judge=2]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 263 (Tei` — Thematisch relevant: Betrug, Internet-Kostenfallen, Täuschungsformen
  > Fischer/Lutz      BT. Zweiundzwanzigster Abschnitt. Fehlvorstellung beim Betrug, GA 2012, 354; Cornelius, Betrug durch verschleierte Kick-Back-Zahlungen bei Immobilienfinanzierungen?, NZWiSt 2012, 259...

#### ragie — Top 3
- **[Judge=3]** `StGB_263_Betrug.md` — Direkt relevant zu Internetbetrug mit Taeuschungshandlungen
  > StGB_263_Betrug.md Entsprechendes gilt auch für sog. Abofallen im Internet (dazu NJW 2014, 2595; Routenplaner). Dies sind scheinbar unentgeltliche Informationsangebote (Wetterberichte; Routenplaner; B...
- **[Judge=3]** `StGB_263_Betrug.md` — Direkt relevant - behandelt Internetbetrug und Täuschungshandlungen
  > StGB_263_Betrug.md In Fällen sog. „Kostenfallen“ im Internet (vgl. dazu Eisele NStZ 2010, 193), bei denen unerfahrene Verbraucher durch (wahre) Versprechen besonders günstiger Angebote zum Abschluss v...
- **[Judge=2]** `StGB_263_Betrug.md` — Thematisch relevant, behandelt Internetbetrug und Täuschungshandlungen
  > StGB_263_Betrug.md Fehlvorstellung beim Betrug, GA 2012, 354; Cornelius, Betrug durch verschleierte Kick-Back-Zahlungen bei Immobilienfinanzierungen?, NZWiSt 2012, 259; Cramer, Zur Strafbarkeit von Pr...

#### openai — Top 3
- **[Judge=3]** `Probenheld-KOMPLETT.md` — Direkt relevant: Internetbetrug mit Täuschung und Kundenschäden
  > ## 3. Zusammenhänge  Aufgrund der IP-Adressen der Webseiten, des Registranten der Webseiten, der Hoster, der Anschriften und der Hotlines scheinen hier alle Firmen im Zusammenhang zustehen.  Die zentr...
- **[Judge=2]** `Probenheld-KOMPLETT.md` — Internetbetrug-Ermittlungen, Domain-Abfrage und Täuschungsvorwurf relevant
  > Polizeiinspektion Salzgitter, 19.07.2018  KRUCK, Polizeioberkommissar  ## Antwort DENIC Domainauskunft Slimsticks.de - 19. Juli 2018  **Von:** DENIC Whois <noreply@denic.de> **An:** Kruck, Detlef (PI ...
- **[Judge=3]** `Probenheld-KOMPLETT.md` — Konkreter Internetbetrugsfall mit Taeuschungshandlung dokumentiert
  > Aktuell informiert uns ein Nichtkunde unserer Sparkasse mit dem im Anhang beigefügten E-Mail-Verkehr, dass er sich durch die Firma Payplus GmbH betrogen fühle. Darüber hinaus liegen uns zwischenzeitli...

### q10 — alltagssprache

**Query:** Wann darf die Polizei bei jemandem zu Hause suchen?

**Kontext:** Durchsuchungsvoraussetzungen, §§ 102 ff. StPO

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours | 0.99 | 70% | 100% | 3 | 5.0s |
| ragie | 0.95 | 83% | 67% | 3 | 2.2s |
| openai | 0.33 | 0% | 0% | 0 | 1.6s |

#### ours — Top 3
- **[Judge=3]** `§ 102 StPO – Rn. 102` — Direkt relevant: Durchsuchung Wohnung/Räume, Voraussetzungen § 102
  > 102 Bei dem, welcher als Täter oder Teilnehmer einer Straftat oder der Datenhehlerei, Begünstigung, Strafvereitelung oder Hehlerei  Köhler    Ermittlungsmaßnahmen  verdächtig ist, kann eine Durchsuchu...
- **[Judge=3]** `§ 102 StPO – Rn. 10` — Direkt relevant zu Durchsuchungsvoraussetzungen und Verhältnismäßigkeit
  > II. Auffinden von Beweismitteln. Zu den Beweismitteln (→ § 94 Rn. 4 ff.) gehören auch die nur in § 103 erwähnten Spuren (SK-StPO/Jäger/Wohlers Rn. 21) u. Personen, die zu Beweiszwecken in Augenschein ...
- **[Judge=3]** `§ 102 StPO – Rn. 3` — Direkt relevant: Durchsuchung Wohnungen und Räume
  > **Teilnehmer** nach §§ 25 ff. StGB, nicht die sog. notwendigen Teilnehmer (zum Begriff: Fischer/Fischer StGB Vor § 25 Rn. 7), stehen den Tatverdächtigen gleich. Bei jedem v. ihnen sowie bei den der Be...

#### ragie — Top 3
- **[Judge=3]** `Strafprozessordnung.md` — Direkt relevant: Durchsuchungsvoraussetzungen bei Wohnungen und Räumen
  > Strafprozessordnung.md 102 Bei dem, welcher als Täter oder Teilnehmer einer Straftat oder der Datenhehlerei, Begünstigung, Strafvereitelung oder Hehlerei  Köhler  ---  ## Seite 613  Ermittlungsmaßnahm...
- **[Judge=3]** `Strafprozessordnung.md` — Direkt relevant: Durchsuchungsvoraussetzungen und Nachtzeit-Regelungen
  > Strafprozessordnung.md 15 E. Raumdurchsuchung bei Ergreifung oder Verfolgung des Beschuldigten (Abs. 2). Wird der Beschuldigte, auch der aus der Strafhaft entflohene Verurteilte (BayObLGSt 2020, 152),...
- **[Judge=0]** `Strafprozessordnung.md` — Behandelt Zeugenbeweis in Hauptverhandlung, nicht Durchsuchungsrecht
  > Strafprozessordnung.md Schmitt  ---  ## Seite 917  Hauptverhandlung § 252 StPO  der Wohnungstür geklingelt hat, ihr Mann sei nicht zu Hause (OLG Stuttgart Justiz 1972, 322), nicht aber die Angabe, er ...

#### openai — Top 3
- **[Judge=0]** `Strafprozessordnung.md` — Zeugnisverweigerungsrecht, nicht Durchsuchung
  > 26 H. Belehrung (Abs. 3 S. 1). Die Belehrung (Abs. 3 S. 1) muss in allen Fällen, nicht nur in denen des Abs. 2, dem Zeugen eine genügende Vorstellung v. der Bedeutung des Zeugnisverweigerungsrechts zu...
- **[Judge=0]** `StGB_Kommentar.md` — Behandelt § 145d StGB, nicht Durchsuchungsrecht StPO
  > Fischer  ---  ## Seite 1190  Straftaten gegen die öffentliche Ordnung  § 145d  auf einen anderen lenkt, für den die Handlung nicht strafbar wäre (BGHSt 19, 305; OLG Köln NJW 1953, 596; OLG Hamm NJW 19...
- **[Judge=0]** `Probenheld-KOMPLETT.md` — Betrifft Kontenauskunft, nicht Wohnungsdurchsuchung
  > **Ermittlungsverfahren gegen Eduard Müller, wegen Betruges** **hier: Auskunft über IBAN: DE40 110101002679195112** **für den Zeitraum vom 01.01.2019 bis 25.03.2019**  Sehr geehrte Damen und Herren, in...

### q11 — alltagssprache

**Query:** Was passiert wenn jemand luegt damit er Geld bekommt?

**Kontext:** Laienhafte Umschreibung des Betrugstatbestandes

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours | 1.00 | 100% | 100% | 3 | 5.8s |
| ragie | 1.00 | 83% | 100% | 3 | 2.4s |
| openai | 0.84 | 20% | 33% | 3 | 1.9s |

#### ours — Top 3
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 5` — Definiert direkt Betrugstatbestand mit Täuschen für Vermögensvorteil
  > 5 C. Grundtatbestand, Abs. 1. Tathandlung ist das Täuschen einer natürlichen Person (vgl. NStZ 2005, 213) über Tatsachen. Erfolg dieser Handlung muss ein Irrtum des Täuschungsadressaten sein; dieser m...
- **[Judge=3]** `§ 263 StGB – I. Vermögensbegriff  – Rn. 263` — Direkt relevanter Betrugstatbestand mit allen Tatbestandsmerkmalen
  > 263 (1) Wer in der Absicht, sich oder einem Dritten einen rechtswidrigen Vermögensvorteil zu verschaffen, das Vermögen eines anderen dadurch beschädigt, daß er durch Vorspiegelung falscher oder durch ...
- **[Judge=3]** `§ 263 StGB – BT. Zweitundzwanzigster Abschnitt – Rn. 69` — Direkter Bezug zu Betrug und Vermögensverfügung
  > 69 Anders ist es, wenn der Verfügende seinerseits nur (gutgläubige) Hilfsperson eines bösgläubigen Dritten ist. Hier ist auf den Irrtum des Entscheidungsbefugten abzustellen: Erkennt dieser die Unrich...

#### ragie — Top 3
- **[Judge=3]** `StGB_263_Betrug.md` — Betrug direkt erklärt: lügen für Gelderlangung
  > StGB_263_Betrug.md Schwieriger ist die Abgrenzung bei zeitlich gestrecktem Fälligkeitstermin 34 (Mietzins; Ratenzahlungsverpflichtung; Arbeitsentgelt); auch hinsichtlich der Anforderungen an die konkl...
- **[Judge=3]** `StGB_263_Betrug.md` — Direkt relevant - Betrugstatbestand durch Täuschung zur Gelderlangung
  > StGB_263_Betrug.md durch Verschweigen von Vermögensdelikten eines Bauleiters; zw.); NJW 1978, 2042 (Vermögensdelikt bei Einkäufer)). Bei Täuschung über eine frühere MfS-Mitarbeit war ein Schaden nur g...
- **[Judge=3]** `StGB_263_Betrug.md` — Direkt relevant, zentrale Betrugstatbestände vollstaendig enthalten
  > StGB_263_Betrug.md Betrug  RiStBV 236–238  263 (1) Wer in der Absicht, sich oder einem Dritten einen rechtswidrigen Vermögensvorteil zu verschaffen, das Vermögen eines anderen dadurch beschädigt, daß ...

#### openai — Top 3
- **[Judge=3]** `Probenheld-KOMPLETT.md` — Direkter Betrugsfall mit Täuschung zur Gelderlangung
  > Durch einen Bekannten bekommt der GS nun den Hinweis, dass es sich um eine Betrugsmasche handelt, bei der lediglich weitere Papiere per Nachnahme zugesandt werden, man am Ende noch einige hundert Euro...
- **[Judge=0]** `analyses_findings.md` — Zivilrechtliche Vertragsstreitigkeiten, nicht Betrugstatbestand
  > ### 107Js198620 d (107Js198620 d.md) - Seitenbesuch: Seitenkontakt geschildert | Z.995: Er gab an, dass er im Internet auf eine Werbung geklickt hatte, bei der ihm versprochen wurde, dass er 7000 € be...
- **[Judge=0]** `Probenheld-KOMPLETT.md` — Forumsbeiträge zu Internetbetrug, nicht Betrugstatbestand
  > ### Anonymous 26. JANUAR 2019 UM 19:13  Genau das habe ich auch bekommen.Erst Master Card und dann Seitensprung. Ich habe auch nichts bestellt. Jetzt übergebe ich das einem Anwalt. Was habt ihr gemach...

### q12 — alltagssprache

**Query:** Wann muss jemand ins Gefaengnis waehrend die Tat noch nicht bewiesen ist?

**Kontext:** Untersuchungshaft, §§ 112 ff. StPO

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours | 0.99 | 100% | 100% | 3 | 6.2s |
| ragie | 0.86 | 56% | 67% | 3 | 2.0s |
| openai | 0.00 | 0% | 0% | 0 | 1.5s |

#### ours — Top 3
- **[Judge=3]** `§ 112 StPO – Rn. 112` — Beantwortet direkt die Frage nach Untersuchungshaft-Voraussetzungen
  > 112 (1) ¹ Die Untersuchungshaft darf gegen den Beschuldigten angeordnet werden, wenn er der Tat dringend verdächtig ist und ein Haftgrund besteht. ² Sie darf nicht angeordnet werden, wenn sie zu der B...
- **[Judge=3]** `§ 112 StPO – III. Flucht (Abs – Rn. 23` — Direkt relevant: Haftgruende bei unbewie­sener Tat
  > Bei einer besonders hohen Straferwartung braucht daher nur geprüft zu werden, ob Umstände vorhanden sind, die die hieraus herzuleitende Fluchtgefahr ausräumen können (KG StV 1996, 383; OLG München Str...
- **[Judge=3]** `§ 112 StPO – Rn. 112` — Definiert dringenden Tatverdacht für Untersuchungshaft-Voraussetzungen
  > Haftunfähigkeit des Beschuldigten schließt den Erlass des Haftbefehls nicht aus, sondern hindert nur seinen Vollzug (OLG Düsseldorf JZ 1984, 248; OLG Frankfurt a.M. NJW 1968, 2302; OLG Nürnberg OLGSt ...

#### ragie — Top 3
- **[Judge=3]** `Strafprozessordnung.md` — Direkt relevant: behandelt Untersuchungshaft vor Verurteilung
  > Strafprozessordnung.md A. UHaft. Die UHaft nach §§ 112 ff., §§ 72, 72a JGG, dh die Inhaftierung eines noch nicht (o. noch nkr) verurteilten Beschuldigten, lässt sich mit der Unschuldsvermutung des Art...
- **[Judge=0]** `StGB_Kommentar.md` — Behandelt Vollstreckungsvereitelung, nicht Untersuchungshaft
  > StGB_Kommentar.md Fischer/Lutz  1941  ---  ## Seite 682  § 258  BT. Einundzwanzigster Abschnitt.  über für die Bewertung maßgebliche Umstände bewusst unterdrückt oder verschweigt. Dasselbe gilt entspr...
- **[Judge=3]** `Strafprozessordnung.md` — Direkt relevant zu Untersuchungshaft und Haftgruenden
  > Strafprozessordnung.md 2 Freiheitsstrafe iSv Abs. 1 ist auch der Strafarrest nach § 9 WStG, nicht aber der Jugendarrest nach § 16 JGG (Löwe/Rosenberg/Hilger Rn. 3), auch wenn dieser neben Jugendstrafe...

#### openai — Top 3
- **[Judge=0]** `Strafprozessordnung.md` — Behandelt Tatmehrheit/Freispruch, nicht Untersuchungshaft
  > Tatmehrheit: Wird nicht wegen aller Delikte verurteilt, die nach der Anklage in Tatmehrheit (§ 53 StGB) begangen worden sein sollen, so muss insoweit freigesprochen werden (BGH NStZ-RR 2008, 287 mwN; ...
- **[Judge=0]** `StGB_Kommentar.md` — Vollstreckungsvereitelung, nicht Untersuchungshaft
  > 29 D. Vollstreckungsvereitelung (Abs. 2). Voraussetzung der Vollstreckungsvereitelung ist, dass eine gegen eine andere Person rechtskräftig (§ 449 StPO) verhängte Strafe (→ Rn. 5f.) oder Maßnahme (→ R...
- **[Judge=0]** `Strafprozessordnung.md` — Behandelt Beweisverwertung, nicht Untersuchungshaft
  > Der Verwertung steht auch nicht entgegen, wenn sich wegen einer **Änderung der rechtlichen Beurteilung** der Tat während des Verfahrens diese sich im Urteilszeitpunkt aus tatsächlichen oder rechtliche...

### q13 — stpo-prozess

**Query:** Welche Voraussetzungen hat die Untersuchungshaft wegen Fluchtgefahr?

**Kontext:** § 112 Abs. 2 Nr. 2 StPO Fluchtgefahr

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours | 0.94 | 70% | 67% | 3 | 4.8s |
| ragie | 0.93 | 90% | 100% | 2 | 1.8s |
| openai | 0.92 | 90% | 100% | 2 | 1.6s |

#### ours — Top 3
- **[Judge=3]** `§ 112 StPO – Rn. 112` — Enthält zentrale Tatbestandsmerkmale der Fluchtgefahr
  > 112 (1) ¹ Die Untersuchungshaft darf gegen den Beschuldigten angeordnet werden, wenn er der Tat dringend verdächtig ist und ein Haftgrund besteht. ² Sie darf nicht angeordnet werden, wenn sie zu der B...
- **[Judge=1]** `§ 112 StPO – Rn. 112` — Allgemeine Haftvoraussetzungen, nicht spezifisch Fluchtgefahr
  > Haftunfähigkeit des Beschuldigten schließt den Erlass des Haftbefehls nicht aus, sondern hindert nur seinen Vollzug (OLG Düsseldorf JZ 1984, 248; OLG Frankfurt a.M. NJW 1968, 2302; OLG Nürnberg OLGSt ...
- **[Judge=3]** `§ 112 StPO – III. Flucht (Abs – Rn. 16` — Direkt relevant zu Fluchtgefahr-Voraussetzungen nach § 112 Abs. 2 Nr. 2
  > 16 Bei Ergreifung des Beschuldigten aufgrund des nach Abs. 2 Nr. 1 erlassenen Haftbefehls entfällt der Haftgrund der Flucht. In der Regel wird die vorherige Flucht aber die Aufrechterhaltung des Haftb...

#### ragie — Top 3
- **[Judge=2]** `Strafprozessordnung.md` — Behandelt Fluchtgefahr, aber bei leichteren Taten
  > Strafprozessordnung.md ## Untersuchungshaft bei leichteren Taten  113 (1) Ist die Tat nur mit Freiheitsstrafe bis zu sechs Monaten oder mit Geldstrafe bis zu einhundertachtzig Tagessätzen bedroht, so ...
- **[Judge=3]** `Strafprozessordnung.md` — Beantwortet direkt Fluchtgefahr-Voraussetzungen nach § 112
  > Strafprozessordnung.md Fluchtgefahr begründen idR auffälliger Wohnungs- o. Arbeitsplatzwechsel, Verwendung falscher Namen o. Papiere, Flucht in einem früheren Verf. o. Verfahrensabschnitt u. Zugehörig...
- **[Judge=3]** `Strafprozessordnung.md` — Direkt relevant: Fluchtgefahr EU-Ausländer, Bindungen, Umstände
  > Strafprozessordnung.md Schmitt  ---  ## Seite 728  StPO § 112  Erstes Buch. Neunter Abschnitt  Böhm NStZ 2001, 635). Die realistische Möglichkeit einer Unterbringung nach § 63 StGB kann die Annahme v....

#### openai — Top 3
- **[Judge=2]** `Strafprozessordnung.md` — Behandelt § 113 StPO, nicht § 112 Fluchtgefahr
  > 3, Abs. 2 schließt auch aus, den auf § 112 gestützten Haftbefehl hilfsweise auf den Haftgrund der Wiederholungsgefahr zu stützen; denn auch dann handelt es sich um eine Anwendung dieses Haftgrundes (L...
- **[Judge=3]** `Strafprozessordnung.md` — Direkter Gesetzestext zu Fluchtgefahr-Voraussetzungen
  > 15 G. Bestand des Haftbefehls. Wird der Haftbefehl nicht aufgeh., bleibt er grds. in Kraft; er wird nicht durch Zeitablauf wirkungslos (OLG Hamm NStZ 2016, 304).  Voraussetzungen der Untersuchungshaft...
- **[Judge=2]** `Strafprozessordnung.md` — Behandelt Alternativen zur Untersuchungshaft bei Fluchtgefahr
  > ## Aussetzung des Vollzugs des Haftbefehls RiStBV 54, 57  116 (1) Der Richter setzt den Vollzug eines Haftbefehls, der lediglich wegen Fluchtgefahr gerechtfertigt ist, aus, wenn weniger einschneidende...

### q14 — stpo-prozess

**Query:** Wie lange darf die Untersuchungshaft maximal dauern?

**Kontext:** § 121 StPO Sechs-Monats-Grenze, Haftpruefung OLG

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours | 0.96 | 80% | 100% | 3 | 4.8s |
| ragie | 1.00 | 100% | 100% | 3 | 1.7s |
| openai | 0.99 | 10% | 33% | 2 | 1.4s |

#### ours — Top 3
- **[Judge=3]** `§ 121 StPO – Rn. 1` — Beantwortet direkt die Frage nach maximaler Haftdauer
  > Eine absolute Höchstgrenze für die Dauer v. UHaft sieht weder die StPO noch die EMRK vor (EGMR EuGRZ 1993, 384). Es kommt auf eine Abwägung aller Umstände des Einzelfalls an. Eine ein Jahr übersteigen...
- **[Judge=2]** `§ 121 StPO – Rn. 8 (Teil 1)` — Behandelt UHaft-Beschränkungen, aber nicht direkt Höchstdauer
  > 8 II. Zeitliche Geltung der Beschränkungen der UHaft. Bis zu einem auf Freiheitsentziehung lautenden Urteil (Freiheitsstrafe mit o. ohne Bewährung o. freiheitsentziehende Sicherungsmaßregeln) gelten d...
- **[Judge=3]** `§ 121 StPO – Rn. 121` — Beantwortet direkt die Frage zur maximalen UHaft-Dauer
  > 121 (1) Solange kein Urteil ergangen ist, das auf Freiheitsstrafe oder eine freiheitsentziehende Maßregel der Besserung und Sicherung erkennt, darf der Vollzug der Untersuchungshaft wegen derselben Ta...

#### ragie — Top 3
- **[Judge=3]** `Strafprozessordnung.md` — Behandelt direkt Dauer der Untersuchungshaft und Fristen
  > Strafprozessordnung.md die 6 Monate überschritten werden (Abs. 2), eine UHaft v. mehr als 1 Jahr bis zum Beginn der HV kann nur in ganz bes. Ausnahmefällen gerechtfertigt sein (BVerfG NJW 2018, 2948; ...
- **[Judge=3]** `Strafprozessordnung.md` — Behandelt direkt § 121 StPO Sechs-Monats-Grenze
  > Strafprozessordnung.md Der Haftbefehl wird gegenstandslos (BVerfGE 9, 160; KG NStZ 2012, 230; OLG Düsseldorf Rpfleger 1984, 73; OLG Hamm StraFo 2002, 100; OLG Stuttgart Justiz 1984, 213). Dies soll we...
- **[Judge=3]** `Strafprozessordnung.md` — Direkt zur Sechs-Monats-Grenze und zeitlichen Begrenzung der UHaft
  > Strafprozessordnung.md Die zeitliche Begrenzung der UHaft nach Abs. 1 gilt nicht, wenn der Haftbefehl nach § 230 Abs. 2 (→ § 230 Rn. 10), § 236 oder § 329 Abs. 4 S. 1 (→ § 329 Rn. 45) ergangen ist, au...

#### openai — Top 3
- **[Judge=2]** `Strafprozessordnung.md` — Jugendstrafrecht: andere Haftregeln als allgemeine Fristen
  > (5) Befindet sich ein Jugendlicher in Untersuchungshaft, so ist das Verfahren mit besonderer Beschleunigung durchzuführen.  (6) Die richterlichen Entscheidungen, welche die Untersuchungshaft betreffen...
- **[Judge=1]** `Strafprozessordnung.md` — Jugendstrafrecht, aber nicht Haftdauer-Grenzen
  > 2667  ---  ## Seite 2392  Anh. 1 JGG Jugendgerichtsgesetz  die zugrundeliegenden tatsächlichen Feststellungen letztmals geprüft werden konnten.² Wird die Vollstreckung des Restes der lebenslangen Frei...
- **[Judge=1]** `StGB_Kommentar.md` — Jugendstrafrecht, aber nicht allgemeine Haftdauer-Grenzwerte
  > (3) In den Fällen des Absatzes 1 gilt § 85 Abs. 6 entsprechend mit der Maßgabe, daß der Vollstreckungsleiter die Vollstreckung der Jugendstrafe abgeben kann, wenn der Verurteilte das einundzwanzigste ...

### q15 — stpo-prozess

**Query:** Was regelt § 136 StPO zur Beschuldigtenvernehmung?

**Kontext:** Belehrungspflichten, Recht auf Verteidiger

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours | 0.93 | 60% | 100% | 2 | 8.6s |
| ragie | 0.91 | 75% | 100% | 2 | 2.1s |
| openai | 0.99 | 50% | 100% | 2 | 1.6s |

#### ours — Top 3
- **[Judge=2]** `StPO – III. Steuerstrafverfahren – Rn. 79` — Behandelt Belehrungspflichten bei Vernehmungen, aber nicht § 136
  > 79 3. Die informatorische Befragung der Tatverdächtigen, die nach diesen Grundsätzen noch keine Beschuldigten sind, ist Zeugenvernehmung. Die Bestrebungen des Schrifttums, neben Beschuldigte u. Zeugen...
- **[Judge=3]** `§ 500 StPO – ILL. für das Strafverfahren und das Bußgeldverf` — Direkt relevant zu § 136 StPO Belehrungspflichten
  > (4) Zeugen können zur Aufenthaltsermittlung ausgeschrieben werden.  (5) Für die internationale Fahndung nach Personen, einschließlich der Fahndung nach Personen im SIS und aufgrund eines Europäischen ...
- **[Judge=3]** `StPO – III. Steuerstrafverfahren – Rn. 25` — Direkt relevant zu § 136 StPO Beschuldigtenvernehmung
  > Das nemo-tenetur-Prinzip (nemo tenetur se ipsum accusare und nemo tenetur se ipsum prodere) o. der Grundsatz der Selbstbelastungsfreiheit bedeutet, dass niemand verpflichtet ist, sich selbst anzuklage...

#### ragie — Top 3
- **[Judge=2]** `Strafprozessordnung.md` — Behandelt Beschuldigtenvernehmung und Belehrungspflichten, aber nicht direkt § 136
  > Strafprozessordnung.md 77a Der Verfolgungsbehörde steht insoweit ein – objektiv zu bestimmender – Beurteilungsspielraum zu (BGHSt 38, 214 (228); BGHSt 64, 89; StraFo 2005, 27; erg. → StPO § 163a Rn. 4...
- **[Judge=2]** `Strafprozessordnung.md` — Behandelt Vernehmungsverfahren, aber nicht § 136 selbst
  > Strafprozessordnung.md (2) In der Ladung zu einer richterlichen oder staatsanwaltschaftlichen Vernehmung sollen Zwangsmaßnahmen für den Fall des Ausbleibens nur angedroht werden, wenn sie gegen den un...
- **[Judge=2]** `Strafprozessordnung.md` — Behandelt Vernehmungsform, aber nicht § 136 selbst
  > Strafprozessordnung.md 45. Form der Vernehmung und Niederschrift. (1) ¹ Die Belehrung des Beschuldigten vor seiner Vernehmung nach § 136 Absatz 1, § 163a Absatz 3 Satz 2 StPO ist aktenkundig zu machen...

#### openai — Top 3
- **[Judge=2]** `Strafprozessordnung.md` — Behandelt Belehrungspflichten bei Beschuldigtenvernehmung, verweist auf § 136
  > aber auch BayObLGSt 2004, 141). Ist die Einleitung eines Ermittlungsverfahrens geboten, weil der Vernehmungsbeamte den Verdächtigen als Täter überführen will, dann darf dieser nicht als Zeuge vernomme...
- **[Judge=2]** `Strafprozessordnung.md` — Behandelt Beschuldigteneigenschaft, nicht direkt § 136
  > 77 1. Tatverdacht allein begründet allerdings weder die Beschuldigteneigenschaft noch zwingt er ohne weiteres zur Einleitung v. Ermittlungen (BGHSt 64, 89 = NJW 2019, 2627 (2630)), auch nicht allein d...
- **[Judge=2]** `StGB_Kommentar.md` — Behandelt § 136 StPO, aber nicht Belehrungspflichten
  > Abs. 2 enthält eine Bestimmung des Unterbrechungszeitpunkts, wenn dieser eine schriftliche Anordnung oder Entscheidung voraussetzt. Die Regelung ist durch G vom 15.6.2021 (BGBl. I 2099) geändert worde...

### q16 — cross-reference

**Query:** Worin unterscheidet sich Betrug von Unterschlagung?

**Kontext:** Abgrenzung § 263 vs § 246 StGB

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours | 0.93 | 50% | 67% | 3 | 9.2s |
| ragie | 0.89 | 67% | 67% | 2 | 2.9s |
| openai | 0.98 | 40% | 67% | 3 | 1.5s |

#### ours — Top 3
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 76` — Betrifft direkt Abgrenzung zwischen Betrug und Diebstahl/Unterschlagung
  > 4. Dreiecksbetrug. Da die Getäuschte und die verfügende, nicht aber die verfügende und die geschädigte Person identisch sein müssen, ist der Tatbestand des § 263 nur erfüllt, wenn die Vermögensverfügu...
- **[Judge=1]** `§ 263 StGB – BT. Zweitundzwanzigster Abschnitt – Rn. 69` — Behandelt nur Betrug, nicht Unterschlagungsabgrenzung
  > 69 Anders ist es, wenn der Verfügende seinerseits nur (gutgläubige) Hilfsperson eines bösgläubigen Dritten ist. Hier ist auf den Irrtum des Entscheidungsbefugten abzustellen: Erkennt dieser die Unrich...
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 76` — Direkt relevant: zentrale Abgrenzungskriterien Betrug/Verfügung erklärt
  > 76 3. Unmittelbarkeit der Verfügung. Neben der Freiwilligkeit ist das Merkmal der Unmittelbarkeit nach stRspr und hM das wichtigste Kriterium zur Beschränkung der § 263 unterfallenden Selbstschädigung...

#### ragie — Top 3
- **[Judge=2]** `StGB_Kommentar.md` — Behandelt Wahlfeststellungen zwischen Betrug und Unterschlagung
  > StGB_Kommentar.md 3. Einzelfälle. a) Zulässig sind Wahlfeststellungen nach hM (umfassende Dokumentation bei Wolter (→ Rn. 38) S. 174 ff.) zwischen:  Diebstahl und Hehlerei (BGHSt 1, 302; 12, 386; 15, ...
- **[Judge=1]** `StGB_Kommentar.md` — Nur Inhaltsverzeichnis, keine Abgrenzung der Tatbestände
  > StGB_Kommentar.md # Neunzehnter Abschnitt. Diebstahl und Unterschlagung  Diebstahl ... § 242 Besonders schwerer Fall des Diebstahls ... § 243 Diebstahl mit Waffen; Bandendiebstahl; Wohnungseinbruchdie...
- **[Judge=3]** `StGB_263_Betrug.md` — Direkte Abgrenzung zwischen Betrug und anderen Delikten
  > StGB_263_Betrug.md Fischer/Lutz  ---  ## Seite 747  Betrug und Untreue § 263  Dagegen fehlt eine Vermögensverfügung, wenn durch die Handlung des Getäuschten nur eine Zugriffsmöglichkeit für den Täter ...

#### openai — Top 3
- **[Judge=3]** `StGB_Kommentar.md` — Direkte Abgrenzung § 246 zu § 263 erklärt
  > Für den Vortäter kann die Unterschlagung mit Drittzueignungswillen zugleich Beihilfe zur Hehlerei sein; in diesem Fall dürfte die Beteiligung an § 259 ebenso zurücktreten wie im Fall einer real konkur...
- **[Judge=2]** `StGB_Kommentar.md` — Thematisch relevant: behandelt Konkurrenz § 246/§ 263
  > Für Fälle des Abs. 2 ist für den Vergleich der Strafdrohungen auf den Strafrahmen der (tatbestandlichen) Qualifikation abzustellen. Daraus ergeben sich zufällig erscheinende Konkurrenz-Folgen.  23d Pr...
- **[Judge=1]** `Probenheld-KOMPLETT.md` — Behandelt nur Betrug, nicht Abgrenzung zur Unterschlagung
  > Vermögensschaden trotz fehlender Zahlung: Die Gerichte werten auch die bloße Berechnung einer Forderung als schadensbegründend; der fehlende Zahlungswille des Kunden verhindert nicht die Strafbarkeit....

### q17 — cross-reference

**Query:** Was sind die Unterschiede zwischen Diebstahl und Raub?

**Kontext:** § 242 vs § 249 StGB — Abgrenzung durch Gewalt/Drohung

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours | 0.96 | 90% | 100% | 3 | 10.6s |
| ragie | 0.99 | 100% | 100% | 3 | 2.0s |
| openai | 0.91 | 30% | 67% | 2 | 1.9s |

#### ours — Top 3
- **[Judge=3]** `§ 249 StGB – BT. Zwanzigster Abschnitt – Rn. 15` — Erklärt subjektiven Tatbestand bei Raub vs Diebstahl
  > G. Subjektiver Tatbestand. Der Vorsatz muss entsprechend der Doppelnatur des Raubs sowohl Wegnahme (vgl. dazu → § 242 Rn. 29 ff.) als auch Nötigung (→ § 240 Rn. 53 f.) sowie deren Verknüpfung umfassen...
- **[Judge=3]** `§ 249 StGB` — Direkt relevant: Raub-Definition mit Nötigungsmitteln vs Diebstahl
  > NStZ 2023, 351). Danach ist § 249 gegenüber § 255 ein spezielles Delikt; in jedem Raub liegt eine räuberische Erpressung (aA die hM in der Literatur). Die Unterscheidung richtet sich nach dem äußeren ...
- **[Judge=3]** `§ 241a StGB – BT. Achtzchniter Abschnitt – Rn. 242` — Direkt relevant: Tatbestandsmerkmale des Diebstahls
  > 242 (1) Wer eine fremde bewegliche Sache einem anderen in der Absicht wegnimmt, die Sache sich oder einem Dritten rechtswidrig zuzueignen, wird mit Freiheitsstrafe bis zu fünf Jahren oder mit Geldstra...

#### ragie — Top 3
- **[Judge=3]** `StGB_Kommentar.md` — Direkte Abgrenzung Raub-Diebstahl mit Gewaltkriterium
  > StGB_Kommentar.md Rechtsprechungsübersichten: Maier/Percic NStZ-RR 2010, 129; Maier NStZ-RR 2012, 297; 2013, 329 (364); 2015, 33; 2017, 1, 2018, 33; 2025, 129; 2025, 161.  2 B. Systematische Stellung....
- **[Judge=3]** `StGB_Kommentar.md` — Behandelt direkt Abgrenzung und Konkurrenzen zwischen Diebstahl und Raub
  > StGB_Kommentar.md J. Konkurrenzen. Gesetzeseinheit liegt zwischen § 249 und §§ 242, 243, 244, 244a vor, die von § 249 verdrängt werden (vgl. BGHSt 20, 235 (237 f.); NStZ-RR 2005, 202 (203)). Entsprech...
- **[Judge=3]** `StGB_Kommentar.md` — Direkt relevant: behandelt Raub-Definition und Abgrenzungskriterien
  > StGB_Kommentar.md E. Strafantrag. Abs. 3 regelt ein Antragserfordernis entspr. §§ 247, 248a (vgl. → § 247 Rn. 1 ff., → § 248a Rn. 1 ff.).  F. Abs. 4. Nach Abs. 4 wird milder bestraft, wer ohne Zueignu...

#### openai — Top 3
- **[Judge=2]** `StGB_Kommentar.md` — Konkurrenzen zwischen Raub/Diebstahl, nicht direkte Abgrenzung
  > 12 I. Konkurrenzen. Gesetzeseinheit besteht mit §§ 242, 244 sowie mit § 240 (diff. NK-StGB/Kindhäuser Rn. 28). § 249 verdrängt § 252, wenn Raubmittel zunächst zur Wegnahme und später zur Sicherung des...
- **[Judge=1]** `StGB_Kommentar.md` — Schwerer Raub, nicht Grundabgrenzung Diebstahl/Raub
  > 1); zwischen § 249 und § 255, wenn neben der vom Tatopfer herausgegebenen Sache noch eine weitere gewaltsam weggenommen wird (BGH NStZ 2025, 40); mit § 223 (BGH NStZ-RR 1999, 173; NK-StGB/Kindhäuser R...
- **[Judge=3]** `StGB_Kommentar.md` — Erklärt zentrale Abgrenzung Diebstahl/Raub durch Konkurrenzregeln
  > J. Konkurrenzen. Gesetzeseinheit liegt zwischen § 249 und §§ 242, 243, 244, 244a vor, die von § 249 verdrängt werden (vgl. BGHSt 20, 235 (237 f.); NStZ-RR 2005, 202 (203)). Entsprechendes gilt zwische...

### q18 — cross-reference

**Query:** Wann wird Betrug zu Computerbetrug und umgekehrt?

**Kontext:** § 263 vs § 263a StGB — Abgrenzung bei elektronischer Datenverarbeitung

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours | 1.00 | 100% | 100% | 3 | 11.6s |
| ragie | 0.89 | 78% | 100% | 2 | 1.8s |
| openai | 0.67 | 10% | 0% | 0 | 1.6s |

#### ours — Top 3
- **[Judge=3]** `§ 263a StGB – M. Sonstige Vorschriften 40 – Rn. 239` — Direkter Kommentar zu § 263a StGB Computerbetrug
  > 239 I. Sonstige Vorschriften. FAufsicht §§ 263 Abs. 5, 68 Abs. 1. Zuständigkeit in Wirtschaftsstrafaschen § 74c Abs. 1 Nr. 6, § 74e Nr. 2 GVG iVm § 103 Abs. 2 JGG. TKÜ § 100a Abs. 2 Nr. 1 Buchst. n St...
- **[Judge=3]** `§ 263a StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 23` — Direkte Abgrenzung § 263 vs § 263a
  > 23 G. Subjektiver Tatbestand. Die Tat setzt (bedingten) Vorsatz voraus. Er muss sich auf alle Tatbestandsmerkmale, zu denen auch die Unbefugtheit (→ Rn. 10) gehört, dh auch auf die Voraussetzungen ers...
- **[Judge=3]** `§ 263a StGB – L. Konkurrenzen – Rn. 33` — Behandelt direkt Abgrenzung § 263 vs § 263a
  > II. Verhältnis zu sonstigen Tatbeständen. § 263a und § 263 schließen sich aus, wenn derselbe Schaden sowohl durch die Manipulationsweisen des § 263a als auch durch Täuschung bewirkt wird. Mit § 263 is...

#### ragie — Top 3
- **[Judge=2]** `StGB_Kommentar.md` — Behandelt § 263a, aber nicht die Abgrenzung zu § 263
  > StGB_Kommentar.md Fischer/Lutz  ---  ## Seite 799  Betrug und Untreue § 263a  IV. Subjektiver Tatbestand. In subjektiver Hinsicht ist (mindestens bedingter) Vorsatz hinsichtlich der Merkmale des Compu...
- **[Judge=2]** `StGB_263_Betrug.md` — Erwähnt Betrug vs Computerbetrug, aber nur Literaturverweis
  > StGB_263_Betrug.md FS Samson, 2010, 455; Ruha, Neue Wege für das Betrugsstrafrecht, FS Rissing-van Saan, 2011, 567; Satzger, Der Submissionsbetrug, 1994; Scheinfeld, Betrug durch unternehmerisches Wer...
- **[Judge=3]** `StGB_Kommentar.md` — Zentraler Paragraph Computerbetrug, direkt relevant fuer Abgrenzung
  > StGB_Kommentar.md ## Computerbetrug  263a (1) Wer in der Absicht, sich oder einem Dritten einen rechtswidrigen Vermögensvorteil zu verschaffen, das Vermögen eines anderen dadurch beschädigt, daß er da...

#### openai — Top 3
- **[Judge=0]** `Probenheld-KOMPLETT.md` — Tabellarische Auflistung von Verfahren, keine Abgrenzungskriterien
  > | § 263 StGB Betrug | Vg / 281492 / 2019 | Bezikakriminalinapek Iron Kiel, <br> Fachinapektion 1, <br> Kommissariat 14 | Uda Mark, (8575) | 0431/180-3183 | StA M.Öpiglt: 56/2/19 <br> StA Kiel: 596 UJa...
- **[Judge=1]** `Probenheld-KOMPLETT.md` — Akteninhalt zu Computerbetrug, keine rechtliche Abgrenzung
  > **Betrug** **101109** **(1)**  ## Weggelegt  **Aufzubewahren bis**  - dauernd -  **Aktenzeichen:** **107 Js 1871/19** **Datum:** **12.12.2019**  **Verfahrensgegenstand nach der Justizstatistik**  | Sc...
- **[Judge=1]** `Probenheld-KOMPLETT.md` — Behandelt § 263a aber nicht die Abgrenzung
  > Das vorliegende Verfahren wird abgeschlossen und der STA Cottbus mit der Bitte um Kenntnisnahme und zur weiteren Entscheidung übersandt.  ## ABSCHLIEßENDER BERICHT  Polizeipräsidium Polizeidirektion S...