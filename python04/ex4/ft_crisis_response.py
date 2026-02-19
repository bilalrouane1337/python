#!/usr/bin/env python3

def crisis_handler(file_name):

    try:

        if file_name == "standard_archive.txt":
            print(f"ROUTINE ACCESS: Attempting access to '{file_name}'...")
        else:
            print(f"CRISIS ALERT: Attempting access to '{file_name}'...")

        with open(file_name, "r") as archive:
            content = archive.read().strip()

        print(f"SUCCESS: Archive recovered - \"{content}\"")
        print("STATUS: Normal operations resumed")

    except FileNotFoundError:

        print("RESPONSE: Archive not found in storage matrix")
        print("STATUS: Crisis handled, system stable\n")

    except PermissionError:

        print("RESPONSE: Security protocols deny access")
        print("STATUS: Crisis handled, security maintained\n")

    except Exception:

        print("RESPONSE: Unexpected system anomaly detected")
        print("STATUS: Crisis handled, system stabilized\n")
    

if __name__ == "__main__":

    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===\n")

    crisis_handler("lost_archive.txt")
    crisis_handler("classified_vault.txt")
    crisis_handler("standard_archive.txt")

    print("All crisis scenarios handled successfully. Archives secure.")
