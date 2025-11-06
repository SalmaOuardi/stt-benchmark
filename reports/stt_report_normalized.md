# Speech-to-Text Benchmark Report

Generated from 8 audio samples.

## audio_01_clean.wav
- Audio file: `data/processed/audio_01_clean.wav`
- Reference transcript: `data/processed/audio_01_reference.txt`
- Reference text: Bonjour, je suis chef de chantier sur le site de Vinci Construction.

Aujourd'hui, le six novembre deux mille vingt-cinq, je fais l'inspection du bâtiment A.

Je me trouve actuellement au troisième étage, devant l'entrée principale.

J'ai remarqué trois fissures importantes sur le mur est. Les fissures mesurent environ quinze à vingt centimètres de longueur.

L'état du béton armé semble préoccupant. Je recommande une inspection détaillée par un ingénieur structures.

Le coffrage du voile présente également des défauts. Il y a des traces d'infiltration d'eau près des banches.

Les étais sont en bon état, mais il faut vérifier la stabilité avant de poursuivre les travaux.

Je vais maintenant inspecter le quatrième étage pour vérifier l'état des dalles et des poutres.

Fin de l'inspection du bâtiment A, troisième étage.

### Model: gpt-audio
- Status: ✅ Success
- Latency: 3.28s
- Word Error Rate: 19.69%
- Transcript: Bonjour, je suis chef de chantier sur le site de Vinci Construction. Aujourd’hui, le 6 novembre 2025, je fais l’inspection du bâtiment A. Je me trouve actuellement au troisième étage devant l’entrée principale. J’ai remarqué trois fissures importantes sur le mur est, les fissures mesurent environ 15 à 20 centimètres de longueur. L’état du béton armé semble préoccupant, je recommande une inspection détaillée par un ingénieur structure. Le coffrage du voile présente également des défauts, il y a des traces d’infiltration d’eau près des banches. Les étais sont en bon état, mais il faut vérifier la stabilité avant de poursuivre les travaux. Il faut maintenant inspecter le quatrième étage pour vérifier l’état des dalles et des poutres. Fin de l’inspection du bâtiment A, troisième étage.
- Errors: substitutions=25, insertions=0, deletions=0
#### Error Details
- Replace: expected "Aujourd'hui," | actual "Aujourd’hui,"
- Replace: expected "six" | actual "6"
- Replace: expected "deux mille vingt-cinq," | actual "2025,"
- Replace: expected "l'inspection" | actual "l’inspection"
- Replace: expected "étage," | actual "étage"
- Replace: expected "l'entrée" | actual "l’entrée"
- Replace: expected "J'ai" | actual "J’ai"
- Replace: expected "est. Les" | actual "est, les"
- Replace: expected "quinze" | actual "15"
- Replace: expected "vingt" | actual "20"
- Replace: expected "L'état" | actual "L’état"
- Replace: expected "préoccupant. Je" | actual "préoccupant, je"
- Replace: expected "structures." | actual "structure."
- Replace: expected "défauts. Il" | actual "défauts, il"
- Replace: expected "d'infiltration d'eau" | actual "d’infiltration d’eau"
- Replace: expected "Je vais" | actual "Il faut"
- Replace: expected "l'état" | actual "l’état"
- Replace: expected "l'inspection" | actual "l’inspection"
- Normalized Word Error Rate: 2.40%
- Normalized Reference: bonjour je suis chef de chantier sur le site de vinci construction aujourd'hui le 6 novembre 2025, je fais l'inspection du bâtiment a je me trouve actuellement au troisième étage devant l'entrée principale j'ai remarqué trois fissures importantes sur le mur est les fissures mesurent environ 15 à 20 centimètres de longueur l'état du béton armé semble préoccupant je recommande une inspection détaillée par un ingénieur structures le coffrage du voile présente également des défauts il y a des traces d'infiltration d'eau près des banches les étais sont en bon état mais il faut vérifier la stabilité avant de poursuivre les travaux je vais maintenant inspecter le quatrième étage pour vérifier l'état des dalles et des poutres fin de l'inspection du bâtiment a troisième étage
- Normalized Transcript: bonjour je suis chef de chantier sur le site de vinci construction aujourd'hui le 6 novembre 2025, je fais l'inspection du bâtiment a je me trouve actuellement au troisième étage devant l'entrée principale j'ai remarqué trois fissures importantes sur le mur est les fissures mesurent environ 15 à 20 centimètres de longueur l'état du béton armé semble préoccupant je recommande une inspection détaillée par un ingénieur structure le coffrage du voile présente également des défauts il y a des traces d'infiltration d'eau près des banches les étais sont en bon état mais il faut vérifier la stabilité avant de poursuivre les travaux il faut maintenant inspecter le quatrième étage pour vérifier l'état des dalles et des poutres fin de l'inspection du bâtiment a troisième étage
- Normalized Errors: substitutions=3, insertions=0, deletions=0
#### Normalized Error Details
- Replace: expected "structures" | actual "structure"
- Replace: expected "je vais" | actual "il faut"

### Model: gpt-audio-mini
- Status: ✅ Success
- Latency: 3.50s
- Word Error Rate: 11.81%
- Transcript: Bonjour, je suis chef de chantier sur le site de Vinci Construction. Aujourd'hui, le 6 novembre 2025, je fais l'inspection du bâtiment A. Je me trouve actuellement au troisième étage devant l'entrée principale. J'ai remarqué trois fissures importantes sur le mur Est. Les fissures mesurent environ 15 à 20 centimètres de longueur. L'état du béton armé semble préoccupant. Je recommande une inspection détaillée par un ingénieur structure. Le coffrage du voile présente également des défauts et il y a des traces d'infiltration d'eau près des bancs. Les étais sont en bon état, mais il faut vérifier la stabilité avant de poursuivre les travaux. Il faut maintenant inspecter le quatrième étage pour vérifier l'état des dalles et des poutres. Fin de l'inspection du bâtiment A, troisième étage.
- Errors: substitutions=15, insertions=0, deletions=0
#### Error Details
- Replace: expected "six" | actual "6"
- Replace: expected "deux mille vingt-cinq," | actual "2025,"
- Replace: expected "étage," | actual "étage"
- Replace: expected "est." | actual "Est."
- Replace: expected "quinze" | actual "15"
- Replace: expected "vingt" | actual "20"
- Replace: expected "structures." | actual "structure."
- Replace: expected "défauts. Il" | actual "défauts et il"
- Replace: expected "banches." | actual "bancs."
- Replace: expected "Je vais" | actual "Il faut"
- Normalized Word Error Rate: 4.00%
- Normalized Reference: bonjour je suis chef de chantier sur le site de vinci construction aujourd'hui le 6 novembre 2025, je fais l'inspection du bâtiment a je me trouve actuellement au troisième étage devant l'entrée principale j'ai remarqué trois fissures importantes sur le mur est les fissures mesurent environ 15 à 20 centimètres de longueur l'état du béton armé semble préoccupant je recommande une inspection détaillée par un ingénieur structures le coffrage du voile présente également des défauts il y a des traces d'infiltration d'eau près des banches les étais sont en bon état mais il faut vérifier la stabilité avant de poursuivre les travaux je vais maintenant inspecter le quatrième étage pour vérifier l'état des dalles et des poutres fin de l'inspection du bâtiment a troisième étage
- Normalized Transcript: bonjour je suis chef de chantier sur le site de vinci construction aujourd'hui le 6 novembre 2025, je fais l'inspection du bâtiment a je me trouve actuellement au troisième étage devant l'entrée principale j'ai remarqué trois fissures importantes sur le mur est les fissures mesurent environ 15 à 20 centimètres de longueur l'état du béton armé semble préoccupant je recommande une inspection détaillée par un ingénieur structure le coffrage du voile présente également des défauts et il y a des traces d'infiltration d'eau près des bancs les étais sont en bon état mais il faut vérifier la stabilité avant de poursuivre les travaux il faut maintenant inspecter le quatrième étage pour vérifier l'état des dalles et des poutres fin de l'inspection du bâtiment a troisième étage
- Normalized Errors: substitutions=4, insertions=1, deletions=0
#### Normalized Error Details
- Replace: expected "structures" | actual "structure"
- Insert: expected "" | actual "et"
- Replace: expected "banches" | actual "bancs"
- Replace: expected "je vais" | actual "il faut"

### Model: gpt-4o-audio-preview
- Status: ✅ Success
- Latency: 2.62s
- Word Error Rate: 11.02%
- Transcript: Bonjour. Je suis chef de chantier sur le site de Vinci Construction. Aujourd'hui, le 6 novembre 2025, je fais l'inspection du bâtiment A. Je me trouve actuellement au troisième étage, devant l'entrée principale. J'ai remarqué trois fissures importantes sur le mur est. Les fissures mesurent environ 15 à 20 centimètres de longueur. L'état du béton armé semble préoccupant. Je recommande une inspection détaillée par un ingénieur structure. Le coffrage du voile présente également des défauts, et il y a des traces d'infiltration d'eau près des banches. Les étais sont en bon état, mais il faut vérifier la stabilité avant de poursuivre les travaux. Il faut maintenant inspecter le quatrième étage pour vérifier l'état des dalles et des poutres. Fin de l'inspection du bâtiment A, troisième étage.
- Errors: substitutions=14, insertions=0, deletions=0
#### Error Details
- Replace: expected "Bonjour, je" | actual "Bonjour. Je"
- Replace: expected "six" | actual "6"
- Replace: expected "deux mille vingt-cinq," | actual "2025,"
- Replace: expected "quinze" | actual "15"
- Replace: expected "vingt" | actual "20"
- Replace: expected "structures." | actual "structure."
- Replace: expected "défauts. Il" | actual "défauts, et il"
- Replace: expected "Je vais" | actual "Il faut"
- Normalized Word Error Rate: 3.20%
- Normalized Reference: bonjour je suis chef de chantier sur le site de vinci construction aujourd'hui le 6 novembre 2025, je fais l'inspection du bâtiment a je me trouve actuellement au troisième étage devant l'entrée principale j'ai remarqué trois fissures importantes sur le mur est les fissures mesurent environ 15 à 20 centimètres de longueur l'état du béton armé semble préoccupant je recommande une inspection détaillée par un ingénieur structures le coffrage du voile présente également des défauts il y a des traces d'infiltration d'eau près des banches les étais sont en bon état mais il faut vérifier la stabilité avant de poursuivre les travaux je vais maintenant inspecter le quatrième étage pour vérifier l'état des dalles et des poutres fin de l'inspection du bâtiment a troisième étage
- Normalized Transcript: bonjour je suis chef de chantier sur le site de vinci construction aujourd'hui le 6 novembre 2025, je fais l'inspection du bâtiment a je me trouve actuellement au troisième étage devant l'entrée principale j'ai remarqué trois fissures importantes sur le mur est les fissures mesurent environ 15 à 20 centimètres de longueur l'état du béton armé semble préoccupant je recommande une inspection détaillée par un ingénieur structure le coffrage du voile présente également des défauts et il y a des traces d'infiltration d'eau près des banches les étais sont en bon état mais il faut vérifier la stabilité avant de poursuivre les travaux il faut maintenant inspecter le quatrième étage pour vérifier l'état des dalles et des poutres fin de l'inspection du bâtiment a troisième étage
- Normalized Errors: substitutions=3, insertions=1, deletions=0
#### Normalized Error Details
- Replace: expected "structures" | actual "structure"
- Insert: expected "" | actual "et"
- Replace: expected "je vais" | actual "il faut"

---

## audio_02_technical.wav
- Audio file: `data/processed/audio_02_technical.wav`
- Reference transcript: `data/processed/audio_02_reference.txt`
- Reference text: Inspection technique du bâtiment B, niveau moins un.

Le coffrage métallique présente des déformations au niveau des panneaux. Les banches doivent être remplacées avant la prochaine coulée.

Le ferraillage du voile en béton armé est conforme aux plans. Les aciers haute adhérence HA quatre cent sont correctement positionnés.

Les étais tubulaires supportant le plancher du rez-de-chaussée sont espacés de un mètre vingt. C'est conforme aux prescriptions du bureau d'études.

J'observe des nids de gravier dans la dalle. Le béton n'a pas été correctement vibré lors de la coulée précédente.

Les joints de dilatation nécessitent un calfeutrement. Il y a des infiltrations d'eau par les reprises de bétonnage.

Le cuvelage du sous-sol présente des fissurations en escalier. Cela indique probablement un tassement différentiel des fondations.

Les armatures en attente dépassent de quarante centimètres. Elles doivent être protégées contre la corrosion.

Le décoffrage peut être effectué dans quarante-huit heures, sous réserve d'un essai de résistance du béton.

Fin de l'inspection technique.

### Model: gpt-audio
- Status: ✅ Success
- Latency: 4.65s
- Word Error Rate: 16.98%
- Transcript: Inspection technique du bâtiment B – niveau moins un. Le coffrage métallique présente des déformations au niveau des panneaux. Les banches doivent être remplacées dans la prochaine coulée. Le ferraillage du voile en béton armé est conforme au plan, les aciers haute adhérence HA 400 sont correctement positionnés. Les étais tubulaires supportant le plancher du rez-de-chaussée sont espacés de 1 mètre 20, c’est conforme aux prescriptions du bureau d’étude. J’observe des nids de graviers dans la dalle. Le béton n’a pas été correctement vibré lors de la coulée précédente. Les joints de dilatation nécessitent un calfeutrement. Il y a des infiltrations d’eau par les reprises de bétonnage. Le cuvelage du sous-sol présente des fissures en escalier – cela indique probablement un tassement différentiel des fondations. Les armatures en attente dépassent de 40 centimètres : elles doivent être protégées contre la corrosion. Le décoffrage peut être effectué dans 48 heures, sous réserve d’un essai de résistance du béton. Fin de l’inspection technique.
- Errors: substitutions=27, insertions=0, deletions=0
#### Error Details
- Replace: expected "B," | actual "B –"
- Replace: expected "avant" | actual "dans"
- Replace: expected "aux plans. Les" | actual "au plan, les"
- Replace: expected "quatre cent" | actual "400"
- Replace: expected "un" | actual "1"
- Replace: expected "vingt. C'est" | actual "20, c’est"
- Replace: expected "d'études. J'observe" | actual "d’étude. J’observe"
- Replace: expected "gravier" | actual "graviers"
- Replace: expected "n'a" | actual "n’a"
- Replace: expected "d'eau" | actual "d’eau"
- Replace: expected "fissurations" | actual "fissures"
- Replace: expected "escalier. Cela" | actual "escalier – cela"
- Replace: expected "quarante centimètres. Elles" | actual "40 centimètres : elles"
- Replace: expected "quarante-huit" | actual "48"
- Replace: expected "d'un" | actual "d’un"
- Replace: expected "l'inspection" | actual "l’inspection"
- Normalized Word Error Rate: 8.39%
- Normalized Reference: inspection technique du bâtiment b niveau -1 le coffrage métallique présente des déformations au niveau des panneaux les banches doivent être remplacées avant la prochaine coulée le ferraillage du voile en béton armé est conforme aux plans les aciers haute adhérence ha400 sont correctement positionnés les étais tubulaires supportant le plancher du rez-de-chaussée sont espacés de 1.20 m c'est conforme aux prescriptions du bureau d'études j'observe des nids de gravier dans la dalle le béton n'a pas été correctement vibré lors de la coulée précédente les joints de dilatation nécessitent un calfeutrement il y a des infiltrations d'eau par les reprises de bétonnage le cuvelage du sous-sol présente des fissures en escalier cela indique probablement un tassement différentiel des fondations les armatures en attente dépassent de 40 cm elles doivent être protégées contre la corrosion le décoffrage peut être effectué dans 48 heures sous réserve d'un essai de résistance du béton fin de l'inspection technique
- Normalized Transcript: inspection technique du bâtiment b – niveau -1 le coffrage métallique présente des déformations au niveau des panneaux les banches doivent être remplacées dans la prochaine coulée le ferraillage du voile en béton armé est conforme au plan les aciers haute adhérence ha 400 sont correctement positionnés les étais tubulaires supportant le plancher du rez-de-chaussée sont espacés de 1 mètre 20, c'est conforme aux prescriptions du bureau d'étude j'observe des nids de graviers dans la dalle le béton n'a pas été correctement vibré lors de la coulée précédente les joints de dilatation nécessitent un calfeutrement il y a des infiltrations d'eau par les reprises de bétonnage le cuvelage du sous-sol présente des fissures en escalier – cela indique probablement un tassement différentiel des fondations les armatures en attente dépassent de 40 centimètres elles doivent être protégées contre la corrosion le décoffrage peut être effectué dans 48 heures sous réserve d'un essai de résistance du béton fin de l'inspection technique
- Normalized Errors: substitutions=11, insertions=2, deletions=0
#### Normalized Error Details
- Insert: expected "" | actual "–"
- Replace: expected "avant" | actual "dans"
- Replace: expected "aux plans" | actual "au plan"
- Replace: expected "ha400" | actual "ha 400"
- Replace: expected "1.20 m" | actual "1 mètre 20,"
- Replace: expected "d'études" | actual "d'étude"
- Replace: expected "gravier" | actual "graviers"
- Insert: expected "" | actual "–"
- Replace: expected "cm" | actual "centimètres"

### Model: gpt-audio-mini
- Status: ✅ Success
- Latency: 4.24s
- Word Error Rate: 13.21%
- Transcript: 欢迎您收听本次法语音频。以下是完整的文字记录：

Inspection technique du bâtiment B niveau -1. Le coffrage métallique présente des déformations au niveau des panneaux. Les banches doivent être remplacées dans la prochaine coulée. Le ferraillage du voile en béton armé est conforme au plan. Les aciers haute adhérence HA 400 sont correctement positionnés. Les étais tubulaires supportant le plancher du rez-de-chaussée sont espacés de 1,20 m. C'est conforme aux prescriptions du bureau d'études. J'observe des nids de gravier dans la dalle. Le béton n'a pas été correctement vibré lors de la coulée précédente. Les joints de dilatation nécessitent un calfeutrement. Il y a des infiltrations d'eau par les reprises de bétonnage. Le cuvelage du sous-sol présente des fissures en escalier. Cela indique probablement un tassement différentiel des fondations. Les armatures en attente dépassent de 40 cm. Elles doivent être protégées contre la corrosion. Le décoffrage peut être effectué dans 48 heures sous réserve d'un essai de résistance du béton. Fin de l'inspection technique.

Merci de votre écoute.
- Errors: substitutions=16, insertions=5, deletions=0
#### Error Details
- Insert: expected "" | actual "欢迎您收听本次法语音频。以下是完整的文字记录："
- Replace: expected "B," | actual "B"
- Replace: expected "moins un." | actual "-1."
- Replace: expected "avant" | actual "dans"
- Replace: expected "aux plans." | actual "au plan."
- Replace: expected "quatre cent" | actual "400"
- Replace: expected "un mètre vingt." | actual "1,20 m."
- Replace: expected "fissurations" | actual "fissures"
- Replace: expected "quarante centimètres." | actual "40 cm."
- Replace: expected "quarante-huit heures," | actual "48 heures"
- Insert: expected "" | actual "Merci de votre écoute."
- Normalized Word Error Rate: 6.45%
- Normalized Reference: inspection technique du bâtiment b niveau -1 le coffrage métallique présente des déformations au niveau des panneaux les banches doivent être remplacées avant la prochaine coulée le ferraillage du voile en béton armé est conforme aux plans les aciers haute adhérence ha400 sont correctement positionnés les étais tubulaires supportant le plancher du rez-de-chaussée sont espacés de 1.20 m c'est conforme aux prescriptions du bureau d'études j'observe des nids de gravier dans la dalle le béton n'a pas été correctement vibré lors de la coulée précédente les joints de dilatation nécessitent un calfeutrement il y a des infiltrations d'eau par les reprises de bétonnage le cuvelage du sous-sol présente des fissures en escalier cela indique probablement un tassement différentiel des fondations les armatures en attente dépassent de 40 cm elles doivent être protégées contre la corrosion le décoffrage peut être effectué dans 48 heures sous réserve d'un essai de résistance du béton fin de l'inspection technique
- Normalized Transcript: 欢迎您收听本次法语音频。以下是完整的文字记录 inspection technique du bâtiment b niveau -1 le coffrage métallique présente des déformations au niveau des panneaux les banches doivent être remplacées dans la prochaine coulée le ferraillage du voile en béton armé est conforme au plan les aciers haute adhérence ha 400 sont correctement positionnés les étais tubulaires supportant le plancher du rez-de-chaussée sont espacés de 1.20 m c'est conforme aux prescriptions du bureau d'études j'observe des nids de gravier dans la dalle le béton n'a pas été correctement vibré lors de la coulée précédente les joints de dilatation nécessitent un calfeutrement il y a des infiltrations d'eau par les reprises de bétonnage le cuvelage du sous-sol présente des fissures en escalier cela indique probablement un tassement différentiel des fondations les armatures en attente dépassent de 40 cm elles doivent être protégées contre la corrosion le décoffrage peut être effectué dans 48 heures sous réserve d'un essai de résistance du béton fin de l'inspection technique merci de votre écoute
- Normalized Errors: substitutions=5, insertions=5, deletions=0
#### Normalized Error Details
- Insert: expected "" | actual "欢迎您收听本次法语音频。以下是完整的文字记录"
- Replace: expected "avant" | actual "dans"
- Replace: expected "aux plans" | actual "au plan"
- Replace: expected "ha400" | actual "ha 400"
- Insert: expected "" | actual "merci de votre écoute"

