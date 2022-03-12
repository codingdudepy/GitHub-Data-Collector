# GitHub-Bot
💻A bot and future website that gets github data using the github API
If you do not want to install the bot via code and host it yourself your more then welcome to use my link for it and invite it to your server to get updates whenever they happen! 
<a href="https://discord.com/api/oauth2/authorize?client_id=949120605549125632&permissions=277025770560&scope=bot">Invite Link For Bot</a>
<h1>Setup</h1>
<ul>
  <li>Get a bot token from the discord bot development portal if you need help please go <a href="https://www.youtube.com/watch?v=b61kcgfOm_4">to this video</a></li>
  <li>Then replace where it says token on the last line to the actual token. This can be put in a variable, doesnt matter</li>
  <li>Install the required packages listed below</li>
</ul>

# Packages
````
pip install discord.py
````
````
pip install PyGithub requests
````

# Updates
I plan to continue updating this project eventually making it into a webiste so keep your eyes peeled! If you have any suggestions feel free to contact me on twitter or submit a pr if you have code

# GitHub Website
The <a href="https://githubdatacollection.herokuapp.com/">GitHub website</a> is fairly easy to use I used heroku to deploy but you can use any hosting service you want that works with flask. However, for heroku if you want to use it please install all the files in the folder. If your not using heroku you can delete the following files:
<br>
<ul>
  <li>Procfile</li>
  <li>wsgi.py</li>
  <li>requirements.txt</li>
</ul>
