from flask import Flask, render_template, request
import requests
import json

data = requests.get("https://api.bestbuy.com/v1/products/trendingViewed(categoryId=abcat0400000)?format=json&show=name,salePrice,description,image&apiKey=tyP7wRXV364rYiZc16B7dJAt").json()

data2 = requests.get("https://api.bestbuy.com/v1/products/mostViewed(categoryId=abcat0107000)?format=json&show=name,salePrice,description,image&apiKey=tyP7wRXV364rYiZc16B7dJAt").json()

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('mainpage.html', data=data, data2=data2)

@app.route("/camera/")
def getStuff():
    return render_template('dropdown1.html', data=data)

@app.route("/antenna/")
def getAntenna():
    return render_template('dropdown2.html', data2=data2)

@app.route("/InsigniaProducts/")
def getInsigniaProducts():
    return render_template('dropdown3.html', data2=data2)


@app.route('/', methods=('GET', 'POST'))
def getPost():
    
    if request.method == 'POST':
        title = request.form['names']
        data = requests.get(f"'https://api.bestbuy.com/v1/products/mostViewed(categoryId=abcat0107000)?format=json&show=name,salePrice,description,image&apiKey=tyP7wRXV364rYiZc16B7dJAt{title}").json()
        print(data)
        return render_template('test.html',data=data)
    else:
        return render_template('mainpage.html')


@app.route("/product/<path:product>")
def poopy(product):
    for x in data['results']:
        if x["sku"] == product:
            return render_template('product.html', x=x)
