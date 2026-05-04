import json

# Bu listeye istediğin kadar yeni sayı ekleyebilirsin
veriler = [120, 150, 110, 180, 210, 195, 250, 230]

def analiz_et(liste):
    sonuclar = []
    for i, deger in enumerate(liste):
        degisim = 0 if i == 0 else deger - liste[i-1]
        durum = "Sabit"
        if degisim > 0: durum = "Yükseliş 📈"
        elif degisim < 0: durum = "Düşüş 📉"
        
        sonuclar.append({
            "nokta": i + 1,
            "deger": deger,
            "degisim": degisim,
            "durum": durum
        })
    
    # Basit bir gelecek tahmini ekleyelim
    ortalama_degisim = sum(d['degisim'] for d in sonuclar) / len(sonuclar)
    tahmin = liste[-1] + ortalama_degisim
    
    # Tahmini de sonuca ekleyelim
    sonuclar.append({
        "nokta": "TAHMİN",
        "deger": round(tahmin, 2),
        "degisim": round(ortalama_degisim, 2),
        "durum": "Öngörü 🔮"
    })
    
    return sonuclar

if __name__ == "__main__":
    cikti = analiz_et(veriler)
    with open("results.json", "w") as f:
        json.dump(cikti, f)
