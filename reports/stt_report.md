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

### Model: whisper
- Status: ✅ Success
- Latency: 2.34s
- Word Error Rate: 99.21%
- Transcript: Hello, I am a construction manager on the site of 26 Construction. Today, November 6, 2025, I am inspecting building A. I am currently on the third floor in front of the main entrance. I noticed three major cracks on the east wall. The cracks are about 15 to 20 centimeters long. The state of the reinforced concrete seems worrisome. I recommend a detailed inspection by a structural engineer. The casting of the sail also presents defects. There are traces of water infiltration near the banks. The STs are in good condition, but it is necessary to check the stability before continuing the work. It is now necessary to inspect the fourth floor to check the condition of the slabs and beams. End of inspection of building A, third floor.
- Errors: substitutions=141, insertions=0, deletions=0
#### Error Details
- Replace: expected "Bonjour, je suis chef de chantier sur le" | actual "Hello, I am a construction manager on the"
- Replace: expected "de Vinci" | actual "of 26"
- Replace: expected "Aujourd'hui, le six novembre deux mille vingt-cinq, je fais l'inspection du bâtiment" | actual "Today, November 6, 2025, I am inspecting building"
- Replace: expected "Je me trouve actuellement au troisième étage, devant l'entrée principale. J'ai remarqué trois fissures importantes sur le mur est. Les fissures mesurent environ quinze à vingt centimètres de longueur. L'état du béton armé semble préoccupant. Je recommande une" | actual "I am currently on the third floor in front of the main entrance. I noticed three major cracks on the east wall. The cracks are about 15 to 20 centimeters long. The state of the reinforced concrete seems worrisome. I recommend a detailed"
- Replace: expected "détaillée par un ingénieur structures. Le coffrage du voile présente également des défauts. Il y" | actual "by"
- Replace: expected "des" | actual "structural engineer. The casting of the sail also presents defects. There are"
- Replace: expected "d'infiltration d'eau près des banches. Les étais sont en bon état, mais il faut vérifier la stabilité avant de poursuivre les travaux. Je vais maintenant inspecter le quatrième étage pour vérifier l'état des dalles et des poutres. Fin de l'inspection du bâtiment" | actual "of water infiltration near the banks. The STs are in good condition, but it is necessary to check the stability before continuing the work. It is now necessary to inspect the fourth floor to check the condition of the slabs and beams. End of inspection of building"
- Replace: expected "troisième étage." | actual "third floor."

### Model: gpt-audio
- Status: ✅ Success
- Latency: 3.32s
- Word Error Rate: 18.11%
- Transcript: Bonjour, je suis chef de chantier sur le site de Vinci Construction. Aujourd’hui, le 6 novembre 2025, je fais l’inspection du bâtiment A. Je me trouve actuellement au troisième étage devant l’entrée principale. J’ai remarqué trois fissures importantes sur le mur Est. Les fissures mesurent environ 15 à 20 centimètres de longueur. L’état du béton armé semble préoccupant. Je recommande une inspection détaillée par un ingénieur structure. Le coffrage du voile présente également des défauts et il y a des traces d’infiltration d’eau près des banches. Les étais sont en bon état, mais il faut vérifier la stabilité avant de poursuivre les travaux. Il faut maintenant inspecter le quatrième étage pour vérifier l’état des dalles et des poutres. Fin de l’inspection du bâtiment A, troisième étage.
- Errors: substitutions=23, insertions=0, deletions=0
#### Error Details
- Replace: expected "Aujourd'hui," | actual "Aujourd’hui,"
- Replace: expected "six" | actual "6"
- Replace: expected "deux mille vingt-cinq," | actual "2025,"
- Replace: expected "l'inspection" | actual "l’inspection"
- Replace: expected "étage," | actual "étage"
- Replace: expected "l'entrée" | actual "l’entrée"
- Replace: expected "J'ai" | actual "J’ai"
- Replace: expected "est." | actual "Est."
- Replace: expected "quinze" | actual "15"
- Replace: expected "vingt" | actual "20"
- Replace: expected "L'état" | actual "L’état"
- Replace: expected "structures." | actual "structure."
- Replace: expected "défauts. Il" | actual "défauts et il"
- Replace: expected "d'infiltration d'eau" | actual "d’infiltration d’eau"
- Replace: expected "Je vais" | actual "Il faut"
- Replace: expected "l'état" | actual "l’état"
- Replace: expected "l'inspection" | actual "l’inspection"

### Model: gpt-audio-mini
- Status: ✅ Success
- Latency: 3.88s
- Word Error Rate: 17.32%
- Transcript: Bonjour, je suis chef de chantier sur le site de Vancy Construction. Aujourd'hui, le 6 novembre 2025, je fais l'inspection du bâtiment A. Je me trouve actuellement au 3e étage devant l'entrée principale. J'ai remarqué 3 fissures importantes sur le mur Est. Les fissures mesurent environ 15 à 20 cm de longueur. L'état du béton armé semble préoccupant. Je recommande une inspection détaillée par un ingénieur structure. Le coffrage du voile présente également des défauts et il y a des traces d'infiltration d'eau près des banques. Les étés sont en bon état, mais il faut vérifier la stabilité avant de poursuivre les travaux. Il faut maintenant inspecter le 4e étage pour vérifier l'état des dalles et des poutres. Fin de l'inspection du bâtiment A, 3e étage.
- Errors: substitutions=22, insertions=0, deletions=0
#### Error Details
- Replace: expected "Vinci" | actual "Vancy"
- Replace: expected "six" | actual "6"
- Replace: expected "deux mille vingt-cinq," | actual "2025,"
- Replace: expected "troisième étage," | actual "3e étage"
- Replace: expected "trois" | actual "3"
- Replace: expected "est." | actual "Est."
- Replace: expected "quinze" | actual "15"
- Replace: expected "vingt centimètres" | actual "20 cm"
- Replace: expected "structures." | actual "structure."
- Replace: expected "défauts. Il" | actual "défauts et il"
- Replace: expected "banches." | actual "banques."
- Replace: expected "étais" | actual "étés"
- Replace: expected "Je vais" | actual "Il faut"
- Replace: expected "quatrième" | actual "4e"
- Replace: expected "troisième" | actual "3e"

### Model: gpt-4o-audio-preview
- Status: ✅ Success
- Latency: 2.78s
- Word Error Rate: 14.96%
- Transcript: Bonjour, je suis chef de chantier sur le site de Vinci Construction. Aujourd'hui le 6 novembre 2025, je fais l'inspection du bâtiment A. Je me trouve actuellement au troisième étage devant l'entrée principale. J'ai remarqué trois fissures importantes sur le mur Est. Les fissures mesurent environ 15 à 20 centimètres de longueur. L'état du béton armé semble préoccupant, je recommande une inspection détaillée par un ingénieur structure. Le coffrage du voile présente également des défauts, et il y a des traces d'infiltration d'eau près des banches. Les étais sont en bon état, mais il faut vérifier la stabilité avant de poursuivre les travaux. Il faut maintenant inspecter le quatrième étage pour vérifier l'état des dalles et des poutres.
Fin de l'inspection du bâtiment A, troisième étage.
- Errors: substitutions=17, insertions=0, deletions=0
#### Error Details
- Replace: expected "Aujourd'hui," | actual "Aujourd'hui"
- Replace: expected "six" | actual "6"
- Replace: expected "deux mille vingt-cinq," | actual "2025,"
- Replace: expected "étage," | actual "étage"
- Replace: expected "est." | actual "Est."
- Replace: expected "quinze" | actual "15"
- Replace: expected "vingt" | actual "20"
- Replace: expected "préoccupant. Je" | actual "préoccupant, je"
- Replace: expected "structures." | actual "structure."
- Replace: expected "défauts. Il" | actual "défauts, et il"
- Replace: expected "Je vais" | actual "Il faut"

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

### Model: whisper
- Status: ✅ Success
- Latency: 3.28s
- Word Error Rate: 98.74%
- Transcript: Technical inspection of building B, level minus 1. The metal frame presents deformations at the panel level. The benches must be replaced in the next flow. The framing of the reinforced concrete veil is in line with the plan. The high-strength steel, HA-400 adhesion, are correctly positioned. The tubular supports supporting the floor of the ground floor are spaced 1.20 m. It is in line with the prescriptions of the study office. I observe gravel nests in the slab. The concrete was not correctly vibrated during the previous flow. The dilation joints require a calfing. There are infiltrations of water through the concrete joints. The underfloor piping presents cracks in the stairs. This probably indicates a differential layering of the foundations. The waiting armatures exceed 40 cm. They must be protected against corrosion. The decoupling can be carried out in 48 hours, under the pretext of a concrete resistance test. End of the technical inspection.
- Errors: substitutions=159, insertions=0, deletions=0
#### Error Details
- Replace: expected "Inspection technique du bâtiment" | actual "Technical inspection of building"
- Replace: expected "niveau moins un. Le coffrage métallique présente des déformations au niveau des panneaux. Les banches doivent être remplacées avant la prochaine coulée. Le ferraillage du voile en béton armé est conforme aux plans. Les aciers haute adhérence HA quatre cent sont correctement positionnés. Les étais tubulaires supportant le plancher du rez-de-chaussée sont espacés de un mètre vingt. C'est conforme aux" | actual "level minus 1. The metal frame presents deformations at the panel level. The benches must be replaced in the next flow. The framing of the reinforced concrete veil is in line with the plan. The high-strength steel, HA-400 adhesion, are correctly positioned. The tubular supports supporting the floor of the ground floor are spaced 1.20 m. It is in line with the"
- Replace: expected "du bureau d'études. J'observe des nids de gravier dans la dalle. Le béton n'a pas été correctement vibré lors de la coulée précédente. Les" | actual "of the study office. I observe gravel nests in the slab. The concrete was not correctly vibrated during the previous flow. The dilation"
- Replace: expected "de dilatation nécessitent un calfeutrement. Il y" | actual "require"
- Replace: expected "des" | actual "calfing. There are"
- Replace: expected "d'eau par les reprises de bétonnage. Le cuvelage du sous-sol présente des fissurations en escalier. Cela indique probablement un tassement différentiel des fondations. Les" | actual "of water through the concrete joints. The underfloor piping presents cracks in the stairs. This probably indicates a differential layering of the foundations. The waiting"
- Replace: expected "en attente dépassent de quarante centimètres. Elles doivent être protégées contre la" | actual "exceed 40 cm. They must be protected against"
- Replace: expected "Le décoffrage peut être effectué dans quarante-huit heures, sous réserve d'un essai de résistance du béton. Fin de l'inspection technique." | actual "The decoupling can be carried out in 48 hours, under the pretext of a concrete resistance test. End of the technical inspection."

