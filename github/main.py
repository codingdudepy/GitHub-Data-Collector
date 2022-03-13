#Importing required modules
from distutils.log import debug
from posixpath import split
from flask import Flask, render_template, request, send_from_directory
import base64
from github import Github
import requests
from flask import Markup
import gunicorn
app = Flask(__name__)
import os
from flask import Flask,render_template,request,redirect
import smtplib, ssl
from flask_mail import Mail, Message


#defining flask name
app = Flask(__name__)

#Defining favicon (Still in development of fixing server issues with heroku displaying corrrect info)
@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static', 'images'),
                               'unnamed.ico', mimetype='image/png') 

#Defining home page(form.html)
@app.route('/')
def form():
    return render_template('form.html')

#Defining repo function
@app.route('/repo', methods = ['POST', 'GET'])
def repo():
    if request.method == 'POST':
        names = request.form['names']
        return redirect(f"/users/{names}")

#Defining repo function for returning data
@app.route('/users/<names>')
def users(names):
    g = Github()
    repo_list = []
    user = g.get_user(names)
    for repo in user.get_repos():
        repo_list.append("<br>")

        repo_list.append(repo.full_name)

   
    return render_template("repo.html", splits = Markup(f'<b>Repos:</b> {repo_list}<br>')
)







#Returning output for user data
@app.route('/output', methods = ['POST', 'GET'])
def verify():
    if request.method == 'POST':
        name = request.form['name']
        return redirect(f"/user/{name}")
 
@app.route('/user/<name>', methods =["GET", "POST"])
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


    return render_template("data.html",  splits = Markup(f'<b>Bio:</b> {bio}<br><b>Followers:</b> {followers}<br><b>Following:</b> {following}<br><b>Public Repos:</b> {public}<br><b>Company:</b> {company}<br><b>ID:</b> {id}<br><b>Avatar:</b> {avatar}<br><b>Twitter username: @</b>{twitter}<br><b>Blog:</b> {blog}<br><b>Location:</b> {location}')
)







@app.route('/email', methods = ['POST', 'GET'])
def verifys():
    if request.method == 'POST':
        namea = request.form['namea']
        nameswa = request.form['namesw']

        return redirect(f"/userss/{namea}/{nameswa}")




@app.route('/userss/<namea>/<nameswa>', methods =["GET", "POST"])
def userss(namea, nameswa):
    mail= Mail(app)

    app.config['MAIL_SERVER']='smtp.gmail.com'
    app.config['MAIL_PORT'] = 465
    app.config['MAIL_USERNAME'] = 'githubdatacollection21@gmail.com'
    app.config['MAIL_PASSWORD'] = '*********'
    app.config['MAIL_USE_TLS'] = False
    app.config['MAIL_USE_SSL'] = True
    mail = Mail(app)

    url = f"https://api.github.com/users/{namea}"
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
    splits = Markup(f'<b>Bio:</b> {bio}<br><b>Followers:</b> {followers}<br><b>Following:</b> {following}<br><b>Public Repos:</b> {public}<br><b>Company:</b> {company}<br><b>ID:</b> {id}<br><b>Avatar:</b> {avatar}<br><b>Twitter username: @</b>{twitter}<br><b>Blog:</b> {blog}<br><b>Location:</b> {location}')
    msg = Message('Hello', sender = 'githubdatacollection21@gmail.com', recipients = [nameswa])
    msg.body = splits
    mail.send(msg)
    return render_template("data.html",   splits = Markup(f'<b>Bio:</b> {bio}<br><b>Followers:</b> {followers}<br><b>Following:</b> {following}<br><b>Public Repos:</b> {public}<br><b>Company:</b> {company}<br><b>ID:</b> {id}<br><b>Avatar:</b> {avatar}<br><b>Twitter username: @</b>{twitter}<br><b>Blog:</b> {blog}<br><b>Location:</b> {location}')
)
    

#Running Flask
if __name__ == "__main__":
    app.run(debug=True)