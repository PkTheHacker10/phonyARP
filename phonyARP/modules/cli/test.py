import subprocess
result = subprocess.run(["hostname", "-I"], capture_output=True, text=True)

print(result.stdout)
