# python-rest-services

https://stackoverflow.com/questions/49015957/how-to-get-python-graph-output-into-html-webpage-directly
https://towardsdatascience.com/build-your-own-python-restful-web-service-840ed7766832

A simple program that create a rest service. 

requirements.txt contains the packages to include when building application image.

oc new-build  --name=python-rest-service  --binary --image-stream=python:latest -e APP_FILE=ws.py

oc start-build python-rest-service   --from-dir=.  --follow

oc new-app python-rest-service -e APP_FILE=ws.py


curl -d '{"num1" : [1, 2, 3], "num2":[4, 5, 6]}' -H "Content-Type: application/json" -X POST http://python-rest-service-aaa.apps.cluster-pbcmk.pbcmk.sandbox511.opentlc.com/process

oc new-project dev
oc create serviceaccount pipeline 
oc policy add-role-to-user admin system:serviceaccount:pipeline:pipeline  -n dev

oc new-project sit
oc policy add-role-to-user admin system:serviceaccount:pipeline:pipeline  -n sit
oc policy add-role-to-user system:image-puller system:serviceaccount:sit:default -n dev

