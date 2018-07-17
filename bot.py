import requests                                                                                                                                                                                                    
from bs4 import BeautifulSoup
import telepot

bot = telepot.Bot("TOKEN HERE")

palavroes = ['Alienado', 'Animal de Teta', 'Anormal', 'Argentino', 'Arregassado', 'Arrombado', 'Babaca', 'Baitola', 'Baleia', 'Barril', 'Benfiquista', 'Biba', 'Bicha', 'BIOS', 'Biroska', 'Bobo', 'Bocal','Boludo', 'Bolagato', 'Boqueteiro', 'Bosta', 'Buceta', 'Bundao', 'Burro', 'Cabaco', 'Cacete', 'Cadelona', 'Cafona', 'Carai', 'Cambista', 'Capiroto', 'Caralho', 'Catraia', 'Cepo', 'Cocodrilo', 'Cocozento', 'Cu', 'DebilMental', 'Demente', 'Desciclope', 'Desgracado', 'Drogado', 'EGUENORANTE', 'Endemoniado', 'Energumeno', 'Enfianocu', 'EngoleRola', 'Escroto', 'Esdruxulo', 'Esporrado', 'Estigalhado', 'Estrume', 'Estrunxado', 'Estupido', 'FDP', 'Fidumaegua', 'FilhodaPuta', 'Fiofo', 'Foda', 'Fuder', 'Fudido', 'Fulera', 'Galinha', 'Gambiarra', 'GeisyArruda', 'Gnu', 'Gonorreia', 'GordoEscroto', 'Gozado', 'Herege', 'Idiota', 'Ignorante', 'Imbecil', 'Imundo', 'Inascivel', 'Inseto', 'Invertebrado', 'Jacu', 'Jegue', 'Jumento', 'KCT', 'Komodo', 'Ku', 'Karai', 'lazarento', 'Lazaro!', 'Leproso', 'lerdo', 'lesma', 'Lezado', 'lico', 'Limpezaanal', 'lixo', 'lombriga', 'Macaco', 'MariMoon', 'Merda', 'Meretriz', 'MiolodeCu', 'Mocorongo', 'MontedeMerda', 'Morfetico', 'Mulambo', 'n00b', 'Nazista', 'Nerd', 'Newbie', 'Nhaca', 'Nonsense', 'Ogro', 'Olhodocu', 'OlhoGordo', 'Otario', 'Palhaco', 'Panaca', 'Paraguaio', 'Passaralho', 'PauNoCu', 'Periquita', 'Pimenteira', 'Pipoca', 'Piranha', 'Piroca', 'Pistoleira', 'Porra', 'prostituta', 'Punheta', 'Puta', 'PutaQuePariu', 'Quasimodo', 'Quenga', 'Quirguistao', 'Rampero', 'Rapariga', 'Raspadinha', 'Retardado', 'Rusguento', 'Sanguesuga', 'Sujo', 'Tapado', 'Tarado', 'Tesao', 'Tetuda', 'Tetudo', 'Tosco', 'Tragado', 'Travesti', 'Trepadeira', 'Troglodita', 'Tnc', 'Urubu', 'Vaca', 'Vadia', 'Vagabundo', 'Vagaranha', 'Vai a merda', 'vai se fuder', 'Vai tomar no cu', 'Vascaino', 'Verme', 'Viado','Vsf', 'Xavasca', 'Xereca', 'Xixizento', 'Xoxota', 'Xupetinha', 'Xupisco', 'Xurupita', 'Xuxexo', 'XXT', 'XXX', 'ZeBuceta', 'Ziguizira', 'Zina', 'Zoado', 'Zoiudo', 'Zoneira', 'Zuado', 'Zuera', 'Zulu', 'Zureta']
for i in range(len(palavroes)):
	palavroes[i] = palavroes[i].lower()



def getPalavrao(msg,id,name):
	for palavra in msg.split():
		if(palavra.lower() in palavroes):
			bot.sendMessage(id, name + ' para de xingar, porra')
			break
			
def getBuild(busca,id):

	url = 'https://www.probuilds.net/champions/details/' + busca

	r = requests.get(url,stream=True)

	soup = BeautifulSoup(r.text, 'html.parser')
	divTag = soup.find_all("div", {"class":"item tooltip"})

	i = 1

	if(len(divTag) == 0):
		bot.sendMessage(id, busca + ' não encontrado')


	for tag in divTag:
		if(i > 6):
			break
		palavra = str(tag)
		palavra = palavra.split('src="')
		palavra[1] = palavra[1][:-10]
		bot.sendPhoto(id,palavra[1])
		print(palavra[1])
		i += 1

