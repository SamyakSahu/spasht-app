from flask import Flask, render_template, url_for, send_file, request, redirect
import extract
# import classify_script

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    # extract.run()
    return render_template('page1.html')

@app.route('/extract', methods=['GET', 'POST'])
def extract():
    if request.method == 'POST':
        # sharpFrame = extract.spit()
        return redirect(url_for('index'))


    return render_template('page2.html', frame = sharpFrame)


if __name__ == "__main__":
    app.run(debug=True)
    
'''
def loadVideo():
    # get video path via JQuery
'''
# @app.route('/classify', methods=['GET', 'POST'])
# def classify():
#     if request.method == 'POST':
#         # do stuff when the form is submitted
#         # redirect to end the POST handling
#         # the redirect can be to the same route or somewhere else
#         return redirect(url_for('extract'))
#     # show the form, it wasn't submitted
#     return render_template('page3.html')

# @app.route('/result', methods=['GET', 'POST'])
# def result():
#     if request.method == 'POST':
#         # do stuff when the form is submitted
#         # redirect to end the POST handling
#         # the redirect can be to the same route or somewhere else
#         return redirect(url_for('classify'))
#     # show the form, it wasn't submitted
#     return render_template('page4.html')



# def index(user):
#     if request.method == "POST":
#         user = request.form['username']
#         return redirect(url_for('home'), username = user)
#     return render_template('lang.html', name = user)

# @app.route('/home')
# def home(name):
#     return 'Welcome %s' % name

