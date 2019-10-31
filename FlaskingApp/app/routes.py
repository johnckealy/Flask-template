from flask import Flask, jsonify, render_template
from app import app



@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home')


@app.route('/about')
def about():
    user = { 'username': 'John' }
    return render_template('about.html', title='About', user=user)
