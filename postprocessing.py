import json
import glob

def findSigFiles(filepath):
    print "Number of files: " ,len(glob.glob(filepath+"/*.sig"))
    return glob.glob(filepath+"/*.sig")

def readJsonFromFileSys(filepath):
    file = open(filepath,"r")
    decoded = json.load(file)
    return str(decoded.get("coefficents").get("mean"))

def constructData(filepath,label):
    constructedData=''
    rawData = findSigFiles(filepath)
    for raw in rawData:
        constructedData = constructedData+readJsonFromFileSys(raw)+","+label+"\n"

    return constructedData

def writeIntoFile(data,filename):
    newFile = open(filename,"w")
    newFile.write(data)
    newFile.close()

print constructData("/home/firat/PycharmProjects/car_horn","traffic")
toBeWritten = constructData("/home/firat/PycharmProjects/car_horn","traffic")
writeIntoFile(toBeWritten,"traffic")

