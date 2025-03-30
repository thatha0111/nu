import os, re, requests, json, time
from .logo import Logo
from yxdfb.Fesnuk import Wangsaff
from yxdig.kyna import Insta
from botfb.kyna import Main

M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
N = '\x1b[0m'     # WARNA MATI
R = "\x1b[0;31m"  # Merah

class yayanxd:

    def __init__(self):
        self.paket = {
            "nama": "Premium User",
            "expired": "Lifetime",
            "readtext": "Unlimited",
            "paket": ["sc ig", "sc fb", "bot fb", "bot ig"]
        }
        self.lim = f"{H}Premium License{N}"

    def cekin(self):
        yxz = "Premium License"
        asu = (
            f"""
        Hello {H}{self.paket["nama"]}!{N}, Anda adalah pengguna {H}Premium{N}.
  Lisensi Anda aktif secara permanen ({H}Lifetime Access{N})
    Gunakan tools ini dengan bijak dan manfaatkan sebaik mungkin! 
            """
        )
        sc_crk_ig = sc_crk_fb = sc_bot_fb = sc_bot_ig = f"[{H}Active{N}]"
        return sc_crk_ig, sc_crk_fb, sc_bot_fb, sc_bot_ig, yxz, asu

    def hapus(self):
        os.system("git pull")
        Logo("barme")
        patch = [
            "botfb/data/apcb.txt",
            "data/HASIL-CEK-CP/CP/apcb.txt", "data/HASIL-CEK-CP/OK/apcb.txt", 
            "data/HASIL-CEK-CP/json/apcb.txt", "data/result/OK/apcb.txt", 
            "data/result/CP/apcb.txt", "data/results/OK/apcb.txt", 
            "data/results/CP/apcb.txt",
        ]
        for file in patch:
            if os.path.exists(file):
                try: os.remove(file)
                except: pass

    def remove_ansi(self, text):
        ansi_escape = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')
        return ansi_escape.sub('', text)

    def menu(self):
        sc_crk_ig, sc_crk_fb, sc_bot_fb, sc_bot_ig, lim, asw = self.cekin()
        while True:
            Logo("barme")
            m2k = "     Selamat menikmati semua fitur premium secara gratis! "
            print(asw)
            print(
        f"""{m2k}
  01. Start Crack FB {sc_crk_fb}
  02. Start Crack IG {sc_crk_ig}
  03. Start Bot Fesnuk {sc_bot_fb}
""")
            asu = input(" >> ")
            if asu in ["1", "01"]:
                self.save_to_json("data/cache/.ua_fb.json", "https://pastebin.com/raw/69wptz3D")
                Wangsaff(lim, asw)
            elif asu in ["2", "02"]:
                self.save_to_json("data/cache/.ua_ig.json", "https://pastebin.com/raw/dgRettD3")
                Insta(lim, asw).menu()
            elif asu in ["3", "03"]:
                Main(lim, asw).main_menu()
            else:
                print(f"\n  [{M}!{N}] Pilih menu yang valid")
                time.sleep(1)
                self.menu()

    def save_to_json(self, filename, remote_url):
        try:
            headers = {'User-Agent': 'Mozilla/5.0'}
            response = requests.get(remote_url, headers=headers)
            response.raise_for_status()
            new_data = response.json()
        except:
            new_data = []

        with open(filename, "w", encoding="utf-8") as f:
            json.dump(new_data, f, indent=2, ensure_ascii=False)