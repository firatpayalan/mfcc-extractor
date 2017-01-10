# first, we need to import our essentia module. It is aptly named 'essentia'!
import essentia

# as there are 2 operating modes in essentia which have the same algorithms,
# these latter are dispatched into 2 submodules:
import essentia.standard
import essentia.streaming

from pylab import plot, show, figure, imshow
from IPython import get_ipython

import matplotlib.pyplot as plt
from essentia.standard import *


w = Windowing(type = 'hann')
spectrum = Spectrum()  # FFT() would return the complex FFT, here we just want the magnitude spectrum
mfcc = MFCC()
loader = essentia.standard.MonoLoader(filename='/home/firat/Desktop/samples/sokak_gurultusu/st2.wav')
audio=loader()

frame = audio[1*44100 : 2*44100 + 1024] #
plot(audio[2*44100 : 2*44100 + 1024])
plt.savefig("frame.png")
spec = spectrum(w(frame))
mfcc_bands, mfcc_coeffs = mfcc(spec)
print "mel coefficients"
print mfcc_coeffs
print "mel bands"
print mfcc_bands

# plot(spec)
# plt.title("The spectrum of a frame:")
# plt.savefig('st2_specframe.png')
#show() # unnecessary if you started "ipython --pylab"

# plot(mfcc_bands)
# plt.title("Mel band spectral energies of a frame:")
# plt.savefig('st2_melspecenergy.png')
# #show() # unnecessary if you started "ipython --pylab"
#
# plot(mfcc_coeffs)
# plt.title("First 13 MFCCs of a frame:")
# plt.savefig('st2_mfccframe.png')
#show() # unnecessary if you started "ipython --pylab"