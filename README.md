# Enterprise IAM Lifecycle Automation (JML)
This project demonstrates an automated **Joiner-Mover-Leaver (JML)** lifecycle using **Python** and **Keycloak (OIDC)**.

##  Project Overview
In a corporate environment, manual user management is a security risk. This project automates the identity lifecycle to ensure **Least Privilege** and rapid **Incident Response**.

## Why I Made This
I built this automation suite to bridge the gap between Identity Management and Security Operations. My goal was to prove that IAM isn't just a business process; it’s a critical security defense that can be automated to reduce human error and minimize the attack surface of an organization.

## Technical Stack
* **Identity Provider:** Keycloak (IAM)
* **Language:** Python 3
* **Protocol:** OAuth2 / OpenID Connect
* **Platform:** Docker / Kali Linux

##  The Three Phases
1. **Joiner (`provisioner.py`):** Automates onboarding. It creates users with specific security metadata and enforces email verification for external auditors.
2. **Mover (`role_swap.py`):** Prevents "Privilege Creep" by programmatically revoking old roles and assigning new ones during department transfers.
3. **Leaver (`kill_switch.py`):** An emergency response script that disables a user account and instantly revokes all active web sessions.

## Security Highlights
* **RBAC Implementation:** Role-Based Access Control via Keycloak API.
* **Token-Based Auth:** Secure communication using Client Credentials flow.
* **Session Revocation:** Demonstrates ability to mitigate active threats by killing OIDC sessions.
