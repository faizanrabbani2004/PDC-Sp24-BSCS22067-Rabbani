from fastapi import FastAPI
import time

app = FastAPI()

# Circuit breaker variables
failure_count = 0
CIRCUIT_OPEN = False
LAST_FAILURE_TIME = 0

FAILURE_THRESHOLD = 3
RESET_TIMEOUT = 10  # seconds

# 🔴 REQUIRED MIDDLEWARE (DO NOT CHANGE FORMAT)
@app.middleware("http")
async def add_student_id_header(request, call_next):
    response = await call_next(request)
    response.headers["X-Student-ID"] = "BSCS22067"
    return response


def call_llm():
    # Simulating external API failure
    raise Exception("LLM API failed")


@app.get("/ask")
def ask_question():
    global failure_count, CIRCUIT_OPEN, LAST_FAILURE_TIME

    # Check if circuit is open
    if CIRCUIT_OPEN:
        if time.time() - LAST_FAILURE_TIME > RESET_TIMEOUT:
            CIRCUIT_OPEN = False
        else:
            return {"message": "Fallback response (API unavailable)"}

    try:
        result = call_llm()
        failure_count = 0
        return {"response": result}

    except Exception:
        failure_count += 1
        LAST_FAILURE_TIME = time.time()

        if failure_count >= FAILURE_THRESHOLD:
            CIRCUIT_OPEN = True

        return {"message": "Fallback response due to failure"}