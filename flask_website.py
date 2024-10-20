# Importing flask for deploying our website on development server
from flask import Flask
 
# Flask constructor takes the name of
# current module (__name__) as argument.
app = Flask(__name__)
 
# The route() function will tell the which function to call if this appear in url
@app.route('/')
# '/' URL is linked with hello_world() function.
def hello_world():
    return 'Hello World'

# '/hello' is linked to me function
@app.route("/hello")
def me():
    return "Hello" 

if __name__ == '__main__':
    # runs the application
    app.run()