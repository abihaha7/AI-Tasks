import pickle

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def save_user(self, filename):
        with open(filename, "wb") as file:
            pickle.dump(self, file)

    @staticmethod
    def load_user(filename):
        with open(filename, "rb") as file:
            return pickle.load(file)

# Example Usage
user1 = User("admin", "1234")
user1.save_user("user_data.pkl")

loaded_user = User.load_user("user_data.pkl")
print(loaded_user.username, loaded_user.password)
