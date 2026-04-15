# RAG Benchmark Report

_Generiert: 2026-04-15T22:46:10_


- Queries: **18**
- Top-K: **10**
- Systeme: ours, ragie

## Gesamtvergleich

| Metrik | ours | ragie |
|--------|--------|--------|
| nDCG@10 | 0.858 | 0.937 |
| Relevance@10 | 67.2% | 78.9% |
| Relevance@3 | 81.5% | 75.9% |
| Top-1-Score | 2.50 | 2.50 |
| Mean-Score | 2.03 | 2.35 |
| Latenz (s) | 5.80 | 2.91 |

## Nach Kategorie


### alltagssprache

| Metrik | ours | ragie |
|--------|--------|--------|
| nDCG@10 | 0.986 | 0.937 |
| Relevance@10 | 92.5% | 80.6% |
| Relevance@3 | 100.0% | 83.3% |

### cross-reference

| Metrik | ours | ragie |
|--------|--------|--------|
| nDCG@10 | 0.621 | 0.934 |
| Relevance@10 | 33.3% | 71.9% |
| Relevance@3 | 44.4% | 66.7% |

### exakte-paragraphen

| Metrik | ours | ragie |
|--------|--------|--------|
| nDCG@10 | 0.987 | 0.879 |
| Relevance@10 | 77.5% | 71.1% |
| Relevance@3 | 100.0% | 50.0% |

### konzept

| Metrik | ours | ragie |
|--------|--------|--------|
| nDCG@10 | 0.933 | 0.982 |
| Relevance@10 | 65.0% | 83.3% |
| Relevance@3 | 83.3% | 83.3% |

### stpo-prozess

| Metrik | ours | ragie |
|--------|--------|--------|
| nDCG@10 | 0.656 | 0.954 |
| Relevance@10 | 56.7% | 88.3% |
| Relevance@3 | 66.7% | 100.0% |

## Detail pro Query


### q01 — exakte-paragraphen

**Query:** Welche Voraussetzungen hat der gewerbsmaessige Bandenbetrug nach § 263 Abs. 5 StGB?

**Kontext:** Qualifikationstatbestand des Bandenbetrugs im Fischer-Kommentar

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours | 1.00 | 60% | 100% | 3 | 6.1s |
| ragie | 0.99 | 100% | 100% | 3 | 2.5s |

#### ours — Top 3
- **[Judge=3]** `§ 263 StGB – BT. Zweriindzwanzigster Abschnitt – Rn. 225` — Direkt relevant: Bandenbetrug Abs. 5 Voraussetzungen erklärt
  > IV. Qualifikation (Abs. 5). Abs. 5 enthält einen Qualifikationstatbestand, der die Tat in Fällen kumulativ gewerbs- und bandenmäßiger Begehung zum Verbrechen macht. Die Qualifikation ist in die Urteil...
- **[Judge=3]** `§ 263 StGB – I. Vermögensbegriff  – Rn. 263` — Enthält direkt § 263 Abs. 5 Bandenbetrug-Voraussetzungen
  > 263 (1) Wer in der Absicht, sich oder einem Dritten einen rechtswidrigen Vermögensvorteil zu verschaffen, das Vermögen eines anderen dadurch beschädigt, daß er durch Vorspiegelung falscher oder durch ...
- **[Judge=3]** `§ 263 StGB – BT. Zweijundzwanzigster Abschnitt – Rn. 213` — Direkte Erläuterung der Qualifikationstatbestände nach Abs. 5
  > 213 Sind beide Varianten erfüllt, ist eine Qualifikation nach Abs. 5 gegeben. Die Abgrenzung des Abs. 3 Nr. 1 zum Verbrechen nach Abs. 5 ist in Fällen bandenmäßiger Begehung schwierig, denn eine auf f...

#### ragie — Top 3
- **[Judge=3]** `StGB_263_Betrug.md` — Behandelt direkt Bandenbetrug § 263 Abs. 5 Voraussetzungen
  > StGB_263_Betrug.md 213 Sind beide Varianten erfüllt, ist eine Qualifikation nach Abs. 5 gegeben. Die Abgrenzung des Abs. 3 Nr. 1 zum Verbrechen nach Abs. 5 ist in Fällen bandenmäßiger Begehung schwier...
- **[Judge=3]** `StGB_Kommentar.md` — Direkt relevant zu Bandenbetrug § 263 Abs. 5 Voraussetzungen
  > StGB_Kommentar.md 213 Sind beide Varianten erfüllt, ist eine Qualifikation nach Abs. 5 gegeben. Die Abgrenzung des Abs. 3 Nr. 1 zum Verbrechen nach Abs. 5 ist in Fällen bandenmäßiger Begehung schwieri...
- **[Judge=3]** `StGB_263_Betrug.md` — Direkt relevant: Erklärt Voraussetzungen von § 263 Abs. 5
  > StGB_263_Betrug.md IV. Qualifikation (Abs. 5). Abs. 5 enthält einen Qualifikationstatbestand, der die Tat in Fällen kumulativ gewerbs- und bandenmäßiger Begehung zum Verbrechen macht. Die Qualifikatio...

### q02 — exakte-paragraphen

**Query:** Was regelt § 112 StPO zur Untersuchungshaft?

**Kontext:** Anordnungsvoraussetzungen der U-Haft (dringender Tatverdacht, Haftgrund) im Schmitt/Koehler

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours | 1.00 | 100% | 100% | 3 | 5.8s |
| ragie | 0.95 | 75% | 67% | 3 | 2.6s |

#### ours — Top 3
- **[Judge=3]** `§ 112 StPO – Rn. 112` — Vollständiger Gesetzestext zu § 112 StPO Untersuchungshaft
  > 112 (1) ¹ Die Untersuchungshaft darf gegen den Beschuldigten angeordnet werden, wenn er der Tat dringend verdächtig ist und ein Haftgrund besteht. ² Sie darf nicht angeordnet werden, wenn sie zu der B...
- **[Judge=3]** `§ 112 StPO – III. Flucht (Abs – Rn. 32 (Teil 2)` — Direkt relevant - behandelt Verdunkelungsgefahr als Haftgrund
  > Wenn die Verdunkelungshandlungen nicht geeignet sind, die Ermittlung der Wahrheit zu erschweren, darf UHaft nicht angeordnet werden. Der Haftgrund liegt daher nicht vor, wenn der Sachverhalt schon in ...
