Install the required packages:
```bash
    sudo apt update
    sudo apt install python3
    sudo apt install python3-pip
    sudo apt install python3-pil
    sudo apt install python3-RPi.GPIO
    sudo apt install python3-smbus
    sudo apt install python3-i2cdevice
    sudo apt install python3-flask
    sudo apt install python3-os
    sudo apt install python3-sys
    sudo apt install python3-datetime
    sudo apt install python3-csv
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
