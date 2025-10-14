import threading
import requests
import time

def download(url):
    print(f"Starting download from {url} ")
    resp = requests.get(url)
    print(f"finfnshed downloading from {url} ,size:{len(resp.content)} byte")

urls = [
    "https://httpbin.org/image/jpeg",
    "https://httpsbin.org/image/png",
    "https://httpsbin.org/image/svg",
]

start = time.time()
threads = []
for url in urls:
    t = threading.Thread(target=download,args=(url,))
    t.start()
    threads.append(t)

for t in threads:
    t.join()

end = time.time()

print(f"All downloads done in {end-start:.2f} seconds")
