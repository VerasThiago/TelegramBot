import requests                                                                                                                                                                                                    
from bs4 import BeautifulSoup
import telepot

bot = telepot.Bot("573177973:AAHRwV6IsmBSGllKx8MZQ_3PdonRqHB_aN0")

palavroes = ['Alienado', 'Animal de Teta', 'Anormal', 'Argentino', 'Arregassado', 'Arrombado', 'Babaca', 'Baitola', 'Baleia', 'Barril', 'Benfiquista', 'Biba', 'Bicha', 'BIOS', 'Biroska', 'Bobo', 'Bocal', 'bolagato', 'Boqueteiro', 'Bosta', 'Buceta', 'Bundao', 'Burro', 'Cabaco', 'Cacete', 'Cadelona', 'Cafona', 'Cambista', 'Capiroto', 'Caralho', 'Catraia', 'Cepo', 'Cocodrilo', 'Cocozento', 'Cu', 'DebilMental', 'Demente', 'Desciclope', 'Desgracado', 'Drogado', 'EGUENORANTE', 'Endemoniado', 'Energumeno', 'Enfianocu', 'EngoleRola', 'Escroto', 'Esdruxulo', 'Esporrado', 'Estigalhado', 'Estrume', 'Estrunxado', 'Estupido', 'FDP', 'Fidumaegua', 'FilhodaPuta', 'Fiofo', 'Foda', 'Fuder', 'Fudido', 'Fulera', 'Galinha', 'Gambiarra', 'GeisyArruda', 'Gnu', 'Gonorreia', 'GordoEscroto', 'Gozado', 'Herege', 'Idiota', 'Ignorante', 'Imbecil', 'Imundo', 'Inascivel', 'Inseto', 'Invertebrado', 'Jacu', 'Jegue', 'Jumento', 'KCT', 'Komodo', 'Ku', 'lazarento', 'Lazaro!', 'Leproso', 'lerdo', 'lesma', 'Lezado', 'lico', 'Limpezaanal', 'lixo', 'lombriga', 'Macaco', 'MariMoon', 'Merda', 'Meretriz', 'MiolodeCu', 'Mocorongo', 'MontedeMerda', 'Morfetico', 'Mulambo', 'n00b', 'Nazista', 'Nerd', 'Newbie', 'Nhaca', 'Nonsense', 'Ogro', 'Olhodocu', 'OlhoGordo', 'Otario', 'Palhaco', 'Panaca', 'Paraguaio', 'Passaralho', 'PauNoCu', 'Periquita', 'Pimenteira', 'Pipoca', 'Piranha', 'Piroca', 'Pistoleira', 'Porra', 'prostituta', 'Punheta', 'Puta', 'PutaQuePariu', 'Quasimodo', 'Quenga', 'Quirguistao', 'Rampero', 'Rapariga', 'Raspadinha', 'Retardado', 'Rusguento', 'Sanguesuga', 'Sujo', 'Tapado', 'Tarado', 'Tesao', 'Tetuda', 'Tetudo', 'Tosco', 'Tragado', 'Travesti', 'Trepadeira', 'Troglodita', 'Tnc', 'Urubu', 'Vaca', 'Vadia', 'Vagabundo', 'Vagaranha', 'Vaiamerda', 'vaisefuder', 'Vaitomarnocu', 'Vascaino', 'Verme', 'Viado', 'Xavasca', 'Xereca', 'Xixizento', 'Xoxota', 'Xupetinha', 'Xupisco', 'Xurupita', 'Xuxexo', 'XXT', 'XXX', 'ZeBuceta', 'Ziguizira', 'Zina', 'Zoado', 'Zoiudo', 'Zoneira', 'Zuado', 'Zuera', 'Zulu', 'Zureta']
for i in range(len(palavroes)):
	palavroes[i] = palavroes[i].lower()



def getPalavrao(msg,id):
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

def getMessage(message):
	msg = message['text']
	id = message['chat']['id']
	name = message['from']['first_name']

	print('Id :', id, 'Nome :',name, 'Mensagem :', msg)
	

	func = msg.split(' ',1)

	#if(func[0] == '/build'):
	#	getBuild(func[1],id)
	
	getPalavrao(msg,id)



	




	

bot.message_loop(getMessage)

while True:
	pass