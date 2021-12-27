
"""
PHONE-NUMBER NORMALIZER : IT RECEIVES A PHONE NUMBER AS AN INPUT WITH DIFFERENT POSSIBLE COMBINATIONS,
AND GIVES IT BACK WITH THE FORM : 1-234-567-8910
ON THE THIRD AND FORTH GROUP, THE FIRST NUMBER MUST BE INCLUDED BETWEEN 1 AND 9
REGEX METHOD IS USED TO SORT THE INPUT
"""
import re
phonebook = []
cont = "S"

def recognize(phonenumber):
    """
    AREA NUMBER NOT MANDATORY. CHARTS POSSIBLES BETWEEN NUMBER'S CLUSTERS : (space),-.()
    """
    rege = re.compile(r"(\+)?(?P<prefisso>(\d))?"
                      r"([ \.\-\(])?(?P<first>(\d{3}))([ \.\-\)])?"
                      r"([ \.\-\(])?(?P<second>([1-9]\d{2}))([ \.\-\(])?"
                      r"([ \.\-\(])?(?P<third>([1-9]\d{3}))")
    
    def correct_pattern(phonenumber):
        if phonenumber.group("prefisso") == None:
            area_code = str(input("Please insert the area code number: "))
            return (area_code +"-"+phonenumber.group("first")+"-"+phonenumber.group("second")+"-"+phonenumber.group("third"))
        else:
            return (phonenumber.group("prefisso")+"-"+phonenumber.group("first")+"-"+phonenumber.group("second")+"-"+phonenumber.group("third"))


    if rege.search(phonenumber):
        phonenumber = rege.sub(correct_pattern,phonenumber)
        return phonenumber
    else:
        return("The number insert is wrong, please try again.")

while cont == "S":
    phonenum = input("Insert a Phone Number : ")
    print(recognize(phonenum))
    cont = input("Do you want to insert another number? S/N ")
