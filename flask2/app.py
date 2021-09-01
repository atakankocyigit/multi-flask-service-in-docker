#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#import cv2
#import numpy as np
#import os
from flask import Flask, flash, request, redirect, url_for, render_template , abort
#from flask import session as login_session
#from werkzeug.utils import secure_filename
#import re, time, base64
#from PIL import Image
#from io import BytesIO

DEVELOPMENT_ENV  = True



app = Flask(__name__)

app_data = {
    
}


@app.route('/flask2/')
def index():
    return render_template('index.html', app_data=app_data)

if __name__ == '__main__':
    
    app.secret_key = 'some secret key'

    app.debug = True
    app.run(debug=DEVELOPMENT_ENV)
    
    

    
