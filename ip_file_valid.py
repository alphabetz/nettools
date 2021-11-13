import os.path
import sys

# Check whether file contaning ip is valid.
def ip_file_valid():
    ip_file = input("\n# Enter IPv4 address file path and name: ")
    if os.path.isfile(ip_file):
        print("\n* IPv4 address file is valid \n")
    else:
        print("\n File {} does not exist please recheck.\n",format(ip_file))
        sys.exit()
    selected_ip_file = open(ip_file, 'r')
    selected_ip_file.seek(0)
    ip_list = selected_ip_file.readlines()
    selected_ip_file.close()

    return ip_list

if __name__ == "__main__":
    ip_file_valid()