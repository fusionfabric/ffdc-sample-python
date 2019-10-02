# Welcome

This sample client application is an implementation of the OAuth2 Client Credentials authorization grant flow for FusionFabric.cloud.

**To run this sample**
> You need a recent installation of Python. Download and install it from [python.org](https://www.python.org/downloads/).

1. Open a Command Prompt or a Terminal and install the required Python packages with
 `pip install requests_oauthlib flask python-dotenv pyjwt cryptography` 
2. Register an application on [**Fusion**Fabric.cloud Developer Portal](https://developer.fusionfabric.cloud), and include the **Referential Data** API. Use `*` as the reply URL.
3. Clone the current project.
4. Copy `.env.sample` to `.env`, open it and enter `<%YOUR-CLIENT-ID%>`, and `<%YOUR-SECRET-KEY%>` of the application created at the step 2. 

> The value for `<%TOKEN_URL%>` is provided by the [Discovery service](https://developer.fusionfabric.cloud/documentation?workspace=FusionCreator%20Developer%20Portal&board=Home&uri=oauth2-grants.html#discovery-service) of the **Fusion**Fabric.cloud Developer Portal.

5. (Optional) If you want to use private key authentication, instead of the standard authentication based on secret value, follow [the steps from the documentation](https://developer.fusionfabric.cloud/documentation?workspace=FusionCreator%20Developer%20Portal&board=Home&uri=oauth2-grants.html#jwk-auth-procedure) to sign and upload a JSON Web Key to your application, and save the private RSA key in a file named **private.pem**. Edit `.env` as follows:
+ remove or comment the line containing the secret value: 
```
# CLIENT_SECRET="<%YOUR-SECRET-KEY%>"
```
+ set `STRONG=True`

6. Open a Command Prompt or a Terminal in this directory and run the application with `python Client-Credential.py`. The application has started running. 
7. Point your browser to http://localhost:5000. The homepage of the sample application opens.   
8. (Optional) Click 
	+ **Acquire Access Token** to get the confirmation of authentication and display the token.
	+ **Get Data** to get the lists of countries with their names, currency and codes, from the **Referential Data** API.
	+ **Remove Access Token** to display a confirmation message upon a successful removal of the access token.