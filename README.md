
# INTRODUCTIO

In this project, ESP32 reads data, with help of dht11 and publishes data to mosquitto or MQTT. our weather station suscribes the data from mosquitto. weather station shows temperature and humidity and their graphs.

## NOTE

Here, we can use ngrok to host Weather station and can access server from anywhere over the internet 



## what to do

   1. In cmd run
   ```bash
   ipconfig
   ```
   2. Note ipv4 address which is our broker address.Put it in esp32 code

   3. Upload the code to esp32.

   4. run mosquitto
   ```bash
   mosquitto -c "C:\Program Files\mosquitto\mosquitto.conf" -v
```

   5. run init_db.py
   ```bash
   python init_db.py
   ```
   6. run mqtt_subscriber.py
   ```bash
   python mqtt_subscriber.py
   ```
   7.run app.py
   ```bash
   python app.py
   ```



## To host this weather station
run the following command in cmd
```bash
ngrok http http://localhost:8080
```

