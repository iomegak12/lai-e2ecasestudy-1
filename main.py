import uvicorn
import os

from art import tprint

if __name__ == "__main__":
    # Print the logo
    tprint("Stores API")
    print("Starting Store Service...")

    # Get the environment variable for the host and port
    host = os.getenv("HOST", "0.0.0.0")
    port = int(os.getenv("PORT", 8000))

    uvicorn.run(
        "store_service.api:app",
        host=host,
        port=port,
        log_level="info",
        reload=True,
        workers=1,
    )

    print("Store Service started successfully.")