### Model: gpt-audio
- Status: ✅ Success
- Latency: 4.81s
- Word Error Rate: 13.84%
- Transcript: Inspection technique du bâtiment B, niveau -1. Le coffrage métallique présente des déformations au niveau des panneaux. Les banches doivent être remplacées dans la prochaine coulée. Le ferraillage du voile en béton armé est conforme au plan. Les aciers haute adhérence HA400 sont correctement positionnés. Les étais tubulaires supportant le plancher du rez-de-chaussée sont espacés de 1,20 m. C’est conforme aux prescriptions du bureau d’études. J’observe des nids de gravier dans la dalle. Le béton n’a pas été correctement vibré lors de la coulée précédente. Les joints de dilatation nécessitent un calfeutrement. Il y a des infiltrations d’eau par les reprises de bétonnage. Le cuvelage du sous-sol présente des fissures en escalier. Cela indique probablement un tassement différentiel des fondations. Les armatures en attente dépassent de 40 cm. Elles doivent être protégées contre la corrosion. Le décoffrage peut être effectué dans 48 heures, sous réserve d’un essai de résistance du béton. Fin de l’inspection technique.
- Errors: substitutions=22, insertions=0, deletions=0
#### Error Details
- Replace: expected "moins un." | actual "-1."
- Replace: expected "avant" | actual "dans"
- Replace: expected "aux plans." | actual "au plan."
- Replace: expected "HA quatre cent" | actual "HA400"
- Replace: expected "un mètre vingt. C'est" | actual "1,20 m. C’est"
- Replace: expected "d'études. J'observe" | actual "d’études. J’observe"
- Replace: expected "n'a" | actual "n’a"
- Replace: expected "d'eau" | actual "d’eau"
- Replace: expected "fissurations" | actual "fissures"
- Replace: expected "quarante centimètres." | actual "40 cm."
- Replace: expected "quarante-huit" | actual "48"
- Replace: expected "d'un" | actual "d’un"
- Replace: expected "l'inspection" | actual "l’inspection"

### Model: gpt-audio-mini
- Status: ✅ Success
- Latency: 2.83s
- Word Error Rate: 11.32%
- Transcript: {"text":"Inspection technique du bâtiment B, niveau -1. Le coffrage métallique présente des déformations au niveau des panneaux. Les banches doivent être remplacées dans la prochaine coulée. Le ferraillage du voile en béton armé est conforme au plan. Les aciers haute adhérence HA 400 sont correctement positionnés. Les étais tubulaires, supportant le plancher du rez-de-chaussée, sont espacés de 1,20 m. C'est conforme aux prescriptions du bureau d'études. J'observe des nids de gravier dans la dalle. Le béton n'a pas été correctement vibré lors de la coulée précédente. Les joints de dilatation nécessitent un calfeutrement. Il y a des infiltrations d'eau par les reprises de bétonnage. Le cuvelage du sous-sol présente des fissures en escalier. Cela indique probablement un tassement différentiel des fondations. Les armatures en attente dépassent de 40 cm. Elles doivent être protégées contre la corrosion. Le décoffrage peut être effectué dans 48 heures, sous réserve d'un essai de résistance du béton. Fin de l'inspection technique."}
- Errors: substitutions=18, insertions=0, deletions=0
#### Error Details
- Replace: expected "Inspection" | actual "{"text":"Inspection"
- Replace: expected "moins un." | actual "-1."
- Replace: expected "avant" | actual "dans"
- Replace: expected "aux plans." | actual "au plan."
- Replace: expected "quatre cent" | actual "400"
- Replace: expected "tubulaires" | actual "tubulaires,"
- Replace: expected "rez-de-chaussée" | actual "rez-de-chaussée,"
- Replace: expected "un mètre vingt." | actual "1,20 m."
- Replace: expected "fissurations" | actual "fissures"
- Replace: expected "quarante centimètres." | actual "40 cm."
- Replace: expected "quarante-huit" | actual "48"
- Replace: expected "technique." | actual "technique."}"

### Model: gpt-4o-audio-preview
- Status: ✅ Success
- Latency: 3.45s
- Word Error Rate: 12.58%
- Transcript: Inspection technique du bâtiment B, niveau moins un. Le coffrage métallique présente des déformations au niveau des panneaux. Les banche doivent être remplacées dans la prochaine coulée. Le ferraillage du voile en béton armé est conforme au plan, les aciers haute adhérence HA 400 sont correctement positionnés. Les étais tubulaires supportant le plancher du rez-de-chaussée sont espacés de un mètre vingt, c'est conforme aux prescriptions du bureau d'études. J'observe des nids de gravier dans la dalle, le béton n'a pas été correctement vibré lors de la coulée précédente. Les joints de dilatation nécessitent un calfeutrage. Il y a des infiltrations d'eau par les reprises de bétonnage. Le cuvelage du sous-sol présente des fissures en escalier, cela indique probablement un tassement différentiel des fondations. Les armatures en attente dépassent de 40 cm, elles doivent être protégées contre la corrosion. Le décoffrage peut être effectué dans 48 heures sous réserve d'un essai de résistance du béton. Fin de l'inspection technique.
- Errors: substitutions=20, insertions=0, deletions=0
#### Error Details
- Replace: expected "banches" | actual "banche"
- Replace: expected "avant" | actual "dans"
- Replace: expected "aux plans. Les" | actual "au plan, les"
- Replace: expected "quatre cent" | actual "400"
- Replace: expected "vingt. C'est" | actual "vingt, c'est"
- Replace: expected "dalle. Le" | actual "dalle, le"
- Replace: expected "calfeutrement." | actual "calfeutrage."
- Replace: expected "fissurations" | actual "fissures"
- Replace: expected "escalier. Cela" | actual "escalier, cela"
- Replace: expected "quarante centimètres. Elles" | actual "40 cm, elles"
- Replace: expected "quarante-huit heures," | actual "48 heures"

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

### Model: whisper
- Status: ✅ Success
- Latency: 3.38s
- Word Error Rate: 60.99%
- Transcript: Relevé de mesure, bâtiment C, étage 2, fissure numéro 1, longueur 23 cm, largeur 2 mm, profondeur environ 5 mm. Fissure numéro 2, longueur 37 cm, largeur 3 mm, orientation 45 degrés par rapport à l'horizontale. Fissure numéro 3, largeur 15 cm, située à 1,40 m du sol, surface totale du mur, 4 murs d'auteur sur 8 m de longueur, soit 32 m². Nombre d'armature visible, 12 bar, diamètre 16 mm, espacement entre les poteaux, 4,50 m, épaisseur du voile, 25 cm, charge prévue sur la dalle, 500 kg par m², concrete temperature, 18 ° C, relative humidity, 65 %, tested concrete resistance, 30 MPa after 28 days. Flèches mesurées au centre de la poutre, 8 mm, dans les tolérances acceptables. Nombre d'ouvriers présent, 15 personnes. Fin du relevé des mesures.
- Errors: substitutions=104, insertions=0, deletions=0
#### Error Details
- Replace: expected "des mesures," | actual "de mesure,"
- Replace: expected "deux." | actual "2, fissure numéro 1, longueur 23 cm, largeur 2 mm, profondeur environ 5 mm."
- Replace: expected "un:" | actual "2,"
- Replace: expected "vingt-trois centimètres," | actual "37 cm,"
- Replace: expected "deux millimètres, profondeur environ cinq millimètres. Fissure numéro deux: longueur trente-sept centimètres, largeur trois millimètres," | actual "3 mm,"
- Replace: expected "quarante-cinq" | actual "45"
- Replace: expected "trois: longueur quinze centimètres," | actual "3, largeur 15 cm,"
- Replace: expected "un mètre cinquante" | actual "1,40 m"
- Replace: expected "sol. Surface" | actual "sol, surface"
- Replace: expected "mur: quatre mètres de hauteur" | actual "mur, 4 murs d'auteur"
- Replace: expected "huit mètres" | actual "8 m"
- Replace: expected "trente-deux mètres carrés." | actual "32 m²."
- Replace: expected "d'armatures visibles: douze barres de" | actual "d'armature visible, 12 bar,"
- Replace: expected "seize millimètres. Espacement" | actual "16 mm, espacement"
- Replace: expected "poteaux: quatre mètres cinquante. Épaisseur" | actual "poteaux, 4,50 m, épaisseur"
- Replace: expected "voile: vingt-cinq centimètres. Charge" | actual "voile, 25 cm, charge"
- Replace: expected "dalle: cinq cents kilogrammes" | actual "dalle, 500 kg"
- Replace: expected "mètre carré. Température du béton: dix-huit degrés Celsius. Humidité relative: soixante-cinq pour cent. Résistance du béton testée: trente mégapascals après vingt-huit jours. Flèche mesurée" | actual "m², concrete temperature, 18 ° C, relative humidity, 65 %, tested concrete resistance, 30 MPa after 28 days. Flèches mesurées"
- Replace: expected "poutre: huit millimètres," | actual "poutre, 8 mm,"
- Replace: expected "présents: quinze" | actual "présent, 15"

### Model: gpt-audio
- Status: ✅ Success
- Latency: 4.17s
- Word Error Rate: 56.74%
- Transcript: Relevé de mesures bâtiment C étage 2 :  
Fissure numéro 1 : longueur 23 cm, largeur 2 mm, profondeur environ 5 mm.  
Fissure numéro 2 : longueur 37 cm, largeur 3 mm, orientation 45 degrés par rapport à l’horizontale.  
Fissure numéro 3 : largeur 15 cm, située à 1 m 40 du sol.  
Surface totale du mur : 4 murs de hauteur sur 8 m de longueur, soit 32 m².  
Nombre d’armatures visibles : 12 barres de diamètre 16 mm.  
Espacement entre les poteaux : 4 m 50.  
Épaisseur du voile : 25 cm.  
Charge prévue sur la dalle : 500 kg/m².  
Température du béton : 18 degrés Celsius.  
Humidité relative : 65 %.  
Résistance du béton testée : 30 MPa après 28 jours.  
Flèche mesurée au centre de la poutre : 8 mm dans les tolérances acceptables.  
Nombre d’ouvriers présents : 15 personnes.  
Fin du relevé des mesures.
- Errors: substitutions=80, insertions=0, deletions=0
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
- Replace: expected "un mètre cinquante" | actual "1 m 40"
- Replace: expected "mur: quatre mètres" | actual "mur : 4 murs"
- Replace: expected "huit mètres" | actual "8 m"
- Replace: expected "trente-deux mètres carrés." | actual "32 m²."
- Replace: expected "d'armatures visibles: douze" | actual "d’armatures visibles : 12"
- Replace: expected "seize millimètres." | actual "16 mm."
- Replace: expected "poteaux: quatre mètres cinquante." | actual "poteaux : 4 m 50."
- Replace: expected "voile: vingt-cinq centimètres." | actual "voile : 25 cm."
- Replace: expected "dalle: cinq cents kilogrammes par mètre carré." | actual "dalle : 500 kg/m²."
- Replace: expected "béton: dix-huit" | actual "béton : 18"
- Replace: expected "relative: soixante-cinq pour cent." | actual "relative : 65 %."
- Replace: expected "testée: trente mégapascals" | actual "testée : 30 MPa"
- Replace: expected "vingt-huit" | actual "28"
- Replace: expected "poutre: huit millimètres," | actual "poutre : 8 mm"
- Replace: expected "d'ouvriers présents: quinze" | actual "d’ouvriers présents : 15"

