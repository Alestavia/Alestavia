import os
import subprocess
import time

# Renkler için terminal kodları
class TerminalColors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# Emoji desteği için terminalde daha anlaşılır mesajlar
def print_emoji(text, emoji):
    print(f"{TerminalColors.OKGREEN}{emoji} {text} {emoji}{TerminalColors.ENDC}")

# ASCII Sanatı (ALESTASCAN) - Daha sade ve mobil uyumlu
def ascii_art():
    print(f"""
{TerminalColors.HEADER}{TerminalColors.WARNING}
+-----------------------------------+
|  /_\  | |   | __|/ __||_   _|/_\  |
| / _ \ | |__ | _| \__ \  | | / _ \ |
|/_/ \_\|____||___||___/  |_|/_/ \_\|
+-----------------------------------+
{TerminalColors.ENDC}
""")

def clear_screen():
    subprocess.run("clear", shell=True)

def print_header():
    ascii_art()  # ASCII art başlık ekle

def show_menu():
    print(f"""
{TerminalColors.OKGREEN}###########################
#   ALSTASCAN - v1.0       #
########################### {TerminalColors.ENDC}
    {TerminalColors.OKBLUE}1) 📋 Site Hakkında Bilgi
    2) ⚡ Hızlı Port Taraması
    3) 🧑‍💻 Versiyon Bilgisi
    4) 🖥️ Sistem Durumu
    5) ❌ Çıkış{TerminalColors.ENDC}
    """)

def check_and_install(command, emoji):
    """Komutun yüklü olup olmadığını kontrol et, yüklü değilse yükle"""
    if subprocess.call(f"command -v {command}", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE) != 0:
        print_emoji(f"{command} yüklü değil, yükleniyor...", emoji)
        subprocess.run(f"pkg install {command} -y", shell=True)
    else:
        print_emoji(f"{command} zaten yüklü.", emoji)

def execute_command(command):
    try:
        result = subprocess.run(command, shell=True, text=True, capture_output=True)
        if result.stdout:
            print(f"{TerminalColors.OKGREEN}{result.stdout}{TerminalColors.ENDC}")
        if result.stderr:
            print(f"{TerminalColors.FAIL}{result.stderr}{TerminalColors.ENDC}")
    except Exception as e:
        print(f"{TerminalColors.FAIL}Bir hata oluştu: {e}{TerminalColors.ENDC}")

def site_information():
    hedefip = input(f"{TerminalColors.OKGREEN}Hedef Site veya IP Girin: {TerminalColors.ENDC}")
    print(f"{TerminalColors.WARNING}Site hakkında bilgi alınıyor...{TerminalColors.ENDC}")
    execute_command(f"whois {hedefip}")
    input(f"{TerminalColors.OKBLUE}Devam etmek için Enter'a basın...{TerminalColors.ENDC}")

def quick_port_scan():
    hedefip = input(f"{TerminalColors.OKGREEN}Hedef Site veya IP Girin: {TerminalColors.ENDC}")
    print(f"{TerminalColors.WARNING}Port taraması yapılıyor...{TerminalColors.ENDC}")
    execute_command(f"nmap {hedefip}")
    input(f"{TerminalColors.OKBLUE}Devam etmek için Enter'a basın...{TerminalColors.ENDC}")

def version_info():
    hedefip = input(f"{TerminalColors.OKGREEN}Hedef Site veya IP Girin: {TerminalColors.ENDC}")
    print(f"{TerminalColors.WARNING}Versiyon bilgisi alınıyor...{TerminalColors.ENDC}")
    execute_command(f"nmap -sV {hedefip}")
    input(f"{TerminalColors.OKBLUE}Devam etmek için Enter'a basın...{TerminalColors.ENDC}")

def system_status():
    print(f"{TerminalColors.WARNING}Sistem durumu kontrol ediliyor...{TerminalColors.ENDC}")
    execute_command("top -n 1")
    input(f"{TerminalColors.OKBLUE}Devam etmek için Enter'a basın...{TerminalColors.ENDC}")

def main():
    while True:
        clear_screen()  # Ekranı her menüye girişte temizle
        print_header()  # ASCII art başlık ekle
        show_menu()  # Menü göster

        # nmap ve whois'in yüklü olduğunu kontrol et
        check_and_install("nmap", "⚙️")
        check_and_install("whois", "🔍")

        islemno = input(f"{TerminalColors.OKGREEN}İşlem numaranızı girin: {TerminalColors.ENDC}")

        if islemno == "1":
            site_information()
        elif islemno == "2":
            quick_port_scan()
        elif islemno == "3":
            version_info()
        elif islemno == "4":
            system_status()
        elif islemno == "5":
            print_emoji("Çıkılıyor... 🙏", "❌")
            time.sleep(2)
            break
        else:
            print_emoji("Geçersiz işlem numarası, lütfen tekrar deneyin. ⚠️", "❌")
            time.sleep(2)

if __name__ == "__main__":
    main()
