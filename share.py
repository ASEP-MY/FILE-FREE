import requests, json
ses=requests.Session()
print("┌─────────────────────────────────────────────────────────────┐ │                                                             │ │   █████╗ ███████╗███████╗██████╗       ███╗   ███╗██╗   ██╗ │")
print("│  ██╔══██╗██╔════╝██╔════╝██╔══██╗      ████╗ ████║╚██╗ ██╔╝ │ │  ███████║███████╗█████╗  ██████╔╝█████╗██╔████╔██║ ╚████╔╝  │ │  ██╔══██║╚════██║██╔══╝  ██╔═══╝ ╚════╝██║╚██╔╝██║  ╚██╔╝   │")
print("│  ██║  ██║███████║███████╗██║           ██║ ╚═╝ ██║   ██║    │ │  ╚═╝  ╚═╝╚══════╝╚══════╝╚═╝           ╚═╝     ╚═╝   ╚═╝    │ │                                          ASEP YUSUP  2022   │")
print("└─────────────────────────────────────────────────────────────┘")
print("=================================================")
print("╔══◍➤\x1b[1;97mAutor     : \x1b[1;92mSUKAMAKMUR")
print("╠══◍➤\x1b[1;97mGithub    : \x1b[1;92mhttps://github.com/KangCrot")
print("╠══◍➤\x1b[1;97mFacebook  : \x1b[1;92mfb.me/ᏗᏕᏋᎮ ᎷᏗᏬᏝᏗᏁᏗ ᎽᏬᏕᏬᎮ")
print("╚══◍➤\x1b[1;97mCoded By  : \x1b[1;92mAsep \x1b[1;97m& \x1b[1;92mDinda")
print("=================================================")

def menu():
	os.system('clear')
	print("SILAHKAN LOGIN USERNAME SAMA PASSWORD\n")
	username = input("[>] USERNAME \033[1;91m: \033[1;92m")
	password = input("[>] PASSWORD \033[1;91m: \033[1;92m")
	if username =="ASEP" and password =="GANTENG":
		print("[>] LOGIN BERASIL")
		#time.sleep(1)
		login()
	else:
		print("[>] LOGIN GAGAL!!!")
		print("ANDA AKAN DI ARAHAN KE TELEGRAM MINTA USERNAME SAMA PASSWORD")
		os.system('xdg-open https://t.me/ASEPYUSUP')
		time.sleep(1);menu()

def login():
cok = input(" masukan cookie : ")
token = input(" masukan token : ")
idt = input(" masukan link : ")
limit = int(input(" masukan limit : "))
cookie = {"cookie":cok}
try:
	n = 0
	header = {"authority":"graph.facebook.com","cache-control":"max-age=0","sec-ch-ua-mobile":"?0","user-agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.66 Safari/537.36"}
	for x in range(limit):
		n+=1
		post = ses.post(f"https://graph.facebook.com/v13.0/me/feed?link={idt}&published=0&access_token={token}",headers=header, cookies=cookie).text
		data = json.loads(post)
		if "id" in post:
			print(f" {n}. berhasil membagikan {data['id']}")
		else:
			exit(" gagal membagikan, kemungkinan token invalid")
except:
	exit(" gagal membagikan, kemungkinan token invalid")


if __name__ == '__main__':
	menu()