from app import app


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("project:app", host="127.0.0.1", port=8000)
