# API Testing Report

## Objective
Validate backend API functionality.

## API Tested

### POST /api/chat

Input:
{
  "prompt": "Is this news fake?"
}

Expected Response:
{
  "response": "Prediction generated successfully."
}

Status Code:
200 OK

---

### GET /api/history

Expected Response:
Returns previous conversations.

Status Code:
200 OK

---

## Error Testing

Missing Prompt

Status Code:
400 Bad Request

Response:
{
  "error": "Prompt required"
}

---

## Conclusion

The APIs return proper JSON responses and handle errors correctly.
