from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def home():
    data_list = requests.get(url="https://api.npoint.io/4af156202f984d3464c3").json()
    return render_template("index.html", data=data_list)

@app.route('/post/<post_number>')
def blog_page(post_number):
    data_list = requests.get(url="https://api.npoint.io/4af156202f984d3464c3").json()
    return render_template("post.html", post_number = post_number, data=data_list)


if __name__ == "__main__":
    app.run(debug=True, port=8001)
