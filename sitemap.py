from googleapiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials
import httplib2
import json
from colorama import Fore, Style, init

init(autoreset=True)


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
site_url = input(f"[{Fore.YELLOW}1{Style.RESET_ALL}] Masukkan URL situs: ")
feedpath = input(f"[{Fore.YELLOW}2{Style.RESET_ALL}] Masukkan path feed (contoh: {Fore.YELLOW}https://www.web.com/rss.xml{Style.RESET_ALL}): ")
JSON_KEY_FILE = input(f"[{Fore.YELLOW}3{Style.RESET_ALL}] Masukkan nama file JSON kredensial: ")


add_sitemap(site_url, feedpath)

