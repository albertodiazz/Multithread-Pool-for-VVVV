# MultiServices in Parallelism

This webApps was made for communicated multiple clients with a custom developent made in [VVVV](https://vvvv.org/) who made real time data representation. 

## Backend 
Is made in python and run multiple services like UDP, Websocket, Flask the database is Mongo. 

## EndPoint Flask
We only have one endpoint and is made for see when the data base is update with a new value, in that moment our server send the data through websocket to VVVV.
```bash
/data PUT
```

## Setup
+ In the root path you need to create a .env file.
```bash
USERMONGO=[Client]
PASSMONGO=[Password]
DB=[Data base name]
IP=[Ip data base]
PORT=[Port data base]
```
+ Install the packages.
```python
pip install -r requirements.txt
```
+ Run the app.
```python
python app.py
```
## FlowChart
![image](https://i.ibb.co/pvCwmhB/Sharding-Database.jpg)
