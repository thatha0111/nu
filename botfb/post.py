import requests, re, time, json, sys

from rich.console import Console
from rich.panel import Panel
from .apcb import ABCD

console = Console()

K = "\x1b[0;33m"  # Kuning
M = "\x1b[0;31m"  # Merah
H = "\x1b[0;32m"  # Hijau
C = "\x1b[0;36m"  # Cyan
O = "\x1b[0m"     # Reset ke default

class ASU:

    def __init__(self, cok, usr):
        self.cok = {"cookie": cok}
        self.usr, self.lop = usr,0 
        self.grp, self.asu = [], []
        self.url = "https://www.facebook.com"

        # KELUAR DARI GRUP MENGGUNAKAN ID
        self.id_grup = [
            "1254052852418843",
            #"815140854023400",
            #"447580913460211",
            #"116407765651331",
        ]

    def postt_grup(self):
        asu = ABCD(self.cok)
        while True:
            gmb = asu.setting_gambar()
            if gmb == "balik":
                continue
            else:
                tdk, psn = self.setting_pesan(asu)
                break
        self.dump_grup()
        self.apcb(tdk, psn, gmb)

    def apcb(self, abcd, efgh, awok):
        print("\n" + "-" * 50)
        print(">> sedang proses posting ke grup")
        print("-" * 50)
        for i in self.grp:
            #self.chek(i["id"], i["name"], abcd, efgh, awok)
            self.post(i["id"], i["name"], abcd, efgh, awok)
        print("\n" + "=" * 50)
        efgh.my_kisah()
        efgh.animasi_mengetik(f"  {H}✓{O} berhasil posting kesemua grup.")
        efgh.animasi_mengetik(f"  {H}•{O} Tekan Enter untuk melanjutkan...")
        print("=" * 50 + "\n")
        input()

    def setting_pesan(self, katz):
        while True:
            peringatan_text = (
                "ketik '[bold yellow]Pesan[/]'  gunakan pesan sendiri\n"
                "ketik '[bold yellow]Post[/]'   jika ingin menghapus post\n"
                "tekan '[bold yellow]Enter[/]'  gunakan Pesan bawaan script\n"
            )
            panel_peringatan = Panel(
                peringatan_text,
                title="[bold red]Program untuk Membuat Pesan[/bold red]",
                width=50,
                height=5
            )
            console.print(panel_peringatan)
            pilihan = input("\nTindakan (Pesan/Post/Enter): ").strip().lower()
            sios, osjc = katz.oalah_asu()
            if pilihan == "pesan":
                if sios:
                    print("-" * 50)
                    print(" * Masukkan pesan (gunakan <> untuk baris baru)")
                    self.pesan = input(" * pesan: ").replace("<>", "\n").strip()
                    while not self.pesan:
                        self.pesan = input("\n ! Pesan tidak boleh kosong. Silakan coba lagi.\n * pesan: ").replace("<>", "\n").strip()
                    print("\n" + "-" * 50)
                    print(" > Anda menggunakan pesan yang telah di setting.")
                    print("-" * 50)
                    return "pake", katz
                else:
                    exit("\n" + "-" * 50 + "\n" + osjc)
            elif pilihan in ["", "enter"]:
                if sios:
                    katz.main()
                    print("-" * 50)
                    print(" > Anda menggunakan pesan bawaan script.")
                    print("-" * 50)
                    return "kgak", katz
                else:
                    exit("\n" + "-" * 50 + "\n" + osjc)
            elif pilihan in ["post", "post"]:
                if sios:
                    self.apacoba()
                    break
                else:
                    exit("\n" + "-" * 50 + "\n" + osjc)
            else:
                print("\n ! pilih yang bener lah!")
                print("-" * 50)
                time.sleep(1)
                continue

    def apacoba(self):
        self.dump_grup()
        print("\n" + "-" *50)
        print(" * PROSES POSTINGAN YANG MENUNGGU PERSETUJUAN")
        print("-" *50)
        for z in self.grp:
            self.hapus(z["id"], z["name"], "my_pending_content")
        print("-" *50)
        print(" * PROSES POSTINGAN YANG TELAH DI HAPUS")
        print("-" *50)
        for z in self.grp:
            self.hapus(z["id"], z["name"], "my_removed_content")
        print("-" *50)
        print(" * PROSES POSTINGAN YANG TELAH DI TOLAK")
        print("-" *50)
        for z in self.grp:
            self.hapus(z["id"], z["name"], "my_declined_content")
        exit(f" {H}√{O} berhasil menghapus postingan.")

    def dump_grup(self):
        list_grup_fesnuk = []
        try:
            acapona = requests.Session()
            acapona.headers.update({'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7', 'accept-encoding': 'gzip, deflate', 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7', 'cache-control': 'max-age=0', 'dnt': '1', 'dpr': '2.8125', 'sec-ch-prefers-color-scheme': 'light', 'sec-ch-ua': '"Android WebView";v="131", "Chromium";v="131", "Not_A Brand";v="24"', 'sec-ch-ua-full-version-list': '', 'sec-ch-ua-mobile': '?1', 'sec-ch-ua-model': '""', 'sec-ch-ua-platform': '"Android"', 'sec-ch-ua-platform-version': '""', 'sec-fetch-dest': 'document', 'sec-fetch-mode': 'navigate', 'sec-fetch-site': 'same-origin', 'sec-fetch-user': '?1', 'upgrade-insecure-requests': '1', 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36', 'viewport-width': '980'})
            res = acapona.get(self.url + "/groups/feed/", cookies=self.cok)
            try:
                intinya_adalah_data = {"server_timestamps": "true", "doc_id": "9822178014474235", "fb_api_caller_class": "RelayModern", "fb_api_req_friendly_name": "GroupsLeftRailYourGroupsPaginatedQuery", '__aaid': '0', 'av': self.usr, '__user': self.usr, '__a': '1', '__req': '15', '__hs': re.search('"haste_session":"(.*?)"', res.text).group(1), 'dpr': '3', '__ccg': 'GOOD', '__rev': re.search('{"rev":(.*?)}', res.text).group(1), '__hsi': re.search('"hsi":"(.*?)",',res.text).group(1), '__comet_req': '15', 'fb_dtsg':  re.search('"DTSGInitialData",\[\],{"token":"(.*?)"', res.text).group(1), 'jazoest': re.search('&jazoest=(.*?)"', res.text).group(1), 'lsd': re.search('"LSD",\[\],{"token":"(.*?)"', res.text).group(1), '__spin_r': re.search('"__spin_r":(.*?),', res.text).group(1), '__spin_b': 'trunk', '__spin_t': re.search('"__spin_t":(.*?),', res.text).group(1)}
            except AttributeError:
                pass

            acapona.headers.update({"content-type": "application/x-www-form-urlencoded", "x-fb-lsd": intinya_adalah_data["lsd"], "x-asbd-id": "129477", "referer": "https://www.facebook.com/groups/feed/", "origin": "https://www.facebook.com", "x-fb-friendly-name": "GroupsLeftRailYourGroupsPaginatedQuery"})
            if (jsondata := re.search('(\{"require":\[\["ScheduledServerJS","handle",.+,\[\{"__bbox":\{"require":\[\["RelayPrefetchedStreamCache","next",\[\],\["adp_GroupsCometLeftRailContainerQueryRelayPreloader.*?)</script>', res.text)):
                abcoda = json.loads(jsondata.group(1))
                ofkors = abcoda["require"][0][3][0]["__bbox"]["require"][0][3][1]["__bbox"]["result"]["data"]["nonAdminGroups"]["groups_tab"]["tab_groups_list"]
                while True:
                    for i in ofkors["edges"]:
                        list_grup_fesnuk.append({"id": i["node"]["id"], "name": i["node"]["name"]})
                        print(f"\r + Mengambil ({H}{len(list_grup_fesnuk)}{O}) ID Grup. (Ctrl+C untuk berhenti)", end="", flush=True)
                    if (sure := ofkors.get("page_info")):
                         if not sure["has_next_page"]:
                             break
                         intinya_adalah_data["variables"] = json.dumps({'count': 10, 'cursor': sure["end_cursor"], 'listType': 'NON_ADMIN_MODERATOR_GROUPS', 'scale': 3})
                         res = acapona.post(self.url + "/api/graphql/", data=intinya_adalah_data, cookies=self.cok)
                         try:
                             magnum = json.loads(res.text)
                         except Exception as o:
                             print(o)
                             break
                         ofkors = magnum["data"]["viewer"]["groups_tab"]["tab_groups_list"]
                         continue
                    break
            else:
                exit(" ! gagal dump grup")
        except KeyboardInterrupt:
            print()
        except Exception as e:
            print(e)
        except requests.exceptions.RequestException as e:
            print()
            ABCD("").koneksi_error()
        finally:
            if not list_grup_fesnuk:
                exit(" ! gagal dump grup")
            self.grp = list_grup_fesnuk

    def chek(self, yxzz, name, ktss, kyna, yxz88):
        if yxzz in self.id_grup:
            kyna.keluar_grup(yxzz, self.usr)
            print(f"\r {H}+{O} berhasil keluar group {M}{name}{O}")
            print(f"   URL: {self.url}/groups/{yxzz}")
            print("\r--------------------------------------------------")
            self.lop+=1
        else:
            self.post(yxzz, name, ktss, kyna, yxz88)

    def post(self, yxzz, name, ktss, kyna, yxz88):
        for detik in range(63, 0, -1):
            sys.stdout.write(f"\r {H}•{O} mulai post ke {H}{str(self.lop)}{O}/{H}{len(self.grp)}{O} grup. delay:{H}{detik}{O}    ")
            sys.stdout.flush()
            time.sleep(1)
        sys.stdout.write("\r" + " " * 50)
        try:
            aocb = requests.Session()
            if ktss == "pake":apa = self.pesan
            else:apa = kyna.katz_default()
            nama, user, kata = name, yxzz, apa
            aocb.headers.update({'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7', 'accept-encoding': 'gzip, deflate', 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7', 'cache-control': 'max-age=0', 'dnt': '1', 'dpr': '2.8125', 'sec-ch-prefers-color-scheme': 'light', 'sec-ch-ua': '"Android WebView";v="131", "Chromium";v="131", "Not_A Brand";v="24"', 'sec-ch-ua-full-version-list': '', 'sec-ch-ua-mobile': '?1', 'sec-ch-ua-model': '""', 'sec-ch-ua-platform': '"Android"', 'sec-ch-ua-platform-version': '""', 'sec-fetch-dest': 'document', 'sec-fetch-mode': 'navigate', 'sec-fetch-site': 'same-origin', 'sec-fetch-user': '?1', 'upgrade-insecure-requests': '1', 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36', 'viewport-width': '980'})
            res = aocb.get(self.url + "/groups/" + user, cookies=self.cok, timeout=10)
            data_also_params = {'__aaid': '0', 'av': self.usr, '__user': self.usr, '__a': '1', '__req': '15', '__hs': re.search('"haste_session":"(.*?)"', res.text).group(1), 'dpr': '3', '__ccg': 'GOOD', '__rev': re.search('{"rev":(.*?)}', res.text).group(1), '__hsi': re.search('"hsi":"(.*?)",',res.text).group(1), '__comet_req': '15', 'fb_dtsg':  re.search('"DTSGInitialData",\[\],{"token":"(.*?)"', res.text).group(1), 'jazoest': re.search('&jazoest=(.*?)"', res.text).group(1), 'lsd': re.search('"LSD",\[\],{"token":"(.*?)"', res.text).group(1), '__spin_r': re.search('"__spin_r":(.*?),', res.text).group(1), '__spin_b': 'trunk', '__spin_t': re.search('"__spin_t":(.*?),', res.text).group(1)}
            aocb.headers.update({"origin": "https://www.facebook.com", "referer": "https://www.facebook.com/"})
            foto = kyna.foto_post(data_also_params, aocb, self.usr, yxz88)
            if "gakpake" in foto:
                dataz = {"fb_api_caller_class": "RelayModern", "fb_api_req_friendly_name": "ComposerStoryCreateMutation", "server_timestamps": "true", "doc_id": "9811110625572785", "variables": json.dumps({'input': {'composer_entry_point': 'inline_composer', 'composer_source_surface': 'group', 'composer_type': 'group', 'logging': {'composer_session_id': __import__("uuid").uuid4().__str__()}, 'source': 'WWW', 'message': {'ranges': [], 'text': kata}, 'with_tags_ids': None, 'inline_activities': [], 'text_format_preset_id': '0', 'navigation_data': {'attribution_id_v2': f'CometGroupDiscussionRoot.react,comet.group,via_cold_start,{user},896883,2361831622,,'}, 'tracking': [None], 'event_share_metadata': {'surface': 'newsfeed'}, 'audience': {'to_id': user}, 'actor_id': self.usr, 'client_mutation_id': '1'}, 'feedLocation': 'GROUP', 'feedbackSource': 0, 'focusCommentID': None, 'gridMediaWidth': None, 'groupID': None, 'scale': 3, 'privacySelectorRenderLocation': 'COMET_STREAM', 'checkPhotosToReelsUpsellEligibility': False, 'renderLocation': 'group', 'useDefaultActor': False, 'inviteShortLinkKey': None, 'isFeed': False, 'isFundraiser': False, 'isFunFactPost': False, 'isGroup': True, 'isEvent': False, 'isTimeline': False, 'isSocialLearning': False, 'isPageNewsFeed': False, 'isProfileReviews': False, 'isWorkSharedDraft': False, 'hashtag': None, 'canUserManageOffers': False, '__relay_internal__pv__CometUFIShareActionMigrationrelayprovider': True, '__relay_internal__pv__GHLShouldChangeSponsoredDataFieldNamerelayprovider': True, '__relay_internal__pv__GHLShouldChangeAdIdFieldNamerelayprovider': False, '__relay_internal__pv__IsWorkUserrelayprovider': False, '__relay_internal__pv__CometUFIReactionsEnableShortNamerelayprovider': False, '__relay_internal__pv__CometFeedStoryDynamicResolutionPhotoAttachmentRenderer_experimentWidthrelayprovider': 500, '__relay_internal__pv__CometImmersivePhotoCanUserDisable3DMotionrelayprovider': False, '__relay_internal__pv__IsMergQAPollsrelayprovider': False, '__relay_internal__pv__FBReelsMediaFooter_comet_enable_reels_ads_gkrelayprovider': False, '__relay_internal__pv__StoriesArmadilloReplyEnabledrelayprovider': True, '__relay_internal__pv__EventCometCardImage_prefetchEventImagerelayprovider': True, '__relay_internal__pv__GHLShouldChangeSponsoredAuctionDistanceFieldNamerelayprovider': False})}
            else:
                dataz = {"fb_api_caller_class": "RelayModern", "fb_api_req_friendly_name": "ComposerStoryCreateMutation", "server_timestamps": "true", "doc_id": "9811110625572785", "variables": json.dumps({'input': {'composer_entry_point': 'inline_composer', 'composer_source_surface': 'group', 'composer_type': 'group', 'logging': {'composer_session_id': __import__("uuid").uuid4().__str__()}, 'source': 'WWW', 'message': {'ranges': [], 'text': kata}, 'with_tags_ids': None, 'inline_activities': [], 'text_format_preset_id': '0', 'attachments': [{'photo': {'id': foto}}], 'navigation_data': {'attribution_id_v2': f'CometGroupDiscussionRoot.react,comet.group,via_cold_start,{user},896883,2361831622,,'}, 'tracking': [None], 'event_share_metadata': {'surface': 'newsfeed'}, 'audience': {'to_id': user}, 'actor_id': self.usr, 'client_mutation_id': '1'}, 'feedLocation': 'GROUP', 'feedbackSource': 0, 'focusCommentID': None, 'gridMediaWidth': None, 'groupID': None, 'scale': 3, 'privacySelectorRenderLocation': 'COMET_STREAM', 'checkPhotosToReelsUpsellEligibility': False, 'renderLocation': 'group', 'useDefaultActor': False, 'inviteShortLinkKey': None, 'isFeed': False, 'isFundraiser': False, 'isFunFactPost': False, 'isGroup': True, 'isEvent': False, 'isTimeline': False, 'isSocialLearning': False, 'isPageNewsFeed': False, 'isProfileReviews': False, 'isWorkSharedDraft': False, 'hashtag': None, 'canUserManageOffers': False, '__relay_internal__pv__CometUFIShareActionMigrationrelayprovider': True, '__relay_internal__pv__GHLShouldChangeSponsoredDataFieldNamerelayprovider': True, '__relay_internal__pv__GHLShouldChangeAdIdFieldNamerelayprovider': False, '__relay_internal__pv__IsWorkUserrelayprovider': False, '__relay_internal__pv__CometUFIReactionsEnableShortNamerelayprovider': False, '__relay_internal__pv__CometFeedStoryDynamicResolutionPhotoAttachmentRenderer_experimentWidthrelayprovider': 500, '__relay_internal__pv__CometImmersivePhotoCanUserDisable3DMotionrelayprovider': False, '__relay_internal__pv__IsMergQAPollsrelayprovider': False, '__relay_internal__pv__FBReelsMediaFooter_comet_enable_reels_ads_gkrelayprovider': False, '__relay_internal__pv__StoriesArmadilloReplyEnabledrelayprovider': True, '__relay_internal__pv__EventCometCardImage_prefetchEventImagerelayprovider': True, '__relay_internal__pv__GHLShouldChangeSponsoredAuctionDistanceFieldNamerelayprovider': False})}
            aocb.headers.update({"content-type": "application/x-www-form-urlencoded", "x-fb-lsd": data_also_params["lsd"], "x-asbd-id": "129477", "x-fb-friendly-name": "ComposerStoryCreateMutation"})
            payload = {**data_also_params, **dataz}
            res3 = aocb.post(
                self.url + "/api/graphql/",
                data=payload,
                cookies=self.cok
            )
            if "Maaf, fitur ini tidak tersedia untuk saat ini" in res3.text:
                print("\n")
                kyna.animasi_mengetik(f" {M}✗{O} akun terkena spam")
                kyna.animasi_mengetik(f" {M}>{O} Ada masalah saat memproses permintaan ini. Coba lagi nanti.");exit()
            elif "Anda Tidak Dapat Menggunakan Fitur Ini Sekarang" in res3.text:
                print("\n")
                kyna.animasi_mengetik(f" {M}✗{O} akun terkena spam")
                kyna.animasi_mengetik(f" {M}>{O} Kami membatasi seberapa sering Anda dapat memposting, berkomentar, atau melakukan hal-hal lain dalam jumlah waktu tertentu guna membantu melindungi komunitas dari spam. Anda bisa mencoba lagi nanti.");exit()
            elif "Anda telah diblokir sementara untuk melakukan tindakan ini." in res3.text:
                print("\n")
                kyna.animasi_mengetik(f" {M}✗{O} akun terkena spam")
                kyna.animasi_mengetik(f" {M}>{O} Kami membatasi seberapa sering Anda dapat memposting, berkomentar, atau melakukan hal-hal lain dalam jumlah waktu tertentu guna membantu melindungi komunitas dari spam. Anda bisa mencoba lagi nanti.");exit()
            elif (postid := re.search(r'"publish_time\\":\d*,\\"story_name\\":\\"EntGroupMallPostCreationStory\\",\\"story_fbid\\":\[\\"(\d*)\\"\]', res3.text)):
                print(f"\r {H}+{O} berhasil memposting ke group {H}{nama}{O}")
                print(f"   URL: {self.url}/groups/{user}/{postid.group(1)}")
                print("\r--------------------------------------------------")
            else:
                print(f"\r {M}!{O} gagal memposting ke group {M}{nama}{O}")
                print("\r--------------------------------------------------")
        except requests.exceptions.RequestException as e:
            print()
            kyna.koneksi_error()
        except Exception as e:
            print("\n")
            kyna.animasi_mengetik(f" {M}!{O} Kesalahan saat memproses postingan: {e}");exit()

        self.lop+=1

    def hapus(self, mmk, nma, apc):
        cihuy = 0
        try:
            print(f" - proses cek postingan grup {K}{nma}{O}")
            ses = requests.Session()
            ses.headers.update({'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7', 'accept-encoding': 'gzip, deflate', 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7', 'cache-control': 'max-age=0', 'dnt': '1', 'dpr': '2.8125', 'sec-ch-prefers-color-scheme': 'light', 'sec-ch-ua': '"Android WebView";v="131", "Chromium";v="131", "Not_A Brand";v="24"', 'sec-ch-ua-full-version-list': '', 'sec-ch-ua-mobile': '?1', 'sec-ch-ua-model': '""', 'sec-ch-ua-platform': '"Android"', 'sec-ch-ua-platform-version': '""', 'sec-fetch-dest': 'document', 'sec-fetch-mode': 'navigate', 'sec-fetch-site': 'same-origin', 'sec-fetch-user': '?1', 'upgrade-insecure-requests': '1', 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36', 'viewport-width': '980'})
            res = ses.get(f"{self.url}/groups/{mmk}/{apc}", cookies=self.cok, timeout=10)
            if "Page not found" in res.text:
                exit("\n\n ! Cookie ter logout.")
            else:
                pos = re.findall('"story":{"id":"(.*?)"', res.text)
                if not pos:
                    print(" ! Tidak ada postingan yang ditemukan.", end="\r")
                    time.sleep(1)
                    print(" " * 50, end="\r")
                    return
                for car in pos:
                    cihuy += 1
                    data_also_params = {'__aaid': '0', 'av': self.usr, '__user': self.usr, '__a': '1', '__req': '15', '__hs': re.search('"haste_session":"(.*?)"', res.text).group(1), 'dpr': '3', '__ccg': 'GOOD', '__rev': re.search('{"rev":(.*?)}', res.text).group(1), '__hsi': re.search('"hsi":"(.*?)",',res.text).group(1), '__comet_req': '15', 'fb_dtsg':  re.search('"DTSGInitialData",\[\],{"token":"(.*?)"', res.text).group(1), 'jazoest': re.search('&jazoest=(.*?)"', res.text).group(1), 'lsd': re.search('"LSD",\[\],{"token":"(.*?)"', res.text).group(1), '__spin_r': re.search('"__spin_r":(.*?),', res.text).group(1), '__spin_b': 'trunk', '__spin_t': re.search('"__spin_t":(.*?),', res.text).group(1)}
                    data_also_params.update({
                        'fb_api_caller_class': 'RelayModern',
                        'fb_api_req_friendly_name': 'useCometFeedStoryDeleteMutation',
                        'variables': json.dumps({"input":{"story_id":car,"story_location":"GROUP","actor_id":self.usr,"client_mutation_id":"2"},"groupID":None,"inviteShortLinkKey":None,"renderLocation":None,"scale":1}),
                        'server_timestamps': 'true',
                        'doc_id': '9052705268176005',
                    })
                    ses.headers.update({"content-type": "application/x-www-form-urlencoded", "x-fb-lsd": data_also_params["lsd"], "x-asbd-id": "129477", "x-fb-friendly-name": "useCometFeedStoryDeleteMutation"})
                    try:
                        response = ses.post(self.url + "/api/graphql/", cookies=self.cok, data=data_also_params, timeout=10)
                        if response.status_code == 200:
                            print(f" + Postingan ke {C}{cihuy}{O} berhasil dihapus", end="\r")
                        else:
                            print(f" - Gagal menghapus postingan {cihuy}: {response.status_code} {response.text}", end="\r")
                    except requests.exceptions.RequestException as e:
                        print()
                        ABCD("").koneksi_error()
                    time.sleep(2)
        except requests.exceptions.RequestException as e:
            print()
            ABCD("").koneksi_error()
        except Exception as e:
            print("\n")
            exit(f" {M}!{O} Kesalahan saat memproses postingan: {e}\n")