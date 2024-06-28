# Chatbot doc: https://huggingface.co/microsoft/DialoGPT-medium
from flask import Flask, render_template, request, jsonify
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
import os

# Initialize model 
model_name = 'microsoft/DialoGPT-medium'
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

chat_history_ids = None

app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.route("/")
def index(): 
    return render_template('chat.html')

@app.route("/get", methods=["GET", "POST"])
def chat(): 
    msg = request.form["msg"].lower()
    input = msg
    return get_chat_response(input)

# Define code for the chatbot
# Use Microsoft's DialoGPT-medium 
def get_chat_response(text): 
    global chat_history_ids

    # encode the new user input, add the eos_token and return a tensor in Pytorch
    # where 'text' is user's input and eos_token is the end-of-sequence token. It generates a tensor
    new_user_input_ids = tokenizer.encode(str(text) + tokenizer.eos_token, return_tensors='pt')

    # Append the new user input tokens to the chat history
    if chat_history_ids is not None:
        bot_input_ids = torch.cat([chat_history_ids, new_user_input_ids], dim=-1)
    else:
        bot_input_ids = new_user_input_ids
    # Generate attention mask 
    bot_attention_mask = torch.ones_like(bot_input_ids)

    # generated a response while limiting the total chat history to 1000 tokens, 
    # chat_history_ids = model.generate(bot_input_ids, max_length=1000, pad_token_id=tokenizer.eos_token_id)
    chat_history_ids = model.generate(
        input_ids=bot_input_ids,
        attention_mask=bot_attention_mask,
        max_length=1000,
        pad_token_id=tokenizer.eos_token_id,
        do_sample=True,
        temperature=0.3,  # Adjust temperature for more diverse responses
        top_k=50,  # Top-k sampling
        top_p=0.95  # Top-p (nucleus) sampling
    )

    # pretty print last ouput tokens from bot
    output = tokenizer.decode(chat_history_ids[:, bot_input_ids.shape[-1]:][0], skip_special_tokens=True)
    return output


if __name__ == '__main__':
    app.run(debug=True)