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
