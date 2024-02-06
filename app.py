from flask import Flask
app = Flask(__name__)

@app.route('/')
def main():
	def fib(n):
		if n<= 1:
			return n
		else:
			return(fib(n-1) + fib(n-2))
	iterations = 25
	arr = []
	for i in range(iterations):
		arr.append(fib(i))
	return arr
