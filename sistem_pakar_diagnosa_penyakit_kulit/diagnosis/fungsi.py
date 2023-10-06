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
    penyakit_sesuai = []  # Define penyakit_sesuai as a class variable

    @classmethod
    def chainFowarding(cls, rules, input):
        cls.penyakit_sesuai.clear()
        penyakit_percentage = {}
        maxPercentage = 0

        for penyakit, gejala_penyakit in rules.items():
            matching_gejala = [gejala_k for gejala_k in gejala_penyakit if gejala_k in input]
            percentage = (len(matching_gejala) / len(gejala_penyakit)) * 100

            penyakit_percentage[penyakit] = percentage

            if percentage > maxPercentage:
                cls.penyakit_sesuai.clear()  # Clear the list when a higher percentage is found
                cls.penyakit_sesuai.append(penyakit)
                maxPercentage = percentage
            
            elif percentage == maxPercentage:
                # If the percentage is equal to the max, append the current penyakit to the list
                cls.penyakit_sesuai.clear()

        # Menampilkan hasil chain forwarding dengan presentase
        if cls.penyakit_sesuai:
            print("Berdasarkan gejala yang Anda berikan, penyakit medis yang paling mungkin adalah:")
            for penyakit in cls.penyakit_sesuai:
                print(f"- {penyakit} ({penyakit_percentage[penyakit]:.2f}% matching)")
        else:
            print("Tidak dapat menentukan penyakit medis berdasarkan gejala yang diberikan.")

    @classmethod
    def getPenyakit(cls):
        if cls.penyakit_sesuai:
            return cls.penyakit_sesuai[0]  # Return the first element (highest percentage)
        else:
            return ""
