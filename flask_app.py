from flask import Flask, request, session, redirect, url_for, \
                  send_from_directory, render_template

from parser import make_file
from transitions import make_option_files


from numpy import asarray
import json




app = Flask(__name__)


@app.route('/')
def Start():
	make_option_files("Start")
	make_file("Start")
	return render_template('page.html')

@app.route('/next', methods =['POST'])
def  next():
	if request.method == 'POST':
		form = request.form['option']
		# Page for the pronunciation evaluation.
		if(form == "PronEval"):
			return render_template('PronEval.html')
		# Page for inteligibility remediation information.
		elif(form == "Info"):
			return render_template('Info.html')
		else:
			make_option_files(form)
			make_file(form)
			return render_template('page.html')


if __name__ == '__main__':
   app.run(debug = True)
