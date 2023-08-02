from my_secrets import SECRET_KEY
import openai
openai.organization = "org-JGXhEVWZxbDg56XKVgC1J7db"
openai.api_key = SECRET_KEY

QUIT_STRING = "'q' to quit"
seperator = ": "
USER_NAME = f"You ({QUIT_STRING}){seperator}"
BOT_NAME = f"Bot{seperator}"


messages = []

user_msg = input(f"{USER_NAME}")
print("\n\n")
while user_msg!= "q":
    messages.append({"role": "system", "content": user_msg})

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", 
        messages=messages)
    first_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "system", "content": first_reply})

    print(BOT_NAME + first_reply)
    print("\n\n")

    user_msg = input(f"{USER_NAME}")
    print("\n\n")

