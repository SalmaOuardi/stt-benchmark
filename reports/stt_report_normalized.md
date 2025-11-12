# Speech-to-Text Evaluation Report

Generated from 8 audio samples with reference transcripts.

## audio_01_clean.wav
- Audio file: `data/mine/processed/audio_01_clean.wav`
- Reference transcript: `data/mine/processed/audio_01_reference.txt`
- Reference text: Bonjour, je suis chef de chantier sur le site de Vinci Construction.

Aujourd'hui, le 6 novembre 2025, je fais l'inspection du bâtiment A.

Je me trouve actuellement au troisième étage, devant l'entrée principale.

J'ai remarqué 3 fissures importantes sur le mur est. Les fissures mesurent environ 15 à 20 centimètres de longueur.

L'état du béton armé semble préoccupant. Je recommande une inspection détaillée par un ingénieur structures.

Le coffrage du voile présente également des défauts. Il y a des traces d'infiltration d'eau près des banches.

Les étais sont en bon état, mais il faut vérifier la stabilité avant de poursuivre les travaux.

Je vais maintenant inspecter le quatrième étage pour vérifier l'état des dalles et des poutres.

Fin de l'inspection du bâtiment A, troisième étage.

### Model: gpt-audio
- Status: ✅ Success
- Latency: 3.58s
- **Word Error Rate (Meaningful): 3.20%**
- Transcript: Bonjour, je suis chef de chantier sur le site de Vinci Construction. Aujourd’hui, le 6 novembre 2025, je fais l’inspection du bâtiment A. Je me trouve actuellement au troisième étage devant l’entrée principale. J’ai remarqué trois fissures importantes sur le mur Est. Les fissures mesurent environ 15 à 20 centimètres de longueur. L’état du béton armé semble préoccupant. Je recommande une inspection détaillée par un ingénieur structure. Le coffrage du voile présente également des défauts, il y a des traces d’infiltrations d’eau près des banches. Les étais sont en bon état, mais il faut vérifier la stabilité avant de poursuivre les travaux. Il faut maintenant inspecter le quatrième étage pour vérifier l’état des dalles et des poutres. Fin de l’inspection du bâtiment A, troisième étage.
- Meaningful Errors: substitutions=4, insertions=0, deletions=0
#### Meaningful Error Details (Semantic differences only)
- Replace: expected "aujourd'hui" | actual "aujourdhui"
- Replace: expected "structures" | actual "structure"
- Replace: expected "je vais" | actual "il faut"
- Raw WER (before normalization): 13.60%
- Normalized Reference: bonjour je suis chef de chantier sur le site de vinci construction aujourd'hui le 6 novembre 2025 je fais linspection du batiment a je me trouve actuellement au 3eme etage devant lentre principale jai remarque 3 fissures importantes sur le mur est les fissures mesurent environ 15 a 20 centimetres de longueur letat du beton arme semble preoccupant je recommande une inspection detaillee par un ingenieur structures le coffrage du voile presente egalement des defauts il y a des traces dinfiltration deau pres des banches les etais sont en bon etat mais il faut verifier la stabilite avant de poursuivre les travaux je vais maintenant inspecter le 4eme etage pour verifier letat des dalles et des poutres fin de linspection du batiment a 3eme etage
- Normalized Transcript: bonjour je suis chef de chantier sur le site de vinci construction aujourdhui le 6 novembre 2025 je fais linspection du batiment a je me trouve actuellement au 3eme etage devant lentre principale jai remarque 3 fissures importantes sur le mur est les fissures mesurent environ 15 a 20 centimetres de longueur letat du beton arme semble preoccupant je recommande une inspection detaillee par un ingenieur structure le coffrage du voile presente egalement des defauts il y a des traces dinfiltration deau pres des banches les etais sont en bon etat mais il faut verifier la stabilite avant de poursuivre les travaux il faut maintenant inspecter le 4eme etage pour verifier letat des dalles et des poutres fin de linspection du batiment a 3eme etage

### Model: gpt-audio-mini
- Status: ✅ Success
- Latency: 4.51s
- **Word Error Rate (Meaningful): 3.94%**
- Transcript: Bonjour, je suis chef de chantier sur le site de Vinci Construction. Aujourd'hui, le 6 novembre 2025, je fais l'inspection du bâtiment A. Je me trouve actuellement au troisième étage devant l'entrée principale. J'ai remarqué trois fissures importantes sur le mur Est. Les fissures mesurent environ 15 à 20 cm de longueur. L'état du béton armé semble préoccupant. Je recommande une inspection détaillée par un ingénieur structure. Le coffrage du voile présente également des défauts et il y a des traces d'infiltration d'eau près des bancs. Les étés sont en bon état, mais il faut vérifier la stabilité avant de poursuivre les travaux. Il faut maintenant inspecter le quatrième étage pour vérifier l'état des dalles et des poutres. Fin de l'inspection du bâtiment A, troisième étage.
- Meaningful Errors: substitutions=4, insertions=1, deletions=0
#### Meaningful Error Details (Semantic differences only)
- Replace: expected "centimetres" | actual "cm"
- Replace: expected "structures" | actual "structure"
- Insert: expected "" | actual "et"
- Replace: expected "je vais" | actual "il faut"
- Raw WER (before normalization): 9.60%
- Normalized Reference: bonjour je suis chef de chantier sur le site de vinci construction aujourd'hui le 6 novembre 2025 je fais linspection du batiment a je me trouve actuellement au 3eme etage devant lentre principale jai remarque 3 fissures importantes sur le mur est les fissures mesurent environ 15 a 20 centimetres de longueur l etat du beton arme semble preoccupant je recommande une inspection detaillee par un ingenieur structures le coffrage du voile presente egalement des defauts il y a des traces dinfiltration deau pres des banches les etais sont en bon etat mais il faut verifier la stabilite avant de poursuivre les travaux je vais maintenant inspecter le 4eme etage pour verifier l etat des dalles et des poutres fin de linspection du batiment a 3eme etage
- Normalized Transcript: bonjour je suis chef de chantier sur le site de vinci construction aujourd'hui le 6 novembre 2025 je fais linspection du batiment a je me trouve actuellement au 3eme etage devant lentre principale jai remarque 3 fissures importantes sur le mur est les fissures mesurent environ 15 a 20 cm de longueur l etat du beton arme semble preoccupant je recommande une inspection detaillee par un ingenieur structure le coffrage du voile presente egalement des defauts et il y a des traces dinfiltration deau pres des banches les etais sont en bon etat mais il faut verifier la stabilite avant de poursuivre les travaux il faut maintenant inspecter le 4eme etage pour verifier l etat des dalles et des poutres fin de linspection du batiment a 3eme etage

### Model: gpt-4o-transcribe
- Status: ❌ Failed
- Error: `Error code: 404 - {'error': {'code': 'DeploymentNotFound', 'message': 'The API deployment for this resource does not exist. If you created the deployment within the last 5 minutes, please wait a moment and try again.'}}`

### Model: gpt-4o-mini-transcribe
- Status: ❌ Failed
- Error: `Error code: 404 - {'error': {'code': 'DeploymentNotFound', 'message': 'The API deployment for this resource does not exist. If you created the deployment within the last 5 minutes, please wait a moment and try again.'}}`

### Model: gpt-4o-audio-preview
- Status: ✅ Success
- Latency: 2.89s
- **Word Error Rate (Meaningful): 2.40%**
- Transcript: Bonjour, je suis chef de chantier sur le site de Vinci Construction. Aujourd'hui, le 6 novembre 2025, je fais l'inspection du bâtiment A. Je me trouve actuellement au troisième étage, devant l'entrée principale. J'ai remarqué trois fissures importantes sur le mur est. Les fissures mesurent environ 15 à 20 centimètres de longueur. L'état du béton armé semble préoccupant; je recommande une inspection détaillée par un ingénieur structure. Le coffrage du voile présente également des défauts. Il y a des traces d'infiltration d'eau près des banches. Les étais sont en bon état, mais il faut vérifier la stabilité avant de poursuivre les travaux. Il faut maintenant inspecter le quatrième étage pour vérifier l'état des dalles et des poutres. Fin de l'inspection du bâtiment A, troisième étage.
- Meaningful Errors: substitutions=3, insertions=0, deletions=0
#### Meaningful Error Details (Semantic differences only)
- Replace: expected "structures" | actual "structure"
- Replace: expected "je vais" | actual "il faut"
- Raw WER (before normalization): 4.80%
- Normalized Reference: bonjour je suis chef de chantier sur le site de vinci construction aujourd'hui le 6 novembre 2025 je fais linspection du batiment a je me trouve actuellement au 3eme etage devant lentre principale jai remarque 3 fissures importantes sur le mur est les fissures mesurent environ 15 a 20 centimetres de longueur letat du beton arme semble preoccupant je recommande une inspection detaillee par un ingenieur structures le coffrage du voile presente egalement des defauts il y a des traces dinfiltration deau pres des banches les etais sont en bon etat mais il faut verifier la stabilite avant de poursuivre les travaux je vais maintenant inspecter le 4eme etage pour verifier letat des dalles et des poutres fin de linspection du batiment a 3eme etage
- Normalized Transcript: bonjour je suis chef de chantier sur le site de vinci construction aujourd'hui le 6 novembre 2025 je fais linspection du batiment a je me trouve actuellement au 3eme etage devant lentre principale jai remarque 3 fissures importantes sur le mur est les fissures mesurent environ 15 a 20 centimetres de longueur letat du beton arme semble preoccupant je recommande une inspection detaillee par un ingenieur structure le coffrage du voile presente egalement des defauts il y a des traces dinfiltration deau pres des banches les etais sont en bon etat mais il faut verifier la stabilite avant de poursuivre les travaux il faut maintenant inspecter le 4eme etage pour verifier letat des dalles et des poutres fin de linspection du batiment a 3eme etage

---

## audio_02_technical.wav
- Audio file: `data/mine/processed/audio_02_technical.wav`
- Reference transcript: `data/mine/processed/audio_02_reference.txt`
- Reference text: Inspection technique du bâtiment B, niveau -1.

Le coffrage métallique présente des déformations au niveau des panneaux. Les banches doivent être remplacées avant la prochaine coulée.

Le ferraillage du voile en béton armé est conforme aux plans. Les aciers haute adhérence HA400 sont correctement positionnés.

Les étais tubulaires supportant le plancher du rez-de-chaussée sont espacés de 1m20. C'est conforme aux prescriptions du bureau d'études.

J'observe des nids de gravier dans la dalle. Le béton n'a pas été correctement vibré lors de la coulée précédente.

Les joints de dilatation nécessitent un calfeutrement. Il y a des infiltrations d'eau par les reprises de bétonnage.

Le cuvelage du sous-sol présente des fissurations en escalier. Cela indique probablement un tassement différentiel des fondations.

Les armatures en attente dépassent de quarante centimètres. Elles doivent être protégées contre la corrosion.

Le décoffrage peut être effectué dans 48H , sous réserve d'un essai de résistance du béton.

Fin de l'inspection technique.

### Model: gpt-audio
- Status: ✅ Success
- Latency: 4.11s
- **Word Error Rate (Meaningful): 6.71%**
- Transcript: Inspection technique du bâtiment B, niveau moins un. Le coffrage métallique présente des déformations au niveau des panneaux, les banches doivent être remplacées dans la prochaine coulée. Le ferraillage du voile en béton armé est conforme au plan, les aciers haute adhérence HA 400 sont correctement positionnés. Les étais tubulaires supportant le plancher du rez-de-chaussée sont espacés de 1 mètre 20. C’est conforme aux prescriptions du bureau d’études. J’observe des nids de gravier dans la dalle. Le béton n’a pas été correctement vibré lors de la coulée précédente. Les joints de dilatation nécessitent un calfeutrement. Il y a des infiltrations d’eau par les reprises de bétonnage. Le cuvelage du sous-sol présente des fissures en escalier, cela indique probablement un tassement différentiel des fondations. Les armatures en attente dépassent de 40 centimètres, elles doivent être protégées contre la corrosion. Le décoffrage peut être effectué dans 48 heures sous réserve d’un essai de résistance du béton. Fin de l’inspection technique.
- Meaningful Errors: substitutions=11, insertions=0, deletions=0
#### Meaningful Error Details (Semantic differences only)
- Replace: expected "avant" | actual "dans"
- Replace: expected "aux plans" | actual "au plan"
- Replace: expected "ha400" | actual "ha 400"
- Replace: expected "1m20" | actual "1 metre 20"
- Replace: expected "fissurations" | actual "fissures"
- Replace: expected "48h" | actual "48 heures"
- Raw WER (before normalization): 18.18%
- Normalized Reference: inspection technique du batiment b niveau moins 1 le coffrage metallique presente des deformations au niveau des panneaux les banches doivent etre remplacees avant la prochaine coulee le ferraillage du voile en beton arme est conforme aux plans les aciers haute adherence ha400 sont correctement positionnes les etais tubulaires supportant le plancher du rez de chaussee sont espaces de 1m20 c est conforme aux prescriptions du bureau d etudes j observe des nids de gravier dans la dalle le beton n a pas ete correctement vibre lors de la coulee precedente les joints de dilatation necessitent un calfeutrement il y a des infiltrations d eau par les reprises de betonnage le cuvelage du sous sol presente des fissurations en escalier cela indique probablement un tassement differentiel des fondations les armatures en attente depassent de 40 centimetres elles doivent etre protegees contre la corrosion le decoffrage peut etre effectue dans 48h sous reserve d un essai de resistance du beton fin de l inspection technique
- Normalized Transcript: inspection technique du batiment b niveau moins 1 le coffrage metallique presente des deformations au niveau des panneaux les banches doivent etre remplacees dans la prochaine coulee le ferraillage du voile en beton arme est conforme au plan les aciers haute adherence ha 400 sont correctement positionnes les etais tubulaires supportant le plancher du rez de chaussee sont espaces de 1 metre 20 c est conforme aux prescriptions du bureau d etudes j observe des nids de gravier dans la dalle le beton n a pas ete correctement vibre lors de la coulee precedente les joints de dilatation necessitent un calfeutrement il y a des infiltrations d eau par les reprises de betonnage le cuvelage du sous sol presente des fissures en escalier cela indique probablement un tassement differentiel des fondations les armatures en attente depassent de 40 centimetres elles doivent etre protegees contre la corrosion le decoffrage peut etre effectue dans 48 heures sous reserve d un essai de resistance du beton fin de l inspection technique

