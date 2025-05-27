import socket
import argparse

try:
    import whois
except ImportError:
    whois = None

def get_ip(domain):
    try:
        return socket.gethostbyname(domain)
    except socket.gaierror:
        return None

def get_whois(domain):
    if whois is None:
        return None
    try:
        w = whois.whois(domain)
        return str(w)
    except Exception:
        return None

def main():
    parser = argparse.ArgumentParser(description="Basit Siber Güvenlik Recon Aracı")
    parser.add_argument("domain", help="Hedef domain adresi")
    args = parser.parse_args()

    domain = args.domain
    print(f"[*] Hedef: {domain}")

    ip = get_ip(domain)
    if ip:
        print(f"[+] IP Adresi: {ip}")
    else:
        print("[-] IP adresi bulunamadı.")

    whois_info = get_whois(domain)
    if whois_info:
        print("[+] Whois Bilgileri:\n")
        print(whois_info)
    else:
        print("[-] Whois bilgisi alınamadı.")

if __name__ == "__main__":
    main()
