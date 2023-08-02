from my_secrets import SECRET_KEY
import openai
import gradio as gr
openai.organization = "org-JGXhEVWZxbDg56XKVgC1J7db"
openai.api_key = SECRET_KEY

history = []
history_openai = []

history_openai.append({"role": "system", "content": "you are an AI chatbot assistant"})

def chat_func(user_msg, history):
    history_openai.append({"role": "system", "content": user_msg})
    response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", 
            messages=history_openai)
    first_reply = response["choices"][0]["message"]["content"]
    history_openai.append({"role": "system", "content": first_reply})

    # history.append([user_msg, first_reply])
    return first_reply


demo = gr.ChatInterface(chat_func)

demo.launch(share=True)