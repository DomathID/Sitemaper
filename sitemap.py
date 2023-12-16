from googleapiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials
import httplib2
from colorama import Fore, Style, init

init(autoreset=True)

JSON_KEY_FILE = input(f"[{Fore.YELLOW}3{Style.RESET_ALL}] Masukkan nama file JSON kredensial: ")

def get_credentials():
    credentials = ServiceAccountCredentials.from_json_keyfile_name(
        JSON_KEY_FILE, ['https://www.googleapis.com/auth/webmasters'])
    return credentials.authorize(httplib2.Http())

def add_sitemap(site_url, feedpath):
    credentials = get_credentials()
    webmasters_service = build('webmasters', 'v3', http=credentials)

    try:
        request = webmasters_service.sitemaps().submit(
            siteUrl=site_url, feedpath=feedpath).execute()

        print(f"{Fore.GREEN}Hasil: Pemetaan situs berhasil ditambahkan.{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}Hasil: Terjadi kesalahan: {e}{Style.RESET_ALL}")

def get_sitemap_info(site_url, feedpath):
    credentials = get_credentials()
    webmasters_service = build('webmasters', 'v3', http=credentials)

    try:
        request = webmasters_service.sitemaps().get(
            siteUrl=site_url, feedpath=feedpath).execute()

        path = request.get('path', '')
        last_submitted = request.get('lastSubmitted', '')
        is_pending = request.get('isPending', '')
        contents = request.get('contents', [])

        print(f"{Fore.YELLOW}Path:{Style.RESET_ALL} {path}")
        print(f"{Fore.YELLOW}Last Submitted:{Style.RESET_ALL} {last_submitted}")
        print(f"{Fore.YELLOW}Is Pending:{Style.RESET_ALL} {is_pending}")

        if contents:
            content = contents[0]
            content_type = content.get('type', '')
            submitted = content.get('submitted', '')
            indexed = content.get('indexed', '')

            print(f"{Fore.YELLOW}Contents:{Style.RESET_ALL}")
            print(f"  {Fore.CYAN}Type:{Style.RESET_ALL} {content_type}")
            print(f"  {Fore.CYAN}Submitted:{Style.RESET_ALL} {submitted}")
            print(f"  {Fore.CYAN}Indexed:{Style.RESET_ALL} {indexed}")

    except Exception as e:
        print(f"{Fore.RED}Hasil: Terjadi kesalahan: {e}{Style.RESET_ALL}")

def delete_sitemap(site_url, feedpath):
    credentials = get_credentials()
    webmasters_service = build('webmasters', 'v3', http=credentials)

    try:
        webmasters_service.sitemaps().delete(
            siteUrl=site_url, feedpath=feedpath).execute()

        print(f"{Fore.GREEN}Hasil: Pemetaan situs berhasil dihapus.{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}Hasil: Terjadi kesalahan: {e}{Style.RESET_ALL}")

def list_sitemaps(site_url, sitemap_index=None):
    credentials = get_credentials()
    webmasters_service = build('webmasters', 'v3', http=credentials)

    try:
        request = webmasters_service.sitemaps().list(
            siteUrl=site_url, sitemapIndex=sitemap_index).execute()

        sitemaps = request.get('sitemap', [])

        print(f"{Fore.YELLOW}List Sitemaps:{Style.RESET_ALL}")

        for sitemap in sitemaps:
            path = sitemap.get('path', '')
            last_submitted = sitemap.get('lastSubmitted', '')
            is_pending = sitemap.get('isPending', '')

            print(f"  {Fore.CYAN}Path:{Style.RESET_ALL} {path}")
            print(f"  {Fore.CYAN}Last Submitted:{Style.RESET_ALL} {last_submitted}")
            print(f"  {Fore.CYAN}Is Pending:{Style.RESET_ALL} {is_pending}")
            print()

    except Exception as e:
        print(f"{Fore.RED}Hasil: Terjadi kesalahan: {e}{Style.RESET_ALL}")

