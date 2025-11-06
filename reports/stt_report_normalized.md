# Speech-to-Text Benchmark Report

Generated from 1 audio samples.

## audio_01_clean.wav
- Audio file: `data/processed/audio_01_clean.wav`
- Reference transcript: `data/processed/audio_01_reference.txt`
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
- Latency: 4.19s
- Word Error Rate: 13.60%
- Transcript: Bonjour, je suis chef de chantier sur le site de Vinci Construction. Aujourd’hui le 6 novembre 2025, je fais l’inspection du bâtiment A. Je me trouve actuellement au troisième étage devant l’entrée principale. J’ai remarqué trois fissures importantes sur le mur est. Les fissures mesurent environ 15 à 20 centimètres de longueur. L’état du béton armé semble préoccupant. Je recommande une inspection détaillée par un ingénieur structure. Le coffrage du voile présente également des défauts, il y a des traces d’infiltration d’eau près des banches. Les étais sont en bon état mais il faut vérifier la stabilité avant de poursuivre les travaux. Il faut maintenant inspecter le quatrième étage pour vérifier l’état des dalles et des poutres. Fin de l’inspection du bâtiment A, troisième étage.
- Errors: substitutions=17, insertions=0, deletions=0
#### Error Details
- Replace: expected "Aujourd'hui," | actual "Aujourd’hui"
- Replace: expected "l'inspection" | actual "l’inspection"
- Replace: expected "étage," | actual "étage"
- Replace: expected "l'entrée" | actual "l’entrée"
- Replace: expected "J'ai" | actual "J’ai"
- Replace: expected "3" | actual "trois"
- Replace: expected "L'état" | actual "L’état"
- Replace: expected "structures." | actual "structure."
- Replace: expected "défauts. Il" | actual "défauts, il"
- Replace: expected "d'infiltration d'eau" | actual "d’infiltration d’eau"
- Replace: expected "état," | actual "état"
- Replace: expected "Je vais" | actual "Il faut"
- Replace: expected "l'état" | actual "l’état"
- Replace: expected "l'inspection" | actual "l’inspection"
- Normalized Word Error Rate: 3.20%
- Normalized Reference: bonjour je suis chef de chantier sur le site de vinci construction aujourd'hui le 6 novembre 2025, je fais l'inspection du bâtiment a je me trouve actuellement au troisième étage devant l'entrée principale j'ai remarqué 3 fissures importantes sur le mur est les fissures mesurent environ 15 à 20 centimètres de longueur l'état du béton armé semble préoccupant je recommande une inspection détaillée par un ingénieur structures le coffrage du voile présente également des défauts il y a des traces d'infiltration d'eau près des banches les étais sont en bon état mais il faut vérifier la stabilité avant de poursuivre les travaux je vais maintenant inspecter le quatrième étage pour vérifier l'état des dalles et des poutres fin de l'inspection du bâtiment a troisième étage
- Normalized Transcript: bonjour je suis chef de chantier sur le site de vinci construction aujourd'hui le 6 novembre 2025, je fais l'inspection du bâtiment a je me trouve actuellement au troisième étage devant l'entrée principale j'ai remarqué trois fissures importantes sur le mur est les fissures mesurent environ 15 à 20 centimètres de longueur l'état du béton armé semble préoccupant je recommande une inspection détaillée par un ingénieur structure le coffrage du voile présente également des défauts il y a des traces d'infiltration d'eau près des banches les étais sont en bon état mais il faut vérifier la stabilité avant de poursuivre les travaux il faut maintenant inspecter le quatrième étage pour vérifier l'état des dalles et des poutres fin de l'inspection du bâtiment a troisième étage
- Normalized Errors: substitutions=4, insertions=0, deletions=0
#### Normalized Error Details
- Replace: expected "3" | actual "trois"
- Replace: expected "structures" | actual "structure"
- Replace: expected "je vais" | actual "il faut"

