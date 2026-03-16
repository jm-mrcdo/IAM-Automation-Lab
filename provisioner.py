import requests

# CONFIGURATION
KEYCLOAK_URL = "http://localhost:8080"
REALM_NAME = "CyberLab-ENT"
CLIENT_ID = "automation-script"
CLIENT_SECRET = "CLIENT_SECRET_HERE"

# 1. Get Access Token (The Script "Logs In")
token_url = f"http://localhost:8080/realms/{REALM_NAME}/protocol/openid-connect/token"
token_data = {
    "grant_type": "client_credentials",
    "client_id": CLIENT_ID,
    "client_secret": CLIENT_SECRET,
}
r = requests.post(token_url, data=token_data)
token = r.json().get("access_token")
headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}

# 2. Function to provision a user
# 2. Updated Provisioning Function
def provision_user(username, first, last, is_contractor=False):
    user_url = f"{KEYCLOAK_URL}/admin/realms/{REALM_NAME}/users"
    
    # Logic: Contractors get emailVerified=False, Employees get True
    email_status = not is_contractor 
    user_role = "Contractor" if is_contractor else "Employee"

    user_payload = {
        "username": username,
        "firstName": first,
        "lastName": last,
        "enabled": True,
        "emailVerified": email_status,
        "attributes": {
            "User-Type": ["contractor"],
            "Project": ["Tokyo-Drifters-Imports"]
        }
    }
    
    response = requests.post(user_url, json=user_payload, headers=headers)
    if response.status_code == 201:
        print(f"[+] Successfully provisioned: {username} ({user_role})")
    elif response.status_code == 409:
        print(f"[-] MPTE: {username} already exists in {REALM_NAME}. Skipping Creation.") 
    else:
        # If user already exists, it will show an error here
        print(f"[!] ERROR FOR {username}: {response.status_code} - {response.text}")

# 3. THE "HR FEED" (Simulating New Hires)
new_hires = [
    {"u": "jdoe_cyber", "f": "John", "l": "Doe"},
    {"u": "mscarlet_sec", "f": "Miss", "l": "Scarlet"},
    {"u": "pwhite_iam", "f": "Professor", "l": "White"},
    {"u": "audit_01_ext", "f": "auditor", "l": "01"},
    {"u": "audit_02_ext", "f": "auditor 2", "l": "02"}
]

# 4. Execution Loop
print(f"Starting Provisioning Batch for {REALM_NAME}...")

for person in new_hires:
    # If the username contains 'audit', they are treated as contractors
    is_ext = "audit" in person['u']
    provision_user(person['u'], person['f'], person['l'], is_contractor=is_ext)
