#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#import cv2
#import numpy as np
#import os
from flask import Flask, flash, request, redirect, url_for, render_template , abort
import os 
#from flask import session as login_session
#from werkzeug.utils import secure_filename
#import re, time, base64
#from PIL import Image
#from io import BytesIO

DEVELOPMENT_ENV  = True
app = Flask(__name__)
app_data = {
    
}
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

UPLOAD_FOLDER = os.path.dirname(os.path.realpath(__file__))
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/flask/')
def index():
    return render_template('index.html', app_data=app_data)

@app.route('/flask/about')
def about():
    return render_template('about.html', app_data=app_data)


@app.route('/flask/service')
def service():
    return render_template('service.html', app_data=app_data)


@app.route('/flask/contact')
def contact():
    return render_template('contact.html', app_data=app_data)


if __name__ == '__main__':
    
    app.secret_key = 'some secret key'

    app.debug = True
    app.run(debug=DEVELOPMENT_ENV)