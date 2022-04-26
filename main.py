import os

from sqlalchemy import false


class Contacts:
    def __init__(self, option):
        self.__phonebook = []
        if option == 1:
            self.__contactData()
        elif option == 2:
            self.showContacts()
        elif option == 3:
            self.removeContacts()
        elif option == 4:
            self.searchContact()
        elif option == 5:
            return 
            

    def __contactData(self):
        self.__name = self.putName()
        self.__email = self.insertEmail()
        self.__phonenumber = self.insertNumber(self.__name, self.__email)

    
    def putName(self):
        name = input("Contact Name: ")
        return name
        

    def insertEmail(self):
        email = input("Email: ")
        return email


    def insertNumber(self, name, email):
        number = int(input("Number: "))
        self.saveContact(name, email, number)
        return number  

    
    def saveContact(self, name, email, number):
        with open ('Contacts/contatos.txt', 'a') as contatos:
            contatos.writelines(f"Name: {name}; Number: {number}; E-mail: {email}; \n")


    def showContacts(self):
        with open('Contacts/contatos.txt', 'r') as contatos:
            print(
            ''' 
==============================================================================================================
                                            Phonebook
            ''')
            print(contatos.read())
            print(
            '''   
==============================================================================================================
            ''')


    def removeContacts(self):
        removedName = input('Insert name you want to remove: ')
        phonebook = open('Contacts/contatos.txt', 'r')
        aux = []
        aux2 = []
        for i in phonebook:
            aux.append(i)
        for i in range(0, len(aux)):
            if removedName not in aux[i]:
                aux2.append(aux[i])
        phonebook = open('Contacts/contatos.txt', 'w')
        for i in aux2:
            phonebook.write(i)


    def searchContact(self):
        searchedName = input('''Name to search: ''')
        phonebook = open('Contacts/contatos.txt', 'r')
        for contact in phonebook:
            if searchedName in (contact.split(";")[0]):
                print(contact)
        

def menu():
    option = int(input('''
==============================================================================================================
                                            PHONEBOOK                                                                          
    MENU:

[1] Add Contact
[2] Show Contacts
[3] Delete Contact
[4] Search Contact
[5] Quit
==============================================================================================================
    Insert your choice: '''))
    return option


ok= True
while ok:
    option = menu()
    if option == 5:
        ok == False
        break
    new = Contacts(option)
