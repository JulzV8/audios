# Code source: Stefan Balke
# License: ISC
# sphinx_gallery_thumbnail_number = 4

import numpy as np
import matplotlib
import matplotlib.pyplot as plt

import librosa
import librosa.display

x = np.arange(0, 5, 0.1)
print(x)
y = np.sin(x)
print(y)
fig, ax = plt.subplots()
ax.plot(x, y)

plt.show()
