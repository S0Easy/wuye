import psutil
import paramiko
import re

def get_cpu_info(ip, username, password):

    with paramiko.SSHClient() as ssh:
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname=ip, username=username, password=password)
        stdin, stdout, stderr = ssh.exec_command("lscpu")
        output = stdout.read().decode('utf-8')
        match = re.search(r'CPU\(s\):\s+(\d+)', output)
        cores = match.group(1) if match else 0
    return cores

