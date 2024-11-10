# Minecraft server

Tools to manage a Minecraft server

## Manage a server

This script support the following features:

- Start a minecraft server
- Automatically stop/start the server during closing/opening hours
- Make automatic announcements

```bash
python3 manage-server.py
```

When stopping the script, you will need to manually stop the minecraft server and the screen session.
You will also need to remove the screenlog.0 file.

## Get a server infos

```bash
# Create a virtual environment
python3 -m venv venv
source venv/bin/activate

# Install the requirements
pip install -r requirements.txt

# Run the script
python3 server-status.py
```