- **[Judge=3]** `§ 112 StPO – III. Flucht (Abs – Rn. 23` — Direkt relevant: behandelt zentrale Haftgruende nach § 112 StPO
  > Bei einer besonders hohen Straferwartung braucht daher nur geprüft zu werden, ob Umstände vorhanden sind, die die hieraus herzuleitende Fluchtgefahr ausräumen können (KG StV 1996, 383; OLG München Str...

#### ragie — Top 3
- **[Judge=3]** `Strafprozessordnung.md` — Direkt relevant: behandelt § 112 StPO Haftvoraussetzungen
  > Strafprozessordnung.md Werden mehrere Haftbefehle in verschiedenen Sachen erlassen, so kann nur einer v. ihnen vollzogen werden. Eine „Doppelhaft“ ist ausgeschlossen (Münchhalffen/Gatzweiler Untersuch...
- **[Judge=3]** `Strafprozessordnung.md` — Direkt relevant: behandelt Anordnungsvoraussetzungen § 112 StPO
  > Strafprozessordnung.md a) der dringende Tatverdacht, b) der Haftgrund  ergeben.  ---  ## Seite 2435  Anh. 3 RiStBV  RL für das Strafverfahren und das Bußgeldverfahren  (2) Wenn die Anwendung des § 112...
- **[Judge=1]** `Strafprozessordnung.md` — Jugendstrafrecht, nicht allgemeine Regeln des § 112 StPO
  > Strafprozessordnung.md § 72 Untersuchungshaft. (1) ¹ Untersuchungshaft darf nur verhängt und vollstreckt werden, wenn ihr Zweck nicht durch eine vorläufige Anordnung über die Erziehung oder durch ande...

### q03 — exakte-paragraphen

**Query:** Welche Haftgruende nennt § 112 Abs. 2 StPO?

**Kontext:** Fluchtgefahr, Verdunkelungsgefahr, Flucht — im StPO-Kommentar

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours | 0.98 | 90% | 100% | 3 | 4.8s |
| ragie | 0.76 | 43% | 0% | 1 | 3.3s |

#### ours — Top 3
- **[Judge=3]** `§ 112 StPO – Rn. 112` — Beantwortet die Frage direkt mit den Haftgruenden
  > 112 (1) ¹ Die Untersuchungshaft darf gegen den Beschuldigten angeordnet werden, wenn er der Tat dringend verdächtig ist und ein Haftgrund besteht. ² Sie darf nicht angeordnet werden, wenn sie zu der B...
