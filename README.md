Install the required packages:
```bash
    sudo apt update
    sudo apt install python3 -y  
    sudo apt install python3-pip -y
    sudo apt install python3-pil -y
    sudo apt install python3-RPi.GPIO -y
    sudo apt install python3-smbus -y
    sudo apt install python3-i2cdevice -y
    sudo apt install python3-flask -y
    sudo rm /usr/lib/python3.11/EXTERNALLY-MANAGED
    sudo apt install python3-datetime -y
    sudo apt install python3-csv -y
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
