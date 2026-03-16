import requests

# 1. CONFIGURATION (Matching your screenshot)
BASE_URL = "http://localhost:8080"
REALM = "CyberLab-ENT"
CLIENT_ID = "automation-script"
CLIENT_SECRET = "m9OyQsuUX13oLK8KTk3t98bkjHwWeboF"
TARGET_USER = "jdoe_cyber"
NEW_ROLE_ID = "9e90feb1-3ce4-4d1c-a67a-49c241ea0ad4"
NEW_ROLE_NAME = "DevOps-Engineer"

# 2. Get Access Token
token_url = f"{BASE_URL}/realms/{REALM}/protocol/openid-connect/token"
data = {"grant_type": "client_credentials", "client_id": CLIENT_ID, "client_secret": CLIENT_SECRET}
r_token = requests.post(token_url, data=data)
token = r_token.json().get("access_token")
headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}

# 3. Search for User (The Debugger)
search_url = f"{BASE_URL}/admin/realms/{REALM}/users?username={TARGET_USER}"
print(f"DEBUG: Searching at {search_url}")

response = requests.get(search_url, headers=headers)
user_list = response.json()

if not user_list:
    print(f"[!] ERROR: No user found. Check Keycloak UI for realm '{REALM}' and user '{TARGET_USER}'")
    exit()

user_id = user_list[0]['id']
print(f"[+] Found User ID: {user_id}")

# 4. PERFORM THE SWAP
# Assign new role
role_payload = [{"id": NEW_ROLE_ID, "name": NEW_ROLE_NAME}]
requests.post(f"{BASE_URL}/admin/realms/{REALM}/users/{user_id}/role-mappings/realm", json=role_payload, headers=headers)

print(f"SUCCESS: {TARGET_USER} has been updated.")
