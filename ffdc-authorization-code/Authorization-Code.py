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
authorization_endpoint = os.getenv("AUTHORIZATION_URL")
token_endpoint = os.getenv("TOKEN_URL")
scope = os.getenv("SCOPE")
redirect_uri = os.getenv("REDIRECT_URI")
base_url = os.getenv("BASE_URL")

oauth = None

# Home page
@app.route('/')
def auth():
    return render_template('index.html')

# Autenticaiton page to get redirect url
@app.route("/login")
def demo():
    oauth = OAuth2Session(client_id, scope=scope, redirect_uri=redirect_uri)
    authorization_url, state = oauth.authorization_url(authorization_endpoint)
    session['oauth_state'] = state
    return redirect(authorization_url)

# Get the token, return the auth page
@app.route("/callback")
def callback():
    url = request.url
    parsed = urlparse.urlparse(url)
    accesscode = urlparse.parse_qs(parsed.query)['code']
    code = accesscode[0]

    global oauth
    oauth = OAuth2Session(client_id,
                          state=session['oauth_state'],
                          redirect_uri=redirect_uri)

    token = oauth.fetch_token(token_endpoint,
                              client_secret=access_key,
                              code=code)

    return render_template('auth.html', token=token['access_token'])

# Display the results
@app.route('/results')
def results():
    try:
        result = oauth.get(base_url + '/capital-market/trade-capture/static-data/v1/reference-sources?applicableEntities=legal-entities')
        json_data = json.loads(result.text)['items']
        return render_template('results.html', results=json_data)
    except:
        return render_template('error.html',
                               error="Please Login to get the data")

# Logout
@app.route('/logout')
def logout():
    global oauth
    oauth = None
    return redirect('/')

# Main script
if __name__ == "__main__":
    # This allows us to use a plain HTTP callback
    os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = "1"
    
    app.secret_key = os.urandom(24)
    app.run(debug=True, host='0.0.0.0')