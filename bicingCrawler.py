import urllib2
import datetime
import time

while True:
    timestamp = datetime.datetime.now().isoformat()
    
    req = urllib2.urlopen("http://bicing.cat/formmap/getJsonObject")
    response = req.read()
    # response = req.read().decode('unicode-escape').encode('utf8')
    # #print response.decode('unicode-escape')

    myFileName = "data/" + timestamp + ".json"
    # print response
    
    file = open(myFileName, "w")
    file.write(response)
    file.close()

    time.sleep(60);

    # mystring = "03 - C\\/ D'AL\u00cd BEI 44"
    # print unicode(mystring.decode('unicode-escape'))
    # break