# Session-03-SpecklePy
Basics of SpecklePy

## Instructions
- Clone this repo
- Install uv if you don't have it
```
pip install uv
```

- Create a new project with virtual environment
```
uv init my-speckle-project
cd my-speckle-project
```

- Add specklepy
```
uv add specklepy
```

- Activate or select the virtual environment created by uv, localted in .venv > Scripts > Python.exe

- Run main.py

- To test Specklepy installation, add this code to Main.py
```
import specklepy
from specklepy.api.client import SpeckleClient
from specklepy.objects.geometry import Point
from specklepy.api import operations

print("✓ specklepy installed successfully!")
```

- Commit your changes to GitHub.
```
git config --global commit.gpgsign false
```