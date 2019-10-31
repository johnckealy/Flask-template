from flask import Flask, jsonify, render_template, request
from query_db import Temperature, connect2DB, query_nearest_point
from app import app
import numpy as np
import json



@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home')


@app.route('/about')
def about():
    user = { 'username': 'John' }
    return render_template('about.html', title='About', user=user)


@app.route('/deleteme')
def deleteme():
    return render_template('deleteme.html', title='Deleteme')


@app.route('/climo', methods=['POST'])
def climo():

    session = connect2DB()

    latpoint = request.json['lat']
    lonpoint = request.json['lon']
    
    T = query_nearest_point(session, latpoint, lonpoint)

    return json.dumps({ 'lat': latpoint, 'lon': lonpoint, 'Temperature': T})
