def main():
    user_input = input("Please paste your input string here: ")
    user_input = user(user_input)
    print(user_input)

def user(user_input):
    user_input = user_input.replace(":)","🙂")
    user_input = user_input.replace(":(","🙁")
    return user_input

main()