### Model: gpt-audio-mini
- Status: ✅ Success
- Latency: 6.05s
- **Word Error Rate (Meaningful): 5.73%**
- Transcript: Tu n'as pas joint de fichier audio, seulement du texte. Voici la transcription exacte de ton texte :

Inspection technique du bâtiment B, niveau -1. Le coffrage métallique présente des déformations au niveau des panneaux. Les bancs doivent être remplacés dans la prochaine coulée. Le ferraillage du voile en béton armé est conforme au plan. Les aciers haute, adhérence HA 400, sont correctement positionnés. Les étais tubulaires soutenant le plancher du rez-de-chaussée sont espacés de 1,20 m. C'est conforme aux prescriptions du bureau d'études. J'observe des nids de gravier dans la dalle. Le béton n'a pas été correctement vibré lors de la coulée précédente. Les joints de dilatation nécessitent un calfeutrement. Il y a des infiltrations d'eau par les reprises de bétonnage. Le cuvelage du sous-sol présente des fissures en escalier. Cela indique probablement un tassement différentiel des fondations. Les armatures en attente dépassent de 40 cm. Elles doivent être protégées contre la corrosion. Le décoffrage peut être effectué dans 48 heures, sous réserve d'un essai de résistance du béton. Fin de l'inspection technique.
- Meaningful Errors: substitutions=9, insertions=0, deletions=0
#### Meaningful Error Details (Semantic differences only)
- Replace: expected "avant" | actual "dans"
- Replace: expected "aux plans" | actual "au plan"
- Replace: expected "ha400" | actual "ha 400"
- Replace: expected "supportant" | actual "soutenant"
- Replace: expected "fissurations" | actual "fissures"
- Replace: expected "48h" | actual "48 heures"
- Raw WER (before normalization): 22.08%
- Normalized Reference: inspection technique du batiment b niveau moins 1 le coffrage metallique presente des deformations au niveau des panneaux les banches doivent etre remplacees avant la prochaine coulee le ferraillage du voile en beton arme est conforme aux plans les aciers haute adherence ha400 sont correctement positionnes les etais tubulaires supportant le plancher du rez de chaussee sont espaces de 1m20 cest conforme aux prescriptions du bureau detudes jobserve des nids de gravier dans la dalle le beton na pas ete correctement vibre lors de la coulee precedente les joints de dilatation necessitent un calfeutrement il y a des infiltrations deau par les reprises de betonnage le cuvelage du sous sol presente des fissurations en escalier cela indique probablement un tassement differentiel des fondations les armatures en attente depassent de 40 centimetres elles doivent etre protegees contre la corrosion le decoffrage peut etre effectue dans 48h sous reserve dun essai de resistance du beton fin de linspection technique
- Normalized Transcript: inspection technique du batiment b niveau moins 1 le coffrage metallique presente des deformations au niveau des panneaux les banches doivent etre remplacees dans la prochaine coulee le ferraillage du voile en beton arme est conforme au plan les aciers haute adherence ha 400 sont correctement positionnes les etais tubulaires soutenant le plancher du rez de chaussee sont espaces de 1m20 cest conforme aux prescriptions du bureau detudes jobserve des nids de gravier dans la dalle le beton na pas ete correctement vibre lors de la coulee precedente les joints de dilatation necessitent un calfeutrement il y a des infiltrations deau par les reprises de betonnage le cuvelage du sous sol presente des fissures en escalier cela indique probablement un tassement differentiel des fondations les armatures en attente depassent de 40 centimetres elles doivent etre protegees contre la corrosion le decoffrage peut etre effectue dans 48 heures sous reserve dun essai de resistance du beton fin de linspection technique

### Model: gpt-4o-transcribe
- Status: ❌ Failed
- Error: `Error code: 404 - {'error': {'code': 'DeploymentNotFound', 'message': 'The API deployment for this resource does not exist. If you created the deployment within the last 5 minutes, please wait a moment and try again.'}}`

### Model: gpt-4o-mini-transcribe
- Status: ❌ Failed
- Error: `Error code: 404 - {'error': {'code': 'DeploymentNotFound', 'message': 'The API deployment for this resource does not exist. If you created the deployment within the last 5 minutes, please wait a moment and try again.'}}`

### Model: gpt-4o-audio-preview
- Status: ✅ Success
- Latency: 3.71s
- **Word Error Rate (Meaningful): 4.88%**
- Transcript: Inspection technique du bâtiment B - niveau moins un. Le coffrage métallique présente des déformations au niveau des panneaux. Les planches doivent être remplacées dans la prochaine coulée. Le ferraillage du voile en béton armé est conforme au plan; les aciers haute adhérence, H.A. 400, sont correctement positionnés. Les étais tubulaires supportant le plancher du rez-de-chaussée sont espacés de 1 mètre 20 ; c’est conforme aux prescriptions du bureau d'études. J'observe des nids de gravier dans la dalle. Le béton n'a pas été correctement vibré lors de la coulée précédente. Les joints de dilatation nécessitent un calfeutrage. Il y a des infiltrations d'eau par les reprises de bétonnage. Le cuvelage du sous-sol présente des fissures en escalier ; cela indique probablement un tassement différentiel des fondations. Les armatures en attente dépassent de 40 centimètres ; elles doivent être protégées contre la corrosion. Le décoffrage peut être effectué dans 48 heures, sous réserve d'un essai de résistance du béton. Fin de l'inspection technique.
- Meaningful Errors: substitutions=8, insertions=0, deletions=0
#### Meaningful Error Details (Semantic differences only)
- Replace: expected "avant" | actual "dans"
- Replace: expected "aux plans" | actual "au plan"
- Replace: expected "ha400" | actual "ha 400"
- Replace: expected "fissurations" | actual "fissures"
- Replace: expected "48h" | actual "48 heures"
- Raw WER (before normalization): 18.18%
- Normalized Reference: inspection technique du batiment b niveau moins 1 le coffrage metallique presente des deformations au niveau des panneaux les banches doivent etre remplacees avant la prochaine coulee le ferraillage du voile en beton arme est conforme aux plans les aciers haute adherence ha400 sont correctement positionnes les etais tubulaires supportant le plancher du rez de chaussee sont espaces de 1m20 c est conforme aux prescriptions du bureau d etudes j observe des nids de gravier dans la dalle le beton n a pas ete correctement vibre lors de la coulee precedente les joints de dilatation necessitent un calfeutrement il y a des infiltrations d eau par les reprises de betonnage le cuvelage du sous sol presente des fissurations en escalier cela indique probablement un tassement differentiel des fondations les armatures en attente depassent de 40 centimetres elles doivent etre protegees contre la corrosion le decoffrage peut etre effectue dans 48h sous reserve d un essai de resistance du beton fin de l inspection technique
- Normalized Transcript: inspection technique du batiment b niveau moins 1 le coffrage metallique presente des deformations au niveau des panneaux les banches doivent etre remplacees dans la prochaine coulee le ferraillage du voile en beton arme est conforme au plan les aciers haute adherence ha 400 sont correctement positionnes les etais tubulaires supportant le plancher du rez de chaussee sont espaces de 1m20 c est conforme aux prescriptions du bureau d etudes j observe des nids de gravier dans la dalle le beton n a pas ete correctement vibre lors de la coulee precedente les joints de dilatation necessitent un calfeutrement il y a des infiltrations d eau par les reprises de betonnage le cuvelage du sous sol presente des fissures en escalier cela indique probablement un tassement differentiel des fondations les armatures en attente depassent de 40 centimetres elles doivent etre protegees contre la corrosion le decoffrage peut etre effectue dans 48 heures sous reserve d un essai de resistance du beton fin de l inspection technique

---

## audio_03_numbers.wav
- Audio file: `data/mine/processed/audio_03_numbers.wav`
- Reference transcript: `data/mine/processed/audio_03_reference.txt`
- Reference text: Relevé des mesures, bâtiment C, étage deux.

Fissure numéro 1: longueur 23 cm, largeur 2 mm, profondeur environ 5 mm.

Fissure numéro deux: longueur 37 cm, largeur 3 mm, orientation 45 degrés par rapport à l'horizontale.

Fissure numéro trois: longueur 15 cm, située à un mètre cinquante du sol.

Surface totale du mur: 4 m de hauteur sur 8 m de longueur, soit 32 mètres carrés.

Nombre d'armatures visibles: 12 barres de diamètre 16 mm.

Espacement entre les poteaux: 4 m 50.

Épaisseur du voile: 26 cm.

Charge prévue sur la dalle: 500 kilogrammes par mètre carré.

Température du béton: 18 degrés Celsius.

Humidité relative: 65 pour cent.

Résistance du béton testée: 30 mégapascals après 28 jours.

Flèche mesurée au centre de la poutre: 8 millimètres, dans les tolérances acceptables.

Nombre d'ouvriers présents: 15 personnes.

Fin du relevé des mesures.

### Model: gpt-audio
- Status: ✅ Success
- Latency: 4.11s
- **Word Error Rate (Meaningful): 3.50%**
- Transcript: Relevé de mesures, bâtiment C, étage 2. Fissure numéro 1 : longueur 23 cm, largeur 2 mm, profondeur environ 5 mm. Fissure numéro 2 : longueur 37 cm, largeur 3 mm, orientation 45 degrés par rapport à l'horizontale. Fissure numéro 3 : largeur 15 cm, située à 1 mètre 40 du sol. Surface totale du mur : 4 murs de hauteur sur 8 mètres de longueur, soit 32 mètres carrés. Nombre d’armatures visibles : 12 barres de diamètre 16 mm. Espacement entre les poteaux : 4 mètres 50. Épaisseur du voile : 25 cm. Charge prévue sur la dalle : 500 kg par mètre carré. Température du béton : 18 degrés Celsius. Humidité relative : 65 %. Résistance du béton testée : 30 mégapascals après 28 jours. Flèche mesurée au centre de la poutre : 8 mm, dans les tolérances acceptables. Nombre d’ouvriers présents : 15 personnes. Fin du relevé des mesures.
- Meaningful Errors: substitutions=5, insertions=0, deletions=0
#### Meaningful Error Details (Semantic differences only)
- Replace: expected "longueur" | actual "largeur"
- Replace: expected "50" | actual "40"
- Replace: expected "26" | actual "25"
- Replace: expected "kilogrammes" | actual "kg"
- Replace: expected "millimètres" | actual "mm"
- Raw WER (before normalization): 29.29%
- Normalized Reference: relevé des mesures bâtiment c étage 2 fissure numéro 1 longueur 23 cm largeur 2 mm profondeur environ 5 mm fissure numéro 2 longueur 37 cm largeur 3 mm orientation 45 degrés par rapport à l horizontale fissure numéro 3 longueur 15 cm située à 1 mètre 50 du sol surface totale du mur 4 m de hauteur sur 8 m de longueur soit 32 mètres carrés nombre d armatures visibles 12 barres de diamètre 16 mm espacement entre les poteaux 4 m 50 épaisseur du voile 26 cm charge prévue sur la dalle 500 kilogrammes par mètre carré température du béton 18 degrés celsius humidité relative 65 pour cent résistance du béton testée 30 mégapascals après 28 jours flèche mesurée au centre de la poutre 8 millimètres dans les tolérances acceptables nombre d ouvriers présents 15 personnes fin du relevé des mesures
- Normalized Transcript: relevé des mesures bâtiment c étage 2 fissure numéro 1 longueur 23 cm largeur 2 mm profondeur environ 5 mm fissure numéro 2 longueur 37 cm largeur 3 mm orientation 45 degrés par rapport à l horizontale fissure numéro 3 largeur 15 cm située à 1 mètre 40 du sol surface totale du mur 4 m de hauteur sur 8 m de longueur soit 32 mètres carrés nombre d armatures visibles 12 barres de diamètre 16 mm espacement entre les poteaux 4 m 50 épaisseur du voile 25 cm charge prévue sur la dalle 500 kg par mètre carré température du béton 18 degrés celsius humidité relative 65 pour cent résistance du béton testée 30 mégapascals après 28 jours flèche mesurée au centre de la poutre 8 mm dans les tolérances acceptables nombre d ouvriers présents 15 personnes fin du relevé des mesures

