#!/bin/python3

###### IMPORT ALL BELONGINGS
import json
import serial, time
from datetime import datetime, date
from influxdb import InfluxDBClient

######  CONNECT TO InfluxDB LOCAL
dbClient = InfluxDBClient('localhost', 8086, '', '', 'arduino')

###### START INFINITE CICLE
count = 0 
while True:
	###### CONNECT TO SERIAL DEVICE TO READ INPUT
	with serial.Serial('/dev/ttyACM0',9600) as ser:
		x = ser.read(26)
	
	###### create actual timestamp
	TS=datetime.timestamp(datetime.now())

	#### discard first line of input
	if count > 0 :
		#### Transform in JSON format the output
		valsD = json.loads(x.decode("utf-8"))
		
		##### FILL THE LIST
		datas = [{"measurement": "ardu","tags": {"sensore": "DHT11"},
			"datetime": str(TS),
			"fields": valsD
		}]
		##### WRITE THE LIST TO DB
		dbClient.write_points(datas)

		#### write output to a file
		##### OPEN A FILE FOR TRACKING
		f = open("./arduino_read.out","a")
		###print("Leggo e scrivo")
		tempo = datetime.fromtimestamp(TS)
		f.write(str(tempo) + " - " + x.decode("utf-8") + " \n" )
		##### CLOSE THE FILE 
		f.close()
	#### wait a pair if secs and increase the counter
	time.sleep(2)
	count = count + 1
##### END OF SCRIPT
