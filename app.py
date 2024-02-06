from flask import Flask
app = Flask(__name__)

@app.route('/')
def main():
	name = input("What is your name?")
	return name