### Model: gpt-4o-audio-preview
- Status: ✅ Success
- Latency: 3.50s
- Word Error Rate: 16.35%
- Transcript: Inspection technique du bâtiment B, niveau -1. Le coffrage métallique présente des déformations au niveau des panneaux. Les banche doivent être remplacées dans la prochaine coulée. Le ferraillage du voile en béton armé est conforme au plan. Les aciers haute adhérence HA400 sont correctement positionnés. Les étais tubulaires supportant le plancher du rez-de-chaussée sont espacés de 1,20 m. C’est conforme aux prescriptions du bureau d’études. J’observe des nids de gravier dans la dalle. Le béton n’a pas été correctement vibré lors de la coulée précédente. Les joints de dilatation nécessitent un calfeutrement. Il y a des infiltrations d’eau par les reprises de bétonnage. Le cuvelage du sous-sol présente des fissures en escalier, cela indique probablement un tassement différentiel des fondations. Les armatures en attente dépassent de 40 cm. Elles doivent être protégées contre la corrosion. Le décoffrage peut être effectué dans 48 heures sous réserve d’un essai de résistance du béton. Fin de l’inspection technique.
- Errors: substitutions=26, insertions=0, deletions=0
#### Error Details
- Replace: expected "moins un." | actual "-1."
- Replace: expected "banches" | actual "banche"
- Replace: expected "avant" | actual "dans"
- Replace: expected "aux plans." | actual "au plan."
- Replace: expected "HA quatre cent" | actual "HA400"
- Replace: expected "un mètre vingt. C'est" | actual "1,20 m. C’est"
- Replace: expected "d'études. J'observe" | actual "d’études. J’observe"
- Replace: expected "n'a" | actual "n’a"
- Replace: expected "d'eau" | actual "d’eau"
- Replace: expected "fissurations" | actual "fissures"
- Replace: expected "escalier. Cela" | actual "escalier, cela"
- Replace: expected "quarante centimètres." | actual "40 cm."
- Replace: expected "quarante-huit heures," | actual "48 heures"
- Replace: expected "d'un" | actual "d’un"
- Replace: expected "l'inspection" | actual "l’inspection"
- Normalized Word Error Rate: 2.58%
- Normalized Reference: inspection technique du bâtiment b niveau -1 le coffrage métallique présente des déformations au niveau des panneaux les banches doivent être remplacées avant la prochaine coulée le ferraillage du voile en béton armé est conforme aux plans les aciers haute adhérence ha400 sont correctement positionnés les étais tubulaires supportant le plancher du rez-de-chaussée sont espacés de 1.20 m c'est conforme aux prescriptions du bureau d'études j'observe des nids de gravier dans la dalle le béton n'a pas été correctement vibré lors de la coulée précédente les joints de dilatation nécessitent un calfeutrement il y a des infiltrations d'eau par les reprises de bétonnage le cuvelage du sous-sol présente des fissures en escalier cela indique probablement un tassement différentiel des fondations les armatures en attente dépassent de 40 cm elles doivent être protégées contre la corrosion le décoffrage peut être effectué dans 48 heures sous réserve d'un essai de résistance du béton fin de l'inspection technique
- Normalized Transcript: inspection technique du bâtiment b niveau -1 le coffrage métallique présente des déformations au niveau des panneaux les banche doivent être remplacées dans la prochaine coulée le ferraillage du voile en béton armé est conforme au plan les aciers haute adhérence ha400 sont correctement positionnés les étais tubulaires supportant le plancher du rez-de-chaussée sont espacés de 1.20 m c'est conforme aux prescriptions du bureau d'études j'observe des nids de gravier dans la dalle le béton n'a pas été correctement vibré lors de la coulée précédente les joints de dilatation nécessitent un calfeutrement il y a des infiltrations d'eau par les reprises de bétonnage le cuvelage du sous-sol présente des fissures en escalier cela indique probablement un tassement différentiel des fondations les armatures en attente dépassent de 40 cm elles doivent être protégées contre la corrosion le décoffrage peut être effectué dans 48 heures sous réserve d'un essai de résistance du béton fin de l'inspection technique
- Normalized Errors: substitutions=4, insertions=0, deletions=0
#### Normalized Error Details
- Replace: expected "banches" | actual "banche"
- Replace: expected "avant" | actual "dans"
- Replace: expected "aux plans" | actual "au plan"

---

## audio_03_numbers.wav
- Audio file: `data/processed/audio_03_numbers.wav`
- Reference transcript: `data/processed/audio_03_reference.txt`
- Reference text: Relevé des mesures, bâtiment C, étage deux.

Fissure numéro un: longueur vingt-trois centimètres, largeur deux millimètres, profondeur environ cinq millimètres.

Fissure numéro deux: longueur trente-sept centimètres, largeur trois millimètres, orientation quarante-cinq degrés par rapport à l'horizontale.

Fissure numéro trois: longueur quinze centimètres, située à un mètre cinquante du sol.

Surface totale du mur: quatre mètres de hauteur sur huit mètres de longueur, soit trente-deux mètres carrés.

Nombre d'armatures visibles: douze barres de diamètre seize millimètres.

Espacement entre les poteaux: quatre mètres cinquante.

Épaisseur du voile: vingt-cinq centimètres.

Charge prévue sur la dalle: cinq cents kilogrammes par mètre carré.

Température du béton: dix-huit degrés Celsius.

Humidité relative: soixante-cinq pour cent.

Résistance du béton testée: trente mégapascals après vingt-huit jours.

Flèche mesurée au centre de la poutre: huit millimètres, dans les tolérances acceptables.

Nombre d'ouvriers présents: quinze personnes.

Fin du relevé des mesures.

### Model: gpt-audio
- Status: ✅ Success
- Latency: 4.32s
- Word Error Rate: 50.35%
- Transcript: Relevé de mesures bâtiment C étage 2 :  
Fissure numéro 1 : longueur 23 cm, largeur 2 mm, profondeur environ 5 mm.  
Fissure numéro 2 : longueur 37 cm, largeur 3 mm, orientation 45 degrés par rapport à l’horizontale.  
Fissure numéro 3 : largeur 15 cm, située à 1 mètre 40 du sol.  
Surface totale du mur : 4 murs de hauteur sur 8 mètres de longueur, soit 32 mètres carrés.  
Nombre d’armatures visibles : 12 barres de diamètre 16 mm.  
Espacement entre les poteaux : 4 mètres 50.  
Épaisseur du voile : 25 cm.  
Charge prévue sur la dalle : 500 kg par mètre carré.  
Température du béton : 18 degrés Celsius.  
Humidité relative : 65 %.  
Résistance du béton testée : 30 mégapascals après 28 jours.  
Flèche mesurée au centre de la poutre : 8 mm, dans les tolérances acceptables.  
Nombre d’ouvriers présents : 15 personnes.  
Fin du relevé des mesures.
- Errors: substitutions=71, insertions=0, deletions=0
#### Error Details
- Replace: expected "des mesures," | actual "de mesures"
- Replace: expected "C," | actual "C"
- Replace: expected "deux." | actual "2 :"
- Replace: expected "un:" | actual "1 :"
- Replace: expected "vingt-trois centimètres," | actual "23 cm,"
- Replace: expected "deux millimètres," | actual "2 mm,"
- Replace: expected "cinq millimètres." | actual "5 mm."
- Replace: expected "deux:" | actual "2 :"
- Replace: expected "trente-sept centimètres," | actual "37 cm,"
- Replace: expected "trois millimètres," | actual "3 mm,"
- Replace: expected "quarante-cinq" | actual "45"
- Replace: expected "l'horizontale." | actual "l’horizontale."
- Replace: expected "trois: longueur quinze centimètres," | actual "3 : largeur 15 cm,"
- Replace: expected "un" | actual "1"
- Replace: expected "cinquante" | actual "40"
- Replace: expected "mur: quatre mètres" | actual "mur : 4 murs"
- Replace: expected "huit" | actual "8"
- Replace: expected "trente-deux" | actual "32"
- Replace: expected "d'armatures visibles: douze" | actual "d’armatures visibles : 12"
- Replace: expected "seize millimètres." | actual "16 mm."
- Replace: expected "poteaux: quatre" | actual "poteaux : 4"
- Replace: expected "cinquante." | actual "50."
- Replace: expected "voile: vingt-cinq centimètres." | actual "voile : 25 cm."
- Replace: expected "dalle: cinq cents kilogrammes" | actual "dalle : 500 kg"
- Replace: expected "béton: dix-huit" | actual "béton : 18"
- Replace: expected "relative: soixante-cinq pour cent." | actual "relative : 65 %."
- Replace: expected "testée: trente" | actual "testée : 30"
- Replace: expected "vingt-huit" | actual "28"
- Replace: expected "poutre: huit millimètres," | actual "poutre : 8 mm,"
- Replace: expected "d'ouvriers présents: quinze" | actual "d’ouvriers présents : 15"
- Normalized Word Error Rate: 24.82%
- Normalized Reference: relevé des mesures bâtiment c étage deux fissure numéro un longueur vingt-trois centimètres largeur deux millimètres profondeur environ cinq millimètres fissure numéro deux longueur 30-7 centimètres largeur trois millimètres orientation quarante-cinq degrés par rapport à l'horizontale fissure numéro trois longueur 15 centimètres située à un mètre 50 du sol surface totale du mur quatre mètres de hauteur sur 8 mètres de longueur soit trente-deux mètres carrés nombre d'armatures visibles 12 barres de diamètre 16 millimètres espacement entre les poteaux quatre mètres 50 épaisseur du voile vingt-cinq centimètres charge prévue sur la dalle cinq cents kilogrammes par mètre carré température du béton 18 degrés celsius humidité relative soixante-cinq pour cent résistance du béton testée 30 mégapascals après 20-8 jours flèche mesurée au centre de la poutre 8 millimètres dans les tolérances acceptables nombre d'ouvriers présents 15 personnes fin du relevé des mesures
- Normalized Transcript: relevé de mesures bâtiment c étage 2 fissure numéro 1 longueur 23 cm largeur 2 mm profondeur environ 5 mm fissure numéro 2 longueur 37 cm largeur 3 mm orientation 45 degrés par rapport à l'horizontale fissure numéro 3 largeur 15 cm située à 1 mètre 40 du sol surface totale du mur 4 murs de hauteur sur 8 mètres de longueur soit 32 mètres carrés nombre d'armatures visibles 12 barres de diamètre 16 mm espacement entre les poteaux 4 mètres 50 épaisseur du voile 25 cm charge prévue sur la dalle 500 kg par mètre carré température du béton 18 degrés celsius humidité relative 65 % résistance du béton testée 30 mégapascals après 28 jours flèche mesurée au centre de la poutre 8 mm dans les tolérances acceptables nombre d'ouvriers présents 15 personnes fin du relevé des mesures
- Normalized Errors: substitutions=35, insertions=0, deletions=0
#### Normalized Error Details
- Replace: expected "des" | actual "de"
- Replace: expected "deux" | actual "2"
- Replace: expected "un" | actual "1"
- Replace: expected "vingt-trois centimètres" | actual "23 cm"
- Replace: expected "deux millimètres" | actual "2 mm"
- Replace: expected "cinq millimètres" | actual "5 mm"
- Replace: expected "deux" | actual "2"
- Replace: expected "30-7 centimètres" | actual "37 cm"
- Replace: expected "trois millimètres" | actual "3 mm"
- Replace: expected "quarante-cinq" | actual "45"
- Replace: expected "trois longueur" | actual "3 largeur"
- Replace: expected "centimètres" | actual "cm"
- Replace: expected "un" | actual "1"
- Replace: expected "50" | actual "40"
- Replace: expected "quatre mètres" | actual "4 murs"
- Replace: expected "trente-deux" | actual "32"
- Replace: expected "millimètres" | actual "mm"
- Replace: expected "quatre" | actual "4"
- Replace: expected "vingt-cinq centimètres" | actual "25 cm"
- Replace: expected "cinq cents kilogrammes" | actual "500 kg"
- Replace: expected "soixante-cinq pour cent" | actual "65 %"
- Replace: expected "20-8" | actual "28"
- Replace: expected "millimètres" | actual "mm"

### Model: gpt-audio-mini
- Status: ✅ Success
- Latency: 4.48s
- Word Error Rate: 75.89%
- Transcript: Dans l'écoute précédente, il n'y avait pas de contenu audio à transcrire, mais plutôt un texte écrit. Voici donc la transcription exacte de ce texte français :

Relevé de mesures, bâtiment C, étage 2.

Fissure n°1 : Longueur 23 cm, largeur 2 mm, profondeur environ 5 mm.

Fissure n°2 : Longueur 37 cm, largeur 3 mm, orientation 45° par rapport à l'horizontal.

Fissure n°3 : Largeur 15 cm, située à 1,40 m du sol.

Surface totale du mur : 4 murs d'une hauteur sur 8 m de longueur, soit 32 m².

Nombre d'armature visible : 12 barres de diamètre 16 mm.

Espacement entre les poteaux : 4,50 m.

Épaisseur du voile : 25 cm.

Charge prévue sur la dalle : 500 kg par m².

Température du béton : 18°C.

Humidité relative : 65 %.

Résistance du béton testée : 30 MPa après 28 jours.

Flèche mesurée au centre de la poutre : 8 mm, dont les tolérances acceptables.

Nombre d'ouvriers présents : 15 personnes.

Fin du relevé des mesures.
- Errors: substitutions=80, insertions=27, deletions=0
#### Error Details
- Insert: expected "" | actual "Dans l'écoute précédente, il n'y avait pas de contenu audio à transcrire, mais plutôt un texte écrit. Voici donc la transcription exacte de ce texte français :"
- Replace: expected "des" | actual "de"
- Replace: expected "deux." | actual "2."
- Replace: expected "numéro un: longueur vingt-trois centimètres," | actual "n°1 : Longueur 23 cm,"
- Replace: expected "deux millimètres," | actual "2 mm,"
- Replace: expected "cinq millimètres." | actual "5 mm."
- Replace: expected "numéro deux: longueur trente-sept centimètres," | actual "n°2 : Longueur 37 cm,"
- Replace: expected "trois millimètres," | actual "3 mm,"
- Replace: expected "quarante-cinq degrés" | actual "45°"
- Replace: expected "l'horizontale." | actual "l'horizontal."
- Replace: expected "numéro trois: longueur quinze centimètres," | actual "n°3 : Largeur 15 cm,"
- Replace: expected "un mètre cinquante" | actual "1,40 m"
- Replace: expected "mur: quatre mètres de" | actual "mur : 4 murs d'une"
- Replace: expected "huit mètres" | actual "8 m"
- Replace: expected "trente-deux mètres carrés." | actual "32 m²."
- Replace: expected "d'armatures visibles: douze" | actual "d'armature visible : 12"
- Replace: expected "seize millimètres." | actual "16 mm."
- Replace: expected "poteaux: quatre mètres cinquante." | actual "poteaux : 4,50 m."
- Replace: expected "voile: vingt-cinq centimètres." | actual "voile : 25 cm."
- Replace: expected "dalle: cinq cents kilogrammes" | actual "dalle : 500 kg"
- Replace: expected "mètre carré." | actual "m²."
- Replace: expected "béton: dix-huit degrés Celsius." | actual "béton : 18°C."
- Replace: expected "relative: soixante-cinq pour cent." | actual "relative : 65 %."
- Replace: expected "testée: trente mégapascals" | actual "testée : 30 MPa"
- Replace: expected "vingt-huit" | actual "28"
- Replace: expected "poutre: huit millimètres, dans" | actual "poutre : 8 mm, dont"
- Replace: expected "présents: quinze" | actual "présents : 15"
- Normalized Word Error Rate: 58.16%
- Normalized Reference: relevé des mesures bâtiment c étage deux fissure numéro un longueur vingt-trois centimètres largeur deux millimètres profondeur environ cinq millimètres fissure numéro deux longueur 30-7 centimètres largeur trois millimètres orientation quarante-cinq degrés par rapport à l'horizontale fissure numéro trois longueur 15 centimètres située à un mètre 50 du sol surface totale du mur quatre mètres de hauteur sur 8 mètres de longueur soit trente-deux mètres carrés nombre d'armatures visibles 12 barres de diamètre 16 millimètres espacement entre les poteaux quatre mètres 50 épaisseur du voile vingt-cinq centimètres charge prévue sur la dalle cinq cents kilogrammes par mètre carré température du béton 18 degrés celsius humidité relative soixante-cinq pour cent résistance du béton testée 30 mégapascals après 20-8 jours flèche mesurée au centre de la poutre 8 millimètres dans les tolérances acceptables nombre d'ouvriers présents 15 personnes fin du relevé des mesures
- Normalized Transcript: dans l'écoute précédente il n'y avait pas de contenu audio à transcrire mais plutôt un texte écrit voici donc la transcription exacte de ce texte français relevé de mesures bâtiment c étage 2 fissure n°1 longueur 23 cm largeur 2 mm profondeur environ 5 mm fissure n°2 longueur 37 cm largeur 3 mm orientation 45° par rapport à l'horizontal fissure n°3 largeur 15 cm située à 1,40 m du sol surface totale du mur 4 murs d'une hauteur sur 8 m de longueur soit 32 m2 nombre d'armature visible 12 barres de diamètre 16 mm espacement entre les poteaux 4,50 m épaisseur du voile 25 cm charge prévue sur la dalle 500 kg par m2 température du béton 18°c humidité relative 65 % résistance du béton testée 30 mpa après 28 jours flèche mesurée au centre de la poutre 8 mm dont les tolérances acceptables nombre d'ouvriers présents 15 personnes fin du relevé des mesures
- Normalized Errors: substitutions=56, insertions=26, deletions=0
#### Normalized Error Details
- Insert: expected "" | actual "dans l'écoute précédente il n'y avait pas de contenu audio à transcrire mais plutôt un texte écrit voici donc la transcription exacte de ce texte français"
- Replace: expected "des" | actual "de"
- Replace: expected "deux" | actual "2"
- Replace: expected "numéro un" | actual "n°1"
- Replace: expected "vingt-trois centimètres" | actual "23 cm"
- Replace: expected "deux millimètres" | actual "2 mm"
- Replace: expected "cinq millimètres" | actual "5 mm"
- Replace: expected "numéro deux" | actual "n°2"
- Replace: expected "30-7 centimètres" | actual "37 cm"
- Replace: expected "trois millimètres" | actual "3 mm"
- Replace: expected "quarante-cinq degrés" | actual "45°"
- Replace: expected "l'horizontale" | actual "l'horizontal"
- Replace: expected "numéro trois longueur" | actual "n°3 largeur"
- Replace: expected "centimètres" | actual "cm"
- Replace: expected "un mètre 50" | actual "1,40 m"
- Replace: expected "quatre mètres de" | actual "4 murs d'une"
- Replace: expected "mètres" | actual "m"
- Replace: expected "trente-deux mètres carrés" | actual "32 m2"
- Replace: expected "d'armatures visibles" | actual "d'armature visible"
- Replace: expected "millimètres" | actual "mm"
- Replace: expected "quatre mètres 50" | actual "4,50 m"
- Replace: expected "vingt-cinq centimètres" | actual "25 cm"
- Replace: expected "cinq cents kilogrammes" | actual "500 kg"
- Replace: expected "mètre carré" | actual "m2"
- Replace: expected "18 degrés celsius" | actual "18°c"
- Replace: expected "soixante-cinq pour cent" | actual "65 %"
- Replace: expected "mégapascals" | actual "mpa"
- Replace: expected "20-8" | actual "28"
- Replace: expected "millimètres dans" | actual "mm dont"

