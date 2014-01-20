import json
import csv
import sys
from pprint import pprint
import decimal
# import matplotlib.pyplot as plt
import os

if len(sys.argv) > 1:
    inputPath = sys.argv[1]
    outputPath = sys.argv[2]
else:
    print "Enter the location of the input files: "; directory = raw_input()
    inputPath = r"%s" % directory
    print "Enter the location for the output files: "; directory = raw_input()
    outputPath = r"%s" % directory

print "Input Path: " + inputPath
print "Output Path: " + outputPath

for file in os.listdir(inputPath):
    print "File: " + file
    current_file = os.path.join(inputPath, file)

    date = file[0:file.index('T')]
    time = file[file.index('T')+1:file.index('.')]

    f = open(current_file, "rb")

    data = json.load(f)
    f.close()

    delimiter = ","

    stationData = json.loads(data[1]['data'])

    store = dict()

    outFile = open(outputPath + file, "w")

    for item in stationData:
        latitude  = unicode(round(decimal.Decimal(item[u'AddressGmapsLatitude']),6))
        longitude = unicode(round(decimal.Decimal(item[u'AddressGmapsLongitude']),6))
        bikes     = item[u'StationAvailableBikes']
        freeSlots = item[u'StationFreeSlot']
        id = unicode(item[u'StationID'])
        
        output = date + delimiter + time + delimiter + unicode(item[u'StationID']) + delimiter + unicode(item[u'StationAvailableBikes']) + delimiter + unicode(item[u'StationFreeSlot']) + delimiter + unicode(round(decimal.Decimal(item[u'AddressGmapsLatitude']),6)) + delimiter + unicode(round(decimal.Decimal(item[u'AddressGmapsLongitude']),6)) + '\n'
        store[id] = {'latitude': latitude, 'longitude': longitude, 'bikes': bikes, 'freeSlots': freeSlots}
        outFile.write(output)
   
    outFile.close()
