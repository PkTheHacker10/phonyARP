import socket

ip=socket.gethostbyname(socket.gethostname())
print(f"Ip : {ip}")

first_octet=ip.split(".")[0]
print(first_octet)
def classip(first_octet):
    if 1 <= first_octet <= 126:
        return "Class A"
    elif 128 <= first_octet <= 191:
        return "Class B"
    elif 192 <= first_octet <= 223:
        return "Class C"
    elif 224 <= first_octet <= 239:
        return "Class D (Multicast)"
    elif 240 <= first_octet <= 255:
        return "Class E (Experimental)"
    else:
        return "Unknown Class"

print(classip(int(first_octet)))