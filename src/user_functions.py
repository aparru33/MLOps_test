
# More elaborated version (copy to src/user_functions.py)
def get_email_from_input():
    """ Contains '@' and '.' """
    email = input("Write down your email: ")
    if ("@" not in email or "." not in email):
        print('Email is not valid.')
    else:
        return email

def get_user_name_from_input():
    """ Not empty string. No spaces. """
    name= input("Create your user name: ").strip()
    if " " in name or name=="":
        print('Name cannot have empty space or be null')
    else: 
        return name
    
def get_password_from_input():
    """ Password needs to be at least 8 characters long with at least one number, one special character and one letter. """
    pwd= input("Create your password: ")
    if 20>=len(pwd)>=8 and has_digit(pwd) and has_special_char(pwd) and has_letter(pwd):
        return pwd
    else:
        print('Password needs to be at least 8 characters long with at least one number, one special character and one letter.')

s=list('[@_!#$%^&*()<>?/\\|}{~:]')
has_digit=lambda x:any(chr.isdigit() for chr in x)
has_special_char=lambda x:any(c in s for c in x)
def has_letter(s):
    for c in s:
        if not c.isdigit() and not has_special_char(c):
            return True
    return False

def is_palindrome():
    s=input()
    s=s.replace(" ",'')
    for c in ['é','è','ê']:s=s.replace(c,'e') 
    s=s.lower()
    l=list(s)
    rl=l[::-1]
    return all([l[i]==rl[i] for i in range(len(l))])

if __name__=="__main__":
    print(is_palindrome())