### Model: gpt-audio-mini
- Status: ✅ Success
- Latency: 3.01s
- Word Error Rate: 48.23%
- Transcript: Rélevé de mesures, bâtiment C, étage 2. Fissure numéro 1, longueur 23 cm, largeur 2 mm, profondeur environ 5 mm. Fissure numéro 2, longueur 37 cm, largeur 3 mm, orientation 45 degrés par rapport à l'horizontale. Fissure numéro 3, largeur 15 cm, située à 1,40 m du sol. Surface totale du mur, 4 murs d'hauteur sur 8 m de longueur, soit 32 m². Nombre d'armatures visibles, 12 barres de diamètre 16 mm. Espacement entre les poteaux, 4,50 m. Épaisseur du voile, 25 cm. Charge prévue sur la dalle, 500 kg par m². Température du béton, 18 °C. Humidité relative, 65 %. Résistance du béton testée, 30 MPa après 28 jours. Flèche mesurée au centre de la poutre, 8 mm, dont les tolérances acceptables. Nombre d'ouvriers présents, 15 personnes. Fin du relevé des mesures.
- Errors: substitutions=68, insertions=0, deletions=0
#### Error Details
- Replace: expected "Relevé des" | actual "Rélevé de"
- Replace: expected "deux." | actual "2."
- Replace: expected "un:" | actual "1,"
- Replace: expected "vingt-trois centimètres," | actual "23 cm,"
- Replace: expected "deux millimètres," | actual "2 mm,"
- Replace: expected "cinq millimètres." | actual "5 mm."
- Replace: expected "deux:" | actual "2,"
- Replace: expected "trente-sept centimètres," | actual "37 cm,"
- Replace: expected "trois millimètres," | actual "3 mm,"
- Replace: expected "quarante-cinq" | actual "45"
- Replace: expected "trois: longueur quinze centimètres," | actual "3, largeur 15 cm,"
- Replace: expected "un mètre cinquante" | actual "1,40 m"
- Replace: expected "mur: quatre mètres de hauteur" | actual "mur, 4 murs d'hauteur"
- Replace: expected "huit mètres" | actual "8 m"
- Replace: expected "trente-deux mètres carrés." | actual "32 m²."
- Replace: expected "visibles: douze" | actual "visibles, 12"
- Replace: expected "seize millimètres." | actual "16 mm."
- Replace: expected "poteaux: quatre mètres cinquante." | actual "poteaux, 4,50 m."
- Replace: expected "voile: vingt-cinq centimètres." | actual "voile, 25 cm."
- Replace: expected "dalle: cinq cents kilogrammes" | actual "dalle, 500 kg"
- Replace: expected "mètre carré." | actual "m²."
- Replace: expected "béton: dix-huit degrés Celsius." | actual "béton, 18 °C."
- Replace: expected "relative: soixante-cinq pour cent." | actual "relative, 65 %."
- Replace: expected "testée: trente mégapascals" | actual "testée, 30 MPa"
- Replace: expected "vingt-huit" | actual "28"
- Replace: expected "poutre: huit millimètres, dans" | actual "poutre, 8 mm, dont"
- Replace: expected "présents: quinze" | actual "présents, 15"

### Model: gpt-4o-audio-preview
- Status: ✅ Success
- Latency: 3.55s
- Word Error Rate: 40.43%
- Transcript: Relevé de mesures, bâtiment C, étage 2. Fissure numéro 1 : longueur 23 centimètres, largeur 2 millimètres, profondeur environ 5 millimètres. Fissure numéro 2 : longueur 37 centimètres, largeur 3 millimètres, orientation 45 degrés par rapport à l’horizontale. Fissure numéro 3 : largeur 15 centimètres, située à 1 mètre 40 du sol. Surface totale du mur : 4 murs de hauteur sur 8 mètres de longueur, soit 32 mètres carrés. Nombres d'armatures visibles : 12 barres de diamètre 16 millimètres. Espacement entre les poteaux : 4 mètres 50. Épaisseur du voile : 25 centimètres. Charge prévue sur la dalle : 500 kilogrammes par mètre carré. Température du béton : 18 degrés Celsius. Humidité relative : 65 pourcents. Résistance du béton testée : 30 mégapascals après 28 jours. Flèche mesurée au centre de la poutre : 8 millimètres, dans les tolérances acceptables. Nombre d'ouvriers présents : 15 personnes. Fin du relevé des mesures.
- Errors: substitutions=57, insertions=0, deletions=0
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
- Replace: expected "l'horizontale." | actual "l’horizontale."
- Replace: expected "trois: longueur quinze" | actual "3 : largeur 15"
- Replace: expected "un" | actual "1"
- Replace: expected "cinquante" | actual "40"
- Replace: expected "mur: quatre mètres" | actual "mur : 4 murs"
- Replace: expected "huit" | actual "8"
- Replace: expected "trente-deux" | actual "32"
- Replace: expected "Nombre" | actual "Nombres"
- Replace: expected "visibles: douze" | actual "visibles : 12"
- Replace: expected "seize" | actual "16"
- Replace: expected "poteaux: quatre" | actual "poteaux : 4"
- Replace: expected "cinquante." | actual "50."
- Replace: expected "voile: vingt-cinq" | actual "voile : 25"
- Replace: expected "dalle: cinq cents" | actual "dalle : 500"
- Replace: expected "béton: dix-huit" | actual "béton : 18"
- Replace: expected "relative: soixante-cinq pour cent." | actual "relative : 65 pourcents."
- Replace: expected "testée: trente" | actual "testée : 30"
- Replace: expected "vingt-huit" | actual "28"
- Replace: expected "poutre: huit" | actual "poutre : 8"
- Replace: expected "présents: quinze" | actual "présents : 15"

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

### Model: whisper
- Status: ❌ Failed
- Error: `{"error":{"code":"RateLimitReached","message": "Your requests to whisper for whisper in Sweden Central have exceeded the call rate limit for your current AIServices S0 pricing tier. This request was for Audio_Translations under Azure OpenAI API version 2024-06-01. Please retry after 10 seconds. To increase your default rate limit, visit: https://aka.ms/oai/quotaincrease."}}`

### Model: gpt-audio
- Status: ✅ Success
- Latency: 5.54s
- Word Error Rate: 35.98%
- Transcript: Note numéro 1 : Appeler le fournisseur de ciment demain matin à 9h.  
Note numéro 2 : Le camion toupie arrive à 14h pour la coulée du radier.  
Note numéro 3 : Vérifier la conformité des plans avec l’architecte avant mercredi.  
Note numéro 4 : Commander 30 m³ de béton C25/30 pour la semaine prochaine.  
Note numéro 5 : Réunion de coordination vendredi à 10h avec tous les corps d’état.  
Note numéro 6 : Prévoir l’évacuation des gravats du sous-sol, volume estimé : 50 m³.  
Note numéro 7 : Le contrôle technique passe lundi matin, préparer le document de suivi.  
Note numéro 8 : Problème avec la grue à tour, le mécanicien doit intervenir aujourd’hui.  
Note numéro 9 : Livraison des planches reportée au jeudi, adapter le plan en conséquence.  
Note numéro 10 : Installer les gardes-corps au niveau du 5ème étage avant la fin de semaine.  
Note numéro 11 : Mettre en place la signalétique de sécurité sur l’ensemble du chantier.  
Note numéro 12 : Fin des notes rapides.
- Errors: substitutions=59, insertions=0, deletions=0
#### Error Details
- Replace: expected "un:" | actual "1 :"
- Replace: expected "neuf heures." | actual "9h."
- Replace: expected "deux:" | actual "2 :"
- Replace: expected "quatorze heures" | actual "14h"
- Replace: expected "trois:" | actual "3 :"
- Replace: expected "l'architecte" | actual "l’architecte"
- Replace: expected "quatre:" | actual "4 :"
- Replace: expected "trente mètres cubes" | actual "30 m³"
- Replace: expected "C vingt-cinq trente" | actual "C25/30"
- Replace: expected "cinq:" | actual "5 :"
- Replace: expected "dix heures" | actual "10h"
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
- Replace: expected "banches" | actual "planches"
- Replace: expected "jeudi. Adapter" | actual "jeudi, adapter"
- Replace: expected "planning" | actual "plan"
- Replace: expected "dix:" | actual "10 :"
- Replace: expected "garde-corps" | actual "gardes-corps"
- Replace: expected "cinquième" | actual "5ème"
- Replace: expected "onze:" | actual "11 :"
- Replace: expected "l'ensemble" | actual "l’ensemble"
- Replace: expected "douze:" | actual "12 :"

### Model: gpt-audio-mini
- Status: ✅ Success
- Latency: 2.85s
- Word Error Rate: 31.71%
- Transcript: Vous avez déjà la transcription :