### Model: gpt-audio-mini
- Status: ✅ Success
- Latency: 5.37s
- **Word Error Rate (Meaningful): 8.39%**
- Transcript: {"message": "Relevé de mesures, bâtiment C, étage 2.\nFissure n° 1 : Longueur 23 cm, largeur 2 mm, profondeur environ 5 mm.\nFissure n° 2 : Longueur 37 cm, largeur 3 mm, orientation 45° par rapport à l'horizontale.\nFissure n° 3 : Largeur 15 cm, située à 1,40 m du sol.\nSurface totale du mur : 4 murs d'hauteur sur 8 m de longueur, soit 32 m².\nNombre d'armatures visibles : 12 barres de diamètre 16 mm.\nEspacement entre les poteaux : 4 m 50.\nÉpaisseur du voile : 25 cm.\nCharge prévue sur la dalle : 500 kg par m².\nTempérature du béton : 18°C.\nHumidité relative : 65 %.\nRésistance du béton testée : 30 MPa après 28 jours.\nFlèche mesurée au centre de la poutre : 8 mm, dont les tolérances acceptables.\nNombre d'ouvriers présents : 15 personnes.\nFin du relevé des mesures."}
- Meaningful Errors: substitutions=12, insertions=0, deletions=0
#### Meaningful Error Details (Semantic differences only)
- Replace: expected "des" | actual "de"
- Replace: expected "deux" | actual "2"
- Replace: expected "numéro" | actual "n°"
- Replace: expected "numéro" | actual "n°"
- Replace: expected "numéro" | actual "n°"
- Replace: expected "longueur" | actual "largeur"
- Replace: expected "un mètre cinquante" | actual "1 m 50"
- Replace: expected "de" | actual "d"
- Replace: expected "mètres" | actual "m"
- Replace: expected "26" | actual "25"
- Raw WER (before normalization): 54.29%
- Normalized Reference: relevé des mesures bâtiment c étage deux fissure numéro 1 longueur 23 cm largeur 2 mm profondeur environ 5 mm fissure numéro 2 longueur 37 cm largeur 3 mm orientation 45 degrés par rapport à l horizontale fissure numéro 3 longueur 15 cm située à un mètre cinquante du sol surface totale du mur 4 m de hauteur sur 8 m de longueur soit 32 mètres carrés nombre d armatures visibles 12 barres de diamètre 16 mm espacement entre les poteaux 4 m 50 épaisseur du voile 26 cm charge prévue sur la dalle 500 kilogrammes par mètre carré température du béton 18 degrés celsius humidité relative 65 pour cent résistance du béton testée 30 mégapascals après 28 jours flèche mesurée au centre de la poutre 8 millimètres dans les tolérances acceptables nombre d ouvriers présents 15 personnes fin du relevé des mesures
- Normalized Transcript: relevé de mesures bâtiment c étage 2 fissure n° 1 longueur 23 cm largeur 2 mm profondeur environ 5 mm fissure n° 2 longueur 37 cm largeur 3 mm orientation 45 degrés par rapport à l horizontale fissure n° 3 largeur 15 cm située à 1 m 50 du sol surface totale du mur 4 m d hauteur sur 8 m de longueur soit 32 m carrés nombre d armatures visibles 12 barres de diamètre 16 mm espacement entre les poteaux 4 m 50 épaisseur du voile 25 cm charge prévue sur la dalle 500 kilogrammes par mètre carré température du béton 18 degrés celsius humidité relative 65 pour cent résistance du béton testée 30 mégapascals après 28 jours flèche mesurée au centre de la poutre 8 millimètres dans les tolérances acceptables nombre d ouvriers présents 15 personnes fin du relevé des mesures

### Model: gpt-4o-transcribe
- Status: ❌ Failed
- Error: `Error code: 404 - {'error': {'code': 'DeploymentNotFound', 'message': 'The API deployment for this resource does not exist. If you created the deployment within the last 5 minutes, please wait a moment and try again.'}}`

### Model: gpt-4o-mini-transcribe
- Status: ❌ Failed
- Error: `Error code: 404 - {'error': {'code': 'DeploymentNotFound', 'message': 'The API deployment for this resource does not exist. If you created the deployment within the last 5 minutes, please wait a moment and try again.'}}`

### Model: gpt-4o-audio-preview
- Status: ✅ Success
- Latency: 3.56s
- **Word Error Rate (Meaningful): 6.29%**
- Transcript: Relevé de mesures bâtiment C, étage 2.
Fissure numéro 1 : longueur 23 cm, largeur 2 mm, profondeur environ 5 mm.
Fissure numéro 2 : longueur 37 cm, largeur 3 mm, orientation 45 degrés par rapport à l’horizontale.
Fissure numéro 3 : longueur 15 cm, située à 1,40 m du sol.
Surface totale du mur : 4 murs de 2,50 m de hauteur sur 8 m de longueur, soit 32 m².
Nombre d’armatures visibles : 12 barres de diamètre 16 mm.
Espacement entre les poteaux : 4,50 m.
Épaisseur du voile : 25 cm.
Charge prévue sur la dalle : 500 kg/m².
Température du béton : 18 degrés Celsius.
Humidité relative : 65 %.
Résistance du béton testée : 30 MPa après 28 jours.
Flèche mesurée au centre de la poutre : 8 mm, dans les tolérances acceptables.
Nombre d’ouvriers présents : 15 personnes.
Fin du relevé des mesures.
- Meaningful Errors: substitutions=9, insertions=0, deletions=0
#### Meaningful Error Details (Semantic differences only)
- Replace: expected "des" | actual "de"
- Replace: expected "50" | actual "40"
- Replace: expected "m" | actual "murs de 2 mètre 50"
- Replace: expected "m" | actual "mètre"
- Replace: expected "26" | actual "25"
- Raw WER (before normalization): 49.29%
- Normalized Reference: relevé des mesures bâtiment c étage 2 fissure numéro 1 longueur 23 cm largeur 2 mm profondeur environ 5 mm fissure numéro 2 longueur 37 cm largeur 3 mm orientation 45 degrés par rapport à l horizontale fissure numéro 3 longueur 15 cm située à 1 mètre 50 du sol surface totale du mur 4 m de hauteur sur 8 m de longueur soit 32 mètres carrés nombre d armatures visibles 12 barres de diamètre 16 mm espacement entre les poteaux 4 m 50 épaisseur du voile 26 cm charge prévue sur la dalle 500 kilogrammes par mètre carré température du béton 18 degrés celsius humidité relative 65 pour cent résistance du béton testée 30 mégapascals après 28 jours flèche mesurée au centre de la poutre 8 millimètres dans les tolérances acceptables nombre d ouvriers présents 15 personnes fin du relevé des mesures
- Normalized Transcript: relevé de mesures bâtiment c étage 2 fissure numéro 1 longueur 23 cm largeur 2 mm profondeur environ 5 mm fissure numéro 2 longueur 37 cm largeur 3 mm orientation 45 degrés par rapport à l horizontale fissure numéro 3 longueur 15 cm située à 1 mètre 40 du sol surface totale du mur 4 murs de 2 mètre 50 de hauteur sur 8 m de longueur soit 32 mètres carrés nombre d armatures visibles 12 barres de diamètre 16 mm espacement entre les poteaux 4 mètre 50 épaisseur du voile 25 cm charge prévue sur la dalle 500 kilogrammes par mètre carré température du béton 18 degrés celsius humidité relative 65 pour cent résistance du béton testée 30 mégapascals après 28 jours flèche mesurée au centre de la poutre 8 millimètres dans les tolérances acceptables nombre d ouvriers présents 15 personnes fin du relevé des mesures

---

## audio_04_short_notes.wav
- Audio file: `data/mine/processed/audio_04_short_notes.wav`
- Reference transcript: `data/mine/processed/audio_04_reference.txt`
- Reference text: Note numéro 1: Appeler le fournisseur de ciment demain matin à 9 h.

Note numéro 2: Le camion toupie arrive à quatorze heures pour la coulée du radier.

Note numéro 3: Vérifier la conformité des plans avec l'architecte avant mercredi.

Note numéro 4: Commander 30 mètres cubes de béton C vingt-cinq trente pour la semaine prochaine.

Note numéro 5: Réunion de coordination vendredi à 10 h avec tous les corps d'état.

Note numéro 6: Prévoir l'évacuation des gravats du sous-sol. Volume estimé: 50 mètres cubes.

Note numéro 7: Le contrôle technique passe lundi matin. Préparer les documents de suivi.

Note numéro 8: Problème avec la grue à tour. Le mécanicien doit intervenir aujourd'hui.

Note numéro 9: Livraison des banches reportée au jeudi. Adapter le planning en conséquence.

Note numéro 10: Installer les garde-corps au niveau du cinquième étage avant la fin de semaine.

Note numéro 11: Mettre en place la signalétique de sécurité sur l'ensemble du chantier.

Note numéro 12: Fin des notes rapides.

### Model: gpt-audio
- Status: ✅ Success
- Latency: 4.59s
- **Word Error Rate (Meaningful): 1.78%**
- Transcript: Note numéro 1 : Appeler le fournisseur de ciment demain matin à 9h.  
Note numéro 2 : Le camion toupie arrive à 14h pour la coulée du radier.  
Note numéro 3 : Vérifier la conformité des plans avec l’architecte avant mercredi.  
Note numéro 4 : Commander 30 m³ de béton C2530 pour la semaine prochaine.  
Note numéro 5 : Réunion de coordination vendredi à 10h avec tous les corps d’état.  
Note numéro 6 : Prévoir l’évacuation des gravats du sous-sol, volume estimé 50 m³.  
Note numéro 7 : Le contrôle technique passe lundi matin, préparer le document de suivi.  
Note numéro 8 : Problème avec la grue à tour, le mécanicien doit intervenir aujourd’hui.  
Note numéro 9 : Livraison des banches reportée au jeudi, adapter le plan en conséquence.  
Note numéro 10 : Installer les garde-corps au niveau du cinquième étage avant la fin de semaine.  
Note numéro 11 : Mettre en place la signalétique de sécurité sur l’ensemble du chantier.  
Note numéro 12 : Fin des notes rapides.
- Meaningful Errors: substitutions=3, insertions=0, deletions=0
#### Meaningful Error Details (Semantic differences only)
- Replace: expected "les documents" | actual "le document"
- Replace: expected "planning" | actual "plan"
- Raw WER (before normalization): 32.93%
- Normalized Reference: note numero 1 appeler le fournisseur de ciment demain matin a 9 h note numero 2 le camion toupie arrive a 14 heures pour la coulee du radier note numero 3 verifier la conformite des plans avec l architecte avant mercredi note numero 4 commander 30 metres cubes de beton c 25 30 pour la semaine prochaine note numero 5 reunion de coordination vendredi a 10 h avec tous les corps d etat note numero 6 prevoir levacuation des gravats du sous sol volume estime 50 metres cubes note numero 7 le controle technique passe lundi matin preparer les documents de suivi note numero 8 probleme avec la grue a tour le mecanicien doit intervenir aujourd hui note numero 9 livraison des banches reportee au jeudi adapter le planning en consequence note numero 10 installer les garde corps au niveau du cinquieme etage avant la fin de semaine note numero 11 mettre en place la signaletique de securite sur lensemble du chantier note numero 12 fin des notes rapides
- Normalized Transcript: note numero 1 appeler le fournisseur de ciment demain matin a 9 h note numero 2 le camion toupie arrive a 14 heures pour la coulee du radier note numero 3 verifier la conformite des plans avec l architecte avant mercredi note numero 4 commander 30 metres cubes de beton c 25 30 pour la semaine prochaine note numero 5 reunion de coordination vendredi a 10 h avec tous les corps d etat note numero 6 prevoir levacuation des gravats du sous sol volume estime 50 metres cubes note numero 7 le controle technique passe lundi matin preparer le document de suivi note numero 8 probleme avec la grue a tour le mecanicien doit intervenir aujourd hui note numero 9 livraison des banches reportee au jeudi adapter le plan en consequence note numero 10 installer les garde corps au niveau du cinquieme etage avant la fin de semaine note numero 11 mettre en place la signaletique de securite sur lensemble du chantier note numero 12 fin des notes rapides

### Model: gpt-audio-mini
- Status: ✅ Success
- Latency: 3.35s
- **Word Error Rate (Meaningful): 3.53%**
- Transcript: Nous notons le point numéro 1 : appeler le fournisseur de ciment demain matin à 9h. Note numéro 2 : le camion toupie arrive à 14h pour la coulée du radier. Note numéro 3 : vérifier la conformité des plans avec l'architecte avant mercredi. Note numéro 4 : commander 30 m³ de béton C25/30 pour la semaine prochaine. Note numéro 5 : réunion de coordination vendredi de 6h à 10h avec tous les corps d'état. Note numéro 6 : prévoir l'évacuation des gravats du sous-sol. Volume estimé, 50 m³. Note numéro 7 : le contrôle technique passe lundi matin. Préparer le document de suivi. Note numéro 8 : problème avec la grue à tour. Le mécanicien doit intervenir aujourd'hui. Note numéro 9 : livraison des banches reportée au jeudi. Adapter le plan en conséquence. Note numéro 10 : installer les garde-corps au niveau du 5ème étage avant la fin de semaine. Note numéro 11 : mettre en place la signalétique de sécurité sur l'ensemble du chantier. Note numéro 12 : fin des notes rapides.
- Meaningful Errors: substitutions=3, insertions=3, deletions=0
#### Meaningful Error Details (Semantic differences only)
- Insert: expected "" | actual "de 6 h"
- Replace: expected "les documents" | actual "le document"
- Replace: expected "planning" | actual "plan"
- Raw WER (before normalization): 36.59%
- Normalized Reference: note numero 1 appeler le fournisseur de ciment demain matin a 9 h note numero 2 le camion toupie arrive a 14 heures pour la coulee du radier note numero 3 verifier la conformite des plans avec l architecte avant mercredi note numero 4 commander 30 metres cubes de beton c 25 30 pour la semaine prochaine note numero 5 reunion de coordination vendredi a 10 h avec tous les corps d etat note numero 6 prevoir levacuation des gravats du sous sol volume estime 50 metres cubes note numero 7 le controle technique passe lundi matin preparer les documents de suivi note numero 8 probleme avec la grue a tour le mecanicien doit intervenir aujourd hui note numero 9 livraison des banches reportee au jeudi adapter le planning en consequence note numero 10 installer les garde corps au niveau du cinquieme etage avant la fin de semaine note numero 11 mettre en place la signaletique de securite sur l ensemble du chantier note numero 12 fin des notes rapides
- Normalized Transcript: note numero 1 appeler le fournisseur de ciment demain matin a 9 h note numero 2 le camion toupie arrive a 14 heures pour la coulee du radier note numero 3 verifier la conformite des plans avec l architecte avant mercredi note numero 4 commander 30 metres cubes de beton c 25 30 pour la semaine prochaine note numero 5 reunion de coordination vendredi de 6 h a 10 h avec tous les corps d etat note numero 6 prevoir levacuation des gravats du sous sol volume estime 50 metres cubes note numero 7 le controle technique passe lundi matin preparer le document de suivi note numero 8 probleme avec la grue a tour le mecanicien doit intervenir aujourd hui note numero 9 livraison des banches reportee au jeudi adapter le plan en consequence note numero 10 installer les garde corps au niveau du cinquieme etage avant la fin de semaine note numero 11 mettre en place la signaletique de securite sur l ensemble du chantier note numero 12 fin des notes rapides

