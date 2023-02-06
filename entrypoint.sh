#!/bin/sh
gunicorn app:AplicacionFlask --bind=0.0.0.0:80