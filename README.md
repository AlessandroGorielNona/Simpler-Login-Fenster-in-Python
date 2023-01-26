# Simpler-Login-Fenster-in-Python
Dieser Code erstellt eine Benutzeroberfläche mit Tkinter, einer Python-Bibliothek zur Erstellung von grafischen Benutzeroberflächen. Es ermöglicht es dem Benutzer, sich zu registrieren und anzumelden. Die registrierten Benutzerdaten werden in einer JSON-Datei gespeichert und das Passwort wird gehasht, bevor es gespeichert wird, um die Sicherheit zu erhöhen.

    Importieren der erforderlichen Bibliotheken: tkinter, json und hashlib.
    Erstellen einer Funktion "register()", die die Eingaben des Benutzers für den Benutzernamen und das Passwort erhält.
    Hash des Passwort mit hashlib.sha256().hexdigest() und speichern des hashed password in einer Variable
    Speichern des Benutzernamens und des gehashten Passworts in einer Variablen "user_data" als JSON-Dictionary
    Öffnen der Datei "users.json" im "write" mode und speichern der user_data in der Datei
    Erstellen einer Funktion "login()", die die Eingaben des Benutzers für den Benutzernamen und das Passwort erhält
    Hash des eingegebenen Passwort mit hashlib.sha256().hexdigest() und speichern des hashed password in einer Variable
    Öffnen der Datei "users.json" im "read" mode und laden der user_data in eine Variable
    Überprüfen, ob der eingegebene Benutzername und Passwort übereinstimmt und geben entsprechende Nachricht aus
    Erstellen einer Tkinter-Oberfläche und Platzieren von Label und Entry-Feldern für Benutzernamen und Passwort sowie Buttons zum Registrieren und Anmelden.
    
    Hinweis:
    Dieser Code dient nur zu schulischen zwecken.