### Model: gpt-4o-transcribe
- Status: ❌ Failed
- Error: `Error code: 404 - {'error': {'code': 'DeploymentNotFound', 'message': 'The API deployment for this resource does not exist. If you created the deployment within the last 5 minutes, please wait a moment and try again.'}}`

### Model: gpt-4o-mini-transcribe
- Status: ❌ Failed
- Error: `Error code: 404 - {'error': {'code': 'DeploymentNotFound', 'message': 'The API deployment for this resource does not exist. If you created the deployment within the last 5 minutes, please wait a moment and try again.'}}`

### Model: gpt-4o-audio-preview
- Status: ✅ Success
- Latency: 3.65s
- **Word Error Rate (Meaningful): 1.76%**
- Transcript: 1. Appeler le fournisseur de ciment demain matin à 9h.
2. Le camion toupie arrive à 14h pour la coulée du radier.
3. Vérifier la conformité des plans avec l'architecte avant mercredi.
4. Commander 30m3 de béton C25/30 pour la semaine prochaine.
5. Réunion de coordination vendredi à 10h avec tous les corps d'état.
6. Prévoir l'évacuation des gravats du sous-sol, volume estimé : 50m3.
7. Le contrôle technique passe lundi matin, préparer le document de suivi.
8. Problème avec la grue à tour, le mécanicien doit intervenir aujourd'hui.
9. Livraison des banches reportée au jeudi, adapter le plan en conséquence.
10. Installer les garde-corps au niveau du 5ème étage avant la fin de semaine.
11. Mettre en place la signalétique de sécurité sur l'ensemble du chantier.
12. Fin des notes rapides.
- Meaningful Errors: substitutions=3, insertions=0, deletions=0
#### Meaningful Error Details (Semantic differences only)
- Replace: expected "les documents" | actual "le document"
- Replace: expected "planning" | actual "plan"
- Raw WER (before normalization): 44.51%
- Normalized Reference: note numero 1 appeler le fournisseur de ciment demain matin a 9 h note numero 2 le camion toupie arrive a 14 heures pour la coulee du radier note numero 3 verifier la conformite des plans avec l architecte avant mercredi note numero 4 commander 30 metres cubes de beton c 25 30 pour la semaine prochaine note numero 5 reunion de coordination vendredi a 10 h avec tous les corps d etat note numero 6 prevoir levacuation des gravats du sous sol volume estime 50 metres cubes note numero 7 le controle technique passe lundi matin preparer les documents de suivi note numero 8 probleme avec la grue a tour le mecanicien doit intervenir aujourd hui note numero 9 livraison des banches reportee au jeudi adapter le planning en consequence note numero 10 installer les garde corps au niveau du cinquieme etage avant la fin de semaine note numero 11 mettre en place la signaletique de securite sur l ensemble du chantier note numero 12 fin des notes rapides
- Normalized Transcript: note numero 1 appeler le fournisseur de ciment demain matin a 9 h note numero 2 le camion toupie arrive a 14 heures pour la coulee du radier note numero 3 verifier la conformite des plans avec l architecte avant mercredi note numero 4 commander 30 metres cubes de beton c 25 30 pour la semaine prochaine note numero 5 reunion de coordination vendredi a 10 h avec tous les corps d etat note numero 6 prevoir levacuation des gravats du sous sol volume estime 50 metres cubes note numero 7 le controle technique passe lundi matin preparer le document de suivi note numero 8 probleme avec la grue a tour le mecanicien doit intervenir aujourd hui note numero 9 livraison des banches reportee au jeudi adapter le plan en consequence note numero 10 installer les garde corps au niveau du cinquieme etage avant la fin de semaine note numero 11 mettre en place la signaletique de securite sur l ensemble du chantier note numero 12 fin des notes rapides

---

## audio_05_safety.wav
- Audio file: `data/mine/processed/audio_05_safety.wav`
- Reference transcript: `data/mine/processed/audio_05_reference.txt`
- Reference text: Déclaration d'incident, bâtiment D, niveau quatre.

Date: 6 novembre 2025, heure: 11h45.

Un ouvrier a glissé près du bord de la dalle. Pas de chute, mais situation dangereuse.

Le garde-corps temporaire était mal fixé. Il a bougé sous la pression.

L'ouvrier concerné: Monsieur Dupont, chef d'équipe gros œuvre.

Aucune blessure constatée. L'ouvrier a été examiné par le secouriste du chantier.

Mesures immédiates prises: zone sécurisée, accès interdit jusqu'à réparation complète du garde-corps.

Cause probable: fixation insuffisante des poteaux sur la dalle. Vis de fixation desserrées.

Actions correctives: vérification immédiate de tous les garde-corps sur l'ensemble du chantier.

Responsable sécurité informé à midi. Rapport écrit à transmettre au coordinateur SPS avant 16h.

Formation de rappel sur la sécurité en hauteur programmée pour toute l'équipe demain matin.

Aucun arrêt de travail nécessaire. Les travaux peuvent reprendre dès sécurisation de la zone.

Je reste disponible pour tout complément d'information.

Fin de la déclaration d'incident.

### Model: gpt-audio
- Status: ✅ Success
- Latency: 3.81s
- **Word Error Rate (Meaningful): 3.07%**
- Transcript: Déclaration d’incident bâtiment D, niveau 4. Date : 6 novembre 2025. Heure : 11h45. Un ouvrier a glissé près du bord de la dalle, pas de chute mais situation dangereuse. Le garde-corps temporaire était mal fixé, il a bougé sous la pression. L’ouvrier concerné : Monsieur Dupont, chef d’équipe gros œuvre. Aucune blessure constatée, l’ouvrier a été examiné par le secouriste du chantier. Mesure immédiate prise : zone sécurisée, accès interdit jusqu’à réparation complète du garde-corps. Cause probable : fixation insuffisante des poteaux sur la dalle, vis de fixation desserrées. Action corrective : vérification immédiate de tous les garde-corps sur l’ensemble du chantier, responsable sécurité informé à midi, rapport écrit à transmettre au coordonnateur SPS avant 16h. Formation de rappel sur la sécurité en hauteur programmée pour toute l’équipe demain matin. Aucun arrêt de travail nécessaire, les travaux peuvent reprendre dès sécurisation de la zone. Je reste disponible pour tout complément d’information. Fin de la déclaration d’incident.
- Meaningful Errors: substitutions=5, insertions=0, deletions=0
#### Meaningful Error Details (Semantic differences only)
- Replace: expected "mesures immediates prises" | actual "mesure immediate prise"
- Replace: expected "actions correctives" | actual "action corrective"
- Raw WER (before normalization): 27.15%
- Normalized Reference: declaration d incident batiment d niveau 4 date 6 novembre 2025 heure 11h45 un ouvrier a glisse pres du bord de la dalle pas de chute mais situation dangereuse le garde corps temporaire etait mal fixe il a bouge sous la pression l ouvrier concerne monsieur dupont chef d equipe gros oeuvre aucune blessure constatee l ouvrier a ete examine par le secouriste du chantier mesures immediates prises zone securisee acces interdit jusqu a reparation complete du garde corps cause probable fixation insuffisante des poteaux sur la dalle vis de fixation desserrees actions correctives verification immediate de tous les garde corps sur l ensemble du chantier responsable securite informe a midi rapport ecrit a transmettre au coordinateur sps avant 16h formation de rappel sur la securite en hauteur programmee pour toute l equipe demain matin aucun arret de travail necessaire les travaux peuvent reprendre des securisation de la zone je reste disponible pour tout complement d information fin de la declaration d incident
- Normalized Transcript: declaration d incident batiment d niveau 4 date 6 novembre 2025 heure 11h45 un ouvrier a glisse pres du bord de la dalle pas de chute mais situation dangereuse le garde corps temporaire etait mal fixe il a bouge sous la pression l ouvrier concerne monsieur dupont chef d equipe gros oeuvre aucune blessure constatee l ouvrier a ete examine par le secouriste du chantier mesure immediate prise zone securisee acces interdit jusqu a reparation complete du garde corps cause probable fixation insuffisante des poteaux sur la dalle vis de fixation desserrees action corrective verification immediate de tous les garde corps sur l ensemble du chantier responsable securite informe a midi rapport ecrit a transmettre au coordinateur sps avant 16h formation de rappel sur la securite en hauteur programmee pour toute l equipe demain matin aucun arret de travail necessaire les travaux peuvent reprendre des securisation de la zone je reste disponible pour tout complement d information fin de la declaration d incident

### Model: gpt-audio-mini
- Status: ✅ Success
- Latency: 5.34s
- **Word Error Rate (Meaningful): 1.84%**
- Transcript: {"text":"Déclaration d'incident, bâtiment D, niveau 4. Date, 6 novembre 2025, heure, 11h45. Un ouvrier a glissé près du bord de la dalle, pas de chute, mais situation dangereuse. Le garde-corps temporaire était mal fixé, il a bougé sous la pression. L'ouvrier concerné, M. Dupont, chef d'équipe, gros œuvres. Aucune blessure constatée, l'ouvrier a été examiné par le secouriste du chantier. Mesures immédiates prises, zone sécurisée, accès interdit jusqu'à réparation complète du garde-corps. Cause probable, fixation insuffisante des poteaux sur la dalle. Vis de fixation desserrée. Actions correctives, vérification immédiate de tous les gardes-corps sur l'ensemble du chantier. Responsable sécurité informé à midi. Rapport écrit à transmettre au coordinateur SPS avant 16h. Formation de rappel sur la sécurité en hauteur programmée pour toute l'équipe demain matin. Aucun arrêt de travail nécessaire. Les travaux peuvent reprendre dès sécurisation de la zone. Je reste disponible pour tout complément d'information. Fin de la déclaration d'incident."}
- Meaningful Errors: substitutions=3, insertions=0, deletions=0
#### Meaningful Error Details (Semantic differences only)
- Replace: expected "monsieur" | actual "m"
- Replace: expected "oeuvre" | actual "oeuvres"
- Replace: expected "desserrees" | actual "desserree"
- Raw WER (before normalization): 13.25%
- Normalized Reference: declaration d incident batiment d niveau 4 date 6 novembre 2025 heure 11h45 un ouvrier a glisse pres du bord de la dalle pas de chute mais situation dangereuse le garde corps temporaire etait mal fixe il a bouge sous la pression l ouvrier concerne monsieur dupont chef d equipe gros oeuvre aucune blessure constatee l ouvrier a ete examine par le secouriste du chantier mesures immediates prises zone securisee acces interdit jusqu a reparation complete du garde corps cause probable fixation insuffisante des poteaux sur la dalle vis de fixation desserrees actions correctives verification immediate de tous les garde corps sur l ensemble du chantier responsable securite informe a midi rapport ecrit a transmettre au coordinateur sps avant 16h formation de rappel sur la securite en hauteur programmee pour toute l equipe demain matin aucun arret de travail necessaire les travaux peuvent reprendre des securisation de la zone je reste disponible pour tout complement d information fin de la declaration d incident
- Normalized Transcript: declaration d incident batiment d niveau 4 date 6 novembre 2025 heure 11h45 un ouvrier a glisse pres du bord de la dalle pas de chute mais situation dangereuse le garde corps temporaire etait mal fixe il a bouge sous la pression l ouvrier concerne m dupont chef d equipe gros oeuvres aucune blessure constatee l ouvrier a ete examine par le secouriste du chantier mesures immediates prises zone securisee acces interdit jusqu a reparation complete du garde corps cause probable fixation insuffisante des poteaux sur la dalle vis de fixation desserree actions correctives verification immediate de tous les garde corps sur l ensemble du chantier responsable securite informe a midi rapport ecrit a transmettre au coordinateur sps avant 16h formation de rappel sur la securite en hauteur programmee pour toute l equipe demain matin aucun arret de travail necessaire les travaux peuvent reprendre des securisation de la zone je reste disponible pour tout complement d information fin de la declaration d incident

### Model: gpt-4o-transcribe
- Status: ❌ Failed
- Error: `Error code: 404 - {'error': {'code': 'DeploymentNotFound', 'message': 'The API deployment for this resource does not exist. If you created the deployment within the last 5 minutes, please wait a moment and try again.'}}`

### Model: gpt-4o-mini-transcribe
- Status: ❌ Failed
- Error: `Error code: 404 - {'error': {'code': 'DeploymentNotFound', 'message': 'The API deployment for this resource does not exist. If you created the deployment within the last 5 minutes, please wait a moment and try again.'}}`

