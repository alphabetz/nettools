import sys
import ipaddress

#Check ip addresses are not in reserved IP"

def ip_addr_valid(list):
    for ip in list:
        ip = ip.rstrip()
        if (
            ipaddress.ip_address(ip).is_multicast
            or ipaddress.ip_address(ip).is_global
            or ipaddress.ip_address(ip).is_unspecified
            or ipaddress.ip_address(ip).is_reserved
            or ipaddress.ip_address(ip).is_loopback
            or ipaddress.ip_address(ip).is_link_local
        ):
            print("There is invalid ip!",ip)
            sys.exit()

if __name__ == "__main__":
    list = ["192.168.1.0","192.168.5.4","127.0.0.1"]
    ip_addr_valid(list)