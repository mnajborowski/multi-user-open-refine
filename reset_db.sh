#!/bin/bash
rm /home/randomsec/RandomSec/MUOR/db.sqlite3
touch /home/randomsec/RandomSec/MUOR/db.sqlite3
python3 /home/randomsec/RandomSec/MUOR/manage.py makemigrations
python3 /home/randomsec/RandomSec/MUOR/manage.py migrate