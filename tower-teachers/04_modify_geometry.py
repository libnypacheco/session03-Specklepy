"""
04 - Modify Geometry in a Speckle Model

This script demonstrates how to receive geometry from Speckle,
modify it (e.g., transform, scale), and send it back.
"""

from main import get_client
from specklepy.transports.server import ServerTransport
from specklepy.api import operations
from specklepy.objects.geometry import Point, Line, Mesh


# TODO: Replace with your project and model IDs
PROJECT_ID = "your_project_id"
MODEL_ID = "your_model_id"


def transform_point(point: Point, offset_x=0, offset_y=0, offset_z=0, scale=1.0) -> Point:
    """Apply translation and scale to a point."""
    return Point(
        x=(point.x * scale) + offset_x,
        y=(point.y * scale) + offset_y,
        z=(point.z * scale) + offset_z,
        units=point.units
    )


def transform_mesh_vertices(mesh: Mesh, offset_z=0) -> Mesh:
    """Offset all vertices of a mesh in the Z direction."""
    if mesh.vertices:
        new_vertices = []
        # Vertices are stored as flat list: [x1, y1, z1, x2, y2, z2, ...]
        for i in range(0, len(mesh.vertices), 3):
            new_vertices.append(mesh.vertices[i])      # x
            new_vertices.append(mesh.vertices[i + 1])  # y
            new_vertices.append(mesh.vertices[i + 2] + offset_z)  # z + offset
        mesh.vertices = new_vertices
    return mesh


def main():
    # Authenticate
    client = get_client()

    # Get the latest version
    versions = client.version.get_versions(PROJECT_ID, MODEL_ID, limit=1)
    if not versions.items:
        print("No versions found.")
        return

    latest_version = versions.items[0]
    print(f"✓ Fetching version: {latest_version.id}")

    # Receive the data
    transport = ServerTransport(client=client, stream_id=PROJECT_ID)
    data = operations.receive(latest_version.referencedObject, transport)

    # Process elements and modify geometry
    elements = getattr(data, "@elements", None) or getattr(data, "elements", [])
    modified_count = 0

    for element in elements or []:
        # Example: Offset all points by 10 units in Z
        if isinstance(element, Point):
            element.z += 10.0
            modified_count += 1

        # Example: Offset mesh vertices
        elif isinstance(element, Mesh):
            transform_mesh_vertices(element, offset_z=10.0)
            modified_count += 1

        # Example: Modify lines by transforming their start/end points
        elif isinstance(element, Line):
            if hasattr(element, "start") and isinstance(element.start, Point):
                element.start.z += 10.0
            if hasattr(element, "end") and isinstance(element.end, Point):
                element.end.z += 10.0
            modified_count += 1

    print(f"✓ Modified {modified_count} geometry objects")

    # Send the modified data back
    object_id = operations.send(data, [transport])
    print(f"✓ Sent object: {object_id}")

    # Create a new version
    from specklepy.core.api.inputs.version_inputs import CreateVersionInput

    version = client.version.create(CreateVersionInput(
        projectId=PROJECT_ID,
        modelId=MODEL_ID,
        objectId=object_id,
        message="Modified geometry via specklepy (Z offset +10)"
    ))

    print(f"✓ Created version: {version.id}")


if __name__ == "__main__":
    main()
