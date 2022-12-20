import requests
import json

r = requests.get("https://api.bestbuy.com/v1/products/trendingViewed(categoryId=abcat0400000)?apiKey=tyP7wRXV364rYiZc16B7dJAt").json()
print(r)