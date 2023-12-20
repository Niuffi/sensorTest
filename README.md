Install the required packages:
```bash
    sudo apt update
    sudo apt install python3
    sudo apt install python3-pip
    sudo apt install python3-pil
    pip3 install RPi.GPIO
    pip3 install smbus
    pip3 install i2cdevice
    pip3 install flask
    pip3 install os
    pip3 install sys
    pip3 install datetime
    pip3 install csv
```
Download the repository with the following command:
```bash
    git clone https://github.com/Niuffi/sensorTest.git
```
Change directory to the repository folder:
```bash
    cd sensorTest
```
Add "data" directory:
```bash
    mkdir data
```

Run the program:
```bash
    python3 main.py -n [number of samples] --sensor [coma separated list of sensors]
```
Example:
```bash
    python3 main.py -n 10 --sensor AS7262,AS7341
```
Supported sensors:
- AS7262
- AS7341
- AS7265x

Run web server:
```bash
    sudo python3 web_server.py
```
