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
- Latency: 3.52s
- Word Error Rate: 13.60%
- Transcript: Bonjour, je suis chef de chantier sur le site de Vinci Construction. Aujourd’hui, le 6 novembre 2025, je fais l’inspection du bâtiment A. Je me trouve actuellement au troisième étage devant l’entrée principale. J’ai remarqué trois fissures importantes sur le mur Est. Les fissures mesurent environ 15 à 20 centimètres de longueur. L’état du béton armé semble préoccupant. Je recommande une inspection détaillée par un ingénieur structure. Le coffrage du voile présente également des défauts, il y a des traces d’infiltration d’eau près des banches. Les étais sont en bon état, mais il faut vérifier la stabilité avant de poursuivre les travaux. Il faut maintenant inspecter le quatrième étage pour vérifier l’état des dalles et des poutres. Fin de l’inspection du bâtiment A, troisième étage.
- Errors: substitutions=17, insertions=0, deletions=0
#### Error Details
- Replace: expected "Aujourd'hui," | actual "Aujourd’hui,"
- Replace: expected "l'inspection" | actual "l’inspection"
- Replace: expected "étage," | actual "étage"
- Replace: expected "l'entrée" | actual "l’entrée"
- Replace: expected "J'ai" | actual "J’ai"
- Replace: expected "3" | actual "trois"
- Replace: expected "est." | actual "Est."
- Replace: expected "L'état" | actual "L’état"
- Replace: expected "structures." | actual "structure."
- Replace: expected "défauts. Il" | actual "défauts, il"
- Replace: expected "d'infiltration d'eau" | actual "d’infiltration d’eau"
- Replace: expected "Je vais" | actual "Il faut"
- Replace: expected "l'état" | actual "l’état"
- Replace: expected "l'inspection" | actual "l’inspection"
- Normalized Word Error Rate: 12.00%
- Normalized Reference: bonjour, je suis chef de chantier sur le site de vinci construction.

aujourd'hui, le 6 novembre 2025, je fais l'inspection du bâtiment a.

je me trouve actuellement au troisième étage, devant l'entrée principale.

j'ai remarqué 3 fissures importantes sur le mur est. les fissures mesurent environ 15 à 20 centimètres de longueur.

l'état du béton armé semble préoccupant. je recommande une inspection détaillée par un ingénieur structures.

le coffrage du voile présente également des défauts. il y a des traces d'infiltration d'eau près des banches.

les étais sont en bon état, mais il faut vérifier la stabilité avant de poursuivre les travaux.

je vais maintenant inspecter le quatrième étage pour vérifier l'état des dalles et des poutres.

fin de l'inspection du bâtiment a, troisième étage.
- Normalized Transcript: bonjour, je suis chef de chantier sur le site de vinci construction. aujourd’hui, le 6 novembre 2025, je fais l’inspection du bâtiment a. je me trouve actuellement au troisième étage devant l’entrée principale. j’ai remarqué trois fissures importantes sur le mur est. les fissures mesurent environ 15 à 20 centimètres de longueur. l’état du béton armé semble préoccupant. je recommande une inspection détaillée par un ingénieur structure. le coffrage du voile présente également des défauts, il y a des traces d’infiltration d’eau près des banches. les étais sont en bon état, mais il faut vérifier la stabilité avant de poursuivre les travaux. il faut maintenant inspecter le quatrième étage pour vérifier l’état des dalles et des poutres. fin de l’inspection du bâtiment a, troisième étage.
- Normalized Errors: substitutions=15, insertions=0, deletions=0
#### Normalized Error Details
- Replace: expected "aujourd'hui," | actual "aujourd’hui,"
- Replace: expected "l'inspection" | actual "l’inspection"
- Replace: expected "étage," | actual "étage"
- Replace: expected "l'entrée" | actual "l’entrée"
- Replace: expected "j'ai" | actual "j’ai"
- Replace: expected "3" | actual "trois"
- Replace: expected "l'état" | actual "l’état"
- Replace: expected "structures." | actual "structure."
- Replace: expected "défauts." | actual "défauts,"
- Replace: expected "d'infiltration d'eau" | actual "d’infiltration d’eau"
- Replace: expected "je vais" | actual "il faut"
- Replace: expected "l'état" | actual "l’état"
- Replace: expected "l'inspection" | actual "l’inspection"

### Model: gpt-audio-mini
- Status: ✅ Success
- Latency: 2.53s
- Word Error Rate: 8.00%
- Transcript: Bonjour, je suis chef de chantier sur le site de Vinci Construction. Aujourd'hui, le 6 novembre 2025, je fais l'inspection du bâtiment A. Je me trouve actuellement au troisième étage devant l'entrée principale. J'ai remarqué trois fissures importantes sur le mur Est. Les fissures mesurent environ 15 à 20 cm de longueur. L'état du béton armé semble préoccupant. Je recommande une inspection détaillée par un ingénieur structure. Le coffrage du voile présente également des défauts et il y a des traces d'infiltration d'eau près des banches. Les étais sont en bon état, mais il faut vérifier la stabilité avant de poursuivre les travaux. Il faut maintenant inspecter le quatrième étage pour vérifier l'état des dalles et des poutres. Fin de l'inspection du bâtiment A, troisième étage.
- Errors: substitutions=10, insertions=0, deletions=0
#### Error Details
- Replace: expected "étage," | actual "étage"
- Replace: expected "3" | actual "trois"
- Replace: expected "est." | actual "Est."
- Replace: expected "centimètres" | actual "cm"
- Replace: expected "structures." | actual "structure."
- Replace: expected "défauts. Il" | actual "défauts et il"
- Replace: expected "Je vais" | actual "Il faut"
- Normalized Word Error Rate: 6.40%
- Normalized Reference: bonjour, je suis chef de chantier sur le site de vinci construction.

