# python-rest-services

A simple program that create a rest service. 

requirements.txt contains the packages to include when building application image.

oc new-build  --name=python-rest-service  --binary --image-stream=python:latest -e APP_FILE=ws.py

oc start-build python-rest-service   --from-dir=.  --follow

oc new-app python-rest-service -e APP_FILE=ws.py


curl -d '{"num1" : [1, 2, 3], "num2":[4, 5, 6]}' -H "Content-Type: application/json" -X POST http://python-rest-service-aaa.apps.cluster-pbcmk.pbcmk.sandbox511.opentlc.com/process