while True:
    banner = f'''
{Fore.YELLOW}███████╗██╗████████╗███████╗███╗   ███╗ █████╗ ██████╗{Style.RESET_ALL} ███████╗██████╗ 
{Fore.YELLOW}██╔════╝██║╚══██╔══╝██╔════╝████╗ ████║██╔══██╗██╔══██{Style.RESET_ALL}╗██╔════╝██╔══██╗
{Fore.YELLOW}███████╗██║   ██║   █████╗  ██╔████╔██║███████║██████╔{Style.RESET_ALL}╝█████╗  ██████╔╝
{Fore.YELLOW}╚════██║██║   ██║   ██╔══╝  ██║╚██╔╝██║██╔══██║██╔═══╝{Style.RESET_ALL} ██╔══╝  ██╔══██╗
{Fore.YELLOW}███████║██║   ██║   ███████╗██║ ╚═╝ ██║██║  ██║██║    {Style.RESET_ALL} ███████╗██║  ██║
{Fore.YELLOW}╚══════╝╚═╝   ╚═╝   ╚══════╝╚═╝     ╚═                {Style.RESET_ALL}╚══════╝╚═╝  ╚═╝
[ Author: {Fore.YELLOW}DomathID{Style.RESET_ALL} ] [ Github: {Fore.YELLOW}github.com/DomathID{Style.RESET_ALL} ] [ {Fore.YELLOW}Submit Sitemap{Style.RESET_ALL} ]
'''
    print(banner)
    print("\nMenu Tools:")
    print(f"[{Fore.YELLOW}1{Style.RESET_ALL}] Add Sitemap")
    print(f"[{Fore.YELLOW}2{Style.RESET_ALL}] Get Info Sitemap")
    print(f"[{Fore.YELLOW}3{Style.RESET_ALL}] Delete Sitemap")
    print(f"[{Fore.YELLOW}4{Style.RESET_ALL}] List Sitemaps")
    print(f"[{Fore.YELLOW}0{Style.RESET_ALL}] Keluar")

    choice = input("Pilih menu (0/1/2/3/4): ")

    if choice == '1':
        site_url = input(f"[{Fore.YELLOW}1{Style.RESET_ALL}] Masukkan URL situs: ")
        feedpath = input(f"[{Fore.YELLOW}2{Style.RESET_ALL}] Masukkan path feed (contoh: {Fore.YELLOW}https://www.web.com/rss.xml{Style.RESET_ALL}): ")
        add_sitemap(site_url, feedpath)
    elif choice == '2':
        site_url = input(f"[{Fore.YELLOW}1{Style.RESET_ALL}] Masukkan URL situs: ")
        feedpath = input(f"[{Fore.YELLOW}2{Style.RESET_ALL}] Masukkan path feed (contoh: {Fore.YELLOW}https://www.web.com/rss.xml{Style.RESET_ALL}): ")
        get_sitemap_info(site_url, feedpath)
    elif choice == '3':
        site_url = input(f"[{Fore.YELLOW}1{Style.RESET_ALL}] Masukkan URL situs: ")
        feedpath = input(f"[{Fore.YELLOW}2{Style.RESET_ALL}] Masukkan path feed (contoh: {Fore.YELLOW}https://www.web.com/rss.xml{Style.RESET_ALL}): ")
        delete_sitemap(site_url, feedpath)
    elif choice == '4':
        site_url = input(f"[{Fore.YELLOW}1{Style.RESET_ALL}] Masukkan URL situs: ")
        sitemap_index = input(f"[{Fore.YELLOW}2{Style.RESET_ALL}] Masukkan URL indeks peta situs (opsional): ")
        list_sitemaps(site_url, sitemap_index)
    elif choice == '0':
        break
    else:
        print(f"{Fore.RED}Pilihan tidak valid. Silakan pilih lagi.{Style.RESET_ALL}")

