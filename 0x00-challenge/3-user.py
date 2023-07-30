#!/usr/bin/env python3

class User:
    def __init__(self, password):
        self.__password = password

    def get_password(self):
        return self.__password

    def is_valid_password(self, password):
        return password == self.__password

if __name__ == "__main__":
    user = User("1234")  # Set the user password here
    print("Test User")
    if user.is_valid_password("1234"):
        print("is_valid_password should return True if it's the right password")

