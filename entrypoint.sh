#!/bin/sh
gunicorn AplicacionFlask:AplicacionFlask --bind=0.0.0.0:80