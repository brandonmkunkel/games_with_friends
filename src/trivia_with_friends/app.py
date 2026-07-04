from fastapi import FastAPI

app = FastAPI(
    title="Trivia with Friends",
    description="A phone-based trivia server API.",
    version="0.1.0",
)


@app.get("/")
async def root():
    """Root endpoint to welcome users."""
    return {"message": "Welcome to Trivia with Friends API!"}


@app.get("/health")
async def health():
    """Health check endpoint."""
    return {"status": "ok"}
