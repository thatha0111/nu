import requests, os, sys, re, time

from bluid.getd import Yntks
from bluid.logo import Logo
from .Kynaraa import Kynaa
from .CekCP import Asu

H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
N = '\x1b[0m'	 # WARNA MATI
R = "\x1b[0;31m" # Merah

class Wangsaff:

    def __init__(self, lim, asw):
        self.ses = requests.Session()
        self.lim, self.asw = lim, asw
        self.uid, self.asu, self.apc = [], [], []

        try:open("data/cache/.cok.txt", "r").read()
        except FileNotFoundError:self.login()
        self.main()

    def hapus(self):
        try:os.remove("data/cache/.cok.txt")
        except:pass
        try:os.remove("data/cache/.tok.txt")
        except:pass

    def login(self):
        Logo("fesnuk")
        print(self.asw)
        print(f"   silahkan masukan cookie facebook")
        print("-" * 39)
        cok = input(" ?. cookie: ")
        try:
            self.ses.headers.update({
                'Accept-Language': 'id,en;q=0.9',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
                'Referer': 'https://www.instagram.com/',
                'Host': 'www.facebook.com',
                'Sec-Fetch-Mode': 'cors',
                'Accept': '*/*',
                'Connection': 'keep-alive',
                'Sec-Fetch-Site': 'cross-site',
                'Sec-Fetch-Dest': 'empty',
                'Origin': 'https://www.instagram.com',
                'Accept-Encoding': 'gzip, deflate'
                })
            response = self.ses.get('https://www.facebook.com/x/oauth/status?client_id=124024574287414&wants_cookie_data=true&origin=1&input_token=&sdk=joey&redirect_uri=https://www.instagram.com/yayanxd_/', cookies={'cookie':cok})
            if '"access_token":' in str(response.headers):
                token = re.search('"access_token":"(.*?)"', str(response.headers)).group(1)
                open("data/cache/.tok.txt", "a").write(token);open("data/cache/.cok.txt", "a").write(cok)
                exit("\n*. login telah berhasil, silahkan run ulang script nya.")
            else:print("\n!. login gagal, silahkan pakai cookie lain.");time.sleep(3);self.login()
        except Exception as e:exit(e)

    def main(self):
        token, cookies = open("data/cache/.tok.txt", "r").read().strip(), open("data/cache/.cok.txt", "r").read().strip()
        try:self.ses.get("https://graph.facebook.com/me?fields=name&access_token="+token, cookies = {"cookies":cookies}).json()["name"]
        except (KeyError, FileNotFoundError):
            print(f"[{K}!{N}] cookie kamu invalid.")
            time.sleep(5);self.hapus();self.login()
        except requests.ConnectionError:
            exit(f"[{R}!{N}] Tidak ada koneksi yang tersambung.")
        while True:
            Logo("fesnuk")
            print(self.asw)
            print(f"[{H}1{N}] mulai crack\n[{H}2{N}] cek result\n[{H}3{N}] sett UserAgent\n[{R}0{N}] kembali ke menu")
            pil = input("\n >> ")
            if pil in ["1", "01"]:
                self.apacoba(token, cookies)
            elif pil in ["2", "02"]:
                Asu(self.asw).cek()
            elif pil in ["3", "03"]:
                self.UserAgent()
            elif pil in ["0", "00"]:
                return
            else:
                print(f"\n !. pilih yang bener lah")
                time.sleep(1)
                continue

    def UserAgent(self):
        while True:
            print(f"\n[{H}1{N}] dump UserAgent\n[{H}2{N}] hapus UserAgent\n[{R}3{N}] kembali ke menu")
            fil = input("> ")
            if fil in ["1", "01"]:
                Yntks(self.asw, "data/cache/.sett_UaFB").pilihan()
            elif fil in ["2", "02"]:
                try:os.remove("data/cache/.sett_UaFB.json")
                except:pass
                print(f"\n[{H}✓{N}] berhasil menghapus UserAgent facebook")
                time.sleep(2);self.UserAgent()
            elif fil in ["3", "03"]:
                return
            else:
                print("! pilih yng bnr");time.sleep(1);self.UserAgent()


    def apacoba(self, token, cookies):
        if "Trial" in self.lim:
            print("\n[!] Anda adalah user trial, hanya bisa dump 1K ID.")
            for _ in range(1):
                while True:
                    idd = input("[?] Masukkan user ID: ").strip()
                    if idd:
                        self.uid.append(idd)
                        break
                    print("\n[!] Input tidak boleh kosong. Silakan masukkan ID yang valid.")

            self.pilih(token, cookies, 1000)
        else:
            while True:
                print("[+] Masukkan jumlah target yang mau Anda crack (maksimal 100)")
                try:
                    total = int(input("[?] Masukkan jumlah target: "))
                    if total > 100:
                        print("\n[!] Jumlah target tidak boleh lebih dari 100. Silakan coba lagi.")
                        continue
                    break
                except ValueError:
                    print("\n[!] Masukkan angka yang valid, bukan huruf atau enter.")
                    time.sleep(1)

            print(f"\n[+] Masukkan UID teman Facebook publik.")
            for mnh in range(total):
                while True:
                    idd = input(f"[?] UID ke-{mnh + 1}: ").strip()
                    if idd:
                        self.uid.append(idd)
                        break
                    print("\n[!] Input tidak boleh kosong. Silakan masukkan ID yang valid.")

            self.pilih(token, cookies, 100000000000000000000000)


    def pilih(self, token, cookies, lim):
        print()
        while True:
            print(f"[-] ketik '{H}Y{N}' jika ingin menggunakan metode api")
            pil = input("[?] pilihan metode (Y/t): ")
            if pil in ["Y", "y"]:
                self.dump_id(token, cookies, "api", lim)
            elif pil in ["T", "t"]:
                self.dump_id(token, cookies, "bkn", lim)
            else:
                print(f"\n !. pilih yang bener lah")
                time.sleep(1)
                continue

    def dump_id(self, token, cookies, tod, lim):
        if "api" in tod:
            print("\n[+] proses dump id facebook metode api")
            urz = "id,name,hometown"
        else:
            print("\n[+] proses dump id facebook metode not api")
            urz = "id,name,hometown"

        error_occurred = False
        total_dumped = 0

        for xxx in self.uid:
            if total_dumped >= lim:
                break
            try:
                url = f"https://graph.facebook.com/{xxx}?fields=friends.fields({urz})&access_token={token}"
                req = self.ses.get(url, cookies={"cookies": cookies}).json()
                if 'friends' in req and 'data' in req['friends']:
                    for x in req['friends']['data']:
                        if total_dumped >= lim:
                            break
                        try:
                            user_id = x.get("username", x["id"])
                            hometown = x.get("hometown", {}).get("name", "").split(",")[0] if "hometown" in x else ""
                            self.apc.append(f'{user_id}|{x["name"]}|{hometown}')
                            total_dumped += 1
                        except Exception as e:
                            self.apc.append(f'{x["id"]}|{x["name"]}|')
                            continue
                        sys.stdout.write(f"\r[{H}+{N}] Proses mengumpulkan ({H}{len(self.apc)}{N}) Id...")
                else:
                    if not error_occurred:
                        print(f"\n[!] Error saat memproses UID {xxx}")
                        error_occurred = True
            except:
                continue

        if not self.apc:
            print("\n[!] Tidak ada uid yang berhasil diambil.")
            retry = input("[?] Coba lagi (y/n): ").strip().lower()
            if retry == 'y':
                self.main()
            else:
                print("[!] Keluar dari program.")
                exit()
        else:
            muda = sorted(self.apc, reverse=True)
            self.asu.extend(muda)
            self.pilihan(tod)


    def pilihan(self, tod):
        print()
        if "api" in tod:
            apa = "[1] GRAPH V1\n[2] GRAPH V2"
        else:
            apa = "[1] VALIDATE V1\n[2] VALIDATE V2"

        while True:
            print()
            print(apa)
            inpt = input("\n[?] metode : ")
            print()
            if inpt in ["1", "01"]:
                if "api" in tod:
                    ykh = "graph_v1"
                else:
                    ykh = "valid_v1"
            elif inpt in ["2", "02"]:
                if "api" in tod:
                    ykh = "graph_v2"
                else:
                    ykh = "valid_v2"
            else:
                print(f"\n[!] pilih yang bener lah")
                time.sleep(1)
                continue
            Kynaa(self.asu, self.asw).abcd(ykh)