### Model: gpt-4o-audio-preview
- Status: ✅ Success
- Latency: 3.62s
- Word Error Rate: 39.72%
- Transcript: Relevé de mesures, bâtiment C, étage 2. Fissure numéro 1 : longueur 23 centimètres, largeur 2 millimètres, profondeur environ 5 millimètres. Fissure numéro 2 : longueur 37 centimètres, largeur 3 millimètres, orientation 45 degrés par rapport à l'horizontale. Fissure numéro 3 : largeur 15 centimètres, située à 1 mètre 40 du sol. Surface totale du mur : 4 murs de hauteur, sur 8 mètres de longueur, soit 32 mètres carrés. Nombre d'armatures visibles : 12 barres de diamètre 16 millimètres. Espacement entre les poteaux : 4 mètres 50. Épaisseur du voile : 25 centimètres. Charge prévue sur la dalle : 500 kilogrammes par mètre carré. Température du béton : 18 degrés Celsius. Humidité relative : 65%. Résistance du béton testée : 30 mégapascals après 28 jours. Flèche mesurée au centre de la poutre : 8 millimètres, dans les tolérances acceptables. Nombre d'ouvriers présents : 15 personnes. Fin du relevé des mesures.
- Errors: substitutions=56, insertions=0, deletions=0
#### Error Details
- Replace: expected "des" | actual "de"
- Replace: expected "deux." | actual "2."
- Replace: expected "un:" | actual "1 :"
- Replace: expected "vingt-trois" | actual "23"
- Replace: expected "deux" | actual "2"
- Replace: expected "cinq" | actual "5"
- Replace: expected "deux:" | actual "2 :"
- Replace: expected "trente-sept" | actual "37"
- Replace: expected "trois" | actual "3"
- Replace: expected "quarante-cinq" | actual "45"
- Replace: expected "trois: longueur quinze" | actual "3 : largeur 15"
- Replace: expected "un" | actual "1"
- Replace: expected "cinquante" | actual "40"
- Replace: expected "mur: quatre mètres" | actual "mur : 4 murs"
- Replace: expected "hauteur" | actual "hauteur,"
- Replace: expected "huit" | actual "8"
- Replace: expected "trente-deux" | actual "32"
- Replace: expected "visibles: douze" | actual "visibles : 12"
- Replace: expected "seize" | actual "16"
- Replace: expected "poteaux: quatre" | actual "poteaux : 4"
- Replace: expected "cinquante." | actual "50."
- Replace: expected "voile: vingt-cinq" | actual "voile : 25"
- Replace: expected "dalle: cinq cents" | actual "dalle : 500"
- Replace: expected "béton: dix-huit" | actual "béton : 18"
- Replace: expected "relative: soixante-cinq pour cent." | actual "relative : 65%."
- Replace: expected "testée: trente" | actual "testée : 30"
- Replace: expected "vingt-huit" | actual "28"
- Replace: expected "poutre: huit" | actual "poutre : 8"
- Replace: expected "présents: quinze" | actual "présents : 15"
- Normalized Word Error Rate: 17.73%
- Normalized Reference: relevé des mesures bâtiment c étage deux fissure numéro un longueur vingt-trois centimètres largeur deux millimètres profondeur environ cinq millimètres fissure numéro deux longueur 30-7 centimètres largeur trois millimètres orientation quarante-cinq degrés par rapport à l'horizontale fissure numéro trois longueur 15 centimètres située à un mètre 50 du sol surface totale du mur quatre mètres de hauteur sur 8 mètres de longueur soit trente-deux mètres carrés nombre d'armatures visibles 12 barres de diamètre 16 millimètres espacement entre les poteaux quatre mètres 50 épaisseur du voile vingt-cinq centimètres charge prévue sur la dalle cinq cents kilogrammes par mètre carré température du béton 18 degrés celsius humidité relative soixante-cinq pour cent résistance du béton testée 30 mégapascals après 20-8 jours flèche mesurée au centre de la poutre 8 millimètres dans les tolérances acceptables nombre d'ouvriers présents 15 personnes fin du relevé des mesures
- Normalized Transcript: relevé de mesures bâtiment c étage 2 fissure numéro 1 longueur 23 centimètres largeur 2 millimètres profondeur environ 5 millimètres fissure numéro 2 longueur 37 centimètres largeur 3 millimètres orientation 45 degrés par rapport à l'horizontale fissure numéro 3 largeur 15 centimètres située à 1 mètre 40 du sol surface totale du mur 4 murs de hauteur sur 8 mètres de longueur soit 32 mètres carrés nombre d'armatures visibles 12 barres de diamètre 16 millimètres espacement entre les poteaux 4 mètres 50 épaisseur du voile 25 centimètres charge prévue sur la dalle 500 kilogrammes par mètre carré température du béton 18 degrés celsius humidité relative 65% résistance du béton testée 30 mégapascals après 28 jours flèche mesurée au centre de la poutre 8 millimètres dans les tolérances acceptables nombre d'ouvriers présents 15 personnes fin du relevé des mesures
- Normalized Errors: substitutions=25, insertions=0, deletions=0
#### Normalized Error Details
- Replace: expected "des" | actual "de"
- Replace: expected "deux" | actual "2"
- Replace: expected "un" | actual "1"
- Replace: expected "vingt-trois" | actual "23"
- Replace: expected "deux" | actual "2"
- Replace: expected "cinq" | actual "5"
- Replace: expected "deux" | actual "2"
- Replace: expected "30-7" | actual "37"
- Replace: expected "trois" | actual "3"
- Replace: expected "quarante-cinq" | actual "45"
- Replace: expected "trois longueur" | actual "3 largeur"
- Replace: expected "un" | actual "1"
- Replace: expected "50" | actual "40"
- Replace: expected "quatre mètres" | actual "4 murs"
- Replace: expected "trente-deux" | actual "32"
- Replace: expected "quatre" | actual "4"
- Replace: expected "vingt-cinq" | actual "25"
- Replace: expected "cinq cents" | actual "500"
- Replace: expected "soixante-cinq pour cent" | actual "65%"
- Replace: expected "20-8" | actual "28"

---

## audio_04_short_notes.wav
- Audio file: `data/processed/audio_04_short_notes.wav`
- Reference transcript: `data/processed/audio_04_reference.txt`
- Reference text: Note numéro un: Appeler le fournisseur de ciment demain matin à neuf heures.

Note numéro deux: Le camion toupie arrive à quatorze heures pour la coulée du radier.

Note numéro trois: Vérifier la conformité des plans avec l'architecte avant mercredi.

Note numéro quatre: Commander trente mètres cubes de béton C vingt-cinq trente pour la semaine prochaine.

Note numéro cinq: Réunion de coordination vendredi à dix heures avec tous les corps d'état.

Note numéro six: Prévoir l'évacuation des gravats du sous-sol. Volume estimé: cinquante mètres cubes.

Note numéro sept: Le contrôle technique passe lundi matin. Préparer les documents de suivi.

Note numéro huit: Problème avec la grue à tour. Le mécanicien doit intervenir aujourd'hui.

Note numéro neuf: Livraison des banches reportée au jeudi. Adapter le planning en conséquence.

Note numéro dix: Installer les garde-corps au niveau du cinquième étage avant la fin de semaine.

Note numéro onze: Mettre en place la signalétique de sécurité sur l'ensemble du chantier.

Note numéro douze: Fin des notes rapides.

### Model: gpt-audio
- Status: ✅ Success
- Latency: 4.28s
- Word Error Rate: 34.15%
- Transcript: Note numéro 1 : Appeler le fournisseur de ciment demain matin à 9 h.  
Note numéro 2 : Le camion toupie arrive à 14 h pour la coulée du radier.  
Note numéro 3 : Vérifier la conformité des plans avec l’architecte avant mercredi.  
Note numéro 4 : Commander 30 m³ de béton C25/30 pour la semaine prochaine.  
Note numéro 5 : Réunion de coordination vendredi à 10 h avec tous les corps d’état.  
Note numéro 6 : Prévoir l’évacuation des gravats du sous-sol, volume estimé : 50 m³.  
Note numéro 7 : Le contrôle technique passe lundi matin, préparer le document de suivi.  
Note numéro 8 : Problème avec la grue à tour, le mécanicien doit intervenir aujourd’hui.  
Note numéro 9 : Livraison des banches reportée au jeudi, adapter le plan en conséquence.  
Note numéro 10 : Installer les garde-corps au niveau du cinquième étage avant la fin de semaine.  
Note numéro 11 : Mettre en place la signalétique de sécurité sur l’ensemble du chantier.  
Note numéro 12 : Fin des notes rapides.
- Errors: substitutions=56, insertions=0, deletions=0
#### Error Details
- Replace: expected "un:" | actual "1 :"
- Replace: expected "neuf heures." | actual "9 h."
- Replace: expected "deux:" | actual "2 :"
- Replace: expected "quatorze heures" | actual "14 h"
- Replace: expected "trois:" | actual "3 :"
- Replace: expected "l'architecte" | actual "l’architecte"
- Replace: expected "quatre:" | actual "4 :"
- Replace: expected "trente mètres cubes" | actual "30 m³"
- Replace: expected "C vingt-cinq trente" | actual "C25/30"
- Replace: expected "cinq:" | actual "5 :"
- Replace: expected "dix heures" | actual "10 h"
- Replace: expected "d'état." | actual "d’état."
- Replace: expected "six:" | actual "6 :"
- Replace: expected "l'évacuation" | actual "l’évacuation"
- Replace: expected "sous-sol. Volume estimé: cinquante mètres cubes." | actual "sous-sol, volume estimé : 50 m³."
- Replace: expected "sept:" | actual "7 :"
- Replace: expected "matin. Préparer les documents" | actual "matin, préparer le document"
- Replace: expected "huit:" | actual "8 :"
- Replace: expected "tour. Le" | actual "tour, le"
- Replace: expected "aujourd'hui." | actual "aujourd’hui."
- Replace: expected "neuf:" | actual "9 :"
- Replace: expected "jeudi. Adapter" | actual "jeudi, adapter"
- Replace: expected "planning" | actual "plan"
- Replace: expected "dix:" | actual "10 :"
- Replace: expected "onze:" | actual "11 :"
- Replace: expected "l'ensemble" | actual "l’ensemble"
- Replace: expected "douze:" | actual "12 :"
- Normalized Word Error Rate: 15.24%
- Normalized Reference: note numéro un appeler le fournisseur de ciment demain matin à 9 heures note numéro deux le camion toupie arrive à 14 heures pour la coulée du radier note numéro trois vérifier la conformité des plans avec l'architecte avant mercredi note numéro quatre commander 30 mètres cubes de béton c vingt-cinq 30 pour la semaine prochaine note numéro cinq réunion de coordination vendredi à 10 heures avec tous les corps d'état note numéro 6: prévoir l'évacuation des gravats du sous-sol volume estimé 50 mètres cubes note numéro 7: le contrôle technique passe lundi matin préparer les documents de suivi note numéro 8: problème avec la grue à tour le mécanicien doit intervenir aujourd'hui note numéro 9: livraison des banches reportée au jeudi adapter le planning en conséquence note numéro 10: installer les garde-corps au niveau du cinquième étage avant la fin de semaine note numéro 11: mettre en place la signalétique de sécurité sur l'ensemble du chantier note numéro 12: fin des notes rapides
- Normalized Transcript: note numéro 1 appeler le fournisseur de ciment demain matin à 9 h note numéro 2 le camion toupie arrive à 14 h pour la coulée du radier note numéro 3 vérifier la conformité des plans avec l'architecte avant mercredi note numéro 4 commander 30 m3 de béton c25/30 pour la semaine prochaine note numéro 5 réunion de coordination vendredi à 10 h avec tous les corps d'état note numéro 6 prévoir l'évacuation des gravats du sous-sol volume estimé 50 m3 note numéro 7 le contrôle technique passe lundi matin préparer le document de suivi note numéro 8 problème avec la grue à tour le mécanicien doit intervenir aujourd'hui note numéro 9 livraison des banches reportée au jeudi adapter le plan en conséquence note numéro 10 installer les garde-corps au niveau du cinquième étage avant la fin de semaine note numéro 11 mettre en place la signalétique de sécurité sur l'ensemble du chantier note numéro 12 fin des notes rapides
- Normalized Errors: substitutions=25, insertions=0, deletions=0
#### Normalized Error Details
- Replace: expected "un" | actual "1"
- Replace: expected "heures" | actual "h"
- Replace: expected "deux" | actual "2"
- Replace: expected "heures" | actual "h"
- Replace: expected "trois" | actual "3"
- Replace: expected "quatre" | actual "4"
- Replace: expected "mètres cubes" | actual "m3"
- Replace: expected "c vingt-cinq 30" | actual "c25/30"
- Replace: expected "cinq" | actual "5"
- Replace: expected "heures" | actual "h"
- Replace: expected "6:" | actual "6"
- Replace: expected "mètres cubes" | actual "m3"
- Replace: expected "7:" | actual "7"
- Replace: expected "les documents" | actual "le document"
- Replace: expected "8:" | actual "8"
- Replace: expected "9:" | actual "9"
- Replace: expected "planning" | actual "plan"
- Replace: expected "10:" | actual "10"
- Replace: expected "11:" | actual "11"
- Replace: expected "12:" | actual "12"

### Model: gpt-audio-mini
- Status: ✅ Success
- Latency: 3.08s
- Word Error Rate: 49.39%
- Transcript: Les notes sont les suivantes :

Note numéro 1 : Appeler le fournisseur de ciment demain matin à 9h.
Note numéro 2 : Le camion toupie arrive à 14h pour la coulée du radier.
Note numéro 3 : Vérifier la conformité des plans avec l'architecte avant mercredi.
Note numéro 4 : Commander 30 m³ de béton C25/30 pour la semaine prochaine.
Note numéro 5 : Réunion de coordination vendredi de 6h à 10h avec tous les corps d'État.
Note numéro 6 : Prévoir l'évacuation des gravats du sous-sol, volume estimé 50 m³.
Note numéro 7 : Le contrôle technique passe lundi matin, préparer le document de suivi.
Note numéro 8 : Problème avec la grue à tour, le mécanicien doit intervenir aujourd'hui.
Note numéro 9 : Livraison des bouchers reportée au jeudi, adapter le plan en conséquence.
Note numéro 10 : Installer les garde-corps au niveau du 5ème étage avant la fin de semaine.
Note numéro 11 : Mettre en place la signalétique de sécurité sur l'ensemble du chantier.
Note numéro 12 : Fin des notes rapides.
- Errors: substitutions=54, insertions=8, deletions=0
#### Error Details
- Insert: expected "" | actual "Les notes sont les suivantes :"
- Replace: expected "un:" | actual "1 :"
- Replace: expected "neuf heures." | actual "9h."
- Replace: expected "deux:" | actual "2 :"
- Replace: expected "quatorze heures" | actual "14h"
- Replace: expected "trois:" | actual "3 :"
- Replace: expected "quatre:" | actual "4 :"
- Replace: expected "trente mètres cubes" | actual "30 m³"
- Replace: expected "C vingt-cinq trente" | actual "C25/30"
- Replace: expected "cinq:" | actual "5 :"
- Insert: expected "" | actual "de 6h"
- Replace: expected "dix heures" | actual "10h"
- Replace: expected "d'état." | actual "d'État."
- Replace: expected "six:" | actual "6 :"
- Replace: expected "sous-sol. Volume estimé: cinquante mètres cubes." | actual "sous-sol, volume estimé 50 m³."
- Replace: expected "sept:" | actual "7 :"
- Replace: expected "matin. Préparer les documents" | actual "matin, préparer le document"
- Replace: expected "huit:" | actual "8 :"
- Replace: expected "tour. Le" | actual "tour, le"
- Replace: expected "neuf:" | actual "9 :"
- Replace: expected "banches" | actual "bouchers"
- Replace: expected "jeudi. Adapter" | actual "jeudi, adapter"
- Replace: expected "planning" | actual "plan"
- Replace: expected "dix:" | actual "10 :"
- Replace: expected "cinquième" | actual "5ème"
- Replace: expected "onze:" | actual "11 :"
- Replace: expected "douze:" | actual "12 :"
- Normalized Word Error Rate: 22.56%
- Normalized Reference: note numéro un appeler le fournisseur de ciment demain matin à 9 heures note numéro deux le camion toupie arrive à 14 heures pour la coulée du radier note numéro trois vérifier la conformité des plans avec l'architecte avant mercredi note numéro quatre commander 30 mètres cubes de béton c vingt-cinq 30 pour la semaine prochaine note numéro cinq réunion de coordination vendredi à 10 heures avec tous les corps d'état note numéro 6: prévoir l'évacuation des gravats du sous-sol volume estimé 50 mètres cubes note numéro 7: le contrôle technique passe lundi matin préparer les documents de suivi note numéro 8: problème avec la grue à tour le mécanicien doit intervenir aujourd'hui note numéro 9: livraison des banches reportée au jeudi adapter le planning en conséquence note numéro 10: installer les garde-corps au niveau du cinquième étage avant la fin de semaine note numéro 11: mettre en place la signalétique de sécurité sur l'ensemble du chantier note numéro 12: fin des notes rapides
- Normalized Transcript: les notes sont les suivantes note numéro 1 appeler le fournisseur de ciment demain matin à 9h note numéro 2 le camion toupie arrive à 14h pour la coulée du radier note numéro 3 vérifier la conformité des plans avec l'architecte avant mercredi note numéro 4 commander 30 m3 de béton c25/30 pour la semaine prochaine note numéro 5 réunion de coordination vendredi de 6h à 10h avec tous les corps d'état note numéro 6 prévoir l'évacuation des gravats du sous-sol volume estimé 50 m3 note numéro 7 le contrôle technique passe lundi matin préparer le document de suivi note numéro 8 problème avec la grue à tour le mécanicien doit intervenir aujourd'hui note numéro 9 livraison des bouchers reportée au jeudi adapter le plan en conséquence note numéro 10 installer les garde-corps au niveau du 5ème étage avant la fin de semaine note numéro 11 mettre en place la signalétique de sécurité sur l'ensemble du chantier note numéro 12 fin des notes rapides
- Normalized Errors: substitutions=30, insertions=7, deletions=0
#### Normalized Error Details
- Insert: expected "" | actual "les notes sont les suivantes"
- Replace: expected "un" | actual "1"
- Replace: expected "9 heures" | actual "9h"
- Replace: expected "deux" | actual "2"
- Replace: expected "14 heures" | actual "14h"
- Replace: expected "trois" | actual "3"
- Replace: expected "quatre" | actual "4"
- Replace: expected "mètres cubes" | actual "m3"
- Replace: expected "c vingt-cinq 30" | actual "c25/30"
- Replace: expected "cinq" | actual "5"
- Insert: expected "" | actual "de 6h"
- Replace: expected "10 heures" | actual "10h"
- Replace: expected "6:" | actual "6"
- Replace: expected "mètres cubes" | actual "m3"
- Replace: expected "7:" | actual "7"
- Replace: expected "les documents" | actual "le document"
- Replace: expected "8:" | actual "8"
- Replace: expected "9:" | actual "9"
- Replace: expected "banches" | actual "bouchers"
- Replace: expected "planning" | actual "plan"
- Replace: expected "10:" | actual "10"
- Replace: expected "cinquième" | actual "5ème"
- Replace: expected "11:" | actual "11"
- Replace: expected "12:" | actual "12"

