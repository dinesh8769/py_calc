import subprocess
log=subprocess.run(["git", "log"],capture_output=True)
log_readable=log.stdout.decode()
print("This is log for debugging")
print(log_readable)
file = open("delta.txt", "w")
file.write(log_readable)
file.close()
