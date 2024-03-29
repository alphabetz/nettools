import paramiko
import os.path
import time
import sys

# Check username/password file exist
user_file = input("\n# Enter user file path and name: ")
if os.path.isfile(user_file):
    print("\n *User file loaded* \n")
else:
    print("\n File does not exist please recheck your path and file name.")
    sys.exit()

cmd_file = input("\n# Enter command file path and name: ")
if os.path.isfile(cmd_file):
    print("\n *command loaded* \n")
else:
    print("\n File does not exist please recheck your path and file name.")
    sys.exit()


def ssh_connection(ip):
    global user_file
    global cmd_file

    try:
        selected_user_file = open(user_file, 'r')
        selected_user_file.seek(0)
        lines = selected_user_file.readlines()
        for line in lines:
            username, password = line.rstrip('\n').split(',')
        
        selected_cmd_file = open(cmd_file, 'r')
        selected_cmd_file.seek(0)

        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.RejectPolicy())
        ssh.connect(ip.rstrip("\n"), username = username, password = password.strip())
        print(f"Connecting to \x1b[0;30;42m'{ip}'\x1b[0m with username \x1b[0;30;42m'{username}'\x1b[0m")
        time.sleep(2)

        for cmd in selected_cmd_file.readlines():
            print(f"Sending \x1b[2;30;44m'{cmd.strip()}'\x1b[0m command to \x1b[0;30;42m'{ip}'\x1b[0m")
            time.sleep(2)
            stdin, stdout, stderr = ssh.exec_command(cmd, get_pty=True)
            for line in iter(stdout.readline, ""):
                print(line, end="")
        time.sleep(2)

        ssh.close()
        selected_user_file.close()
        selected_cmd_file.close()

    except paramiko.AuthenticationException:
        print("* Invalid username or password \n* Please check the username/password file or the device configuration.")
        print("* Closing program...")