### Model: gpt-4o-audio-preview
- Status: ✅ Success
- Latency: 3.27s
- **Word Error Rate (Meaningful): 4.29%**
- Transcript: Déclaration d’incident bâtiment D, niveau 4. Date : 6 novembre 2025. Heure : 11h45. Un ouvrier a glissé près du bord de la dalle. Pas de chute, mais situation dangereuse. Le garde-corps temporaire était mal fixé, il a bougé sous la pression. L'ouvrier concerné : M. Dupont, chef d’équipe, gros œuvre. Aucune blessure constatée, l’ouvrier a été examiné par le secouriste du chantier. Mesure immédiate prise : zone sécurisée, accès interdit jusqu’à réparation complète du garde-corps. Cause probable : fixation insuffisante des poteaux sur la dalle, vis de fixation desserrées. Action corrective : vérification immédiate de tous les gardes-corps sur l’ensemble du chantier. Responsable sécurité informé à midi. Rapport écrit à transmettre au coordonnateur SPS avant 16h. Formation de rappel sur la sécurité en hauteur programmée pour toute l’équipe demain matin. Aucun arrêt de travail nécessaire, les travaux peuvent reprendre dès sécurisation de la zone. Je reste disponible pour tout complément d’information. Fin de la déclaration d’incident.
- Meaningful Errors: substitutions=7, insertions=0, deletions=0
#### Meaningful Error Details (Semantic differences only)
- Replace: expected "monsieur" | actual "m"
- Replace: expected "mesures immediates prises" | actual "mesure immediate prise"
- Replace: expected "actions correctives" | actual "action corrective"
- Replace: expected "coordinateur" | actual "coordonnateur"
- Raw WER (before normalization): 23.18%
- Normalized Reference: declaration d incident batiment d niveau 4 date 6 novembre 2025 heure 11h45 un ouvrier a glisse pres du bord de la dalle pas de chute mais situation dangereuse le garde corps temporaire etait mal fixe il a bouge sous la pression l ouvrier concerne monsieur dupont chef d equipe gros oeuvre aucune blessure constatee l ouvrier a ete examine par le secouriste du chantier mesures immediates prises zone securisee acces interdit jusqu a reparation complete du garde corps cause probable fixation insuffisante des poteaux sur la dalle vis de fixation desserrees actions correctives verification immediate de tous les garde corps sur l ensemble du chantier responsable securite informe a midi rapport ecrit a transmettre au coordinateur sps avant 16h formation de rappel sur la securite en hauteur programmee pour toute l equipe demain matin aucun arret de travail necessaire les travaux peuvent reprendre des securisation de la zone je reste disponible pour tout complement d information fin de la declaration d incident
- Normalized Transcript: declaration d incident batiment d niveau 4 date 6 novembre 2025 heure 11h45 un ouvrier a glisse pres du bord de la dalle pas de chute mais situation dangereuse le garde corps temporaire etait mal fixe il a bouge sous la pression l ouvrier concerne m dupont chef d equipe gros oeuvre aucune blessure constatee l ouvrier a ete examine par le secouriste du chantier mesure immediate prise zone securisee acces interdit jusqu a reparation complete du garde corps cause probable fixation insuffisante des poteaux sur la dalle vis de fixation desserrees action corrective verification immediate de tous les garde corps sur l ensemble du chantier responsable securite informe a midi rapport ecrit a transmettre au coordonnateur sps avant 16h formation de rappel sur la securite en hauteur programmee pour toute l equipe demain matin aucun arret de travail necessaire les travaux peuvent reprendre des securisation de la zone je reste disponible pour tout complement d information fin de la declaration d incident

---

## audio_06_moderate_noise.wav
- Audio file: `data/mine/processed/audio_06_moderate_noise.wav`
- Reference transcript: `data/mine/processed/audio_06_reference.txt`
- Reference text: Bonjour, chef de chantier sur le site de Vinci Construction.

Aujourd'hui, le 6 novembre 2025, je fais l'inspection du bâtiment A.

Je me trouve actuellement au troisième étage, devant l'entrée principale.

J'ai remarqué 3 fissures importantes sur le mur est. Les fissures mesurent environ quinze à vingt centimètres de longueur.

L'état du béton armé semble préoccupant. Je recommande une inspection détaillée par un ingénieur structures.

Le coffrage du voile présente également des défauts. Il y a des traces d'infiltration d'eau près des banches.

Les étais sont en bon état, mais il faut vérifier la stabilité avant de poursuivre les travaux.

Je vais maintenant inspecter le quatrième étage pour vérifier l'état des dalles et des poutres.

Fin de l'inspection du bâtiment A, troisième étage.

### Model: gpt-audio
- Status: ✅ Success
- Latency: 3.34s
- **Word Error Rate (Meaningful): 3.10%**
- Transcript: Bonjour, chef de chantier sur le site de Vinci Construction. Aujourd’hui, le 6 novembre 2025, je fais l’inspection du bâtiment A. Je me trouve actuellement au troisième étage, devant l’entrée principale. J’ai remarqué trois fissures importantes sur le mur Est. Les fissures mesurent environ 15 à 20 cm de longueur. L’état du béton armé semble préoccupant. Je recommande une inspection détaillée par un ingénieur structure. Le coffrage du voile présente également des défauts, il y a des traces d’infiltration d’eau près des banches. Les étais sont en bon état, mais il faut vérifier la stabilité avant de poursuivre les travaux. Je vais maintenant inspecter le quatrième étage pour vérifier l’état des dalles et des poutres. Fin de l’inspection du bâtiment A, troisième étage.
- Meaningful Errors: substitutions=4, insertions=0, deletions=0
#### Meaningful Error Details (Semantic differences only)
- Replace: expected "aujourd'hui" | actual "aujourd hui"
- Replace: expected "centimetres" | actual "cm"
- Replace: expected "structures" | actual "structure"
- Raw WER (before normalization): 13.82%
- Normalized Reference: bonjour chef de chantier sur le site de vinci construction aujourd'hui le 6 novembre 2025 je fais l inspection du batiment a je me trouve actuellement au 3 etage devant l entree principale j ai remarque 3 fissures importantes sur le mur est les fissures mesurent environ 15 a 20 centimetres de longueur l etat du beton arme semble preoccupant je recommande une inspection detaillee par un ingenieur structures le coffrage du voile presente egalement des defauts il y a des traces dinfiltration deau pres des banches les etais sont en bon etat mais il faut verifier la stabilite avant de poursuivre les travaux je vais maintenant inspecter le 4 etage pour verifier l etat des dalles et des poutres fin de l inspection du batiment a 3 etage
- Normalized Transcript: bonjour chef de chantier sur le site de vinci construction aujourd hui le 6 novembre 2025 je fais l inspection du batiment a je me trouve actuellement au 3 etage devant l entree principale j ai remarque 3 fissures importantes sur le mur est les fissures mesurent environ 15 a 20 cm de longueur l etat du beton arme semble preoccupant je recommande une inspection detaillee par un ingenieur structure le coffrage du voile presente egalement des defauts il y a des traces dinfiltration deau pres des banches les etais sont en bon etat mais il faut verifier la stabilite avant de poursuivre les travaux je vais maintenant inspecter le 4 etage pour verifier l etat des dalles et des poutres fin de l inspection du batiment a 3 etage

### Model: gpt-audio-mini
- Status: ✅ Success
- Latency: 4.33s
- **Word Error Rate (Meaningful): 4.65%**
- Transcript: Bonjour, chef de chantier sur le site de Vinci Construction. Aujourd'hui, le 6 novembre 2025, je fais l'inspection du bâtiment A. Je me trouve actuellement au 3ème étage, devant l'entrée principale. J'ai remarqué trois fissures importantes sur le mur Est. Les fissures mesurent environ 15 à 20 cm de longueur. L'état du béton armé semble préoccupant. Je recommande une inspection détaillée par un ingénieur structure. Le coffrage du voile présente également des défauts. Il y a des traces d'infiltration d'eau près des bancs. Les étais sont en bon état, mais il faut vérifier la stabilité avant de poursuivre les travaux. Je vais maintenant inspecter le 4ème étage pour vérifier l'état des dalles et des poutres. Fin de l'inspection du bâtiment 1, 3ème étage.
- Meaningful Errors: substitutions=6, insertions=0, deletions=0
#### Meaningful Error Details (Semantic differences only)
- Replace: expected "3" | actual "trois"
- Replace: expected "quinze" | actual "15"
- Replace: expected "vingt centimetres" | actual "20 cm"
- Replace: expected "structures" | actual "structure"
- Replace: expected "a" | actual "1"
- Raw WER (before normalization): 8.94%
- Normalized Reference: bonjour chef de chantier sur le site de vinci construction aujourd'hui le 6 novembre 2025 je fais l inspection du batiment a je me trouve actuellement au troisieme etage devant l entree principale j ai remarque 3 fissures importantes sur le mur est les fissures mesurent environ quinze a vingt centimetres de longueur l etat du beton arme semble preoccupant je recommande une inspection detaillee par un ingenieur structures le coffrage du voile presente egalement des defauts il y a des traces dinfiltration deau pres des banches les etais sont en bon etat mais il faut verifier la stabilite avant de poursuivre les travaux je vais maintenant inspecter le quatrieme etage pour verifier l etat des dalles et des poutres fin de l inspection du batiment a troisieme etage
- Normalized Transcript: bonjour chef de chantier sur le site de vinci construction aujourd'hui le 6 novembre 2025 je fais l inspection du batiment a je me trouve actuellement au troisieme etage devant l entree principale j ai remarque trois fissures importantes sur le mur est les fissures mesurent environ 15 a 20 cm de longueur l etat du beton arme semble preoccupant je recommande une inspection detaillee par un ingenieur structure le coffrage du voile presente egalement des defauts il y a des traces dinfiltration deau pres des banches les etais sont en bon etat mais il faut verifier la stabilite avant de poursuivre les travaux je vais maintenant inspecter le quatrieme etage pour verifier l etat des dalles et des poutres fin de l inspection du batiment 1 troisieme etage

### Model: gpt-4o-transcribe
- Status: ❌ Failed
- Error: `Error code: 404 - {'error': {'code': 'DeploymentNotFound', 'message': 'The API deployment for this resource does not exist. If you created the deployment within the last 5 minutes, please wait a moment and try again.'}}`

### Model: gpt-4o-mini-transcribe
- Status: ❌ Failed
- Error: `Error code: 404 - {'error': {'code': 'DeploymentNotFound', 'message': 'The API deployment for this resource does not exist. If you created the deployment within the last 5 minutes, please wait a moment and try again.'}}`

### Model: gpt-4o-audio-preview
- Status: ✅ Success
- Latency: 2.89s
- **Word Error Rate (Meaningful): 1.63%**
- Transcript: Bonjour. Chef de chantier sur le site de Vinci Construction. Aujourd'hui, le 6 novembre 2025, je fais l'inspection du bâtiment A. Je me trouve actuellement au troisième étage, devant l'entrée principale. J'ai remarqué trois fissures importantes sur le mur Est. Les fissures mesurent environ 15 à 20 centimètres de longueur. L'état du béton armé est préoccupant. Je recommande une inspection détaillée par un ingénieur structure. Le coffrage du voile présente également des défauts. Il y a des traces d'infiltration d'eau près des banches. Les étais sont en bon état, mais il faut vérifier la stabilité avant de poursuivre les travaux. Je vais maintenant inspecter le quatrième étage pour vérifier l'état des dalles et des poutres. Fin de l'inspection du bâtiment A, troisième étage.
- Meaningful Errors: substitutions=2, insertions=0, deletions=0
#### Meaningful Error Details (Semantic differences only)
- Replace: expected "semble" | actual "est"
- Replace: expected "structures" | actual "structure"
- Raw WER (before normalization): 6.50%
- Normalized Reference: bonjour chef de chantier sur le site de vinci construction aujourd'hui le 6 novembre 2025 je fais linspection du batiment a je me trouve actuellement au troisieme etage devant lentre principale jai remarque 3 fissures importantes sur le mur est les fissures mesurent environ 15 a 20 centimetres de longueur letat du beton arme semble preoccupant je recommande une inspection detaillee par un ingenieur structures le coffrage du voile presente egalement des defauts il y a des traces dinfiltration deau pres des banches les etais sont en bon etat mais il faut verifier la stabilite avant de poursuivre les travaux je vais maintenant inspecter le quatrieme etage pour verifier letat des dalles et des poutres fin de linspection du batiment a troisieme etage
- Normalized Transcript: bonjour chef de chantier sur le site de vinci construction aujourd'hui le 6 novembre 2025 je fais linspection du batiment a je me trouve actuellement au troisieme etage devant lentre principale jai remarque 3 fissures importantes sur le mur est les fissures mesurent environ 15 a 20 centimetres de longueur letat du beton arme est preoccupant je recommande une inspection detaillee par un ingenieur structure le coffrage du voile presente egalement des defauts il y a des traces dinfiltration deau pres des banches les etais sont en bon etat mais il faut verifier la stabilite avant de poursuivre les travaux je vais maintenant inspecter le quatrieme etage pour verifier letat des dalles et des poutres fin de linspection du batiment a troisieme etage

---

## audio_07_heavy_noise.wav
- Audio file: `data/mine/processed/audio_07_heavy_noise.wav`
- Reference transcript: `data/mine/processed/audio_07_reference.txt`
- Reference text: Bonjour, chef de chantier sur le site de Vinci Construction.

Aujourd'hui, le 6 novembre 2025, je fais l'inspection du bâtiment A.

Je me trouve actuellement au troisième étage, devant l'entrée principale.

J'ai remarqué 3 fissures importantes sur le mur est. Les fissures mesurent environ quinze à vingt centimètres de longueur.

L'état du béton armé semble préoccupant. Je recommande une inspection détaillée par un ingénieur structures.

Le coffrage du voile présente également des défauts. Il y a des traces d'infiltration d'eau près des banches.

Les étais sont en bon état, mais il faut vérifier la stabilité avant de poursuivre les travaux.

Je vais maintenant inspecter le quatrième étage pour vérifier l'état des dalles et des poutres.

Fin de l'inspection du bâtiment A, troisième étage.

