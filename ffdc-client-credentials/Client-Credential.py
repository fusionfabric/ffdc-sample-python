from oauthlib.oauth2 import BackendApplicationClient
from requests_oauthlib import OAuth2Session
from flask import Flask, request, redirect, session, render_template
from flask import session
import os
import urllib.parse as urlparse
import json
from dotenv import load_dotenv

app = Flask(__name__)

# Global variables
load_dotenv()
client_id = os.getenv("CLIENT_ID")
access_key = os.getenv("CLIENT_SECRET")
token_endpoint = os.getenv("TOKEN_URL")
base_url = os.getenv("BASE_URL")

oauth = None

# Main page
@app.route('/')
def auth():
    return render_template('index.html')


#Get the token using the client credentials
@app.route("/login")
def demo():
    client = BackendApplicationClient(client_id=client_id)
  
    global oauth
    oauth = OAuth2Session(client=client)
    
    token = oauth.fetch_token(token_url=token_endpoint,
                              client_id=client_id,
                              client_secret=access_key)

    return render_template('auth.html', token=token['access_token'])

# Display the results
@app.route('/results')
def results():
    try:
        result = oauth.get(base_url + '/referential/v1/countries')
        json_data = json.loads(result.text)['countries']
        return render_template('results.html', results=json_data)
    except:
        return render_template('error.html', error="Please Login to get the data")

# Logout
@app.route('/logout')
def logout():
    global oauth
    oauth = None
    return render_template('logout.html', error="You successfully logged out")


# Main script
if __name__ == "__main__":
    # This allows us to use a plain HTTP callback
    os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = "1"

    app.secret_key = os.urandom(24)
    app.run(debug=True, host='0.0.0.0')