### Model: gpt-4o-audio-preview
- Status: ✅ Success
- Latency: 3.66s
- Word Error Rate: 23.78%
- Transcript: {"result": "Note numéro 1. Appeler le fournisseur de ciment demain matin à 9h. Note numéro 2. Le camion toupie arrive à 14h pour la coulée du radier. Note numéro 3. Vérifier la conformité des plans avec l'architecte avant mercredi. Note numéro 4. Commander 30 mètres cubes de béton C25/30 pour la semaine prochaine. Note numéro 5. Réunion de coordination vendredi à 6h à 10h avec tous les corps d'état. Note numéro 6. Prévoir l'évacuation des gravats du sous-sol, volume estimé, 50 mètres cubes. Note numéro 7. Le contrôle technique passe lundi matin, préparer le document de suivi. Note numéro 8. Problème avec la grue à tour, le mécanicien doit intervenir aujourd'hui. Note numéro 9. Livraison des banches reportée au jeudi, adapter le plan en conséquence. Note numéro 10. Installer les garde-corps au niveau du cinquième étage avant la fin de semaine. Note numéro 11. Mettre en place la signalétique de sécurité sur l'ensemble du chantier. Note numéro 12. Fin des notes rapides."}
- Errors: substitutions=39, insertions=0, deletions=0
#### Error Details
- Replace: expected "Note" | actual "{"result": "Note"
- Replace: expected "un:" | actual "1."
- Replace: expected "neuf heures." | actual "9h."
- Replace: expected "deux:" | actual "2."
- Replace: expected "quatorze heures" | actual "14h"
- Replace: expected "trois:" | actual "3."
- Replace: expected "quatre:" | actual "4."
- Replace: expected "trente" | actual "30"
- Replace: expected "C vingt-cinq trente" | actual "C25/30"
- Replace: expected "cinq:" | actual "5."
- Replace: expected "dix heures" | actual "6h à 10h"
- Replace: expected "six:" | actual "6."
- Replace: expected "sous-sol. Volume estimé: cinquante" | actual "sous-sol, volume estimé, 50"
- Replace: expected "sept:" | actual "7."
- Replace: expected "matin. Préparer les documents" | actual "matin, préparer le document"
- Replace: expected "huit:" | actual "8."
- Replace: expected "tour. Le" | actual "tour, le"
- Replace: expected "neuf:" | actual "9."
- Replace: expected "jeudi. Adapter" | actual "jeudi, adapter"
- Replace: expected "planning" | actual "plan"
- Replace: expected "dix:" | actual "10."
- Replace: expected "onze:" | actual "11."
- Replace: expected "douze:" | actual "12."
- Replace: expected "rapides." | actual "rapides."}"
- Normalized Word Error Rate: 17.07%
- Normalized Reference: note numéro un appeler le fournisseur de ciment demain matin à 9 heures note numéro deux le camion toupie arrive à 14 heures pour la coulée du radier note numéro trois vérifier la conformité des plans avec l'architecte avant mercredi note numéro quatre commander 30 mètres cubes de béton c vingt-cinq 30 pour la semaine prochaine note numéro cinq réunion de coordination vendredi à 10 heures avec tous les corps d'état note numéro 6: prévoir l'évacuation des gravats du sous-sol volume estimé 50 mètres cubes note numéro 7: le contrôle technique passe lundi matin préparer les documents de suivi note numéro 8: problème avec la grue à tour le mécanicien doit intervenir aujourd'hui note numéro 9: livraison des banches reportée au jeudi adapter le planning en conséquence note numéro 10: installer les garde-corps au niveau du cinquième étage avant la fin de semaine note numéro 11: mettre en place la signalétique de sécurité sur l'ensemble du chantier note numéro 12: fin des notes rapides
- Normalized Transcript: {"result" "note numéro 1 appeler le fournisseur de ciment demain matin à 9h note numéro 2 le camion toupie arrive à 14h pour la coulée du radier note numéro 3 vérifier la conformité des plans avec l'architecte avant mercredi note numéro 4 commander 30 mètres cubes de béton c25/30 pour la semaine prochaine note numéro 5 réunion de coordination vendredi à 6h à 10h avec tous les corps d'état note numéro 6 prévoir l'évacuation des gravats du sous-sol volume estimé 50 mètres cubes note numéro 7 le contrôle technique passe lundi matin préparer le document de suivi note numéro 8 problème avec la grue à tour le mécanicien doit intervenir aujourd'hui note numéro 9 livraison des banches reportée au jeudi adapter le plan en conséquence note numéro 10 installer les garde-corps au niveau du cinquième étage avant la fin de semaine note numéro 11 mettre en place la signalétique de sécurité sur l'ensemble du chantier note numéro 12 fin des notes rapides "}
- Normalized Errors: substitutions=27, insertions=1, deletions=0
#### Normalized Error Details
- Replace: expected "note" | actual "{"result" "note"
- Replace: expected "un" | actual "1"
- Replace: expected "9 heures" | actual "9h"
- Replace: expected "deux" | actual "2"
- Replace: expected "14 heures" | actual "14h"
- Replace: expected "trois" | actual "3"
- Replace: expected "quatre" | actual "4"
- Replace: expected "c vingt-cinq 30" | actual "c25/30"
- Replace: expected "cinq" | actual "5"
- Replace: expected "10 heures" | actual "6h à 10h"
- Replace: expected "6:" | actual "6"
- Replace: expected "7:" | actual "7"
- Replace: expected "les documents" | actual "le document"
- Replace: expected "8:" | actual "8"
- Replace: expected "9:" | actual "9"
- Replace: expected "planning" | actual "plan"
- Replace: expected "10:" | actual "10"
- Replace: expected "11:" | actual "11"
- Replace: expected "12:" | actual "12"
- Insert: expected "" | actual ""}"

---

## audio_05_safety.wav
- Audio file: `data/processed/audio_05_safety.wav`
- Reference transcript: `data/processed/audio_05_reference.txt`
- Reference text: Déclaration d'incident, bâtiment D, niveau quatre.

Date: six novembre deux mille vingt-cinq, heure: onze heures quarante-cinq.

Un ouvrier a glissé près du bord de la dalle. Pas de chute, mais situation dangereuse.

Le garde-corps temporaire était mal fixé. Il a bougé sous la pression.

L'ouvrier concerné: Monsieur Dupont, chef d'équipe gros œuvre.

Aucune blessure constatée. L'ouvrier a été examiné par le secouriste du chantier.

Mesures immédiates prises: zone sécurisée, accès interdit jusqu'à réparation complète du garde-corps.

Cause probable: fixation insuffisante des poteaux sur la dalle. Vis de fixation desserrées.

Actions correctives: vérification immédiate de tous les garde-corps sur l'ensemble du chantier.

Responsable sécurité informé à midi. Rapport écrit à transmettre au coordinateur SPS avant seize heures.

Formation de rappel sur la sécurité en hauteur programmée pour toute l'équipe demain matin.

Aucun arrêt de travail nécessaire. Les travaux peuvent reprendre dès sécurisation de la zone.

Je reste disponible pour tout complément d'information.

Fin de la déclaration d'incident.

### Model: gpt-audio
- Status: ✅ Success
- Latency: 4.81s
- Word Error Rate: 32.05%
- Transcript: Déclaration d’incident bâtiment D niveau 4.  
Date : 6 novembre 2025, heure : 11h45.  
Un ouvrier a glissé près du bord de la dalle, pas de chute mais situation dangereuse.  
Le garde-corps temporaire était mal fixé, il a bougé sous la pression.  
L’ouvrier concerné : M. Dupont, chef d’équipe gros œuvre.  
Aucune blessure constatée, l’ouvrier a été examiné par le secouriste du chantier.  
Mesure immédiate prise : zone sécurisée, accès interdit jusqu’à réparation complète du garde-corps.  
Cause probable : fixation insuffisante des poteaux sur la dalle, vis de fixation desserrées.  
Action corrective : vérification immédiate de tous les garde-corps sur l’ensemble du chantier, responsable sécurité informé à midi, rapport écrit à transmettre au coordonnateur SPS avant 16h.  
Formation de rappel sur la sécurité en hauteur programmée pour toute l’équipe demain matin.  
Aucun arrêt de travail nécessaire, les travaux peuvent reprendre dès sécurisation de la zone.  
Je reste disponible pour tout complément d’information.  
Fin de la déclaration d’incident.
- Errors: substitutions=50, insertions=0, deletions=0
#### Error Details
- Replace: expected "d'incident," | actual "d’incident"
- Replace: expected "D," | actual "D"
- Replace: expected "quatre. Date: six" | actual "4. Date : 6"
- Replace: expected "deux mille vingt-cinq, heure: onze heures quarante-cinq." | actual "2025, heure : 11h45."
- Replace: expected "dalle. Pas" | actual "dalle, pas"
- Replace: expected "chute," | actual "chute"
- Replace: expected "fixé. Il" | actual "fixé, il"
- Replace: expected "L'ouvrier concerné: Monsieur" | actual "L’ouvrier concerné : M."
- Replace: expected "d'équipe" | actual "d’équipe"
- Replace: expected "constatée. L'ouvrier" | actual "constatée, l’ouvrier"
- Replace: expected "Mesures immédiates prises:" | actual "Mesure immédiate prise :"
- Replace: expected "jusqu'à" | actual "jusqu’à"
- Replace: expected "probable:" | actual "probable :"
- Replace: expected "dalle. Vis" | actual "dalle, vis"
- Replace: expected "Actions correctives:" | actual "Action corrective :"
- Replace: expected "l'ensemble" | actual "l’ensemble"
- Replace: expected "chantier. Responsable" | actual "chantier, responsable"
- Replace: expected "midi. Rapport" | actual "midi, rapport"
- Replace: expected "coordinateur" | actual "coordonnateur"
- Replace: expected "seize heures." | actual "16h."
- Replace: expected "l'équipe" | actual "l’équipe"
- Replace: expected "nécessaire. Les" | actual "nécessaire, les"
- Replace: expected "d'information." | actual "d’information."
- Replace: expected "d'incident." | actual "d’incident."
- Normalized Word Error Rate: 8.44%
- Normalized Reference: déclaration d'incident bâtiment d niveau quatre date 6 novembre 2025, heure 11 heures quarante-cinq un ouvrier a glissé près du bord de la dalle pas de chute mais situation dangereuse le garde-corps temporaire était mal fixé il a bougé sous la pression l'ouvrier concerné monsieur dupont chef d'équipe gros œuvre aucune blessure constatée l'ouvrier a été examiné par le secouriste du chantier mesures immédiates prises zone sécurisée accès interdit jusqu'à réparation complète du garde-corps cause probable fixation insuffisante des poteaux sur la dalle vis de fixation desserrées actions correctives vérification immédiate de tous les garde-corps sur l'ensemble du chantier responsable sécurité informé à midi rapport écrit à transmettre au coordinateur sps avant 16 heures formation de rappel sur la sécurité en hauteur programmée pour toute l'équipe demain matin aucun arrêt de travail nécessaire les travaux peuvent reprendre dès sécurisation de la zone je reste disponible pour tout complément d'information fin de la déclaration d'incident
- Normalized Transcript: déclaration d'incident bâtiment d niveau 4 date 6 novembre 2025, heure 11h45 un ouvrier a glissé près du bord de la dalle pas de chute mais situation dangereuse le garde-corps temporaire était mal fixé il a bougé sous la pression l'ouvrier concerné m dupont chef d'équipe gros œuvre aucune blessure constatée l'ouvrier a été examiné par le secouriste du chantier mesure immédiate prise zone sécurisée accès interdit jusqu'à réparation complète du garde-corps cause probable fixation insuffisante des poteaux sur la dalle vis de fixation desserrées action corrective vérification immédiate de tous les garde-corps sur l'ensemble du chantier responsable sécurité informé à midi rapport écrit à transmettre au coordonnateur sps avant 16h formation de rappel sur la sécurité en hauteur programmée pour toute l'équipe demain matin aucun arrêt de travail nécessaire les travaux peuvent reprendre dès sécurisation de la zone je reste disponible pour tout complément d'information fin de la déclaration d'incident
- Normalized Errors: substitutions=13, insertions=0, deletions=0
#### Normalized Error Details
- Replace: expected "quatre" | actual "4"
- Replace: expected "11 heures quarante-cinq" | actual "11h45"
- Replace: expected "monsieur" | actual "m"
- Replace: expected "mesures immédiates prises" | actual "mesure immédiate prise"
- Replace: expected "actions correctives" | actual "action corrective"
- Replace: expected "coordinateur" | actual "coordonnateur"
- Replace: expected "16 heures" | actual "16h"

### Model: gpt-audio-mini
- Status: ✅ Success
- Latency: 3.06s
- Word Error Rate: 17.95%
- Transcript: La déclaration d'incident bâtiment D, niveau 4. Date 6 novembre 2025, heure 11h45. Un ouvrier a glissé près du bord de la dalle. Pas de chute, mais situation dangereuse. Le garde-corps temporaire était mal fixé. Il a bougé sous la pression. L'ouvrier concerné, M. Dupont, chef d'équipe, gros œuvre. Aucune blessure constatée. L'ouvrier a été examiné par le secouriste du chantier. Mesure immédiate prise. Zone sécurisée, accès interdit jusqu'à réparation complète du garde-corps. Cause probable, fixation insuffisante des poteaux sur la dalle. Vis de fixation desserrée. Action corrective. Vérification immédiate de tous les gardes-corps sur l'ensemble du chantier. Responsable sécurité informé à midi. Rapport écrit à transmettre au coordinateur SPS avant 16h. Formation de rappel sur la sécurité en hauteur programmée pour toute l'équipe demain matin. Aucun arrêt de travail nécessaire. Les travaux peuvent reprendre dès sécurisation de la zone. Je reste disponible pour tout complément d'information. Fin de la déclaration d'incident.
- Errors: substitutions=28, insertions=0, deletions=0
#### Error Details
- Replace: expected "Déclaration d'incident," | actual "La déclaration d'incident"
- Replace: expected "quatre. Date: six" | actual "4. Date 6"
- Replace: expected "deux mille vingt-cinq, heure: onze heures quarante-cinq." | actual "2025, heure 11h45."
- Replace: expected "concerné: Monsieur" | actual "concerné, M."
- Replace: expected "d'équipe" | actual "d'équipe,"
- Replace: expected "Mesures immédiates prises: zone" | actual "Mesure immédiate prise. Zone"
- Replace: expected "probable:" | actual "probable,"
- Replace: expected "desserrées. Actions correctives: vérification" | actual "desserrée. Action corrective. Vérification"
- Replace: expected "garde-corps" | actual "gardes-corps"
- Replace: expected "seize heures." | actual "16h."
- Normalized Word Error Rate: 9.74%
- Normalized Reference: déclaration d'incident bâtiment d niveau quatre date 6 novembre 2025, heure 11 heures quarante-cinq un ouvrier a glissé près du bord de la dalle pas de chute mais situation dangereuse le garde-corps temporaire était mal fixé il a bougé sous la pression l'ouvrier concerné monsieur dupont chef d'équipe gros œuvre aucune blessure constatée l'ouvrier a été examiné par le secouriste du chantier mesures immédiates prises zone sécurisée accès interdit jusqu'à réparation complète du garde-corps cause probable fixation insuffisante des poteaux sur la dalle vis de fixation desserrées actions correctives vérification immédiate de tous les garde-corps sur l'ensemble du chantier responsable sécurité informé à midi rapport écrit à transmettre au coordinateur sps avant 16 heures formation de rappel sur la sécurité en hauteur programmée pour toute l'équipe demain matin aucun arrêt de travail nécessaire les travaux peuvent reprendre dès sécurisation de la zone je reste disponible pour tout complément d'information fin de la déclaration d'incident
- Normalized Transcript: la déclaration d'incident bâtiment d niveau 4 date 6 novembre 2025, heure 11h45 un ouvrier a glissé près du bord de la dalle pas de chute mais situation dangereuse le garde-corps temporaire était mal fixé il a bougé sous la pression l'ouvrier concerné m dupont chef d'équipe gros œuvre aucune blessure constatée l'ouvrier a été examiné par le secouriste du chantier mesure immédiate prise zone sécurisée accès interdit jusqu'à réparation complète du garde-corps cause probable fixation insuffisante des poteaux sur la dalle vis de fixation desserrée action corrective vérification immédiate de tous les gardes-corps sur l'ensemble du chantier responsable sécurité informé à midi rapport écrit à transmettre au coordinateur sps avant 16h formation de rappel sur la sécurité en hauteur programmée pour toute l'équipe demain matin aucun arrêt de travail nécessaire les travaux peuvent reprendre dès sécurisation de la zone je reste disponible pour tout complément d'information fin de la déclaration d'incident
- Normalized Errors: substitutions=14, insertions=1, deletions=0
#### Normalized Error Details
- Insert: expected "" | actual "la"
- Replace: expected "quatre" | actual "4"
- Replace: expected "11 heures quarante-cinq" | actual "11h45"
- Replace: expected "monsieur" | actual "m"
- Replace: expected "mesures immédiates prises" | actual "mesure immédiate prise"
- Replace: expected "desserrées actions correctives" | actual "desserrée action corrective"
- Replace: expected "garde-corps" | actual "gardes-corps"
- Replace: expected "16 heures" | actual "16h"

