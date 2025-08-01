# email-encryption-network-analysis
This project demonstrates how to implement secure email communication using **PGP encryption via ProtonMail**, and analyze network traffic to detect anomalies using **Wireshark**.

## 🔐 Part 1: Secure Email communication using PGP & Protonamil


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

🔁 Importing the Recipient’s Public Key
Step 1: Import the Public Key
<img width="1212" height="207" alt="image" src="https://github.com/user-attachments/assets/beb090db-0b54-46db-b2de-dcd72f317284" />
Step 2: Verify the Key Was Imported
<img width="1002" height="252" alt="image" src="https://github.com/user-attachments/assets/ac16c3c7-55ef-4339-b3ef-9ec507acd812" />

✉️ Composing & Encrypting the Message
📝 Step 1: Create a plain text file with a message ( which is secure) - example
<img width="610" height="162" alt="image" src="https://github.com/user-attachments/assets/c23bfe83-d8fc-467a-afca-e9e6cd44edfb" />
🔐 Step 2: Encrypt the Message 
gpg --encrypt --recipient username@protonmail.com filename.txt
<img width="1126" height="275" alt="image" src="https://github.com/user-attachments/assets/b12401a7-36c0-46d0-bc86-98fd04984eca" />
<img width="847" height="307" alt="image" src="https://github.com/user-attachments/assets/84fc832f-5f61-413d-bb2a-a241586e1b29" />

📧 Sending the Encrypted Message via Disposable Email
To test the delivery and decryption of the encrypted message without revealing your actual email identity, you can use a disposable email service.
🔗 Tools Used
https://temp-mail.org/ (Used in this project)
Alternatively: https://www.guerrillamail.com/

✉️ Steps to Send the Email
cat secret-message.txt.asc, Copy the entire contents (including -----BEGIN PGP MESSAGE----- to -----END PGP MESSAGE-----).
Go to the compose message section of Temp-Mail - Add Recipient Email, Subject, Body: Paste the contents of secret-message.txt.asc
<img width="800" height="507" alt="image" src="https://github.com/user-attachments/assets/4a630351-9f25-4eae-a4be-c4a025e7f06d" />

✅ Verifying End-to-End Encryption
Once the message is received in the ProtonMail inbox:
- A green padlock icon next to the sender indicates the message was encrypted end-to-end.
- The subject and body content will match exactly with the encrypted content sent.
- The message will be automatically decrypted and displayed (since the private key resides in the recipient’s ProtonMail account).
<img width="1127" height="515" alt="image" src="https://github.com/user-attachments/assets/f1264e40-5977-42c4-80dd-5873ed96e890" />
<img width="1201" height="516" alt="image" src="https://github.com/user-attachments/assets/b8196d21-6e87-4ef3-a9b0-0b81a2e3550e" />

🔒 This verifies that the message was successfully encrypted, securely delivered, and decrypted using OpenPGP.


## 🔐 Part 2: Python Script To Send Emails Using SMTP 

Apart from using disposable email, you can also auto-send encrypted messages securely using any account (used gmail in this project) using Python script.
🧪 Sample Script: test.py
<img width="1027" height="560" alt="image" src="https://github.com/user-attachments/assets/fb7751ff-ccca-47ac-b6b9-8dd35514d6e6" />

## 🧠 Part 3: Network Traffic Analysis with Wireshark
✅ Analyzing Suspicious IPs
✅ Protocol Inspection - Inspected TCP,HTTP, DNS, and SMTP traffic for suspicious payloads, malformed headers, or unexpected destinations.
✅ Used display filters

<img width="1028" height="623" alt="image" src="https://github.com/user-attachments/assets/7a4433bd-3441-4a72-9e11-a5f038847235" />
<img width="1070" height="603" alt="image" src="https://github.com/user-attachments/assets/3e1148aa-4645-4c70-899e-cc93459abba5" />
<img width="797" height="717" alt="image" src="https://github.com/user-attachments/assets/956adc38-d98d-4847-8766-02c515169d0b" />
<img width="727" height="529" alt="image" src="https://github.com/user-attachments/assets/c79a0c3e-8822-4a6b-b4b2-852e67dbe61d" />
<img width="775" height="365" alt="image" src="https://github.com/user-attachments/assets/e7c4477c-5769-4456-80ce-875b58066177" />












