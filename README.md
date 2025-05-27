# siber-recon-araci
Whois ve port taraması yapan temel siber güvenlik aracı
import socket
import whois
import subprocess
import argparse

def get_ip(domain):
    try:
        ip = socket.gethostbyname(domain)
        print(f"[+] IP Adresi: {ip}")
        return ip
    except Exception as e:
        print(f"[-] IP alınamadı: {e}")
        return None

def get_whois(domain):
    try:
        w = whois.whois(domain)
        print("\n[+] WHOIS Bilgisi:")
        print(w)
    except Exception as e:
        print(f"[-] WHOIS alınamadı: {e}")

def scan_ports(ip):
    print("\n[+] Port taraması başlatılıyor (ilk 1000 port)...")
    try:
        subprocess.run(["nmap", "-F", ip])
    except Exception as e:
        print(f"[-] Nmap çalıştırılamadı: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Siber Keşif Aracı")
    parser.add_argument("domain", help="Hedef domain (örnek: google.com)")
    parser.add_argument("--scan", action="store_true", help="Port taraması yap")
    args = parser.parse_args()

    print(f"[*] Hedef: {args.domain}")
    ip = get_ip(args.domain)
    get_whois(args.domain)

    if args.scan and ip:
        scan_ports(ip)
