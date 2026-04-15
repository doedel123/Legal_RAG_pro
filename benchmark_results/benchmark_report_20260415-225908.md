# RAG Benchmark Report

_Generiert: 2026-04-15T22:59:08_


- Queries: **18**
- Top-K: **10**
- Systeme: ours, ragie

## Gesamtvergleich

| Metrik | ours | ragie |
|--------|--------|--------|
| nDCG@10 | 0.937 | 0.944 |
| Relevance@10 | 77.8% | 80.4% |
| Relevance@3 | 88.9% | 83.3% |
| Top-1-Score | 2.50 | 2.56 |
| Mean-Score | 2.24 | 2.37 |
| Latenz (s) | 6.08 | 2.53 |

## Nach Kategorie


### alltagssprache

| Metrik | ours | ragie |
|--------|--------|--------|
| nDCG@10 | 0.969 | 0.942 |
| Relevance@10 | 95.0% | 76.4% |
| Relevance@3 | 100.0% | 83.3% |

### cross-reference

| Metrik | ours | ragie |
|--------|--------|--------|
| nDCG@10 | 0.828 | 0.922 |
| Relevance@10 | 53.3% | 64.8% |
| Relevance@3 | 66.7% | 77.8% |

### exakte-paragraphen

| Metrik | ours | ragie |
|--------|--------|--------|
| nDCG@10 | 0.986 | 0.900 |
| Relevance@10 | 85.0% | 78.3% |
| Relevance@3 | 100.0% | 66.7% |

### konzept

| Metrik | ours | ragie |
|--------|--------|--------|
| nDCG@10 | 0.926 | 0.982 |
| Relevance@10 | 75.0% | 91.7% |
| Relevance@3 | 75.0% | 91.7% |

### stpo-prozess

| Metrik | ours | ragie |
|--------|--------|--------|
| nDCG@10 | 0.951 | 0.977 |
| Relevance@10 | 73.3% | 89.2% |
| Relevance@3 | 100.0% | 100.0% |

## Detail pro Query


### q01 — exakte-paragraphen

**Query:** Welche Voraussetzungen hat der gewerbsmaessige Bandenbetrug nach § 263 Abs. 5 StGB?

**Kontext:** Qualifikationstatbestand des Bandenbetrugs im Fischer-Kommentar

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours | 1.00 | 80% | 100% | 3 | 7.0s |
| ragie | 0.97 | 100% | 100% | 3 | 2.4s |

#### ours — Top 3
- **[Judge=3]** `§ 263 StGB – BT. Zweriindzwanzigster Abschnitt – Rn. 225` — Erklärt direkt Voraussetzungen des § 263 Abs. 5
  > IV. Qualifikation (Abs. 5). Abs. 5 enthält einen Qualifikationstatbestand, der die Tat in Fällen kumulativ gewerbs- und bandenmäßiger Begehung zum Verbrechen macht. Die Qualifikation ist in die Urteil...
- **[Judge=3]** `§ 263 StGB – BT. Zweijundzwanzigster Abschnitt – Rn. 213` — Direkte Behandlung der Qualifikationstatbestände nach § 263 Abs. 5
  > 213 Sind beide Varianten erfüllt, ist eine Qualifikation nach Abs. 5 gegeben. Die Abgrenzung des Abs. 3 Nr. 1 zum Verbrechen nach Abs. 5 ist in Fällen bandenmäßiger Begehung schwierig, denn eine auf f...
- **[Judge=3]** `§ 263 StGB – BT. Zweijundzwanzigster Abschnitt – Rn. 212` — Direkt relevant: behandelt bandenmäßigen Betrug § 263
  > 212 Der Begriff der Urkundenfälschung ist weit zu fassen; er umfasst neben Taten nach § 267 auch solche nach §§ 268–281 (LK-StGB/Kubiciel/Tiedemann Rn. 297; NK-StGB/Kindhäuser/Hoven Rn. 392). Entsprec...

#### ragie — Top 3
- **[Judge=3]** `StGB_263_Betrug.md` — Direkt zu § 263 Abs. 5 Bandenbetrug
  > StGB_263_Betrug.md 213 Sind beide Varianten erfüllt, ist eine Qualifikation nach Abs. 5 gegeben. Die Abgrenzung des Abs. 3 Nr. 1 zum Verbrechen nach Abs. 5 ist in Fällen bandenmäßiger Begehung schwier...
- **[Judge=2]** `StGB_Kommentar.md` — Behandelt Bandenbetrug, aber fehlende Gewerbsmäßigkeitsmerkmale
  > StGB_Kommentar.md 213 Sind beide Varianten erfüllt, ist eine Qualifikation nach Abs. 5 gegeben. Die Abgrenzung des Abs. 3 Nr. 1 zum Verbrechen nach Abs. 5 ist in Fällen bandenmäßiger Begehung schwieri...
- **[Judge=3]** `StGB_263_Betrug.md` — Direkt relevante Erläuterung der Qualifikationsvoraussetzungen nach Abs. 5
  > StGB_263_Betrug.md IV. Qualifikation (Abs. 5). Abs. 5 enthält einen Qualifikationstatbestand, der die Tat in Fällen kumulativ gewerbs- und bandenmäßiger Begehung zum Verbrechen macht. Die Qualifikatio...

### q02 — exakte-paragraphen

**Query:** Was regelt § 112 StPO zur Untersuchungshaft?

**Kontext:** Anordnungsvoraussetzungen der U-Haft (dringender Tatverdacht, Haftgrund) im Schmitt/Koehler

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours | 0.99 | 100% | 100% | 3 | 5.3s |
| ragie | 0.96 | 75% | 67% | 3 | 1.8s |

#### ours — Top 3
- **[Judge=3]** `§ 112 StPO – Rn. 112` — Beantwortet direkt § 112 StPO Anordnungsvoraussetzungen
  > 112 (1) ¹ Die Untersuchungshaft darf gegen den Beschuldigten angeordnet werden, wenn er der Tat dringend verdächtig ist und ein Haftgrund besteht. ² Sie darf nicht angeordnet werden, wenn sie zu der B...
