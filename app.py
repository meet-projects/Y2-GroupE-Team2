from flask import Flask, render_template, request, redirect, url_for, flash
from flask import session as login_session
import pyrebase

Config = {
  "apiKey": "AIzaSyCs6k0XhtrNjyECIsubgq0itGfSZhzWn8g",
  "authDomain": "individual-project-7bc5e.firebaseapp.com",
  "projectId": "individual-project-7bc5e",
  "storageBucket": "individual-project-7bc5e.appspot.com",
  "messagingSenderId": "305217233371",
  "appId": "1:305217233371:web:2beb79ec73ea43130687fe",
  "measurementId": "G-30QPYFQRYP",
  "databaseURL": "https://individual-project-7bc5e-default-rtdb.firebaseio.com/"
}

firebase = pyrebase.initialize_app(Config)
auth = firebase.auth()
db = firebase.database()

app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = 'super-secret-key'

#Code goes below here







#Code goes above here

if __name__ == '__main__':
    app.run(debug=True)