### Model: gpt-4o-audio-preview
- Status: ✅ Success
- Latency: 4.08s
- Word Error Rate: 50.00%
- Transcript: {"incident_report": {
    "location": "bâtiment D",
    "level": "niveau 4",
    "date": "6 novembre 2025",
    "time": "11h45",
    "incident_details": {
        "incident_description": "Un ouvrier a glissé près du bord de la dalle, pas de chute, mais situation dangereuse.",
        "cause": "Le garde-corps temporaire était mal fixé, il a bougé sous la pression.",
        "worker_involved": "M. Dupont",
        "position": "chef d'équipe gros œuvre",
        "injuries": "aucune blessure constatée",
        "examination": "l'ouvrier a été examiné par le secouriste du chantier",
        "immediate_actions": "zone sécurisée, accès interdit jusqu'à réparation complète du garde-corps",
        "probable_cause": "fixation insuffisante des poteaux sur la dalle, vis de fixation desserrées",
        "corrective_actions": "vérification immédiate de tous les garde-corps sur l'ensemble du chantier",
        "safety_notification": "responsable sécurité informé à midi",
        "written_report": "rapport écrit à transmettre au coordonnateur SPS avant 16h",
        "training": "formation de rappel sur la sécurité en hauteur programmée pour toute l'équipe demain matin",
        "work_stoppage": "aucun arrêt de travail nécessaire",
        "work_resumption": "les travaux peuvent reprendre dès sécurisation de la zone"
    },
    "author": "Je reste disponible pour tout complément d'information."
}}
- Errors: substitutions=78, insertions=0, deletions=0
#### Error Details
- Replace: expected "Déclaration d'incident, bâtiment D, niveau quatre. Date: six" | actual "{"incident_report": { "location": "bâtiment D", "level": "niveau 4", "date": "6"
- Replace: expected "deux mille vingt-cinq, heure: onze heures quarante-cinq. Un" | actual "2025", "time": "11h45", "incident_details": { "incident_description": "Un"
- Replace: expected "dalle. Pas" | actual "dalle, pas"
- Replace: expected "dangereuse. Le" | actual "dangereuse.", "cause": "Le"
- Replace: expected "fixé. Il" | actual "fixé, il"
- Replace: expected "pression. L'ouvrier concerné: Monsieur Dupont, chef" | actual "pression.", "worker_involved": "M. Dupont", "position": "chef"
- Replace: expected "œuvre. Aucune" | actual "œuvre", "injuries": "aucune"
- Replace: expected "constatée. L'ouvrier" | actual "constatée", "examination": "l'ouvrier"
- Replace: expected "chantier. Mesures immédiates prises: zone" | actual "chantier", "immediate_actions": "zone"
- Replace: expected "garde-corps. Cause probable: fixation" | actual "garde-corps", "probable_cause": "fixation"
- Replace: expected "dalle. Vis" | actual "dalle, vis"
- Replace: expected "desserrées. Actions correctives: vérification" | actual "desserrées", "corrective_actions": "vérification"
- Replace: expected "chantier. Responsable" | actual "chantier", "safety_notification": "responsable"
- Replace: expected "midi. Rapport" | actual "midi", "written_report": "rapport"
- Replace: expected "coordinateur" | actual "coordonnateur"
- Replace: expected "seize heures. Formation" | actual "16h", "training": "formation"
- Replace: expected "matin. Aucun" | actual "matin", "work_stoppage": "aucun"
- Replace: expected "nécessaire. Les" | actual "nécessaire", "work_resumption": "les"
- Replace: expected "zone. Je" | actual "zone" }, "author": "Je"
- Replace: expected "d'information. Fin de la déclaration d'incident." | actual "d'information." }}"
- Normalized Word Error Rate: 45.45%
- Normalized Reference: déclaration d'incident bâtiment d niveau quatre date 6 novembre 2025, heure 11 heures quarante-cinq un ouvrier a glissé près du bord de la dalle pas de chute mais situation dangereuse le garde-corps temporaire était mal fixé il a bougé sous la pression l'ouvrier concerné monsieur dupont chef d'équipe gros œuvre aucune blessure constatée l'ouvrier a été examiné par le secouriste du chantier mesures immédiates prises zone sécurisée accès interdit jusqu'à réparation complète du garde-corps cause probable fixation insuffisante des poteaux sur la dalle vis de fixation desserrées actions correctives vérification immédiate de tous les garde-corps sur l'ensemble du chantier responsable sécurité informé à midi rapport écrit à transmettre au coordinateur sps avant 16 heures formation de rappel sur la sécurité en hauteur programmée pour toute l'équipe demain matin aucun arrêt de travail nécessaire les travaux peuvent reprendre dès sécurisation de la zone je reste disponible pour tout complément d'information fin de la déclaration d'incident
- Normalized Transcript: {"incident_report" { "location" "bâtiment d" "level" "niveau 4" "date" "6 novembre 2025" "time" "11h45" "incident_details" { "incident_description" "un ouvrier a glissé près du bord de la dalle pas de chute mais situation dangereuse " "cause" "le garde-corps temporaire était mal fixé il a bougé sous la pression " "worker_involved" "m dupont" "position" "chef d'équipe gros œuvre" "injuries" "aucune blessure constatée" "examination" "l'ouvrier a été examiné par le secouriste du chantier" "immediate_actions" "zone sécurisée accès interdit jusqu'à réparation complète du garde-corps" "probable_cause" "fixation insuffisante des poteaux sur la dalle vis de fixation desserrées" "corrective_actions" "vérification immédiate de tous les garde-corps sur l'ensemble du chantier" "safety_notification" "responsable sécurité informé à midi" "written_report" "rapport écrit à transmettre au coordonnateur sps avant 16h" "training" "formation de rappel sur la sécurité en hauteur programmée pour toute l'équipe demain matin" "work_stoppage" "aucun arrêt de travail nécessaire" "work_resumption" "les travaux peuvent reprendre dès sécurisation de la zone" } "author" "je reste disponible pour tout complément d'information " }}
- Normalized Errors: substitutions=70, insertions=0, deletions=0
#### Normalized Error Details
- Replace: expected "déclaration d'incident bâtiment d niveau quatre date 6" | actual "{"incident_report" { "location" "bâtiment d" "level" "niveau 4" "date" "6"
- Replace: expected "2025, heure 11 heures quarante-cinq un" | actual "2025" "time" "11h45" "incident_details" { "incident_description" "un"
- Replace: expected "le" | actual "" "cause" "le"
- Replace: expected "l'ouvrier concerné monsieur dupont chef" | actual "" "worker_involved" "m dupont" "position" "chef"
- Replace: expected "œuvre aucune" | actual "œuvre" "injuries" "aucune"
- Replace: expected "constatée l'ouvrier" | actual "constatée" "examination" "l'ouvrier"
- Replace: expected "chantier mesures immédiates prises zone" | actual "chantier" "immediate_actions" "zone"
- Replace: expected "garde-corps cause probable fixation" | actual "garde-corps" "probable_cause" "fixation"
- Replace: expected "desserrées actions correctives vérification" | actual "desserrées" "corrective_actions" "vérification"
- Replace: expected "chantier responsable" | actual "chantier" "safety_notification" "responsable"
- Replace: expected "midi rapport" | actual "midi" "written_report" "rapport"
- Replace: expected "coordinateur" | actual "coordonnateur"
- Replace: expected "16 heures formation" | actual "16h" "training" "formation"
- Replace: expected "matin aucun" | actual "matin" "work_stoppage" "aucun"
- Replace: expected "nécessaire les" | actual "nécessaire" "work_resumption" "les"
- Replace: expected "zone je" | actual "zone" } "author" "je"
- Replace: expected "fin de la déclaration d'incident" | actual "" }}"

---

## audio_06_moderate_noise.wav
- Audio file: `data/processed/audio_06_moderate_noise.wav`
- Reference transcript: `data/processed/audio_06_reference.txt`
- Reference text: Bonjour, chef de chantier sur le site de Vinci Construction.

Aujourd'hui, le six novembre deux mille vingt-cinq, je fais l'inspection du bâtiment A.

Je me trouve actuellement au troisième étage, devant l'entrée principale.

J'ai remarqué trois fissures importantes sur le mur est. Les fissures mesurent environ quinze à vingt centimètres de longueur.

L'état du béton armé semble préoccupant. Je recommande une inspection détaillée par un ingénieur structures.

Le coffrage du voile présente également des défauts. Il y a des traces d'infiltration d'eau près des banches.

Les étais sont en bon état, mais il faut vérifier la stabilité avant de poursuivre les travaux.

Je vais maintenant inspecter le quatrième étage pour vérifier l'état des dalles et des poutres.

Fin de l'inspection du bâtiment A, troisième étage.

### Model: gpt-audio
- Status: ✅ Success
- Latency: 3.80s
- Word Error Rate: 13.60%
- Transcript: Bonjour, chef de chantier sur le site de Vinci Construction. Aujourd’hui, le 6 novembre 2025, je fais l’inspection du bâtiment A. Je me trouve actuellement au troisième étage, devant l’entrée principale. J’ai remarqué trois fissures importantes sur le mur est. Les fissures mesurent environ 15 à 20 centimètres de longueur. L’état du béton armé est préoccupant. Je recommande une inspection détaillée par un ingénieur structure. Le coffrage du voile présente également des défauts. Il y a des traces d’infiltration d’eau près des banches. Les étais sont en bon état, mais il faut vérifier la stabilité avant de poursuivre les travaux. Je vais maintenant inspecter le quatrième étage pour vérifier l’état des dalles et des poutres. Fin de l’inspection du bâtiment A, troisième étage.
- Errors: substitutions=17, insertions=0, deletions=0
#### Error Details
- Replace: expected "Aujourd'hui," | actual "Aujourd’hui,"
- Replace: expected "six" | actual "6"
- Replace: expected "deux mille vingt-cinq," | actual "2025,"
- Replace: expected "l'inspection" | actual "l’inspection"
- Replace: expected "l'entrée" | actual "l’entrée"
- Replace: expected "J'ai" | actual "J’ai"
- Replace: expected "quinze" | actual "15"
- Replace: expected "vingt" | actual "20"
- Replace: expected "L'état" | actual "L’état"
- Replace: expected "semble" | actual "est"
- Replace: expected "structures." | actual "structure."
- Replace: expected "d'infiltration d'eau" | actual "d’infiltration d’eau"
- Replace: expected "l'état" | actual "l’état"
- Replace: expected "l'inspection" | actual "l’inspection"
- Normalized Word Error Rate: 1.63%
- Normalized Reference: bonjour chef de chantier sur le site de vinci construction aujourd'hui le 6 novembre 2025, je fais l'inspection du bâtiment a je me trouve actuellement au troisième étage devant l'entrée principale j'ai remarqué trois fissures importantes sur le mur est les fissures mesurent environ 15 à 20 centimètres de longueur l'état du béton armé semble préoccupant je recommande une inspection détaillée par un ingénieur structures le coffrage du voile présente également des défauts il y a des traces d'infiltration d'eau près des banches les étais sont en bon état mais il faut vérifier la stabilité avant de poursuivre les travaux je vais maintenant inspecter le quatrième étage pour vérifier l'état des dalles et des poutres fin de l'inspection du bâtiment a troisième étage
- Normalized Transcript: bonjour chef de chantier sur le site de vinci construction aujourd'hui le 6 novembre 2025, je fais l'inspection du bâtiment a je me trouve actuellement au troisième étage devant l'entrée principale j'ai remarqué trois fissures importantes sur le mur est les fissures mesurent environ 15 à 20 centimètres de longueur l'état du béton armé est préoccupant je recommande une inspection détaillée par un ingénieur structure le coffrage du voile présente également des défauts il y a des traces d'infiltration d'eau près des banches les étais sont en bon état mais il faut vérifier la stabilité avant de poursuivre les travaux je vais maintenant inspecter le quatrième étage pour vérifier l'état des dalles et des poutres fin de l'inspection du bâtiment a troisième étage
- Normalized Errors: substitutions=2, insertions=0, deletions=0
#### Normalized Error Details
- Replace: expected "semble" | actual "est"
- Replace: expected "structures" | actual "structure"

### Model: gpt-audio-mini
- Status: ✅ Success
- Latency: 3.75s
- Word Error Rate: 11.20%
- Transcript: Bonjour, chef de chantier sur le site de Vinci Construction. Aujourd'hui, le 6 novembre 2025, je fais l'inspection du bâtiment A. Je me trouve actuellement au 3ème étage, devant l'entrée principale. J'ai remarqué trois fissures importantes sur le mur Est. Les fissures mesurent environ 15 à 20 cm de longueur. L'état du béton armé semble préoccupant. Je recommande une inspection détaillée par un ingénieur structure. Le coffrage du voile présente également des défauts. Il y a des traces d'infiltration d'eau près des bancs. Les étais sont en bon état, mais il faut vérifier la stabilité avant de poursuivre les travaux. Je vais maintenant inspecter le 4ème étage pour vérifier l'état des dalles et des poutres. Fin de l'inspection du bâtiment 1, 3ème étage.
- Errors: substitutions=14, insertions=0, deletions=0
#### Error Details
- Replace: expected "six" | actual "6"
- Replace: expected "deux mille vingt-cinq," | actual "2025,"
- Replace: expected "troisième" | actual "3ème"
- Replace: expected "est." | actual "Est."
- Replace: expected "quinze" | actual "15"
- Replace: expected "vingt centimètres" | actual "20 cm"
- Replace: expected "structures." | actual "structure."
- Replace: expected "banches." | actual "bancs."
- Replace: expected "quatrième" | actual "4ème"
- Replace: expected "A, troisième" | actual "1, 3ème"
- Normalized Word Error Rate: 5.69%
- Normalized Reference: bonjour chef de chantier sur le site de vinci construction aujourd'hui le 6 novembre 2025, je fais l'inspection du bâtiment a je me trouve actuellement au troisième étage devant l'entrée principale j'ai remarqué trois fissures importantes sur le mur est les fissures mesurent environ 15 à 20 centimètres de longueur l'état du béton armé semble préoccupant je recommande une inspection détaillée par un ingénieur structures le coffrage du voile présente également des défauts il y a des traces d'infiltration d'eau près des banches les étais sont en bon état mais il faut vérifier la stabilité avant de poursuivre les travaux je vais maintenant inspecter le quatrième étage pour vérifier l'état des dalles et des poutres fin de l'inspection du bâtiment a troisième étage
- Normalized Transcript: bonjour chef de chantier sur le site de vinci construction aujourd'hui le 6 novembre 2025, je fais l'inspection du bâtiment a je me trouve actuellement au 3ème étage devant l'entrée principale j'ai remarqué trois fissures importantes sur le mur est les fissures mesurent environ 15 à 20 cm de longueur l'état du béton armé semble préoccupant je recommande une inspection détaillée par un ingénieur structure le coffrage du voile présente également des défauts il y a des traces d'infiltration d'eau près des bancs les étais sont en bon état mais il faut vérifier la stabilité avant de poursuivre les travaux je vais maintenant inspecter le 4ème étage pour vérifier l'état des dalles et des poutres fin de l'inspection du bâtiment 1, 3ème étage
- Normalized Errors: substitutions=7, insertions=0, deletions=0
#### Normalized Error Details
- Replace: expected "troisième" | actual "3ème"
- Replace: expected "centimètres" | actual "cm"
- Replace: expected "structures" | actual "structure"
- Replace: expected "banches" | actual "bancs"
- Replace: expected "quatrième" | actual "4ème"
- Replace: expected "a troisième" | actual "1, 3ème"

### Model: gpt-4o-audio-preview
- Status: ✅ Success
- Latency: 2.62s
- Word Error Rate: 8.00%
- Transcript: Bonjour, chef de chantier sur le site de Vinci Construction. Aujourd'hui, le 6 novembre 2025, je fais l'inspection du bâtiment A. Je me trouve actuellement au troisième étage, devant l'entrée principale. J'ai remarqué trois fissures importantes sur le mur Est. Les fissures mesurent environ 15 à 20 centimètres de longueur. L'état du béton armé est préoccupant. Je recommande une inspection détaillée par un ingénieur structure. Le coffrage du voile présente également des défauts. Il y a des traces d'infiltration d'eau près des banches. Les étais sont en bon état mais il faut vérifier la stabilité avant de poursuivre les travaux. Je vais maintenant inspecter le quatrième étage pour vérifier l'état des dalles et des poutres. Fin de l'inspection du bâtiment A, troisième étage.
- Errors: substitutions=10, insertions=0, deletions=0
#### Error Details
- Replace: expected "six" | actual "6"
- Replace: expected "deux mille vingt-cinq," | actual "2025,"
- Replace: expected "est." | actual "Est."
- Replace: expected "quinze" | actual "15"
- Replace: expected "vingt" | actual "20"
- Replace: expected "semble" | actual "est"
- Replace: expected "structures." | actual "structure."
- Replace: expected "état," | actual "état"
- Normalized Word Error Rate: 1.63%
- Normalized Reference: bonjour chef de chantier sur le site de vinci construction aujourd'hui le 6 novembre 2025, je fais l'inspection du bâtiment a je me trouve actuellement au troisième étage devant l'entrée principale j'ai remarqué trois fissures importantes sur le mur est les fissures mesurent environ 15 à 20 centimètres de longueur l'état du béton armé semble préoccupant je recommande une inspection détaillée par un ingénieur structures le coffrage du voile présente également des défauts il y a des traces d'infiltration d'eau près des banches les étais sont en bon état mais il faut vérifier la stabilité avant de poursuivre les travaux je vais maintenant inspecter le quatrième étage pour vérifier l'état des dalles et des poutres fin de l'inspection du bâtiment a troisième étage
- Normalized Transcript: bonjour chef de chantier sur le site de vinci construction aujourd'hui le 6 novembre 2025, je fais l'inspection du bâtiment a je me trouve actuellement au troisième étage devant l'entrée principale j'ai remarqué trois fissures importantes sur le mur est les fissures mesurent environ 15 à 20 centimètres de longueur l'état du béton armé est préoccupant je recommande une inspection détaillée par un ingénieur structure le coffrage du voile présente également des défauts il y a des traces d'infiltration d'eau près des banches les étais sont en bon état mais il faut vérifier la stabilité avant de poursuivre les travaux je vais maintenant inspecter le quatrième étage pour vérifier l'état des dalles et des poutres fin de l'inspection du bâtiment a troisième étage
- Normalized Errors: substitutions=2, insertions=0, deletions=0
#### Normalized Error Details
- Replace: expected "semble" | actual "est"
- Replace: expected "structures" | actual "structure"

---

## audio_07_heavy_noise.wav
- Audio file: `data/processed/audio_07_heavy_noise.wav`
- Reference transcript: `data/processed/audio_07_reference.txt`
- Reference text: Bonjour, je suis chef de chantier sur le site de Vinci Construction.

Aujourd'hui, le six novembre deux mille vingt-cinq, je fais l'inspection du bâtiment A.

Je me trouve actuellement au troisième étage, devant l'entrée principale.

J'ai remarqué trois fissures importantes sur le mur est. Les fissures mesurent environ quinze à vingt centimètres de longueur.

L'état du béton armé semble préoccupant. Je recommande une inspection détaillée par un ingénieur structures.

Le coffrage du voile présente également des défauts. Il y a des traces d'infiltration d'eau près des banches.

Les étais sont en bon état, mais il faut vérifier la stabilité avant de poursuivre les travaux.

Je vais maintenant inspecter le quatrième étage pour vérifier l'état des dalles et des poutres.

Fin de l'inspection du bâtiment A, troisième étage.

### Model: gpt-audio
- Status: ✅ Success
- Latency: 3.67s
- Word Error Rate: 13.39%
- Transcript: Bonjour, je suis chef de chantier sur le site de Vinci Construction. Aujourd'hui le 6 novembre 2025, j'ai fait une inspection du bâtiment A. Je me trouve actuellement au troisième étage, devant l'entrée principale. J'ai remarqué trois fissures importantes sur le mur est, des fissures mesurent environ 15 à 20 cm de longueur. L'état du béton armé semble préoccupant. Je recommande une inspection détaillée par un ingénieur structure. Le coffrage de voile présente également des défauts. Il y a des traces d'infiltration d'eau près des banches. Les étais sont en bon état, mais il faut vérifier la stabilité avant de poursuivre les travaux. Je vais maintenant inspecter le quatrième étage pour vérifier l'état des dalles et des poutres. Fin d'inspection du bâtiment A, troisième étage.
- Errors: substitutions=17, insertions=0, deletions=0
#### Error Details
- Replace: expected "Aujourd'hui," | actual "Aujourd'hui"
- Replace: expected "six" | actual "6"
- Replace: expected "deux mille vingt-cinq, je fais l'inspection" | actual "2025, j'ai fait une inspection"
- Replace: expected "est. Les" | actual "est, des"
- Replace: expected "quinze" | actual "15"
- Replace: expected "vingt centimètres" | actual "20 cm"
- Replace: expected "structures." | actual "structure."
- Replace: expected "du" | actual "de"
- Replace: expected "de l'inspection" | actual "d'inspection"
- Normalized Word Error Rate: 8.00%
- Normalized Reference: bonjour je suis chef de chantier sur le site de vinci construction aujourd'hui le 6 novembre 2025, je fais l'inspection du bâtiment a je me trouve actuellement au troisième étage devant l'entrée principale j'ai remarqué trois fissures importantes sur le mur est les fissures mesurent environ 15 à 20 centimètres de longueur l'état du béton armé semble préoccupant je recommande une inspection détaillée par un ingénieur structures le coffrage du voile présente également des défauts il y a des traces d'infiltration d'eau près des banches les étais sont en bon état mais il faut vérifier la stabilité avant de poursuivre les travaux je vais maintenant inspecter le quatrième étage pour vérifier l'état des dalles et des poutres fin de l'inspection du bâtiment a troisième étage
- Normalized Transcript: bonjour je suis chef de chantier sur le site de vinci construction aujourd'hui le 6 novembre 2025, j'ai fait une inspection du bâtiment a je me trouve actuellement au troisième étage devant l'entrée principale j'ai remarqué trois fissures importantes sur le mur est des fissures mesurent environ 15 à 20 cm de longueur l'état du béton armé semble préoccupant je recommande une inspection détaillée par un ingénieur structure le coffrage de voile présente également des défauts il y a des traces d'infiltration d'eau près des banches les étais sont en bon état mais il faut vérifier la stabilité avant de poursuivre les travaux je vais maintenant inspecter le quatrième étage pour vérifier l'état des dalles et des poutres fin d'inspection du bâtiment a troisième étage
- Normalized Errors: substitutions=10, insertions=0, deletions=0
#### Normalized Error Details
- Replace: expected "je fais l'inspection" | actual "j'ai fait une inspection"
- Replace: expected "les" | actual "des"
- Replace: expected "centimètres" | actual "cm"
- Replace: expected "structures" | actual "structure"
- Replace: expected "du" | actual "de"
- Replace: expected "de l'inspection" | actual "d'inspection"

