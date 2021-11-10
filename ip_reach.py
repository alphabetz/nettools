import sys
import subprocess

# Check IP reachability


def ip_reach(list)-> None:
    # OS verification
    ping_option = "-c 2"
    try:
        subprocess.run("uname", stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except FileNotFoundError:
        ping_option = "/n 2"
    for ip in list:
        print("Pinging " + ip)
        reply = subprocess.run(
            ["ping", ping_option, ip],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
        if reply.returncode == 0:
            print("\n* {} is reachable\n".format(ip))
            continue
        else:
            print("\n* {} is not reachable, Check ip address and try again.".format(ip))
            sys.exit()


if __name__ == "__main__":
    list = ["192.168.1.1", "192.168.5.4", "127.0.0.1"]
    ip_reach(list)