Note numéro 1 : Appeler le fournisseur de ciment demain matin à 9h.  
Note numéro 2 : Le camion toupie arrive à 14h pour la coulée du radier.  
Note numéro 3 : Vérifier la conformité des plans avec l'architecte avant mercredi.  
Note numéro 4 : Commander 30 m³ de béton C25/30 pour la semaine prochaine.  
Note numéro 5 : Réunion de coordination vendredi de 6h à 10h avec tous les corps d'état.  
Note numéro 6 : Prévoir l'évacuation des gravats du sous-sol. Volume estimé : 50 m³.  
Note numéro 7 : Le contrôle technique passe lundi matin. Préparer le document de suivi.  
Note numéro 8 : Problème avec la grue à tour. Le mécanicien doit intervenir aujourd'hui.  
Note numéro 9 : Livraison des banches reportée au jeudi. Adapter le plan en conséquence.  
Note numéro 10 : Installer les garde-corps au niveau du 5ème étage avant la fin de semaine.  
Note numéro 11 : Mettre en place la signalétique de sécurité sur l'ensemble du chantier.  
Note numéro 12 : Fin des notes rapides.
- Errors: substitutions=44, insertions=8, deletions=0
#### Error Details
- Insert: expected "" | actual "Vous avez déjà la transcription :"
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
- Replace: expected "six:" | actual "6 :"
- Replace: expected "estimé: cinquante mètres cubes." | actual "estimé : 50 m³."
- Replace: expected "sept:" | actual "7 :"
- Replace: expected "les documents" | actual "le document"
- Replace: expected "huit:" | actual "8 :"
- Replace: expected "neuf:" | actual "9 :"
- Replace: expected "planning" | actual "plan"
- Replace: expected "dix:" | actual "10 :"
- Replace: expected "cinquième" | actual "5ème"
- Replace: expected "onze:" | actual "11 :"
- Replace: expected "douze:" | actual "12 :"

### Model: gpt-4o-audio-preview
- Status: ✅ Success
- Latency: 3.26s
- Word Error Rate: 51.22%
- Transcript: Note numéro 1 : appeler le fournisseur de ciment demain matin à 9h.
Note numéro 2 : le camion-toupie arrive à 14h pour la coulée du radier.
Note numéro 3 : vérifier la conformité des plans avec l'architecte avant mercredi.
Note numéro 4 : commander 30 m³ de béton C25/30 pour la semaine prochaine.
Note numéro 5 : réunion de coordination vendredi à 10h avec tous les corps d'état.
Note numéro 6 : prévoir l'évacuation des gravats du sous-sol, volume estimé : 50 m³.
Note numéro 7 : le contrôle technique passe lundi matin, préparer les documents de suivi.
Note numéro 8 : problème avec la grue A-Tour, le mécanicien doit intervenir aujourd'hui.
Note numéro 9 : livraison des banches reportée à jeudi, adapter le plan en conséquence.
Note numéro 10 : installer les garde-corps au niveau du 5ème étage avant la fin de semaine.
Note numéro 11 : mettre en place la signalétique de sécurité sur l'ensemble du chantier.
Note numéro 12 : fin des notes rapides.
- Errors: substitutions=64, insertions=0, deletions=0
#### Error Details
- Replace: expected "un: Appeler" | actual "1 : appeler"
- Replace: expected "neuf heures." | actual "9h."
- Replace: expected "deux: Le camion toupie" | actual "2 : le camion-toupie"
- Replace: expected "quatorze heures" | actual "14h"
- Replace: expected "trois: Vérifier" | actual "3 : vérifier"
- Replace: expected "quatre: Commander trente mètres cubes" | actual "4 : commander 30 m³"
- Replace: expected "C vingt-cinq trente" | actual "C25/30"
- Replace: expected "cinq: Réunion" | actual "5 : réunion"
- Replace: expected "dix heures" | actual "10h"
- Replace: expected "six: Prévoir" | actual "6 : prévoir"
- Replace: expected "sous-sol. Volume estimé: cinquante mètres cubes." | actual "sous-sol, volume estimé : 50 m³."
- Replace: expected "sept: Le" | actual "7 : le"
- Replace: expected "matin. Préparer" | actual "matin, préparer"
- Replace: expected "huit: Problème" | actual "8 : problème"
- Replace: expected "à tour. Le" | actual "A-Tour, le"
- Replace: expected "neuf: Livraison" | actual "9 : livraison"
- Replace: expected "au jeudi. Adapter" | actual "à jeudi, adapter"
- Replace: expected "planning" | actual "plan"
- Replace: expected "dix: Installer" | actual "10 : installer"
- Replace: expected "cinquième" | actual "5ème"
- Replace: expected "onze: Mettre" | actual "11 : mettre"
- Replace: expected "douze: Fin" | actual "12 : fin"

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

### Model: whisper
- Status: ✅ Success
- Latency: 3.83s
- Word Error Rate: 20.51%
- Transcript: Déclaration d'incident bâtiment D, niveau 4, date 6 novembre 2025, heure 11h45. Un ouvrier est glissé près du bord de la dalle. Pas de chute, mais situation dangereuse. Le garde-corps temporaire était mal fixé. Il a bougé sous la pression. L'ouvrier concerné, monsieur Dupont, chef d'équipe, grosse oeuvre. Aucune blessure constatée. L'ouvrier a été examiné par le secouriste du chantier. Mesure immédiate prise. Zone sécurisée. Accès interdit jusqu'à réparation complète du garde-corps. Cause probable. Fixation insuffisante des poteaux sur la dalle. Vise de fixation desserrée. Action corrective. Vérification immédiate de tous les garde-corps sur l'ensemble du chantier. Responsable sécurité informé à midi. Rapport écrit à transmettre au coordinateur SPS avant 16h. Formation de rappel sur la sécurité en hauteur programmée pour toute l'équipe demain matin. Aucun arrêt de travail nécessaire. Les travaux peuvent reprendre dès sécurisation de la zone. Je reste disponible pour tout complément d'information. Fin de la déclaration d'incident.
- Errors: substitutions=32, insertions=0, deletions=0
#### Error Details
- Replace: expected "d'incident," | actual "d'incident"
- Replace: expected "quatre. Date: six" | actual "4, date 6"
- Replace: expected "deux mille vingt-cinq, heure: onze heures quarante-cinq." | actual "2025, heure 11h45."
- Replace: expected "a" | actual "est"
- Replace: expected "concerné: Monsieur" | actual "concerné, monsieur"
- Replace: expected "d'équipe gros œuvre." | actual "d'équipe, grosse oeuvre."
- Replace: expected "Mesures immédiates prises: zone sécurisée, accès" | actual "Mesure immédiate prise. Zone sécurisée. Accès"
- Replace: expected "probable: fixation" | actual "probable. Fixation"
- Replace: expected "Vis" | actual "Vise"
- Replace: expected "desserrées. Actions correctives: vérification" | actual "desserrée. Action corrective. Vérification"
- Replace: expected "seize heures." | actual "16h."

### Model: gpt-audio
- Status: ✅ Success
- Latency: 4.49s
- Word Error Rate: 28.85%
- Transcript: Déclaration d’incident bâtiment D niveau 4  
Date : 6 novembre 2025  
Heure : 11h45  
Un ouvrier a glissé près du bord de la dalle, pas de chute mais situation dangereuse. Le garde-corps temporaire était mal fixé, il a bougé sous la pression.  
L’ouvrier concerné : Monsieur Dupont, chef d’équipe gros œuvre.  
Aucune blessure constatée, l’ouvrier a été examiné par le secouriste du chantier.  
Mesure immédiate prise : zone sécurisée, accès interdit jusqu’à réparation complète du garde-corps.  
Cause probable : fixation insuffisante des poteaux sur la dalle, vis de fixation desserrées.  
Action corrective : vérification immédiate de tous les garde-corps sur l’ensemble du chantier.  
Responsable sécurité informé à midi.  
Rapport écrit à transmettre au coordonnateur SPS avant 16h.  
Formation de rappel sur la sécurité en hauteur programmée pour toute l’équipe demain matin.  
Aucun arrêt de travail nécessaire, les travaux peuvent reprendre dès sécurisation de la zone.  
Je reste disponible pour tout complément d’information.  
Fin de la déclaration d’incident.
- Errors: substitutions=45, insertions=0, deletions=0
#### Error Details
- Replace: expected "d'incident," | actual "d’incident"
- Replace: expected "D," | actual "D"
- Replace: expected "quatre. Date: six" | actual "4 Date : 6"
- Replace: expected "deux mille vingt-cinq, heure: onze heures quarante-cinq." | actual "2025 Heure : 11h45"
- Replace: expected "dalle. Pas" | actual "dalle, pas"
- Replace: expected "chute," | actual "chute"
- Replace: expected "fixé. Il" | actual "fixé, il"
- Replace: expected "L'ouvrier concerné:" | actual "L’ouvrier concerné :"
- Replace: expected "d'équipe" | actual "d’équipe"
- Replace: expected "constatée. L'ouvrier" | actual "constatée, l’ouvrier"
- Replace: expected "Mesures immédiates prises:" | actual "Mesure immédiate prise :"
- Replace: expected "jusqu'à" | actual "jusqu’à"
- Replace: expected "probable:" | actual "probable :"
- Replace: expected "dalle. Vis" | actual "dalle, vis"
- Replace: expected "Actions correctives:" | actual "Action corrective :"
- Replace: expected "l'ensemble" | actual "l’ensemble"
- Replace: expected "coordinateur" | actual "coordonnateur"
- Replace: expected "seize heures." | actual "16h."
- Replace: expected "l'équipe" | actual "l’équipe"
- Replace: expected "nécessaire. Les" | actual "nécessaire, les"
- Replace: expected "d'information." | actual "d’information."
- Replace: expected "d'incident." | actual "d’incident."

### Model: gpt-audio-mini
- Status: ✅ Success
- Latency: 2.77s
- Word Error Rate: 21.15%
- Transcript: {"text":"Déclaration d'incident, bâtiment D, niveau 4. Date : 6 novembre 2025. Heure : 11h45. Un ouvrier a glissé près du bord de la dalle. Pas de chute, mais situation dangereuse. Le garde-corps temporaire était mal fixé, il a bougé sous la pression. L'ouvrier concerné : M. Dupont, chef d'équipe, gros œuvre. Aucune blessure constatée. L'ouvrier a été examiné par le secouriste du chantier. Mesure immédiate prise : zone sécurisée, accès interdit jusqu'à réparation complète du garde-corps. Cause probable : fixation insuffisante des poutaux sur la dalle. Vis de fixation desserrée. Action corrective : vérification immédiate de tous les gardes-corps sur l'ensemble du chantier. Responsable sécurité informé à midi. Rapport écrit à transmettre au coordinateur SPS avant 16h. Formation de rappel sur la sécurité en hauteur programmée pour toute l'équipe demain matin. Aucun arrêt de travail nécessaire. Les travaux peuvent reprendre dès sécurisation de la zone. Je reste disponible pour tout complément d'information. Fin de la déclaration d'incident."}
- Errors: substitutions=33, insertions=0, deletions=0
#### Error Details
- Replace: expected "Déclaration" | actual "{"text":"Déclaration"
- Replace: expected "quatre. Date: six" | actual "4. Date : 6"
- Replace: expected "deux mille vingt-cinq, heure: onze heures quarante-cinq." | actual "2025. Heure : 11h45."
- Replace: expected "fixé. Il" | actual "fixé, il"
- Replace: expected "concerné: Monsieur" | actual "concerné : M."
- Replace: expected "d'équipe" | actual "d'équipe,"
- Replace: expected "Mesures immédiates prises:" | actual "Mesure immédiate prise :"
- Replace: expected "probable:" | actual "probable :"
- Replace: expected "poteaux" | actual "poutaux"
- Replace: expected "desserrées. Actions correctives:" | actual "desserrée. Action corrective :"
- Replace: expected "garde-corps" | actual "gardes-corps"
- Replace: expected "seize heures." | actual "16h."
- Replace: expected "d'incident." | actual "d'incident."}"

