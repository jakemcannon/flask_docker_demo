from flask import Flask

app = Flask(__name__)

@app.route("/hello")
def hello():
	return "hello user!!"

@app.route("/")
def index():
	# this line was changed to see if changes are instant or I would need to rebuild image
	return "This is my Flask application!!"


if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0', port=5005)
