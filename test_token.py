import requests

# CONFIG - CHANGE THESE TWO
REALM_NAME = "CyberLab-ENT" # Or "master" based on Step 1
SECRET = "m9OyQsuUX13oLK8KTk3t98bkjHwWeboF"

url = f"http://localhost:8080/realms/{REALM_NAME}/protocol/openid-connect/token"
data = {
    "grant_type": "client_credentials",
    "client_id": "automation-script",
    "client_secret": SECRET
}

print(f"Testing connection to: {url}")
r = requests.post(url, data=data)

print(f"Status Code: {r.status_code}")
print(f"Response: {r.text}")
