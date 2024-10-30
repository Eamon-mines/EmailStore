import questionary as q
import json

def get_email():
    while True:
        email = str(q.text("Please enter an email to parse: ").ask())
        if '@' in email:
            break

    parts_of_email = email.split('@')
    username = parts_of_email[0]
    domain = parts_of_email[1]
    return (domain, username)

def add_to_json(email: tuple):
    with open("emails.json", "r+") as file:
        data = json.load(file)
        if data.get(email[0]) is not None:
            data[email[0]].append(email[1])
        else:
            data[email[0]] = [email[1]]
        file.seek(0)
        json.dump(data, file, indent=4)


def main():
    print("Hello and welcome to email splitter!")
    while True:
        answer = q.confirm("Would you like to save the email to the json file?", default=True).ask()
        email = get_email()
        if answer:
            add_to_json(email)
        else:
            print(email)
        again = q.confirm("Would you like to add another?", default=True).ask()
        if not again:
            break
    
    
if __name__ == "__main__":
    main()
