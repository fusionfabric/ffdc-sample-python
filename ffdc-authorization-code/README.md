# Welcome

This sample client application is an implementation of the OAuth2 Authorization Code authorization grant flow for FusionFabric.cloud.

**To run this sample**

> You need a recent installation of Python. Download and install it from [python.org](https://www.python.org/downloads/).

1. Open a Command Prompt or a Terminal and install these required Python packages:
 `pip install requests_oauthlib flask python-dotenv pyjwt cryptography`
2. Register an application on [**Fusion**Fabric.cloud Developer Portal](https://developer.fusionfabric.cloud), and include the [Static Data for Trade Capture API](https://developer.fusionfabric.cloud/api/trading-trade-capture-static-data-8faddb99-a71f-464d-9c3d-2220baacc299/docs). Use `http://localhost:5000/callback` as the reply URL.
3. Clone the current project.
4. Copy `.env.sample` to `.env`, open it and enter `<%YOUR-CLIENT-ID%>`, and `<%YOUR-SECRET-KEY%>` of the application created at the step 2. 

> The values for `<%TOKEN-URL%>`, `<%AUTHORIZATION-URL%>` and `<%SCOPE%>` are provided by the [Discovery service](https://developer.fusionfabric.cloud/documentation/oauth2-grants#discovery-service) of the **Fusion**Fabric.cloud Developer Portal.

5. (Optional) If you want to use private key authentication, instead of the standard authentication based on secret value, follow [the steps from the documentation](https://developer.fusionfabric.cloud/ffdc-documentation/oauth2-grants.html#jwk-auth-procedure) to sign and upload a JSON Web Key to your application, and save the private RSA key in a file named **private.pem**. Edit `.env` as follows:
+ remove or comment the line containing the secret value: 
```
# CLIENT_SECRET="<%YOUR-SECRET-KEY%>"
```
+ set `STRONG=True`

6. Open a Command Prompt or a Terminal in this directory and run the application with `python Authorization-Code.py`. The application has started running. 
7. Point your browser to http://localhost:5000. Click **Login**. You are redirected to the **Fusion**Fabric.cloud Developer Portal Authorization Server.
8. Click **Login** and use one of the following credentials to log into Finastra's Authorization Server:

| User        | Password |
| :---------- | :------- |
| `ffdcuser1` | `123456` |
| `ffdcuser2` | `123456` |

The home page of this sample application is displayed.

8. (Optional) Click **Get Data** to get the lists of the legal entities from the **Static Data for Trade Capture** API.
