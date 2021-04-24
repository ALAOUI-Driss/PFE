import re

def mail_check(mail):
    if(re.search("^(\w|\_|\-|\.)+[@](\w|\_|\-|\.)+[.][a-z A-Z]{2,3}$",mail) or mail==""):
        return(0)
    return(1)