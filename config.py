import boto3
from matchmaking_api_client.client import AuthenticatedClient

CLIENT_ID = "3ns1sc0lkrdqh25qvrqb9k3a80"
USERNAME = "<username>
PASSWORD = "<password>"
GAME_ID = "1v1"
API_URL = "https://api.beta.idem.gg"


def _get_auth_token(username, password, client_id):
    client = boto3.client("cognito-idp", region_name="eu-central-1")
    response = client.initiate_auth(
        AuthFlow="USER_PASSWORD_AUTH",
        AuthParameters={"USERNAME": username, "PASSWORD": password},
        ClientId=client_id,
    )
    return response["AuthenticationResult"]["IdToken"]


token = _get_auth_token(USERNAME, PASSWORD, CLIENT_ID)
client = AuthenticatedClient(base_url=API_URL, token=token)


def get_client():
    global client
    return client
