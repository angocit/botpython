import random
class Proxies:
    def proxieran(self):
        r = open('sock.txt', 'r')
        page = r.readlines();
        r.close()
        sock = random.choice(page)
        proxies = {
        'http': 'socks5://'+sock.strip(),
        'https': 'socks5://'+sock.strip()
        }
        # print(proxies)
        return proxies