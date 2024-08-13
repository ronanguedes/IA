import subprocess

# Executa o primeiro script
subprocess.run(["python", "1parte.py"])

# Após o primeiro script terminar, executa o segundo script
subprocess.run(["python", "2parte.py"])