- **[Judge=3]** `§ 112 StPO – III. Flucht (Abs – Rn. 23` — Direkt relevant: behandelt Haftgruende nach § 112 Abs. 2 StPO
  > Bei einer besonders hohen Straferwartung braucht daher nur geprüft zu werden, ob Umstände vorhanden sind, die die hieraus herzuleitende Fluchtgefahr ausräumen können (KG StV 1996, 383; OLG München Str...
- **[Judge=3]** `§ 112 StPO – III. Flucht (Abs – Rn. 32 (Teil 2)` — Direkt zu Verdunkelungsgefahr aus § 112 Abs. 2 StPO
  > Wenn die Verdunkelungshandlungen nicht geeignet sind, die Ermittlung der Wahrheit zu erschweren, darf UHaft nicht angeordnet werden. Der Haftgrund liegt daher nicht vor, wenn der Sachverhalt schon in ...

#### ragie — Top 3
- **[Judge=1]** `Strafprozessordnung.md` — Behandelt § 112 Abs. 3, nicht die gesuchten Haftgründe
  > Strafprozessordnung.md 38 Die Vorschr. begründet bei dieser Auslegung weder eine Vermutung der Haftgründe (aM OLG Düsseldorf MDR 1983, 152; offenbar auch OLG Bremen StV 1983, 288), noch findet eine „U...
- **[Judge=1]** `Strafprozessordnung.md` — Erwähnt § 112 Abs. 2 StPO, nennt aber keine konkreten Haftgründe
  > Strafprozessordnung.md (3) ¹ Hinsichtlich der Möglichkeit und gegebenenfalls Pflicht zur Aufzeichnung der Vernehmung des Beschuldigten in Bild und Ton sind § 136 Absatz 4 StPO bzw. § 70c Absatz 2 Satz...
- **[Judge=1]** `Strafprozessordnung.md` — Behandelt Haftbefehl-Anforderungen, nicht konkrete Haftgruende
  > Strafprozessordnung.md Soweit die Staatssicherheit gefährdet wurde, kann v. der Begründung des dringenden Tatverdachts abgesehen werden (dazu Creifelds NJW 1965, 949); das muss in dem Haftbefehl zum A...

### q04 — exakte-paragraphen

**Query:** Was regelt § 102 StPO zur Durchsuchung beim Beschuldigten?

**Kontext:** Durchsuchungsvoraussetzungen beim Verdaechtigen

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours | 0.97 | 60% | 100% | 3 | 5.5s |
| ragie | 0.82 | 67% | 33% | 1 | 2.7s |

#### ours — Top 3
- **[Judge=3]** `§ 102 StPO – Rn. 102` — Direkter Gesetzestext zu § 102 StPO Durchsuchung
  > 102 Bei dem, welcher als Täter oder Teilnehmer einer Straftat oder der Datenhehlerei, Begünstigung, Strafvereitelung oder Hehlerei  Köhler    Ermittlungsmaßnahmen  verdächtig ist, kann eine Durchsuchu...
- **[Judge=2]** `§ 102 StPO – Rn. 10` — Thematisch relevant zu Durchsuchungsvoraussetzungen, aber nicht spezifisch § 102
  > II. Auffinden von Beweismitteln. Zu den Beweismitteln (→ § 94 Rn. 4 ff.) gehören auch die nur in § 103 erwähnten Spuren (SK-StPO/Jäger/Wohlers Rn. 21) u. Personen, die zu Beweiszwecken in Augenschein ...
- **[Judge=3]** `§ 102 StPO – Rn. 10` — Direkt relevant - erklärt § 102 StPO Durchsuchungsgegenstand
  > 10 III. Sachen. Sachen sind Kleidungsstücke, die der Verdächtige bei sich führt, ohne sie zu tragen, u. seine sonstige bewegliche Habe, gleichgültig, ob sie sich in seinem Umkreis, zB in Gepäckstücken...

#### ragie — Top 3
- **[Judge=1]** `Strafprozessordnung.md` — Behandelt § 103 StPO, nicht § 102 StPO
  > Strafprozessordnung.md 3 B. Durchsuchungsgegenstände. Durchsuchungsgegenstände können die Wohnung u. Räume des Unverdächtigen (→ § 102 Rn. 7) sowie seine Person (→ § 102 Rn. 9) u. die ihm gehörenden S...
- **[Judge=3]** `Strafprozessordnung.md` — Beantwortet direkt Frage zu § 102 StPO
  > Strafprozessordnung.md Durchsuchung bei Beschuldigten RiStBV 73a  102 Bei dem, welcher als Täter oder Teilnehmer einer Straftat oder der Datenhehlerei, Begünstigung, Strafvereitelung oder Hehlerei  Kö...
- **[Judge=1]** `Strafprozessordnung.md` — Behandelt § 103 StPO, nicht § 102 StPO
  > Strafprozessordnung.md 2 Auch Dienstgebäude u. -räume v. Behörden dürfen nur durchsucht werden (vgl. § 105 Abs. 3 S. 3), wenn dies erforderlich, um den Beschuldigten zu ergreifen oder Beweismittel auf...

### q05 — konzept

**Query:** Wann liegt eine konkludente Taeuschung im Sinne des § 263 StGB vor?

**Kontext:** Taeuschungshandlung durch schluessiges Verhalten

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours | 0.85 | 50% | 67% | 1 | 5.6s |
| ragie | 0.95 | 89% | 67% | 3 | 3.8s |

#### ours — Top 3
- **[Judge=1]** `§ 263 StGB – I. Vermögensbegriff  – Rn. 263` — Gesetzestext ohne konkludente Täuschung Definition
  > 263 (1) Wer in der Absicht, sich oder einem Dritten einen rechtswidrigen Vermögensvorteil zu verschaffen, das Vermögen eines anderen dadurch beschädigt, daß er durch Vorspiegelung falscher oder durch ...
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 14` — Definiert direkt konkludente Taeuschung und Abgrenzung
  > Rspr. und hM bejahen darüber hinaus aber die Möglichkeit einer Täuschung durch Unterlassen auch ohne Erklärung gegenüber dem Irrenden (→ Rn. 38; vgl. BGHSt 39, 392 (398); BayObLG NJW 1987, 1654 (mAnm ...
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 14` — Behandelt direkt konkludente Tatsachenbehauptung bei § 263
  > 14 II. Tathandlung. Der Begriff „Täuschen“ ist im Wortlaut des Abs. 1 nicht verwendet; er ergibt sich aus dem Zusammenhang zwischen der Beschreibung der Tathandlung (→ Rn. 18) und dem Irrtum als ihrem...

#### ragie — Top 3
- **[Judge=3]** `StGB_263_Betrug.md` — Definiert konkludente Taeuschung bei § 263 direkt
  > StGB_263_Betrug.md 21 2. Konkludente Erklärungen. Auch durch eine schlüssige Handlung (konkludente Erklärung) kann vorspiegelt werden. Eine solche konkludente Erklärung durch aktives Tun ist von einer...
- **[Judge=1]** `StGB_Kommentar.md` — Erwähnt konkludente Täuschung, aber bei anderem Tatbestand
  > StGB_Kommentar.md E. Vollendung, Versuch. Die Tat ist mit dem Eintritt des Schadens vollendet und idR auch beendet iSv § 78a. Der Versuch ist nicht strafbar. Die (vom Gesetzgeber des 2. WiKG verworfen...
- **[Judge=3]** `StGB_263_Betrug.md` — Direkt relevant: Definition konkludenter Taeuschung § 263
  > StGB_263_Betrug.md 22 Sowohl ausdrücklichen Erklärungen als auch tatsächlichen Handeln kann ein konkludenter Erklärungswert zukommen. Aus der bloßen Feststellung eines Irrtums kann aber nicht schon au...

### q06 — konzept

**Query:** Was ist eine Vermoegensverfuegung und welche Anforderungen stellt die Rechtsprechung?

**Kontext:** Tatbestandsmerkmal der Vermoegensverfuegung beim Betrug

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours | 0.96 | 60% | 100% | 3 | 5.7s |
| ragie | 1.00 | 67% | 67% | 3 | 2.9s |

#### ours — Top 3
- **[Judge=3]** `§ 263 StGB – BT. Zweitundzwanzigster Abschnitt – Rn. 69` — Definiert Vermoegensverfuegung und deren tatbestandsrelevante Anforderungen
  > 69 Anders ist es, wenn der Verfügende seinerseits nur (gutgläubige) Hilfsperson eines bösgläubigen Dritten ist. Hier ist auf den Irrtum des Entscheidungsbefugten abzustellen: Erkennt dieser die Unrich...
- **[Judge=2]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 87` — Behandelt Kausalität und Vermögensschaden, nicht Verfügungsbegriff selbst
  > 87 5. Kausalität. Für die Vermögensverfügung muss der täuschungsbedingte Irrtum kausal sein (vgl. BGHSt 24, 257 (260); 24, 386 (389); NStZ 2003, 313 (314 f.); OLG Düsseldorf NJW 1987, 3145); Mitverurs...
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 74` — Definiert Vermögensverfügung und zentrale Rechtsprechungsanforderungen
  > 74 2. Verfügungsbewusstsein. Vermögensverfügungen sind nach hM grundsätzlich sowohl als bewusst als auch als unbewusst vermögensmindernde Handlungen möglich; eine aktuelle Vorstellung des Verfügenden ...

#### ragie — Top 3
- **[Judge=3]** `StGB_Kommentar.md` — Definiert Vermoegensverfuegung mit konkreten Rechtsprechungsbeispielen
  > StGB_Kommentar.md a) Einzelfälle. Als Verfügungen sind zB angesehen worden: Veranlassung oder Vornahme einer Überweisung (wistra 1987, 257; NStZ 1999, 558); Herausgabe fremder Sachen: Bewilligung von ...
- **[Judge=3]** `StGB_Kommentar.md` — Direkt relevant: Definition und Anforderungen Vermoegensverfuegung
  > StGB_Kommentar.md 1. Verfügungshandlung. Die Anzahl möglicher vermögensmindernder Handlungen ist grds. unbeschränkt; sie sind meist den Fallgruppen des Eingehens oder des Erfüllens einer Verbindlichke...
- **[Judge=1]** `StGB_Kommentar.md` — Behandelt Vermögensschaden, nicht Vermögensverfügung selbst
  > StGB_Kommentar.md 113 2. Vermögensminderung. Erforderlich ist eine durch die Vermögensverfügung kausal verursachte Minderung des Vermögenswerts durch den Verlust oder die Wertminderung von Aktiva oder...

### q07 — konzept

**Query:** Was versteht man unter einem Gefaehrdungsschaden beim Betrug?

**Kontext:** Schadensbegriff, schadensgleiche Vermoegensgefaehrdung

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours | 0.98 | 100% | 100% | 3 | 7.0s |
| ragie | 1.00 | 100% | 100% | 3 | 1.7s |

#### ours — Top 3
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 159` — Definiert Gefaehrdungsschaden beim Betrug vollstaendig
  > 159 b) Voraussetzungen. aa) Ein Gefährdungsschaden ist gegeben, wenn die Wahrscheinlichkeit des endgültigen Verlusts eines Vermögensbestandteils zum Zeitpunkt der täuschungsbedingten Verfügung so groß...
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 182` — Direkt relevant: behandelt Gefährdungsschaden beim Betrug
  > 182 In Fällen des Gefährdungsschadens hat der BGH vielfach entschieden, die Kenntnis von Umständen, welche die Gefahr des Vermögensverlusts begründen, reiche oft, aber nicht in jedem Fall aus, um das ...
- **[Judge=2]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 128` — Erwähnt Gefährdungsschaden, aber ohne Definition oder Erklärung
  > 128 (4) BGHSt 51, 10 = NJW 2006, 1679 hat diese Grundsätze auf Fälle des Anlagebetrugs übertragen. Hier liegt ein Schaden vor, soweit die Zins- und Gewinnerwartungen des über das Risiko Getäuschten hi...

#### ragie — Top 3
- **[Judge=3]** `StGB_263_Betrug.md` — Direkt relevant: erklärt Gefährdungsschaden-Voraussetzungen beim Betrug
  > StGB_263_Betrug.md 159 b) Voraussetzungen. aa) Ein Gefährdungsschaden ist gegeben, wenn die Wahrscheinlichkeit des endgültigen Verlusts eines Vermögensbestandteils zum Zeitpunkt der täuschungsbedingte...
- **[Judge=3]** `StGB_263_Betrug.md` — Definiert direkt Gefährdungsschaden beim Betrug mit Voraussetzungen
  > StGB_263_Betrug.md 158 Der 3. StS hat in BGHSt 54, 69 (122 ff.) (Anm. Joecks wistra 2010, 179; vgl. → Rn. 8; → Rn. 176) sowohl der Sache nach als auch begrifflich am „Gefährdungsschaden“ festgehalten ...
- **[Judge=3]** `StGB_Kommentar.md` — Erklärt Gefährdungsschaden beim Betrug direkt und ausführlich
  > StGB_Kommentar.md Die täuschungsbedingte Herausgabe von EC-Karten, Kreditkarten und weiteren Zugangsdaten zu Bank-Guthaben (PINs, TANs; Passwörter), sei es infolge persönlicher Täuschung oder von „Phi...

### q08 — konzept

**Query:** Wie wird der Vorsatz beim Betrug bestimmt, insbesondere die Bereicherungsabsicht?

**Kontext:** Subjektiver Tatbestand § 263 StGB

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours | 0.94 | 50% | 67% | 3 | 5.6s |
| ragie | 0.98 | 78% | 100% | 3 | 3.5s |

#### ours — Top 3
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 176` — Direkt relevant: behandelt Vorsatz und Bereicherungsabsicht bei Betrug
  > D. Subjektiver Tatbestand. § 263 setzt Vorsatz voraus; darüber hinaus ist die Absicht rechtswidriger Bereicherung erforderlich.   I. Vorsatz. 1. Täuschungsvorsatz. Der Vorsatz (bedingter Vorsatz genüg...
- **[Judge=3]** `§ 263 StGB – I. Sonstige Vorschriften 239 – Rn. 263 (Teil 1)` — Direkter Bezug zu Bereicherungsabsicht und Vorsatz Betrug
  > 3. Einzelne Fallgruppen ... 92 4. Rechtlich missbilligte, sittenwidrige und gesetzeswidrige wirtschaftliche Werte ... 101 VI. Schaden ... 110 1. Grundsätze der Schadensermittlung ... 111 2. Vermögensm...
- **[Judge=1]** `§ 263 StGB – I. Vermögensbegriff  – Rn. 263` — Gesetzestext ohne Erläuterung zu Vorsatz/Bereicherungsabsicht
  > 263 (1) Wer in der Absicht, sich oder einem Dritten einen rechtswidrigen Vermögensvorteil zu verschaffen, das Vermögen eines anderen dadurch beschädigt, daß er durch Vorspiegelung falscher oder durch ...

#### ragie — Top 3
- **[Judge=3]** `StGB_263_Betrug.md` — Direkt relevant zur Bereicherungsabsicht beim Betrug
  > StGB_263_Betrug.md 186 II. Bereicherungsabsicht. Die Tat muss subjektiv auf die Erlangung eines rechtswidrigen Vermögensvorteils für den Täuschenden oder einen Dritten gerichtet sein. Vermögensvorteil...
- **[Judge=3]** `StGB_263_Betrug.md` — Direkt relevant zur Bereicherungsabsicht beim Betrug
  > StGB_263_Betrug.md 183–185 Diese Rspr. setzt einerseits konkrete Gefährdung und (endgültigen) Schadens- erfolg gleich (vgl. BGHSt 48, 331 (347)); andererseits sieht sie die Kenntnis der Gefahr nur als...
- **[Judge=2]** `StGB_Kommentar.md` — Erwähnt Bereicherungsabsicht beim Betrug, aber oberflächlich
  > StGB_Kommentar.md II. Tatbestandsmerkmale unechten Unterlassens. Für unechte Unterlassungsdelikte hat der GrSen (BGHSt 16, 155) entschieden, dass nur die Umstände, welche die Rechtspflicht begründen (...

### q09 — alltagssprache

**Query:** Hat der Angeklagte die Kunden über das Internet betrogen?

**Kontext:** Abstrakte Frage zu Internetbetrug, sucht Taeuschungshandlung + Schaden

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours | 1.00 | 100% | 100% | 3 | 5.4s |
| ragie | 0.99 | 100% | 100% | 3 | 2.7s |

#### ours — Top 3
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 176` — Direkter Bezug zu Betrug: subjektiver Tatbestand, Vorsatzelemente
  > D. Subjektiver Tatbestand. § 263 setzt Vorsatz voraus; darüber hinaus ist die Absicht rechtswidriger Bereicherung erforderlich.   I. Vorsatz. 1. Täuschungsvorsatz. Der Vorsatz (bedingter Vorsatz genüg...
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 87` — Direkt relevant: Betrug Tatbestandsmerkmale Täuschung Kausalität Schaden
  > 87 5. Kausalität. Für die Vermögensverfügung muss der täuschungsbedingte Irrtum kausal sein (vgl. BGHSt 24, 257 (260); 24, 386 (389); NStZ 2003, 313 (314 f.); OLG Düsseldorf NJW 1987, 3145); Mitverurs...
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 109` — Direkt relevant: Schadensbegriff bei Betrug nach § 263
  > VI. Schaden. Vermögensschaden ist ein negativer Saldo zwischen dem Wert des Vermögens vor und nach der irrtumsbedingten Vermögensverfügung des Getäuschten (Prinzip der Gesamtsaldierung; stRspr; vgl. B...

#### ragie — Top 3
- **[Judge=3]** `StGB_263_Betrug.md` — Direkt relevant: Internetbetrug, Täuschungshandlungen, konkrete Beispiele
  > StGB_263_Betrug.md Entsprechendes gilt auch für sog. Abofallen im Internet (dazu NJW 2014, 2595; Routenplaner). Dies sind scheinbar unentgeltliche Informationsangebote (Wetterberichte; Routenplaner; B...
- **[Judge=3]** `StGB_263_Betrug.md` — Direkt relevant: Internetbetrug Taeuschungshandlungen und Schaeden
  > StGB_263_Betrug.md In Fällen sog. „Kostenfallen“ im Internet (vgl. dazu Eisele NStZ 2010, 193), bei denen unerfahrene Verbraucher durch (wahre) Versprechen besonders günstiger Angebote zum Abschluss v...
- **[Judge=2]** `StGB_263_Betrug.md` — Behandelt Betrug allgemein, enthält Internetbetrug-Literaturhinweise
  > StGB_263_Betrug.md Fehlvorstellung beim Betrug, GA 2012, 354; Cornelius, Betrug durch verschleierte Kick-Back-Zahlungen bei Immobilienfinanzierungen?, NZWiSt 2012, 259; Cramer, Zur Strafbarkeit von Pr...

### q10 — alltagssprache

**Query:** Wann darf die Polizei bei jemandem zu Hause suchen?

**Kontext:** Durchsuchungsvoraussetzungen, §§ 102 ff. StPO

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours | 0.97 | 70% | 100% | 3 | 5.9s |
| ragie | 0.95 | 83% | 67% | 3 | 2.1s |

#### ours — Top 3
- **[Judge=3]** `§ 102 StPO – Rn. 102` — Beantwortet direkt die Durchsuchungsvoraussetzungen bei Verdächtigen
  > 102 Bei dem, welcher als Täter oder Teilnehmer einer Straftat oder der Datenhehlerei, Begünstigung, Strafvereitelung oder Hehlerei  Köhler    Ermittlungsmaßnahmen  verdächtig ist, kann eine Durchsuchu...
- **[Judge=2]** `§ 102 StPO – Rn. 10` — Behandelt Durchsuchungsvoraussetzungen, aber nicht die grundlegenden Befugnisse
  > II. Auffinden von Beweismitteln. Zu den Beweismitteln (→ § 94 Rn. 4 ff.) gehören auch die nur in § 103 erwähnten Spuren (SK-StPO/Jäger/Wohlers Rn. 21) u. Personen, die zu Beweiszwecken in Augenschein ...
- **[Judge=3]** `§ 102 StPO – Rn. 3` — Direkt relevant: behandelt Durchsuchung von Wohnungen/Räumen
  > **Teilnehmer** nach §§ 25 ff. StGB, nicht die sog. notwendigen Teilnehmer (zum Begriff: Fischer/Fischer StGB Vor § 25 Rn. 7), stehen den Tatverdächtigen gleich. Bei jedem v. ihnen sowie bei den der Be...

#### ragie — Top 3
- **[Judge=3]** `Strafprozessordnung.md` — Direkt relevant zu Durchsuchungsvoraussetzungen nach StPO
  > Strafprozessordnung.md 102 Bei dem, welcher als Täter oder Teilnehmer einer Straftat oder der Datenhehlerei, Begünstigung, Strafvereitelung oder Hehlerei  Köhler  ---  ## Seite 613  Ermittlungsmaßnahm...
- **[Judge=3]** `Strafprozessordnung.md` — Direkt relevant zu Wohnungsdurchsuchungen und deren Voraussetzungen
  > Strafprozessordnung.md 15 E. Raumdurchsuchung bei Ergreifung oder Verfolgung des Beschuldigten (Abs. 2). Wird der Beschuldigte, auch der aus der Strafhaft entflohene Verurteilte (BayObLGSt 2020, 152),...
- **[Judge=0]** `Strafprozessordnung.md` — Behandelt Zeugenaussagen, nicht Durchsuchungsrecht
  > Strafprozessordnung.md Schmitt  ---  ## Seite 917  Hauptverhandlung § 252 StPO  der Wohnungstür geklingelt hat, ihr Mann sei nicht zu Hause (OLG Stuttgart Justiz 1972, 322), nicht aber die Angabe, er ...

### q11 — alltagssprache

**Query:** Was passiert wenn jemand luegt damit er Geld bekommt?

**Kontext:** Laienhafte Umschreibung des Betrugstatbestandes

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours | 0.99 | 100% | 100% | 3 | 6.7s |
| ragie | 0.98 | 83% | 100% | 3 | 2.5s |

#### ours — Top 3
- **[Judge=3]** `§ 263 StGB – I. Vermögensbegriff  – Rn. 263` — Definiert exakt den Betrugstatbestand: Lügen für Geld
  > 263 (1) Wer in der Absicht, sich oder einem Dritten einen rechtswidrigen Vermögensvorteil zu verschaffen, das Vermögen eines anderen dadurch beschädigt, daß er durch Vorspiegelung falscher oder durch ...
- **[Judge=3]** `§ 263 StGB – BT. Zweitundzwanzigster Abschnitt – Rn. 69` — Definiert Betrug und zentrale Tatbestandsmerkmale
  > 69 Anders ist es, wenn der Verfügende seinerseits nur (gutgläubige) Hilfsperson eines bösgläubigen Dritten ist. Hier ist auf den Irrtum des Entscheidungsbefugten abzustellen: Erkennt dieser die Unrich...
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 176` — Direkt relevant - behandelt subjektive Tatbestandsmerkmale des Betrugs
  > D. Subjektiver Tatbestand. § 263 setzt Vorsatz voraus; darüber hinaus ist die Absicht rechtswidriger Bereicherung erforderlich.   I. Vorsatz. 1. Täuschungsvorsatz. Der Vorsatz (bedingter Vorsatz genüg...

#### ragie — Top 3
- **[Judge=3]** `StGB_263_Betrug.md` — Direkt relevant: behandelt Betrug durch Luegen
  > StGB_263_Betrug.md Schwieriger ist die Abgrenzung bei zeitlich gestrecktem Fälligkeitstermin 34 (Mietzins; Ratenzahlungsverpflichtung; Arbeitsentgelt); auch hinsichtlich der Anforderungen an die konkl...
- **[Judge=2]** `StGB_263_Betrug.md` — Behandelt Betrugstatbestand, aber spezielle Anstellungsfälle
  > StGB_263_Betrug.md durch Verschweigen von Vermögensdelikten eines Bauleiters; zw.); NJW 1978, 2042 (Vermögensdelikt bei Einkäufer)). Bei Täuschung über eine frühere MfS-Mitarbeit war ein Schaden nur g...
- **[Judge=3]** `StGB_263_Betrug.md` — Direkt relevant: definiert Betrug durch Täuschung für Vermögensvorteil
  > StGB_263_Betrug.md Betrug  RiStBV 236–238  263 (1) Wer in der Absicht, sich oder einem Dritten einen rechtswidrigen Vermögensvorteil zu verschaffen, das Vermögen eines anderen dadurch beschädigt, daß ...

### q12 — alltagssprache

**Query:** Wann muss jemand ins Gefaengnis waehrend die Tat noch nicht bewiesen ist?

**Kontext:** Untersuchungshaft, §§ 112 ff. StPO

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours | 0.99 | 100% | 100% | 3 | 6.2s |
| ragie | 0.84 | 56% | 67% | 3 | 2.7s |

#### ours — Top 3
- **[Judge=3]** `§ 112 StPO – Rn. 112` — Direkt relevant: regelt Untersuchungshaft bei unbewiesen Straftaten
  > 112 (1) ¹ Die Untersuchungshaft darf gegen den Beschuldigten angeordnet werden, wenn er der Tat dringend verdächtig ist und ein Haftgrund besteht. ² Sie darf nicht angeordnet werden, wenn sie zu der B...
- **[Judge=3]** `§ 112 StPO – Rn. 112` — Direkt relevant: Voraussetzungen Untersuchungshaft, dringender Tatverdacht
  > Haftunfähigkeit des Beschuldigten schließt den Erlass des Haftbefehls nicht aus, sondern hindert nur seinen Vollzug (OLG Düsseldorf JZ 1984, 248; OLG Frankfurt a.M. NJW 1968, 2302; OLG Nürnberg OLGSt ...
- **[Judge=3]** `§ 112 StPO – III. Flucht (Abs – Rn. 23` — Behandelt direkt Haftgruende der Untersuchungshaft
  > Bei einer besonders hohen Straferwartung braucht daher nur geprüft zu werden, ob Umstände vorhanden sind, die die hieraus herzuleitende Fluchtgefahr ausräumen können (KG StV 1996, 383; OLG München Str...

#### ragie — Top 3
- **[Judge=3]** `Strafprozessordnung.md` — Direkt relevant: erklärt Untersuchungshaft vor Urteil
  > Strafprozessordnung.md A. UHaft. Die UHaft nach §§ 112 ff., §§ 72, 72a JGG, dh die Inhaftierung eines noch nicht (o. noch nkr) verurteilten Beschuldigten, lässt sich mit der Unschuldsvermutung des Art...
- **[Judge=0]** `StGB_Kommentar.md` — Behandelt Vollstreckungsvereitelung, nicht Untersuchungshaft
  > StGB_Kommentar.md Fischer/Lutz  1941  ---  ## Seite 682  § 258  BT. Einundzwanzigster Abschnitt.  über für die Bewertung maßgebliche Umstände bewusst unterdrückt oder verschweigt. Dasselbe gilt entspr...
- **[Judge=2]** `Strafprozessordnung.md` — Behandelt Untersuchungshaft-Voraussetzungen, aber nicht allgemeine Frage
  > Strafprozessordnung.md 2 Freiheitsstrafe iSv Abs. 1 ist auch der Strafarrest nach § 9 WStG, nicht aber der Jugendarrest nach § 16 JGG (Löwe/Rosenberg/Hilger Rn. 3), auch wenn dieser neben Jugendstrafe...

### q13 — stpo-prozess

**Query:** Welche Voraussetzungen hat die Untersuchungshaft wegen Fluchtgefahr?

**Kontext:** § 112 Abs. 2 Nr. 2 StPO Fluchtgefahr

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours | 0.98 | 80% | 100% | 3 | 5.8s |
| ragie | 0.93 | 90% | 100% | 2 | 2.7s |

#### ours — Top 3
- **[Judge=3]** `§ 112 StPO – Rn. 112` — Enthaelt direkt die Fluchtgefahr-Voraussetzungen nach § 112 Abs. 2 Nr. 2 StPO
  > 112 (1) ¹ Die Untersuchungshaft darf gegen den Beschuldigten angeordnet werden, wenn er der Tat dringend verdächtig ist und ein Haftgrund besteht. ² Sie darf nicht angeordnet werden, wenn sie zu der B...
- **[Judge=3]** `§ 112 StPO – III. Flucht (Abs – Rn. 17 (Teil 1)` — Direkt relevant: definiert Fluchtgefahr nach § 112 Abs. 2 Nr. 2 StPO
  > 17 IV. Fluchtgefahr (Abs. 2 Nr. 2). Fluchtgefahr (Abs. 2 Nr. 2) besteht, wenn die Würdigung der Umstände des Falles es wahrscheinlicher macht, dass sich der Beschuldigte dem Strafverfahren entziehen, ...
- **[Judge=3]** `§ 112 StPO – III. Flucht (Abs – Rn. 16` — Direkte Behandlung von Fluchtgefahr nach § 112 Abs. 2 Nr. 2
  > 16 Bei Ergreifung des Beschuldigten aufgrund des nach Abs. 2 Nr. 1 erlassenen Haftbefehls entfällt der Haftgrund der Flucht. In der Regel wird die vorherige Flucht aber die Aufrechterhaltung des Haftb...

#### ragie — Top 3
- **[Judge=2]** `Strafprozessordnung.md` — Behandelt Fluchtgefahr-Beschränkungen bei leichteren Taten
  > Strafprozessordnung.md ## Untersuchungshaft bei leichteren Taten  113 (1) Ist die Tat nur mit Freiheitsstrafe bis zu sechs Monaten oder mit Geldstrafe bis zu einhundertachtzig Tagessätzen bedroht, so ...
- **[Judge=3]** `Strafprozessordnung.md` — Direkt relevante Konkretisierung der Fluchtgefahr-Voraussetzungen
  > Strafprozessordnung.md Fluchtgefahr begründen idR auffälliger Wohnungs- o. Arbeitsplatzwechsel, Verwendung falscher Namen o. Papiere, Flucht in einem früheren Verf. o. Verfahrensabschnitt u. Zugehörig...
- **[Judge=3]** `Strafprozessordnung.md` — Behandelt direkt Fluchtgefahr-Voraussetzungen bei § 112 StPO
  > Strafprozessordnung.md Schmitt  ---  ## Seite 728  StPO § 112  Erstes Buch. Neunter Abschnitt  Böhm NStZ 2001, 635). Die realistische Möglichkeit einer Unterbringung nach § 63 StGB kann die Annahme v....

### q14 — stpo-prozess

**Query:** Wie lange darf die Untersuchungshaft maximal dauern?

**Kontext:** § 121 StPO Sechs-Monats-Grenze, Haftpruefung OLG

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours | 0.98 | 90% | 100% | 3 | 5.8s |
| ragie | 1.00 | 100% | 100% | 3 | 3.3s |

#### ours — Top 3
- **[Judge=3]** `§ 121 StPO – Rn. 1` — Behandelt direkt maximale Dauer der Untersuchungshaft
  > Eine absolute Höchstgrenze für die Dauer v. UHaft sieht weder die StPO noch die EMRK vor (EGMR EuGRZ 1993, 384). Es kommt auf eine Abwägung aller Umstände des Einzelfalls an. Eine ein Jahr übersteigen...
- **[Judge=3]** `§ 121 StPO – Rn. 121` — Beantwortet direkt die Sechs-Monats-Grenze der Untersuchungshaft
  > 121 (1) Solange kein Urteil ergangen ist, das auf Freiheitsstrafe oder eine freiheitsentziehende Maßregel der Besserung und Sicherung erkennt, darf der Vollzug der Untersuchungshaft wegen derselben Ta...
- **[Judge=3]** `§ 121 StPO – Rn. 8 (Teil 2)` — Direkt relevant: behandelt § 121 StPO Sechs-Monats-Grenze
  > 1 ist allein der vollzogene Haftbefehl (BGH BeckRS 2024, 29978). Nur wegen derselben Tat ist die Dauer der UHaft bis zum Urt. auf 6 Monate begrenzt. Der Begriff „derselben Tat“ muss weit ausgelegt wer...

#### ragie — Top 3
- **[Judge=3]** `Strafprozessordnung.md` — Direkt zur Sechsmonats-Grenze und maximaler UHaft-Dauer
  > Strafprozessordnung.md die 6 Monate überschritten werden (Abs. 2), eine UHaft v. mehr als 1 Jahr bis zum Beginn der HV kann nur in ganz bes. Ausnahmefällen gerechtfertigt sein (BVerfG NJW 2018, 2948; ...
- **[Judge=3]** `Strafprozessordnung.md` — Direkt relevant: § 121 StPO Sechs-Monats-Grenze detailliert erklärt
  > Strafprozessordnung.md Der Haftbefehl wird gegenstandslos (BVerfGE 9, 160; KG NStZ 2012, 230; OLG Düsseldorf Rpfleger 1984, 73; OLG Hamm StraFo 2002, 100; OLG Stuttgart Justiz 1984, 213). Dies soll we...
- **[Judge=3]** `Strafprozessordnung.md` — Direkte Antwort zu maximaler Dauer der Untersuchungshaft
  > Strafprozessordnung.md Die zeitliche Begrenzung der UHaft nach Abs. 1 gilt nicht, wenn der Haftbefehl nach § 230 Abs. 2 (→ § 230 Rn. 10), § 236 oder § 329 Abs. 4 S. 1 (→ § 329 Rn. 45) ergangen ist, au...

### q15 — stpo-prozess

**Query:** Was regelt § 136 StPO zur Beschuldigtenvernehmung?

**Kontext:** Belehrungspflichten, Recht auf Verteidiger

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours | 0.00 | 0% | 0% | 0 | 4.8s |
| ragie | 0.93 | 75% | 100% | 2 | 3.8s |

#### ours — Top 3

#### ragie — Top 3
- **[Judge=2]** `Strafprozessordnung.md` — Thematisch relevant, behandelt Beschuldigtenvernehmung und Belehrungspflichten
  > Strafprozessordnung.md 77a Der Verfolgungsbehörde steht insoweit ein – objektiv zu bestimmender – Beurteilungsspielraum zu (BGHSt 38, 214 (228); BGHSt 64, 89; StraFo 2005, 27; erg. → StPO § 163a Rn. 4...
- **[Judge=2]** `Strafprozessordnung.md` — Behandelt Vernehmungsverfahren, aber nicht § 136 direkt
  > Strafprozessordnung.md (2) In der Ladung zu einer richterlichen oder staatsanwaltschaftlichen Vernehmung sollen Zwangsmaßnahmen für den Fall des Ausbleibens nur angedroht werden, wenn sie gegen den un...
- **[Judge=3]** `Strafprozessordnung.md` — Direkt relevant zu § 136 StPO Belehrungspflichten
  > Strafprozessordnung.md 45. Form der Vernehmung und Niederschrift. (1) ¹ Die Belehrung des Beschuldigten vor seiner Vernehmung nach § 136 Absatz 1, § 163a Absatz 3 Satz 2 StPO ist aktenkundig zu machen...

### q16 — cross-reference

**Query:** Worin unterscheidet sich Betrug von Unterschlagung?

**Kontext:** Abgrenzung § 263 vs § 246 StGB

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours | 0.90 | 90% | 100% | 2 | 5.7s |
| ragie | 0.94 | 50% | 33% | 2 | 3.9s |

#### ours — Top 3
- **[Judge=2]** `§ 263 StGB – BT. Zweitundzwanzigster Abschnitt – Rn. 69` — Betrug-Spezifika erklärt, aber keine direkte Abgrenzung zur Unterschlagung
  > 69 Anders ist es, wenn der Verfügende seinerseits nur (gutgläubige) Hilfsperson eines bösgläubigen Dritten ist. Hier ist auf den Irrtum des Entscheidungsbefugten abzustellen: Erkennt dieser die Unrich...
- **[Judge=2]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 76` — Behandelt Betrug, aber nicht Abgrenzung zu Unterschlagung
  > 4. Dreiecksbetrug. Da die Getäuschte und die verfügende, nicht aber die verfügende und die geschädigte Person identisch sein müssen, ist der Tatbestand des § 263 nur erfüllt, wenn die Vermögensverfügu...
- **[Judge=2]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 76` — Betrug-Verfügungsmerkmal relevant, aber keine direkte Abgrenzung Unterschlagung
  > 76 3. Unmittelbarkeit der Verfügung. Neben der Freiwilligkeit ist das Merkmal der Unmittelbarkeit nach stRspr und hM das wichtigste Kriterium zur Beschränkung der § 263 unterfallenden Selbstschädigung...

#### ragie — Top 3
- **[Judge=2]** `StGB_Kommentar.md` — Behandelt Abgrenzung Betrug/Unterschlagung, aber ohne inhaltliche Erklärung
  > StGB_Kommentar.md 3. Einzelfälle. a) Zulässig sind Wahlfeststellungen nach hM (umfassende Dokumentation bei Wolter (→ Rn. 38) S. 174 ff.) zwischen:  Diebstahl und Hehlerei (BGHSt 1, 302; 12, 386; 15, ...
- **[Judge=1]** `StGB_Kommentar.md` — Inhaltsverzeichnis, aber keine inhaltliche Abgrenzung
  > StGB_Kommentar.md # Neunzehnter Abschnitt. Diebstahl und Unterschlagung  Diebstahl ... § 242 Besonders schwerer Fall des Diebstahls ... § 243 Diebstahl mit Waffen; Bandendiebstahl; Wohnungseinbruchdie...
- **[Judge=1]** `StGB_Kommentar.md` — Nur kurze Erwähnung der Abgrenzung, keine Details
  > StGB_Kommentar.md Fischer  ---  ## Seite 93  § 1  AT. Erster Abschnitt. Erster Titel.  60; anderseits BGHSt 20, 104; Einschränkungen in OLG Karlsruhe NJW 1976, 902; offen gelassen in BGH NStZ 1985, 12...

### q17 — cross-reference

**Query:** Was sind die Unterschiede zwischen Diebstahl und Raub?

**Kontext:** § 242 vs § 249 StGB — Abgrenzung durch Gewalt/Drohung

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours | 0.00 | 0% | 0% | 0 | 4.5s |
| ragie | 0.99 | 86% | 100% | 3 | 2.7s |

#### ours — Top 3

#### ragie — Top 3
- **[Judge=3]** `StGB_Kommentar.md` — Direkte Abgrenzung Diebstahl vs Raub, systematische Stellung
  > StGB_Kommentar.md Rechtsprechungsübersichten: Maier/Percic NStZ-RR 2010, 129; Maier NStZ-RR 2012, 297; 2013, 329 (364); 2015, 33; 2017, 1, 2018, 33; 2025, 129; 2025, 161.  2 B. Systematische Stellung....
- **[Judge=3]** `StGB_Kommentar.md` — Behandelt direkt Konkurrenzen zwischen Diebstahl und Raub
  > StGB_Kommentar.md J. Konkurrenzen. Gesetzeseinheit liegt zwischen § 249 und §§ 242, 243, 244, 244a vor, die von § 249 verdrängt werden (vgl. BGHSt 20, 235 (237 f.); NStZ-RR 2005, 202 (203)). Entsprech...
- **[Judge=3]** `StGB_Kommentar.md` — Zentrale Tatbestandsmerkmale des Raubs dargestellt
  > StGB_Kommentar.md E. Strafantrag. Abs. 3 regelt ein Antragserfordernis entspr. §§ 247, 248a (vgl. → § 247 Rn. 1 ff., → § 248a Rn. 1 ff.).  F. Abs. 4. Nach Abs. 4 wird milder bestraft, wer ohne Zueignu...

### q18 — cross-reference

**Query:** Wann wird Betrug zu Computerbetrug und umgekehrt?

**Kontext:** § 263 vs § 263a StGB — Abgrenzung bei elektronischer Datenverarbeitung

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours | 0.96 | 10% | 33% | 3 | 7.4s |
| ragie | 0.87 | 80% | 67% | 1 | 3.0s |

#### ours — Top 3
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 58` — Direkte Abgrenzung § 263/263a bei automatisierten Verfahren
  > 58 Im Geschäftsverkehr wird sich, wer die Berechtigung eines Leistungsverlangens oder -auftrags nicht zu prüfen hat, hierüber idR auch keine (richtigen oder falschen) Gedanken machen (NStZ 1997, 281; ...
- **[Judge=1]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 62` — Behandelt nur Betrug, nicht Abgrenzung zu Computerbetrug
  > Die Kausalität der Täuschung für den Irrtum und dessen Kausalität für die Vermögensverfügung müssen im Einzelfall festgestellt sein. Mitverursachung reicht aus. Dabei darf das Gericht auch bei Serien-...
- **[Judge=0]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 114` — Behandelt Vermögensschaden bei § 263, nicht Abgrenzung § 263a
  > 114 a) Quantifizierbarkeit der Vermögensminderung. Die Vermögensminderung muss quantifizierbar sein (RGSt 16, 4; 44, 249; BGHSt 16, 321). Grds. nicht ausreichend ist eine nicht quantifizierbare Einbuß...

#### ragie — Top 3
- **[Judge=1]** `StGB_Kommentar.md` — Behandelt § 263a, aber nicht die Abgrenzung
  > StGB_Kommentar.md Fischer/Lutz  ---  ## Seite 799  Betrug und Untreue § 263a  IV. Subjektiver Tatbestand. In subjektiver Hinsicht ist (mindestens bedingter) Vorsatz hinsichtlich der Merkmale des Compu...
- **[Judge=3]** `StGB_263_Betrug.md` — Direkt relevant: behandelt explizit Betrug vs Computerbetrug
  > StGB_263_Betrug.md FS Samson, 2010, 455; Ruha, Neue Wege für das Betrugsstrafrecht, FS Rissing-van Saan, 2011, 567; Satzger, Der Submissionsbetrug, 1994; Scheinfeld, Betrug durch unternehmerisches Wer...
- **[Judge=3]** `StGB_Kommentar.md` — Direkter Gesetzeswortlaut zu § 263a StGB Computerbetrug
  > StGB_Kommentar.md ## Computerbetrug  263a (1) Wer in der Absicht, sich oder einem Dritten einen rechtswidrigen Vermögensvorteil zu verschaffen, das Vermögen eines anderen dadurch beschädigt, daß er da...