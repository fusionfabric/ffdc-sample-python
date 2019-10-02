from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend
import os
import jwt
from datetime import datetime
from datetime import timedelta
import uuid  

client_id = os.getenv("CLIENT_ID")
login_url = os.getenv("BASE_LOGIN")
key = os.getenv("KEYID")

token_expiration = (datetime.now() + timedelta(minutes=30)).timestamp() 

def jwToken():
    payload = {}

    payload['jti'] = str(uuid.uuid4())    
    payload['exp'] = token_expiration 
    payload['iss'] = client_id
    payload['aud'] = login_url
    payload['sub'] = client_id  
      
    headers = {}  
    headers['kid'] = key 
       
    with open("private.pem", "rb") as key_file:
        private_key = serialization.load_pem_private_key(
            key_file.read(),
            password=None,
            backend=default_backend()
        )

    encoded_jwt = jwt.encode(payload, private_key,
                            algorithm='RS256', headers=headers)
   
    return encoded_jwt