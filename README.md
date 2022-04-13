# Python-Financial-API-REST

Description:  
This is a Python REST API which will use a docker container, inside an AWS Lambda, with some unit testing functionality and pipeline deployment.
VENV is used like a primitive docker, activate with
Windows: .\app\Scripts\activate
UNIX: source app/Scripts/activate

Extras:  
All models are Serialized: Currently there are only 2 models Users & Companies, Users being the default Django auth model which is currently useless as it's for an optional auth.  
When a Company is made it needs to be correlated if it has a valid symbol according to the NY Stock Exchange using yFinance.  
Expected errors will be logged into error_log.txt.  
Pipeline with Git Hub Actions.  

TO-DO LIST:  
----CRUD ✔  
----NY Stock Exchange Symbol check:  
--------Basic ✔  
--------Optimized  
----Errors Logging ✔  
----Unit Testing:  
--------Basic ✔  
--------Models  
--------Views  
--------Serialization  
----Dockerization ❌
----Pipeline:
--------Basic(Lambda✔) ❌  
--------Checking unit tests  
----AWS:  
--------Lambdas ❌  
----API GATEWAY
----Elastic Beanstalk