### Model: gpt-audio
- Status: ✅ Success
- Latency: 3.11s
- **Word Error Rate (Meaningful): 11.28%**
- Transcript: Bonjour, je suis chargé de chantier sur le site de Vinci Construction. Aujourd’hui, le 6 novembre 2025, j’ai fait une inspection du bâtiment A. Je me trouve actuellement au troisième étage, devant l’entrée principale. J’ai remarqué trois fissures importantes sur le mur Est, des fissures mesurant environ 15 à 20 cm de longueur. L’état du béton armé semble préoccupant, je recommande une inspection détaillée par un ingénieur structure. Le coffrage de voiles présente également des défauts, il y a des traces d’infiltration d’eau près des banches. Les étais sont en bon état mais il faut vérifier la stabilité avant de poursuivre les travaux. Je vais maintenant inspecter le quatrième étage pour vérifier l’état des dalles et des poutres. Fin d’inspection du bâtiment A, troisième étage.
- Meaningful Errors: substitutions=15, insertions=0, deletions=0
#### Meaningful Error Details (Semantic differences only)
- Replace: expected "chef" | actual "je suis charge"
- Replace: expected "je fais l" | actual "j ai fait une"
- Replace: expected "les" | actual "des"
- Replace: expected "mesurent" | actual "mesurant"
- Replace: expected "centimetres" | actual "cm"
- Replace: expected "structures" | actual "structure"
- Replace: expected "du voile" | actual "de voiles"
- Replace: expected "de l" | actual "d"
- Raw WER (before normalization): 25.20%
- Normalized Reference: bonjour chef de chantier sur le site de vinci construction aujourd hui le 6 novembre 2025 je fais l inspection du batiment a je me trouve actuellement au 3 eme etage devant l entree principale j ai remarque 3 fissures importantes sur le mur est les fissures mesurent environ 15 a 20 centimetres de longueur l etat du beton arme semble preoccupant je recommande une inspection detaillee par un ingenieur structures le coffrage du voile presente egalement des defauts il y a des traces dinfiltration deau pres des banches les etais sont en bon etat mais il faut verifier la stabilite avant de poursuivre les travaux je vais maintenant inspecter le 4 eme etage pour verifier l etat des dalles et des poutres fin de l inspection du batiment a 3 eme etage
- Normalized Transcript: bonjour je suis charge de chantier sur le site de vinci construction aujourd hui le 6 novembre 2025 j ai fait une inspection du batiment a je me trouve actuellement au 3 eme etage devant l entree principale j ai remarque 3 fissures importantes sur le mur est des fissures mesurant environ 15 a 20 cm de longueur l etat du beton arme semble preoccupant je recommande une inspection detaillee par un ingenieur structure le coffrage de voiles presente egalement des defauts il y a des traces dinfiltration deau pres des banches les etais sont en bon etat mais il faut verifier la stabilite avant de poursuivre les travaux je vais maintenant inspecter le 4 eme etage pour verifier l etat des dalles et des poutres fin d inspection du batiment a 3 eme etage

### Model: gpt-audio-mini
- Status: ✅ Success
- Latency: 4.37s
- **Word Error Rate (Meaningful): 13.01%**
- Transcript: Bonjour, je suis chef chantier sur le site de Mainzi Construction. Aujourd'hui, le 6 novembre 2025. J'ai fait une inspection du bâtiment A. Je me trouve actuellement au troisième étage, devant l'entrée principale. J'ai remarqué trois fissures importantes sur le mur Est, des fissures mesurant environ 20-15 à 20 cm de longueur. L'état du béton armé semble préoccupant. Je recommande une inspection détaillée par un ingénieur structure. Le coffrage de voil présente également des défauts. Il y a des traces d'infiltration d'eau, près des benches. Les étés sont en bon état, mais il faut vérifier la stabilité avant de poursuivre les travaux. Je vais maintenant inspecter le quatrième étage pour vérifier l'état des dalles et des poutres. Fin d'inspection du bâtiment A, au troisième étage.
- Meaningful Errors: substitutions=11, insertions=4, deletions=1
#### Meaningful Error Details (Semantic differences only)
- Insert: expected "" | actual "je suis"
- Delete: expected "de" | actual ""
- Replace: expected "vinci" | actual "mainzi"
- Replace: expected "je fais linspection" | actual "j'ai fait une inspection"
- Replace: expected "les" | actual "des"
- Replace: expected "mesurent" | actual "mesurant"
- Insert: expected "" | actual "20"
- Replace: expected "structures" | actual "structure"
- Replace: expected "du" | actual "de"
- Replace: expected "de linspection" | actual "d'inspection"
- Insert: expected "" | actual "au"
- Raw WER (before normalization): 20.33%
- Normalized Reference: bonjour chef de chantier sur le site de vinci construction aujourd'hui le 6 novembre 2025 je fais linspection du bâtiment a je me trouve actuellement au 3 étage devant l'entrée principale j'ai remarqué 3 fissures importantes sur le mur est les fissures mesurent environ 15 à 20 centimètres de longueur l'état du béton armé semble préoccupant je recommande une inspection détaillée par un ingénieur structures le coffrage du voile présente également des défauts il y a des traces dinfiltration deau près des banches les étais sont en bon état mais il faut vérifier la stabilité avant de poursuivre les travaux je vais maintenant inspecter le 4 étage pour vérifier l'état des dalles et des poutres fin de linspection du bâtiment a 3 étage
- Normalized Transcript: bonjour je suis chef chantier sur le site de mainzi construction aujourd'hui le 6 novembre 2025 j'ai fait une inspection du bâtiment a je me trouve actuellement au 3 étage devant l'entrée principale j'ai remarqué 3 fissures importantes sur le mur est des fissures mesurant environ 20 15 à 20 centimètres de longueur l'état du béton armé semble préoccupant je recommande une inspection détaillée par un ingénieur structure le coffrage de voile présente également des défauts il y a des traces dinfiltration deau près des banches les étais sont en bon état mais il faut vérifier la stabilité avant de poursuivre les travaux je vais maintenant inspecter le 4 étage pour vérifier l'état des dalles et des poutres fin d'inspection du bâtiment a au 3 étage

### Model: gpt-4o-transcribe
- Status: ❌ Failed
- Error: `Error code: 404 - {'error': {'code': 'DeploymentNotFound', 'message': 'The API deployment for this resource does not exist. If you created the deployment within the last 5 minutes, please wait a moment and try again.'}}`

### Model: gpt-4o-mini-transcribe
- Status: ❌ Failed
- Error: `Error code: 404 - {'error': {'code': 'DeploymentNotFound', 'message': 'The API deployment for this resource does not exist. If you created the deployment within the last 5 minutes, please wait a moment and try again.'}}`

### Model: gpt-4o-audio-preview
- Status: ✅ Success
- Latency: 2.84s
- **Word Error Rate (Meaningful): 9.60%**
- Transcript: Bonjour, je suis chargé de chantier sur le site de Vinci Construction. Aujourd'hui, le 6 novembre 2025, j'ai fait une inspection du bâtiment A. Je me trouve actuellement au 3ᵉ étage devant l'entrée principale. J'ai remarqué trois fissures importantes sur le mur Est, des fissures mesurent environ 15 à 20 centimètres de longueur. L'état du béton armé semble préoccupant. Je recommande une inspection détaillée par un ingénieur structure. Le coffrage des voiles présente également des défauts, il y a des traces d'infiltration d'eau près des banches. Les étais sont en bon état, mais il faut vérifier la stabilité avant de poursuivre les travaux. Je vais maintenant inspecter le 4ᵉ étage pour vérifier l'état des dalles et des poutres. Fin de l'inspection du bâtiment A, 3ᵉ étage.
- Meaningful Errors: substitutions=12, insertions=0, deletions=0
#### Meaningful Error Details (Semantic differences only)
- Replace: expected "chef" | actual "je suis charge"
- Replace: expected "je fais linspection" | actual "jai fait une inspection"
- Replace: expected "3" | actual "trois"
- Replace: expected "les" | actual "des"
- Replace: expected "structures" | actual "structure"
- Replace: expected "du voile" | actual "des voiles"
- Raw WER (before normalization): 17.07%
- Normalized Reference: bonjour chef de chantier sur le site de vinci construction aujourd'hui le 6 novembre 2025 je fais linspection du batiment a je me trouve actuellement au 3 etage devant lentre principale jai remarque 3 fissures importantes sur le mur est les fissures mesurent environ 15 a 20 centimetres de longueur l etat du beton arme semble preoccupant je recommande une inspection detaillee par un ingenieur structures le coffrage du voile presente egalement des defauts il y a des traces dinfiltration deau pres des banches les etais sont en bon etat mais il faut verifier la stabilite avant de poursuivre les travaux je vais maintenant inspecter le 4 etage pour verifier l etat des dalles et des poutres fin de linspection du batiment a 3 etage
- Normalized Transcript: bonjour je suis charge de chantier sur le site de vinci construction aujourd'hui le 6 novembre 2025 jai fait une inspection du batiment a je me trouve actuellement au 3 etage devant lentre principale jai remarque trois fissures importantes sur le mur est des fissures mesurent environ 15 a 20 centimetres de longueur l etat du beton arme semble preoccupant je recommande une inspection detaillee par un ingenieur structure le coffrage des voiles presente egalement des defauts il y a des traces dinfiltration deau pres des banches les etais sont en bon etat mais il faut verifier la stabilite avant de poursuivre les travaux je vais maintenant inspecter le 4 etage pour verifier l etat des dalles et des poutres fin de linspection du batiment a 3 etage

---

## audio_10_long.wav
- Audio file: `data/mine/processed/audio_10_long.wav`
- Reference transcript: `data/mine/processed/audio_10_reference.txt`
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
- Latency: 12.41s
- **Word Error Rate (Meaningful): 5.03%**
- Transcript: Rapport de la fin de journée, mercredi 6 novembre 2025.

Bonjour, je suis chef de chantier. Voici le compte-rendu complet de la journée sur le chantier de Vinci Construction, projet résidentiel Les Jardins de l’Ouest.

Partie 1 : Avancement des travaux. Ce matin, nous avons terminé le coulage de la dalle du troisième étage du bâtiment A. Le volume du béton coulé est de 75 mètres cubes. La coulée a commencé à 7h30 et s’est terminée à 11h15. L’équipe de maçonnerie a monté trois mètres linéaires de voile au quatrième étage. Le ferraillage a préparé et intégré sans problème la géométrie, et conforme au plan. Les électriciens ont achevé le passage des gaines dans les refends du deuxième étage. Reste à faire le câblage prévu pour la semaine prochaine. La plomberie du premier étage est terminée à 90%. Les raccordements aux colonnes montantes sont faits, il reste les finitions dans les salles de bain.

Partie 2 : Livraisons et approvisionnement. Nous avons reçu ce matin la livraison de 15 palettes de parpaings pour le bâtiment B. La qualité est conforme, stockage organisé à proximité de la zone de travail. La livraison des menuiseries extérieures prévue aujourd’hui est reportée à vendredi, le fournisseur ayant un problème logistique. Impact mineur sur le planning général. Les banches métalliques louées dans le bâtiment C sont arrivées hier soir. L’équipe coffreur commence le montage demain matin.

Partie 3 : Effectif et ressources. 15 ouvriers présents aujourd’hui, 3 absents : 1 pour congé maladie, 2 pour formation sécurité obligatoire. La grue à tour numéro 2 a été réparée, elle est de nouveau opérationnelle depuis 14h. Le nouveau chef d’équipe, Monsieur Martin, a pris ses fonctions ce matin. Intégration en cours, il sera autonome d’ici deux semaines.

Partie 4 : Sécurité et qualité. Aucun accident aujourd’hui, le taux d’incident reste à zéro depuis 15 jours. Visite surprise de l’inspecteur du travail à 10h, tout était conforme, aucune remarque ni observation, très satisfaisant. Le contrôle qualité du béton : trois éprouvettes prélevées ce matin lors de la coulée, résultats attendus dans 28 jours. Petit incident : un ouvrier a oublié son harnais de sécurité, appel à l’ordre immédiat, formation de sensibilisation prévue vendredi pour toute l’équipe.

Partie 5 : Points de vigilance. Météo : prévision de pluie pour demain après-midi, prévoir bâches de protection pour les zones en cours de bétonnage. Le planning est serré sur le bâtiment A, il faut terminer le gros œuvre avant la fin du mois : nous sommes dans les temps mais aucune marge de manœuvre. Problème de coordination avec les façadiers, réunion prévue demain matin à 8h pour ajuster les interfaces.

Partie 6 : Actions pour demain. Continuer le montage des voiles au quatrième étage du bâtiment A. Démarrage du coffrage des poteaux du rez-de-chaussée du bâtiment B. Organiser le coulé du radier du bâtiment C si la météo le permet. Réceptionner et contrôler la livraison de 50 tonnes d’armatures, prévue à 9h. Réunion de coordination à 8h avec tous les sous-traitants.

