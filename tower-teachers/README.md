## Speckle Authentication Setup (Windows)

- **Environment variables**: The app reads `SPECKLE_TOKEN` and `SPECKLE_SERVER`.
- **Simple approach**: Values are used as-is, no extra parsing.

### Option 1 — Session-only (PowerShell)

Run these in the VS Code terminal before starting the app:

```powershell
$env:SPECKLE_TOKEN = "your_token_here"
$env:SPECKLE_SERVER = "https://app.speckle.systems"
```

### Option 2 — Persistent user variables

Set once for your Windows user account, then restart VS Code:

```powershell
[Environment]::SetEnvironmentVariable("SPECKLE_TOKEN", "your_token_here", "User")
[Environment]::SetEnvironmentVariable("SPECKLE_SERVER", "https://app.speckle.systems", "User")
```

### Option 3 — `.env` file (recommended)

1. Copy [tower-teachers/.env.example](tower-teachers/.env.example) to `.env`.
2. Fill in your values:

```dotenv
SPECKLE_TOKEN=your_token_here
SPECKLE_SERVER=https://app.speckle.systems
```

### Install dependencies

```powershell
pip install .
```

Dependencies are declared in [tower-teachers/pyproject.toml](tower-teachers/pyproject.toml).

### Run the script

```powershell
python tower-teachers/main.py
```

Expected output on success:

```
✓ specklepy installed successfully!
Hello from tower-teachers!
✓ Authenticated to https://app.speckle.systems
```

If `SPECKLE_TOKEN` is missing, you'll see:

```
ValueError: SPECKLE_TOKEN environment variable not set
```
