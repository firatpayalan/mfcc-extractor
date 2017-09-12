import glob
import os
import essentia.standard
from essentia.standard import *
import time

def findWavFiles(filepath):
    print ("Number of files: " ,len(glob.glob(filepath+"/*.wav")))
    return glob.glob(filepath+"/*.wav")

def loadAudio(audiofilepath):
    loader = essentia.standard.MonoLoader(filename=audiofilepath)
    audio = loader()
    return audio

def exportCalculatedData(pool,exportedfilename):
    aggrPool = PoolAggregator(defaultStats=["mean"])(pool)
    YamlOutput(filename=exportedfilename,format="json")(aggrPool)

def currentTime():
    return int(round(time.time()*1000))

#pool is a "container" data type.
pool = essentia.Pool();
spectrum = Spectrum()
mfcc = MFCC()
w = Windowing(type='hann')

glob = findWavFiles("24003__erdie__mega-thunder.wav")

startTime = currentTime();
for g in glob:

    exportedfilename = os.path.basename(g).replace(".wav","")
    print(exportedfilename)
    audio = loadAudio(g)

    for frame in FrameGenerator(audio,frameSize=1024,hopSize=512,startFromZero=True):
        mfcc_bands,mfcc_coeffs = mfcc(spectrum(w(frame)))
        pool.add("coefficents",mfcc_coeffs)
        pool.add("mel_bands",mfcc_bands)
    exportCalculatedData(pool,exportedfilename+".sig")
    pool.clear()

endTime = currentTime()
totalTime = endTime-startTime
print ("total time is", totalTime)