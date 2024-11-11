from mcstatus import JavaServer
from prompt_toolkit import prompt

ADDRESS_FILE = "last_address.txt"

try:
    with open(ADDRESS_FILE, "r") as last_address_file:
        last_address = last_address_file.read()
except FileNotFoundError:
    last_address = ""

address = prompt("Enter the server address: ", default=last_address)
port = prompt("Enter the server port: ", default="25565")

with open(ADDRESS_FILE, "w") as last_address_file:
    last_address_file.write(address)

server = JavaServer.lookup(f"{address}:{port}")

status = server.status()
print(f"The server has {status.players.online} player(s) online and replied in {status.latency} ms")
if status.players.online > 0:
    players = ", ".join([player.name for player in status.players.sample])
    print("Players online (might not be exhaustive):", players)
