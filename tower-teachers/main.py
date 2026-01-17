import specklepy
from specklepy.api.client import SpeckleClient
from specklepy.objects.geometry import Point
from specklepy.api import operations
import os
from dotenv import load_dotenv

print("✓ specklepy installed successfully!")

def main():
    print("Hello from tower-teachers!")

    # Load environment variables from a local .env file, if present
    load_dotenv()

    # Get token from environment
    token = os.environ.get("SPECKLE_TOKEN")
    server_url = os.environ.get("SPECKLE_SERVER", "app.speckle.systems")

    if not token:
        raise ValueError("SPECKLE_TOKEN environment variable not set")

    # Authenticate
    client = SpeckleClient(host=server_url)
    client.authenticate_with_token(token)
    print(f"✓ Authenticated to {server_url}")


if __name__ == "__main__":
    main()
