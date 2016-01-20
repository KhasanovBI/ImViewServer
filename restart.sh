#!/bin/bash
killall -9 python3
git pull
python3 run.py > out.txt &
