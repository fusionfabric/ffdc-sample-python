from flask import Flask, session, render_template
import requests
import os
import json
import helpers

app = Flask(__name__)

# Global variables
client_id = os.getenv("CLIENT_ID")
access_key = os.getenv("CLIENT_SECRET")
token_endpoint = os.getenv("TOKEN_URL")
base_url = os.getenv("BASE_URL")
strong = os.getenv("STRONG")=='True'

# Main page
@app.route('/')
def auth():
    return render_template('index.html', strong=strong)

# Log in
@app.route("/login", methods=["GET","POST"])
def login():
    
    data = {'grant_type':'client_credentials'}
    if(strong):
        data['client_assertion_type'] = 'urn:ietf:params:oauth:client-assertion-type:jwt-bearer'
        data['client_assertion'] = helpers.jwToken()
    else:
        data['client_id'] = client_id
        data['client_secret'] = access_key    
   
    headers = {'Content-Type':'application/x-www-form-urlencoded'}    
    r = requests.post(token_endpoint, headers=headers, data=data)
    response =  r.json()
    
    if (r.status_code is 200):         
        token = response['access_token']
        # Put token in the session
        session['session_token'] = token    
    
    return render_template('auth.html', token=token, strong=strong)

# Display the results
@app.route('/results')
def results():
    try:
        headers={"Authorization": "Bearer " + session['session_token']}
        result = requests.get(base_url + '/referential/v1/countries', headers=headers)
        json_data = json.loads(result.text)['countries']
        return render_template('results.html', results=json_data, strong=strong)
    except:
        return render_template('error.html', error="Unauthorized!", strong=strong)

# Logout
@app.route('/logout')
def logout():  
    session['session_token']=''
    return render_template('logout.html', error="You successfully removed the access token.", strong=strong)

# Main script
if __name__ == "__main__":
    # This allows us to use a plain HTTP callback
    os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = "1"

    app.secret_key = os.urandom(24)
    app.run(debug=True, host='0.0.0.0')