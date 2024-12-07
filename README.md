The given instructions relate to executing and testing a secure chat application while demonstrating its vulnerability to Man-In-The-Middle (MITM) attacks. Below is an explanation and clarification of the unique terms and concepts mentioned:

Unique Words & Phrases:
Alice: Represents a client/user in cryptographic demonstrations who communicates with Bob.

Bob: Acts as a server or the recipient of messages from Alice in the application.

Trudy: Represents the attacker who performs MITM or downgrade attacks to intercept and manipulate communications.

Secure Chat Application: A hypothetical or real chat program designed with security features to protect user communication.

MITM (Man-In-The-Middle):

An attack where the attacker secretly intercepts or alters the communication between two parties (Alice and Bob).
Poison DNS:

A DNS spoofing attack where the attacker corrupts the DNS cache to redirect users to a malicious address.
Downgrade Attack:

A type of cyberattack where the attacker forces a secure connection to switch to a less secure protocol or encryption.
secure_chat_app:

The script or application used to simulate secure communication between Alice and Bob.
secure_chat_interceptor.py:

A script likely used by Trudy to perform MITM attacks, such as intercepting or downgrading communication.
-s Flag:

Indicates the script is being run in server mode (Bob's mode).
-c Flag:

Indicates the script is being run in client mode (Alice's mode).
-d Flag:

Likely specifies downgrade attack mode for Trudy's script.
-m Flag:

Possibly specifies MITM attack mode, where Trudy actively intercepts communication.
alice1 / bob1:

Identifiers or parameters used for the client/server during communication or to distinguish specific users.
Task 2, Task 3, Task 4:

Different stages of the experiment:
Task 2: Establish a secure connection between Alice and Bob.
Task 3: Demonstrate a downgrade attack.
Task 4: Perform a full MITM attack with DNS poisoning.
