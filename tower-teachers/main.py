import specklepy
from specklepy.api.client import SpeckleClient
import os
from dotenv import load_dotenv

print("✓ specklepy installed successfully!")

def main():
    print("Hello from tower-teachers!")

    # Load environment variables from a local .env file, if present
    load_dotenv()

    # Get token and server host from environment
    token = os.environ.get("SPECKLE_TOKEN")
    server_host = os.environ.get("SPECKLE_SERVER", "app.speckle.systems")

    if not token:
        print("Set SPECKLE_TOKEN in your .env and re-run.")
        return

    # Authenticate
    client = SpeckleClient(host=server_host)
    client.authenticate_with_token(token)
    print(f"✓ Authenticated to {server_host}")

    # Check if authenticated
    if client.account.token:
        print("✓ Authenticated")

    # Get current user info
        user = client.active_user.get()
        print(f"Logged in as: {user.name}")
    else:
        print("✗ Not authenticated")


if __name__ == "__main__":
    main()
