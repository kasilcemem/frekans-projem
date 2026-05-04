import json

# Buradaki sayıları istediğin zaman değiştirebilirsin
veriler = [120, 150, 110, 180, 210, 195, 250]

def detayli_analiz(liste):
    sonuclar = []
    for i in range(len(liste)):
        deger = liste[i]
        degisim = 0
        durum = "Başlangıç"
        
        if i > 0:
            degisim = deger - liste[i-1]
            durum = "Yükseliş" if degisim > 0 else "Düşüş"
        
        sonuclar.append({
            "nokta": i + 1,
            "deger": deger,
            "degisim": degisim,
            "durum": durum
        })
    return sonuclar

if __name__ == "__main__":
    analiz = detayli_analiz(veriler)
    with open("results.json", "w") as f:
        json.dump(analiz, f)