### Model: gpt-4o-audio-preview
- Status: ✅ Success
- Latency: 3.46s
- Word Error Rate: 37.18%
- Transcript: Déclaration d’incident
Bâtiment D, Niveau 4
Date : 6 novembre 2025
Heure : 11h45
Un ouvrier a glissé près du bord de la dalle. Pas de chute, mais situation dangereuse.
Le garde-corps temporaire était mal fixé, il a bougé sous la pression.
Ouvrier concerné : M. Dupont, chef d’équipe gros œuvre.
Aucune blessure constatée, l'ouvrier a été examiné par le secouriste du chantier.
Mesure immédiate prise : zone sécurisée, accès interdit jusqu’à réparation complète du garde-corps.
Cause probable : fixation insuffisante des poteaux sur la dalle, vis de fixation desserrées.
Action corrective : vérification immédiate de tous les garde-corps sur l’ensemble du chantier.
Responsable sécurité informé à midi.
Rapport écrit à transmettre au coordinateur SPS avant 16h.
Formation de rappel sur la sécurité en hauteur programmée pour toute l’équipe demain matin.
Aucun arrêt de travail nécessaire, les travaux peuvent reprendre dès sécurisation de la zone.
Je reste disponible pour tout complément d’information.
Fin de la déclaration d’incident.
- Errors: substitutions=43, insertions=0, deletions=0
#### Error Details
- Replace: expected "d'incident, bâtiment" | actual "d’incident Bâtiment"
- Replace: expected "niveau quatre. Date: six" | actual "Niveau 4 Date : 6"
- Replace: expected "deux mille vingt-cinq, heure: onze heures quarante-cinq." | actual "2025 Heure : 11h45"
- Replace: expected "fixé. Il" | actual "fixé, il"
- Replace: expected "L'ouvrier concerné: Monsieur" | actual "Ouvrier concerné : M."
- Replace: expected "d'équipe" | actual "d’équipe"
- Replace: expected "constatée. L'ouvrier" | actual "constatée, l'ouvrier"
- Replace: expected "Mesures immédiates prises:" | actual "Mesure immédiate prise :"
- Replace: expected "jusqu'à" | actual "jusqu’à"
- Replace: expected "probable:" | actual "probable :"
- Replace: expected "dalle. Vis" | actual "dalle, vis"
- Replace: expected "Actions correctives:" | actual "Action corrective :"
- Replace: expected "l'ensemble" | actual "l’ensemble"
- Replace: expected "seize heures." | actual "16h."
- Replace: expected "l'équipe" | actual "l’équipe"
- Replace: expected "nécessaire. Les" | actual "nécessaire, les"
- Replace: expected "d'information." | actual "d’information."
- Replace: expected "d'incident." | actual "d’incident."

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

### Model: whisper
- Status: ✅ Success
- Latency: 2.28s
- Word Error Rate: 97.60%
- Transcript: Hello, construction site manager at 26 Construction. Today, November 6, 2025, I am inspecting building A. I am currently on the third floor, in front of the main entrance. I noticed three major cracks on the east wall. The cracks are about 15 to 20 cm long. The state of the reinforced concrete is worrying. I recommend a detailed inspection by a structural engineer. The veil casing also has defects. There are traces of water infiltration near the benches. The T-junctions are in good condition, but we must check the stability before continuing the work. I will now inspect the fourth floor to check the condition of the slabs and beams. End of inspection of building A, third floor.
- Errors: substitutions=134, insertions=0, deletions=0
#### Error Details
- Replace: expected "Bonjour, chef de chantier sur le" | actual "Hello, construction"
- Replace: expected "de Vinci" | actual "manager at 26"
- Replace: expected "Aujourd'hui, le six novembre deux mille vingt-cinq, je fais l'inspection du bâtiment" | actual "Today, November 6, 2025, I am inspecting building"
- Replace: expected "Je me trouve actuellement au troisième étage, devant l'entrée principale. J'ai remarqué trois fissures importantes sur le mur est. Les fissures mesurent environ quinze à vingt centimètres de longueur. L'état du béton armé semble préoccupant. Je recommande une" | actual "I am currently on the third floor, in front of the main entrance. I noticed three major cracks on the east wall. The cracks are about 15 to 20 cm long. The state of the reinforced concrete is worrying. I recommend a detailed"
- Replace: expected "détaillée par un ingénieur structures. Le coffrage du voile présente également des défauts. Il y" | actual "by"
- Replace: expected "des" | actual "structural engineer. The veil casing also has defects. There are"
- Replace: expected "d'infiltration d'eau près des banches. Les étais sont en bon état, mais il faut vérifier la stabilité avant de poursuivre les travaux. Je vais maintenant inspecter le quatrième étage pour vérifier l'état des dalles et des poutres. Fin de l'inspection du bâtiment" | actual "of water infiltration near the benches. The T-junctions are in good condition, but we must check the stability before continuing the work. I will now inspect the fourth floor to check the condition of the slabs and beams. End of inspection of building"
- Replace: expected "troisième étage." | actual "third floor."

### Model: gpt-audio
- Status: ✅ Success
- Latency: 3.11s
- Word Error Rate: 14.40%
- Transcript: Bonjour, chef de chantier sur le site de Vinci Construction. Aujourd’hui, le 6 novembre 2025, je fais l’inspection du bâtiment A. Je me trouve actuellement au troisième étage, devant l’entrée principale. J’ai remarqué trois fissures importantes sur le mur Est. Les fissures mesurent environ 15 à 20 cm de longueur. L’état du béton armé semble préoccupant. Je recommande une inspection détaillée par un ingénieur structure. Le coffrage du voile présente également des défauts. Il y a des traces d’infiltration d’eau près des banches. Les étais sont en bon état, mais il faut vérifier la stabilité avant de poursuivre les travaux. Je vais maintenant inspecter le quatrième étage pour vérifier l’état des dalles et des poutres. Fin de l’inspection du bâtiment A, troisième étage.
- Errors: substitutions=18, insertions=0, deletions=0
#### Error Details
- Replace: expected "Aujourd'hui," | actual "Aujourd’hui,"
- Replace: expected "six" | actual "6"
- Replace: expected "deux mille vingt-cinq," | actual "2025,"
- Replace: expected "l'inspection" | actual "l’inspection"
- Replace: expected "l'entrée" | actual "l’entrée"
- Replace: expected "J'ai" | actual "J’ai"
- Replace: expected "est." | actual "Est."
- Replace: expected "quinze" | actual "15"
- Replace: expected "vingt centimètres" | actual "20 cm"
- Replace: expected "L'état" | actual "L’état"
- Replace: expected "structures." | actual "structure."
- Replace: expected "d'infiltration d'eau" | actual "d’infiltration d’eau"
- Replace: expected "l'état" | actual "l’état"
- Replace: expected "l'inspection" | actual "l’inspection"

### Model: gpt-audio-mini
- Status: ✅ Success
- Latency: 3.32s
- Word Error Rate: 9.60%
- Transcript: Bonjour, chef de chantier sur le site de Vinci Construction. Aujourd'hui, le 6 novembre 2025, je fais l'inspection du bâtiment A. Je me trouve actuellement au troisième étage, devant l'entrée principale. J'ai remarqué trois fissures importantes sur le mur est. Les fissures mesurent environ 15 à 20 cm de longueur. L'état du béton armé sont préoccupants. Je recommande une inspection détaillée par un ingénieur structure. Le coffrage du voile présente également des défauts. Il y a des traces d'infiltration d'eau près des branches. Les étais sont en bon état, mais il faut vérifier la stabilité avant de poursuivre les travaux. Je vais maintenant inspecter le quatrième étage pour vérifier l'état des dalles et des poutres. Fin de l'inspection du bâtiment 1, troisième étage.
- Errors: substitutions=12, insertions=0, deletions=0
#### Error Details
- Replace: expected "six" | actual "6"
- Replace: expected "deux mille vingt-cinq," | actual "2025,"
- Replace: expected "quinze" | actual "15"
- Replace: expected "vingt centimètres" | actual "20 cm"
- Replace: expected "semble préoccupant." | actual "sont préoccupants."
- Replace: expected "structures." | actual "structure."
- Replace: expected "banches." | actual "branches."
- Replace: expected "A," | actual "1,"

### Model: gpt-4o-audio-preview
- Status: ✅ Success
- Latency: 2.65s
- Word Error Rate: 12.00%
- Transcript: Bonjour, chef de chantier sur le site de Vinci Construction. Aujourd'hui, le 6 novembre 2023, je fais l'inspection du bâtiment A. Je me trouve actuellement au 3ème étage, devant l'entrée principale. J'ai remarqué trois fissures importantes sur le mur Est. Les fissures mesurent environ 15 à 20 centimètres de longueur. L'état du béton armé est préoccupant. Je recommande une inspection détaillée par un ingénieur structure. Le coffrage du voile présente également des défauts, il y a des traces d'infiltration d'eau près des planches. Les étais sont en bon état, mais il faut vérifier la stabilité avant de poursuivre les travaux. Je vais maintenant inspecter le 4ème étage pour vérifier l'état des dalles et des poutres. Fin de l'inspection du bâtiment A, 3ème étage.
- Errors: substitutions=15, insertions=0, deletions=0
#### Error Details
- Replace: expected "six" | actual "6"
- Replace: expected "deux mille vingt-cinq," | actual "2023,"
- Replace: expected "troisième" | actual "3ème"
- Replace: expected "est." | actual "Est."
- Replace: expected "quinze" | actual "15"
- Replace: expected "vingt" | actual "20"
- Replace: expected "semble" | actual "est"
- Replace: expected "structures." | actual "structure."
- Replace: expected "défauts. Il" | actual "défauts, il"
- Replace: expected "banches." | actual "planches."
- Replace: expected "quatrième" | actual "4ème"
- Replace: expected "troisième" | actual "3ème"

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

