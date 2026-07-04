import uvicorn

if __name__ == "__main__":
    uvicorn.run("src.trivia_with_friends.app:app", port=8080, reload=True)
