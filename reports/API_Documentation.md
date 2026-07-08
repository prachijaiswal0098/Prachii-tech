# API Documentation

## Base URL
http://localhost:5000

### GET /api/health
Purpose: Check if the server is running.

Response:
{
  "status": "Server Running"
}

### POST /api/predict
Purpose: Predict whether the news is Fake or Real.

Request:
{
  "news": "Enter news text"
}

Response:
{
  "prediction": "Fake"
}
