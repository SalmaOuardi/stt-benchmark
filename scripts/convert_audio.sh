#!/bin/bash

# Create test_audio folder if it doesn't exist
mkdir -p test_audio

# Counter for renaming
counter=1

# Convert all M4A files in current directory
for file in *.m4a; do
    if [ -f "$file" ]; then
        # Determine output name based on counter
        case $counter in
            1) output="test_audio/audio_01_clean.wav" ;;
            2) output="test_audio/audio_02_technical.wav" ;;
            3) output="test_audio/audio_03_numbers.wav" ;;
            4) output="test_audio/audio_04_short_notes.wav" ;;
            5) output="test_audio/audio_05_safety.wav" ;;
            6) output="test_audio/audio_06_moderate_noise.wav" ;;
            7) output="test_audio/audio_07_heavy_noise.wav" ;;
            8) output="test_audio/audio_10_long.wav" ;;
        esac
        
        echo "Converting $file to $output..."
        ffmpeg -i "$file" -ar 16000 -ac 1 "$output" -y
        
        counter=$((counter + 1))
    fi
done

echo "✅ All files converted!"