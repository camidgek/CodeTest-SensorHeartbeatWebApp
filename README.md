# CodeTest-SensorHeartbeatWebApp
A web application that displays the latest "heartbeat" from a number of sensors.

## Setup
### Redis
Download, compile, and run Redis in the background (or separate terminal).
```
wget https://download.redis.io/releases/redis-6.2.4.tar.gz
tar xzvf redis-6.2.4.tar.gz
pushd redis-6.2.4/
make
./src/redis-server &
popd
```
### Venv
Create and source a virtual environment.
```
python3 -m venv venv
source ./venv/bin/activate
```
Install dependencies.
```
pip install --upgrade pip
pip install -r requirements.txt
```
## Usage
### Run the server
```
cd mysite/
python manage.py makemigrations sensorheartbeat
python manage.py migrate
python manage.py runserver
```
### Simulate data
Calling this script as so will POST data every **2 seconds**, first a sensor, and then **5 heartbeats** for that sensor, repeating until stopped.
```
cd scripts/
./simulate-data.sh 2 5
```
