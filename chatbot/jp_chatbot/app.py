# Chatbot doc: https://huggingface.co/microsoft/DialoGPT-medium
from flask import Flask, render_template, request, jsonify
import transformers
from transformers import TextStreamer, AutoModelForCausalLM, AutoTokenizer
import torch
# import os

assert transformers.__version__ >= "4.34.1"

app = Flask(__name__)

print("Loading model and tokenizer...")
model_name = "cyberagent/calm2-7b-chat"
model = AutoModelForCausalLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)
# streamer = TextStreamer(tokenizer, skip_prompt=True, skip_special_tokens=True)

@app.route("/")
def index(): 
    return render_template('chat.html')

@app.route("/get", methods=["GET", "POST"])
def chat(): 
    msg = request.form["msg"].lower()
    input = msg
    print(input)

    return get_chat_response(input)

# token_ids = tokenizer.encode(prompt, return_tensors="pt")

# Define code for the chatbot
# Use Microsoft's DialoGPT-medium 
def get_chat_response(text): 

    # Let's chat for 5 lines
    for step in range(5):
        # encode the new user input, add the eos_token and return a tensor in Pytorch
        new_user_input_ids = tokenizer.encode(str(text) + tokenizer.eos_token, return_tensors='pt')

        # append the new user input tokens to the chat history
        bot_input_ids = torch.cat([chat_history_ids, new_user_input_ids], dim=-1) if step > 0 else new_user_input_ids

        # generated a response while limiting the total chat history to 1000 tokens, 
        # chat_history_ids = model.generate(bot_input_ids, max_length=1000, pad_token_id=tokenizer.eos_token_id)
        chat_history_ids = model.generate(
            input_ids=bot_input_ids, 
            max_new_tokens=300,
            do_sample=True, 
            temperature=0.8
            # streamer=streamer
        )

        # pretty print last ouput tokens from bot
        return tokenizer.decode(chat_history_ids[:, bot_input_ids.shape[-1]:][0], skip_special_tokens=True)


if __name__ == '__main__':
    app.run(debug=True)