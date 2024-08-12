                    #================================================================
                    #===== Module 3: Mini-Project | Contact Management System ===+===
                    #================================================================


# Project Requirements
    # Your task is to develop a Contact Management System with the following features:

# User Interface (UI):
    # Create a user-friendly command-line interface (CLI) for the Contact Management System.
    # Display a welcoming message and provide a menu with the following options:
            # Menu:
            # Add a new contact
            # Edit an existing contact
            # Delete a contact
            # Search for a contact
            # Display all contacts
            # Export contacts to a text file
            # Import contacts from a text file
            # Quit 

# Contact Data Storage:
    # Use nested dictionaries as the main data structure for storing contact information.
    # Each contact should have a unique identifier (e.g., a phone number or email address) as the outer dictionary key.
    # Store contact details within the inner dictionary, including:
    # Name
    # Phone number
    # Email address
    # Additional information (e.g., address, notes).


# Menu Actions:
    # Implement the following actions in response to menu selections:
    # Adding a new contact with all relevant details.
    # Editing an existing contact's information (name, phone number, email, etc.).
    # Deleting a contact by searching for their unique identifier.
    # Searching for a contact by their unique identifier and displaying their details.
    # Displaying a list of all contacts with their unique identifiers.
    # Exporting contacts to a text file in a structured format.
    # Importing contacts from a text file and adding them to the system.


# User Interaction:
    # Utilize input() to enable users to select menu options and provide contact details.
    # Implement input validation using regular expressions (regex) to ensure correct formatting of contact information.

# Error Handling:
    # Apply error handling using try, except, else, and finally blocks to manage unexpected issues that may arise during execution.

# GitHub Repository:
    # Create a GitHub repository for your project.
    # Commit your code to the repository regularly.
    # Create a clean and interactive README.md file in your GitHub repository.
    # Include clear instructions on how to run the application and explanations of its features.
    # Provide examples and screenshots, if possible, to enhance user understanding.
    # Include a link to your GitHub repository in your project documentation.

# Optional Bonus Points
    # Contact Categories (Bonus): Implement the ability to categorize contacts into groups (e.g., friends, family, work). Each contact can belong to one or more categories.
    # Contact Search (Bonus): Enhance the contact search functionality to allow users to search for contacts by name, phone number, email address, or additional information.
    # Contact Sorting (Bonus): Implement sorting options to display contacts alphabetically by name or based on other criteria.
    # Backup and Restore (Bonus): Add features to create automatic backups of contact data and the ability to restore data from a backup file.
    # Custom Contact Fields (Bonus): Allow users to define custom fields for contacts (e.g., birthdays, anniversaries) and store this information.

#================================================================================================
#=====================================Begin Code=================================================
#================================================================================================
import re

contacts = {}

def display_menu():
    print("Welcome to the Contact Management System")
    print("Menu:")
    print("1. Add a new contact")
    print("2. Edit an existing contact")
    print("3. Delete a contact")
    print("4. Search for a contact")
    print("5. Display all contacts")
    print("6. Export contacts to a text file")
    print("7. Import contacts from a text file")
    print("8. Quit")

def add_contact():
    print("---- Add a New Contact ----")
    name = input("Enter the name: ")
    phone = input("Enter the phone number: ")
    email = input("Enter the email address: ")
    additional_info = input("Enter additional information: ")
    
    contact = {
        "Name": name,
        "Phone Number": phone,
        "Email Address": email,
        "Additional Information": additional_info
    }
    
    contacts[email] = contact
    
    print("Contact added successfully!")

def edit_contact():
    print("---- Edit a Contact ----")
    email = input("Enter the email address of the contact to edit: ")
    
    if email in contacts:
        contact = contacts[email]
        
        print("Contact Details:")
        print(f"Name: {contact['Name']}")
        print(f"Phone Number: {contact['Phone Number']}")
        print(f"Email Address: {contact['Email Address']}")
        print(f"Additional Information: {contact['Additional Information']}")
        
        print("Enter new details (leave blank to keep existing):")
        name = input("Enter the new name: ")
        phone = input("Enter the new phone number: ")
        email = input("Enter the new email address: ")
        additional_info = input("Enter new additional information: ")
        
        if name.strip() != "":
            contact["Name"] = name
        if phone.strip() != "":
            contact["Phone Number"] = phone
        if email.strip() != "":
            contact["Email Address"] = email
        if additional_info.strip() != "":
            contact["Additional Information"] = additional_info
        
        print("Contact updated successfully!")
    else:
        print("Contact not found.")

def delete_contact():
    print("---- Delete a Contact ----")
    email = input("Enter the email address of the contact to delete: ")
    
    if email in contacts:
        del contacts[email]
        print("Contact deleted successfully!")
    else:
        print("Contact not found.")

def search_contact():
    print("---- Search for a Contact ----")
    email = input("Enter the email address of the contact to search: ")
    
    if email in contacts:
        contact = contacts[email]
        
        print("Contact Details:")
        print(f"Name: {contact['Name']}")
        print(f"Phone Number: {contact['Phone Number']}")
        print(f"Email Address: {contact['Email Address']}")
        print(f"Additional Information: {contact['Additional Information']}")
    else:
        print("Contact not found.")

def display_contacts():
    print("---- All Contacts ----")
    for email, contact in contacts.items():
        print(f"Email Address: {email}")
        print(f"Name: {contact['Name']}")
        print(f"Phone Number: {contact['Phone Number']}")
        print(f"Email Address: {contact['Email Address']}")
        print(f"Additional Information: {contact['Additional Information']}")
        print("")

def export_contacts():
    print("---- Export Contacts ----")
    file_name = input("Enter the file name: ")
    
    with open(file_name, "w") as file:
        for email, contact in contacts.items():
            file.write(f"Email Address: {email}\n")
            file.write(f"Name: {contact['Name']}\n")
            file.write(f"Phone Number: {contact['Phone Number']}\n")
            file.write(f"Email Address: {contact['Email Address']}\n")
            file.write(f"Additional Information: {contact['Additional Information']}\n")
            file.write("\n")
    
    print("Contacts exported successfully!")

def import_contacts():
    print("---- Import Contacts ----")
    file_name = input("Enter the file name: ")
    
    try:
        with open(file_name, "r") as file:
            lines = file.readlines()
        
        email = ""
        name = ""
        phone = ""
        additional_info = ""
        
        for line in lines:
            line = line.strip()
            
            if line.startswith("Email Address:"):
                email = line.replace("Email Address: ", "")
            elif line.startswith("Name:"):
                name = line.replace("Name: ", "")
            elif line.startswith("Phone Number:"):
                phone = line.replace("Phone Number: ", "")
            elif line.startswith("Additional Information:"):
                additional_info = line.replace("Additional Information: ", "")
            elif line == "":
                if email != "":
                    contact = {
                        "Name": name,
                        "Phone Number": phone,
                        "Email Address": email,
                        "Additional Information": additional_info
                    }
                    
                    contacts[email] = contact
                    
                    email = ""
                    name = ""
                    phone = ""
                    additional_info = ""
    except FileNotFoundError:
        print("File not found.")
    else:
        print("Contacts imported successfully!")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice (1-8): ")
        
        if choice == "1":
            add_contact()
        elif choice == "2":
            edit_contact()
        elif choice == "3":
            delete_contact()
        elif choice == "4":
            search_contact()
        elif choice == "5":
            display_contacts()
        elif choice == "6":
            export_contacts()
        elif choice == "7":
            import_contacts()
        elif choice == "8":
            print("Thank you for using the Contact Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

                                    #======= END OF CODE =========


# Author: Roger Block