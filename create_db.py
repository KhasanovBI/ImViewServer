#!/usr/bin/python3
import os

from app import db
try:
    os.remove('app/app.db')
except OSError:
    pass
db.create_all()
