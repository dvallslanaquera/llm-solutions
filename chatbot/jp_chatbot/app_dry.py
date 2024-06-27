# Chatbot doc: https://huggingface.co/microsoft/DialoGPT-medium
from flask import Flask, render_template, request, jsonify
import transformers
from transformers import TextStreamer, AutoModelForCausalLM, AutoTokenizer
import torch
# import os

assert transformers.__version__ >= "4.34.1"

# app = Flask(__name__)

chat_history_ids = None

print("Loading model and tokenizer...")
model_name = "microsoft/dialoGPT-medium"
model = AutoModelForCausalLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)
# streamer = TextStreamer(tokenizer, skip_prompt=True, skip_special_tokens=True)


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
    chat_history_ids = model.generate(
        input_ids=bot_input_ids, 
        attention_mask=bot_attention_mask, 
        max_new_tokens=300,
        do_sample=True, 
        temperature=0.5,  # values >1 turn the model more random. Values close to 0 more conservative
        pad_token_id=tokenizer.eos_token_id
        # streamer=streamer
    )

    # pretty print last ouput tokens from bot
    output = tokenizer.decode(chat_history_ids[:, bot_input_ids.shape[-1]:][0], skip_special_tokens=True)
    print(output)
    print('chat_history_ids:')
    print(chat_history_ids)
    return output

user_input = 'Hi, how are you doing?'
user_input_2 = "doing fine. I hope you don't have any bug..."
user_input_3 = "you don't need me to debug you then?"
get_chat_response(user_input)
get_chat_response(user_input_2)
get_chat_response(user_input_3)