### Model: whisper
- Status: ✅ Success
- Latency: 2.27s
- Word Error Rate: 99.21%
- Transcript: Hello, I am Chef Chantier on site 26 Construction. Today, November 6, 2025, I did the inspection of building A. I am currently on the third floor, in front of the main entrance. I noticed three important cracks on the east wall. Cracks of about 15 to 20 cm in length. The state of the reinforced concrete seems worrying. I recommend a detailed inspection by a structural engineer. The sail casing also has defects. There are traces of water infiltration near the benches. The beams are in good health, in good condition, but it is necessary to check the stability before continuing the work. I will now inspect the fourth floor to check the condition of the slabs and beams. End of inspection of building A, third floor.
- Errors: substitutions=140, insertions=0, deletions=0
#### Error Details
- Replace: expected "Bonjour, je suis chef de chantier sur le" | actual "Hello, I am Chef Chantier on"
- Replace: expected "de Vinci" | actual "26"
- Replace: expected "Aujourd'hui, le six novembre deux mille vingt-cinq, je fais l'inspection du bâtiment" | actual "Today, November 6, 2025, I did the inspection of building"
- Replace: expected "Je me trouve actuellement au troisième étage, devant l'entrée principale. J'ai remarqué trois fissures importantes sur le mur est. Les fissures mesurent environ quinze à vingt centimètres de longueur. L'état du béton armé semble préoccupant. Je recommande une" | actual "I am currently on the third floor, in front of the main entrance. I noticed three important cracks on the east wall. Cracks of about 15 to 20 cm in length. The state of the reinforced concrete seems worrying. I recommend a detailed"
- Replace: expected "détaillée par un ingénieur structures. Le coffrage du voile présente également des défauts. Il y" | actual "by"
- Replace: expected "des" | actual "structural engineer. The sail casing also has defects. There are"
- Replace: expected "d'infiltration d'eau près des banches. Les étais sont en bon état, mais il faut vérifier la stabilité avant de poursuivre les travaux. Je vais maintenant inspecter le quatrième étage pour vérifier l'état des dalles et des poutres. Fin de l'inspection du bâtiment" | actual "of water infiltration near the benches. The beams are in good health, in good condition, but it is necessary to check the stability before continuing the work. I will now inspect the fourth floor to check the condition of the slabs and beams. End of inspection of building"
- Replace: expected "troisième étage." | actual "third floor."

### Model: gpt-audio
- Status: ✅ Success
- Latency: 3.44s
- Word Error Rate: 18.90%
- Transcript: Bonjour, je suis chef de chantier sur le site de Vinci Construction. Aujourd’hui, le 6 novembre 2025, j’ai fait une inspection du bâtiment A. Je me trouve actuellement au troisième étage, devant l’entrée principale. J’ai remarqué trois fissures importantes sur le mur Est. Les fissures mesurent environ 15 à 20 centimètres de longueur. L’état du béton armé semble préoccupant. Je recommande une inspection détaillée par un ingénieur structure. Le coffrage de voile présente également des défauts : il y a des traces d’infiltration d’eau près des banches. Les étais sont en bon état, mais il faut vérifier la stabilité avant de poursuivre les travaux. Je vais maintenant inspecter le quatrième étage pour vérifier l’état des dalles et des poutres. Fin d’inspection du bâtiment A, troisième étage.
- Errors: substitutions=24, insertions=0, deletions=0
#### Error Details
- Replace: expected "Aujourd'hui," | actual "Aujourd’hui,"
- Replace: expected "six" | actual "6"
- Replace: expected "deux mille vingt-cinq, je fais l'inspection" | actual "2025, j’ai fait une inspection"
- Replace: expected "l'entrée" | actual "l’entrée"
- Replace: expected "J'ai" | actual "J’ai"
- Replace: expected "est." | actual "Est."
- Replace: expected "quinze" | actual "15"
- Replace: expected "vingt" | actual "20"
- Replace: expected "L'état" | actual "L’état"
- Replace: expected "structures." | actual "structure."
- Replace: expected "du" | actual "de"
- Replace: expected "défauts. Il" | actual "défauts : il"
- Replace: expected "d'infiltration d'eau" | actual "d’infiltration d’eau"
- Replace: expected "l'état" | actual "l’état"
- Replace: expected "de l'inspection" | actual "d’inspection"

### Model: gpt-audio-mini
- Status: ✅ Success
- Latency: 3.16s
- Word Error Rate: 21.26%
- Transcript: Bonjour, je suis chargé chantier sur le site de Vinci Construction. Aujourd'hui, le 6 novembre 2025, j'ai fait une inspection du bâtiment A. Je me trouve actuellement en 3e étage, devant l'entrée principale. J'ai remarqué trois tirs importants sur le mur Est, des fissures mesures environ 15 à 20 cm de longueur. L'état du béton armé semble préoccupant. Je recommande une inspection détaillée par un ingénieur structure. Le coffrage de voiles présente également des défauts. Il y a des traces d'infiltration d'eau près des banches. Les étés sont en bon état, mais il faut vérifier la stabilité avant de poursuivre les travaux. Je vais maintenant inspecter le 4e étage pour vérifier l'état des dalles et des poutres. Fin d'inspection du bâtiment A, 3e étage.
- Errors: substitutions=27, insertions=0, deletions=0
#### Error Details
- Replace: expected "chef de" | actual "chargé"
- Replace: expected "six" | actual "6"
- Replace: expected "deux mille vingt-cinq, je fais l'inspection" | actual "2025, j'ai fait une inspection"
- Replace: expected "au troisième" | actual "en 3e"
- Replace: expected "fissures importantes" | actual "tirs importants"
- Replace: expected "est. Les" | actual "Est, des"
- Replace: expected "mesurent" | actual "mesures"
- Replace: expected "quinze" | actual "15"
- Replace: expected "vingt centimètres" | actual "20 cm"
- Replace: expected "structures." | actual "structure."
- Replace: expected "du voile" | actual "de voiles"
- Replace: expected "étais" | actual "étés"
- Replace: expected "quatrième" | actual "4e"
- Replace: expected "de l'inspection" | actual "d'inspection"
- Replace: expected "troisième" | actual "3e"

### Model: gpt-4o-audio-preview
- Status: ✅ Success
- Latency: 2.44s
- Word Error Rate: 14.96%
- Transcript: Bonjour, je suis en chantier sur le site de Vinci Construction. Aujourd'hui, le 6 novembre 2023, j'ai fait une inspection du bâtiment A. Je me trouve actuellement au troisième étage, devant l'entrée principale. J'ai remarqué trois fissures importantes sur le mur est, des fissures mesurant environ 15 à 20 centimètres de longueur. L'état du béton armé semble préoccupant. Je recommande une inspection détaillée par un ingénieur structure. Le coffrage de voile présente également des défauts. Il y a des traces d'infiltration d'eau près des banches. Les étais sont en bon état, mais il faut vérifier leur stabilité avant de poursuivre les travaux. Je vais maintenant inspecter le quatrième étage pour vérifier l'état des dalles et des poutres. Fin d'inspection du bâtiment A, troisième étage.
- Errors: substitutions=19, insertions=0, deletions=0
#### Error Details
- Replace: expected "chef de" | actual "en"
- Replace: expected "six" | actual "6"
- Replace: expected "deux mille vingt-cinq, je fais l'inspection" | actual "2023, j'ai fait une inspection"
- Replace: expected "est. Les" | actual "est, des"
- Replace: expected "mesurent" | actual "mesurant"
- Replace: expected "quinze" | actual "15"
- Replace: expected "vingt" | actual "20"
- Replace: expected "structures." | actual "structure."
- Replace: expected "du" | actual "de"
- Replace: expected "la" | actual "leur"
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

### Model: whisper
- Status: ❌ Failed
- Error: `{"error":{"code":"RateLimitReached","message": "Your requests to whisper for whisper in Sweden Central have exceeded the call rate limit for your current AIServices S0 pricing tier. This request was for Audio_Translations under Azure OpenAI API version 2024-06-01. Please retry after 14 seconds. To increase your default rate limit, visit: https://aka.ms/oai/quotaincrease."}}`

### Model: gpt-audio
- Status: ✅ Success
- Latency: 11.48s
- Word Error Rate: 32.84%
- Transcript: Rapport de la fin de journée – Mercredi 6 novembre 2025. Bonjour, je suis chef de chantier. Voici le compte-rendu complet de la journée sur le chantier de Vinci Construction, projet résidentiel « Les Jardins de l’Ouest ».

Partie 1 – Avancement des travaux : Ce matin nous avons terminé le coulage de la dalle du troisième étage du bâtiment A. Le volume du béton coulé est de 75 m³. La coulée a commencé à 7 h 30 et s’est terminée à 11 h 15. L’équipe de maçonnerie a monté 3 mètres linéaires de voiles au quatrième étage, le ferraillage à préparer et a intégré son problème. La géométrie est conforme au plan. Les électriciens ont achevé le passage des gaines dans les refends du deuxième étage, reste à faire le câblage prévu pour la semaine prochaine. La plomberie du premier étage est terminée à 90 %, les raccordements aux colonnes montantes sont faits, il reste les finitions dans les salles de bain.

Partie 2 – Livraisons et approvisionnement : Nous avons reçu ce matin la livraison de 15 palettes de parpaings pour le bâtiment B. La qualité est conforme, stockage organisé à proximité de la zone de travail. La livraison des menuiseries extérieures, prévue aujourd’hui, est reportée à vendredi, le fournisseur étant à un problème logistique. Impact mineur sur le planning général. Les banches métalliques louées dans le bâtiment C sont arrivées hier soir. L’équipe coffreur commence le montage demain matin.

Partie 3 – Effectif et ressources : 15 ouvriers présents aujourd’hui, 3 absents (1 pour congé maladie, 2 pour formation sécurité obligatoire). La grue à tour numéro 2 a été réparée et elle est de nouveau opérationnelle depuis 14 h. Le nouveau chef d’équipe, M. Martin, a pris ses fonctions ce matin, intégration en cours, il sera autonome d’ici deux semaines.

Partie 4 – Sécurité et qualité : Aucun accident aujourd’hui, le taux d’incidents reste à zéro depuis 15 jours. Visite surprise de l’inspecteur de travail à 10 h : tout était conforme, aucune remarque ni observation, très satisfaisant. Le contrôle qualité du béton : 3 éprouvettes prélevées ce matin lors de la coulée, résultat attendu dans 28 jours. Petit incident : un ouvrier a oublié son harnais de sécurité, appel à l’ordre immédiat, formation de sensibilisation prévue vendredi pour toute l’équipe.

