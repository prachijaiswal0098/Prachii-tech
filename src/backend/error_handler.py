def validate_prompt(prompt):
    if not prompt:
        return {
            "error": "Prompt is required"
        }

    return {
        "status": "Valid prompt"
    }
