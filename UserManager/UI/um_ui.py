from flask import Flask;

app = Flask(__name__);

@app.route("/")
def mainpage:
	return "this is the mainpage";

@app.route("/login")
def loginpage:
	return "login";