# Minecraft server

This repository contains two scripts:

- `manage-server.py`: a script to manage a minecraft server
- `server-status.py`: a script to get information about a server

## Manage a server

The `manage-server.py` script supports the following features:

- Start a minecraft server
- Automatically stop/start the server during closing/opening hours
- Make automatic announcements

### How to use?

```bash
python3 manage-server.py
```

When stopping the script, you will need to manually stop the minecraft server and the screen session.
You will also need to remove the screenlog.0 file.

## Get a server info

The `server-status.py` script allows you to get information about a server.

### How to use?

```bash
# Create a virtual environment
python3 -m venv venv
source venv/bin/activate

# Install the requirements
pip install -r requirements.txt

# Run the script
python3 server-status.py
```
