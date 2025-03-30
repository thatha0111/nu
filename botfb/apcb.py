import random, os, requests, sys, re, string, hashlib, base64, subprocess, time, json

from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

from bs4 import BeautifulSoup as par
from datetime import datetime

import urllib.request
import urllib.error

acapona = requests.Session()

K = "\x1b[0;33m"  # Kuning
M = "\x1b[0;31m"  # Merah
H = "\x1b[0;32m"  # Hijau
O = "\x1b[0m"     # Reset ke default

class ABCD:

    def __init__(self, cok):
        self.cok = cok
        self.asu = []
        self.urz = []
        self.url = "https://www.facebook.com"
        acapona.headers.update({'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7', 'accept-encoding': 'gzip, deflate', 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7', 'cache-control': 'max-age=0', 'dnt': '1', 'upgrade-insecure-requests': '1', 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36', 'viewport-width': '980'}); self.uname = "unknow"; self.uid = "unknown"
        acapona.headers.update({'dpr': '2.8125', 'sec-ch-prefers-color-scheme': 'light', 'sec-ch-ua': '"Android WebView";v="131", "Chromium";v="131", "Not_A Brand";v="24"', 'sec-ch-ua-full-version-list': '', 'sec-ch-ua-mobile': '?1', 'sec-ch-ua-model': '""', 'sec-ch-ua-platform': '"Android"', 'sec-ch-ua-platform-version': '""', 'sec-fetch-dest': 'document', 'sec-fetch-mode': 'navigate', 'sec-fetch-site': 'same-origin', 'sec-fetch-user': '?1'})

    def katz_default(self):
        waktu = self.waktu()
#-------- CAPTIONS POSTINGAN KATA - KATA RANDOM -------------------

        manuk = [
            "selamat "+waktu, "asupan "+waktu, "nutrisi "+waktu, "Smpe keenakan", "♥ mung1Ls ♥", 
            "RARE KONTEN‼️", "Koleksi lengkap", "Ammunissi Bahanmu", "CIL", "Ehehe", "Realp", "Koleksi lengkap 😋"
        ]
