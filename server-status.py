from mcstatus import JavaServer
from prompt_toolkit import prompt
from prompt_toolkit.shortcuts import CompleteStyle

address = input("Enter the server address: ")
port = prompt("Enter the server port: ", default="25565")

server = JavaServer.lookup(f"{address}:{port}")

status = server.status()
print(f"The server has {status.players.online} player(s) online and replied in {status.latency} ms")
if status.players.online > 0:
    print("Players online (might not be exhaustive):", ", ".join([player.name for player in status.players.sample]))
