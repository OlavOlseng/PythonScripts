from sys import stdin, stderr

# kapasiteter er den opprinnelige kapasitetsmatrisen, som inneholder n x n elementer (hvor n er antall noder).
# startrom er en liste med indeksene til nodene som tilsvarer startrommene.
# utganger er en liste med indeksene til nodene som tilsvarer utgangene.

def antallIsolerteStier(capacities, sources, sinks):
	# Du kan bruke metoden finnFlytsti for aa forenkle oppgaven.
	# SKRIV DIN KODE HER
	n = len(capacities)
	if n <= 1:
		return n
	Fout = [0]*n
	Fin =  [0]*n
	paths = []
	for source in sources:
		for sink in sinks:
			if source == sink:
				continue
			path = finnFlytsti(source, sink, Fin, Fout, capacities)
			if not path:
				continue
			for flow in range(len(path)-1):
				Fin[path[flow+1]] += 1
				Fout[path[flow]] += 1
			paths.append(path)
	return len(paths)
	
# Finner en sti fra noden med indeks 'kilde' til noden med indeks 'sluk'
# med ledig kapasitet i et flytnettverk med flyt F og kapasitet C.
# Returnerer en liste hvor foerste element er indeksen til en av startnodene, 
# siste element er indeksen til en av utgangene, og elementene imellom er 
# indeksene til de andre nodene paa veien som ble funnet, i riktig rekkefoelge.
# Eksempel: en sti fra startnoden 4 til node 3, node 9, node 7 og til slutt til 
# utgangen 12 vil representeres som [4, 3, 9, 7, 12].

def finnFlytsti(kilde, sluk, Fin, Fout, C):
	n = len(Fin)
	oppdaget = [False] * n
	forelder = [None] * n
	koe = [kilde]
	while koe:
		node = koe.pop(0)
		if node == sluk:
			# Har funnet sluken, lager en array med passerte noder
			sti = []
			i = node
			while True:
				sti.append(i)
				if i == kilde:
					break
				i = forelder[i]
			sti.reverse()
			return sti;
		for nabo in range(n):
			if not oppdaget[nabo] and Fin[nabo] < C[node][nabo] and Fout[node] < 1:
				koe.append(nabo);
				oppdaget[nabo] = True;
				forelder[nabo] = node;
	return None

def start():
	noder, _, _ = [int(x) for x in stdin.readline().split()]
	startrom = [int(x) for x in stdin.readline().split()]
	utganger = [int(x) for x in stdin.readline().split()]
	nabomatrise = []
	for linje in stdin:
		naborad = [int(nabo) for nabo in linje.split()]
		nabomatrise.append(naborad)
	print antallIsolerteStier(nabomatrise, startrom, utganger)

start()