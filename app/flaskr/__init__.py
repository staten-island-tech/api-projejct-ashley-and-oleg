from flask import Flask, render_template
import requests
import json

# r = requests.get("https://api.bestbuy.com/v1/products/trendingViewed(categoryId=abcat0400000)?apiKey=tyP7wRXV364rYiZc16B7dJAt").json()
# print(r)
# r = requests.get("https://api.bestbuy.com/v1/products/8880044/alsoViewed?apiKey=tyP7wRXV364rYiZc16B7dJAt").json()
# print(r)
data = requests.get("https://api.bestbuy.com/v1/products/trendingViewed(categoryId=abcat0400000)?apiKey=tyP7wRXV364rYiZc16B7dJAt").json()
data2 = requests.get("https://api.bestbuy.com/v1/products/8880044/alsoViewed?apiKey=tyP7wRXV364rYiZc16B7dJAt").json()
app = Flask(__name__)

@app.route("/")
def home():
    return render_template('homepage.html', data=data, data2=data2)