### Model: gpt-audio-mini
- Status: ✅ Success
- Latency: 3.10s
- Word Error Rate: 7.20%
- Transcript: Bonjour, je suis chef de chantier sur le site de Vinci Construction. Aujourd'hui, le 6 novembre 2025, je fais l'inspection du bâtiment A. Je me trouve actuellement au troisième étage, devant l'entrée principale. J'ai remarqué trois fissures importantes sur le mur est. Les fissures mesurent environ 15 à 20 cm de longueur. L'état du béton armé semble préoccupant. Je recommande une inspection détaillée par un ingénieur structure. Le coffrage du voile présente également des défauts et il y a des traces d'infiltration d'eau près des manches. Les étais sont en bon état, mais il faut vérifier la stabilité avant de poursuivre les travaux. Il faut maintenant inspecter le quatrième étage pour vérifier l'état des dalles et des poutres. Fin de l'inspection du bâtiment A, troisième étage.
- Errors: substitutions=9, insertions=0, deletions=0
#### Error Details
- Replace: expected "3" | actual "trois"
- Replace: expected "centimètres" | actual "cm"
- Replace: expected "structures." | actual "structure."
- Replace: expected "défauts. Il" | actual "défauts et il"
- Replace: expected "banches." | actual "manches."
- Replace: expected "Je vais" | actual "Il faut"
- Normalized Word Error Rate: 5.60%
- Normalized Reference: bonjour je suis chef de chantier sur le site de vinci construction aujourd'hui le 6 novembre 2025, je fais l'inspection du bâtiment a je me trouve actuellement au troisième étage devant l'entrée principale j'ai remarqué 3 fissures importantes sur le mur est les fissures mesurent environ 15 à 20 centimètres de longueur l'état du béton armé semble préoccupant je recommande une inspection détaillée par un ingénieur structures le coffrage du voile présente également des défauts il y a des traces d'infiltration d'eau près des banches les étais sont en bon état mais il faut vérifier la stabilité avant de poursuivre les travaux je vais maintenant inspecter le quatrième étage pour vérifier l'état des dalles et des poutres fin de l'inspection du bâtiment a troisième étage
- Normalized Transcript: bonjour je suis chef de chantier sur le site de vinci construction aujourd'hui le 6 novembre 2025, je fais l'inspection du bâtiment a je me trouve actuellement au troisième étage devant l'entrée principale j'ai remarqué trois fissures importantes sur le mur est les fissures mesurent environ 15 à 20 cm de longueur l'état du béton armé semble préoccupant je recommande une inspection détaillée par un ingénieur structure le coffrage du voile présente également des défauts et il y a des traces d'infiltration d'eau près des manches les étais sont en bon état mais il faut vérifier la stabilité avant de poursuivre les travaux il faut maintenant inspecter le quatrième étage pour vérifier l'état des dalles et des poutres fin de l'inspection du bâtiment a troisième étage
- Normalized Errors: substitutions=6, insertions=1, deletions=0
#### Normalized Error Details
- Replace: expected "3" | actual "trois"
- Replace: expected "centimètres" | actual "cm"
- Replace: expected "structures" | actual "structure"
- Insert: expected "" | actual "et"
- Replace: expected "banches" | actual "manches"
- Replace: expected "je vais" | actual "il faut"

### Model: gpt-4o-audio-preview
- Status: ✅ Success
- Latency: 2.80s
- Word Error Rate: 10.40%
- Transcript: Bonjour, je suis chef de chantier sur le site de Vinci Construction. Aujourd'hui, le 6 novembre 2023, je fais l'inspection du bâtiment A. Je me trouve actuellement au troisième étage devant l'entrée principale. J'ai remarqué trois fissures importantes sur le mur est. Les fissures mesurent environ quinze à vingt centimètres de longueur. L'état du béton armé semble préoccupant, je recommande une inspection détaillée par un ingénieur structure. Le coffrage du voile présente également des défauts et il y a des traces d'infiltration d'eau près des banches. Les étais sont en bon état, mais il faut vérifier la stabilité avant de poursuivre les travaux. Il faut maintenant inspecter le quatrième étage pour vérifier l'état des dalles et des poutres. Fin de l'inspection du bâtiment A, troisième étage.
- Errors: substitutions=13, insertions=0, deletions=0
#### Error Details
- Replace: expected "2025," | actual "2023,"
- Replace: expected "étage," | actual "étage"
- Replace: expected "3" | actual "trois"
- Replace: expected "15" | actual "quinze"
- Replace: expected "20" | actual "vingt"
- Replace: expected "préoccupant. Je" | actual "préoccupant, je"
- Replace: expected "structures." | actual "structure."
- Replace: expected "défauts. Il" | actual "défauts et il"
- Replace: expected "Je vais" | actual "Il faut"
- Normalized Word Error Rate: 4.80%
- Normalized Reference: bonjour je suis chef de chantier sur le site de vinci construction aujourd'hui le 6 novembre 2025, je fais l'inspection du bâtiment a je me trouve actuellement au troisième étage devant l'entrée principale j'ai remarqué 3 fissures importantes sur le mur est les fissures mesurent environ 15 à 20 centimètres de longueur l'état du béton armé semble préoccupant je recommande une inspection détaillée par un ingénieur structures le coffrage du voile présente également des défauts il y a des traces d'infiltration d'eau près des banches les étais sont en bon état mais il faut vérifier la stabilité avant de poursuivre les travaux je vais maintenant inspecter le quatrième étage pour vérifier l'état des dalles et des poutres fin de l'inspection du bâtiment a troisième étage
- Normalized Transcript: bonjour je suis chef de chantier sur le site de vinci construction aujourd'hui le 6 novembre 2023, je fais l'inspection du bâtiment a je me trouve actuellement au troisième étage devant l'entrée principale j'ai remarqué trois fissures importantes sur le mur est les fissures mesurent environ 15 à 20 centimètres de longueur l'état du béton armé semble préoccupant je recommande une inspection détaillée par un ingénieur structure le coffrage du voile présente également des défauts et il y a des traces d'infiltration d'eau près des banches les étais sont en bon état mais il faut vérifier la stabilité avant de poursuivre les travaux il faut maintenant inspecter le quatrième étage pour vérifier l'état des dalles et des poutres fin de l'inspection du bâtiment a troisième étage
- Normalized Errors: substitutions=5, insertions=1, deletions=0
#### Normalized Error Details
- Replace: expected "2025," | actual "2023,"
- Replace: expected "3" | actual "trois"
- Replace: expected "structures" | actual "structure"
- Insert: expected "" | actual "et"
- Replace: expected "je vais" | actual "il faut"

---
