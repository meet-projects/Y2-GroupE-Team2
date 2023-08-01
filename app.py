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
db = firebase.database()

app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = 'super-secret-key'

#Code goes below here

@app.route('/', methods=['GET', 'POST'])
def home():
    try:
        print("we're in the try clause")
        products = db.child("Products").get().val()
        print(products)
        return render_template("index.html", products=products)
    
    except:
        return render_template("index.html")


@app.route('/p/<string:name>', methods=['GET','POST'])
def product(name):
    product = db.child("Products").child(name).get().val()
    reviews= db.child("Reviews").child(name).get().val()
    if request.method=="POST":
        try:
            text=request.form['review']
            review={"review":text}
            db.child("Reviews").child(name).push(review)
            #reviews= db.child("Reviews").child(name).get().val()
            return render_template("portfolio-details.html", reviews=reviews,name=name,product=product)
        except:
            return render_template("portfolio-details.html")
    return render_template("portfolio-details.html",name=name,product=product,reviews=reviews)


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



@app.route('/review/<string:product_id>', methods=['GET','POST'])
def review(product_id):
    if request.method=="POST":
        try:
            review=request.form['review']
            db.child("Reviews").child(product_id).push(review)
            reviews= db.child("Reviews").child(product_id).get().val()
            product = db.child("Products").child(name).get().val()
            return render_template("", reviews=reviews,product=product )
        except:
            return render_template("portfolio-details.html")
    return render_template("portfolio-details.html")        



#Code goes above here

if __name__ == '__main__':
    app.run(debug=True)