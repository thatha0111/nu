import requests, time, re, json, random, base64, sys

from .apcb import ABCD
from uuid import uuid4
first_time = False

acapona = requests.Session()

H = "\x1b[0;32m"  # Hijau
M = "\x1b[0;31m"  # Merah
N = "\x1b[0m"     # Reset ke default

class ABC:

    def __init__(self, cok, user):    
        self.url = "https://www.facebook.com"
        acapona.headers.update({'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7', 'accept-encoding': 'gzip, deflate', 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7', 'cache-control': 'max-age=0', 'dnt': '1', 'upgrade-insecure-requests': '1', 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36', 'viewport-width': '980'}); self.uname = "unknow"; self.uid = "unknown"
        acapona.headers.update({'dpr': '2.8125', 'sec-ch-prefers-color-scheme': 'light', 'sec-ch-ua': '"Android WebView";v="131", "Chromium";v="131", "Not_A Brand";v="24"', 'sec-ch-ua-full-version-list': '', 'sec-ch-ua-mobile': '?1', 'sec-ch-ua-model': '""', 'sec-ch-ua-platform': '"Android"', 'sec-ch-ua-platform-version': '""', 'sec-fetch-dest': 'document', 'sec-fetch-mode': 'navigate', 'sec-fetch-site': 'same-origin', 'sec-fetch-user': '?1'})
        self.c_user = user
        self.cok = {"cookie": cok}
        self.lop = 0

    def komen_fsnk(self):
        print("\n" + "-" * 50)
        print(">> Masukan kata kunci yang anda cari di fesnuk")
        print("-" * 50)
        my_kisah = ABCD(self.cok)
        sios, osjc = my_kisah.oalah_asu()
        if sios == True:
            query = input("  • Masukkan kata kunci pencarian: ").strip()
            while not query:
                query = input("  • Query tidak boleh kosong, silakan masukkan lagi: ").strip()
            print("\n  • Masukkan pesan (gunakan <> untuk baris baru)")
            comment_text = input("  • Teks komentar: ").replace("<>", "\n").strip()
            while not comment_text:
                comment_text = input("  • Komentar tidak boleh kosong, silakan masukkan lagi: ").replace("<>", "\n").strip()
            self.mulai(my_kisah, query, comment_text)
        else:exit("\n" + "-" * 50 + "\n" + osjc)

    def mulai(self,my_kisah, query, comment_text):
        gambar_setting = my_kisah.setting_gambar()
        if gambar_setting == "balik":
            self.mulai(query, comment_text)
            return
        else:
            etxh = self.search(query)
            self.gow_mari_eksekusi(etxh, comment_text, gambar_setting, my_kisah)

    def gow_mari_eksekusi(self, etxh, comment_text, gambar_setting, my):
        for i, users in enumerate(etxh, start=1):
            try:
                result = self.comment(users["post_id"], comment_text, gambar_setting, my)
            except Exception as e:
                print("\n")
                my.animasi_mengetik(f"\r {M}!{N} Kesalahan saat memproses komentar: {e}")
                continue
            except requests.exceptions.RequestException as e:
                print()
                my.koneksi_error()
            if result is None:
                print(f"\r {M}✗{N} Tidak ada hasil yang ditemukan.\n")
                continue
            if result["status"] == "succes":
                print(f"\r {H}✓{N} Berhasil mengomentari:\n   {result['url']}")
                self.lop+=1
            elif result["status"] == "fail":
                print(f"\r {M}✗{N} Gagal mengomentari:\n   {result['url']}")
                self.lop+=1
            else:
                print(f"\r {M}!{N} Error: Komentar mungkin dinonaktifkan\n   {result['url']}")
                self.lop+=1
            print("\r--------------------------------------------------")
            for detik in range(10, 0, -1):
                sys.stdout.write(f"\r {H}•{N} mulai post ke {H}{self.lop}{N}/{H}{len(etxh)}{N} posingan. delay:{H}{detik}{N}    ")
                sys.stdout.flush()
                time.sleep(1)
            sys.stdout.write("\r" + " " * 50)
            if i % 10 == 0:
                print(f"\n {H}•{N} Sudah {H}{i}{N} komentar. Menunggu jeda 3 menit...")
                for menit in range(3, 0, -1):
                    for detik in range(60, 0, -1):
                        sys.stdout.write(f"\r {H}•{N} Jeda: {H}{menit-1}:{detik:02d}{N}    ")
                        sys.stdout.flush()
                        time.sleep(1)
                sys.stdout.write("\r" + " " * 50 + "\r")
                print(f" {H}✓{N} Jeda selesai. Melanjutkan...")
                print("\r--------------------------------------------------")

        print("\n"+"=" * 50);my.my_kisah()
        my.animasi_mengetik(f"  {H}✓{N} Proses komentar selesai.")
        my.animasi_mengetik(f"  {H}•{N} Tekan Enter untuk melanjutkan...")
        print("=" * 50 + "\n")
        input()

    def search(self, query, gatau=0):
        list_post_id = []
        try:
            res = acapona.get(self.url + "/search/posts?q=" + query + "&filters=eyJyZWNlbnRfcG9zdHM6MCI6IntcIm5hbWVcIjpcInJlY2VudF9wb3N0c1wiLFwiYXJnc1wiOlwiXCJ9In0=", cookies=self.cok)
            self.data = {"__aaid": "0", "av": self.c_user, "__user": self.c_user, "__a": "1", "__req": "15", "__hs": re.search('"haste_session":"(.*?)"', res.text).group(1), "dpr": "3", "__ccg": random.choice(["GOOD", "EXCELLENT"]), "__rev": re.search('{"rev":(.*?)}', res.text).group(1), "__hsi": re.search('"hsi":"(.*?)",',res.text).group(1), "__comet_req": "15", "fb_dtsg":  re.search('"DTSGInitialData",\[\],{"token":"(.*?)"', res.text).group(1), "jazoest": re.search('&jazoest=(.*?)"', res.text).group(1), "lsd": re.search('"LSD",\[\],{"token":"(.*?)"', res.text).group(1), "__spin_r": re.search('"__spin_r":(.*?),', res.text).group(1), "__spin_b": "trunk", "__spin_t": re.search('"__spin_t":(.*?),', res.text).group(1)}; print()
            if (grepe := re.search('(\{"require":\[\["ScheduledServerJS","handle",null,\[\{"__bbox":\{"define":.*\["CometOnFBProfileVerificationBadge.react"\].*?)</script>', res.text)):
                to_json = json.loads(grepe.group(1))
                require = to_json["require"][0][3][0]["__bbox"]["require"]
                for xxx in require:
                    if "{\'has_next_page\': True, \'end_cursor\':" in str(xxx):
                        gatau = require.index(xxx); break
                if not gatau: exit()
                feedbackSource = int(re.search('"feedbackSource":(\d*),', res.text).group(1))
                results = require[gatau][3][1]["__bbox"]["result"]["data"]["serpResponse"]["results"]
                while True:
                    for user in results["edges"]:
                        rendering = user['rendering_strategy']['view_model']["click_model"]
                        content = rendering["story"]['comet_sections']["content"]["story"]
                        actors = content["actors"][0]
                        list_post_id.append({"id": actors["id"], "name": actors["name"], "post_id": content["post_id"]})
                        print(f"\r + Mengambil ({H}{len(list_post_id)}{N}) Postingan. (Ctrl+C untuk berhenti)", end="", flush=True)
                    if (page_info := results.get("page_info")):
                        if page_info["has_next_page"]:
                            res = acapona.post(
                                self.url + "/api/graphql/", 
                                data={**self.data,"fb_api_caller_class": "RelayModern", "fb_api_req_friendly_name": "SearchCometResultsPaginatedResultsQuery", "server_timestamps": "true", "doc_id": "8266858300080485", "variables": json.dumps({'allow_streaming': False, 'args': {'callsite': 'COMET_GLOBAL_SEARCH', 'config': {'exact_match': False, 'high_confidence_config': None, 'intercept_config': None, 'sts_disambiguation': None, 'watch_config': None}, 'context': {'bsid': rendering["logging_model"]["session_id"], 'tsid': None}, 'experience': {'client_defined_experiences': ['ADS_PARALLEL_FETCH'], 'encoded_server_defined_params': None, 'fbid': None, 'type': 'POSTS_TAB'}, 'filters': ["{\"name\":\"recent_posts\",\"args\":\"\"}"], 'text': query}, 'count': 10, 'cursor': page_info["end_cursor"], 'feedLocation': 'SEARCH', 'feedbackSource': feedbackSource, 'fetch_filters': True, 'focusCommentID': None, 'locale': None, 'privacySelectorRenderLocation': 'COMET_STREAM', 'renderLocation': 'search_results_page', 'scale': 3, 'stream_initial_count': 0, 'useDefaultActor': False, '__relay_internal__pv__GHLShouldChangeAdIdFieldNamerelayprovider': False, '__relay_internal__pv__GHLShouldChangeSponsoredDataFieldNamerelayprovider': False, '__relay_internal__pv__IsWorkUserrelayprovider': False, '__relay_internal__pv__CometFeedStoryDynamicResolutionPhotoAttachmentRenderer_experimentWidthrelayprovider': 500, '__relay_internal__pv__CometImmersivePhotoCanUserDisable3DMotionrelayprovider': False, '__relay_internal__pv__IsMergQAPollsrelayprovider': False, '__relay_internal__pv__FBReelsMediaFooter_comet_enable_reels_ads_gkrelayprovider': False, '__relay_internal__pv__CometUFIReactionsEnableShortNamerelayprovider': False, '__relay_internal__pv__CometUFIShareActionMigrationrelayprovider': True, '__relay_internal__pv__StoriesArmadilloReplyEnabledrelayprovider': True, '__relay_internal__pv__EventCometCardImage_prefetchEventImagerelayprovider': True})},
                                headers={**acapona.headers, "content-type": "application/x-www-form-urlencoded", "x-fb-lsd": self.data["lsd"], "x-asbd-id": "129477", "referer": self.url, "origin": "https://www.facebook.com", "x-fb-friendly-name": "SearchCometResultsPaginatedResultsQuery"},
								cookies=self.cok
                            )
                            if (serpResponse := re.search('(\{"data":\{"serpResponse":\{"results":\{"edges":.+\})', res.text)):
                                to_json = json.loads(serpResponse.group(1))
                                results = to_json["data"]["serpResponse"]["results"]
                                continue
                    break
            else:
                exit(" ! Gagal dump postingan")
        except KeyboardInterrupt:
            print()
        except Exception as e:
            print(e)
        except requests.exceptions.RequestException as e:
            print()
            ABCD("").koneksi_error()
        finally:
            if not list_post_id:
                exit(" ! Gagal dump postingan")
        print("-" * 50)
        print(f" * {H}{len(list_post_id)}{N} postingan terambil.")
        print("-" * 50)
        return list_post_id

    def comment(self, post_id, message, awok, kyna):
        res = acapona.get(self.url + "/" + post_id, cookies=self.cok)
        _timestamp = str(int(time.time()) * 1000)
        self.data = {"__aaid": "0", "av": self.c_user, "__user": self.c_user, "__a": "1", "__req": "15", "__hs": re.search('"haste_session":"(.*?)"', res.text).group(1), "dpr": "3", "__ccg": random.choice(["GOOD", "EXCELLENT"]), "__rev": re.search('{"rev":(.*?)}', res.text).group(1), "__hsi": re.search('"hsi":"(.*?)",',res.text).group(1), "__comet_req": "15", "fb_dtsg":  re.search('"DTSGInitialData",\[\],{"token":"(.*?)"', res.text).group(1), "jazoest": re.search('&jazoest=(.*?)"', res.text).group(1), "lsd": re.search('"LSD",\[\],{"token":"(.*?)"', res.text).group(1), "__spin_r": re.search('"__spin_r":(.*?),', res.text).group(1), "__spin_b": "trunk", "__spin_t": re.search('"__spin_t":(.*?),', res.text).group(1)}
        apcb = kyna.uploaded(self.c_user, self.data, awok)
        if not apcb:
            print(f"\r {M}✗{N} Anda memilih gak pake gambar.")
        else:
            print(f"\r {H}+{N} Gambar berhasil diupload.")
        if "/permalink/" in res.url:
            print(f"\r {H}+{N} postingan group terdeteksi")
            _variables = json.dumps({'feedLocation': 'GROUP_PERMALINK', 'feedbackSource': int(re.search('"feedbackSource":(\d*),', res.text).group(1)), 'groupID': None, 'input': {'client_mutation_id': '1', 'actor_id': self.c_user, 'attachments': apcb, 'feedback_id': base64.b64encode(bytes(f"feedback:{post_id}", "utf-8")).decode(), 'formatting_style': None, 'message': {'ranges': [], 'text': message}, 'attribution_id_v2': f'CometGroupPermalinkRoot.react,comet.group.permalink,via_cold_start,{_timestamp},273322,2361831622,,', 'vod_video_timestamp': None, 'is_tracking_encrypted': True, 'tracking': [re.search('"encrypted_tracking":"(.*?)"', res.text).group(1),"{\"assistant_caller\":\"comet_above_composer\",\"conversation_guide_session_id\":\"%s\",\"conversation_guide_shown\":null}" % (str(uuid4()))], 'feedback_source': 'OBJECT', 'idempotence_token': 'client:' + str(uuid4()), 'session_id': str(uuid4())}, 'inviteShortLinkKey': None, 'renderLocation': None, 'scale': 3, 'useDefaultActor': False, 'focusCommentID': None, '__relay_internal__pv__IsWorkUserrelayprovider': False})
        elif "/reel/" in res.url:
            print(f"\r {H}+{N} postingan reels terdeteksi")
            _variables = json.dumps({'feedLocation': 'COMET_MEDIA_VIEWER', 'feedbackSource': int(re.search('"feedbackSource":(\d*),', res.text).group(1)), 'groupID': None, 'input': {'client_mutation_id': '1', 'actor_id': self.c_user, 'attachments': apcb, 'feedback_id': base64.b64encode(bytes(f"feedback:{post_id}", "utf-8")).decode(), 'formatting_style': None, 'message': {'ranges': [], 'text': message}, 'attribution_id_v2': f'FBReelsRoot.react,comet.reels.home,via_cold_start,{_timestamp},211035,,,', 'vod_video_timestamp': None, 'is_tracking_encrypted': True, 'tracking': [json.dumps(eval(re.search(r'\{"creation_story":\{"tracking":"(\{.*?\\"tds_flgs\\":\d*})', res.text).group(1).replace('"', "'").replace("\\","")))], 'feedback_source': 'MEDIA_VIEWER', 'idempotence_token': 'client:' + str(uuid4()), 'session_id': str(uuid4()), 'downstream_share_session_id': str(uuid4()), 'downstream_share_session_origin_uri': res.url, 'downstream_share_session_start_time': _timestamp, 'inviteShortLinkKey': None, 'renderLocation': None, 'scale': 3, 'useDefaultActor': False, 'focusCommentID': None, '__relay_internal__pv__IsWorkUserrelayprovider': False}})
        elif "/watch/" in res.url:
            print(f"\r {H}+{N} postingan video terdeteksi")
            _variables = json.dumps({'feedLocation': 'TAHOE', 'feedbackSource': int(re.search('"feedbackSource":(\d*),', res.text).group(1)), 'groupID': None, 'input': {'client_mutation_id': '1', 'actor_id': self.c_user, 'attachments': apcb, 'feedback_id': base64.b64encode(bytes(f"feedback:{post_id}", "utf-8")).decode(), 'formatting_style': None, 'message': {'ranges': [], 'text': message}, 'attribution_id_v2': f'CometVideoHomeNewPermalinkRoot.react,comet.watch.injection,via_cold_start,{_timestamp},977192,2392950137,,', 'vod_video_timestamp': None, 'is_tracking_encrypted': True, 'tracking': ["{\"assistant_caller\":\"comet_above_composer\",\"conversation_guide_session_id\":null,\"conversation_guide_shown\":null}"], 'feedback_source': 'TAHOE', 'idempotence_token': 'client:' + str(uuid4()), 'session_id': str(uuid4()), 'downstream_share_session_id': str(uuid4()), 'downstream_share_session_origin_uri': res.url, 'downstream_share_session_start_time': _timestamp, 'inviteShortLinkKey': None, 'renderLocation': None, 'scale': 3, 'useDefaultActor': False, 'focusCommentID': None, '__relay_internal__pv__IsWorkUserrelayprovider': False}})
        elif "/posts/" in res.url:
            print(f"\r {H}+{N} postingan biasa terdeteksi")
            _variables = json.dumps({'feedLocation': 'PERMALINK', 'feedbackSource': int(re.search('"feedbackSource":(\d*),', res.text).group(1)), 'groupID': None, 'input': {'client_mutation_id': '1', 'actor_id': self.c_user, 'attachments': apcb, 'feedback_id': base64.b64encode(bytes(f"feedback:{post_id}", "utf-8")).decode(), 'formatting_style': None, 'message': {'ranges': [], 'text': message}, 'attribution_id_v2': f'CometSinglePostDialogRoot.react,comet.post.single_dialog,via_cold_start,{_timestamp},462741,,,', 'vod_video_timestamp': None, 'is_tracking_encrypted': True, 'tracking': ["{\"assistant_caller\":\"comet_above_composer\",\"conversation_guide_session_id\":\"%s\",\"conversation_guide_shown\":null}" % (str(uuid4()))], 'feedback_source': 'OBJECT', 'idempotence_token': 'client:' + str(uuid4()), 'session_id': str(uuid4()), 'downstream_share_session_id': str(uuid4()), 'downstream_share_session_origin_uri': res.url, 'downstream_share_session_start_time': _timestamp}, 'inviteShortLinkKey': None, 'renderLocation': None, 'scale': 3, 'useDefaultActor': False, 'focusCommentID': None, '__relay_internal__pv__IsWorkUserrelayprovider': False})
        else:
            return {"status": "unknown", "id": post_id, "url": res.url}
        if re.search('"attachments": \[.*?\],', _variables):
            res2 = acapona.post(self.url + "/api/graphql/", data={**self.data, "fb_api_caller_class": "RelayModern", "fb_api_req_friendly_name": "useCometUFICreateCommentMutation", "server_timestamps": "true", "doc_id": "8976690469034029",
            "variables": _variables},
            headers={**acapona.headers, "content-type": "application/x-www-form-urlencoded", "x-fb-lsd": self.data["lsd"], "x-asbd-id": "129477", "referer": self.url, "origin": "https://www.facebook.com", "x-fb-friendly-name": "useCometUFICreateCommentMutation"},
            cookies=self.cok)
            if "Anda Tidak Dapat Berkomentar Saat Ini" in res2.text:
                print("\n")
                kyna.animasi_mengetik(f" {M}✗{N} Anda Tidak Dapat Berkomentar Saat Ini")
                kyna.animasi_mengetik(f" {M}>{N} Beberapa komentar Anda sebelumnya tidak mematuhi Standar Komunitas kami tentang spam. Anda bisa mencoba lagi nanti.");exit()
        if '"comment_create":null' in res2.text:
            return {"status": "fail", "id": post_id, "url": res.url}

        return {"status": "succes", "id": post_id, "url": res.url}