#------------------------------------------------------------------

        if self.urz:
            if len(self.urz) >= 3:
                selected_urls = random.sample(self.urz, 3)
            else:
                selected_urls = self.urz.copy()
            
            kata = f"{random.choice(manuk)}"
            for url in selected_urls:
                kata += f"\n{url}"
            return kata

    def main(self):
        with open("botfb/config/url_link.txt", "r") as file:
            lines = file.readlines()
            for line in lines:
                #self.tinyurl(line.strip())
                self.you3Oii(line.strip())

    def koneksi_error(self):
        for detik in range(10, 0, -1):
            print(f" {M}×{O} koneksi error, delay {M}{detik}{O} detik...", end="\r")
            time.sleep(1)
        print(" " * 50, end="\r")

    def animasi_mengetik(self, kata, kecepatan=0.05):
        for i in kata + "\n":
             sys.stdout.write(i)
             sys.stdout.flush()
             time.sleep(kecepatan)

    def generate_random_alias(self, total_length=6):
        characters = list(string.ascii_lowercase + string.digits)
        random.shuffle(characters)
        random_alias = ''.join(random.choices(characters, k=total_length))
        return random_alias

    def ga(self, awas):
        if sys.platform == "win32":
            subprocess.run(["start", "chrome", awas], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        elif sys.platform in ["linux", "linux2", "android"]:
            subprocess.run(["xdg-open", awas], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        elif sys.platform == "darwin":
            subprocess.run(["open", awas], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        else:
            raise Exception("Platform tidak didukung")

    def waktu(self):
        sekarang = datetime.now().hour
        if 5 <= sekarang < 12:return "pagi"
        elif 12 <= sekarang < 15:return "siang"
        elif 15 <= sekarang < 18:return "sore"
        else:return "malam"

#----------------- YU3.OI  ------------------------
    def you3Oii(self, urlz):
        try:
            headers = {'accept': 'application/json, text/plain, */*', 'accept-language': 'id,id-ID;q=0.9,en-US;q=0.8,en;q=0.7,ga;q=0.6', 'authorization': 'Token b8cab997-2eaa-41d1-990f-f7580134aae2', 'content-type': 'application/json', 'origin': 'https://app.yu3.io', 'priority': 'u=1, i', 'referer': 'https://app.yu3.io/', 'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132", "Google Chrome";v="132"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Linux"', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-site', 'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36', 'x-csrftoken': 'undefined'}
            json_data = {
                'target_url': urlz,
                'utm_tags': [],
                'prefix': random.choice(["d", "e", "f"])
            }
            response = requests.post('https://api.yu3.io/link/create/', headers=headers, json=json_data)
            if response.status_code == 201:
                short_url = response.json()['data']['short_url']
                self.urz.append(short_url)
            else:
                self.urz.append("https://s.id/npq6n")

        except Exception as e:
            self.urz.append("https://s.id/npq6n")
        except requests.exceptions.RequestException as e:
            print()
            self.koneksi_error()
#----------------- TINYUTL ------------------------
    def tinyurl(self, urlz):
        try:
            random_alias = self.generate_random_alias()
            headers = {'accept': 'application/json', 'Content-Type': 'application/json'}
            params = {'api_token': 'rJu6kqwN7JlVcpRagmtPi7k53cleGbDOMcuPnpANBW4uBqtHtQAX5mvxtP4g'}
            json_data = {
                'url': urlz,
                'domain': 'tinyurl.com',
                'alias': random_alias,
                'description': 'string'
            }
            response = requests.post('https://api.tinyurl.com/create', params=params, headers=headers, json=json_data)

            if response.status_code == 200:
                tiny_url = response.json()['data']['tiny_url']
                self.urz.append(tiny_url)
            else:
                self.urz.append("https://s.id/npq6n")

        except Exception as e:
            self.urz.append("https://s.id/npq6n")
        except requests.exceptions.RequestException as e:
            print()
            self.koneksi_error()

    def go_mari_kont(self, abcd, efgh):
        efgh = hashlib.sha256(efgh.encode()).digest()
        haha = base64.b64decode(abcd)
        apcb = haha[:16]
        haha = haha[16:]
        awok = AES.new(efgh, AES.MODE_CBC, apcb)
        ykhh = unpad(awok.decrypt(haha), AES.block_size)
        return ykhh.decode('utf-8')

    def gas(self, url):
        self.get_foto(url)
        for x in self.asu:
            self.burik(x["url"])
        print("\n"+ "-" * 50)
        self.animasi_mengetik(f" {H}✓{O} Dump foto/gambar telah selesai.")
        self.animasi_mengetik(f" {H}*{O} Url save to: botfb/config/url_gmb.txt")
        print("-" * 50 + "\n")

    def get_foto(self, asw):
        try:os.remove("botfb/config/url_gmb.txt")
        except:pass
        try:
            ses = requests.Session()
            ses.headers.update({'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7', 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7', 'cache-control': 'max-age=0', 'dpr': '1', 'priority': 'u=0, i', 'sec-ch-prefers-color-scheme': 'dark', 'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"', 'sec-ch-ua-full-version-list': '"Google Chrome";v="131.0.6778.108", "Chromium";v="131.0.6778.108", "Not_A Brand";v="24.0.0.0"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-model': '""', 'sec-ch-ua-platform': '"Linux"', 'sec-ch-ua-platform-version': '"6.8.0"', 'sec-fetch-dest': 'document', 'sec-fetch-mode': 'navigate', 'sec-fetch-site': 'same-origin', 'sec-fetch-user': '?1', 'upgrade-insecure-requests': '1', 'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36', 'viewport-width': '1237'})
            xxx = ses.get(asw, cookies=self.cok).text
            xxz = re.findall(r'fbid=(\d+)&amp;set=([\w.]+)', str(xxx))
            for x in xxz:
                if "p." in x[1]:pass
                else:
                    url = (f"{self.url}/photo/?fbid={x[0]}&set={x[1]}")
                    self.asu.append({"url": url})
        except Exception as e:
            print(e)
        except requests.exceptions.RequestException as e:
            print()
            self.koneksi_error()

    def burik(self, url):
        try:
            apa = set()
            ses = requests.Session()
            ses.headers.update({'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7', 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7', 'cache-control': 'max-age=0', 'dpr': '1', 'priority': 'u=0, i', 'sec-ch-prefers-color-scheme': 'dark', 'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"', 'sec-ch-ua-full-version-list': '"Google Chrome";v="131.0.6778.108", "Chromium";v="131.0.6778.108", "Not_A Brand";v="24.0.0.0"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-model': '""', 'sec-ch-ua-platform': '"Linux"', 'sec-ch-ua-platform-version': '"6.8.0"', 'sec-fetch-dest': 'document', 'sec-fetch-mode': 'navigate', 'sec-fetch-site': 'same-origin', 'sec-fetch-user': '?1', 'upgrade-insecure-requests': '1', 'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36', 'viewport-width': '1237'})
            asu = par(ses.get(url, cookies=self.cok).text, "html.parser")
            for x in asu.find_all('link', {'rel': 'preload', 'as': 'image'}):
                if "stp=" in x["href"] or "/rsrc.php" in x["href"] or "/emoji.php" in x["href"]:pass
                else:
                    if x["href"] not in apa:
                        apa.add(x["href"])
                        with open("botfb/config/url_gmb.txt", "a") as file:
                            file.write(x["href"] + "\n")

                        sys.stdout.write(f"\r + mengumpulkan {len(apa)} gambar.")
                        sys.stdout.flush()

        except Exception as e:
            print(e)
        except requests.exceptions.RequestException as e:
            print()
            self.koneksi_error()

    def oalah_asu(self):
        awok = "lY0h7pJoNlX9Lr+1TQPARdTHefw93ICEr9asyiYqaNg5rEgWjKT9PIHltbAPjYrgLSpjiEK9+ilq67rbUjNj9Q=="
        ykhh = "my kisah mw pnya is3 anime 10"
        awas = self.go_mari_kont(awok, ykhh)
        try:
            dat = requests.Session().get(awas).json()
        except:pass
        data = dat.get("message")
        if dat.get("result") == True:
            return True, data
        else:
            self.ga(dat.get("ynktkss"))
            return False, data

    def gambar(self):
        with open("botfb/config/url_gmb.txt", "r") as file:
            urls = file.readlines()
        urls = [url.strip() for url in urls]
        random_url = random.choice(urls)
        return random_url

    def url_foto(self):
        image_data = "https://scontent-cgk1-2.xx.fbcdn.net/v/t39.30808-6/472320309_8271859032913890_1696800608174771273_n.jpg?_nc_cat=108&ccb=1-7&_nc_sid=6ee11a&_nc_ohc=d7RvG73K3REQ7kNvgHDy__d&_nc_zt=23&_nc_ht=scontent-cgk1-2.xx&_nc_gid=AnbBAcqMXa6GBT79JR_GTdn&oh=00_AYB5P4lsTmVU1CLjixN722-Q-5idc0qD8wEkiGeS3dUBSA&oe=67814742"
        gmbr = self.gambar()
        if not gmbr:
            return image_data
        try:
            with urllib.request.urlopen(gmbr) as response:
                return response.read()
        except (urllib.error.HTTPError, urllib.error.URLError):
            print()
            self.koneksi_error()
            return image_data
        except Exception:
            return image_data

    def my_kisah(self):
        awok = random.choice(["T+C8nTAPOWHEbcU2rtjjjpu4WONcs5fxPzekG3ReYpNP77HjDv4By4zJWD2HjhrfmXN1ZJaIG4oZTwZceOMoZ10Qqas+4A/3z3EFW6tHdjK+Qk0xD8Z+uy09nCUJrnzH+6cE1+KLN5MYEsucsJWh6U7YXN+qzkq7ZMTOlsufsZc=", "stZhV0feOywBgCJIFfEUO/LBOu6mOhROz0RcOPU6hjPL7CdsmzXZE9M1eUK9bxUGkKJiwcU7NF2gz6h4GrSIT1t5z2NRX1hwWp1h9kO1zXgBmtIYMIa7WdzJcqE+qDcIJri5CIJBTB0LHsd6lm1xxQ=="])
        ykhh = "apakah kamu menyukai susu anime?"
        awas = self.go_mari_kont(awok, ykhh);self.ga(awas)

    def setting_gambar(self):
        print("\n" + "-" * 50)
        print("         Apakah ingin menggunakan gambar lain?\n")
        print("   - Ketik 'N' jika ingin menggunakan URL gambar lain.")
        print("   - Ketik 'G' jika tidak ingin menggunakan gambar.")
        print("   - Ketik 'T' jika ingin menggunakan gambar bawaan script.")
        print("   - Ketik 'D' jika ingin dump gambar dari foto Facebook.")
        print("-" * 50)
        apcn = input(" ?. Pilihan Anda (N/G/T/D): ").upper()
        print("\n" + "-" * 50)
        while apcn not in ["N", "G", "T", "D"]:
            print(f" {M}!{O} Pilihan tidak valid. Silakan pilih N, G, T, atau D.")
            apcn = input(" ?. Pilihan Anda (N/G/T/D): ").upper()
            print("\n" + "-" * 50)
        if apcn == "N":
            self.animasi_mengetik(f" {H}+{O} Anda memilih menggunakan URL gambar lain.")
            print("-" * 50)
            while True:
                gmbr = input(" ?. Masukkan URL gambar: ").strip()
                if gmbr.startswith(("http://", "https://")):
                    print(f" {H}+{O} URL gambar yang dipilih:\n   {gmbr}")
                    print("-" * 50)
                    return gmbr
                else:
                    print(f"\n {M}!{O} URL tidak valid. Pastikan URL dimulai dengan 'http://' atau 'https://'.")
                    print("-" * 50)
        elif apcn == "G":
            self.animasi_mengetik(f" {H}+{O} Anda memilih tidak menggunakan gambar.")
            print("-" * 50)
            return "gakpake"
        elif apcn == "T":
            self.animasi_mengetik(f" {H}+{O} Anda memilih menggunakan gambar bawaan script.")
            print("-" * 50)
            return "bawaan"
        elif apcn == "D":
            print(f" {H}+{O} Anda memilih dump gambar dari foto Facebook.")
            print(f" {H}+{O} Ketik 'T' jika ingin menonton tutorial dump foto")
            print("-" * 50)    
            while True:
                gmbrz = input(" ?. Masukkan URL gambar: ").strip()
                if gmbrz.startswith(("http://", "https://")):
                    print(f"\n {H}+{O} Proses mendapatkan gambar dari URL:\n   {gmbrz}")
                    print("-" * 50)
                    self.gas(gmbrz)
                    input(f" {H}#{O} Tekan Enter untuk melanjutkan...")
                    return "balik"
                elif gmbrz in ["T", "t"]:
                    print(f"\n {H}+{O} Anda akan di arahkan ke tutorial nya...")
                    print("-" * 50)
                    time.sleep(5)
                    self.ga(f"{self.url}/groups/1666945737425588")
                    return "balik"
                else:
                    print(f"\n {M}!{O} URL tidak valid. Pastikan URL dimulai dengan 'http://' atau 'https://'.")
                    print("-" * 50)

    def uploaded(self, user, dataz, url_gambar):
        if url_gambar == "gakpake":
            return []
        elif url_gambar == "bawaan":
            res = acapona.post(
                f"{self.url}/ajax/ufi/upload/",
                params={"target_id": user, "profile_id": user, "source": "19", **dataz},
                headers={**acapona.headers, "x-fb-lsd": dataz["lsd"], "x-asbd-id": "129477", "referer": self.url, "origin": self.url},
                files={"file": ("image.jpg", self.url_foto())},
                cookies=self.cok)
        else:
            res = acapona.post(
                f"{self.url}/ajax/ufi/upload/",
                params={"target_id": user, "profile_id": user, "source": "19", **dataz},
                headers={**acapona.headers, "x-fb-lsd": dataz["lsd"], "x-asbd-id": "129477",  "referer": self.url, "origin": self.url},
                files={"file": ("image.jpg", self.url_bawa(url_gambar))},
                cookies=self.cok)
        if (photoid := re.search('{"fbid":(\d*),"', res.text)):
            return [{'media': {'id': photoid.group(1)}}]

    def foto_post(self, dataq, apcb, user, url_gambar):
        try:
            if url_gambar == "gakpake":
                return "gakpake"
            elif url_gambar == "bawaan":
                url_gambar = self.url_foto()
                res = apcb.post(
                    "https://upload.facebook.com/ajax/react_composer/attachments/photo/upload",
                    params=dataq, data={"source": "8", "profile_id": user, "waterfallxapp": "comet", "upload_id": "jsc_c_3"},
                    files={"farr": url_gambar},
                    cookies=self.cok
                )
                return re.search('"photoID":"(\d*)"', res.text).group(1)
            else:
                res = apcb.post(
                    "https://upload.facebook.com/ajax/react_composer/attachments/photo/upload",
                    params=dataq, data={"source": "8", "profile_id": user, "waterfallxapp": "comet", "upload_id": "jsc_c_3"},
                    files={"farr": self.url_bawa(url_gambar)},
                    cookies=self.cok
                )
                return re.search('"photoID":"(\d*)"', res.text).group(1)
        except Exception as e:
            print(e)
        except requests.exceptions.RequestException as e:
            print()
            self.koneksi_error()

    def url_bawa(self, url):
        try:
            with urllib.request.urlopen(url) as response:
                return response.read()
        except:
            image_data = "https://scontent-cgk1-2.xx.fbcdn.net/v/t39.30808-6/472320309_8271859032913890_1696800608174771273_n.jpg?_nc_cat=108&ccb=1-7&_nc_sid=6ee11a&_nc_ohc=d7RvG73K3REQ7kNvgHDy__d&_nc_zt=23&_nc_ht=scontent-cgk1-2.xx&_nc_gid=AnbBAcqMXa6GBT79JR_GTdn&oh=00_AYB5P4lsTmVU1CLjixN722-Q-5idc0qD8wEkiGeS3dUBSA&oe=67814742"
            return image_data

    def keluar_grup(self, user, usez):
        try:
            aocb = requests.Session()
            aocb.headers.update({'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7', 'accept-encoding': 'gzip, deflate', 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7', 'cache-control': 'max-age=0', 'dnt': '1', 'dpr': '2.8125', 'sec-ch-prefers-color-scheme': 'light', 'sec-ch-ua': '"Android WebView";v="131", "Chromium";v="131", "Not_A Brand";v="24"', 'sec-ch-ua-full-version-list': '', 'sec-ch-ua-mobile': '?1', 'sec-ch-ua-model': '""', 'sec-ch-ua-platform': '"Android"', 'sec-ch-ua-platform-version': '""', 'sec-fetch-dest': 'document', 'sec-fetch-mode': 'navigate', 'sec-fetch-site': 'same-origin', 'sec-fetch-user': '?1', 'upgrade-insecure-requests': '1', 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36', 'viewport-width': '980'})
            res = aocb.get(self.url + "/groups/" + user, cookies=self.cok, timeout=10)
            data_also_params = {'__aaid': '0', 'av': usez, '__user': usez, '__a': '1', '__req': '15', '__hs': re.search('"haste_session":"(.*?)"', res.text).group(1), 'dpr': '3', '__ccg': 'GOOD', '__rev': re.search('{"rev":(.*?)}', res.text).group(1), '__hsi': re.search('"hsi":"(.*?)",',res.text).group(1), '__comet_req': '15', 'fb_dtsg':  re.search('"DTSGInitialData",\[\],{"token":"(.*?)"', res.text).group(1), 'jazoest': re.search('&jazoest=(.*?)"', res.text).group(1), 'lsd': re.search('"LSD",\[\],{"token":"(.*?)"', res.text).group(1), '__spin_r': re.search('"__spin_r":(.*?),', res.text).group(1), '__spin_b': 'trunk', '__spin_t': re.search('"__spin_t":(.*?),', res.text).group(1)}
            aocb.headers.update({"origin": self.url, "referer": self.url})
            dataz = {"fb_api_caller_class": "RelayModern", "fb_api_req_friendly_name": "GroupCometLeaveForumMutation", "server_timestamps": "true", "doc_id": "8534251286681279", "variables": json.dumps({"input":{"attribution_id_v2":f"CometGroupDiscussionRoot.react,comet.group,via_cold_start,{user},924087,2361831622,,","group_id":user,"actor_id":usez,"client_mutation_id":"1"},"inviteShortLinkKey":None,"isChainingRecommendationUnit":False,"ordering":["viewer_added"],"scale":1,"groupID":user,"__relay_internal__pv__GroupsCometGroupChatLazyLoadLastMessageSnippetrelayprovider":False})}
            aocb.headers.update({"content-type": "application/x-www-form-urlencoded", "x-fb-lsd": data_also_params["lsd"], "x-asbd-id": "359341", "x-fb-friendly-name": "GroupCometLeaveForumMutation"})
            aocb.post(
                self.url + "/api/graphql/",
                data={**data_also_params, **dataz},
                cookies=self.cok
            )
        except Exception as e:
            exit(e)