"""
02 - Fetch Information from a Speckle Model

This script demonstrates how to fetch and explore data from
an existing Speckle model/version.
"""

from main import get_client
from specklepy.transports.server import ServerTransport
from specklepy.api import operations


# TODO: Replace with your project and model IDs
PROJECT_ID = "your_project_id"
MODEL_ID = "your_model_id"


def main():
    # Authenticate
    client = get_client()

    # Get the model (branch) info
    model = client.model.get(PROJECT_ID, MODEL_ID)
    print(f"✓ Model: {model.name}")

    # Get the latest version (commit)
    versions = client.version.get_versions(PROJECT_ID, MODEL_ID, limit=1)
    if not versions.items:
        print("No versions found in this model.")
        return

    latest_version = versions.items[0]
    print(f"  Latest version: {latest_version.id}")
    print(f"  Message: {latest_version.message}")

    # Receive the data from Speckle
    transport = ServerTransport(client=client, stream_id=PROJECT_ID)
    data = operations.receive(latest_version.referencedObject, transport)

    print(f"\n✓ Received object: {data.speckle_type}")
    print(f"  Total children: {data.totalChildrenCount}")

    # Explore the data structure
    if hasattr(data, "@elements") or hasattr(data, "elements"):
        elements = getattr(data, "@elements", None) or getattr(data, "elements", [])
        print(f"  Elements: {len(elements) if elements else 0}")


if __name__ == "__main__":
    main()
