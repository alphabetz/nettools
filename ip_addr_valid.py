import sys
import ipaddress

#Check ip addresses are not in reserved IP"

def ip_addr_valid(list):
    try:
        for ip in list:
            ip = ip.rstrip()
            if (
                ipaddress.ip_network(ip, strict=False).is_multicast
                or ipaddress.ip_network(ip, strict=False).is_global
                or ipaddress.ip_network(ip, strict=False).is_unspecified
                or ipaddress.ip_network(ip, strict=False).is_reserved
                or ipaddress.ip_network(ip, strict=False).is_loopback
                or ipaddress.ip_network(ip, strict=False).is_link_local
            ):
                print("The ip {0} is a restricted IPv4 in the list please recheck".format(ip))
                sys.exit()
    except ValueError as err:
        print("Value error: {0}".format(err))
        sys.exit()

if __name__ == "__main__":
    list = ["192.168.1.9/24","192.168.5.4", "202.22.0.66"]
    ip_addr_valid(list)