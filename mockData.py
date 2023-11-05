import numpy as np
import time

# Number of EEG channels (leads)
num_channels = 8

# Sampling rate in Hz
sampling_rate = 256

# Create a time vector
t = np.arange(0, 10, 1 / sampling_rate)  # Simulate 10 seconds of data

# Create EEG signal amplitudes for each channel (simulated data)
# You can modify these to simulate different patterns or noise levels
amplitudes = np.random.rand(num_channels) * 50  # Random amplitudes between 0 and 50 µV

# Create a function to generate synthetic EEG data
def generate_eeg_data():
    eeg_data = np.zeros((num_channels, len(t)))
    for i in range(num_channels):
        # Simulate a sine wave with random frequency and phase
        frequency = np.random.uniform(1, 20)  # Frequency between 1 and 20 Hz
        phase = np.random.uniform(0, 2 * np.pi)  # Random phase
        eeg_data[i, :] = amplitudes[i] * np.sin(2 * np.pi * frequency * t + phase)
    return eeg_data

# Simulate real-time EEG data generation
while True:
    eeg_sample = generate_eeg_data()
    # Here, you can send the eeg_sample to your EEG headset interface or perform further processing
    # For this example, we'll just print the data
    print(eeg_sample)
    time.sleep(1.0 / sampling_rate)  # Sleep for the time corresponding to one sample
