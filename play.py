#PRACTICE SERVER FILE
from flask import Flask, render_template
import os

# TEMPLATE_DIR = os.path.abspath('../templates')
# STATIC_DIR = os.path.abspath('../static')

app = Flask(__name__) #template_folder=TEMPLATE_DIR, static_folder=STATIC_DIR)

@app.route('/')
def index():
    return render_template('index.html', name = 'Samyak')

if __name__ == '__main__':
    app.run(debug=True)