### Model: gpt-audio-mini
- Status: ✅ Success
- Latency: 3.22s
- Word Error Rate: 14.96%
- Transcript: Bonjour, je suis chef chantier sur le site de Vinci Construction. Aujourd'hui, le 6 novembre 2025, j'ai fait l'inspection du bâtiment A. Je me trouve actuellement au troisième étage, devant l'entrée principale. J'ai remarqué trois fissures importantes sur le mur est, des fissures mesurant environ 15 à 20 cm de longueur. L'état du béton armé semble préoccupant. Je recommande une inspection détaillée par un ingénieur structure. Le coffrage de voile présente également des défauts. Il y a des traces d'infiltration d'eau près des banses. Les étais sont en bon état, mais il faut vérifier la stabilité avant de poursuivre les travaux. Je vais maintenant inspecter le quatrième étage pour vérifier l'état des dalles et des poutres. Fin d'inspection du bâtiment A, au troisième étage.
- Errors: substitutions=17, insertions=1, deletions=1
#### Error Details
- Delete: expected "de" | actual ""
- Replace: expected "six" | actual "6"
- Replace: expected "deux mille vingt-cinq, je fais" | actual "2025, j'ai fait"
- Replace: expected "est. Les" | actual "est, des"
- Replace: expected "mesurent" | actual "mesurant"
- Replace: expected "quinze" | actual "15"
- Replace: expected "vingt centimètres" | actual "20 cm"
- Replace: expected "structures." | actual "structure."
- Replace: expected "du" | actual "de"
- Replace: expected "banches." | actual "banses."
- Replace: expected "de l'inspection" | actual "d'inspection"
- Insert: expected "" | actual "au"
- Normalized Word Error Rate: 9.60%
- Normalized Reference: bonjour je suis chef de chantier sur le site de vinci construction aujourd'hui le 6 novembre 2025, je fais l'inspection du bâtiment a je me trouve actuellement au troisième étage devant l'entrée principale j'ai remarqué trois fissures importantes sur le mur est les fissures mesurent environ 15 à 20 centimètres de longueur l'état du béton armé semble préoccupant je recommande une inspection détaillée par un ingénieur structures le coffrage du voile présente également des défauts il y a des traces d'infiltration d'eau près des banches les étais sont en bon état mais il faut vérifier la stabilité avant de poursuivre les travaux je vais maintenant inspecter le quatrième étage pour vérifier l'état des dalles et des poutres fin de l'inspection du bâtiment a troisième étage
- Normalized Transcript: bonjour je suis chef chantier sur le site de vinci construction aujourd'hui le 6 novembre 2025, j'ai fait l'inspection du bâtiment a je me trouve actuellement au troisième étage devant l'entrée principale j'ai remarqué trois fissures importantes sur le mur est des fissures mesurant environ 15 à 20 cm de longueur l'état du béton armé semble préoccupant je recommande une inspection détaillée par un ingénieur structure le coffrage de voile présente également des défauts il y a des traces d'infiltration d'eau près des banses les étais sont en bon état mais il faut vérifier la stabilité avant de poursuivre les travaux je vais maintenant inspecter le quatrième étage pour vérifier l'état des dalles et des poutres fin d'inspection du bâtiment a au troisième étage
- Normalized Errors: substitutions=10, insertions=1, deletions=1
#### Normalized Error Details
- Delete: expected "de" | actual ""
- Replace: expected "je fais" | actual "j'ai fait"
- Replace: expected "les" | actual "des"
- Replace: expected "mesurent" | actual "mesurant"
- Replace: expected "centimètres" | actual "cm"
- Replace: expected "structures" | actual "structure"
- Replace: expected "du" | actual "de"
- Replace: expected "banches" | actual "banses"
- Replace: expected "de l'inspection" | actual "d'inspection"
- Insert: expected "" | actual "au"

### Model: gpt-4o-audio-preview
- Status: ✅ Success
- Latency: 2.49s
- Word Error Rate: 17.32%
- Transcript: Bonjour, je suis Isham, chargé sur le site de Vinci Construction. Aujourd'hui le 6 novembre 2023, j'ai fait une inspection du bâtiment A. Je me trouve actuellement au troisième étage, devant l'entrée principale. J'ai remarqué trois fissures importantes sur le mur Est. Légèrement en mesure environ 15 à 20 centimètres de longueur. L'état du béton armé semble préoccupant. Je recommande une inspection détaillée par un ingénieur structure. Le coffrage de voile présente également des défauts. Il y a des traces d'infiltration d'eau près des banches. Les étais sont en bon état mais il faut vérifier la stabilité avant de poursuivre les travaux. Je vais maintenant inspecter le quatrième étage pour vérifier l'état des dalles et des poutres. Fin d'inspection du bâtiment A, troisième étage.
- Errors: substitutions=22, insertions=0, deletions=0
#### Error Details
- Replace: expected "chef de chantier" | actual "Isham, chargé"
- Replace: expected "Aujourd'hui," | actual "Aujourd'hui"
- Replace: expected "six" | actual "6"
- Replace: expected "deux mille vingt-cinq, je fais l'inspection" | actual "2023, j'ai fait une inspection"
- Replace: expected "est. Les fissures mesurent" | actual "Est. Légèrement en mesure"
- Replace: expected "quinze" | actual "15"
- Replace: expected "vingt" | actual "20"
- Replace: expected "structures." | actual "structure."
- Replace: expected "du" | actual "de"
- Replace: expected "état," | actual "état"
- Replace: expected "de l'inspection" | actual "d'inspection"
- Normalized Word Error Rate: 12.00%
- Normalized Reference: bonjour je suis chef de chantier sur le site de vinci construction aujourd'hui le 6 novembre 2025, je fais l'inspection du bâtiment a je me trouve actuellement au troisième étage devant l'entrée principale j'ai remarqué trois fissures importantes sur le mur est les fissures mesurent environ 15 à 20 centimètres de longueur l'état du béton armé semble préoccupant je recommande une inspection détaillée par un ingénieur structures le coffrage du voile présente également des défauts il y a des traces d'infiltration d'eau près des banches les étais sont en bon état mais il faut vérifier la stabilité avant de poursuivre les travaux je vais maintenant inspecter le quatrième étage pour vérifier l'état des dalles et des poutres fin de l'inspection du bâtiment a troisième étage
- Normalized Transcript: bonjour je suis isham chargé sur le site de vinci construction aujourd'hui le 6 novembre 2023, j'ai fait une inspection du bâtiment a je me trouve actuellement au troisième étage devant l'entrée principale j'ai remarqué trois fissures importantes sur le mur est légèrement en mesure environ 15 à 20 centimètres de longueur l'état du béton armé semble préoccupant je recommande une inspection détaillée par un ingénieur structure le coffrage de voile présente également des défauts il y a des traces d'infiltration d'eau près des banches les étais sont en bon état mais il faut vérifier la stabilité avant de poursuivre les travaux je vais maintenant inspecter le quatrième étage pour vérifier l'état des dalles et des poutres fin d'inspection du bâtiment a troisième étage
- Normalized Errors: substitutions=15, insertions=0, deletions=0
#### Normalized Error Details
- Replace: expected "chef de chantier" | actual "isham chargé"
- Replace: expected "2025, je fais l'inspection" | actual "2023, j'ai fait une inspection"
- Replace: expected "les fissures mesurent" | actual "légèrement en mesure"
- Replace: expected "structures" | actual "structure"
- Replace: expected "du" | actual "de"
- Replace: expected "de l'inspection" | actual "d'inspection"

---

## audio_10_long.wav
- Audio file: `data/processed/audio_10_long.wav`
- Reference transcript: `data/processed/audio_10_reference.txt`
- Reference text: Rapport de fin de journée, mercredi six novembre deux mille vingt-cinq.

Bonjour, je suis chef de chantier. Voici le compte-rendu complet de la journée sur le chantier de Vinci Construction, projet résidentiel Les Jardins de l'Ouest.

PARTIE UN: AVANCEMENT DES TRAVAUX

Ce matin, nous avons terminé le coulage de la dalle du troisième étage du bâtiment A. Le volume de béton coulé est de soixante-quinze mètres cubes. La coulée a commencé à sept heures trente et s'est terminée à onze heures quinze.

L'équipe de maçonnerie a monté trois mètres linéaires de voiles au quatrième étage. Le ferraillage préparé hier a été intégré sans problème. La géométrie est conforme aux plans.

Les électriciens ont achevé le passage des gaines dans les refends du deuxième étage. Reste à faire le câblage, prévu pour la semaine prochaine.

La plomberie du premier étage est terminée à quatre-vingt-dix pour cent. Les raccordements aux colonnes montantes sont faits. Il reste les finitions dans les salles de bains.

PARTIE DEUX: LIVRAISONS ET APPROVISIONNEMENTS

Nous avons reçu ce matin la livraison de quinze palettes de parpaings pour le bâtiment B. La qualité est conforme. Stockage organisé à proximité de la zone de travail.

La livraison des menuiseries extérieures prévue aujourd'hui est reportée à vendredi. Le fournisseur a un problème logistique. Impact mineur sur le planning général.

Les banches métalliques louées pour le bâtiment C sont arrivées hier soir. L'équipe coffreur commence le montage demain matin.

PARTIE TROIS: EFFECTIFS ET RESSOURCES

Quinze ouvriers présents aujourd'hui. Trois absents: un pour congé maladie, deux pour formation sécurité obligatoire.

La grue à tour numéro deux a été réparée. Elle est de nouveau opérationnelle depuis quatorze heures.

Le nouveau chef d'équipe, Monsieur Martin, a pris ses fonctions ce matin. Intégration en cours, il sera autonome d'ici deux semaines.

PARTIE QUATRE: SÉCURITÉ ET QUALITÉ

Aucun accident aujourd'hui. Le taux d'incidents reste à zéro depuis quinze jours.

Visite surprise de l'inspecteur du travail à dix heures. Tout était conforme. Aucune remarque ni observation. Très satisfaisant.

Le contrôle qualité du béton: trois éprouvettes prélevées ce matin lors de la coulée. Résultats attendus dans vingt-huit jours.

Petit incident: un ouvrier a oublié son harnais de sécurité. Rappel à l'ordre immédiat. Formation de sensibilisation prévue vendredi pour toute l'équipe.

PARTIE CINQ: POINTS DE VIGILANCE

Météo: prévisions de pluie pour demain après-midi. Prévoir bâches de protection pour les zones en cours de bétonnage.

Le planning est serré sur le bâtiment A. Il faut terminer le gros œuvre avant la fin du mois. Nous sommes dans les temps, mais aucune marge de manœuvre.

Problème de coordination avec les façadiers. Réunion prévue demain matin à huit heures pour ajuster les interfaces.

PARTIE SIX: ACTIONS POUR DEMAIN

Continuer le montage des voiles au quatrième étage du bâtiment A.

Démarrer le coffrage des poteaux du rez-de-chaussée du bâtiment B.

Organiser la coulée du radier du bâtiment C, si la météo le permet.

Réceptionner et contrôler la livraison de cinquante tonnes d'armatures prévue à neuf heures.

Réunion de coordination à huit heures avec tous les sous-traitants.

CONCLUSION

Bonne journée dans l'ensemble. Avancement conforme au planning. Aucun retard significatif. Tous les indicateurs sont au vert.

Prochain rapport demain soir à la même heure.

Bonne soirée à tous.

Fin du rapport de fin de journée.

### Model: gpt-audio
- Status: ✅ Success
- Latency: 12.01s
- Word Error Rate: 29.13%
- Transcript: Rapport de la fin de journée, mercredi 6 novembre 2025.

Bonjour, je suis chef de chantier. Voici le compte rendu complet de la journée sur le chantier de Vinci Construction – Projet Résidentiel Les Jardins de l’Ouest.

Partie 1 : Avancement des travaux.
Ce matin, nous avons terminé le coulage de la dalle du troisième étage du bâtiment A. Le volume du béton coulé est de 75 mètres cubes. La coulée a commencé à 7h30 et s’est terminée à 11h15. L’équipe de maçonnerie a monté 3 mètres linéaires de voiles au quatrième étage. Le ferraillage a préparé et intégré son problème, la géométrie est conforme au plan. Les électriciens ont achevé le passage des gaines dans les refends du deuxième étage. Reste à faire le câblage prévu pour la semaine prochaine. La plomberie du premier étage est terminée à 90 %, les raccordements aux colonnes montantes sont faits, il reste les finitions dans les salles de bain.

Partie 2 : Livraisons et approvisionnement.
Nous avons reçu ce matin la livraison de 15 palettes de parpaings pour le bâtiment B. La qualité est conforme, stockage organisé à proximité de la zone de travail. La livraison des menuiseries extérieures, prévue aujourd’hui, est reportée à vendredi, le fournisseur ayant un problème logistique. Impact mineur sur le planning général. Les banches métalliques louées dans le bâtiment C sont arrivées hier soir. L’équipe coffreur commence le montage demain matin.

Partie 3 : Effectif et ressources.
15 ouvriers présents aujourd’hui, 3 absents : 1 pour congé maladie, 2 pour formation sécurité obligatoire. La grue à tour numéro 2 a été réparée, elle est de nouveau opérationnelle depuis 14h. Le nouveau chef d’équipe, Monsieur Martin, a pris ses fonctions ce matin, intégration en cours, il sera autonome d’ici deux semaines.

Partie 4 : Sécurité et qualité.
Aucun accident aujourd’hui, le taux d’incidents reste à zéro depuis 15 jours. Visite surprise de l’inspecteur de travail à 10h : tout était conforme, aucune remarque ni observation, très satisfaisant. Le contrôle qualité du béton : 3 éprouvettes prélevées ce matin lors de la coulée, résultat attendu dans 28 jours. Petit incident : un ouvrier a oublié son harnais de sécurité. Appel à l’ordre immédiat, formation de sensibilisation prévue vendredi pour toute l’équipe.

Partie 5 : Points de vigilance.
Météo : prévision de pluie pour demain après-midi. Prévoir bâches de protection pour les zones en cours de bétonnage. Le planning est serré sur le bâtiment A, il faut terminer le gros œuvre avant la fin du mois. Nous sommes dans les temps, mais aucune marge de manœuvre. Problème de coordination avec les façadiers : réunion prévue demain matin à 8h pour ajuster les interfaces.

Partie 6 : Actions pour demain.
Continuer le montage des voiles au quatrième étage du bâtiment A. Démarrage du coffrage des poteaux du rez-de-chaussée du bâtiment B. Organiser le coulé du radier du bâtiment C si la météo le permet. Réceptionner et contrôler la livraison de 50 tonnes d’armatures prévue à 9h. Réunion de coordination à 8h avec tous les sous-traitants.