aujourd'hui, le 6 novembre 2025, je fais l'inspection du bâtiment a.

je me trouve actuellement au troisième étage, devant l'entrée principale.

j'ai remarqué 3 fissures importantes sur le mur est. les fissures mesurent environ 15 à 20 centimètres de longueur.

l'état du béton armé semble préoccupant. je recommande une inspection détaillée par un ingénieur structures.

le coffrage du voile présente également des défauts. il y a des traces d'infiltration d'eau près des banches.

les étais sont en bon état, mais il faut vérifier la stabilité avant de poursuivre les travaux.

je vais maintenant inspecter le quatrième étage pour vérifier l'état des dalles et des poutres.

fin de l'inspection du bâtiment a, troisième étage.
- Normalized Transcript: bonjour, je suis chef de chantier sur le site de vinci construction. aujourd'hui, le 6 novembre 2025, je fais l'inspection du bâtiment a. je me trouve actuellement au troisième étage devant l'entrée principale. j'ai remarqué trois fissures importantes sur le mur est. les fissures mesurent environ 15 à 20 cm de longueur. l'état du béton armé semble préoccupant. je recommande une inspection détaillée par un ingénieur structure. le coffrage du voile présente également des défauts et il y a des traces d'infiltration d'eau près des banches. les étais sont en bon état, mais il faut vérifier la stabilité avant de poursuivre les travaux. il faut maintenant inspecter le quatrième étage pour vérifier l'état des dalles et des poutres. fin de l'inspection du bâtiment a, troisième étage.
- Normalized Errors: substitutions=8, insertions=0, deletions=0
#### Normalized Error Details
- Replace: expected "étage," | actual "étage"
- Replace: expected "3" | actual "trois"
- Replace: expected "centimètres" | actual "cm"
- Replace: expected "structures." | actual "structure."
- Replace: expected "défauts." | actual "défauts et"
- Replace: expected "je vais" | actual "il faut"

### Model: gpt-4o-audio-preview
- Status: ✅ Success
- Latency: 2.59s
- Word Error Rate: 5.60%
- Transcript: Bonjour, je suis chef de chantier sur le site de Vinci Construction. Aujourd'hui, le 6 novembre 2025, je fais l'inspection du bâtiment A. Je me trouve actuellement au troisième étage, devant l'entrée principale. J'ai remarqué trois fissures importantes sur le mur est. Les fissures mesurent environ 15 à 20 centimètres de longueur. L'état du béton armé semble préoccupant. Je recommande une inspection détaillée par un ingénieur structure. Le coffrage du voile présente également des défauts; il y a des traces d'infiltration d'eau près des banche. Les étais sont en bon état, mais il faut vérifier la stabilité avant de poursuivre les travaux. Il faut maintenant inspecter le quatrième étage pour vérifier l'état des dalles et des poutres. Fin de l'inspection du bâtiment A, troisième étage.
- Errors: substitutions=7, insertions=0, deletions=0
#### Error Details
- Replace: expected "3" | actual "trois"
- Replace: expected "structures." | actual "structure."
- Replace: expected "défauts. Il" | actual "défauts; il"
- Replace: expected "banches." | actual "banche."
- Replace: expected "Je vais" | actual "Il faut"
- Normalized Word Error Rate: 4.80%
- Normalized Reference: bonjour, je suis chef de chantier sur le site de vinci construction.

aujourd'hui, le 6 novembre 2025, je fais l'inspection du bâtiment a.

je me trouve actuellement au troisième étage, devant l'entrée principale.

j'ai remarqué 3 fissures importantes sur le mur est. les fissures mesurent environ 15 à 20 centimètres de longueur.

l'état du béton armé semble préoccupant. je recommande une inspection détaillée par un ingénieur structures.

le coffrage du voile présente également des défauts. il y a des traces d'infiltration d'eau près des banches.

les étais sont en bon état, mais il faut vérifier la stabilité avant de poursuivre les travaux.

je vais maintenant inspecter le quatrième étage pour vérifier l'état des dalles et des poutres.

fin de l'inspection du bâtiment a, troisième étage.
- Normalized Transcript: bonjour, je suis chef de chantier sur le site de vinci construction. aujourd'hui, le 6 novembre 2025, je fais l'inspection du bâtiment a. je me trouve actuellement au troisième étage, devant l'entrée principale. j'ai remarqué trois fissures importantes sur le mur est. les fissures mesurent environ 15 à 20 centimètres de longueur. l'état du béton armé semble préoccupant. je recommande une inspection détaillée par un ingénieur structure. le coffrage du voile présente également des défauts; il y a des traces d'infiltration d'eau près des banche. les étais sont en bon état, mais il faut vérifier la stabilité avant de poursuivre les travaux. il faut maintenant inspecter le quatrième étage pour vérifier l'état des dalles et des poutres. fin de l'inspection du bâtiment a, troisième étage.
- Normalized Errors: substitutions=6, insertions=0, deletions=0
#### Normalized Error Details
- Replace: expected "3" | actual "trois"
- Replace: expected "structures." | actual "structure."
- Replace: expected "défauts." | actual "défauts;"
- Replace: expected "banches." | actual "banche."
- Replace: expected "je vais" | actual "il faut"

---
