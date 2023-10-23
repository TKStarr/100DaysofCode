class User:
    def __init__(self, user_id="001", username="John Doe"):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers = user.followers + 1
        self.following = self.following + 1



user_1 = User("007", "James Bond")
user_1.followers = 500000

print(user_1.id)
print(user_1.username)
print(user_1.followers)

user_2 = User()
print(user_2.id)
print(user_2.username)
print(user_2.followers)

user_2.follow(user_1)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)
