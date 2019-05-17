/*

This Arduino code need an DHT11 sensor for Humidity and Temperature.
You can also change with whatever sensor is needed, the focus is on the output
sended to the Serial port that must be a sort of JSON format.

THIS IS THE SIMPLE VERSION WITH ONLY THE SENSOR

There is a more complex version that use also a led and an LCD screen.

*Almost the total of this coda was picked from Arduino examples sketches
*/

// NEEDE LIBRARIES
#include <DHT.h>

// DHT CONFIGURATION
#define DHTPIN            7         // Pin which is connected to the DHT sensor.
#define DHTTYPE           DHT11     // DHT 11

DHT dht(DHTPIN, DHTTYPE);

// INITIALIZE DHT AND Serial PORT
void setup() {
	dht.begin();
	Serial.begin(9600);
}

// MAIN LOOP
void loop() {
	//Read infos
	// float f = dht.readTemperature(true); // for temperature in Fahrenheit
	float f_h = dht.readHumidity();
	float f_t = dht.readTemperature();
 	
	// WRITE TO SERIAL PORT LIKE JSON FORMAT output: {"TEMP":22.00,"UMI":54.00} 
	Serial.print("{\"TEMP\":");
	Serial.print(f_t);
	Serial.print(",\"UMI\":");
	Serial.print(f_h);
	Serial.print("}");
	Serial.println("");
	delay(2000);
}
