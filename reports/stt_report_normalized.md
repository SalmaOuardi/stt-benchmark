# Speech-to-Text Model Benchmark Report

## Executive Summary

**Test Configuration:**
- Number of audio samples: 1
- Evaluation metric: Word Error Rate (WER)
- Normalization: Disabled (raw WER calculation)

### Model Performance Comparison

| Model | Avg WER | Min WER | Max WER | Avg Latency | Total Errors | Status |
|-------|---------|---------|---------|-------------|--------------|--------|
| gpt-4o-mini-transcribe | 0.00% | 0.00% | 0.00% | 1.93s | 0 | ✅ |
| gpt-4o-transcribe | 2.60% | 2.60% | 2.60% | 1.95s | 2 | ✅ |
| gpt-4o-audio-preview | 3.90% | 3.90% | 3.90% | 2.39s | 3 | ✅ |
| gpt-audio | 9.09% | 9.09% | 9.09% | 2.55s | 7 | ✅ |
| gpt-audio-mini | 100.00% | 100.00% | 100.00% | 6.79s | 77 | ✅ |

### 🏆 Best Model: **gpt-4o-mini-transcribe**
- Average WER: **0.00%**
- Average Latency: **1.93s**
- Total Errors: **0**

### Error Type Breakdown

| Model | Substitutions | Insertions | Deletions | Total |
|-------|---------------|------------|-----------|-------|
| gpt-4o-mini-transcribe | 0 | 0 | 0 | 0 |
| gpt-4o-transcribe | 2 | 0 | 0 | 2 |
| gpt-4o-audio-preview | 3 | 0 | 0 | 3 |
| gpt-audio | 7 | 0 | 0 | 7 |
| gpt-audio-mini | 77 | 0 | 0 | 77 |

---

## Detailed Results by Audio Sample

### Audio Sample: audio_clean.wav

**Reference Text:**
> Donc aujourd'hui le 6 novembre à 16h35, on vient de découvrir un réseau non prévu sur les plans. J'ai mis en arrêt immédiat les travaux sur la zone concernée. Avec les gars, on met en sécurité le périmètre et on interdit tout accès dans la zone. Il faudra prévoir avec toi une solution et un plan d'action. Mais l'idée c'est d'avoir aucune reprise de travaux avant l'identification complète du réseau et la validation de la procédure ensemble.

**File Paths:**
- Audio: `data/off/processed/audio_clean.wav`
- Reference: `data/off/processed/audio_clean_reference.txt`

**Model Performance:**

| Model | WER | Latency | Sub | Ins | Del | Status |
|-------|-----|---------|-----|-----|-----|--------|
| gpt-audio | 9.09% | 2.55s | 7 | 0 | 0 | ✅ |
| gpt-audio-mini | 100.00% | 6.79s | 77 | 0 | 0 | ✅ |
| gpt-4o-transcribe | 2.60% | 1.95s | 2 | 0 | 0 | ✅ |
| gpt-4o-mini-transcribe | 0.00% | 1.93s | 0 | 0 | 0 | ✅ |
| gpt-4o-audio-preview | 3.90% | 2.39s | 3 | 0 | 0 | ✅ |

**Detailed Transcripts:**

#### gpt-audio
**Transcript:**
```
Donc aujourd’hui le 6 novembre à 16h35, on vient de découvrir un réseau non prévu sur les plans. J’ai mis en arrêt immédiat les travaux sur la zone concernée. Avec les gars, on met en sécurité le périmètre et on interdit tout accès dans la zone. Il faudra prévoir avec toi une solution et un plan d’action. Mais l’idée c’est d’avoir aucune reprise de travaux avant l’identification complète du réseau et la validation de la procédure ensemble.
```

**Error Analysis (5 errors):**
- **Replace:** Expected `aujourd'hui` → Got `aujourd’hui`
- **Replace:** Expected `j'ai` → Got `j’ai`
- **Replace:** Expected `d'action.` → Got `d’action.`
- **Replace:** Expected `l'idée c'est d'avoir` → Got `l’idée c’est d’avoir`
- **Replace:** Expected `l'identification` → Got `l’identification`

#### gpt-audio-mini
**Transcript:**
```
Thank you for the clarification. If you have any further requests or need additional assistance, feel free to let me know.
```

**Error Analysis (1 errors):**
- **Replace:** Expected `donc aujourd'hui le 6 novembre à 16h35, on vient de découvrir un réseau non prévu sur les plans. j'ai mis en arrêt immédiat les travaux sur la zone concernée. avec les gars, on met en sécurité le périmètre et on interdit tout accès dans la zone. il faudra prévoir avec toi une solution et un plan d'action. mais l'idée c'est d'avoir aucune reprise de travaux avant l'identification complète du réseau et la validation de la procédure ensemble.` → Got `thank you for the clarification. if you have any further requests or need additional assistance, feel free to let me know.`

#### gpt-4o-transcribe
**Transcript:**
```
Donc aujourd'hui, le 6 novembre à 16h35, on vient de découvrir un réseau non prévu sur les plans. J'ai mis en arrêt immédiat les travaux sur la zone concernée. Avec les gars, on met en sécurité le périmètre et on interdit tout accès dans la zone. Il faudra prévoir avec toi une solution et un plan d'action. Mais l'idée, c'est d'avoir aucune reprise de travaux avant l'identification complète du réseau et la validation de la procédure ensemble.
```

**Error Analysis (2 errors):**
- **Replace:** Expected `aujourd'hui` → Got `aujourd'hui,`
- **Replace:** Expected `l'idée` → Got `l'idée,`

#### gpt-4o-mini-transcribe
**Transcript:**
```
Donc aujourd'hui le 6 novembre à 16h35, on vient de découvrir un réseau non prévu sur les plans. J'ai mis en arrêt immédiat les travaux sur la zone concernée. Avec les gars, on met en sécurité le périmètre et on interdit tout accès dans la zone. Il faudra prévoir avec toi une solution et un plan d'action. Mais l'idée c'est d'avoir aucune reprise de travaux avant l'identification complète du réseau et la validation de la procédure ensemble.
```

✅ **Perfect match - No errors!**

#### gpt-4o-audio-preview
**Transcript:**
```
Donc aujourd'hui le 6 novembre à 16h35, on vient de découvrir un réseau non prévu sur les plans. J'ai mis en arrêt immédiat les travaux sur la zone concernée. Avec les gars, on met en sécurité le périmètre et on interdit tout accès dans la zone. Il faudra prévoir avec toi une solution et un plan d'action, mais l'idée c'est de n'avoir aucune reprise de travaux avant l'identification complète du réseau et la validation de la procédure ensemble.
```

**Error Analysis (2 errors):**
- **Replace:** Expected `d'action.` → Got `d'action,`
- **Replace:** Expected `d'avoir` → Got `de n'avoir`

---
