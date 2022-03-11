from distutils.log import debug
from flask import Flask, render_template, request
import base64
from github import Github
import requests
from flask import Markup
import gunicorn
app = Flask(__name__)

from flask import Flask,render_template,request,redirect
 
app = Flask(__name__)
 
@app.route('/')
def form():
    return render_template('form.html')
 
@app.route('/output', methods = ['POST', 'GET'])
def verify():
    if request.method == 'POST':
        name = request.form['name']
        return redirect(f"/user/{name}")
 
@app.route('/user/<name>')
def user(name):
    url = f"https://api.github.com/users/{name}"
    user_data = requests.get(url).json()
    bio = (str(user_data["bio"]))
    followers = (int(user_data["followers"]))
    following = (int(user_data["following"]))
    public = (str(user_data["public_repos"]))
    company = (str(user_data["company"]))
    id = (int(user_data["id"]))
    avatar = (str(user_data["avatar_url"]))
    twitter = (str(user_data["twitter_username"]))
    blog = (str(user_data["blog"]))
    location = (str(user_data["location"]))

    return render_template("data.html", split = Markup(f'<b>Bio:</b> {bio}<br><b>Followers:</b> {followers}<br><b>Following:</b> {following}<br><b>Public Repos:</b> {public}<br><b>Company:</b> {company}<br><b>ID:</b> {id}<br><b>Avatar:</b> {avatar}<br><b>Twitter username:</b> {twitter}<br><b>Blog:</b> {blog}<br><b>Location:</b> {location}')
)

    
 
 


if __name__ == "__main__":
    app.run()