Conclusion : bonne journée dans l’ensemble, avancement conforme au planning, aucun retard significatif, tous les indicateurs sont au vert. Prochain rapport demain soir à la même heure. Bonne soirée à tous. Fin du rapport de fin de journée.
- Errors: substitutions=158, insertions=2, deletions=0
#### Error Details
- Insert: expected "" | actual "la"
- Replace: expected "six" | actual "6"
- Replace: expected "deux mille vingt-cinq." | actual "2025."
- Replace: expected "compte-rendu" | actual "compte rendu"
- Replace: expected "Construction, projet résidentiel" | actual "Construction – Projet Résidentiel"
- Replace: expected "l'Ouest. PARTIE UN: AVANCEMENT DES TRAVAUX" | actual "l’Ouest. Partie 1 : Avancement des travaux."
- Replace: expected "de" | actual "du"
- Replace: expected "soixante-quinze" | actual "75"
- Replace: expected "sept heures trente" | actual "7h30"
- Replace: expected "s'est" | actual "s’est"
- Replace: expected "onze heures quinze. L'équipe" | actual "11h15. L’équipe"
- Replace: expected "trois" | actual "3"
- Insert: expected "" | actual "a"
- Replace: expected "hier a été" | actual "et"
- Replace: expected "sans problème. La" | actual "son problème, la"
- Replace: expected "aux plans." | actual "au plan."
- Replace: expected "câblage," | actual "câblage"
- Replace: expected "quatre-vingt-dix pour cent. Les" | actual "90 %, les"
- Replace: expected "faits. Il" | actual "faits, il"
- Replace: expected "bains. PARTIE DEUX: LIVRAISONS ET APPROVISIONNEMENTS" | actual "bain. Partie 2 : Livraisons et approvisionnement."
- Replace: expected "quinze" | actual "15"
- Replace: expected "conforme. Stockage" | actual "conforme, stockage"
- Replace: expected "extérieures" | actual "extérieures,"
- Replace: expected "aujourd'hui" | actual "aujourd’hui,"
- Replace: expected "vendredi. Le" | actual "vendredi, le"
- Replace: expected "a" | actual "ayant"
- Replace: expected "pour" | actual "dans"
- Replace: expected "L'équipe" | actual "L’équipe"
- Replace: expected "PARTIE TROIS: EFFECTIFS ET RESSOURCES Quinze" | actual "Partie 3 : Effectif et ressources. 15"
- Replace: expected "aujourd'hui. Trois absents: un" | actual "aujourd’hui, 3 absents : 1"
- Replace: expected "deux" | actual "2"
- Replace: expected "deux" | actual "2"
- Replace: expected "réparée. Elle" | actual "réparée, elle"
- Replace: expected "quatorze heures." | actual "14h."
- Replace: expected "d'équipe," | actual "d’équipe,"
- Replace: expected "matin. Intégration" | actual "matin, intégration"
- Replace: expected "d'ici" | actual "d’ici"
- Replace: expected "PARTIE QUATRE: SÉCURITÉ ET QUALITÉ" | actual "Partie 4 : Sécurité et qualité."
- Replace: expected "aujourd'hui. Le" | actual "aujourd’hui, le"
- Replace: expected "d'incidents" | actual "d’incidents"
- Replace: expected "quinze" | actual "15"
- Replace: expected "l'inspecteur du" | actual "l’inspecteur de"
- Replace: expected "dix heures. Tout" | actual "10h : tout"
- Replace: expected "conforme. Aucune" | actual "conforme, aucune"
- Replace: expected "observation. Très" | actual "observation, très"
- Replace: expected "béton: trois" | actual "béton : 3"
- Replace: expected "coulée. Résultats attendus" | actual "coulée, résultat attendu"
- Replace: expected "vingt-huit" | actual "28"
- Replace: expected "incident:" | actual "incident :"
- Replace: expected "Rappel à l'ordre immédiat. Formation" | actual "Appel à l’ordre immédiat, formation"
- Replace: expected "l'équipe. PARTIE CINQ: POINTS DE VIGILANCE Météo: prévisions" | actual "l’équipe. Partie 5 : Points de vigilance. Météo : prévision"
- Replace: expected "A. Il" | actual "A, il"
- Replace: expected "façadiers. Réunion" | actual "façadiers : réunion"
- Replace: expected "huit heures" | actual "8h"
- Replace: expected "PARTIE SIX: ACTIONS POUR DEMAIN" | actual "Partie 6 : Actions pour demain."
- Replace: expected "Démarrer le" | actual "Démarrage du"
- Replace: expected "la coulée" | actual "le coulé"
- Replace: expected "C," | actual "C"
- Replace: expected "cinquante" | actual "50"
- Replace: expected "d'armatures" | actual "d’armatures"
- Replace: expected "neuf heures." | actual "9h."
- Replace: expected "huit heures" | actual "8h"
- Replace: expected "CONCLUSION Bonne" | actual "Conclusion : bonne"
- Replace: expected "l'ensemble. Avancement" | actual "l’ensemble, avancement"
- Replace: expected "planning. Aucun" | actual "planning, aucun"
- Replace: expected "significatif. Tous" | actual "significatif, tous"
- Normalized Word Error Rate: 10.80%
- Normalized Reference: rapport de fin de journée mercredi 6 novembre 2025 bonjour je suis chef de chantier voici le compte-rendu complet de la journée sur le chantier de vinci construction projet résidentiel les jardins de l'ouest partie un avancement des travaux ce matin nous avons terminé le coulage de la dalle du troisième étage du bâtiment a le volume de béton coulé est de 60-15 mètres cubes la coulée a commencé à 7 heures 30 et s'est terminée à 11 heures 15 l'équipe de maçonnerie a monté trois mètres linéaires de voiles au quatrième étage le ferraillage préparé hier a été intégré sans problème la géométrie est conforme aux plans les électriciens ont achevé le passage des gaines dans les refends du deuxième étage reste à faire le câblage prévu pour la semaine prochaine la plomberie du premier étage est terminée à 90 pour cent les raccordements aux colonnes montantes sont faits il reste les finitions dans les salles de bains partie deux livraisons et approvisionnements nous avons reçu ce matin la livraison de 15 palettes de parpaings pour le bâtiment b la qualité est conforme stockage organisé à proximité de la zone de travail la livraison des menuiseries extérieures prévue aujourd'hui est reportée à vendredi le fournisseur a un problème logistique impact mineur sur le planning général les banches métalliques louées pour le bâtiment c sont arrivées hier soir l'équipe coffreur commence le montage demain matin partie trois effectifs et ressources 15 ouvriers présents aujourd'hui trois absents un pour congé maladie deux pour formation sécurité obligatoire la grue à tour numéro deux a été réparée elle est de nouveau opérationnelle depuis 14 heures le nouveau chef d'équipe monsieur martin a pris ses fonctions ce matin intégration en cours il sera autonome d'ici deux semaines partie quatre sécurité et qualité aucun accident aujourd'hui le taux d'incidents reste à zéro depuis 15 jours visite surprise de l'inspecteur du travail à 10 heures tout était conforme aucune remarque ni observation très satisfaisant le contrôle qualité du béton trois éprouvettes prélevées ce matin lors de la coulée résultats attendus dans 20-8 jours petit incident un ouvrier a oublié son harnais de sécurité rappel à l'ordre immédiat formation de sensibilisation prévue vendredi pour toute l'équipe partie cinq points de vigilance météo prévisions de pluie pour demain après-midi prévoir bâches de protection pour les zones en cours de bétonnage le planning est serré sur le bâtiment a il faut terminer le gros œuvre avant la fin du mois nous sommes dans les temps mais aucune marge de manœuvre problème de coordination avec les façadiers réunion prévue demain matin à 8 heures pour ajuster les interfaces partie 6: actions pour demain continuer le montage des voiles au quatrième étage du bâtiment a démarrer le coffrage des poteaux du rez-de-chaussée du bâtiment b organiser la coulée du radier du bâtiment c si la météo le permet réceptionner et contrôler la livraison de 50 tonnes d'armatures prévue à 9 heures réunion de coordination à 8 heures avec tous les sous-traitants conclusion bonne journée dans l'ensemble avancement conforme au planning aucun retard significatif tous les indicateurs sont au vert prochain rapport demain soir à la même heure bonne soirée à tous fin du rapport de fin de journée
- Normalized Transcript: rapport de la fin de journée mercredi 6 novembre 2025 bonjour je suis chef de chantier voici le compte rendu complet de la journée sur le chantier de vinci construction – projet résidentiel les jardins de l'ouest partie 1 avancement des travaux ce matin nous avons terminé le coulage de la dalle du troisième étage du bâtiment a le volume du béton coulé est de 75 mètres cubes la coulée a commencé à 7h30 et s'est terminée à 11h15 l'équipe de maçonnerie a monté 3 mètres linéaires de voiles au quatrième étage le ferraillage a préparé et intégré son problème la géométrie est conforme au plan les électriciens ont achevé le passage des gaines dans les refends du deuxième étage reste à faire le câblage prévu pour la semaine prochaine la plomberie du premier étage est terminée à 90 % les raccordements aux colonnes montantes sont faits il reste les finitions dans les salles de bain partie 2 livraisons et approvisionnement nous avons reçu ce matin la livraison de 15 palettes de parpaings pour le bâtiment b la qualité est conforme stockage organisé à proximité de la zone de travail la livraison des menuiseries extérieures prévue aujourd'hui est reportée à vendredi le fournisseur ayant un problème logistique impact mineur sur le planning général les banches métalliques louées dans le bâtiment c sont arrivées hier soir l'équipe coffreur commence le montage demain matin partie 3 effectif et ressources 15 ouvriers présents aujourd'hui 3 absents 1 pour congé maladie 2 pour formation sécurité obligatoire la grue à tour numéro 2 a été réparée elle est de nouveau opérationnelle depuis 14h le nouveau chef d'équipe monsieur martin a pris ses fonctions ce matin intégration en cours il sera autonome d'ici deux semaines partie 4 sécurité et qualité aucun accident aujourd'hui le taux d'incidents reste à zéro depuis 15 jours visite surprise de l'inspecteur de travail à 10h tout était conforme aucune remarque ni observation très satisfaisant le contrôle qualité du béton 3 éprouvettes prélevées ce matin lors de la coulée résultat attendu dans 28 jours petit incident un ouvrier a oublié son harnais de sécurité appel à l'ordre immédiat formation de sensibilisation prévue vendredi pour toute l'équipe partie 5 points de vigilance météo prévision de pluie pour demain après-midi prévoir bâches de protection pour les zones en cours de bétonnage le planning est serré sur le bâtiment a il faut terminer le gros œuvre avant la fin du mois nous sommes dans les temps mais aucune marge de manœuvre problème de coordination avec les façadiers réunion prévue demain matin à 8h pour ajuster les interfaces partie 6 actions pour demain continuer le montage des voiles au quatrième étage du bâtiment a démarrage du coffrage des poteaux du rez-de-chaussée du bâtiment b organiser le coulé du radier du bâtiment c si la météo le permet réceptionner et contrôler la livraison de 50 tonnes d'armatures prévue à 9h réunion de coordination à 8h avec tous les sous-traitants conclusion bonne journée dans l'ensemble avancement conforme au planning aucun retard significatif tous les indicateurs sont au vert prochain rapport demain soir à la même heure bonne soirée à tous fin du rapport de fin de journée
- Normalized Errors: substitutions=55, insertions=3, deletions=0
#### Normalized Error Details
- Insert: expected "" | actual "la"
- Replace: expected "compte-rendu" | actual "compte rendu"
- Insert: expected "" | actual "–"
- Replace: expected "un" | actual "1"
- Replace: expected "de" | actual "du"
- Replace: expected "60-15" | actual "75"
- Replace: expected "7 heures 30" | actual "7h30"
- Replace: expected "11 heures 15" | actual "11h15"
- Replace: expected "trois" | actual "3"
- Insert: expected "" | actual "a"
- Replace: expected "hier a été" | actual "et"
- Replace: expected "sans" | actual "son"
- Replace: expected "aux plans" | actual "au plan"
- Replace: expected "pour cent" | actual "%"
- Replace: expected "bains" | actual "bain"
- Replace: expected "deux" | actual "2"
- Replace: expected "approvisionnements" | actual "approvisionnement"
- Replace: expected "a" | actual "ayant"
- Replace: expected "pour" | actual "dans"
- Replace: expected "trois effectifs" | actual "3 effectif"
- Replace: expected "trois" | actual "3"
- Replace: expected "un" | actual "1"
- Replace: expected "deux" | actual "2"
- Replace: expected "deux" | actual "2"
- Replace: expected "14 heures" | actual "14h"
- Replace: expected "quatre" | actual "4"
- Replace: expected "du" | actual "de"
- Replace: expected "10 heures" | actual "10h"
- Replace: expected "trois" | actual "3"
- Replace: expected "résultats attendus" | actual "résultat attendu"
- Replace: expected "20-8" | actual "28"
- Replace: expected "rappel" | actual "appel"
- Replace: expected "cinq" | actual "5"
- Replace: expected "prévisions" | actual "prévision"
- Replace: expected "8 heures" | actual "8h"
- Replace: expected "6:" | actual "6"
- Replace: expected "démarrer le" | actual "démarrage du"
- Replace: expected "la coulée" | actual "le coulé"
- Replace: expected "9 heures" | actual "9h"
- Replace: expected "8 heures" | actual "8h"

### Model: gpt-audio-mini
- Status: ✅ Success
- Latency: 8.55s
- Word Error Rate: 19.67%
- Transcript: Rapport de la fin de journée, mercredi 6 novembre 2025. Bonjour, je suis chef de chantier. Voici le compte rendu complet de la journée sur le chantier de Vinci Construction, projet résidentiel Les Jardins de l'Ouest. Partie 1. Avancement des travaux. Ce matin, nous avons terminé le coulage de la dalle du troisième étage du bâtiment A. Le volume du béton coulé est de 75 mètres cubes. La coulée a commencé à 7h30 et s'est terminée à 11h15. L'équipe de maçonnerie a monté 3 mètres linéaires de voiles au quatrième étage. Le ferraillage a préparé et intégré son problème. La géométrie est conforme au plan. Les électriciens ont achevé le passage des gaines dans les refends du deuxième étage. Reste à faire le câblage, prévu pour la semaine prochaine. La plomberie du premier étage est terminée à 90%. Les raccordements aux colonnes montantes sont faits. Il reste les finitions dans les salles de bain. Partie 2. Livraison et approvisionnement. Nous avons reçu ce matin la livraison de 15 palettes de parpaings pour le bâtiment B. La qualité est conforme. Stockage organisé à proximité de la zone de travail. La livraison des menuiseries extérieures prévue aujourd'hui est reportée à vendredi. Le fournisseur a un problème logistique. Impact mineur sur le planning général. Les bens métalliques loués dans le bâtiment C sont arrivés hier soir. L'équipe coffreur commence le montage demain matin. Partie 3. Effectifs et ressources. 15 ouvriers présents aujourd'hui, 3 absents. 1 pour congé maladie. 2 pour formation sécurité obligatoire. La grue, à tour numéro 2, a été réparée. Elle est de nouveau opérationnelle depuis 14h. Le nouveau chef d'équipe, M. Martin, a pris ses fonctions ce matin. Intégration en cours. Il sera autonome d'ici deux semaines. Partie 4. Sécurité et qualité. Aucun accident aujourd'hui. Le taux d'incident reste à zéro depuis 15 jours. Visite surprise de l'inspecteur du travail à 10h. Tout était conforme. Aucune remarque ni observation. Très satisfaisant. Le contrôle qualité du béton. Trois éprouvettes prélevées ce matin lors de la coulée. Résultat attendu dans 28 jours. Petit incident. Un ouvrier a oublié son harnais de sécurité. Appel à l'ordre immédiat. Formation de sensibilisation prévue vendredi pour toute l'équipe. Partie 5. Point de vigilance. Météo. Prévision de pluie pour demain après-midi. Prévoir bâche de protection pour les zones en cours de bétonnage. Le planning est serré sur le bâtiment A. Il faut terminer le gros œuvre avant la fin du mois. Nous sommes dans les temps, mais aucun marge de manœuvre. Problème de coordination avec les façadiers. Réunion prévue demain matin à 8h pour ajuster les interfaces. Partie 6. Actions pour demain. Continuer le montage des voiles au quatrième étage du bâtiment A. Démarrage de coffrage des poteaux du rez-de-chaussée du bâtiment B. Organiser le coulé du radier du bâtiment C, si la météo le permet. Réceptionner et contrôler la livraison de 50 tonnes d'armatures prévue à 9h. Réunion de coordination à 8h avec tous les sous-traitants. Conclusion. Bonne journée dans l'ensemble. Avancement conforme au planning. Aucun retard significatif. Tous les indicateurs sont envers. Prochain rapport demain soir à la même heure. Bonne soirée à tous. Fin du rapport de fin de journée.
- Errors: substitutions=104, insertions=2, deletions=0
#### Error Details
- Insert: expected "" | actual "la"
- Replace: expected "six" | actual "6"
- Replace: expected "deux mille vingt-cinq." | actual "2025."
- Replace: expected "compte-rendu" | actual "compte rendu"
- Replace: expected "PARTIE UN: AVANCEMENT DES TRAVAUX" | actual "Partie 1. Avancement des travaux."
- Replace: expected "de" | actual "du"
- Replace: expected "soixante-quinze" | actual "75"
- Replace: expected "sept heures trente" | actual "7h30"
- Replace: expected "onze heures quinze." | actual "11h15."
- Replace: expected "trois" | actual "3"
- Insert: expected "" | actual "a"
- Replace: expected "hier a été" | actual "et"
- Replace: expected "sans" | actual "son"
- Replace: expected "aux plans." | actual "au plan."
- Replace: expected "quatre-vingt-dix pour cent." | actual "90%."
- Replace: expected "bains. PARTIE DEUX: LIVRAISONS ET APPROVISIONNEMENTS" | actual "bain. Partie 2. Livraison et approvisionnement."
- Replace: expected "quinze" | actual "15"
- Replace: expected "banches" | actual "bens"
- Replace: expected "louées pour" | actual "loués dans"
- Replace: expected "arrivées" | actual "arrivés"
- Replace: expected "PARTIE TROIS: EFFECTIFS ET RESSOURCES Quinze" | actual "Partie 3. Effectifs et ressources. 15"
- Replace: expected "aujourd'hui. Trois absents: un" | actual "aujourd'hui, 3 absents. 1"
- Replace: expected "maladie, deux" | actual "maladie. 2"
- Replace: expected "grue" | actual "grue,"
- Replace: expected "deux" | actual "2,"
- Replace: expected "quatorze heures." | actual "14h."
- Replace: expected "Monsieur" | actual "M."
- Replace: expected "cours, il" | actual "cours. Il"
- Replace: expected "PARTIE QUATRE: SÉCURITÉ ET QUALITÉ" | actual "Partie 4. Sécurité et qualité."
- Replace: expected "d'incidents" | actual "d'incident"
- Replace: expected "quinze" | actual "15"
- Replace: expected "dix heures." | actual "10h."
- Replace: expected "béton: trois" | actual "béton. Trois"
- Replace: expected "Résultats attendus" | actual "Résultat attendu"
- Replace: expected "vingt-huit" | actual "28"
- Replace: expected "incident: un" | actual "incident. Un"
- Replace: expected "Rappel" | actual "Appel"
- Replace: expected "PARTIE CINQ: POINTS DE VIGILANCE Météo: prévisions" | actual "Partie 5. Point de vigilance. Météo. Prévision"
- Replace: expected "bâches" | actual "bâche"
- Replace: expected "aucune" | actual "aucun"
- Replace: expected "huit heures" | actual "8h"
- Replace: expected "PARTIE SIX: ACTIONS POUR DEMAIN" | actual "Partie 6. Actions pour demain."
- Replace: expected "Démarrer le" | actual "Démarrage de"
- Replace: expected "la coulée" | actual "le coulé"
- Replace: expected "cinquante" | actual "50"
- Replace: expected "neuf heures." | actual "9h."
- Replace: expected "huit heures" | actual "8h"
- Replace: expected "CONCLUSION" | actual "Conclusion."
- Replace: expected "au vert." | actual "envers."
- Normalized Word Error Rate: 12.10%
- Normalized Reference: rapport de fin de journée mercredi 6 novembre 2025 bonjour je suis chef de chantier voici le compte-rendu complet de la journée sur le chantier de vinci construction projet résidentiel les jardins de l'ouest partie un avancement des travaux ce matin nous avons terminé le coulage de la dalle du troisième étage du bâtiment a le volume de béton coulé est de 60-15 mètres cubes la coulée a commencé à 7 heures 30 et s'est terminée à 11 heures 15 l'équipe de maçonnerie a monté trois mètres linéaires de voiles au quatrième étage le ferraillage préparé hier a été intégré sans problème la géométrie est conforme aux plans les électriciens ont achevé le passage des gaines dans les refends du deuxième étage reste à faire le câblage prévu pour la semaine prochaine la plomberie du premier étage est terminée à 90 pour cent les raccordements aux colonnes montantes sont faits il reste les finitions dans les salles de bains partie deux livraisons et approvisionnements nous avons reçu ce matin la livraison de 15 palettes de parpaings pour le bâtiment b la qualité est conforme stockage organisé à proximité de la zone de travail la livraison des menuiseries extérieures prévue aujourd'hui est reportée à vendredi le fournisseur a un problème logistique impact mineur sur le planning général les banches métalliques louées pour le bâtiment c sont arrivées hier soir l'équipe coffreur commence le montage demain matin partie trois effectifs et ressources 15 ouvriers présents aujourd'hui trois absents un pour congé maladie deux pour formation sécurité obligatoire la grue à tour numéro deux a été réparée elle est de nouveau opérationnelle depuis 14 heures le nouveau chef d'équipe monsieur martin a pris ses fonctions ce matin intégration en cours il sera autonome d'ici deux semaines partie quatre sécurité et qualité aucun accident aujourd'hui le taux d'incidents reste à zéro depuis 15 jours visite surprise de l'inspecteur du travail à 10 heures tout était conforme aucune remarque ni observation très satisfaisant le contrôle qualité du béton trois éprouvettes prélevées ce matin lors de la coulée résultats attendus dans 20-8 jours petit incident un ouvrier a oublié son harnais de sécurité rappel à l'ordre immédiat formation de sensibilisation prévue vendredi pour toute l'équipe partie cinq points de vigilance météo prévisions de pluie pour demain après-midi prévoir bâches de protection pour les zones en cours de bétonnage le planning est serré sur le bâtiment a il faut terminer le gros œuvre avant la fin du mois nous sommes dans les temps mais aucune marge de manœuvre problème de coordination avec les façadiers réunion prévue demain matin à 8 heures pour ajuster les interfaces partie 6: actions pour demain continuer le montage des voiles au quatrième étage du bâtiment a démarrer le coffrage des poteaux du rez-de-chaussée du bâtiment b organiser la coulée du radier du bâtiment c si la météo le permet réceptionner et contrôler la livraison de 50 tonnes d'armatures prévue à 9 heures réunion de coordination à 8 heures avec tous les sous-traitants conclusion bonne journée dans l'ensemble avancement conforme au planning aucun retard significatif tous les indicateurs sont au vert prochain rapport demain soir à la même heure bonne soirée à tous fin du rapport de fin de journée
- Normalized Transcript: rapport de la fin de journée mercredi 6 novembre 2025 bonjour je suis chef de chantier voici le compte rendu complet de la journée sur le chantier de vinci construction projet résidentiel les jardins de l'ouest partie 1 avancement des travaux ce matin nous avons terminé le coulage de la dalle du troisième étage du bâtiment a le volume du béton coulé est de 75 mètres cubes la coulée a commencé à 7h30 et s'est terminée à 11h15 l'équipe de maçonnerie a monté 3 mètres linéaires de voiles au quatrième étage le ferraillage a préparé et intégré son problème la géométrie est conforme au plan les électriciens ont achevé le passage des gaines dans les refends du deuxième étage reste à faire le câblage prévu pour la semaine prochaine la plomberie du premier étage est terminée à 90% les raccordements aux colonnes montantes sont faits il reste les finitions dans les salles de bain partie 2 livraison et approvisionnement nous avons reçu ce matin la livraison de 15 palettes de parpaings pour le bâtiment b la qualité est conforme stockage organisé à proximité de la zone de travail la livraison des menuiseries extérieures prévue aujourd'hui est reportée à vendredi le fournisseur a un problème logistique impact mineur sur le planning général les bens métalliques loués dans le bâtiment c sont arrivés hier soir l'équipe coffreur commence le montage demain matin partie 3 effectifs et ressources 15 ouvriers présents aujourd'hui 3 absents 1 pour congé maladie 2 pour formation sécurité obligatoire la grue à tour numéro 2, a été réparée elle est de nouveau opérationnelle depuis 14h le nouveau chef d'équipe m martin a pris ses fonctions ce matin intégration en cours il sera autonome d'ici deux semaines partie 4 sécurité et qualité aucun accident aujourd'hui le taux d'incident reste à zéro depuis 15 jours visite surprise de l'inspecteur du travail à 10h tout était conforme aucune remarque ni observation très satisfaisant le contrôle qualité du béton trois éprouvettes prélevées ce matin lors de la coulée résultat attendu dans 28 jours petit incident un ouvrier a oublié son harnais de sécurité appel à l'ordre immédiat formation de sensibilisation prévue vendredi pour toute l'équipe partie 5 point de vigilance météo prévision de pluie pour demain après-midi prévoir bâche de protection pour les zones en cours de bétonnage le planning est serré sur le bâtiment a il faut terminer le gros œuvre avant la fin du mois nous sommes dans les temps mais aucun marge de manœuvre problème de coordination avec les façadiers réunion prévue demain matin à 8h pour ajuster les interfaces partie 6 actions pour demain continuer le montage des voiles au quatrième étage du bâtiment a démarrage de coffrage des poteaux du rez-de-chaussée du bâtiment b organiser le coulé du radier du bâtiment c si la météo le permet réceptionner et contrôler la livraison de 50 tonnes d'armatures prévue à 9h réunion de coordination à 8h avec tous les sous-traitants conclusion bonne journée dans l'ensemble avancement conforme au planning aucun retard significatif tous les indicateurs sont envers prochain rapport demain soir à la même heure bonne soirée à tous fin du rapport de fin de journée
- Normalized Errors: substitutions=63, insertions=2, deletions=0
#### Normalized Error Details
- Insert: expected "" | actual "la"
- Replace: expected "compte-rendu" | actual "compte rendu"
- Replace: expected "un" | actual "1"
- Replace: expected "de" | actual "du"
- Replace: expected "60-15" | actual "75"
- Replace: expected "7 heures 30" | actual "7h30"
- Replace: expected "11 heures 15" | actual "11h15"
- Replace: expected "trois" | actual "3"
- Insert: expected "" | actual "a"
- Replace: expected "hier a été" | actual "et"
- Replace: expected "sans" | actual "son"
- Replace: expected "aux plans" | actual "au plan"
- Replace: expected "90 pour cent" | actual "90%"
- Replace: expected "bains" | actual "bain"
- Replace: expected "deux livraisons" | actual "2 livraison"
- Replace: expected "approvisionnements" | actual "approvisionnement"
- Replace: expected "banches" | actual "bens"
- Replace: expected "louées pour" | actual "loués dans"
- Replace: expected "arrivées" | actual "arrivés"
- Replace: expected "trois" | actual "3"
- Replace: expected "trois" | actual "3"
- Replace: expected "un" | actual "1"
- Replace: expected "deux" | actual "2"
- Replace: expected "deux" | actual "2,"
- Replace: expected "14 heures" | actual "14h"
- Replace: expected "monsieur" | actual "m"
- Replace: expected "quatre" | actual "4"
- Replace: expected "d'incidents" | actual "d'incident"
- Replace: expected "10 heures" | actual "10h"
- Replace: expected "résultats attendus" | actual "résultat attendu"
- Replace: expected "20-8" | actual "28"
- Replace: expected "rappel" | actual "appel"
- Replace: expected "cinq points" | actual "5 point"
- Replace: expected "prévisions" | actual "prévision"
- Replace: expected "bâches" | actual "bâche"
- Replace: expected "aucune" | actual "aucun"
- Replace: expected "8 heures" | actual "8h"
- Replace: expected "6:" | actual "6"
- Replace: expected "démarrer le" | actual "démarrage de"
- Replace: expected "la coulée" | actual "le coulé"
- Replace: expected "9 heures" | actual "9h"
- Replace: expected "8 heures" | actual "8h"
- Replace: expected "au vert" | actual "envers"

