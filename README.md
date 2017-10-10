# Coursera Dump

The program collects data from N courses in Coursera and saves it to a file

### How to Install

Python 3 should be already installed. Then use pip (or pip3 if there is a conflict with old Python 2 setup) to install dependencies:

```bash
pip install -r requirements.txt # alternatively try pip3
```

### How to use
```bash

$ python3 coursera.py -h
usage: coursera.py [-h] [-a AMOUNT] -f FILE

optional arguments:
  -h, --help            show this help message and exit
  -a AMOUNT, --amount AMOUNT
                        Amount of Coursera courses to view
  -f FILE, --file FILE  Path to output Excel .xlsx file
```

### Sample output
```bash
$ python coursera.py -a 20 -f sample.xlsx

30% (6 of 20) |#######                   | Elapsed Time: 0:00:09 ETA:  0:00:21
```
Remember, it is recommended to use [virtualenv/venv](https://devman.org/encyclopedia/pip/pip_virtualenv/) for better isolation.

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
