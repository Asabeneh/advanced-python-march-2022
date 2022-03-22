from itertools import count
import re

print(dir(re))
# match
# search
# findall
# sub
# split

# match
txt = 'I love people'
match = re.match('i love', txt, re.I)
print(match)

# search
txt = 'It is good to Love each other. love is the best thing in this world.'
print(re.search('love', txt, re.I))


# findall
txt = 'I love people. It is good to love one another. If you love, you will feel great. Love is the greatest thing in this world.'
print(re.findall('love', txt, re.I))

# SUB

new_text = re.sub('[lL]ove', 'like', txt)
print(new_text)

pattern = r'[^a-zA-Z ]'
txt = '''%I@ a%m te%%a%?@%che?%r% a%n%d %% I# l%o%ve te%ach%ing. 
T%?he%re i%s n%o%?th%ing as r%ewarding a%s e%duc%at%i%ng a%n?%d e%m%p%ow%er%ing p%e%o%ple.
I fo%un?d te%a%ching m%ore i%n%t%er%%es%ting t_%h%an any ot$her %jobs. 
D%o%es th?i%s m%ot%iv%a%te %y%o%u to b%e a t%e%a%cher?'''

print(re.sub(pattern, '', txt))

txt = 'I love people. If you look for hate it could be also a. It too quick to jump form love to hate, let just like each other'
pattern = r'love|hate|like'
words = re.findall(pattern, txt)
print(words)


pattern = r'\b[\d]{4}\b'
txt = 'The break can be transformed into broken breaking. I am interest only the basic word break not its different forms 1233 ?$S.SS. Number ae very import some time in a text 1920 or 80 or 15 or 2'
print(re.findall(pattern, txt))

def count_most_frequent_words(txt):
	from collections import Counter
	pattern = r'[^a-zA-Z ]'
	cleaned_text = re.sub(pattern, '', txt )
	words = cleaned_text.lower().split(' ')
	counter = Counter(words)
	return counter

txt = '''
Studies that estimate and rank the most common words in English examine texts written in English. Perhaps the most comprehensive such analysis is one that was conducted against the Oxford English Corpus (OEC), a very large collection of texts from around the world that are written in the English language. A text corpus is a large collection of written works that are organised in a way that makes such analysis easier.

In total, the texts in the Oxford English Corpus contain more than 2 billion words.[1] The OEC includes a wide variety of writing samples, such as literary works, novels, academic journals, newspapers, magazines, Hansard's Parliamentary Debates, blogs, chat logs, and emails.[2]

Another English corpus that has been used to study word frequency is the Brown Corpus, which was compiled by researchers at Brown University in the 1960s. The researchers published their analysis of the Brown Corpus in 1967. Their findings were similar, but not identical, to the findings of the OEC analysis.

According to The Reading Teacher's Book of Lists, the first 25 words in the OEC make up about one-third of all printed material in English, and the first 100 words make up about half of all written English.[3] According to a study cited by Robert McCrum in The Story of English, all of the first hundred of the most common words in English are of Anglo-Saxon origin,[4] except for "people", ultimately from Latin "populus", and "because", in part from Latin "causa".

Some lists of common words distinguish between word forms, while others rank all forms of a word as a single lexeme (the form of the word as it would appear in a dictionary). For example, the lexeme be (as in to be) comprises all its conjugations (is, was, am, are, were, etc.), and contractions of those conjugations.[5] These top 100 lemmas listed below account for 50% of all the words in the Oxford English Corpus.[1]
'''
print(count_most_frequent_words(txt))
txt = '''VENÄJÄN presidentti Vladimir Putin on yrittänyt taivutella Valko-Venäjän itsevaltiasta johtajaa Aljaksandr Lukashenkaa osallistumaan venäläisten rinnalle Ukrainan sotaan.

Valko-Venäjä on toistaiseksi torjunut pyynnön. Se on tarjonnut maataan käytettäväksi vain venäläisille armeijan tukikohtana.

Viime päivinä on raportoitu, miten valkovenäläisiä joukkoja on siirtynyt Ukrainan rajan tuntumaan ja lähelle Puolan rajaa.

Puolustusliitto Naton tiedustelu arvioi maanantaina, että Valko-Venäjän liittyminen näyttää entistä todennäköisemmältä.

PÄÄESIKUNNAN entinen tiedustelupäällikkö, kenraalimajuri evp Pekka Toveri sanoo, että Putin selkeästi painostaa Lukashenkaa ”aivan hulluna”, jotta Valko-Venäjä lähtisi mukaan.

– Jaettu tuska on pienempi tuska ja Putin tarvitsee apua.

Toveri sanoo, ettei Valko-Venäjän asevoimilla sotaa ratkaista.

Valko-Venäjällä on 50 000 sotilaan armeija, joista varsinaisia taistelujoukkoja on vajaa puolet. Sotilaat ovat pääosin varusmiehiä.

Valkovenäläisten kalusto on Toverin mukaan samanlaista kuin venäläisillä, mutta vähän vanhempaa. Kalustoa ei ole modernisoitu samaan tahtiin kuin venäläisillä.

– Periaatteessa heillä on heikompi kalusto.

TOVERI sanoo, että Valko-Venäjän armeijassa on jo nyt nähty kieltäytymisiä ja ilmeisesti eroamisia upseerikunnassa, kun kukaan ei halua lähteä sotimaan. He ovat nähneet, mitä Ukrainassa tapahtuu.

– Kuka nyt sinne lihamyllyyn haluaisi mennä ukrainalaisia vastaan taistelemaan?

Yhden prikaatin komentajan on kerrottu loikanneen Puolaan, ja huhuja liikkuu, että armeijassa olisi ollut muitakin irtisanoutumisia.

Toveri sanoo, että valkovenäläiset eivät haluaisi lähteä taistelemaan Ukrainaan, mutta jos Lukashenka käskee, armeija ehkä yrittää jotain.

– En usko, että se sotaa ratkaisee, koska ukrainalaiset ovat varautuneet tähän ja pitäneet monta viikkoa silmällä tilannetta.

Ukrainalaiset ovat valmiina siihen, että valkovenäläiset lähtevät hyökkäämään Brestin suunnalta ja yrittävät katkaista ukrainalaisten maayhteydet länteen.

– En kauheasti laskisi sen varaan, että valkovenäläiset kauhean pitkälle pääsisivät.

Omat haasteensa tuo se, että Valko-Venäjän ja Ukrainan välillä on Pripetin laaja suoalue. Siinä ei ole monta kohtaa, josta voi hyökätä.

VALKO-VENÄJÄLLÄ on nähty Ukrainan sodan aikana vastarintaa. Valkovenäläiset ovat sabotoineet muun muassa venäläisten junayhteyksiä.

Vastarinnan takia Lukashenka ei todennäköisesti halua lähteä Ukrainaan.

– Lukashenka pelkää, että jos hän hyökkää Ukrainaan, siellä kuolee kasapäin porukkaa. Kansannousu voi lähteä uudestaan liikkeelle, Toveri arvioi.'''



print(count_most_frequent_words(txt))




