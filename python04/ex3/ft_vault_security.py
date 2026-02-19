#!/usr/bin/env python3

if __name__ == "__main__":
    
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===\n")
    print("Initiating secure vault access...")

    try:
        print("Vault connection established with failsafe protocols")

        with open("classified_data.txt", "r") as vault:
            print("\nSECURE EXTRACTION:")
            print(vault.read())

        with open("security_log.txt", "w") as vault:
            print("\nSECURE PRESERVATION:")
            vault.write("[CLASSIFIED] New security protocols archived")

        with open("security_log.txt", "r") as vault:
            print(vault.read())

        print("Vault automatically sealed upon completion\n")

    except Exception as error:
        print(f"Vault access error: {error}")
    
    print("All vault operations completed with maximum security.")