- **[Judge=3]** `§ 112 StPO – Rn. 112` — Direkte Erklärung der Haftbefehl-Voraussetzungen nach § 112 StPO
  > Haftunfähigkeit des Beschuldigten schließt den Erlass des Haftbefehls nicht aus, sondern hindert nur seinen Vollzug (OLG Düsseldorf JZ 1984, 248; OLG Frankfurt a.M. NJW 1968, 2302; OLG Nürnberg OLGSt ...
- **[Judge=3]** `§ 112 StPO – III. Flucht (Abs – Rn. 23` — Behandelt direkt Haftgruende nach § 112 StPO
  > Bei einer besonders hohen Straferwartung braucht daher nur geprüft zu werden, ob Umstände vorhanden sind, die die hieraus herzuleitende Fluchtgefahr ausräumen können (KG StV 1996, 383; OLG München Str...

#### ragie — Top 3
- **[Judge=3]** `Strafprozessordnung.md` — Direkter Paragraphbeginn mit Haftvoraussetzungen und Haftgründen
  > Strafprozessordnung.md Werden mehrere Haftbefehle in verschiedenen Sachen erlassen, so kann nur einer v. ihnen vollzogen werden. Eine „Doppelhaft“ ist ausgeschlossen (Münchhalffen/Gatzweiler Untersuch...
- **[Judge=3]** `Strafprozessordnung.md` — Direkt relevant: behandelt § 112 StPO Anordnungsvoraussetzungen
  > Strafprozessordnung.md a) der dringende Tatverdacht, b) der Haftgrund  ergeben.  ---  ## Seite 2435  Anh. 3 RiStBV  RL für das Strafverfahren und das Bußgeldverfahren  (2) Wenn die Anwendung des § 112...
- **[Judge=1]** `Strafprozessordnung.md` — Jugendstrafrecht, nicht allgemeines Strafverfahren § 112 StPO
  > Strafprozessordnung.md § 72 Untersuchungshaft. (1) ¹ Untersuchungshaft darf nur verhängt und vollstreckt werden, wenn ihr Zweck nicht durch eine vorläufige Anordnung über die Erziehung oder durch ande...

### q03 — exakte-paragraphen

**Query:** Welche Haftgruende nennt § 112 Abs. 2 StPO?

**Kontext:** Fluchtgefahr, Verdunkelungsgefahr, Flucht — im StPO-Kommentar

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours | 0.98 | 90% | 100% | 3 | 4.6s |
| ragie | 0.86 | 71% | 67% | 2 | 2.5s |

#### ours — Top 3
- **[Judge=3]** `§ 112 StPO – Rn. 112` — Nennt exakt alle Haftgründe des § 112 Abs. 2 StPO
  > 112 (1) ¹ Die Untersuchungshaft darf gegen den Beschuldigten angeordnet werden, wenn er der Tat dringend verdächtig ist und ein Haftgrund besteht. ² Sie darf nicht angeordnet werden, wenn sie zu der B...
- **[Judge=3]** `§ 112 StPO – III. Flucht (Abs – Rn. 23` — Behandelt direkt die Haftgruende aus § 112 Abs. 2 StPO
  > Bei einer besonders hohen Straferwartung braucht daher nur geprüft zu werden, ob Umstände vorhanden sind, die die hieraus herzuleitende Fluchtgefahr ausräumen können (KG StV 1996, 383; OLG München Str...
- **[Judge=2]** `§ 112 StPO – III. Flucht (Abs – Rn. 32 (Teil 2)` — Behandelt Verdunkelungsgefahr, aber nicht die anderen Haftgruende
  > Wenn die Verdunkelungshandlungen nicht geeignet sind, die Ermittlung der Wahrheit zu erschweren, darf UHaft nicht angeordnet werden. Der Haftgrund liegt daher nicht vor, wenn der Sachverhalt schon in ...

#### ragie — Top 3
- **[Judge=2]** `Strafprozessordnung.md` — Behandelt Haftgruende aber nicht § 112 Abs. 2
  > Strafprozessordnung.md 38 Die Vorschr. begründet bei dieser Auslegung weder eine Vermutung der Haftgründe (aM OLG Düsseldorf MDR 1983, 152; offenbar auch OLG Bremen StV 1983, 288), noch findet eine „U...
- **[Judge=1]** `Strafprozessordnung.md` — Erwähnt § 112 Abs. 2, aber nennt nicht konkrete Haftgründe
  > Strafprozessordnung.md (3) ¹ Hinsichtlich der Möglichkeit und gegebenenfalls Pflicht zur Aufzeichnung der Vernehmung des Beschuldigten in Bild und Ton sind § 136 Absatz 4 StPO bzw. § 70c Absatz 2 Satz...
- **[Judge=2]** `Strafprozessordnung.md` — Behandelt Haftgründe allgemein, nicht spezifisch § 112 Abs. 2
  > Strafprozessordnung.md Soweit die Staatssicherheit gefährdet wurde, kann v. der Begründung des dringenden Tatverdachts abgesehen werden (dazu Creifelds NJW 1965, 949); das muss in dem Haftbefehl zum A...

### q04 — exakte-paragraphen

**Query:** Was regelt § 102 StPO zur Durchsuchung beim Beschuldigten?

**Kontext:** Durchsuchungsvoraussetzungen beim Verdaechtigen

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours | 0.98 | 70% | 100% | 3 | 5.2s |
| ragie | 0.82 | 67% | 33% | 1 | 2.1s |

#### ours — Top 3
- **[Judge=3]** `§ 102 StPO – Rn. 102` — Direkt relevant, behandelt genau § 102 StPO Durchsuchungsvoraussetzungen
  > 102 Bei dem, welcher als Täter oder Teilnehmer einer Straftat oder der Datenhehlerei, Begünstigung, Strafvereitelung oder Hehlerei  Köhler    Ermittlungsmaßnahmen  verdächtig ist, kann eine Durchsuchu...
- **[Judge=3]** `§ 102 StPO – Rn. 10` — Direkt relevant: behandelt § 102 StPO Durchsuchungsgegenstände
  > 10 III. Sachen. Sachen sind Kleidungsstücke, die der Verdächtige bei sich führt, ohne sie zu tragen, u. seine sonstige bewegliche Habe, gleichgültig, ob sie sich in seinem Umkreis, zB in Gepäckstücken...
- **[Judge=2]** `§ 102 StPO – Rn. 10` — Behandelt Durchsuchungsvoraussetzungen, aber nicht spezifisch § 102
  > II. Auffinden von Beweismitteln. Zu den Beweismitteln (→ § 94 Rn. 4 ff.) gehören auch die nur in § 103 erwähnten Spuren (SK-StPO/Jäger/Wohlers Rn. 21) u. Personen, die zu Beweiszwecken in Augenschein ...

#### ragie — Top 3
- **[Judge=1]** `Strafprozessordnung.md` — Behandelt § 103 StPO, nicht § 102 StPO
  > Strafprozessordnung.md 3 B. Durchsuchungsgegenstände. Durchsuchungsgegenstände können die Wohnung u. Räume des Unverdächtigen (→ § 102 Rn. 7) sowie seine Person (→ § 102 Rn. 9) u. die ihm gehörenden S...
- **[Judge=3]** `Strafprozessordnung.md` — Direkt relevanter Gesetzestext zu § 102 StPO
  > Strafprozessordnung.md Durchsuchung bei Beschuldigten RiStBV 73a  102 Bei dem, welcher als Täter oder Teilnehmer einer Straftat oder der Datenhehlerei, Begünstigung, Strafvereitelung oder Hehlerei  Kö...
- **[Judge=1]** `Strafprozessordnung.md` — § 103 behandelt, nicht § 102 beim Beschuldigten
  > Strafprozessordnung.md 2 Auch Dienstgebäude u. -räume v. Behörden dürfen nur durchsucht werden (vgl. § 105 Abs. 3 S. 3), wenn dies erforderlich, um den Beschuldigten zu ergreifen oder Beweismittel auf...

### q05 — konzept

**Query:** Wann liegt eine konkludente Taeuschung im Sinne des § 263 StGB vor?

**Kontext:** Taeuschungshandlung durch schluessiges Verhalten

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours | 0.84 | 60% | 67% | 1 | 6.0s |
| ragie | 0.95 | 89% | 67% | 3 | 4.5s |

#### ours — Top 3
- **[Judge=1]** `§ 263 StGB – I. Vermögensbegriff  – Rn. 263` — Gesetzestext ohne konkludente Taeuschung-Erklaerung
  > 263 (1) Wer in der Absicht, sich oder einem Dritten einen rechtswidrigen Vermögensvorteil zu verschaffen, das Vermögen eines anderen dadurch beschädigt, daß er durch Vorspiegelung falscher oder durch ...
- **[Judge=2]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 263 (Tei` — Literaturverzeichnis zu Betrug, enthält relevante Quellen
  > Heghmanns, Strafbarkeit des „Phishing“ von Bankkontendaten und ihrer Verwertung, wistra 2007, 167; Hilgendorf, Tatsachenaussagen u. Werturteile im Strafrecht, 1998; Hillenkamp, Zum Schutz „deliktische...
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 14` — Behandelt direkt konkludente Taeuschung bei § 263
  > Rspr. und hM bejahen darüber hinaus aber die Möglichkeit einer Täuschung durch Unterlassen auch ohne Erklärung gegenüber dem Irrenden (→ Rn. 38; vgl. BGHSt 39, 392 (398); BayObLG NJW 1987, 1654 (mAnm ...

#### ragie — Top 3
- **[Judge=3]** `StGB_263_Betrug.md` — Definiert direkt konkludente Taeuschung nach § 263
  > StGB_263_Betrug.md 21 2. Konkludente Erklärungen. Auch durch eine schlüssige Handlung (konkludente Erklärung) kann vorspiegelt werden. Eine solche konkludente Erklärung durch aktives Tun ist von einer...
- **[Judge=1]** `StGB_Kommentar.md` — Erwähnt konkludente Täuschung, aber bei anderem Sachverhalt
  > StGB_Kommentar.md E. Vollendung, Versuch. Die Tat ist mit dem Eintritt des Schadens vollendet und idR auch beendet iSv § 78a. Der Versuch ist nicht strafbar. Die (vom Gesetzgeber des 2. WiKG verworfen...
- **[Judge=3]** `StGB_263_Betrug.md` — Direkt relevant, definiert konkludente Taeuschung mit Beispielen
  > StGB_263_Betrug.md 22 Sowohl ausdrücklichen Erklärungen als auch tatsächlichen Handeln kann ein konkludenter Erklärungswert zukommen. Aus der bloßen Feststellung eines Irrtums kann aber nicht schon au...

### q06 — konzept

**Query:** Was ist eine Vermoegensverfuegung und welche Anforderungen stellt die Rechtsprechung?

**Kontext:** Tatbestandsmerkmal der Vermoegensverfuegung beim Betrug

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours | 0.91 | 70% | 33% | 3 | 6.2s |
| ragie | 1.00 | 100% | 100% | 3 | 1.8s |

#### ours — Top 3
- **[Judge=3]** `§ 263 StGB – BT. Zweitundzwanzigster Abschnitt – Rn. 69` — Definiert Vermoegensverfuegung und nennt zentrale Rechtsprechungsanforderungen
  > 69 Anders ist es, wenn der Verfügende seinerseits nur (gutgläubige) Hilfsperson eines bösgläubigen Dritten ist. Hier ist auf den Irrtum des Entscheidungsbefugten abzustellen: Erkennt dieser die Unrich...
- **[Judge=1]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 87` — Kausalität bei Vermögensverfügung, nicht deren Definition
  > 87 5. Kausalität. Für die Vermögensverfügung muss der täuschungsbedingte Irrtum kausal sein (vgl. BGHSt 24, 257 (260); 24, 386 (389); NStZ 2003, 313 (314 f.); OLG Düsseldorf NJW 1987, 3145); Mitverurs...
- **[Judge=1]** `§ 263 StGB – I. Vermögensbegriff  – Rn. 263` — Betrug-Paragraph, aber keine Vermoegensverfuegung definiert
  > 263 (1) Wer in der Absicht, sich oder einem Dritten einen rechtswidrigen Vermögensvorteil zu verschaffen, das Vermögen eines anderen dadurch beschädigt, daß er durch Vorspiegelung falscher oder durch ...

#### ragie — Top 3
- **[Judge=3]** `StGB_Kommentar.md` — Direkt relevant: definiert Vermoegensverfuegung mit Rechtsprechungsbeispielen
  > StGB_Kommentar.md a) Einzelfälle. Als Verfügungen sind zB angesehen worden: Veranlassung oder Vornahme einer Überweisung (wistra 1987, 257; NStZ 1999, 558); Herausgabe fremder Sachen: Bewilligung von ...
- **[Judge=3]** `StGB_Kommentar.md` — Direkt relevant: Definition und Rechtsprechung zur Vermoegensverfuegung
  > StGB_Kommentar.md 1. Verfügungshandlung. Die Anzahl möglicher vermögensmindernder Handlungen ist grds. unbeschränkt; sie sind meist den Fallgruppen des Eingehens oder des Erfüllens einer Verbindlichke...
- **[Judge=2]** `StGB_Kommentar.md` — Behandelt Vermögensschaden, nicht Vermögensverfügung selbst
  > StGB_Kommentar.md 113 2. Vermögensminderung. Erforderlich ist eine durch die Vermögensverfügung kausal verursachte Minderung des Vermögenswerts durch den Verlust oder die Wertminderung von Aktiva oder...

### q07 — konzept

**Query:** Was versteht man unter einem Gefaehrdungsschaden beim Betrug?

**Kontext:** Schadensbegriff, schadensgleiche Vermoegensgefaehrdung

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours | 0.96 | 100% | 100% | 3 | 7.5s |
| ragie | 1.00 | 100% | 100% | 3 | 1.8s |

#### ours — Top 3
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 159` — Direkt relevant: definiert Gefaehrdungsschaden beim Betrug
  > 159 b) Voraussetzungen. aa) Ein Gefährdungsschaden ist gegeben, wenn die Wahrscheinlichkeit des endgültigen Verlusts eines Vermögensbestandteils zum Zeitpunkt der täuschungsbedingten Verfügung so groß...
- **[Judge=2]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 109` — Behandelt Schadensbegriff, erwaehnt Gefaehrdungsschaden kurz
  > VI. Schaden. Vermögensschaden ist ein negativer Saldo zwischen dem Wert des Vermögens vor und nach der irrtumsbedingten Vermögensverfügung des Getäuschten (Prinzip der Gesamtsaldierung; stRspr; vgl. B...
- **[Judge=3]** `§ 263 StGB – BT. Zwei undzwanzigster Abschnitt – Rn. 263` — Behandelt direkt Gefährdungsschaden beim Betrug
  > **Rechtsprechungsübersicht:** Scholz, Die Entwicklung des Berufs- und Vertragsarztrechts, medstra 2019, 331; 2021, 349; 2022, 355; 2023, 355; 2024, 351.  Weinrich/Wostry, Der Abrechnungsbetrug in der ...

#### ragie — Top 3
- **[Judge=3]** `StGB_263_Betrug.md` — Definiert direkt Gefährdungsschaden beim Betrug
  > StGB_263_Betrug.md 159 b) Voraussetzungen. aa) Ein Gefährdungsschaden ist gegeben, wenn die Wahrscheinlichkeit des endgültigen Verlusts eines Vermögensbestandteils zum Zeitpunkt der täuschungsbedingte...
- **[Judge=3]** `StGB_263_Betrug.md` — Definiert direkt Gefährdungsschaden beim Betrug
  > StGB_263_Betrug.md 158 Der 3. StS hat in BGHSt 54, 69 (122 ff.) (Anm. Joecks wistra 2010, 179; vgl. → Rn. 8; → Rn. 176) sowohl der Sache nach als auch begrifflich am „Gefährdungsschaden“ festgehalten ...
- **[Judge=3]** `StGB_Kommentar.md` — Definiert Gefährdungsschaden bei Betrug konkret
  > StGB_Kommentar.md Die täuschungsbedingte Herausgabe von EC-Karten, Kreditkarten und weiteren Zugangsdaten zu Bank-Guthaben (PINs, TANs; Passwörter), sei es infolge persönlicher Täuschung oder von „Phi...

### q08 — konzept

**Query:** Wie wird der Vorsatz beim Betrug bestimmt, insbesondere die Bereicherungsabsicht?

**Kontext:** Subjektiver Tatbestand § 263 StGB

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours | 0.99 | 70% | 100% | 3 | 6.0s |
| ragie | 0.98 | 78% | 100% | 3 | 2.0s |

#### ours — Top 3
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 176` — Direkt relevant: Vorsatz bei Betrug detailliert erklaert
  > D. Subjektiver Tatbestand. § 263 setzt Vorsatz voraus; darüber hinaus ist die Absicht rechtswidriger Bereicherung erforderlich.   I. Vorsatz. 1. Täuschungsvorsatz. Der Vorsatz (bedingter Vorsatz genüg...
- **[Judge=3]** `§ 263 StGB – I. Sonstige Vorschriften 239 – Rn. 263 (Teil 1)` — Behandelt direkt Bereicherungsabsicht und subjektiven Tatbestand
  > 3. Einzelne Fallgruppen ... 92 4. Rechtlich missbilligte, sittenwidrige und gesetzeswidrige wirtschaftliche Werte ... 101 VI. Schaden ... 110 1. Grundsätze der Schadensermittlung ... 111 2. Vermögensm...
- **[Judge=2]** `§ 263 StGB – I. Vermögensbegriff  – Rn. 263` — Enthaelt Bereicherungsabsicht, aber keine detaillierte Vorsatzbestimmung
  > 263 (1) Wer in der Absicht, sich oder einem Dritten einen rechtswidrigen Vermögensvorteil zu verschaffen, das Vermögen eines anderen dadurch beschädigt, daß er durch Vorspiegelung falscher oder durch ...

#### ragie — Top 3
- **[Judge=3]** `StGB_263_Betrug.md` — Direkt relevant: Bereicherungsabsicht beim Betrug detailliert erklärt
  > StGB_263_Betrug.md 186 II. Bereicherungsabsicht. Die Tat muss subjektiv auf die Erlangung eines rechtswidrigen Vermögensvorteils für den Täuschenden oder einen Dritten gerichtet sein. Vermögensvorteil...
- **[Judge=3]** `StGB_263_Betrug.md` — Direkter Bezug zur Bereicherungsabsicht beim Betrug
  > StGB_263_Betrug.md 183–185 Diese Rspr. setzt einerseits konkrete Gefährdung und (endgültigen) Schadens- erfolg gleich (vgl. BGHSt 48, 331 (347)); andererseits sieht sie die Kenntnis der Gefahr nur als...
- **[Judge=2]** `StGB_Kommentar.md` — Bereicherungsabsicht beim Betrug explizit erwähnt, aber nur beispielhaft
  > StGB_Kommentar.md II. Tatbestandsmerkmale unechten Unterlassens. Für unechte Unterlassungsdelikte hat der GrSen (BGHSt 16, 155) entschieden, dass nur die Umstände, welche die Rechtspflicht begründen (...

### q09 — alltagssprache

**Query:** Hat der Angeklagte die Kunden über das Internet betrogen?

**Kontext:** Abstrakte Frage zu Internetbetrug, sucht Taeuschungshandlung + Schaden

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours | 0.93 | 100% | 100% | 2 | 5.2s |
| ragie | 0.99 | 100% | 100% | 3 | 2.3s |

#### ours — Top 3
- **[Judge=2]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 186` — Betrugsmerkmale relevant, aber nicht internetspezifisch
  > 186 II. Bereicherungsabsicht. Die Tat muss subjektiv auf die Erlangung eines rechtswidrigen Vermögensvorteils für den Täuschenden oder einen Dritten gerichtet sein. Vermögensvorteil ist die Erhöhung d...
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 109` — Definiert Vermögensschaden bei Betrug - zentral relevant
  > VI. Schaden. Vermögensschaden ist ein negativer Saldo zwischen dem Wert des Vermögens vor und nach der irrtumsbedingten Vermögensverfügung des Getäuschten (Prinzip der Gesamtsaldierung; stRspr; vgl. B...
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 176` — Zentrale Tatbestandsmerkmale des Betrugs nach § 263 StGB
  > D. Subjektiver Tatbestand. § 263 setzt Vorsatz voraus; darüber hinaus ist die Absicht rechtswidriger Bereicherung erforderlich.   I. Vorsatz. 1. Täuschungsvorsatz. Der Vorsatz (bedingter Vorsatz genüg...

#### ragie — Top 3
- **[Judge=3]** `StGB_263_Betrug.md` — Direkte Antwort zu Internetbetrug und Taeuschungshandlungen
  > StGB_263_Betrug.md Entsprechendes gilt auch für sog. Abofallen im Internet (dazu NJW 2014, 2595; Routenplaner). Dies sind scheinbar unentgeltliche Informationsangebote (Wetterberichte; Routenplaner; B...
- **[Judge=3]** `StGB_263_Betrug.md` — Direkt relevant: behandelt Internetbetrug und Täuschungshandlungen
  > StGB_263_Betrug.md In Fällen sog. „Kostenfallen“ im Internet (vgl. dazu Eisele NStZ 2010, 193), bei denen unerfahrene Verbraucher durch (wahre) Versprechen besonders günstiger Angebote zum Abschluss v...
- **[Judge=2]** `StGB_263_Betrug.md` — Behandelt Internetbetrug, aber nur Literaturverweise ohne Tatbestandsmerkmale
  > StGB_263_Betrug.md Fehlvorstellung beim Betrug, GA 2012, 354; Cornelius, Betrug durch verschleierte Kick-Back-Zahlungen bei Immobilienfinanzierungen?, NZWiSt 2012, 259; Cramer, Zur Strafbarkeit von Pr...

### q10 — alltagssprache

**Query:** Wann darf die Polizei bei jemandem zu Hause suchen?

**Kontext:** Durchsuchungsvoraussetzungen, §§ 102 ff. StPO

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours | 0.99 | 80% | 100% | 3 | 5.5s |
| ragie | 0.95 | 83% | 67% | 3 | 1.9s |

#### ours — Top 3
- **[Judge=3]** `§ 102 StPO – Rn. 102` — Definiert zentrale Durchsuchungsvoraussetzungen des § 102 StPO
  > 102 Bei dem, welcher als Täter oder Teilnehmer einer Straftat oder der Datenhehlerei, Begünstigung, Strafvereitelung oder Hehlerei  Köhler    Ermittlungsmaßnahmen  verdächtig ist, kann eine Durchsuchu...
- **[Judge=3]** `§ 102 StPO – Rn. 3` — Direkt relevant für Durchsuchungsvoraussetzungen nach StPO
  > **Teilnehmer** nach §§ 25 ff. StGB, nicht die sog. notwendigen Teilnehmer (zum Begriff: Fischer/Fischer StGB Vor § 25 Rn. 7), stehen den Tatverdächtigen gleich. Bei jedem v. ihnen sowie bei den der Be...
- **[Judge=3]** `§ 102 StPO – Rn. 10` — Direkt relevant: Durchsuchungsvoraussetzungen und Verhältnismäßigkeitsgrundsatz
  > II. Auffinden von Beweismitteln. Zu den Beweismitteln (→ § 94 Rn. 4 ff.) gehören auch die nur in § 103 erwähnten Spuren (SK-StPO/Jäger/Wohlers Rn. 21) u. Personen, die zu Beweiszwecken in Augenschein ...

#### ragie — Top 3
- **[Judge=3]** `Strafprozessordnung.md` — Direkt relevant: zentrale Durchsuchungsvoraussetzungen nach § 102 StPO
  > Strafprozessordnung.md 102 Bei dem, welcher als Täter oder Teilnehmer einer Straftat oder der Datenhehlerei, Begünstigung, Strafvereitelung oder Hehlerei  Köhler  ---  ## Seite 613  Ermittlungsmaßnahm...
- **[Judge=3]** `Strafprozessordnung.md` — Direkt relevant: Durchsuchungsvoraussetzungen nach StPO
  > Strafprozessordnung.md 15 E. Raumdurchsuchung bei Ergreifung oder Verfolgung des Beschuldigten (Abs. 2). Wird der Beschuldigte, auch der aus der Strafhaft entflohene Verurteilte (BayObLGSt 2020, 152),...
- **[Judge=0]** `Strafprozessordnung.md` — Behandelt Zeugenbeweis, nicht Durchsuchungsrecht
  > Strafprozessordnung.md Schmitt  ---  ## Seite 917  Hauptverhandlung § 252 StPO  der Wohnungstür geklingelt hat, ihr Mann sei nicht zu Hause (OLG Stuttgart Justiz 1972, 322), nicht aber die Angabe, er ...

### q11 — alltagssprache

**Query:** Was passiert wenn jemand luegt damit er Geld bekommt?

**Kontext:** Laienhafte Umschreibung des Betrugstatbestandes

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours | 0.97 | 100% | 100% | 3 | 6.2s |
| ragie | 0.97 | 67% | 100% | 3 | 2.1s |

#### ours — Top 3
- **[Judge=3]** `§ 263 StGB – I. Vermögensbegriff  – Rn. 263` — Direkter Betrugstatbestand - perfekte Übereinstimmung
  > 263 (1) Wer in der Absicht, sich oder einem Dritten einen rechtswidrigen Vermögensvorteil zu verschaffen, das Vermögen eines anderen dadurch beschädigt, daß er durch Vorspiegelung falscher oder durch ...
- **[Judge=2]** `§ 263 StGB – BT. Zweitundzwanzigster Abschnitt – Rn. 69` — Behandelt Betrug §263, aber nicht Grundtatbestand
  > 69 Anders ist es, wenn der Verfügende seinerseits nur (gutgläubige) Hilfsperson eines bösgläubigen Dritten ist. Hier ist auf den Irrtum des Entscheidungsbefugten abzustellen: Erkennt dieser die Unrich...
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 176` — Direkt relevant: behandelt Betrug, Vorsatz und Bereicherungsabsicht
  > D. Subjektiver Tatbestand. § 263 setzt Vorsatz voraus; darüber hinaus ist die Absicht rechtswidriger Bereicherung erforderlich.   I. Vorsatz. 1. Täuschungsvorsatz. Der Vorsatz (bedingter Vorsatz genüg...

#### ragie — Top 3
- **[Judge=3]** `StGB_263_Betrug.md` — Direkt relevant: Betrug durch Lügen um Geld
  > StGB_263_Betrug.md Schwieriger ist die Abgrenzung bei zeitlich gestrecktem Fälligkeitstermin 34 (Mietzins; Ratenzahlungsverpflichtung; Arbeitsentgelt); auch hinsichtlich der Anforderungen an die konkl...
- **[Judge=2]** `StGB_263_Betrug.md` — Behandelt Betrug durch Täuschung um Geld/Vorteile
  > StGB_263_Betrug.md durch Verschweigen von Vermögensdelikten eines Bauleiters; zw.); NJW 1978, 2042 (Vermögensdelikt bei Einkäufer)). Bei Täuschung über eine frühere MfS-Mitarbeit war ein Schaden nur g...
- **[Judge=3]** `StGB_263_Betrug.md` — Direkte Antwort: Betrug durch Vorspiegelung falscher Tatsachen
  > StGB_263_Betrug.md Betrug  RiStBV 236–238  263 (1) Wer in der Absicht, sich oder einem Dritten einen rechtswidrigen Vermögensvorteil zu verschaffen, das Vermögen eines anderen dadurch beschädigt, daß ...

### q12 — alltagssprache

**Query:** Wann muss jemand ins Gefaengnis waehrend die Tat noch nicht bewiesen ist?

**Kontext:** Untersuchungshaft, §§ 112 ff. StPO

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours | 0.99 | 100% | 100% | 3 | 6.4s |
| ragie | 0.86 | 56% | 67% | 3 | 4.2s |

#### ours — Top 3
- **[Judge=3]** `§ 112 StPO – Rn. 112` — Definiert direkt Voraussetzungen für Untersuchungshaft trotz fehlenden Beweises
  > 112 (1) ¹ Die Untersuchungshaft darf gegen den Beschuldigten angeordnet werden, wenn er der Tat dringend verdächtig ist und ein Haftgrund besteht. ² Sie darf nicht angeordnet werden, wenn sie zu der B...
- **[Judge=3]** `§ 112 StPO – III. Flucht (Abs – Rn. 23` — Direkt relevant zu Untersuchungshaft und Haftgruenden
  > Bei einer besonders hohen Straferwartung braucht daher nur geprüft zu werden, ob Umstände vorhanden sind, die die hieraus herzuleitende Fluchtgefahr ausräumen können (KG StV 1996, 383; OLG München Str...
- **[Judge=3]** `§ 112 StPO – III. Flucht (Abs – Rn. 32 (Teil 2)` — Direkt zur Untersuchungshaft, behandelt Verdunkelungsgefahr als Haftgrund
  > Wenn die Verdunkelungshandlungen nicht geeignet sind, die Ermittlung der Wahrheit zu erschweren, darf UHaft nicht angeordnet werden. Der Haftgrund liegt daher nicht vor, wenn der Sachverhalt schon in ...

#### ragie — Top 3
- **[Judge=3]** `Strafprozessordnung.md` — Direkt zur Untersuchungshaft, beantwortet die Frage vollständig
  > Strafprozessordnung.md A. UHaft. Die UHaft nach §§ 112 ff., §§ 72, 72a JGG, dh die Inhaftierung eines noch nicht (o. noch nkr) verurteilten Beschuldigten, lässt sich mit der Unschuldsvermutung des Art...
- **[Judge=0]** `StGB_Kommentar.md` — Behandelt Vollstreckungsvereitelung, nicht Untersuchungshaft
  > StGB_Kommentar.md Fischer/Lutz  1941  ---  ## Seite 682  § 258  BT. Einundzwanzigster Abschnitt.  über für die Bewertung maßgebliche Umstände bewusst unterdrückt oder verschweigt. Dasselbe gilt entspr...
- **[Judge=3]** `Strafprozessordnung.md` — Direkt relevant: Haftgruende und Voraussetzungen fuer Untersuchungshaft
  > Strafprozessordnung.md 2 Freiheitsstrafe iSv Abs. 1 ist auch der Strafarrest nach § 9 WStG, nicht aber der Jugendarrest nach § 16 JGG (Löwe/Rosenberg/Hilger Rn. 3), auch wenn dieser neben Jugendstrafe...

### q13 — stpo-prozess

**Query:** Welche Voraussetzungen hat die Untersuchungshaft wegen Fluchtgefahr?

**Kontext:** § 112 Abs. 2 Nr. 2 StPO Fluchtgefahr

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours | 0.99 | 70% | 100% | 3 | 5.5s |
| ragie | 0.93 | 80% | 100% | 2 | 2.2s |

#### ours — Top 3
- **[Judge=3]** `§ 112 StPO – Rn. 112` — Direkter Gesetzestext zu Fluchtgefahr und Voraussetzungen
  > 112 (1) ¹ Die Untersuchungshaft darf gegen den Beschuldigten angeordnet werden, wenn er der Tat dringend verdächtig ist und ein Haftgrund besteht. ² Sie darf nicht angeordnet werden, wenn sie zu der B...
- **[Judge=3]** `§ 112 StPO – III. Flucht (Abs – Rn. 22` — Zentrale Voraussetzungen für Fluchtgefahr nach § 112
  > 22 Die Fluchtgefahr darf nur aus bestimmten Tatsachen hergeleitet werden. Bloße Mutmaßungen u. Befürchtungen genügen nicht. Die Tatsachen brauchen aber nicht zur vollen Überzeugung des Gerichts festzu...
- **[Judge=3]** `§ 112 StPO – III. Flucht (Abs – Rn. 17 (Teil 1)` — Direkt relevant: Definition und Voraussetzungen der Fluchtgefahr
  > 17 IV. Fluchtgefahr (Abs. 2 Nr. 2). Fluchtgefahr (Abs. 2 Nr. 2) besteht, wenn die Würdigung der Umstände des Falles es wahrscheinlicher macht, dass sich der Beschuldigte dem Strafverfahren entziehen, ...

#### ragie — Top 3
- **[Judge=2]** `Strafprozessordnung.md` — Einschränkungen bei leichten Taten, ergänzende Regelung
  > Strafprozessordnung.md ## Untersuchungshaft bei leichteren Taten  113 (1) Ist die Tat nur mit Freiheitsstrafe bis zu sechs Monaten oder mit Geldstrafe bis zu einhundertachtzig Tagessätzen bedroht, so ...
- **[Judge=3]** `Strafprozessordnung.md` — Direkt relevant: Voraussetzungen für Fluchtgefahr § 112
  > Strafprozessordnung.md Fluchtgefahr begründen idR auffälliger Wohnungs- o. Arbeitsplatzwechsel, Verwendung falscher Namen o. Papiere, Flucht in einem früheren Verf. o. Verfahrensabschnitt u. Zugehörig...
- **[Judge=3]** `Strafprozessordnung.md` — Behandelt direkt Fluchtgefahr nach § 112 StPO
  > Strafprozessordnung.md Schmitt  ---  ## Seite 728  StPO § 112  Erstes Buch. Neunter Abschnitt  Böhm NStZ 2001, 635). Die realistische Möglichkeit einer Unterbringung nach § 63 StGB kann die Annahme v....

### q14 — stpo-prozess

**Query:** Wie lange darf die Untersuchungshaft maximal dauern?

**Kontext:** § 121 StPO Sechs-Monats-Grenze, Haftpruefung OLG

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours | 0.97 | 90% | 100% | 3 | 4.7s |
| ragie | 1.00 | 100% | 100% | 3 | 2.9s |

#### ours — Top 3
- **[Judge=3]** `§ 121 StPO – Rn. 1` — Direkt relevant: behandelt Sechs-Monats-Grenze und OLG-Anordnung
  > 1 A. Beschleunigungsgebot. Einen Anspruch auf beschleunigte Aburteilung hat der in UHaft (und einstweiliger Unterbringung) befindliche Beschuldigte nach Art. 5 Abs. 3 S. 2 EMRK (→ EMRK Art. 5 Rn. 10 f...
- **[Judge=3]** `§ 121 StPO – Rn. 1` — Direkt relevant: behandelt Höchstgrenzen der Untersuchungshaft detailliert
  > Eine absolute Höchstgrenze für die Dauer v. UHaft sieht weder die StPO noch die EMRK vor (EGMR EuGRZ 1993, 384). Es kommt auf eine Abwägung aller Umstände des Einzelfalls an. Eine ein Jahr übersteigen...
- **[Judge=2]** `§ 121 StPO – Rn. 1` — Behandelt Haftdauer nach Anklageerhebung, nicht Höchstgrenzen allgemein
  > Schmitt    Verhaftung und vorläufige Festnahme   → § 120 Rn. 3a), Auch nach Beginn der Hauptverhandlung sind an den zügigen Fortgang des Verfahrens umso strengere Anforderungen zu stellen, je länger d...

#### ragie — Top 3
- **[Judge=3]** `Strafprozessordnung.md` — Direkt relevant, behandelt maximale Untersuchungshaftdauer und Fristen
  > Strafprozessordnung.md die 6 Monate überschritten werden (Abs. 2), eine UHaft v. mehr als 1 Jahr bis zum Beginn der HV kann nur in ganz bes. Ausnahmefällen gerechtfertigt sein (BVerfG NJW 2018, 2948; ...
- **[Judge=3]** `Strafprozessordnung.md` — Behandelt direkt § 121 StPO Sechs-Monats-Grenze
  > Strafprozessordnung.md Der Haftbefehl wird gegenstandslos (BVerfGE 9, 160; KG NStZ 2012, 230; OLG Düsseldorf Rpfleger 1984, 73; OLG Hamm StraFo 2002, 100; OLG Stuttgart Justiz 1984, 213). Dies soll we...
- **[Judge=3]** `Strafprozessordnung.md` — Direkt relevant: erklärt 6-Monats-Frist und Ausnahmen
  > Strafprozessordnung.md Die zeitliche Begrenzung der UHaft nach Abs. 1 gilt nicht, wenn der Haftbefehl nach § 230 Abs. 2 (→ § 230 Rn. 10), § 236 oder § 329 Abs. 4 S. 1 (→ § 329 Rn. 45) ergangen ist, au...

### q15 — stpo-prozess

**Query:** Was regelt § 136 StPO zur Beschuldigtenvernehmung?

**Kontext:** Belehrungspflichten, Recht auf Verteidiger

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours | 0.90 | 60% | 100% | 2 | 5.8s |
| ragie | 1.00 | 88% | 100% | 2 | 2.1s |

#### ours — Top 3
- **[Judge=2]** `StPO – III. Steuerstrafverfahren – Rn. 79` — Behandelt Belehrungspflichten, aber fokussiert informatorische Befragung
  > 79 3. Die informatorische Befragung der Tatverdächtigen, die nach diesen Grundsätzen noch keine Beschuldigten sind, ist Zeugenvernehmung. Die Bestrebungen des Schrifttums, neben Beschuldigte u. Zeugen...
- **[Judge=3]** `§ 114b StPO – I. Abs – Rn. 5` — Direkt relevant: behandelt § 136 StPO Belehrungspflichten
  > 5 II. Abs. 2 S. 1 Nr. 2–4. Hier wird die auch nach § 136 Abs. 1 S. 2, 3 und § 163a Abs. 3 S. 2, 4 vor Beginn der ersten richterlichen bzw. staatsanwaltschaftlichen o. polizeilichen Vernehmung bestehen...
- **[Judge=2]** `§ 500 StPO – ILL. für das Strafverfahren und das Bußgeldverf` — Behandelt Beschuldigtenvernehmung, aber nicht direkt § 136 StPO
  > (4) Zeugen können zur Aufenthaltsermittlung ausgeschrieben werden.  (5) Für die internationale Fahndung nach Personen, einschließlich der Fahndung nach Personen im SIS und aufgrund eines Europäischen ...

#### ragie — Top 3
- **[Judge=2]** `Strafprozessordnung.md` — Behandelt Beschuldigtenvernehmung und Belehrungspflichten, aber nicht § 136 direkt
  > Strafprozessordnung.md 77a Der Verfolgungsbehörde steht insoweit ein – objektiv zu bestimmender – Beurteilungsspielraum zu (BGHSt 38, 214 (228); BGHSt 64, 89; StraFo 2005, 27; erg. → StPO § 163a Rn. 4...
- **[Judge=2]** `Strafprozessordnung.md` — Behandelt Vernehmungskontext, aber nicht § 136 direkt
  > Strafprozessordnung.md (2) In der Ladung zu einer richterlichen oder staatsanwaltschaftlichen Vernehmung sollen Zwangsmaßnahmen für den Fall des Ausbleibens nur angedroht werden, wenn sie gegen den un...
- **[Judge=2]** `Strafprozessordnung.md` — Thematisch relevant, behandelt Belehrungspflichten bei Beschuldigtenvernehmung
  > Strafprozessordnung.md 45. Form der Vernehmung und Niederschrift. (1) ¹ Die Belehrung des Beschuldigten vor seiner Vernehmung nach § 136 Absatz 1, § 163a Absatz 3 Satz 2 StPO ist aktenkundig zu machen...

### q16 — cross-reference

**Query:** Worin unterscheidet sich Betrug von Unterschlagung?

**Kontext:** Abgrenzung § 263 vs § 246 StGB

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours | 0.83 | 60% | 67% | 1 | 7.9s |
| ragie | 0.88 | 17% | 33% | 1 | 1.8s |

#### ours — Top 3
- **[Judge=1]** `§ 263 StGB – BT. Zweitundzwanzigster Abschnitt – Rn. 69` — Behandelt nur Betrug, keine Abgrenzung zu Unterschlagung
  > 69 Anders ist es, wenn der Verfügende seinerseits nur (gutgläubige) Hilfsperson eines bösgläubigen Dritten ist. Hier ist auf den Irrtum des Entscheidungsbefugten abzustellen: Erkennt dieser die Unrich...
- **[Judge=2]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 76` — Behandelt Betrug, aber nicht Unterschlagungsabgrenzung
  > 4. Dreiecksbetrug. Da die Getäuschte und die verfügende, nicht aber die verfügende und die geschädigte Person identisch sein müssen, ist der Tatbestand des § 263 nur erfüllt, wenn die Vermögensverfügu...
- **[Judge=3]** `§ 263 StGB – I. Vermögensbegriff  – Rn. 263` — Zeigt zentrale Tatbestandsmerkmale des Betrugs für Abgrenzung
  > 263 (1) Wer in der Absicht, sich oder einem Dritten einen rechtswidrigen Vermögensvorteil zu verschaffen, das Vermögen eines anderen dadurch beschädigt, daß er durch Vorspiegelung falscher oder durch ...

#### ragie — Top 3
- **[Judge=1]** `StGB_Kommentar.md` — Erwähnt Betrug-Unterschlagung-Abgrenzung nur beiläufig als Wahlfeststellung
  > StGB_Kommentar.md 3. Einzelfälle. a) Zulässig sind Wahlfeststellungen nach hM (umfassende Dokumentation bei Wolter (→ Rn. 38) S. 174 ff.) zwischen:  Diebstahl und Hehlerei (BGHSt 1, 302; 12, 386; 15, ...
- **[Judge=1]** `StGB_Kommentar.md` — Inhaltsverzeichnis, keine inhaltliche Abgrenzung zwischen §263/§246
  > StGB_Kommentar.md # Neunzehnter Abschnitt. Diebstahl und Unterschlagung  Diebstahl ... § 242 Besonders schwerer Fall des Diebstahls ... § 243 Diebstahl mit Waffen; Bandendiebstahl; Wohnungseinbruchdie...
- **[Judge=2]** `StGB_Kommentar.md` — Erwähnt Betrug-Unterschlagung-Abgrenzung, aber ohne inhaltliche Erklärung
  > StGB_Kommentar.md Fischer  ---  ## Seite 93  § 1  AT. Erster Abschnitt. Erster Titel.  60; anderseits BGHSt 20, 104; Einschränkungen in OLG Karlsruhe NJW 1976, 902; offen gelassen in BGH NStZ 1985, 12...

### q17 — cross-reference

**Query:** Was sind die Unterschiede zwischen Diebstahl und Raub?

**Kontext:** § 242 vs § 249 StGB — Abgrenzung durch Gewalt/Drohung

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours | 0.99 | 90% | 100% | 3 | 7.1s |
| ragie | 0.99 | 100% | 100% | 3 | 3.3s |

#### ours — Top 3
- **[Judge=3]** `§ 249 StGB` — Direkt relevant: zentrale Abgrenzung Raub/Diebstahl durch Nötigungsmittel
  > NStZ 2023, 351). Danach ist § 249 gegenüber § 255 ein spezielles Delikt; in jedem Raub liegt eine räuberische Erpressung (aA die hM in der Literatur). Die Unterscheidung richtet sich nach dem äußeren ...
- **[Judge=3]** `§ 249 StGB – BT. Zwanzigster Abschnitt – Rn. 15` — Direkt relevant: Abgrenzung Raub zu Diebstahl erklärt
  > G. Subjektiver Tatbestand. Der Vorsatz muss entsprechend der Doppelnatur des Raubs sowohl Wegnahme (vgl. dazu → § 242 Rn. 29 ff.) als auch Nötigung (→ § 240 Rn. 53 f.) sowie deren Verknüpfung umfassen...
- **[Judge=3]** `§ 249 StGB – BT. Zwanzigster Abschnitt – Rn. 15` — Erklärt zentrale Abgrenzung Raub/Diebstahl durch Gewalt/Drohung
  > 15 Drohen setzt eine Handlung des Täters im Sinne einer ausdrücklichen oder konkludenten Gedankenäußerung voraus. Eine solche ist nicht schon dann gegeben, wenn der Täter die Furcht des Opfers vor (we...

#### ragie — Top 3
- **[Judge=3]** `StGB_Kommentar.md` — Erklärt direkt Abgrenzung Raub/Diebstahl mit Gewaltkriterium
  > StGB_Kommentar.md Rechtsprechungsübersichten: Maier/Percic NStZ-RR 2010, 129; Maier NStZ-RR 2012, 297; 2013, 329 (364); 2015, 33; 2017, 1, 2018, 33; 2025, 129; 2025, 161.  2 B. Systematische Stellung....
- **[Judge=3]** `StGB_Kommentar.md` — Direkt relevant: Abgrenzung Diebstahl-Raub durch Verdrängungsregeln
  > StGB_Kommentar.md J. Konkurrenzen. Gesetzeseinheit liegt zwischen § 249 und §§ 242, 243, 244, 244a vor, die von § 249 verdrängt werden (vgl. BGHSt 20, 235 (237 f.); NStZ-RR 2005, 202 (203)). Entsprech...
- **[Judge=3]** `StGB_Kommentar.md` — Direkt relevant - Raub-Definition mit Gewalt/Drohung
  > StGB_Kommentar.md E. Strafantrag. Abs. 3 regelt ein Antragserfordernis entspr. §§ 247, 248a (vgl. → § 247 Rn. 1 ff., → § 248a Rn. 1 ff.).  F. Abs. 4. Nach Abs. 4 wird milder bestraft, wer ohne Zueignu...

### q18 — cross-reference

**Query:** Wann wird Betrug zu Computerbetrug und umgekehrt?

**Kontext:** § 263 vs § 263a StGB — Abgrenzung bei elektronischer Datenverarbeitung

| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |
|--------|------|--------|-------|-------|--------|
| ours | 0.67 | 10% | 33% | 0 | 7.3s |
| ragie | 0.89 | 78% | 100% | 2 | 3.9s |

#### ours — Top 3
- **[Judge=0]** `§ 263 StGB – BT. Zweitundzwanzigster Abschnitt – Rn. 69` — Behandelt nur Betrug, keine Computerbetrug-Abgrenzung
  > 69 Anders ist es, wenn der Verfügende seinerseits nur (gutgläubige) Hilfsperson eines bösgläubigen Dritten ist. Hier ist auf den Irrtum des Entscheidungsbefugten abzustellen: Erkennt dieser die Unrich...
- **[Judge=1]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 62` — Allgemeine Betrugsregeln, aber nicht spezielle 263/263a-Abgrenzung
  > Die Kausalität der Täuschung für den Irrtum und dessen Kausalität für die Vermögensverfügung müssen im Einzelfall festgestellt sein. Mitverursachung reicht aus. Dabei darf das Gericht auch bei Serien-...
- **[Judge=3]** `§ 263 StGB – BT. Zweiundzwanzigster Abschnitt – Rn. 58` — Direkte Abgrenzung § 263/263a bei elektronischen Verfahren
  > 58 Im Geschäftsverkehr wird sich, wer die Berechtigung eines Leistungsverlangens oder -auftrags nicht zu prüfen hat, hierüber idR auch keine (richtigen oder falschen) Gedanken machen (NStZ 1997, 281; ...

#### ragie — Top 3
- **[Judge=2]** `StGB_Kommentar.md` — Behandelt § 263a, aber nicht die direkte Abgrenzung
  > StGB_Kommentar.md Fischer/Lutz  ---  ## Seite 799  Betrug und Untreue § 263a  IV. Subjektiver Tatbestand. In subjektiver Hinsicht ist (mindestens bedingter) Vorsatz hinsichtlich der Merkmale des Compu...
- **[Judge=2]** `StGB_263_Betrug.md` — Literaturhinweise zu Betrug vs Computerbetrug, thematisch relevant
  > StGB_263_Betrug.md FS Samson, 2010, 455; Ruha, Neue Wege für das Betrugsstrafrecht, FS Rissing-van Saan, 2011, 567; Satzger, Der Submissionsbetrug, 1994; Scheinfeld, Betrug durch unternehmerisches Wer...
- **[Judge=3]** `StGB_Kommentar.md` — Direkt relevant: Computerbetrug § 263a Tatbestandsmerkmale erklärt
  > StGB_Kommentar.md ## Computerbetrug  263a (1) Wer in der Absicht, sich oder einem Dritten einen rechtswidrigen Vermögensvorteil zu verschaffen, das Vermögen eines anderen dadurch beschädigt, daß er da...