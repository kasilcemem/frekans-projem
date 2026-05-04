import json
import requests

def hava_durumu_cek():
    # İstanbul koordinatları: 41.0082, 28.9784
    url = "https://api.open-meteo.com/v1/forecast?latitude=41.0082&longitude=28.9784&daily=temperature_2m_max,temperature_2m_min&timezone=auto"
    
    try:
        cevap = requests.get(url)
        veri = cevap.json()
        
        gunluk = veri['daily']
        sonuclar = []
        
        for i in range(len(gunluk['time'])):
            tarih = gunluk['time'][i]
            maks = gunluk['temperature_2m_max'][i]
            min_derece = gunluk['temperature_2m_min'][i]
            ortalama = round((maks + min_derece) / 2, 1)
            
            sonuclar.append({
                "nokta": tarih,  # Tarih bilgisi
                "deger": ortalama, # Ortalama sıcaklık
                "degisim": maks,   # Maksimum sıcaklık
                "durum": f"Min: {min_derece}°C" # Bilgi notu
            })
        return sonuclar
    except Exception as e:
        print(f"Hata oluştu: {e}")
        return []

if __name__ == "__main__":
    analiz_verisi = hava_durumu_cek()
    if analiz_verisi:
        with open("results.json", "w") as f:
            json.dump(analiz_verisi, f)