### Model: gpt-4o-audio-preview
- Status: ✅ Success
- Latency: 9.14s
- Word Error Rate: 35.44%
- Transcript: Rapport de la fin de journée, mercredi 6 novembre 2025.

Bonjour, je suis chef de chantier. Voici le compte rendu complet de la journée sur le chantier de Vinci Construction, projet résidentiel "Les Jardins de l'Ouest".

**Partie 1 : Avancement des travaux**
Ce matin, nous avons terminé le coulage de la dalle du troisième étage du bâtiment A. Le volume du béton coulé est de 75 m³. La coulée a commencé à 7h30 et s'est terminée à 11h15.
L’équipe de maçonnerie a monté trois mètres linéaires de voile au quatrième étage.
Le ferraillage a préparé les armatures pour les poteaux. Aucune anomalie n’est à signaler, le contrôle géométrique est conforme au plan.
Les électriciens ont achevé le passage des gaines dans les plafonds du deuxième étage. Il reste à faire le câblage, prévu pour la semaine prochaine.
La plomberie du premier étage est terminée à 90%. Les raccordements aux colonnes montantes sont faits, il reste les finitions dans les salles de bain.

**Partie 2 : Livraison et approvisionnement**
Nous avons reçu ce matin la livraison de quinze palettes de parpaings pour le bâtiment B. La qualité est conforme, stockage organisé à proximité de la zone de travail.
La livraison des menuiseries extérieures prévue aujourd’hui est reportée à vendredi, le fournisseur étant en retard pour cause de problème logistique. Impact mineur sur le planning général.
Les banches métalliques louées pour le bâtiment C sont arrivées hier soir, l’équipe coffreur commence le montage demain matin.

**Partie 3 : Effectif et ressources**
Quinze ouvriers présents aujourd'hui, trois absents (un pour congé maladie, deux pour formation sécurité obligatoire).
La grue à tour numéro 2 a été réparée et est de nouveau opérationnelle depuis 14h.
Le nouveau chef d’équipe, Monsieur Martin, a pris ses fonctions ce matin, intégration en cours, il sera autonome d’ici deux semaines.

**Partie 4 : Sécurité et qualité**
Aucun accident aujourd’hui, le taux d’incident reste à zéro depuis quinze jours. 
Visite surprise de l’inspecteur du travail à 10h, tout était conforme, aucune remarque ni observation, très satisfaisant.
Le contrôle qualité du béton : trois éprouvettes prélevées ce matin lors de la coulée, résultats attendus dans 28 jours.
Petit incident : un ouvrier a oublié son harnais de sécurité; appel à l’ordre immédiat, formation de sensibilisation prévue vendredi pour toute l’équipe.

**Partie 5 : Points de vigilance**
Météo : prévision de pluie pour demain après-midi, prévoir bâches de protection pour les zones en cours de bétonnage.
Le planning est serré sur le bâtiment A, il faut terminer le gros œuvre avant la fin du mois, nous sommes dans les temps mais aucune marge de manœuvre.
Problème de coordination avec les façadiers, réunion prévue demain matin à 8h pour ajuster les interfaces.

**Partie 6 : Actions pour demain**
Continuer le montage des voiles au quatrième étage du bâtiment A.
Démarrage du coffrage des poteaux du rez-de-chaussée du bâtiment B.
Organiser le coulage du radier du bâtiment C si la météo le permet.
Réceptionner et contrôler la livraison de cinquante tonnes d’armatures prévue à 9h.
Réunion de coordination à 8h avec tous les sous-traitants.

**Conclusion**
Bonne journée dans l’ensemble. Avancement conforme au planning, aucun retard significatif. Tous les indicateurs sont au vert.
Prochain rapport demain soir à la même heure.
Bonne soirée à tous.
Fin du rapport de fin de journée.
- Errors: substitutions=160, insertions=2, deletions=0
#### Error Details
- Insert: expected "" | actual "la"
- Replace: expected "six" | actual "6"
- Replace: expected "deux mille vingt-cinq." | actual "2025."
- Replace: expected "compte-rendu" | actual "compte rendu"
- Replace: expected "Les" | actual ""Les"
- Replace: expected "l'Ouest. PARTIE UN: AVANCEMENT DES TRAVAUX" | actual "l'Ouest". **Partie 1 : Avancement des travaux**"
- Replace: expected "de" | actual "du"
- Replace: expected "soixante-quinze mètres cubes." | actual "75 m³."
- Replace: expected "sept heures trente" | actual "7h30"
- Replace: expected "onze heures quinze. L'équipe" | actual "11h15. L’équipe"
- Replace: expected "voiles" | actual "voile"
- Insert: expected "" | actual "a"
- Replace: expected "hier a été intégré sans problème. La géométrie" | actual "les armatures pour les poteaux. Aucune anomalie n’est à signaler, le contrôle géométrique"
- Replace: expected "aux plans." | actual "au plan."
- Replace: expected "refends" | actual "plafonds"
- Replace: expected "Reste" | actual "Il reste"
- Replace: expected "quatre-vingt-dix pour cent." | actual "90%."
- Replace: expected "faits. Il" | actual "faits, il"
- Replace: expected "bains. PARTIE DEUX: LIVRAISONS ET APPROVISIONNEMENTS" | actual "bain. **Partie 2 : Livraison et approvisionnement**"
- Replace: expected "conforme. Stockage" | actual "conforme, stockage"
- Replace: expected "aujourd'hui" | actual "aujourd’hui"
- Replace: expected "vendredi. Le" | actual "vendredi, le"
- Replace: expected "a un" | actual "étant en retard pour cause de"
- Replace: expected "soir. L'équipe" | actual "soir, l’équipe"
- Replace: expected "PARTIE TROIS: EFFECTIFS ET RESSOURCES" | actual "**Partie 3 : Effectif et ressources**"
- Replace: expected "aujourd'hui. Trois absents: un" | actual "aujourd'hui, trois absents (un"
- Replace: expected "obligatoire." | actual "obligatoire)."
- Replace: expected "deux" | actual "2"
- Replace: expected "réparée. Elle" | actual "réparée et"
- Replace: expected "quatorze heures." | actual "14h."
- Replace: expected "d'équipe," | actual "d’équipe,"
- Replace: expected "matin. Intégration" | actual "matin, intégration"
- Replace: expected "d'ici" | actual "d’ici"
- Replace: expected "PARTIE QUATRE: SÉCURITÉ ET QUALITÉ" | actual "**Partie 4 : Sécurité et qualité**"
- Replace: expected "aujourd'hui. Le" | actual "aujourd’hui, le"
- Replace: expected "d'incidents" | actual "d’incident"
- Replace: expected "l'inspecteur" | actual "l’inspecteur"
- Replace: expected "dix heures. Tout" | actual "10h, tout"
- Replace: expected "conforme. Aucune" | actual "conforme, aucune"
- Replace: expected "observation. Très" | actual "observation, très"
- Replace: expected "béton:" | actual "béton :"
- Replace: expected "coulée. Résultats" | actual "coulée, résultats"
- Replace: expected "vingt-huit" | actual "28"
- Replace: expected "incident:" | actual "incident :"
- Replace: expected "sécurité. Rappel à l'ordre immédiat. Formation" | actual "sécurité; appel à l’ordre immédiat, formation"
- Replace: expected "l'équipe. PARTIE CINQ: POINTS DE VIGILANCE Météo: prévisions" | actual "l’équipe. **Partie 5 : Points de vigilance** Météo : prévision"
- Replace: expected "après-midi. Prévoir" | actual "après-midi, prévoir"
- Replace: expected "A. Il" | actual "A, il"
- Replace: expected "mois. Nous" | actual "mois, nous"
- Replace: expected "temps," | actual "temps"
- Replace: expected "façadiers. Réunion" | actual "façadiers, réunion"
- Replace: expected "huit heures" | actual "8h"
- Replace: expected "PARTIE SIX: ACTIONS POUR DEMAIN" | actual "**Partie 6 : Actions pour demain**"
- Replace: expected "Démarrer le" | actual "Démarrage du"
- Replace: expected "la coulée" | actual "le coulage"
- Replace: expected "C," | actual "C"
- Replace: expected "d'armatures" | actual "d’armatures"
- Replace: expected "neuf heures." | actual "9h."
- Replace: expected "huit heures" | actual "8h"
- Replace: expected "CONCLUSION" | actual "**Conclusion**"
- Replace: expected "l'ensemble." | actual "l’ensemble."
- Replace: expected "planning. Aucun" | actual "planning, aucun"
- Normalized Word Error Rate: 16.20%
- Normalized Reference: rapport de fin de journée mercredi 6 novembre 2025 bonjour je suis chef de chantier voici le compte-rendu complet de la journée sur le chantier de vinci construction projet résidentiel les jardins de l'ouest partie un avancement des travaux ce matin nous avons terminé le coulage de la dalle du troisième étage du bâtiment a le volume de béton coulé est de 60-15 mètres cubes la coulée a commencé à 7 heures 30 et s'est terminée à 11 heures 15 l'équipe de maçonnerie a monté trois mètres linéaires de voiles au quatrième étage le ferraillage préparé hier a été intégré sans problème la géométrie est conforme aux plans les électriciens ont achevé le passage des gaines dans les refends du deuxième étage reste à faire le câblage prévu pour la semaine prochaine la plomberie du premier étage est terminée à 90 pour cent les raccordements aux colonnes montantes sont faits il reste les finitions dans les salles de bains partie deux livraisons et approvisionnements nous avons reçu ce matin la livraison de 15 palettes de parpaings pour le bâtiment b la qualité est conforme stockage organisé à proximité de la zone de travail la livraison des menuiseries extérieures prévue aujourd'hui est reportée à vendredi le fournisseur a un problème logistique impact mineur sur le planning général les banches métalliques louées pour le bâtiment c sont arrivées hier soir l'équipe coffreur commence le montage demain matin partie trois effectifs et ressources 15 ouvriers présents aujourd'hui trois absents un pour congé maladie deux pour formation sécurité obligatoire la grue à tour numéro deux a été réparée elle est de nouveau opérationnelle depuis 14 heures le nouveau chef d'équipe monsieur martin a pris ses fonctions ce matin intégration en cours il sera autonome d'ici deux semaines partie quatre sécurité et qualité aucun accident aujourd'hui le taux d'incidents reste à zéro depuis 15 jours visite surprise de l'inspecteur du travail à 10 heures tout était conforme aucune remarque ni observation très satisfaisant le contrôle qualité du béton trois éprouvettes prélevées ce matin lors de la coulée résultats attendus dans 20-8 jours petit incident un ouvrier a oublié son harnais de sécurité rappel à l'ordre immédiat formation de sensibilisation prévue vendredi pour toute l'équipe partie cinq points de vigilance météo prévisions de pluie pour demain après-midi prévoir bâches de protection pour les zones en cours de bétonnage le planning est serré sur le bâtiment a il faut terminer le gros œuvre avant la fin du mois nous sommes dans les temps mais aucune marge de manœuvre problème de coordination avec les façadiers réunion prévue demain matin à 8 heures pour ajuster les interfaces partie 6: actions pour demain continuer le montage des voiles au quatrième étage du bâtiment a démarrer le coffrage des poteaux du rez-de-chaussée du bâtiment b organiser la coulée du radier du bâtiment c si la météo le permet réceptionner et contrôler la livraison de 50 tonnes d'armatures prévue à 9 heures réunion de coordination à 8 heures avec tous les sous-traitants conclusion bonne journée dans l'ensemble avancement conforme au planning aucun retard significatif tous les indicateurs sont au vert prochain rapport demain soir à la même heure bonne soirée à tous fin du rapport de fin de journée
- Normalized Transcript: rapport de la fin de journée mercredi 6 novembre 2025 bonjour je suis chef de chantier voici le compte rendu complet de la journée sur le chantier de vinci construction projet résidentiel "les jardins de l'ouest" **partie 1 avancement des travaux** ce matin nous avons terminé le coulage de la dalle du troisième étage du bâtiment a le volume du béton coulé est de 75 m3 la coulée a commencé à 7h30 et s'est terminée à 11h15 l'équipe de maçonnerie a monté trois mètres linéaires de voile au quatrième étage le ferraillage a préparé les armatures pour les poteaux aucune anomalie n'est à signaler le contrôle géométrique est conforme au plan les électriciens ont achevé le passage des gaines dans les plafonds du deuxième étage il reste à faire le câblage prévu pour la semaine prochaine la plomberie du premier étage est terminée à 90% les raccordements aux colonnes montantes sont faits il reste les finitions dans les salles de bain **partie 2 livraison et approvisionnement** nous avons reçu ce matin la livraison de 15 palettes de parpaings pour le bâtiment b la qualité est conforme stockage organisé à proximité de la zone de travail la livraison des menuiseries extérieures prévue aujourd'hui est reportée à vendredi le fournisseur étant en retard pour cause de problème logistique impact mineur sur le planning général les banches métalliques louées pour le bâtiment c sont arrivées hier soir l'équipe coffreur commence le montage demain matin **partie 3 effectif et ressources** 15 ouvriers présents aujourd'hui trois absents (un pour congé maladie deux pour formation sécurité obligatoire) la grue à tour numéro 2 a été réparée et est de nouveau opérationnelle depuis 14h le nouveau chef d'équipe monsieur martin a pris ses fonctions ce matin intégration en cours il sera autonome d'ici deux semaines **partie 4 sécurité et qualité** aucun accident aujourd'hui le taux d'incident reste à zéro depuis 15 jours visite surprise de l'inspecteur du travail à 10h tout était conforme aucune remarque ni observation très satisfaisant le contrôle qualité du béton trois éprouvettes prélevées ce matin lors de la coulée résultats attendus dans 28 jours petit incident un ouvrier a oublié son harnais de sécurité appel à l'ordre immédiat formation de sensibilisation prévue vendredi pour toute l'équipe **partie 5 points de vigilance** météo prévision de pluie pour demain après-midi prévoir bâches de protection pour les zones en cours de bétonnage le planning est serré sur le bâtiment a il faut terminer le gros œuvre avant la fin du mois nous sommes dans les temps mais aucune marge de manœuvre problème de coordination avec les façadiers réunion prévue demain matin à 8h pour ajuster les interfaces **partie 6 actions pour demain** continuer le montage des voiles au quatrième étage du bâtiment a démarrage du coffrage des poteaux du rez-de-chaussée du bâtiment b organiser le coulage du radier du bâtiment c si la météo le permet réceptionner et contrôler la livraison de 50 tonnes d'armatures prévue à 9h réunion de coordination à 8h avec tous les sous-traitants **conclusion** bonne journée dans l'ensemble avancement conforme au planning aucun retard significatif tous les indicateurs sont au vert prochain rapport demain soir à la même heure bonne soirée à tous fin du rapport de fin de journée
- Normalized Errors: substitutions=84, insertions=3, deletions=0
#### Normalized Error Details
- Insert: expected "" | actual "la"
- Replace: expected "compte-rendu" | actual "compte rendu"
- Replace: expected "les" | actual ""les"
- Replace: expected "l'ouest partie un" | actual "l'ouest" **partie 1"
- Replace: expected "travaux" | actual "travaux**"
- Replace: expected "de" | actual "du"
- Replace: expected "60-15 mètres cubes" | actual "75 m3"
- Replace: expected "7 heures 30" | actual "7h30"
- Replace: expected "11 heures 15" | actual "11h15"
- Replace: expected "voiles" | actual "voile"
- Insert: expected "" | actual "a"
- Replace: expected "hier a été intégré sans problème la géométrie" | actual "les armatures pour les poteaux aucune anomalie n'est à signaler le contrôle géométrique"
- Replace: expected "aux plans" | actual "au plan"
- Replace: expected "refends" | actual "plafonds"
- Insert: expected "" | actual "il"
- Replace: expected "90 pour cent" | actual "90%"
- Replace: expected "bains partie deux livraisons" | actual "bain **partie 2 livraison"
- Replace: expected "approvisionnements" | actual "approvisionnement**"
- Replace: expected "a un" | actual "étant en retard pour cause de"
- Replace: expected "partie trois effectifs" | actual "**partie 3 effectif"
- Replace: expected "ressources" | actual "ressources**"
- Replace: expected "un" | actual "(un"
- Replace: expected "obligatoire" | actual "obligatoire)"
- Replace: expected "deux" | actual "2"
- Replace: expected "elle" | actual "et"
- Replace: expected "14 heures" | actual "14h"
- Replace: expected "partie quatre" | actual "**partie 4"
- Replace: expected "qualité" | actual "qualité**"
- Replace: expected "d'incidents" | actual "d'incident"
- Replace: expected "10 heures" | actual "10h"
- Replace: expected "20-8" | actual "28"
- Replace: expected "rappel" | actual "appel"
- Replace: expected "partie cinq" | actual "**partie 5"
- Replace: expected "vigilance" | actual "vigilance**"
- Replace: expected "prévisions" | actual "prévision"
- Replace: expected "8 heures" | actual "8h"
- Replace: expected "partie 6:" | actual "**partie 6"
- Replace: expected "demain" | actual "demain**"
- Replace: expected "démarrer le" | actual "démarrage du"
- Replace: expected "la coulée" | actual "le coulage"
- Replace: expected "9 heures" | actual "9h"
- Replace: expected "8 heures" | actual "8h"
- Replace: expected "conclusion" | actual "**conclusion**"

---
