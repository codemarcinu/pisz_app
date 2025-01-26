#!/bin/bash

# Uruchomienie backendu Flask
cd app
flask --app __init__.py run &

# Uruchomienie frontendu React
cd ../frontend
npm start