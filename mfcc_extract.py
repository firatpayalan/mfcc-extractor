#simple mfcc extractor

import essentia.standard
import glob

from essentia.standard import *

#pool is a "container" data type.
pool = essentia.Pool();


#load audio file from file system
w = Windowing(type = 'hann')
spectrum = Spectrum()  # FFT() would return the complex FFT, here we just want the magnitude spectrum
mfcc = MFCC()
loader = essentia.standard.MonoLoader(filename='/home/firat/Desktop/samples/street_music/152570.wav')
audio=loader()

mfccs=[]
melbands=[]
for frm in FrameGenerator(audio,frameSize=1024,hopSize=512,startFromZero=True):
    mfcc_bands,mfcc_coeffs = mfcc(spectrum(w(frm)))
    pool.add("coefficients",mfcc_coeffs);
    pool.add("mel_bands",mfcc_bands);
    mfccs.append(mfcc_coeffs)
    melbands.append(mfcc_bands)
#mfccs = essentia.array(mfccs).T
# melbands = essentia.array(melbands).T
# print mfccs
# print len(mfccs)

#pool aggregator supplies statistical operations.
aggrPool = PoolAggregator(defaultStats=["mean"])(pool)
print aggrPool.descriptorNames()
YamlOutput(filename="mfccmean.sig",format="json")(aggrPool)
