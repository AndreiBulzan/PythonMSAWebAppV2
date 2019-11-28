import os
import time
#import magic
import urllib.request
from app import app
from flask import Flask, flash, request, redirect, render_template, send_file
from werkzeug.utils import secure_filename
from flask_dropzone import Dropzone

dropzone = Dropzone(app)

ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
@app.route('/download')
def downloadFile ():
    #For windows you need to use drive name [ex: F:/Example.pdf]
    path = "D:/uploads/myOutput0.txt"
    return send_file(path, as_attachment=True)    
@app.route('/')
def upload_form():
    return render_template('home.html')
@app.route('/upload')    
def upload_form1():
    return render_template('upload.html')    


@app.route('/upload', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No file selected for uploading')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            flash("Hello world")
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            print(filename)
            os.startfile('MyProg.py')
            time.sleep(10)
            f = open("myOutput0.txt", "r")
            flash(f.read())
            os.remove(filename)
            return redirect('/')
        else:
            flash('Allowed file types are txt, pdf, png, jpg, jpeg, gif')
            return redirect(request.url)

if __name__ == "__main__":
    app.run()
