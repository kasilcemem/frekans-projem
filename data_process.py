import json
import requests

def hava_durumu_cek():
    # Antalya ilçeleri koordinatları
    ilceler = {
        "Kaş ☀️": {"lat": 36.2000, "lon": 29.6333},
        "Demre 🍅": {"lat": 36.2444, "lon": 29.9856},
        "Finike 🍊": {"lat": 36.2956, "lon": 30.1444},
        "Alanya 🏰": {"lat": 36.5437, "lon": 31.9998}
    }
    
    sonuclar = []
    
    for isim, koord in ilceler.items():
        url = f"https://api.open-meteo.com/v1/forecast?latitude={koord['lat']}&longitude={koord['lon']}&current_weather=true"
        try:
            cevap = requests.get(url)
            veri = cevap.json()
            su_an = veri['current_weather']
            
            sonuclar.append({
                "nokta": isim,
                "deger": su_an['temperature'],
                "degisim": su_an['windspeed'], # Rüzgar hızı
                "durum": f"Rüzgar: {su_an['windspeed']} km/s"
            })
        except:
            print(f"{isim} verisi alınamadı.")
            
    return sonuclar

if __name__ == "__main__":
    analiz_verisi = hava_durumu_cek()
    if analiz_verisi:
        with open("results.json", "w") as f:
            json.dump(analiz_verisi, f)
