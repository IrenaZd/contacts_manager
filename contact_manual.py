contacts = [
   {
        "name": "Anicka",
        "email": "anicka@email.com",
        "phone": "777 777 777"
   },
   {
        "name": "Nikol",
        "email": "nikol@email.com", 
        "phone": "777 777 778"
   }
]

# vypsat cely 1. kontakt
print(contacts[0])
print(contacts[1])

# vypsat hodnotu klice "name" v polozce na indexu 0
print(contacts[0]["name"])

# pridame kontakt
name = "Anicka"
email = "anicka_2@mail.com"
phone = ""

contact = {
    "name": name,
    "email": email,
    "phone": phone
}

# pridat contact do contacts
contacts.append(contact)

print(contacts)


