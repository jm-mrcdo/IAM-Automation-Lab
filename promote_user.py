import requests

# CONFIGURATION
KEYCLOAK_URL = "http://localhost:8080"
REALM = "CyberLab-ENT"
CLIENT_ID = "automation-script"
CLIENT_SECRET = "m9OyQsuUX13oLK8KTk3t98bkjHwWeboF"
TARGET_USERNAME = "pwhite_iam"  # We are promoting Professor White
ROLE_ID = "caf7ecc5-87b6-405b-b134-d24bdd04b036"
ROLE_NAME = "Manager"

# 1. Get Access Token
token_url = f"{KEYCLOAK_URL}/realms/{REALM}/protocol/openid-connect/token"
data = {"grant_type": "client_credentials", "client_id": CLIENT_ID, "client_secret": CLIENT_SECRET}
token = requests.post(token_url, data=data).json().get("access_token")
headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}

# 2. Find the User's Internal ID
user_search = requests.get(f"{KEYCLOAK_URL}/admin/realms/{REALM}/users?username={TARGET_USERNAME}", headers=headers)
user_uuid = user_search.json()[0]['id']

# 3. PROMOTE: Assign the Manager Role
role_data = [{"id": ROLE_ID, "name": ROLE_NAME}]
promote_url = f"{KEYCLOAK_URL}/admin/realms/{REALM}/users/{user_uuid}/role-mappings/realm"

response = requests.post(promote_url, json=role_data, headers=headers)

if response.status_code == 204:
    print(f"SUCCESS: {TARGET_USERNAME} has been promoted to {ROLE_NAME}!")
else:
    print(f"FAILED: {response.text}")
