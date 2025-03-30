import requests, random, re, time, json, os
from bs4 import BeautifulSoup

H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
N = '\x1b[0m'	 # WARNA MATI

class Yntks:

    def __init__(self, asw, uas):
        self.asw = asw
        self.uas = uas
        self.dump_brand_dan_model = []


    def get_model(self, url):
        try:
            headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
            full_url = "https://www.gsmarena.com/" + url
            
            response = requests.get(full_url, headers=headers)
            soup = BeautifulSoup(response.text, 'html.parser')
            next_page = soup.find('a', class_='prevnextbutton', title='Next page')

            operators = ["Telkomsel", "XL", "Indosat", "Smartfren", "Tri"]
            random.shuffle(operators)

            for idx, item in enumerate(soup.select("div.makers > ul > li")):
                model_span = item.find('span')
                model_name = model_span.text.strip() if model_span else item.text.strip()
                
                model_url = item.find('a')['href']
                model_full_url = f"https://www.gsmarena.com/{model_url}"
                time.sleep(1)

                detail_response = requests.get(model_full_url, headers=headers)
                detail_soup = BeautifulSoup(detail_response.text, 'html.parser')

                os_tag = detail_soup.find('td', {'data-spec': 'os'})
                android_version = "13"
                if os_tag:
                    os_text = os_tag.text.strip()
                    
                    android_match = re.search(r'Android\s([0-9]+)', os_text)
                    if android_match:
                        major_version = android_match.group(1)
                        android_version = f"{major_version}"
                    else:
                        android_version = random.choice(["13", "14", "12"])

                models_tag = detail_soup.find('td', {'data-spec': 'models'})
                official_model = models_tag.text.split(',')[0].strip() if models_tag else self.generate_model_number(url)

                resolution_tag = detail_soup.find('td', {'data-spec': 'displayresolution'})
                if resolution_tag:
                    resolution_text = resolution_tag.text
                    res_match = re.search(r'(\d+)\s*x\s*(\d+).*?~(\d+)\s*ppi', resolution_text)
                    if res_match:
                        width, height, ppi = res_match.groups()
                    else:
                        width, height, ppi = 1080, 1920, 320
                else:
                    width, height, ppi = 1080, 1920, 320

                chipset_tag = detail_soup.find('td', {'data-spec': 'chipset'})
                chipset = self.format_chipset(chipset_tag.text) if chipset_tag else "unknown"

                brand = (
                    "Samsung" if "samsung" in url.lower() else "Xiaomi" if "xiaomi" in url.lower() else
                    "Tecno" if "tecno" in url.lower() else
                    "Vivo" if "vivo" in url.lower() else
                    "Itel" if "itel" in url.lower() else
                    "Google" if "google" in url.lower() else "Oppo" if "oppo" in url.lower() else
                    "OnePlus" if "oneplus" in url.lower() else "Nothing" if "nothing" in url.lower() else \
                    "Meizu" if "meizu" in url.lower() else "Apple" if "apple" in url.lower() else \
                    "Honor" if "honor" in url.lower() else "Asus" if "asus" in url.lower() else \
                    "Huawei" if "huawei" in url.lower() else "Nokia" if "nokia" in url.lower() else \
                    "Realme" if "realme" in url.lower() else "Alcatel" if "alcatel" in url.lower() else \
                    "LG" if "lg" in url.lower() else "Lenovo" if "lenovo" in url.lower() else \
                    "Microsoft" if "microsoft" in url.lower() else "Umidigi" if "umidigi" in url.lower() else \
                    "Sony" if "sony" in url.lower() else "HTC" if "htc" in url.lower() else \
                    "Motorola" if "motorola" in url.lower() else "Coolpad" if "coolpad" in url.lower() else \
                    "Sharp" if "sharp" in url.lower() else "Doogee" if "doogee" in url.lower() else \
                    "Micromax" if "micromax" in url.lower() else "Blackview" if "blackview" in url.lower() else \
                    "TCL" if "tcl" in url.lower() else "Cubot" if "cubot" in url.lower() else \
                    "Ulefone" if "ulefone" in url.lower() else "Oukitel" if "oukitel" in url.lower() else \
                    "Cat" if "cat" in url.lower() else "Unknown"
                )

                data = {
                    "brand": brand,
                    "device": model_name,
                    "model": official_model,
                    "width": width,
                    "height": height,
                    "density": self.calculate_density(int(ppi)),
                    "operators": random.choice(operators),
                    "model_chipset": chipset,
                    "android_version": android_version

                }
                self.dump_brand_dan_model.append(data)
                self.save_to_json()

                print(f"\r[{H}+{N}] Mengambil ({H}{len(self.dump_brand_dan_model)}{N}) model. (Ctrl+C untuk berhenti)", end="", flush=True)

            if next_page:
                self.get_model(next_page['href'])

        except Exception as e:
            print(f"\n{K}Error:{N}", e)
            self.dump_default_data(num_data=15)
        except KeyboardInterrupt:
            print()

    def format_chipset(self, chipset_text):
        try:
            chipset = re.sub(r'\s*\(.*?\)', '', chipset_text).strip()
            if 'exynos' in chipset.lower():
                numbers = re.findall(r'\d+', chipset)
                return f"exynos_{numbers[0]}" if numbers else "exynos_unknown"
            elif 'snapdragon' in chipset.lower():
                parts = [p.lower() for p in chipset.split()]
                if 'sm' in ''.join(parts):
                    code = next((p for p in parts if p.startswith('sm')), "unknown")
                    return f"qualcomm_{code}"
                else:
                    numbers = re.findall(r'\d+', chipset)
                    return f"qualcomm_snapdragon_{'_'.join(numbers)}" if numbers else "qualcomm_unknown"
            elif 'dimensity' in chipset.lower() or 'helio' in chipset.lower():
                return '_'.join(re.findall(r'\b\w+\b', chipset)).lower()
            return '_'.join(chipset.split()).lower()
        except:
            return "unknown"


    def generate_model_number(self, url):
        if 'samsung' in url.lower():
            return f"SM-A{random.randint(100,999)}{random.choice(['', 'B', 'E'])}"
        elif 'xiaomi' in url.lower():
            return f"{random.randint(2000,2300)}{random.choice(['T', 'K', 'G'])}{random.randint(100,999)}"
        return "Unknown"


    def save_to_json(self):
        filename = f"{self.uas}.json"
        if os.path.exists(filename):
            try:
                with open(filename, "r", encoding="utf-8") as f:
                    old_data = json.load(f)
            except json.JSONDecodeError:
                old_data = []
        else:
            old_data = []

        combined_data = {json.dumps(d, sort_keys=True) for d in old_data + self.dump_brand_dan_model}
        unique_data = [json.loads(d) for d in combined_data]
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(unique_data, f, indent=2, ensure_ascii=False)


    def dump_default_data(self, num_data=15):
        models = ["SM-G930F", "SM-G991B", "SM-A536B", "SM-G998B", "SM-A127F"]
        operators = ["Indosat Ooredoo", "Telkomsel", "Axis", "INDOSAT", "XL Axiata"]
        
        combinations = [
            (m, o) 
            for m in random.sample(models, len(models))
            for o in random.sample(operators, len(operators))
        ][:num_data]

        for model, operator in combinations:
            self.dump_brand_dan_model.append({
                "device": "samsung",
                "brand": "Samsung",
                "model": model,
                "width": "1080",
                "height": "1920",
                "density": "3.0",
                "operators": operator,
                "model_chipset": f"unknown"

            })


    def calculate_density(self, ppi):
        if ppi >= 640: return 4.0
        elif ppi >= 480: return 3.0
        elif ppi >= 320: return 2.0
        elif ppi >= 240: return 1.5
        elif ppi >= 213: return 1.33
        elif ppi >= 160: return 1.0
        else: return 0.75


    def pilihan(self):
        while True:
            os.system("clear")
            print(
    f"""

   ______     __  __  __               ___                    __ 
  / ____/__  / /_/ / / /_______  _____/   | ____ ____  ____  / /_
 / / __/ _ \/ __/ / / / ___/ _ \/ ___/ /| |/ __ `/ _ \/ __ \/ __/
/ /_/ /  __/ /_/ /_/ (__  )  __/ /  / ___ / /_/ /  __/ / / / /_  
\____/\___/\__/\____/____/\___/_/  /_/  |_\__, /\___/_/ /_/\__/  
                                         /____/                  

{self.asw}

                [{H}*{N}] KUMPULAN TIPE MEREK HP [{H}*{N}]

[{H}01{N}] Samsung    [{H}06{N}] Oppo      [{H}11{N}] OnePlus    [{H}16{N}] Nothing    [{H}21{N}] Meizu
[{H}02{N}] Apple      [{H}07{N}] Google    [{H}12{N}] Honor      [{H}17{N}] vivo       [{H}22{N}] Asus
[{H}03{N}] Huawei     [{H}08{N}] Nokia     [{H}13{N}] Realme     [{H}18{N}] Alcatel    [{H}23{N}] ZTE
[{H}04{N}] Sony       [{H}09{N}] LG        [{H}14{N}] Lenovo     [{H}19{N}] Microsoft  [{H}24{N}] Umidigi
[{H}05{N}] HTC        [{H}10{N}] Motorola  [{H}15{N}] Xiaomi     [{H}20{N}] Coolpad    [{H}25{N}] Cat

         [{H}26{N}] Sharp      [{H}31{N}] Doogee      [{H}36{N}] Itel
         [{H}27{N}] Micromax   [{H}32{N}] Blackview   [{H}37{N}] TCL
         [{H}28{N}] Infinix    [{H}33{N}] Cubot
         [{H}29{N}] Ulefone    [{H}34{N}] Oukitel
         [{H}30{N}] Tecno      [{H}35{N}] Ulefone
""")


            choices = input(f"[?] masukkan nomor merek (misal: 1,2): ")
            urls = {
                "1": "samsung-phones-9.php",     "6": "oppo-phones-82.php",  
                "2": "apple-phones-48.php",      "7": "google-phones-107.php",  
                "3": "huawei-phones-58.php",     "8": "nokia-phones-1.php",  
                "4": "sony-phones-7.php",        "9": "lg-phones-20.php",  
                "5": "htc-phones-5.php",        "10": "motorola-phones-4.php",  

                "11": "oneplus-phones-95.php",   "16": "nothing-phones-150.php",  
                "12": "honor-phones-121.php",    "17": "vivo-phones-98.php",  
                "13": "realme-phones-118.php",   "18": "alcatel-phones-65.php",  
                "14": "lenovo-phones-73.php",    "19": "microsoft-phones-94.php",  
                "15": "xiaomi-phones-80.php",    "20": "coolpad-phones-109.php",  

                "21": "meizu-phones-74.php",     "26": "sharp-phones-89.php",  
                "22": "asus-phones-46.php",      "27": "micromax-phones-72.php",  
                "23": "zte-phones-62.php",       "28": "infinix-phones-127.php",  
                "24": "umidigi-phones-140.php",  "29": "ulefone-phones-139.php",  
                "25": "cat-phones-132.php",      "30": "tecno-phones-120.php",  

                "31": "doogee-phones-141.php",   "36": "itel-phones-131.php",  
                "32": "blackview-phones-142.php","37": "tcl-phones-85.php",  
                "33": "cubot-phones-143.php",  
                "34": "oukitel-phones-144.php",  
                "35": "ulefone-phones-145.php"  
            }
            selected_urls = [urls[choice.strip()] for choice in choices.split(',') if choice.strip() in urls]
            if not selected_urls:
                print("Input tidak valid! Pilih nomor 1, 2, 3, atau 4.")
                continue
            for selected_url in selected_urls:
                self.get_model(selected_url)
            exit(f"\n\n[{H}#{N}] selesai mengumpulkan device dan merek UserAgent\n[{H}#{N}] jalankan ulang sc nya ketik: python run.py")