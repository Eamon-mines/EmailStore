import questionary as q
import json

def read_emails():
    data = {}
    with open("emails.json", "r") as file:
        data = json.load(file)
    emails = []
    for key, val in data.items():
        for user in val:
            emails.append(user + '@' + key)
    emails.sort()
    return emails

if __name__ == "__main__":
    emails = read_emails()
    print("""Welcome to the email checker. 
This is for double checking if you remember the email that you are entering.""")
    emails.append("Not Here!")
    known = q.autocomplete("Enter the email:", emails).ask()
    print(f"""Here is the selected email:
          {known}""")