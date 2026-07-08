# Error Handling

## Objective
Handle invalid requests and provide meaningful error messages.

## Possible Errors

### 400 Bad Request
Occurs when the user does not provide any news text.

Response:
{
  "error": "Prompt is required"
}

### 404 Not Found
Occurs when the requested API endpoint does not exist.

### 500 Internal Server Error
Occurs if there is an unexpected server error.