Partie 5 – Points de vigilance : Météo : prévision de pluie pour demain après-midi, prévoir bâches de protection pour les zones en cours de bétonnage. Le planning est serré sur le bâtiment A, il faut terminer le gros œuvre avant la fin du mois. Nous sommes dans les temps mais aucune marge de manœuvre. Problème de coordination avec les façadiers : réunion prévue demain matin à 8 h pour ajuster les interfaces.

Partie 6 – Actions pour demain : Continuer le montage des voiles au quatrième étage du bâtiment A, démarrage du coffrage des poteaux du rez-de-chaussée du bâtiment B. Organiser le coulé du radier du bâtiment C si la météo le permet. Réceptionner et contrôler la livraison de 50 tonnes d’armatures prévue à 9 h. Réunion de coordination à 8 h avec tous les sous-traitants.

Conclusion : Bonne journée dans l’ensemble, avancement conforme au planning, aucun retard significatif, tous les indicateurs sont au vert. Prochain rapport demain soir à la même heure. Bonne soirée à tous. Fin du rapport de fin de journée.
- Errors: substitutions=176, insertions=2, deletions=1
#### Error Details
- Insert: expected "" | actual "la"
- Replace: expected "journée, mercredi six" | actual "journée – Mercredi 6"
- Replace: expected "deux mille vingt-cinq." | actual "2025."
- Insert: expected "" | actual "«"
- Replace: expected "l'Ouest. PARTIE UN: AVANCEMENT DES TRAVAUX" | actual "l’Ouest ». Partie 1 – Avancement des travaux :"
- Replace: expected "matin," | actual "matin"
- Replace: expected "de" | actual "du"
- Replace: expected "soixante-quinze mètres cubes." | actual "75 m³."
- Replace: expected "sept heures trente et s'est" | actual "7 h 30 et s’est"
- Replace: expected "onze heures quinze. L'équipe" | actual "11 h 15. L’équipe"
- Replace: expected "trois" | actual "3"
- Replace: expected "étage. Le" | actual "étage, le"
- Replace: expected "préparé hier" | actual "à préparer et"
- Delete: expected "été" | actual ""
- Replace: expected "sans" | actual "son"
- Replace: expected "aux plans." | actual "au plan."
- Replace: expected "étage. Reste" | actual "étage, reste"
- Replace: expected "câblage," | actual "câblage"
- Replace: expected "quatre-vingt-dix pour cent. Les" | actual "90 %, les"
- Replace: expected "faits. Il" | actual "faits, il"
- Replace: expected "bains. PARTIE DEUX: LIVRAISONS ET APPROVISIONNEMENTS" | actual "bain. Partie 2 – Livraisons et approvisionnement :"
- Replace: expected "quinze" | actual "15"
- Replace: expected "conforme. Stockage" | actual "conforme, stockage"
- Replace: expected "extérieures" | actual "extérieures,"
- Replace: expected "aujourd'hui" | actual "aujourd’hui,"
- Replace: expected "vendredi. Le" | actual "vendredi, le"
- Replace: expected "a" | actual "étant à"
- Replace: expected "pour" | actual "dans"
- Replace: expected "L'équipe" | actual "L’équipe"
- Replace: expected "PARTIE TROIS: EFFECTIFS ET RESSOURCES Quinze" | actual "Partie 3 – Effectif et ressources : 15"
- Replace: expected "aujourd'hui. Trois absents: un" | actual "aujourd’hui, 3 absents (1"
- Replace: expected "deux" | actual "2"
- Replace: expected "obligatoire." | actual "obligatoire)."
- Replace: expected "deux" | actual "2"
- Replace: expected "réparée. Elle" | actual "réparée et elle"
- Replace: expected "quatorze heures." | actual "14 h."
- Replace: expected "d'équipe, Monsieur" | actual "d’équipe, M."
- Replace: expected "matin. Intégration" | actual "matin, intégration"
- Replace: expected "d'ici" | actual "d’ici"
- Replace: expected "PARTIE QUATRE: SÉCURITÉ ET QUALITÉ" | actual "Partie 4 – Sécurité et qualité :"
- Replace: expected "aujourd'hui. Le" | actual "aujourd’hui, le"
- Replace: expected "d'incidents" | actual "d’incidents"
- Replace: expected "quinze" | actual "15"
- Replace: expected "l'inspecteur du" | actual "l’inspecteur de"
- Replace: expected "dix heures. Tout" | actual "10 h : tout"
- Replace: expected "conforme. Aucune" | actual "conforme, aucune"
- Replace: expected "observation. Très" | actual "observation, très"
- Replace: expected "béton: trois" | actual "béton : 3"
- Replace: expected "coulée. Résultats attendus" | actual "coulée, résultat attendu"
- Replace: expected "vingt-huit" | actual "28"
- Replace: expected "incident:" | actual "incident :"
- Replace: expected "sécurité. Rappel à l'ordre immédiat. Formation" | actual "sécurité, appel à l’ordre immédiat, formation"
- Replace: expected "l'équipe. PARTIE CINQ: POINTS DE VIGILANCE Météo: prévisions" | actual "l’équipe. Partie 5 – Points de vigilance : Météo : prévision"
- Replace: expected "après-midi. Prévoir" | actual "après-midi, prévoir"
- Replace: expected "A. Il" | actual "A, il"
- Replace: expected "temps," | actual "temps"
- Replace: expected "façadiers. Réunion" | actual "façadiers : réunion"
- Replace: expected "huit heures" | actual "8 h"
- Replace: expected "PARTIE SIX: ACTIONS POUR DEMAIN" | actual "Partie 6 – Actions pour demain :"
- Replace: expected "A. Démarrer le" | actual "A, démarrage du"
- Replace: expected "la coulée" | actual "le coulé"
- Replace: expected "C," | actual "C"
- Replace: expected "cinquante" | actual "50"
- Replace: expected "d'armatures" | actual "d’armatures"
- Replace: expected "neuf heures." | actual "9 h."
- Replace: expected "huit heures" | actual "8 h"
- Replace: expected "CONCLUSION" | actual "Conclusion :"
- Replace: expected "l'ensemble. Avancement" | actual "l’ensemble, avancement"
- Replace: expected "planning. Aucun" | actual "planning, aucun"
- Replace: expected "significatif. Tous" | actual "significatif, tous"

### Model: gpt-audio-mini
- Status: ✅ Success
- Latency: 8.59s
- Word Error Rate: 20.78%
- Transcript: Rapport de fin de journée, mercredi 6 novembre 2025. Bonjour, je suis chef de chantier. Voici le compte-rendu complet de la journée sur le chantier de Vinci Construction, projet résidentiel, les Jardins de l'Ouest. Partie 1. Avancement des travaux. Ce matin, nous avons terminé le coulage de la dalle du troisième étage du bâtiment A. Le volume du béton coulé est de 75 m³. La coulée a commencé à 7h30 et s'est terminée à 11h15. L'équipe de maçonnerie a monté 3 m linéaires de voiles au quatrième étage. Le ferraillage a préparé et intégré son problème. La géométrie est conforme au plan. Les électriciens ont achevé le passage des gaines dans les refonds du deuxième étage. Reste à faire le câblage prévu pour la semaine prochaine. La plomberie du premier étage est terminée à 90 %. Les raccordements aux colonnes montantes sont faits. Il reste les finitions dans les salles de bain. Partie 2. Livraison et approvisionnements. Nous avons reçu ce matin la livraison de 15 palettes de parpaings pour le bâtiment B. La qualité est conforme. Stockage organisé à proximité de la zone de travail. La livraison des menuiseries extérieures, prévue aujourd'hui, est reportée à vendredi. Le fournisseur a un problème logistique. Impact mineur sur le planning général. Les banches métalliques louées dans le bâtiment C sont arrivées hier soir. L'équipe coffreur commence le montage demain matin. Partie 3. Effectifs et ressources. 15 ouvriers présents aujourd'hui, 3 absents. 1 pour congé maladie, 2 pour formation sécurité obligatoire. La grue, à tour numéro 2, a été réparée. Elle est de nouveau opérationnelle depuis 14h. Le nouveau chef d'équipe, M. Martin, a pris ses fonctions ce matin. Intégration en cours. Il sera autonome d'ici deux semaines. Partie 4. Sécurité et qualité. Aucun accident aujourd'hui. Le taux d'incidents reste à zéro depuis 15 jours. Visite surprise de l'inspecteur de travail à 10h. Tout était conforme. Aucune remarque ni observation. Très satisfaisant. Le contrôle qualité du béton, 3 éprouvettes prélevées ce matin lors de la coulée. Résultat attendu dans 28 jours. Petit incident. Un ouvrier a oublié son harnais de sécurité. Appel à l'ordre immédiat. Formation de sensibilisation prévue vendredi pour toute l'équipe. Partie 5. Point de vigilance. Météo. Prévision de pluie pour demain après-midi. Prévoir bâche de protection pour les zones en cours de bétonnage. Le planning est serré sur le bâtiment A. Il faut terminer le gros œuvre avant la fin du mois. Nous sommes dans les temps, mais aucun marge de manoeuvre. Problème de coordination avec les façadiers. Réunion prévue demain matin à 8h pour ajuster les interfaces. Partie 6. Actions pour demain. Continuer le montage des voiles au quatrième étage du bâtiment A. Démarrage du coffrage des poteaux du rez-de-chaussée du bâtiment B. Organiser le coulé du radier du bâtiment C, si la météo le permet. Réceptionner et contrôler la livraison de 50 tonnes d'armature, prévu à 9h. Réunion de coordination à 8h avec tous les sous-traitants. Conclusion. Bonne journée dans l'ensemble. Avancements conformes au planning. Aucun retard significatif. Tous les indicateurs sont au vert. Prochain rapport demain soir, à la même heure. Bonne soirée à tous. Fin du rapport de fin de journée.
- Errors: substitutions=112, insertions=1, deletions=0
#### Error Details
- Replace: expected "six" | actual "6"
- Replace: expected "deux mille vingt-cinq." | actual "2025."
- Replace: expected "résidentiel Les" | actual "résidentiel, les"
- Replace: expected "PARTIE UN: AVANCEMENT DES TRAVAUX" | actual "Partie 1. Avancement des travaux."
- Replace: expected "de" | actual "du"
- Replace: expected "soixante-quinze mètres cubes." | actual "75 m³."
- Replace: expected "sept heures trente" | actual "7h30"
- Replace: expected "onze heures quinze." | actual "11h15."
- Replace: expected "trois mètres" | actual "3 m"
- Insert: expected "" | actual "a"
- Replace: expected "hier a été" | actual "et"
- Replace: expected "sans" | actual "son"
- Replace: expected "aux plans." | actual "au plan."
- Replace: expected "refends" | actual "refonds"
- Replace: expected "câblage," | actual "câblage"
- Replace: expected "quatre-vingt-dix pour cent." | actual "90 %."
- Replace: expected "bains. PARTIE DEUX: LIVRAISONS ET APPROVISIONNEMENTS" | actual "bain. Partie 2. Livraison et approvisionnements."
- Replace: expected "quinze" | actual "15"
- Replace: expected "extérieures" | actual "extérieures,"
- Replace: expected "aujourd'hui" | actual "aujourd'hui,"
- Replace: expected "pour" | actual "dans"
- Replace: expected "PARTIE TROIS: EFFECTIFS ET RESSOURCES Quinze" | actual "Partie 3. Effectifs et ressources. 15"
- Replace: expected "aujourd'hui. Trois absents: un" | actual "aujourd'hui, 3 absents. 1"
- Replace: expected "deux" | actual "2"
- Replace: expected "grue" | actual "grue,"
- Replace: expected "deux" | actual "2,"
- Replace: expected "quatorze heures." | actual "14h."
- Replace: expected "Monsieur" | actual "M."
- Replace: expected "cours, il" | actual "cours. Il"
- Replace: expected "PARTIE QUATRE: SÉCURITÉ ET QUALITÉ" | actual "Partie 4. Sécurité et qualité."
- Replace: expected "quinze" | actual "15"
- Replace: expected "du" | actual "de"
- Replace: expected "dix heures." | actual "10h."
- Replace: expected "béton: trois" | actual "béton, 3"
- Replace: expected "Résultats attendus" | actual "Résultat attendu"
- Replace: expected "vingt-huit" | actual "28"
- Replace: expected "incident: un" | actual "incident. Un"
- Replace: expected "Rappel" | actual "Appel"
- Replace: expected "PARTIE CINQ: POINTS DE VIGILANCE Météo: prévisions" | actual "Partie 5. Point de vigilance. Météo. Prévision"
- Replace: expected "bâches" | actual "bâche"
- Replace: expected "aucune" | actual "aucun"
- Replace: expected "manœuvre." | actual "manoeuvre."
- Replace: expected "huit heures" | actual "8h"
- Replace: expected "PARTIE SIX: ACTIONS POUR DEMAIN" | actual "Partie 6. Actions pour demain."
- Replace: expected "Démarrer le" | actual "Démarrage du"
- Replace: expected "la coulée" | actual "le coulé"
- Replace: expected "cinquante" | actual "50"
- Replace: expected "d'armatures prévue à neuf heures." | actual "d'armature, prévu à 9h."
- Replace: expected "huit heures" | actual "8h"
- Replace: expected "CONCLUSION" | actual "Conclusion."
- Replace: expected "Avancement conforme" | actual "Avancements conformes"
- Replace: expected "soir" | actual "soir,"

