class User:


    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_reward_member = False
        self.gold_card_points = 0

    def display_info(self):
        print(f"First_name : {self.first_name}\nLast_name : {self.last_name}\nEmail: {self.email}\nAge : {self.age}\nIs_Reward_Member: {self.is_reward_member}\nGold_Card_Points : {self.gold_card_points}" )

    def enroll(self):
        if self.is_reward_member == True:
            print("Already Memeber")
            return
        else:
            self.is_reward_member = True
            self.gold_card_points = 200

    def spendPoints(self, spent):
        self.gold_card_points =self.gold_card_points - spent
    


Anna = User("Anna", "Last", "Hello@goodbye.com", 33)
Bob = User("Bob", "Last", "emaily@ohno.com", 55)
Cindy = User("Cindy", "Last", "emaily@ohno.com", 43)

Anna.spendPoints(50).display_info()
Bob.enroll().spendPoints(80)
Cindy.display_info()










