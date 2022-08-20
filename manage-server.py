import os
import time
import datetime
from threading import Thread
import random

class Server:
	def __init__(self):
		self.is_running = False
		self.is_stopping = False

	def Started(self):
		self.is_running = True

	def Stopped(self):
		self.is_running = False
		self.is_stopping = False

	def Stopping(self):
		self.is_stopping = True

def start_server():
	os.system('screen -dmS "minecraft" -L java -Xmx1024M -Xms1024M -jar server.jar nogui')
	print_without_new_line("Server is starting ")

def stop_server():
	run_command('stop')
	print_without_new_line("Stopping server ")

def run_command(command):
	os.system('screen -S minecraft -X stuff "{}\015"'.format(command))

def server_started() -> bool:
	with open('screenlog.0', 'r') as reader:
		return "Done" in reader.read()

def server_stopped() -> bool:
	running_sessions = os.popen('screen -ls').read()
	return 'minecraft' not in running_sessions

def make_announcements(server):
	announcements = [
		"§6Ne me déranger pas entre 5 h et 11 h du matin ! Je fais dodo :)",
		"§6HODL !",
		"§601001000 01100101 01111001",
		"§6Je me demande à quoi ressemble un monde qui n\'est pas fait de cubes ...",
		"§6ATTENTION AUX CREEPERS !",
		"§6Allez ! Minez ! Minez !",
		"§6Tout le monde dit que le cercle est la forme parfaite, personnellement, je préfère le cube :)",
		"§6Le cube figure parmi les solides les plus remarquables de l\'espace, c\'est pas moi qui le dis, c\'est Wikipedia :)"
	]

	while True:
		time.sleep(1)
		if server.is_running and not server.is_stopping:
			announcement = random.choice(announcements)
			run_command('say '+announcement)
			print("The following announcement has just been made: "+announcement)

			# send a message every 15 minutes
			time.sleep(900)

def print_without_new_line(text):
	print(text, end="", flush=True)

def time_in_range(current, start, end) -> bool:
	return start <= current <= end

def main():
	server = Server()

	server_shutdown_time = datetime.time(5)
	server_opening_time = datetime.time(11)

	announcements_thread = Thread(target = make_announcements, args = (server,))
	announcements_thread.start()

	while True:
		currentTime = datetime.datetime.now().time()
		is_in_closure_hours = time_in_range(currentTime, server_shutdown_time, server_opening_time)

		# Server needs to be started
		if not server.is_running and not is_in_closure_hours:
			start_server()

			# Time.sleep required to give the system time to create the file 'screenlog.0'
			time.sleep(3)

			while not server_started():
				print_without_new_line(".")
				time.sleep(1)

			server.Started()
			print(" Done")
			continue

		time.sleep(20)

		# Server needs to be stopped
		if server.is_running and is_in_closure_hours:
			server.Stopping()
			stop_server()

			while(not server_stopped()):
				print_without_new_line(".")
				time.sleep(1)

			os.remove("screenlog.0")
			server.Stopped()
			print(" Done")

if __name__ == "__main__": main()

# TODO when stopping the script :
# - remove the screenlog.0 file
# - stop the minecraft server (and the screen session if needed)
