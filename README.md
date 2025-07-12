# secure-email-network-analysis
This project demonstrates how to implement secure email communication using **PGP encryption via ProtonMail**, and analyze network traffic to detect anomalies using **Wireshark**.

## 🔐 Part 1: Secure Email with PGP


### 🔧 Tools/Libraries Used
- ProtonMail
- OPENPGP
- GNUPG
- smtplib / email modules Python
- GPG
-  temporary email links: 
a. https://www.guerrillamail.com/inbox 
b. https://temp-mail.org/


### 📌 Features
- Encrypts messages using PGP public key.
- Sends email securely via ProtonMail SMTP server.
- Demonstrates privacy-focused communication.

### 🚀 Implementation of Secure email with PGP Encryption
-  Created an account in Protonmail

🔑 Exporting Recipient's Public Key from ProtonMail
- Log in to the recipient's ProtonMail account.
- Navigate to: Settings → Encryption & Keys or Settings → Keys (depending on UI version).
- Click on EXPORT in the "Actions" column.
- Choose PUBLIC KEY to download a .asc file (e.g., recipient_public_key.asc).

<img width="1816" height="813" alt="image" src="https://github.com/user-attachments/assets/6a3fcbde-b0fd-40fb-ac74-367a4ee6e773" />
<img width="788" height="267" alt="image" src="https://github.com/user-attachments/assets/2778c55a-61b9-4903-bcd8-74fe128f9ab5" />


















