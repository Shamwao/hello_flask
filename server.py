from flask import Flask  

app = Flask(__name__)    

@app.route('/')          
def hello_world():
    return 'Hello World!'  

@app.route('<str/dojo>')
def dojo():
    return 'Dojo!'

@app.route('/say/<string:name>')
def hello(name):
    return 'Hello ' + name

@app.route('/repeat/<int:num>/<str:greeting>')
def repeat(num, greeting):
    return greeting * num

if __name__=="__main__":     
    app.run(debug=True)    

