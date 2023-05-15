from dataclasses import dataclass
import ssl 
import smtplib

@dataclass
class User:
    Email:str
    Name:str 

@dataclass
class UserRegistrationService:
    Users = []

    def Find(self, email):
        for user in self.Users:
            if user.Email == email:
                return user
        return None

    def Register(self, email, name):
        user = self.Find(email)
        print(user)
        if user == None:
            self.Users.append(User(email,name))
            self.sendWelcomeMailTo(email,name)
            return True
        return False 

    def sendWelcomeMailTo(self, email,name):
        port = 587  # For starttls
        smtp_server = "smtp.gmail.com"
        sender_email = "my@gmail.com"
        receiver_email = email
        password ="SecretPassword"
        message = """\
        Subject: Hi there

        Welcome as a new user."""

        context = ssl.create_default_context()
        with smtplib.SMTP(smtp_server, port) as server:
            server.ehlo()  # Can be omitted
            server.starttls(context=context)
            server.ehlo()  # Can be omitted
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message)