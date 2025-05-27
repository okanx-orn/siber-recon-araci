# siber-recon-araci
Whois ve port taraması yapan temel siber güvenlik aracı
# Recon Tool – Basit OSINT & Bilgi Toplama Aracı

Bu Python aracı, verilen bir domain'e ait IP adresini ve whois bilgilerini elde etmek için kullanılır. Siber güvenlik ve OSINT alanında başlangıç seviyesinde bir recon (bilgi toplama) pratiği yapmak isteyenler için uygundur.
## 🔧 Özellikler

- IP adresi çözümleme
- Whois bilgisi alma
- Komut satırı argüman desteği
- Basit, anlaşılır kod yapısı
## 📦 Gereksinimler

- Python 3.10 veya üzeri
- Windows işletim sistemi
- `C:\Tools\whois.exe` dosyasının bulunması (Manual kurulum gerekli)
## 🚀 Kurulum

1. Python kurulu olduğundan emin olun:  
   https://www.python.org/downloads/

2. `whois.exe` aracını indirin ve `C:\Tools\` klasörüne yerleştirin.  
   İndirme: https://docs.microsoft.com/en-us/sysinternals/downloads/whois

3. Kod dosyasını indirin veya klonlayın:

```bash
git clone https://github.com/kullaniciadi/recon-tool.git
cd recon-tool

---

### 5. ⚙️ Kullanım
```markdown
## ⚙️ Kullanım

```bash
py recon.py example.com
[*] Hedef: example.com
[+] IP Adresi: 93.184.216.34
[+] Whois Bilgileri:
...

---

### 6. 📚 Öğrendikleriniz
```markdown
## 📚 Bu Projeyle Öğrenilecekler

- Python ile socket ve subprocess kullanımı
- Komut satırı argüman yönetimi
- OSINT ve bilgi toplama süreçleri
## 🤖 Geliştirme Fikirleri

- Nmap entegrasyonu
- GUI arayüz (Tkinter, PyQt)
- Subdomain keşfi (crt.sh API, DNS brute)
- Şifre kırıcı modülü (zip, FTP, HTTP Auth)

Projeyi geliştirmek istersen, "Issues" kısmına bakmayı unutma 👇 (ilk yaptığım proje o yüzden milyonlarca hata beklenir)
