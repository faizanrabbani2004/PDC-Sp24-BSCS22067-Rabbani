Faizan Rabbani - BSCS22067

# PDC Assignment 4 - Circuit Breaker Implementation

## Overview
This project demonstrates a Fault Tolerance solution using the Circuit Breaker pattern in a FastAPI application.

The system simulates failure of an external LLM API and prevents the application from blocking by returning a fallback response after repeated failures. This ensures that the system remains responsive even when external services fail.

---

## Features
- Circuit Breaker implementation
- Failure detection using threshold
- Automatic circuit open after repeated failures
- Fallback response when API is unavailable
- Automatic recovery after timeout
- Custom middleware header included in every response

---

## Requirements
Before running this project, make sure you have installed:

- Python 3.x
- pip (Python package manager)

---

## Installation Steps

### 1. Clone the repository

git clone YOUR_REPO_LINK
cd PDC-Sp24-BSCS22067-Rabbani


### 2. Create a virtual environment

python -m venv venv


### 3. Activate the virtual environment

venv\Scripts\activate


### 4. Install dependencies

pip install fastapi uvicorn requests


---

## Running the Project

Run the FastAPI server using:


uvicorn main:app --reload


After running, open your browser and go to:


http://127.0.0.1:8000/ask


---

## How the System Works

1. The system simulates an external API (LLM) that always fails.
2. Initially, the API is called and fails.
3. After 3 consecutive failures, the Circuit Breaker activates.
4. When the circuit is open:
   - No request is sent to the external API
   - A fallback response is returned instantly
5. After 10 seconds, the system attempts to recover automatically.

This prevents the system from blocking and improves availability.

---

## API Endpoint

### GET /ask

Possible responses:

- Before circuit opens:

Fallback response due to failure


- After circuit opens:

Fallback response (API unavailable)


---

## Middleware Requirement

This project includes a required FastAPI middleware.

Every API response contains the following header:


X-Student-ID: BSCS22067


---

## Demo Description

The demo video shows:

1. Running the FastAPI server
2. Sending requests to the API
3. Observing repeated failures
4. Circuit breaker activation after threshold
5. Instant fallback response after activation

---

## Author

Faizan Rabbani  
BSCS22067
