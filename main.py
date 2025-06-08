import os

from flask import Flask, request, jsonify
import pickle
import os
import random

app = Flask(__name__)

@app.route("/affinity", methods=["POST"])
def affinity_score():
  return str(random.random())

# --- DANGER ZONE ---
# This server demonstrates a SERIOUS VULNERABILITY.
# DO NOT USE pickle.loads() on untrusted data in real applications.
# Its purpose is PURELY EDUCATIONAL to show the risks.
# --- DANGER ZONE ---

# --- Configuration ---
# The server will create this file upon startup. The malicious pickle will attempt to delete it.
FILE_TO_BE_DELETED_BY_PICKLE = "IMPORTANT_FILE_DEMO.txt"

def setup_important_file():
    """Creates or recreates the dummy important file for the demo."""
    # Ensure a clean state or re-create if deleted
    if os.path.exists(FILE_TO_BE_DELETED_BY_PICKLE):
        print(f"[SERVER] Pre-existing '{FILE_TO_BE_DELETED_BY_PICKLE}' found.")
    else:
        print(f"[SERVER] '{FILE_TO_BE_DELETED_BY_PICKLE}' not found, creating it.")
    
    try:
        with open(FILE_TO_BE_DELETED_BY_PICKLE, "w") as f:
            f.write("This is a very important file that the demo will attempt to delete.\n" * 3)
        print(f"[SERVER] Created/Verified dummy important file: '{FILE_TO_BE_DELETED_BY_PICKLE}'")
    except Exception as e:
        print(f"[SERVER] Error creating/verifying file: {e}")


@app.route('/unpickle_dangerously', methods=['POST'])
def unpickle_dangerously_route():
    print("\n--- Server: Received request at /unpickle_dangerously ---")
    
    if not request.data:
        return jsonify({"error": "No data received"}), 400

    print(f"[SERVER] Received payload of length: {len(request.data)} bytes.")
    
    # Check file state BEFORE unpickling
    file_existed_before = os.path.exists(FILE_TO_BE_DELETED_BY_PICKLE)
    print(f"[SERVER] File '{FILE_TO_BE_DELETED_BY_PICKLE}' exists BEFORE unpickling: {file_existed_before}")

    response_message = ""
    unpickle_error = None
    try:
        # !!! THE DANGEROUS PART !!!
        # Unpickling data directly from an untrusted request payload.
        # The __reduce__ method of the pickled object will be called here by pickle.loads().
        print("[SERVER] Attempting to unpickle the received payload (THIS IS THE DANGER POINT)...")
        # reconstructed_object = pickle.loads(request.data)
        pickle.loads(request.data) # We don't even need to assign it for os.remove to work via __reduce__
        
        print("[SERVER] Unpickling completed. Malicious code (if any) in __reduce__ would have executed.")
        response_message = "Payload unpickled. Malicious code may have executed."

    except FileNotFoundError:
        # This specific exception might occur if os.remove was successful
        # and the object returned by __reduce__ (None for os.remove) was then processed
        # by pickle in a way that expected a file. Or, if the file was already gone.
        print("[SERVER] FileNotFoundError during/after unpickling (could indicate successful deletion by os.remove, or file never existed).")
        response_message = "Payload unpickled. FileNotFoundError encountered."
    except Exception as e:
        unpickle_error = str(e)
        print(f"[SERVER] An error occurred during unpickling: {e}")
        response_message = f"Error during unpickling: {str(e)}"

    # Check file state AFTER unpickling
    file_existed_after = os.path.exists(FILE_TO_BE_DELETED_BY_PICKLE)
    print(f"[SERVER] File '{FILE_TO_BE_DELETED_BY_PICKLE}' exists AFTER unpickling: {file_existed_after}")

    status_detail = ""
    if file_existed_before and not file_existed_after:
        status_detail = f"ATTACK SUCCESSFUL: '{FILE_TO_BE_DELETED_BY_PICKLE}' was DELETED!"
        print(f"[SERVER] {status_detail}")
    elif not file_existed_before and not file_existed_after:
        status_detail = "File did not exist before, and does not exist now. (Attack might have targeted an already deleted/non-existent file or did something else)."
        print(f"[SERVER] {status_detail}")
    elif file_existed_before and file_existed_after:
        status_detail = "ATTACK FAILED or targeted a different action: File still exists."
        if unpickle_error:
             status_detail += f" Unpickle error: {unpickle_error}"
        print(f"[SERVER] {status_detail}")
    else: # not file_existed_before and file_existed_after (could happen if setup failed and then pickle created it somehow - unlikely for os.remove)
        status_detail = "File did not exist before but exists now (unexpected for os.remove)."
        print(f"[SERVER] {status_detail}")

    # For demo purposes, re-create the file if it was deleted, so you can run the demo again.
    # A real victim system wouldn't do this.
    # if not file_existed_after and file_existed_before:
    #     print(f"[SERVER] Re-creating '{FILE_TO_BE_DELETED_BY_PICKLE}' for the next demo run.")
    #     setup_important_file()

    return jsonify({
        "message_from_server": response_message,
        "file_targetted": FILE_TO_BE_DELETED_BY_PICKLE,
        "file_existed_before_unpickle": file_existed_before,
        "file_existed_after_unpickle": file_existed_after,
        "attack_status_detail": status_detail
    }), 200

if __name__ == '__main__':
    print("--- Victim Server Starting ---")
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! WARNING !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    print("This server is INTENTIONALLY VULNERABLE to demonstrate pickle insecurity.")
    print("It will execute code embedded in pickle payloads, including file deletion.")
    # print("DO NOT run this in a production environment or where it can access sensitive files.")
    # print("Run this ONLY in a controlled, isolated environment for educational purposes.")
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    
    # Create the dummy file that the attacker will try to delete
    setup_important_file()
    
    print(f"[SERVER] Server will listen on http://127.0.0.1:5000")
    print(f"[SERVER] Send malicious pickle payloads via POST to /unpickle_dangerously")
    # Setting debug=False. Flask's reloader can sometimes cause issues with file state for this type of demo.
    # Use host='0.0.0.0' to make it accessible if attacker is on a different (virtual) machine in the same network.
    # For local testing, 127.0.0.1 is fine.
    app.run(debug=False, host='127.0.0.1', port=5000)
