history = []

def save_conversation(user_input, prediction):
    history.append({
        "user_input": user_input,
        "prediction": prediction
    })

def get_history():
    return history
