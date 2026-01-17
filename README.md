# Session-03-SpecklePy
Basics of SpecklePy

## Instructions
- Create a repository in your Github account named "session-03"
- Clone it to your PC (make a local copy):
- Copy the repo's URL
- In VSCode (in the Welcome tab), use the option "Clone Git Repository...", providing the URL.

- Open VSCode's terminal and Install uv
```
pip install uv
```

- Create a new project with virtual environment
```
uv init session-03
cd session-03
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