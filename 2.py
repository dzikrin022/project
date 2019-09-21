import re
def is_username_valid(username):
    angka = str([0,1,2,3,4,5,6,7,8,9])
    special = ['+','|','#','!','$','%','^','*','&','=','{}','?','<>',';',':','/','\',','()','@','~',"`"]
    if len(username) < 5:
        return False
    elif len(username) > 9:
        return False
    elif any(char.isupper() for char in username):
        return False
    elif not any(char.islower() for char in username):
        return False
    elif any(char in special for char in username):
        return False
    elif any(char in angka for char in username):
        return False
    else:
        return True

def is_password_valid(password):
    angka = str([0,1,2,3,4,5,6,7,8,9])
    special_regex = re.compile(r'[@]|[+]|[#]|[!]|[$]|[%]|[^]|[*]|[&]|[=]|[{}]|[?]|[<>]|[;]|[:]|[/]|[\]|[`]')
    special_val = special_regex.search(password)
    if special_val == None:
        return False
    elif len(password) < 10:
        return False
    elif len(password) > 10:
        return False
    elif not any(char.isupper() for char in password):
        return False
    elif not any(char.islower() for char in password):
        return False
    elif not any(char in angka for char in password):
        return False
    else:
        return True
                 