### Model: gpt-4o-audio-preview
- Status: ✅ Success
- Latency: 8.59s
- Word Error Rate: 24.30%
- Transcript: Rapport de la fin de journée, mercredi 6 novembre 2025. Bonjour, je suis chef de chantier. Voici le compte-rendu complet de la journée sur le chantier de Vinci Construction, projet résidentiel Les Jardins de l'Ouest. Partie 1 : Avancement des travaux. Ce matin, nous avons terminé le coulage de la dalle du troisième étage du bâtiment A. Le volume de béton coulé est de 75 mètres cubes. La coulée a commencé à 7h30 et s'est terminée à 11h15. L'équipe de maçonnerie a monté trois mètres linéaires de voile au quatrième étage. Le ferraillage a été intégré sans problème, la géométrie est conforme au plan. Les électriciens ont achevé le passage des gaines dans les refends du deuxième étage, reste à faire le câblage prévu pour la semaine prochaine. La plomberie du premier étage est terminée à 90%, les raccordements aux colonnes montantes sont faits, il reste les finitions dans les salles de bain. Partie 2 : Livraisons et approvisionnement. Nous avons reçu ce matin la livraison de quinze palettes de parpaings pour le bâtiment B. La qualité est conforme, stockage organisé à proximité de la zone de travail. La livraison des menuiseries extérieures prévue aujourd'hui est reportée à vendredi, le fournisseur ayant un problème logistique. Impact mineur sur le planning général. Les banches métalliques louées pour le bâtiment C sont arrivées hier soir, l'équipe coffreur commence le montage demain matin. Partie 3 : Effectif et ressources. Quinze ouvriers présents aujourd'hui, trois absents, un pour congé maladie, deux pour formation sécurité obligatoire. La grue à tour numéro deux a été réparée et est de nouveau opérationnelle depuis 14h. Le nouveau chef d'équipe, Monsieur Martin, a pris ses fonctions ce matin, intégration en cours, il sera autonome d'ici deux semaines. Partie 4 : Sécurité et qualité. Aucun accident aujourd'hui, le taux d'incident reste à zéro depuis quinze jours. Visite surprise de l'inspecteur du travail à 10h, tout était conforme, aucune remarque ni observation. Très satisfaisant. Le contrôle qualité du béton : trois éprouvettes prélevées ce matin lors de la coulée, résultat attendu dans 28 jours. Petit incident : un ouvrier a oublié son harnais de sécurité, appel à l'ordre immédiat, formation de sensibilisation prévue vendredi pour toute l'équipe. Partie 5 : Points de vigilance. Météo : prévision de pluie pour demain après-midi, prévoir bâches de protection pour les zones en cours de bétonnage. Le planning est serré sur le bâtiment A, il faut terminer le gros œuvre avant la fin du mois. Nous sommes dans les temps mais aucune marge de manœuvre. Problème de coordination avec les façadiers, réunion prévue demain matin à 8h pour ajuster les interfaces. Partie 6 : Actions pour demain. Continuer le montage des voiles au quatrième étage du bâtiment A. Démarrage du coffrage des poteaux du rez-de-chaussée du bâtiment B. Organiser le coulage du radier du bâtiment C si la météo le permet. Réceptionner et contrôler la livraison de 50 tonnes d'armatures prévue à 9h. Réunion de coordination à 8h avec tous les sous-traitants. Conclusion : Bonne journée dans l'ensemble, avancement conforme au planning, aucun retard significatif, tous les indicateurs sont au vert. Prochain rapport demain soir à la même heure. Bonne soirée à tous. Fin du rapport de fin de journée.
- Errors: substitutions=128, insertions=1, deletions=2
#### Error Details
- Insert: expected "" | actual "la"
- Replace: expected "six" | actual "6"
- Replace: expected "deux mille vingt-cinq." | actual "2025."
- Replace: expected "PARTIE UN: AVANCEMENT DES TRAVAUX" | actual "Partie 1 : Avancement des travaux."
- Replace: expected "soixante-quinze" | actual "75"
- Replace: expected "sept heures trente" | actual "7h30"
- Replace: expected "onze heures quinze." | actual "11h15."
- Replace: expected "voiles" | actual "voile"
- Delete: expected "préparé hier" | actual ""
- Replace: expected "problème. La" | actual "problème, la"
- Replace: expected "aux plans." | actual "au plan."
- Replace: expected "étage. Reste" | actual "étage, reste"
- Replace: expected "câblage," | actual "câblage"
- Replace: expected "quatre-vingt-dix pour cent. Les" | actual "90%, les"
- Replace: expected "faits. Il" | actual "faits, il"
- Replace: expected "bains. PARTIE DEUX: LIVRAISONS ET APPROVISIONNEMENTS" | actual "bain. Partie 2 : Livraisons et approvisionnement."
- Replace: expected "conforme. Stockage" | actual "conforme, stockage"
- Replace: expected "vendredi. Le" | actual "vendredi, le"
- Replace: expected "a" | actual "ayant"
- Replace: expected "soir. L'équipe" | actual "soir, l'équipe"
- Replace: expected "PARTIE TROIS: EFFECTIFS ET RESSOURCES" | actual "Partie 3 : Effectif et ressources."
- Replace: expected "aujourd'hui. Trois absents:" | actual "aujourd'hui, trois absents,"
- Replace: expected "réparée. Elle" | actual "réparée et"
- Replace: expected "quatorze heures." | actual "14h."
- Replace: expected "matin. Intégration" | actual "matin, intégration"
- Replace: expected "PARTIE QUATRE: SÉCURITÉ ET QUALITÉ" | actual "Partie 4 : Sécurité et qualité."
- Replace: expected "aujourd'hui. Le" | actual "aujourd'hui, le"
- Replace: expected "d'incidents" | actual "d'incident"
- Replace: expected "dix heures. Tout" | actual "10h, tout"
- Replace: expected "conforme. Aucune" | actual "conforme, aucune"
- Replace: expected "béton:" | actual "béton :"
- Replace: expected "coulée. Résultats attendus" | actual "coulée, résultat attendu"
- Replace: expected "vingt-huit" | actual "28"
- Replace: expected "incident:" | actual "incident :"
- Replace: expected "sécurité. Rappel" | actual "sécurité, appel"
- Replace: expected "immédiat. Formation" | actual "immédiat, formation"
- Replace: expected "PARTIE CINQ: POINTS DE VIGILANCE Météo: prévisions" | actual "Partie 5 : Points de vigilance. Météo : prévision"
- Replace: expected "après-midi. Prévoir" | actual "après-midi, prévoir"
- Replace: expected "A. Il" | actual "A, il"
- Replace: expected "temps," | actual "temps"
- Replace: expected "façadiers. Réunion" | actual "façadiers, réunion"
- Replace: expected "huit heures" | actual "8h"
- Replace: expected "PARTIE SIX: ACTIONS POUR DEMAIN" | actual "Partie 6 : Actions pour demain."
- Replace: expected "Démarrer le" | actual "Démarrage du"
- Replace: expected "la coulée" | actual "le coulage"
- Replace: expected "C," | actual "C"
- Replace: expected "cinquante" | actual "50"
- Replace: expected "neuf heures." | actual "9h."
- Replace: expected "huit heures" | actual "8h"
- Replace: expected "CONCLUSION" | actual "Conclusion :"
- Replace: expected "l'ensemble. Avancement" | actual "l'ensemble, avancement"
- Replace: expected "planning. Aucun" | actual "planning, aucun"
- Replace: expected "significatif. Tous" | actual "significatif, tous"

---
