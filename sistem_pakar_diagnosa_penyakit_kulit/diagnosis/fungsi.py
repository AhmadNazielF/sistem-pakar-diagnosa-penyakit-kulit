import re

result_dict = {}
penyakit_sesuai = []

class dict:
  
# Memproses setiap elemen dalam data_pengetahuan
    def dict(rules):
        # Memisahkan string menjadi item-item
        pattern = r'<basisPengetauan: (\w+) : ([^>]+)>'
        matches = re.findall(pattern, rules)

        # Melakukan pengelompokan berdasarkan penyakit
        for match in matches:
            disease = match[0].strip()
            symptom = match[1].strip()
            if disease not in result_dict:
                result_dict[disease] = [symptom]
            else:
                result_dict[disease].append(symptom)

        print(result_dict)

    def getDict():
        return result_dict 
    
class chainFowarding:
    def chainFowarding(rules,input):
        penyakit_sesuai.clear()
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
         