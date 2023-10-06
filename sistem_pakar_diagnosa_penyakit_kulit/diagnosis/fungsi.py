data_dict = {}
penyakit_sesuai = []

class dict:
  
# Memproses setiap elemen dalam data_pengetahuan
    def dict(rules):
        queryset_str = str(rules)
        # Remove unnecessary characters and split the string into individual records
        queryset_str = queryset_str.replace("<QuerySet [", "").replace("]>", "").replace("<basisPengetauan: ", "").replace(", <basisPengetauan: ","").replace('>', '')
        records = queryset_str.split(', ')

        print(records)
            
# Iterasi melalui setiap elemen dalam list
        for item in records:
            # Pisahkan elemen menjadi penyakit dan gejala
            parts = item.split(' : ')
            
            if len(parts) == 2:
                penyakit, gejala = parts
                penyakit = penyakit.strip()
                # Jika penyakit belum ada di dictionary, tambahkan sebagai kunci dengan daftar gejala
                if penyakit not in data_dict :
                    data_dict [penyakit] = [gejala]
                else:
                    data_dict [penyakit].append(gejala)
            else:
                # Jika ada elemen tambahan yang bukan gejala, gabungkan dengan gejala sebelumnya
                data_dict [penyakit][-1] += f', {item}'

    def getDict():
        return data_dict 
    
class chainFowarding:
    def chainFowarding(rules,input):
        
        for penyakit, gejala_penyakit in rules.items():
            if all(gejala_k in input for gejala_k in gejala_penyakit):
                penyakit_sesuai.append(penyakit)

        # Menampilkan hasil chain forwarding
        if penyakit_sesuai:
            print("Berdasarkan gejala yang Anda berikan, kemungkinan penyakit medis yang sesuai adalah:")
            for penyakit in penyakit_sesuai:
                print(f"- {penyakit}")
        else:
            print("Tidak dapat menentukan penyakit medis berdasarkan gejala yang diberikan.")

    def getPenyakit():
        if penyakit_sesuai:
            penyakit = penyakit_sesuai[0]
            return penyakit
        else:
            penyakit = ""
            return penyakit
         