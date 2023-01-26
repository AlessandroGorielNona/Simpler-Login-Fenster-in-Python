import tkinter as tk
import json
import hashlib

def register():
    # Hole die Eingaben des Benutzers
    username = username_entry.get()
    password = password_entry.get()

    # Hash das Passwort
    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    # Speichere die Anmeldeinformationen des Benutzers in einer JSON-Datei
    user_data = {username: hashed_password}
    with open("users.json", "w") as file:
        json.dump(user_data, file)

def login():
    # Hole die Eingaben des Benutzers
    username = username_entry.get()
    password = password_entry.get()

    # Hash das eingegebene Passwort
    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    # Lade die gespeicherten Anmeldeinformationen des Benutzers aus der JSON-Datei
    with open("users.json", "r") as file:
        user_data = json.load(file)

    # Überprüfe, ob die eingegebenen Anmeldeinformationen korrekt sind
    if username in user_data and user_data[username] == hashed_password:
        # Anmeldeinformationen sind korrekt
        print("Anmeldung erfolgreich!")
    else:
        # Anmeldeinformationen sind falsch
        print("Anmeldung fehlgeschlagen.")

root = tk.Tk()
root.title("Registrierung/Anmeldung")

username_label = tk.Label(root, text="Benutzername:")
username_label.grid(row=0, column=0)

username_entry = tk.Entry(root)
username_entry.grid(row=0, column=1)

password_label = tk.Label(root, text="Passwort:")
password_label.grid(row=1
, column=0)

password_entry = tk.Entry(root, show="*")
password_entry.grid(row=1, column=1)

register_button = tk.Button(root, text="Registrieren", command=register)
register_button.grid(row=2, column=0)

login_button = tk.Button(root, text="Anmelden", command=login)
login_button.grid(row=2, column=1)

root.mainloop()
