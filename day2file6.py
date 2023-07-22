#Custom Exception

username = "John"

class UserNameDoesNotMatch(Exception):
    def __init__(self,message):
        super().__init__(message)

if username != "james":
    raise UserNameDoesNotMatch("Invalid username")
