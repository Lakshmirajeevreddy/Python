class UserExists(Exception):
    def __init__(self):
        self.value = "User already Exists. Please enter new name"
        
    def __str__(self):
        return(self.value)
    
class UserNotFound(Exception):
    def __init__(self):
        self.value = "Wrong USer Name or Password"
        
    def __str__(self):
        return(self.value)