class Pws:
    
    def generate_passwords(self, nama, asal, pw_tambahan):
        nama = nama.lower().strip()
        asal = asal.lower().strip() if asal else ""
        nama_split = nama.split()
        depan = nama_split[0] if len(nama_split) > 0 else ""
        
        pasw = []
        if len(nama) <= 5:
            if len(depan) >= 3:
                pasw.extend([nama, depan + "123", depan + "1234", depan + "12345", depan + "123456", depan + "01", depan + "02", depan + "05", depan + "11", depan + "12"])
        else:
            if len(depan) >= 3:
                pasw.extend([nama, depan + "123", depan + "1234", depan + "12345", depan + "123456", depan + "01", depan + "02", depan + "11", depan + "12"])
            else:
                pasw.append(nama)
        
        pasw.extend(pw_tambahan)
        return pasw