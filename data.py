questions = [
    {
        "id": "1",
        "text": "Do you want to grow wings?",
        "answers": {
            "yes": {
                "outcome_tags": ["wings"],
                "next_question": "2"
            },
            "no": {
                "outcome_tags": ["no_wings"],
                "next_question": "2"
            }
        }
    },
    # ... other questions
]

outcomes = {
    "outcome_key_1": {
        "text": "Your character is now growing wings...",
        "color": "blue",
        "time": 7,
        "tags": ["wings"]
    },
    "outcome_key_2": {
        "text": "Your character feels unchanged...",
        "color": "grey",
        "time": 3,
        "tags": ["no_wings"]
    },
    # ... other outcomes
}

additional_texts = {
    "boot": {
        "type": "sequence",
        "messages": [
            {"text": "System Initializing...", "color": "green", "time": 3},
            {"text": "Loading components...", "color": "green", "time": 2}
        ]
    },
    "initiation": {
        "type": "random",
        "messages": [
            {"text": "Transformation process started...", "color": "yellow", "time": 2},
            {"text": "Beginning transformation...", "color": "yellow", "time": 2}
        ]
    },
    # ... and so on
}