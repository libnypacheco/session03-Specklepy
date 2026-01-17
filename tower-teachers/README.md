### — `.env` file (recommended)

1. Create a file `.env`.
2. Fill in your values:

```dotenv
SPECKLE_TOKEN=your_token_here
SPECKLE_SERVER=https://app.speckle.systems
```

### Install dependencies

```powershell
uv add python-dotenv
uv sync
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
