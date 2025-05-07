import game_data
import random
import art
def get_random_data():
    """Return a random dictionary item from game data"""
    return random.choice(game_data.data)


who_has_more_follower = ""
score = 0
continue_the_game = True

account_a = get_random_data()
account_b = get_random_data()

#check that both data should not be same.
if account_a == account_b :
    account_b = get_random_data()



def formatted_data(account):
    """Returns data into a proper format"""
    return f"{account["name"]} ,{account["description"]} ,from {account["country"]}"


def check_answer(user_answer,follower_a,follower_b):
    """Compare both account follower and return True if user answer is correct"""
    if follower_a["follower_count"] > follower_b["follower_count"]:
        return user_answer == "a"
    else:
        return user_answer == "b"



print(art.logo)
while continue_the_game:
    print(f"Compare A : {formatted_data(account_a)}.")
    print(art.vs)
    print(f"Against B : {formatted_data(account_b)}.")
    answer = str(input("Who has more followers? Type 'A' or 'B' : ").lower())

    is_correct = check_answer(answer,account_a,account_b)
    if is_correct == True :
        score += 1
        print("\n" * 20)
        print(art.logo)
        print(f"You are right! Current score : {score}")
        account_a = account_b
        account_b = get_random_data()
        if account_a == account_b :
            account_b = get_random_data()
    else:
        print(f"You are wrong. Final score : {score}")
        continue_the_game = False