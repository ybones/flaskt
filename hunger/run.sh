#!/bin/bash

gunicorn -c conf_gun.py app:app