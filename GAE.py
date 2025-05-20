# 12. Create a simple “Hello World” web app using Python on GAE

from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello from Google App Engine!'


# 13. Modify your GAE Python app to take a name as input and greet the user

from flask import Flask, request
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def greet():
    if request.method == 'POST':
        name = request.form.get('name', 'Guest')
        return f'Hello, {name}!'
    return '''
        <form method="post">
            Enter your name: <input type="text" name="name">
            <input type="submit" value="Greet Me">
        </form>
    '''


# 15. Create a webpage using HTML hosted in a Python GAE app

from flask import Flask
app = Flask(__name__)

@app.route('/')
def html_page():
    return '''
        <html>
        <head><title>My HTML Page</title></head>
        <body>
            <h1>Welcome to My HTML Page!</h1>
            <p>This page is served from Python on GAE.</p>
        </body>
        </html>
    '''


# 17. Modify the Python app to display current date and time using the datetime module

from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def show_time():
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return f'<h2>Current Date and Time:</h2><p>{now}</p>'


# JAVA

# mvn archetype:generate -DgroupId=com.example -DartifactId=helloworld \
#   -DarchetypeArtifactId=maven-archetype-webapp -DinteractiveMode=false


# https://nadin-460312.el.r.appspot.com/


# gcloud projects add-iam-policy-binding nadin-460312 --member="serviceAccount:nadin-460312@appspot.gserviceaccount.com" --role="roles/storage.admin"