Conclusion : Bonne journée dans l’ensemble, avancement conforme au planning, aucun retard significatif, tous les indicateurs sont au vert. Prochain rapport demain soir à la même heure. Bonne soirée à tous. Fin du rapport de fin de journée.
- Meaningful Errors: substitutions=26, insertions=2, deletions=0
#### Meaningful Error Details (Semantic differences only)
- Insert: expected "" | actual "la"
- Replace: expected "un" | actual "1"
- Replace: expected "de" | actual "du"
- Insert: expected "" | actual "a"
- Replace: expected "hier a été" | actual "et"
- Replace: expected "est" | actual "et"
- Replace: expected "aux plans" | actual "au plan"
- Replace: expected "bains" | actual "bain"
- Replace: expected "deux" | actual "2"
- Replace: expected "approvisionnements" | actual "approvisionnement"
- Replace: expected "a" | actual "ayant"
- Replace: expected "pour" | actual "dans"
- Replace: expected "trois effectifs" | actual "3 effectif"
- Replace: expected "un" | actual "1"
- Replace: expected "deux" | actual "2"
- Replace: expected "quatre" | actual "4"
- Replace: expected "rappel" | actual "appel"
- Replace: expected "cinq" | actual "5"
- Replace: expected "prévisions" | actual "prévision"
- Replace: expected "six" | actual "6"
- Replace: expected "démarrer le" | actual "démarrage du"
- Replace: expected "la coulée" | actual "le coulé"
- Raw WER (before normalization): 28.20%
- Normalized Reference: rapport de fin de journée mercredi 6 novembre 2025 bonjour je suis chef de chantier voici le compte rendu complet de la journée sur le chantier de vinci construction projet résidentiel les jardins de l ouest partie un avancement des travaux ce matin nous avons terminé le coulage de la dalle du troisième étage du bâtiment a le volume de béton coulé est de 75 mètres cubes la coulée a commencé à 7 heures 30 et s est terminée à 11 heures 15 l équipe de maçonnerie a monté 3 mètres linéaires de voiles au quatrième étage le ferraillage préparé hier a été intégré sans problème la géométrie est conforme aux plans les électriciens ont achevé le passage des gaines dans les refends du deuxième étage reste à faire le câblage prévu pour la semaine prochaine la plomberie du premier étage est terminée à 90 pour cent les raccordements aux colonnes montantes sont faits il reste les finitions dans les salles de bains partie deux livraisons et approvisionnements nous avons reçu ce matin la livraison de 15 palettes de parpaings pour le bâtiment b la qualité est conforme stockage organisé à proximité de la zone de travail la livraison des menuiseries extérieures prévue aujourd hui est reportée à vendredi le fournisseur a un problème logistique impact mineur sur le planning général les banches métalliques louées pour le bâtiment c sont arrivées hier soir l équipe coffreur commence le montage demain matin partie trois effectifs et ressources 15 ouvriers présents aujourd hui 3 absents un pour congé maladie deux pour formation sécurité obligatoire la grue à tour numéro 2 a été réparée elle est de nouveau opérationnelle depuis 14 heures le nouveau chef d équipe monsieur martin a pris ses fonctions ce matin intégration en cours il sera autonome d ici deux semaines partie quatre sécurité et qualité aucun accident aujourd hui le taux d incidents reste à zéro depuis 15 jours visite surprise de l inspecteur du travail à 10 heures tout était conforme aucune remarque ni observation très satisfaisant le contrôle qualité du béton trois éprouvettes prélevées ce matin lors de la coulée résultats attendus dans 28 jours petit incident un ouvrier a oublié son harnais de sécurité rappel à l ordre immédiat formation de sensibilisation prévue vendredi pour toute l équipe partie cinq points de vigilance météo prévisions de pluie pour demain après midi prévoir bâches de protection pour les zones en cours de bétonnage le planning est serré sur le bâtiment a il faut terminer le gros œuvre avant la fin du mois nous sommes dans les temps mais aucune marge de manœuvre problème de coordination avec les façadiers réunion prévue demain matin à 8 heures pour ajuster les interfaces partie six actions pour demain continuer le montage des voiles au quatrième étage du bâtiment a démarrer le coffrage des poteaux du rez de chaussée du bâtiment b organiser la coulée du radier du bâtiment c si la météo le permet réceptionner et contrôler la livraison de 50 tonnes d armatures prévue à 9 heures réunion de coordination à 8 heures avec tous les sous traitants conclusion bonne journée dans l ensemble avancement conforme au planning aucun retard significatif tous les indicateurs sont au vert prochain rapport demain soir à la même heure bonne soirée à tous fin du rapport de fin de journée
- Normalized Transcript: rapport de la fin de journée mercredi 6 novembre 2025 bonjour je suis chef de chantier voici le compte rendu complet de la journée sur le chantier de vinci construction projet résidentiel les jardins de l ouest partie 1 avancement des travaux ce matin nous avons terminé le coulage de la dalle du troisième étage du bâtiment a le volume du béton coulé est de 75 mètres cubes la coulée a commencé à 7 heures 30 et s est terminée à 11 heures 15 l équipe de maçonnerie a monté 3 mètres linéaires de voiles au quatrième étage le ferraillage a préparé et intégré sans problème la géométrie et conforme au plan les électriciens ont achevé le passage des gaines dans les refends du deuxième étage reste à faire le câblage prévu pour la semaine prochaine la plomberie du premier étage est terminée à 90 pour cent les raccordements aux colonnes montantes sont faits il reste les finitions dans les salles de bain partie 2 livraisons et approvisionnement nous avons reçu ce matin la livraison de 15 palettes de parpaings pour le bâtiment b la qualité est conforme stockage organisé à proximité de la zone de travail la livraison des menuiseries extérieures prévue aujourd hui est reportée à vendredi le fournisseur ayant un problème logistique impact mineur sur le planning général les banches métalliques louées dans le bâtiment c sont arrivées hier soir l équipe coffreur commence le montage demain matin partie 3 effectif et ressources 15 ouvriers présents aujourd hui 3 absents 1 pour congé maladie 2 pour formation sécurité obligatoire la grue à tour numéro 2 a été réparée elle est de nouveau opérationnelle depuis 14 heures le nouveau chef d équipe monsieur martin a pris ses fonctions ce matin intégration en cours il sera autonome d ici deux semaines partie 4 sécurité et qualité aucun accident aujourd hui le taux d incidents reste à zéro depuis 15 jours visite surprise de l inspecteur du travail à 10 heures tout était conforme aucune remarque ni observation très satisfaisant le contrôle qualité du béton trois éprouvettes prélevées ce matin lors de la coulée résultats attendus dans 28 jours petit incident un ouvrier a oublié son harnais de sécurité appel à l ordre immédiat formation de sensibilisation prévue vendredi pour toute l équipe partie 5 points de vigilance météo prévision de pluie pour demain après midi prévoir bâches de protection pour les zones en cours de bétonnage le planning est serré sur le bâtiment a il faut terminer le gros œuvre avant la fin du mois nous sommes dans les temps mais aucune marge de manœuvre problème de coordination avec les façadiers réunion prévue demain matin à 8 heures pour ajuster les interfaces partie 6 actions pour demain continuer le montage des voiles au quatrième étage du bâtiment a démarrage du coffrage des poteaux du rez de chaussée du bâtiment b organiser le coulé du radier du bâtiment c si la météo le permet réceptionner et contrôler la livraison de 50 tonnes d armatures prévue à 9 heures réunion de coordination à 8 heures avec tous les sous traitants conclusion bonne journée dans l ensemble avancement conforme au planning aucun retard significatif tous les indicateurs sont au vert prochain rapport demain soir à la même heure bonne soirée à tous fin du rapport de fin de journée

### Model: gpt-audio-mini
- Status: ✅ Success
- Latency: 10.00s
- **Word Error Rate (Meaningful): 5.13%**
- Transcript: Rapport de la fin de journée, mercredi 6 novembre 2025.

Bonjour, je suis chef de chantier. Voici le compte-rendu complet de la journée sur le chantier de Vinci Construction, projet résidentiel Les Jardins de l'Ouest.

Partie 1 – Avancement des travaux
Ce matin, nous avons terminé le coulage de la dalle du troisième étage du bâtiment A. Le volume du béton coulé est de 75 m³. La coulée a commencé à 7h30 et s'est terminée à 11h15.

L'équipe de maçonnerie a monté 3 mètres linéaires de voile au quatrième étage. Le ferraillage préparé hier a été intégré sans problème, la géométrie est conforme au plan.

Les électriciens ont achevé le passage des gaines dans les refends du deuxième étage. Reste à faire le câblage, prévu pour la semaine prochaine.

La plomberie du premier étage est terminée à 90 %. Les raccordements aux colonnes montantes sont faits, il reste les finitions dans les salles de bain.

Partie 2 – Livraison et approvisionnement
Nous avons reçu ce matin la livraison de 15 palettes de parpaings pour le bâtiment B. La qualité est conforme, stockage organisé à proximité de la zone de travail.

La livraison des menuiseries extérieures, prévue aujourd'hui, est reportée à vendredi. Le fournisseur a un problème logistique. Impact mineur sur le planning général.

Les banches métalliques louées dans le bâtiment C sont arrivées hier soir. L'équipe coffreur commence le montage demain matin.

Partie 3 – Effectifs et ressources
15 ouvriers présents aujourd'hui, 3 absents : 1 pour congé maladie, 2 pour formation sécurité obligatoire.

La grue, à tour numéro 2, a été réparée et est de nouveau opérationnelle depuis 14h.

Le nouveau chef d'équipe, M. Martin, a pris ses fonctions ce matin. Intégration en cours, il sera autonome d'ici deux semaines.

Partie 4 – Sécurité et qualité
Aucun accident aujourd'hui. Le taux d'incidents reste à zéro depuis 15 jours. Visite surprise de l'inspecteur de travail à 10h, tout était conforme. Aucune remarque ni observation, très satisfaisant.

Le contrôle qualité du béton : 3 éprouvettes prélevées ce matin lors de la coulée. Résultat attendu dans 28 jours.

Petit incident : un ouvrier a oublié son harnais de sécurité. Appel à l'ordre immédiat. Formation de sensibilisation prévue vendredi pour toute l'équipe.

Partie 5 – Point de vigilance
Météo : prévision de pluie pour demain après-midi. Prévoir bâches de protection pour les zones en cours de bétonnage.

Le planning est serré sur le bâtiment A, il faut terminer le gros œuvre avant la fin du mois. Nous sommes dans les temps, mais aucun marge de manœuvre.

Problème de coordination avec les façadiers. Réunion prévue demain matin à 8h pour ajuster les interfaces.

Partie 6 – Actions pour demain
Continuer le montage des voiles au quatrième étage du bâtiment A. Démarrage du coffrage des poteaux du rez-de-chaussée du bâtiment B. Organiser le coulé du radier du bâtiment C si la météo le permet.

Réceptionner et contrôler la livraison de 50 tonnes d'armature, prévue à 9h. Réunion de coordination à 8h avec tous les sous-traitants.

Conclusion
Bonne journée dans l'ensemble. Avancements conformes au planning, aucun retard significatif. Tous les indicateurs sont au vert.

Prochain rapport demain soir à la même heure.

Bonne soirée à tous. Fin du rapport de fin de journée.
- Meaningful Errors: substitutions=27, insertions=1, deletions=0
#### Meaningful Error Details (Semantic differences only)
- Insert: expected "" | actual "la"
- Replace: expected "un" | actual "1"
- Replace: expected "de" | actual "du"
- Replace: expected "aux plans" | actual "au plan"
- Replace: expected "bains" | actual "bain"
- Replace: expected "deux livraisons" | actual "2 livraison"
- Replace: expected "approvisionnements" | actual "approvisionnement"
- Replace: expected "pour" | actual "dans"
- Replace: expected "trois" | actual "3"
- Replace: expected "elle" | actual "et"
- Replace: expected "quatre" | actual "4"
- Replace: expected "résultats attendus" | actual "résultat attendu"
- Replace: expected "rappel" | actual "appel"
- Replace: expected "cinq points" | actual "5 point"
- Replace: expected "prévisions" | actual "prévision"
- Replace: expected "aucune" | actual "aucun"
- Replace: expected "six" | actual "6"
- Replace: expected "démarrer le" | actual "démarrage du"
- Replace: expected "la coulée" | actual "le coulé"
- Replace: expected "armatures" | actual "armature"
- Replace: expected "avancement conforme" | actual "avancements conformes"
- Raw WER (before normalization): 22.63%
- Normalized Reference: rapport de fin de journée mercredi 6 novembre 2025 bonjour je suis chef de chantier voici le compte rendu complet de la journée sur le chantier de vinci construction projet résidentiel les jardins de l ouest partie un avancement des travaux ce matin nous avons terminé le coulage de la dalle du 3ème étage du bâtiment a le volume de béton coulé est de 75 mètres cubes la coulée a commencé à 7h30 et s est terminée à 11h15 l équipe de maçonnerie a monté 3 mètres linéaires de voiles au 4ème étage le ferraillage préparé hier a été intégré sans problème la géométrie est conforme aux plans les électriciens ont achevé le passage des gaines dans les refends du 2ème étage reste à faire le câblage prévu pour la semaine prochaine la plomberie du 1er étage est terminée à 90 les raccordements aux colonnes montantes sont faits il reste les finitions dans les salles de bains partie deux livraisons et approvisionnements nous avons reçu ce matin la livraison de 15 palettes de parpaings pour le bâtiment b la qualité est conforme stockage organisé à proximité de la zone de travail la livraison des menuiseries extérieures prévue aujourd hui est reportée à vendredi le fournisseur a un problème logistique impact mineur sur le planning général les banches métalliques louées pour le bâtiment c sont arrivées hier soir l équipe coffreur commence le montage demain matin partie trois effectifs et ressources 15 ouvriers présents aujourd hui 3 absents un pour congé maladie deux pour formation sécurité obligatoire la grue à tour numéro 2 a été réparée elle est de nouveau opérationnelle depuis 14h le nouveau chef d équipe monsieur martin a pris ses fonctions ce matin intégration en cours il sera autonome d ici deux semaines partie quatre sécurité et qualité aucun accident aujourd hui le taux d incidents reste à zéro depuis 15 jours visite surprise de l inspecteur du travail à 10h tout était conforme aucune remarque ni observation très satisfaisant le contrôle qualité du béton 3 éprouvettes prélevées ce matin lors de la coulée résultats attendus dans 28 jours petit incident un ouvrier a oublié son harnais de sécurité rappel à l ordre immédiat formation de sensibilisation prévue vendredi pour toute l équipe partie cinq points de vigilance météo prévisions de pluie pour demain après midi prévoir bâches de protection pour les zones en cours de bétonnage le planning est serré sur le bâtiment a il faut terminer le gros œuvre avant la fin du mois nous sommes dans les temps mais aucune marge de manœuvre problème de coordination avec les façadiers réunion prévue demain matin à 8h pour ajuster les interfaces partie six actions pour demain continuer le montage des voiles au 4ème étage du bâtiment a démarrer le coffrage des poteaux du rez de chaussée du bâtiment b organiser la coulée du radier du bâtiment c si la météo le permet réceptionner et contrôler la livraison de 50 tonnes d armatures prévue à 9h réunion de coordination à 8h avec tous les sous traitants conclusion bonne journée dans l ensemble avancement conforme au planning aucun retard significatif tous les indicateurs sont au vert prochain rapport demain soir à la même heure bonne soirée à tous fin du rapport de fin de journée
- Normalized Transcript: rapport de la fin de journée mercredi 6 novembre 2025 bonjour je suis chef de chantier voici le compte rendu complet de la journée sur le chantier de vinci construction projet résidentiel les jardins de l ouest partie 1 avancement des travaux ce matin nous avons terminé le coulage de la dalle du 3ème étage du bâtiment a le volume du béton coulé est de 75 mètres cubes la coulée a commencé à 7h30 et s est terminée à 11h15 l équipe de maçonnerie a monté 3 mètres linéaires de voiles au 4ème étage le ferraillage préparé hier a été intégré sans problème la géométrie est conforme au plan les électriciens ont achevé le passage des gaines dans les refends du 2ème étage reste à faire le câblage prévu pour la semaine prochaine la plomberie du 1er étage est terminée à 90 les raccordements aux colonnes montantes sont faits il reste les finitions dans les salles de bain partie 2 livraison et approvisionnement nous avons reçu ce matin la livraison de 15 palettes de parpaings pour le bâtiment b la qualité est conforme stockage organisé à proximité de la zone de travail la livraison des menuiseries extérieures prévue aujourd hui est reportée à vendredi le fournisseur a un problème logistique impact mineur sur le planning général les banches métalliques louées dans le bâtiment c sont arrivées hier soir l équipe coffreur commence le montage demain matin partie 3 effectifs et ressources 15 ouvriers présents aujourd hui 3 absents un pour congé maladie deux pour formation sécurité obligatoire la grue à tour numéro 2 a été réparée et est de nouveau opérationnelle depuis 14h le nouveau chef d équipe monsieur martin a pris ses fonctions ce matin intégration en cours il sera autonome d ici deux semaines partie 4 sécurité et qualité aucun accident aujourd hui le taux d incidents reste à zéro depuis 15 jours visite surprise de l inspecteur du travail à 10h tout était conforme aucune remarque ni observation très satisfaisant le contrôle qualité du béton 3 éprouvettes prélevées ce matin lors de la coulée résultat attendu dans 28 jours petit incident un ouvrier a oublié son harnais de sécurité appel à l ordre immédiat formation de sensibilisation prévue vendredi pour toute l équipe partie 5 point de vigilance météo prévision de pluie pour demain après midi prévoir bâches de protection pour les zones en cours de bétonnage le planning est serré sur le bâtiment a il faut terminer le gros œuvre avant la fin du mois nous sommes dans les temps mais aucun marge de manœuvre problème de coordination avec les façadiers réunion prévue demain matin à 8h pour ajuster les interfaces partie 6 actions pour demain continuer le montage des voiles au 4ème étage du bâtiment a démarrage du coffrage des poteaux du rez de chaussée du bâtiment b organiser le coulé du radier du bâtiment c si la météo le permet réceptionner et contrôler la livraison de 50 tonnes d armature prévue à 9h réunion de coordination à 8h avec tous les sous traitants conclusion bonne journée dans l ensemble avancements conformes au planning aucun retard significatif tous les indicateurs sont au vert prochain rapport demain soir à la même heure bonne soirée à tous fin du rapport de fin de journée

