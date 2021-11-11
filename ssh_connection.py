import paramiko
import os.path
import time
import sys
import re

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

        session = paramiko.SSHClient()
        session.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        session.connect(ip.rstip("\n"), username = username, password = password)
        connection = session.invoke_shell()

        connection.send("enable\n")
        connection.send("terminal length 0\n")
        time.sleep(1)

        connection.send("\n")
        connection.send("configure terminal")
        time.sleep(1)

        selected_cmd_file = open(cmd_file, 'r')
        selected_cmd_file.seek(0)
        for each_line in selected_cmd_file.readlines():
            connection.send(each_line + '\n')
            time.sleep(2)
        
        selected_user_file.close()
        selected_cmd_file.close()

        router_output = connection.recv(65535)
        if re.search(b"% Invalid input", router_output):
            print("* There was at least one IOS syntax error on device {} :(".format(ip))
        else:
            print("\nDONE for device {} :)\n".format(ip))
    except paramiko.AuthenticationException:
        print("* Invalid username or password :( \n* Please check the username/password file or the device configuration.")
        print("* Closing program... Bye!")


