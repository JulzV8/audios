# Code source: Stefan Balke
# License: ISC
# sphinx_gallery_thumbnail_number = 4

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import scipy

import librosa
import librosa.display

sample, fs = librosa.load('nutcracker.ogg', duration=45, sr=8000)
mask, fs = librosa.load('nutcracker.ogg', duration=10, offset=20, sr=8000)

correlation = scipy.signal.correlate(sample, mask, mode="valid")
maskedSample = correlation[np.argmax(correlation):(
    np.argmax(correlation)+len(mask))]
# correlationMask = scipy.signal.correlate(mask, mask)

print("len mask", len(mask))
print("len maskedSample", len(maskedSample))


plt.plot(correlation)
plt.show()
