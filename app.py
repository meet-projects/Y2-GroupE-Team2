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
  "databaseURL": "https://ukko-project-default-rtdb.firebaseio.com/"
}

firebase = pyrebase.initialize_app(Config)
auth = firebase.auth()
db = firebase.database()

app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = 'super-secret-key'

#Code goes below here

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template("index.html")


@app.route('/learn_more', methods=['GET', 'POST'])
def learn():
    return render_template("learn.html")


@app.route('/products', methods=['GET', 'POST'])
def products():

    try:
        products = db.child("Products").get().val()
        return render_template("products.html", products=products)
    except:
        return render_template("products.html")

@app.route('/pro/<string:product_id>',methods=['GET','POST'])
def pro(product_id):
    product = db.child("Products").child(product_id).get().val()

    if request.method=="POST":
        try:
            review=request.form['review']
            db.child("Reviews").child(product_id).push(review)
            reviews= db.child("Reviews").child(product_id).get().val()
            return render_template("pro.html", reviews=reviews,product_id=product_id,product=product)
        except:
            return render_template("pro.html")
    return render_template("pro.html",product_id=product_id,product=product)



@app.route('/add_product', methods=['GET','POST'])
def add_product():
    if request.method == "POST":
        try:
            title=request.form['title']
            img=request.form['image']
            text=request.form['text']
            product={"title": title, "img": img, "text":text }
            db.child("Products").push(product)
        except:
            return render_template("add_product.html")
    return render_template("add_product.html")

@app.route('/index')
def index():
    return render_template("index.html")



# @app.route('/review/<string:product_id>', methods=['GET','POST'])
# def review(product_id):
#     if request.method=="POST":
#         try:
#             review=request.form['review']
#             db.child("Reviews").child(product_id).push(review)
#             reviews= db.child("Reviews").child(product_id).get().val()
#             return (url_for('review'))
#             #return render_template("pro.html", reviews=reviews)
#         except:
#             return render_template("pro.html")
#     return render_template("pro.html")        



#Code goes above here

if __name__ == '__main__':
    app.run(debug=True)