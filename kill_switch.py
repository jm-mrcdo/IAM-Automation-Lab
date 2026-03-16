import requests

# 1. CONFIGURATION
BASE_URL = "http://localhost:8080"
REALM = "CyberLab-ENT"
CLIENT_ID = "automation-script"
CLIENT_SECRET = "CLIENT_SECRET_HERE"
TARGET_USER = "audit_01_ext" # We'll test this on one of the auditors

# 2. Get Access Token
token_url = f"{BASE_URL}/realms/{REALM}/protocol/openid-connect/token"
data = {"grant_type": "client_credentials", "client_id": CLIENT_ID, "client_secret": CLIENT_SECRET}
token = requests.post(token_url, data=data).json().get("access_token")
headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}

# 3. Find User ID
search_url = f"{BASE_URL}/admin/realms/{REALM}/users?username={TARGET_USER}"
user_list = requests.get(search_url, headers=headers).json()

if not user_list:
    print(f"[!] User {TARGET_USER} not found.")
    exit()

user_id = user_list[0]['id']

# 4. THE KILL SWITCH
# Action A: Disable the account (sets 'enabled' to False)
disable_url = f"{BASE_URL}/admin/realms/{REALM}/users/{user_id}"
requests.put(disable_url, json={"enabled": False}, headers=headers)

# Action B: Logout (Revokes all active sessions)
logout_url = f"{BASE_URL}/admin/realms/{REALM}/users/{user_id}/logout"
requests.post(logout_url, headers=headers)

print(f"[-] TERMINATED: {TARGET_USER} has been disabled and all sessions revoked.")
