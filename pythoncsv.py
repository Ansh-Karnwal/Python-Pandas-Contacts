import pandas as pd

class Contact:
    contacts = pd.DataFrame(columns=['name', 'address', 'phone number', 'email address'])
    contacts = contacts.set_index("name")
    def __init__(self, name, address, phone_number, email_address):
        self.name = name
        self.address = address
        self.phone_number = phone_number
        self.email_address = email_address
        if self.name in Contact.get_contacts().index:
            duplicate = input('Do you want to add the duplicate value (y/n): ')
            if duplicate.lower() == 'y':
                self.name += ' (duplicate)'
            else:
                return
        contact = pd.Series(dtype='object')
        contact["name"] = self.name
        contact["address"] = self.address
        contact["phone number"] = self.phone_number
        contact["email address"] = self.email_address
        contact = pd.DataFrame(contact)
        contact = contact.transpose().set_index("name")
        Contact.contacts = Contact.contacts.append(contact)
        
    def __repr__(self):
        return f"name: '{self.name}', address: '{self.address}', phone number: '{self.phone_number}', email address: '{self.email_address}')"
    
    @staticmethod
    def get_contacts():
        return Contact.contacts

    def update_contact_name(self, new_name):
        Contact.contacts = Contact.contacts.rename({self.name : new_name})

    def update_contact_address(self, new_address):
        Contact.contacts.loc[self.name, "address"] = new_address

    def update_contact_phone_number(self, new_phone_number):
        Contact.contacts.loc[self.name, "phone number"] = new_phone_number

    def update_contact_email_address(self, new_email_address):
        Contact.contacts.loc[self.name, "email address"] = new_email_address
    
    def delete_contact(self):    
        Contact.contacts = Contact.contacts.drop(self.name)
    
    @staticmethod
    def get_contact_by_name(name):
        return Contact.contacts.loc[name]
    
    @staticmethod
    def get_contact_by_address(address):
        address_index = Contact.contacts.set_index('address')
        return address_index.loc[address] 
    
    @staticmethod
    def get_contact_by_phone_number(phone_number):
        phone_number_index = Contact.contacts.set_index('phone number')
        return phone_number_index.loc[phone_number]
    
    @staticmethod
    def get_contact_by_email_address(email_address):
        email_address_index = Contact.contacts.set_index('email address')
        return email_address_index.loc[email_address]

    @staticmethod
    def export_contacts():
        return Contact.contacts.to_csv('contacts.csv')
    
    
contact_1 = Contact('John Doe', '0000 Random Address', '000-000-0000', 'johndoe@email.com')
contact_2 = Contact('Jane Doe', '1111 Random Address', '111-111-1111', 'janedoe@email.com')
Contact.export_contacts()

# This is one of the excellent python projects for beginners. Everyone uses a contact book to save contact details, including name, address, phone number, and even
# email address. This is a command-line project where you will design a contact book application that users can use to save and find contact details. The application should
# also allow users to update contact information, delete contacts, and list saved contacts. The SQLite database is the ideal platform for saving contacts. To handle a
# project with Python for beginners can be helpful to build your career with a good start.