def getUnB(name,id):

	cookies = {
	    'TS01fe7044': '011d1b331253d11a4e839216c35be9a2d925ba79165537a36a2c1f39b3e8a2e4dd2d74edb13822df0ed013c26c5a15c326aef377b31e057f24053fe914f41b033e49aae732b5fac1ec4dbc43c47871dff0f761345ba8bcd07cccbdfc079025a2a406e4d369',
	    '_ga': 'GA1.2.634353066.1523032756',
	    '_gid': 'GA1.2.1986405471.1531756199',
	    'cebraspe': '2281701386.47873.0000',
	    'f5_cspm': '1234',
	    'f5avr1720246155aaaaaaaaaaaaaaaa': 'MHGFMDJCECMDJODDPFDAMDLCNNEBPKEJGLEONNFGIMOFPMLOICFHHIABIOFGOCIOHBGCFHBKCFHOPJBCKMDAPMIJAGKIFACBLIBPIGENCGCBCNNNDGGDHDBJIMAHPIOM',
	    'f5avrbbbbbbbbbbbbbbbb': 'HGLCOCJBFGMMBCCDBMAKPELCKJGADHGJCPKOKIFGJMOFPMLOLMFHHJABIOFGOCIOHBGDFHBKJMKFPEMJKMDAPMIJGPONLPGEILACDGINCGCBCNHNNHJFBJGJIMAHPIEA',
	    'f5avrbbbbbbbbbbbbbbbb': 'BPKJBAIMKLNBMKNEBALEDHHMMFIJBHMHBEECHAFAEFMEPDBAEEJLOFKHDDAAOMLLJLJDMNPHKMFOGIEDAKAAKBAHGPEMPCEAJNLBOABCGOGFBIIJBJAAOLHCOHCNENDL'
	}


	payload = {
	    '__VIEWSTATE': '/wEPDwULLTIwNDcwNjgyNzgPZBYCAgMPZBYEAgkPPCsAEQMADxYEHgtfIURhdGFCb3VuZGceC18hSXRlbUNvdW50ZmQBEBYAFgAWAAwUKwAAZAILDw9kDxAWAWYWARYCHg5QYXJhbWV0ZXJWYWx1ZWUWAWZkZBgBBQlHcmlkVmlldzEPPCsADAEIZmRKNfzIDfPcDzZ8JDptWaVnglla4KM67vUb2pA9eP8IBA==',
	    '__VIEWSTATEGENERATOR': '1E89593C',
	    '__EVENTVALIDATION': '/wEdAAMVqGChLN6KXH7kzeptnD+aha8fMqpdVfgdiIcywQp19DppxJvnrmWsj7+A71jlP/x0KW3rH/zhqC0eBW02w2FmxS40jH2h9/HMimFwHf0w3g==',
	    'txtNome': name,
	    'btnBuscar': 'Pesquisar'
	}

	r = requests.post('https://www.security.cespe.unb.br/VESTUNB_18_2/Consulta1Chamada_d54d97e1/', cookies=cookies, data=payload)


	parsed = BeautifulSoup(r.text, 'html.parser')

	qnt = 1

	x = parsed.find_all('font', attrs={'color':'Black'})
	texto = ""
	if(len(x) == 0):
		bot.sendMessage(id,  name + ' não econtrado')
	else:
		bot.sendMessage(id, 'Resultado para ' + name + ' : ' + str(len(x)//4 - 1) + ' econtrado(s)')
		while(qnt*4 < len(x)):
			nome = str(x[qnt*4])
			nome = nome.replace(nome[:20], '')
			nome = nome[:-7]
			curso = str(x[qnt*4+1])
			curso = curso.replace(curso[:20],'')
			curso = curso[:-7]
			texto += 'Nome: ' + nome + '\nCurso: ' + curso + '\n\n'
			qnt += 1
			
	bot.sendMessage(id, texto)
	bot.sendMessage(id, 'Para mais informações, consulte o site do CESPE:\n https://www.security.cespe.unb.br/VESTUNB_18_2/Consulta1Chamada_d54d97e1/')



def getMessage(message):
	msg = message['text']
	id = message['chat']['id']
	name = message['from']['first_name']

	print('Id :', id, 'Nome :',name, 'Mensagem :', msg)

	func = msg.split(' ', 1)

	if(msg.startswith('/build')):
		getBuild(func[1],id)
	
	if(msg.startswith('/vest')):
		getUnB(func[1],id)

	getPalavrao(msg,id,name)

bot.message_loop(getMessage)

while True:
	pass