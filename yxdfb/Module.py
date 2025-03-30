import requests
from datetime import datetime

class Tod:

    def __init__(self):
        pass

    def tggl(hari=None, bulan=None, tahun=None):
        nama_bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
        if hari is None or bulan is None or tahun is None:
            sekarang = datetime.now()
            hari = sekarang.day
            bulan = sekarang.month
            tahun = sekarang.year

        return f"{hari:02d}-{nama_bulan[bulan - 1]}-{tahun}"

    def get_ip(self):
        try:
            response = requests.Session().get(
                "http://ip-api.com/json/"
            ).json()
            if response["status"] == "success":
                return response["query"]
            else:
                return True
        except:
            return True