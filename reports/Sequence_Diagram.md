# Sequence Diagram

User
  │
  │ Enter news text
  ▼
Frontend (HTML/CSS/JavaScript)
  │
  │ POST /api/predict
  ▼
Backend (Flask)
  │
  │ Sends request
  ▼
AI Model
  │
  │ Returns prediction
  ▼
Backend (Flask)
  │
  │ JSON Response
  ▼
Frontend
  │
  │ Display Result
  ▼
User
