import json

def comp_pass(vuln_pass, input_pass):
    if len(vuln_pass) != len(input_pass):
        return False
    for i in range(len(vuln_pass)):
        if vuln_pass[i]!=input_pass[i]:
            return False
    return True

def load_password(file_path="credentials.json"):
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)["password"]

def login(user_pass):
    pswd = load_password()
    if comp_pass(pswd, user_pass):
        return print('User Has Access')
    return print('User does not have access')

def main():
    inp_pass=input("Enter Password: ")
    login(inp_pass)

main()
