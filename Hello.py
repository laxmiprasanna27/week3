from flask import Flask
app=Flask(__name__)
@app.route('/')
def hello():
	return ("Hello world have a nice daya!!")
if __name__=='__main__':
    app.run(debug=True)