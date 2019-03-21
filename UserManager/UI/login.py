from flask import Flask;
from flask import render_template;
from flask import request;

app = Flask(__name__);

@app.route('/login/')
def login():
	if request.method == 'POST':
		pass;
		
	return render_template('tpl_login.html')