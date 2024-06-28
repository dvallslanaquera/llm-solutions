The models in this project are zero-shot approaches using checkpoints in HuggingFace.
For better performing models, BERT-based models should be considered. These models offer better results but they require fine-tuning with conversational data, which is not available in most cases. 
The data should be formatted in JSON as follows: 

```json
[
    {
        "context": "Book a flight to New York.",
        "response": "When do you want to travel to New York?",
        "entities": {"destination": "New York"}
    },
    ...
]
```


To try the chatbot on your local machine, download the code and on the terminal go to the root directory with your virtual environment activated. From there you can open the app from your browser entering the following line of code:

```bash 
python app.py
```

The host of the app will be specified after entering the previous code in the terminal. 