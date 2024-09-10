# generate a basic flask api
from flask import Flask 
app = Flask(__name__)

@app.route('/') # define the route
def hello_world():
    return 'welcome to Python'

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000)
    
# run the app with python app.py
# go to http://127.0.0.1:5000/ to see the output
# to stop the app, press ctrl+c
