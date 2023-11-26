# Simple LDAP search and data verification

Simple demo to show how python can replace proprietary tools for that reads via ldap, verfies data quality and other similar actions.

LDAP using https://ldap3.readthedocs.io/en/latest/welcome.html

Accessing SQL databases can be done using similar means

Calling Webservices can over SOAP can be done using libraries like this: https://docs.python-zeep.org/en/master/ 

Java classes can be called from Python using https://jpype.readthedocs.io/en/latest/ if needed. 


## Change history

Change ldap library, seems ldap3 is more easy to work with than python-ldap

## Installation

Requires Python3

```
#Install dependences
pip install -r requirements.txt
```


## Run

```
# Run as any python script
python searchAllUsers.py 
```