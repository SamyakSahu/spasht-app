import os
from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
from extract import ext

UPLOAD_FOLDER = 'static'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'mp4'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('process')) #this points to the next page
    return render_template('index.html')

@app.route('/process', methods=['GET', 'POST'])
def process():
    ext()
    return render_template('splashscreen.html')

@app.route('/sf', methods=['GET'])
def showImg():
    return render_template('postupload.html')

app.run(debug=True)

# Candidate main server

'''
To do:
1. Main page to upload a photo
2. Run the DL model and create rectangles
3. Take that image and generate the output
'''

# from flask import Flask, render_template, request
# from werkzeug.utils import secure_filename
# app = Flask(__name__)

# @app.route('/')
# def upload_file():
#    return render_template('upload.html')
	
# @app.route('/uploader', methods = ['GET', 'POST'])
# def uploader():
#    if request.method == 'POST':
#       f = request.files['file']
#       f.save(secure_filename(f.filename))
#       return 'file uploaded successfully'
		
# if __name__ == '__main__':
#    app.run(debug = True)