### Model: gpt-4o-transcribe
- Status: ❌ Failed
- Error: `Error code: 404 - {'error': {'code': 'DeploymentNotFound', 'message': 'The API deployment for this resource does not exist. If you created the deployment within the last 5 minutes, please wait a moment and try again.'}}`

### Model: gpt-4o-mini-transcribe
- Status: ❌ Failed
- Error: `Error code: 404 - {'error': {'code': 'DeploymentNotFound', 'message': 'The API deployment for this resource does not exist. If you created the deployment within the last 5 minutes, please wait a moment and try again.'}}`

### Model: gpt-4o-audio-preview
- Status: ✅ Success
- Latency: 9.84s
- **Word Error Rate (Meaningful): 3.30%**
- Transcript: Rapport de la fin de journée, mercredi 6 novembre 2025. Bonjour, je suis chef de chantier, voici le compte rendu complet de la journée sur le chantier de Vinci Construction, projet résidentiel Les Jardins de l'Ouest. Partie 1 : Avancement des travaux. Ce matin, nous avons terminé le coulage de la dalle du troisième étage du bâtiment A. Le volume de béton coulé est de 75 mètres cubes. La coulée a commencé à 7h30 et s'est terminée à 11h15. L'équipe de maçonnerie a monté 3 mètres linéaires de voile au quatrième étage. Le ferraillage a intégré sans problème, la géométrie est conforme au plan. Les électriciens ont achevé le passage des gaines dans les refends du deuxième étage, reste à faire le câblage prévu pour la semaine prochaine. La plomberie du premier étage est terminée à 90%, les raccordements aux colonnes montantes sont faits, il reste les finitions dans les salles de bain. Partie 2 : Livraison et approvisionnement. Nous avons reçu ce matin la livraison de 15 palettes de parpaings pour le bâtiment B, la qualité est conforme, stockage organisé à proximité de la zone de travail. La livraison des menuiseries extérieures prévue aujourd'hui est reportée à vendredi, le fournisseur étant a un problème logistique, impact mineur sur le planning général. Les banches métalliques louées pour le bâtiment C sont arrivées hier soir, l'équipe coffreur commence le montage demain matin. Partie 3 : Effectif et ressources. 15 ouvriers présents aujourd’hui, 3 absents, un pour congé maladie, 2 pour formation sécurité obligatoire. La grue à tour numéro 2 a été réparée et est de nouveau opérationnelle depuis 14h. Le nouveau chef d’équipe, Monsieur Martin, a pris ses fonctions ce matin, intégration en cours, il sera autonome d’ici deux semaines. Partie 4 : Sécurité et qualité. Aucun accident aujourd'hui, le taux d'incident reste à zéro depuis 15 jours. Visite surprise de l'inspecteur du travail à 10h, tout était conforme, aucune remarque ni observation, très satisfaisant. Le contrôle qualité du béton : 3 éprouvettes prélevées ce matin lors de la coulée, résultats attendus dans 28 jours. Petit incident : un ouvrier a oublié son harnais de sécurité, appel à l'ordre immédiat, formation de sensibilisation prévue vendredi pour toute l’équipe. Partie 5 : Points de vigilance. Météo : prévision de pluie pour demain après-midi, prévoir bâches de protection pour les zones en cours de bétonnage. Le planning est serré sur le bâtiment A, il faut terminer le gros œuvre avant la fin du mois, nous sommes dans les temps mais aucune marge de manœuvre. Problème de coordination avec les façadiers, réunion prévue demain matin à 8h pour ajuster les interfaces. Partie 6 : Actions pour demain. Continuer le montage des voiles au quatrième étage du bâtiment A. Démarrage du coffrage des poteaux du rez-de-chaussée du bâtiment B. Organiser le coulé du radier du bâtiment C, si la météo le permet. Réceptionner et contrôler la livraison de 50 tonnes d’armature prévue à 9h. Réunion de coordination à 8h avec tous les sous-traitants. Conclusion : Bonne journée dans l'ensemble, avancement conforme au planning, aucun retard significatif, tous les indicateurs sont au vert. Prochain rapport demain soir, à la même heure. Bonne soirée à tous. Fin du rapport de fin de journée.
- Meaningful Errors: substitutions=15, insertions=1, deletions=2
#### Meaningful Error Details (Semantic differences only)
- Insert: expected "" | actual "la"
- Replace: expected "un" | actual "1"
- Delete: expected "préparé hier" | actual ""
- Replace: expected "aux plans" | actual "au plan"
- Replace: expected "bains" | actual "bain"
- Replace: expected "deux livraisons" | actual "2 livraison"
- Replace: expected "approvisionnements" | actual "approvisionnement"
- Replace: expected "trois effectifs" | actual "3 effectif"
- Replace: expected "elle" | actual "et"
- Replace: expected "quatre" | actual "4"
- Replace: expected "rappel" | actual "appel"
- Replace: expected "cinq" | actual "5"
- Replace: expected "prévisions" | actual "prévision"
- Replace: expected "six" | actual "6"
- Raw WER (before normalization): 28.57%
- Normalized Reference: rapport de fin de journée mercredi 6 novembre 2025 bonjour je suis chef de chantier voici le compte rendu complet de la journée sur le chantier de vinci construction projet résidentiel les jardins de l ouest partie un avancement des travaux ce matin nous avons terminé le coulage de la dalle du 3ème étage du bâtiment a le volume de béton coulé est de 75 mètres cubes la coulée a commencé à 7h30 et s est terminée à 11h15 l équipe de maçonnerie a monté 3 mètres linéaires de voiles au 4ème étage le ferraillage préparé hier a été intégré sans problème la géométrie est conforme aux plans les électriciens ont achevé le passage des gaines dans les refends du 2ème étage reste à faire le câblage prévu pour la semaine prochaine la plomberie du 1er étage est terminée à 90% les raccordements aux colonnes montantes sont faits il reste les finitions dans les salles de bains partie deux livraisons et approvisionnements nous avons reçu ce matin la livraison de 15 palettes de parpaings pour le bâtiment b la qualité est conforme stockage organisé à proximité de la zone de travail la livraison des menuiseries extérieures prévue aujourd hui est reportée à vendredi le fournisseur a un problème logistique impact mineur sur le planning général les banches métalliques louées pour le bâtiment c sont arrivées hier soir l équipe coffreur commence le montage demain matin partie trois effectifs et ressources 15 ouvriers présents aujourd hui 3 absents un pour congé maladie deux pour formation sécurité obligatoire la grue à tour numéro 2 a été réparée elle est de nouveau opérationnelle depuis 14h le nouveau chef d équipe monsieur martin a pris ses fonctions ce matin intégration en cours il sera autonome d ici deux semaines partie quatre sécurité et qualité aucun accident aujourd hui le taux d incidents reste à zéro depuis 15 jours visite surprise de l inspecteur du travail à 10h tout était conforme aucune remarque ni observation très satisfaisant le contrôle qualité du béton 3 éprouvettes prélevées ce matin lors de la coulée résultats attendus dans 28 jours petit incident un ouvrier a oublié son harnais de sécurité rappel à l ordre immédiat formation de sensibilisation prévue vendredi pour toute l équipe partie cinq points de vigilance météo prévisions de pluie pour demain après midi prévoir bâches de protection pour les zones en cours de bétonnage le planning est serré sur le bâtiment a il faut terminer le gros œuvre avant la fin du mois nous sommes dans les temps mais aucune marge de manœuvre problème de coordination avec les façadiers réunion prévue demain matin à 8h pour ajuster les interfaces partie six actions pour demain continuer le montage des voiles au 4ème étage du bâtiment a démarrer le coffrage des poteaux du rez de chaussée du bâtiment b organiser la coulée du radier du bâtiment c si la météo le permet réceptionner et contrôler la livraison de 50 tonnes d armatures prévue à 9h réunion de coordination à 8h avec tous les sous traitants conclusion bonne journée dans l ensemble avancement conforme au planning aucun retard significatif tous les indicateurs sont au vert prochain rapport demain soir à la même heure bonne soirée à tous fin du rapport de fin de journée
- Normalized Transcript: rapport de la fin de journée mercredi 6 novembre 2025 bonjour je suis chef de chantier voici le compte rendu complet de la journée sur le chantier de vinci construction projet résidentiel les jardins de l ouest partie 1 avancement des travaux ce matin nous avons terminé le coulage de la dalle du 3ème étage du bâtiment a le volume de béton coulé est de 75 mètres cubes la coulée a commencé à 7h30 et s est terminée à 11h15 l équipe de maçonnerie a monté 3 mètres linéaires de voiles au 4ème étage le ferraillage a été intégré sans problème la géométrie est conforme au plan les électriciens ont achevé le passage des gaines dans les refends du 2ème étage reste à faire le câblage prévu pour la semaine prochaine la plomberie du 1er étage est terminée à 90% les raccordements aux colonnes montantes sont faits il reste les finitions dans les salles de bain partie 2 livraison et approvisionnement nous avons reçu ce matin la livraison de 15 palettes de parpaings pour le bâtiment b la qualité est conforme stockage organisé à proximité de la zone de travail la livraison des menuiseries extérieures prévue aujourd hui est reportée à vendredi le fournisseur a un problème logistique impact mineur sur le planning général les banches métalliques louées pour le bâtiment c sont arrivées hier soir l équipe coffreur commence le montage demain matin partie 3 effectif et ressources 15 ouvriers présents aujourd hui 3 absents un pour congé maladie deux pour formation sécurité obligatoire la grue à tour numéro 2 a été réparée et est de nouveau opérationnelle depuis 14h le nouveau chef d équipe monsieur martin a pris ses fonctions ce matin intégration en cours il sera autonome d ici deux semaines partie 4 sécurité et qualité aucun accident aujourd hui le taux d incidents reste à zéro depuis 15 jours visite surprise de l inspecteur du travail à 10h tout était conforme aucune remarque ni observation très satisfaisant le contrôle qualité du béton 3 éprouvettes prélevées ce matin lors de la coulée résultats attendus dans 28 jours petit incident un ouvrier a oublié son harnais de sécurité appel à l ordre immédiat formation de sensibilisation prévue vendredi pour toute l équipe partie 5 points de vigilance météo prévision de pluie pour demain après midi prévoir bâches de protection pour les zones en cours de bétonnage le planning est serré sur le bâtiment a il faut terminer le gros œuvre avant la fin du mois nous sommes dans les temps mais aucune marge de manœuvre problème de coordination avec les façadiers réunion prévue demain matin à 8h pour ajuster les interfaces partie 6 actions pour demain continuer le montage des voiles au 4ème étage du bâtiment a démarrer le coffrage des poteaux du rez de chaussée du bâtiment b organiser la coulée du radier du bâtiment c si la météo le permet réceptionner et contrôler la livraison de 50 tonnes d armatures prévue à 9h réunion de coordination à 8h avec tous les sous traitants conclusion bonne journée dans l ensemble avancement conforme au planning aucun retard significatif tous les indicateurs sont au vert prochain rapport demain soir à la même heure bonne soirée à tous fin du rapport de fin de journée

---
