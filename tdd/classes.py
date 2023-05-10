from dataclasses import dataclass

@dataclass
class User:
    Email:str
    Name:str 

@dataclass
class UserRegistrationService:
    Users = []

    def FindUser(self,email):
        for user in self.Users:
            if user.Email == email:
                return user
        return None

    def Register(self,email, name):
        if "@" not in email:
            return False
        # om email finns i Users 
        if self.FindUser(email) is None:
            self.Users.append(User(email,name))
            return True
        return False
