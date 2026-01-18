# Session-03-SpecklePy
Basics of SpecklePy

## Installation
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

- Activate or select the virtual environment created by uv, located in .venv > Scripts > Python.exe

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

## Authentication

_IMPORTANT: to avoid sharing or publishing password, tokens or files, you can create a .gitinore file and inside it add the files you dont want to be sent to the repository:_

```
# Ignore environment files containing secrets
.env
*.env

# Optional: ignore local virtual environments
.venv/
```


1. Create token in app.speckle.system. Click your avatar → Settings → Profile → Developer → Access Tokens

2. Click “New Token”, give it a name and select the required scopes, then copy the token.

3. Create a ".env" file in the "tower-teacher" folder

4. Fill in your values:

```dotenv
SPECKLE_TOKEN=your_token_here
SPECKLE_SERVER=https://app.speckle.systems
```

5. Before testing the authentication (by running main.py), install the package python-dotenv using uv, with the following code:

```
uv add python-dotenv
uv sync

```