#!/bin/bash

# check if python is installed
python3 -m venv myenv
# check if venv already exists
source myenv/bin/activate
pip3 install -r requirements.txt
clear
python3 main.py