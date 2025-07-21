import subprocess
subprocess.run(["date"])
subprocess.run(["sleep","2"])  # sleeps for 2 seconds
# subprocess.run(["ls","this_file_does_not_exist"])

subprocess.run(["mkdir","sample"])
subprocess.run(["echo","Hi"])

# changing teh permissions
