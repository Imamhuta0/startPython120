from ipaddress import*
net = ip_network('192.168.32.160/255.255.255.240')
for ip in net:
    print(ip)

def valid(ip):
    return f'{ip:b}'.count('1') % 2 == 0
net = ip_network('192.168.32.160/255.255.255.240')
count = 0
for ip in net:
    if valid(ip):
     count +=1
print(count)
