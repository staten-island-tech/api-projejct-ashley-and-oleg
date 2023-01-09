from flask import Flask, render_template, request
import requests
import json

data = requests.get("https://api.bestbuy.com/v1/products/mostViewed(categoryId=abcat0107000)?format=json&show=name,salePrice,description,image&apiKey=tyP7wRXV364rYiZc16B7dJAt").json()
data2 = requests.get("https://api.bestbuy.com/v1/products/8880044/alsoViewed?apiKey=tyP7wRXV364rYiZc16B7dJAt").json()
app = Flask(__name__)

@app.route("/")
def home():
    return render_template('mainpage.html', data=data, data2=data2)

@app.route('/', methods=('GET', 'POST'))
def getPost():
    if request.method == 'POST':
        title = request.form['names']
        data = requests.get(f"https://api.bestbuy.com/v1/products/mostViewed(categoryId=abcat0107000)?format=json&show=name,salePrice,description,image&apiKey=tyP7wRXV364rYiZc16B7dJAt/{title}").json()

        print(request.form)
        return render_template('test.html',data=data)
    else:
        return render_template('mainpage.html')

@app.route('/<path>')
def searchbar(cards):
    list = []
    for thing in data or data2:
        list.append(thing)
    if cards in list:
        return render_template('test.html')
