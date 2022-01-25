class User:

    def __init__(self, profile, username, password):
        self.profile = profile
        self._username = username
        self._password = password
        self.__validation_code = "0101"

    def set_password(self, password):
        str(password)
        if len(password) >= 8:
            self._password = password
            print("New password attributed.")
        else:
            print("Password too short")

    def get_password(self):
        print(self._password)
        return self._password

    def get_username(self):
        print(self._username)
        return self._username

    def __check_code(self, validation_code):
        if validation_code == self.__validation_code:
            return True
        else:
            return False

    def set_username(self, code, new_username):
        if self.__check_code(code) == True:
            self._username = new_username
            print("new username attributed.")
        else:
            print("Validation code incorrect.")


my_profile = User('Adrien Dzikowski', 'Subuton', "pass123")
my_profile.get_username()
my_profile.get_password()
my_profile.set_password("123")
my_profile.set_password("123456789")
my_profile.get_password()
my_profile.set_username("010", "Falzon")
my_profile.set_username("0101", "Sh03x")
