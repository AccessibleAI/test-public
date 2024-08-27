from fastapi import FastAPI
import sys

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

if __name__ == "__main__":
    import uvicorn
    # Default port
    port = 8000

    # Check if a port was given as a command line argument
    if len(sys.argv) > 1:
        try:
            port = int(sys.argv[1])
        except ValueError:
            print("Invalid port number. Using default port 8000.")

    # Start the server with the specified port
    uvicorn.run(app, host="0.0.0.0", port=port)
