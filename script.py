import subprocess

command = "python app.py &"

subprocess.Popen(command, shell=True)