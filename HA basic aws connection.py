# Import SDK packages

import os
import sys
import AWSIoTPythonSDK
sys.path.insert(0, os.path.dirname(AWSIoTPythonSDK.__file__))
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient

# For certificate based connection
myMQTTClient = AWSIoTMQTTClient("myClientID")
# For Websocket connection
# myMQTTClient = AWSIoTMQTTClient("myClientID", useWebsocket=True)
# Configurations
# For TLS mutual authentication
myMQTTClient.configureEndpoint("a3cd6yyy4as8ey.iot.us-west-2.amazonaws.com", 8883)
# For Websocket
# myMQTTClient.configureEndpoint("Your end point", 443)
cwd = os.getcwd()
print(cwd)
certificateFolder =  "certificates"
CA_certificatefileName =cwd +"/"+certificateFolder + "/rootCA.pem"  
privateKeyName = cwd +"/"+certificateFolder + "/d91b3ba369-private.pem.key"  
certificateFileName = cwd +"/"+certificateFolder + "/d91b3ba369-certificate.pem.crt"  

def message(self,data,message):
    print "message called"
    print data
    print message.payload
    payload = message.payload
    if payload =="1":
        print "light going to turn on"
    else :
        print "payload is not known"
myMQTTClient.configureCredentials(CA_certificatefileName, privateKeyName, certificateFileName)
# For Websocket, we only need to configure the root CA
# myMQTTClient.configureCredentials("YOUR/ROOT/CA/PATH")
myMQTTClient.configureOfflinePublishQueueing(-1)  # Infinite offline Publish queueing
myMQTTClient.configureDrainingFrequency(2)  # Draining: 2 Hz
myMQTTClient.configureConnectDisconnectTimeout(10)  # 10 sec
myMQTTClient.configureMQTTOperationTimeout(5)  # 5 sec

myMQTTClient.connect()
myMQTTClient.publish("myTopic", "myPayload", 0)
myMQTTClient.subscribe("myTopic", 1, message)
##myMQTTClient.unsubscribe("myTopic")
