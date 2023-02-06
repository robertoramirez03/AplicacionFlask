#!/bin/sh
gunicorn AplicacionFlask:app --bind=0.0.0.0:80