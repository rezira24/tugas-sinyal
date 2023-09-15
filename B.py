import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, lfilter

# ID
print("Nama: Rezi Rafidan Alfizar")
print("NRP: 5009211024")

# Generate a noisy sinusoidal signal
fs = 1000  # Sampling frequency (Hz)
t = np.arange(0, 1, 1/fs)  # Time vector from 0 to 1 second
f_signal = 5  # Frequency of the signal (Hz)
signal = np.sin(2 * np.pi * f_signal * t)  # Clean sinusoidal signal
noise = 0.5 * np.random.normal(0, 1, len(t))  # Gaussian noise
noisy_signal = signal + noise  # Noisy signal

# Define a function for low-pass Butterworth filter
def butter_lowpass(cutoff, fs, order=5):
    nyquist = 0.5 * fs
    normal_cutoff = cutoff / nyquist
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    return b, a

def butter_lowpass_filter(data, cutoff, fs, order=5):
    b, a = butter_lowpass(cutoff, fs, order=order)
    y = lfilter(b, a, data)
    return y

# Apply low-pass filter to the noisy signal
cutoff_freq = 30  # Cutoff frequency of the filter (Hz)
filtered_signal = butter_lowpass_filter(noisy_signal, cutoff_freq, fs)

# Plot the original signal, noisy signal, and filtered signal
plt.figure(figsize=(12, 6))
plt.subplot(2, 1, 1)
plt.plot(t, noisy_signal, 'b-', label='Noisy Signal')
plt.plot(t, signal, 'g', linewidth=2, label='Clean Signal')
plt.legend()
plt.title('Noisy Signal and Clean Signal')
plt.xlabel('Time (s)')
plt.grid()

plt.subplot(2, 1, 2)
plt.plot(t, filtered_signal, 'r', label='Filtered Signal')
plt.legend()
plt.title('Filtered Signal (Low-Pass Butterworth)')
plt.xlabel('Time (s)')
plt.grid()

plt.tight_layout()
plt.show()
