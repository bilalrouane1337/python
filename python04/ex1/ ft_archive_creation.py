def create_data():

    try:

        my_file = open(file_name, 'w')

        my_file.write(
            "[ENTRY 001] New quantum algorithm discovered\n"
            "[ENTRY 002] Efficiency increased by 347%\n"
            "[ENTRY 003] Archived by Data Archivist trainee"
            )

        print("Storage unit created successfully...\n")
        
        my_file = open(file_name, 'r')

        print("Inscribing preservation data...")
        print(my_file.read())

    except Exception as e:

        print(f"Error: {e}")

    finally:
        
        my_file.close()
        print("\nData inscription complete. Storage unit sealed.")


if __name__ == "__main__":

    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===\n")

    file_name = "new_discovery.txt"
    print(f"Initializing new storage unit: {file_name}")
    create_data()
    print(f"Archive '{file_name}' ready for long-term preservation.")
