# izveidojam kontaktu aplikāciju, izmantojot:
# funkcijas
# datu strukturas (JSON)
# file input/output
import json

contacts = []

def LoadContacts():
    with open('contacts.json', 'r', encoding='UTF8') as file:
        contacts = json.load(file)
        print(contacts)

def PrintContacts():
    for contact in contacts:
        print(f"{contact['name']} {contact['surname']} {contact['number']} {contact['email']}")

def AddContact():
    name = input('Enter name: ')
    surname = input('Enter surname: ')
    number = input('Enter number: ')
    email = input('Enter email: ')

    contact = {
        'name': name, 
        'surname': surname, 
        'number': number,
        'email': email
    }

    contacts.append(contact)

def SaveContacts():
    with open('contacts.json', 'w', encoding='UTF8') as file:
        json.dump(contacts, file, indent=4)

LoadContacts()

while(True):
    response = input('N-add new, P-print, E-exit: ')
    if response == 'N':
        AddContact()
        SaveContacts()
    elif response == 'P':
        PrintContacts()
    elif response == 'E':
        break