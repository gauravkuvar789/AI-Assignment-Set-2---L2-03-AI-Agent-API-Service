# AI Agent API Service

## Overview

This project is developed for OS3 AI Engineer Evaluation (L2-03).

It provides an AI Agent REST API using Google Gemini.

---

## Features

- FastAPI Backend
- Google Gemini Integration
- AI Agent Endpoint
- Health Check API
- Time Tool
- JSON Responses

---

## APIs

### GET /health

Returns application health.

### GET /time

Returns current system time.

### POST /agent

Request

```json
{
    "task":"Explain Machine Learning"
}
```

Response

```json
{
    "result":"Machine Learning is..."
}
```

---

## Technologies

- Python
- FastAPI
- Google Gemini API
- Pydantic

---

## Run

```
python run.py
```

Server

```
http://localhost:8000
```

---

## Author

Gaurav Kuvar
