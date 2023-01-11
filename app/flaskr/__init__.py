from flask import Flask, render_template
import requests
import json

data = requests.get("https://api.bestbuy.com/v1/products/trendingViewed(categoryId=abcat0400000)?format=json&show=name,salePrice,description,image&apiKey=tyP7wRXV364rYiZc16B7dJAt").json()
data2 = requests.get("https://api.bestbuy.com/v1/products/8880044/alsoViewed?apiKey=tyP7wRXV364rYiZc16B7dJAt").json()
app = Flask(__name__)

@app.route("/")
def home():
    return render_template('mainpage.html', data=data, data2=data2)
@app.route("/product/<path:product>")
def poopy(product):
    for sku in data['results']:
        if product in sku['sku']:
            return render_template('product.html')
        else:
            return('U SUCK LOL')
