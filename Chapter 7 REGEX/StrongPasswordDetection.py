import re
# https://www.thepolyglotdeveloper.com/2015/05/use-regex-to-test-password-strength-in-javascript/ regex from here

def StrongPasswordDetection(password):
    strongPassword = re.compile("^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.{8,})") # atleast one lower-case letter, atleast one upper-case letter
                                                                               # atleast one digit and 8 characters long


    if strongPassword.search(password): #if matches the regex
        print("Great Password")
    else:
        print("Not a strong password, Please try again")






