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
myMQTTClient.configureEndpoint("YOUR.ENDPOINT", 8883)
# For Websocket
# myMQTTClient.configureEndpoint("YOUR.ENDPOINT", 443)
cwd = os.getcwd()
print cwd

certificateFolder =  "certificates"
CA_certificatefileName =cwd +"/"+certificateFolder + "/rootCA.pem"  
privateKeyName = cwd.join(certificateFolder + "/d91b3ba369-private.pem.key")  
certificateFileName = cwd.join(certificateFolder + "/d91b3ba369-certificate.pem.crt")
print CA_certificatefileName
