import os
import json
import random

class UserAgent:

    def __init__(self):
        ua_ig_path = "data/cache/.ua_ig.json"
        ua_fb_path = "data/cache/.ua_fb.json"
        sett_uaig_path = "data/cache/.sett_UaIG.json"
        sett_uafb_path = "data/cache/.sett_UaFB.json"

        if os.path.exists(sett_uaig_path):
            ua_ig_path = sett_uaig_path

        if os.path.exists(sett_uafb_path):
            ua_fb_path = sett_uafb_path

        self.ua_fb = self.load_json(ua_fb_path)
        self.ua_ig = self.load_json(ua_ig_path)

        self.api_devices = [
            d for d in self.ua_fb 
            if ("Ultra" in d['model'] or "+" in d['model']) and 
               "Unknown" not in d["brand"] and 
               "Unknown" not in d["model"]
        ]

        if not self.api_devices:
            self.api_devices = [
                d for d in self.ua_fb 
                if "Unknown" not in d["brand"] and "Unknown" not in d["model"]
            ]

    @staticmethod
    def load_json(file_path):
        try:
            with open(file_path, "r") as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def ua_fb_api(self):
        if not self.api_devices:
            return ""
        
        while True:
            device = random.choice(self.api_devices)
            if "Unknown" in device["brand"] or "Unknown" in device["model"]:
                continue
            ua1 = {
                'FBAN': 'FB4A',
                'FBAV': random.choice(["364.0.0.24.132", "364.0.0.14.77", "364.1.0.25.132"]),
                'FBBV': str(random.randint(653066364, 953066364)),
                'FBDM': f"{{density={device['density']},width={device['width']},height={device['height']}}}",
                'FBLC': "id_ID",
                'FBRV': '0',
                'FBCR': device['operators'],
                'FBMF': device['brand'],
                'FBBD': device['brand'],
                'FBPN': "com.facebook.mahos",
                'FBDV': device['model'],
                'FBSV': device['android_version'],
                'FBOP': '1',
                'FBCA': "arm64-v8a:;"
            }
            
            return f"[{';'.join(f'{k}/{v}' for k, v in ua1.items())}]".replace("  ", " ")
    
    def ua_fb_val(self):
        if not self.ua_fb:
            return ""
        
        while True:
            device = random.choice(self.ua_fb)
            if "Unknown" in device["brand"] or "Unknown" in device["model"]:
                continue

            build_prefix = random.choice(["TP1A", "SP1A", "SQ3A"])
            build_date = f"{random.randint(20, 23)}{random.randint(1,12):02}"
            build_number = f"{build_prefix}.{build_date}.{random.randint(100, 999)}"

            chrome_versions = [f"12{random.randint(0,2)}.0.{random.randint(1000, 9999)}.{random.randint(1, 99)}" for _ in range(3)]
            firefox_versions = ["115.0", "114.0.2"]
            edge_versions = [f"12{random.randint(0,2)}.0.{random.randint(1000, 9999)}.0" for _ in range(2)]
            browser_variants = ["Chrome", "Firefox", "Edge"]
            browser_variant = random.choice(browser_variants)

            if device["brand"].lower() == "samsung":
                samsung_version = random.choice(["25.0.1.251", "24.0.0.7"])
                chrome_core_version = random.choice(["114.0.5735.196", "115.0.5790.186"])
                user_agent = (
                    f"Mozilla/5.0 (Linux; Android {device['android_version']}; {device['model']} Build/{build_number}) "
                    f"AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/{samsung_version} Chrome/{chrome_core_version} Mobile Safari/537.36"
                )
            else:
                browser_version = (
                    random.choice(chrome_versions) if browser_variant == "Chrome" else 
                    random.choice(firefox_versions) if browser_variant == "Firefox"
                    else random.choice(edge_versions)
                )

                user_agent = (
                    f"Mozilla/5.0 (Linux; Android {device['android_version']}; {device['model']} Build/{build_number}) "
                    f"AppleWebKit/537.36 (KHTML, like Gecko) {browser_variant}/{browser_version} Mobile Safari/537.36"
                )
            
            return user_agent.replace('  ', ' ')

    def get_valid_device(self):
        while True:
            device = random.choice(self.ua_ig)
            if any(val.lower() in ["unknown", ""] for val in [device["brand"], device["model"], device["model_chipset"]]):
                continue
            return device


    def ua_instagram(self, barcelona):
        version = '364.0.0.35.110' if barcelona else '360.0.0.52.192'
        version_code = '687078620' if barcelona else '672535977'
        device = self.get_valid_device()

        android_versions = [
            ('34', '12'), ('33', '11'),
            ('32', '10'), ('31', '10'),
            ('30', '11'), ('29', '10'),
            ('28', '9')
        ]
        android_ver = random.choice(android_versions)

        dpi = f"{round(float(device['density']) * 160)}dpi"
        chipset_mapping = {
            'qualcomm': lambda x: 'qcom',
            'exynos': lambda x: x.replace('_', ''),
            'mediatek': lambda x: x.split('_')[1] if "_" in x else x,
            'tensor': lambda x: 'tensor',
            'dimensity': lambda x: x.split('_')[1] if "_" in x else x,
            'helio': lambda x: x.split('_')[1] if "_" in x else x
        }

        chipset = device["model_chipset"].lower()
        processed_chipset = chipset.split('_')[0]
        for key in chipset_mapping:
            if key in chipset:
                processed_chipset = chipset_mapping[key](chipset)
                break

        model_prefix = ''.join([c for c in device['model'] if c.isalpha()])
        model_number = ''.join([c for c in device['model'] if c.isdigit()])
        short_model = f"{model_prefix.lower()}{model_number[:2]}" if model_prefix else device['model'][:4]
        #bahasa = random.choice(["in_ID", "fa_IR", "bs_BA", "en_ZA", "ar_AR", "es_MX"])
        ua1 = (
            f'Instagram {version} Android '
            f'({android_ver[0]}/{android_ver[1]}; '
            f'{dpi}; '
            f'{device["width"]}x{device["height"]}; '
            f'{device["brand"].lower()}; '
            f'{device["model"]}; '
            f'{short_model}; '
            f'{processed_chipset}; '
            f'in_ID; '
            f'{version_code})'
        )
        ua2 = (
            f'Instagram {version} Android '
            f'({android_ver[0]}/{android_ver[1]}; '
            f'{dpi}; '
            f'{device["width"]}x{device["height"]}; '
            f'{device["brand"]}/{device["model"]}; '
            f'{device["device"]}; '
            #f'{short_model}; '
            f'{processed_chipset}; '
            f'in_ID; '
            f'{version_code})'
        )
        ua3 = (
            f'Barcelona 348.1.0.44.109 Android '
            f'({android_ver[0]}/{android_ver[1]}; '
            f'{dpi}; '
            f'{device["width"]}x{device["height"]}; '
            f'{device["brand"].lower()}; '
            f'{device["model"]}; '
            f'{short_model}; '
            f'{processed_chipset}; '
            f'in_ID; '
            f'640443180)'
        )
        return random.choice([ua1, ua3]).replace('  ', ' ')
"""
import os
os.system("clear")
ua = UserAgent()
for _ in range(6):
    print()
    print(ua.ua_fb_api())
    print()
    print(ua.ua_instagram(""))
"""