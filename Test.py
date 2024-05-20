# Beat tracking example
import pandas as pd
import numpy as np
import matplotlib.pylab as plt
#import seaborn as sns
#from glob import glob
import librosa
import librosa.display
import IPython.display as ipd


audio_path = "StarWars60.wav"
y,sr = librosa.load(audio_path)
# Define the speed of approach (positive for approaching, negative for moving away)
approach_speed = 0.1  # Adjust as needed

# Calculate the time delay based on the approach speed
max_delay_samples = int(sr / abs(approach_speed))

# Initialize the output array with zeros
y_doppler = np.zeros_like(y)

# Apply the Doppler effect
for t in range(len(y)):
    # Calculate the delay based on the approach speed
    delay = int(t * approach_speed)
    
    # Apply the delay to the audio sample
    if delay < max_delay_samples:
        y_doppler[t] = y[t - delay]

# Normalize the audio to ensure it remains within the valid range [-1, 1]
y_doppler /= np.max(np.abs(y_doppler))

# Play the original and modified audio
print("Playing original audio...")
librosa.output.write_wav('original_audio.wav', y, sr)
librosa.display.waveshow(y, sr=sr)
plt.show()

print("Playing audio with Doppler effect...")
librosa.output.write_wav('doppler_audio.wav', y_doppler, sr)
librosa.display.waveshow(y_doppler, sr=sr)
plt.show()