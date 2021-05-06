################################################################################
# Progetto: Studio della Cirulla                                               #
# Autore: Paolo Pertino                                                        #
#                                                                              #
# Descrizione: il progetto si pone l'obiettivo di simulare partite del famoso  #
#              gioco di carte ligure della cirulla. Dato un numero elevato di  #
#              simulazioni, siamo interessati ad evidenziare le probabilità    #
#              di verificarsi di eventi di interesse, quali l'ottenere un      #
#              un decino, la bussata e la distribuzione di un tavolo iniziale  #
#              "fortunato".                                                    #
################################################################################

import random
import os

################################################################################
#                             OGGETTI DI INTERESSE                             #
################################################################################
class mazzo():
    numeroDiCarte = 40

    def __init__(self, valCarte, semiCarte):
        self.valori = valCarte
        self.semi = semiCarte
        self.mazzoOrdinato = []

        for valore in self.valori:
            for seme in self.semi:
                nuovaCarta = [valore,seme]
                self.mazzoOrdinato.append(nuovaCarta)


class partita():
    carteUscite = []
    tavolaIniziale = []
    giocatore1 = []
    giocatore2 = []

    def __init__(self,mazzoPartita):
        self.mazzoMischiato = mazzoPartita.mazzoOrdinato

    def prendiCarta(self):
        flag = 0

        while(flag == 0):
            cartaEstratta = random.choice(self.mazzoMischiato)

            if(not(cartaEstratta in self.carteUscite)):
                self.carteUscite.append(cartaEstratta)
                flag = 1

                return cartaEstratta

    def iniziaPartita(self):
        self.carteUscite = []
        self.tavolaIniziale = []
        self.giocatore1 = []
        self.giocatore2 = []
        random.shuffle(self.mazzoMischiato)

    def primaMano(self):
        for i in range(3):
            self.giocatore1.append(self.prendiCarta())
            self.giocatore2.append(self.prendiCarta())

        for i in range(4):
            self.tavolaIniziale.append(self.prendiCarta())

    def secondaMano(self):
        self.giocatore1 = []
        self.giocatore2 = []

        for i in range(3):
            self.giocatore1.append(self.prendiCarta())
            self.giocatore2.append(self.prendiCarta())

    def terzaMano(self):
        self.giocatore1 = []
        self.giocatore2 = []

        for i in range(3):
            self.giocatore1.append(self.prendiCarta())
            self.giocatore2.append(self.prendiCarta())

    def quartaMano(self):
        self.giocatore1 = []
        self.giocatore2 = []

        for i in range(3):
            self.giocatore1.append(self.prendiCarta())
            self.giocatore2.append(self.prendiCarta())

    def quintaMano(self):
        self.giocatore1 = []
        self.giocatore2 = []

        for i in range(3):
            self.giocatore1.append(self.prendiCarta())
            self.giocatore2.append(self.prendiCarta())

    def sestaMano(self):
        self.giocatore1 = []
        self.giocatore2 = []

        for i in range(3):
            self.giocatore1.append(self.prendiCarta())
            self.giocatore2.append(self.prendiCarta())

################################################################################
#                                  FUNZIONI                                    #
################################################################################
################################################################################
# - clearConsole()                                                             #
#       Pulisce la console.                                                    #
# - trovaDecino(manoGiocatore1,manoGiocatore2)                                 #
#       Date in ingresso le mani di carte del giocatore 1 e del giocatore 2,   #
#       dove con mano intendiamo una lista di 3 carte, la funzione restituisce #
#       il numero di decini della mano corrente.                               #
# - trovaLuckyTable(piatto)                                                    #
#       La funzione riceve in ingresso il piatto iniziale, composto da 4 carte #
#       e restituisce 1 se esso è un piatto fortunato, altrimenti 0            #
# - trovaBussata(manoGiocatore1,manoGiocatore2)                                #
#       Date in ingresso le mani di carte del giocatore 1 e del giocatore 2,   #
#       dove con mano intendiamo una lista di 3 carte,                         #
#       la funzione calcola se i giocatori possono bussare:                    #
#       Se entrambi possono bussare la funzione restituisce 2, se solo uno dei #
#       due, restituisce 1, altrimenti 0. (NB: in caso il calcolo venisse      #
#       effettuato solo su un giocatore, la funzione restituisce o 0 o 1)      #
################################################################################
def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

def trovaDecino(manoGiocatore1,manoGiocatore2):
    deciniTrovati = 0
    if((manoGiocatore1[0][0] == manoGiocatore1[1][0] and manoGiocatore1[1][0] == manoGiocatore1[2][0]) or ((manoGiocatore1[0][0] == manoGiocatore1[1][0] or manoGiocatore1[0][0] == manoGiocatore1[2][0] or manoGiocatore1[1][0] == manoGiocatore1[2][0]) and (any(["7","Cuori"] == carta for carta in manoGiocatore1) and not(["7","Quadri"] in manoGiocatore1) and not(["7","Fiori"] in manoGiocatore1) and not(["7","Picche"] in manoGiocatore1))) or (manoGiocatore1[0][0] == "7" and manoGiocatore1[1][0] == "7" and manoGiocatore1[2][0] == "7")):
        deciniTrovati += 1
    if(((manoGiocatore2[0][0] == manoGiocatore2[1][0] and manoGiocatore2[1][0] == manoGiocatore2[2][0]) or ((manoGiocatore2[0][0] == manoGiocatore2[1][0] or manoGiocatore2[0][0] == manoGiocatore2[2][0] or manoGiocatore2[1][0] == manoGiocatore2[2][0]) and (any(["7","Cuori"] == carta for carta in manoGiocatore2) and not(["7","Quadri"] in manoGiocatore2) and not(["7","Fiori"] in manoGiocatore2) and not(["7","Picche"] in manoGiocatore2))) or (manoGiocatore2[0][0] == "7" and manoGiocatore2[1][0] == "7" and manoGiocatore2[2][0] == "7")) and flagProbabilitaDoppia):
        deciniTrovati += 1

    return deciniTrovati

def trovaLuckyTable(piatto):
    isLucky = 0
    somma = 0

    # Converto J,Q,K,A in valori
    for i in range(4):
        if(piatto[i][0] == "A"):
            piatto[i][0] = "1"
        if(piatto[i][0] == "J"):
            piatto[i][0] = "8"
        if(piatto[i][0] == "Q"):
            piatto[i][0] = "9"
        if(piatto[i][0] == "K"):
            piatto[i][0] = "10"

    # Controllo le somme dei valori delle carte.
    for i in range(4):
        somma += int(piatto[i][0])

    if(any(["7","Cuori"] == carta for carta in piatto)):
        if(somma - 7 < 15 or somma - 7 > 19):
            isLucky = 1
    else:
        if(somma == 15 or somma == 30):
            isLucky = 1

    return isLucky

def trovaBussata(manoGiocatore1,manoGiocatore2):
    isBussata = 0
    somma1 = 0
    somma2 = 0

    if(trovaDecino(manoGiocatore1,manoGiocatore2) >= 1):
        return 1

    for i in range(3):
        if(manoGiocatore2[i][0] == "A"):
            manoGiocatore2[i][0] = "1"
        if(manoGiocatore2[i][0] == "J"):
            manoGiocatore2[i][0] = "8"
        if(manoGiocatore2[i][0] == "Q"):
            manoGiocatore2[i][0] = "9"
        if(manoGiocatore2[i][0] == "K"):
            manoGiocatore2[i][0] = "10"
        if(manoGiocatore1[i][0] == "A"):
            manoGiocatore1[i][0] = "1"
        if(manoGiocatore1[i][0] == "J"):
            manoGiocatore1[i][0] = "8"
        if(manoGiocatore1[i][0] == "Q"):
            manoGiocatore1[i][0] = "9"
        if(manoGiocatore1[i][0] == "K"):
            manoGiocatore1[i][0] = "10"

    for i in range(3):
        somma1 += int(manoGiocatore1[i][0])
        somma2 += int(manoGiocatore2[i][0])

    if(any(["7","Cuori"] == carta for carta in manoGiocatore1)):
        if(somma1-7 < 9):
            # print(manoGiocatore1)
            isBussata += 1
    else:
        if(somma1 <= 9):
            isBussata += 1
            # print(manoGiocatore1)

    if(flagProbabilitaDoppia):
        if(any(["7","Cuori"] == carta for carta in manoGiocatore2)):
            if(somma2-7 < 9):
                # print(manoGiocatore2)
                isBussata += 1
        else:
            if(somma2 <= 9):
                isBussata += 1
                # print(manoGiocatore2)

    return isBussata

################################################################################
#                                   MAIN                                       #
################################################################################
################################################################################
# Inizializzazione delle proprietà delle carte, del mazzo e della partita.     #
################################################################################
valoreCarta = ["A","2","3","4","5","6","7","J","Q","K"]
semeCarta = ["Quadri","Cuori","Fiori","Picche"]

mazzoDiCarte = mazzo(valoreCarta,semeCarta)
partitaCirulla = partita(mazzoDiCarte)

################################################################################
# Inizializzo parametri della simulazione:                                     #
#   1. Richiedo quante partite voglio simulare;                                #
#   2. Richiedo per quante volte voglio effettuare la simulazione;             #
#   3. Richiedo se le probabilità di interesse devono essere calcolate sul     #
#      singolo giocatore o sulla coppia di giocatori.                          #
#   4. Richiedo se l'utente vuole visualizzare gli output.                     #
################################################################################
clearConsole()
numeroPartiteDaSimulare = int(input('Inserisci quante partite vuoi simulare : '))
clearConsole()
numeroTotaleSimulazioni = int(input(f'Inserisci per quante volte vuoi simulare {numeroPartiteDaSimulare} partite: '))
clearConsole()
flagProbabilitaDoppia = bool(int(input('Vuoi calcolare la probabilità del verificarsi degli eventi di interesse per un singolo giocatore o per la coppia ?\n0. Inserisci 0 per calcolare le probabilità riferite al singolo giocatore.\n1. Inserisci 1 per calcolare le probabilità riferite alla coppia di giocatori.\nScelta: ')))
clearConsole()
flagOutput = bool(int(input('Vuoi visualizzare gli output intermedi?\n0. Inserisci 0 per non visualizzare output intermedi.\n1. Inserisci 1 per visualizzare output intermedi (SCONSIGLIATO PER SIMULAZIONI GRANDI)\nScelta: ')))
clearConsole()

################################################################################
# Vengono ora effettuate le simulazioni.                                       #
################################################################################

for j in range(numeroTotaleSimulazioni):
    print("----------------------------------------------")
    #Variabili di ausilio per il calcolo delle probabilità
    decino = 0
    bussata = 0
    numeroPartiteSenzaBussate = 0
    numeroDeciniTotale = 0
    numeroDeciniSingolaMano = 0
    numeroBussateTotale = 0
    numeroBussateSingolaMano = 0
    numeroLuckyTable = 0

    for i in range(numeroPartiteDaSimulare):
        numeroBussatePartita = 0
        partitaCirulla.iniziaPartita()
        partitaCirulla.primaMano()

        if(flagOutput): print(f'-------- PARTITA NUMERO {i+1} -----------')
        if(flagOutput): print(f'Tavola: {partitaCirulla.tavolaIniziale} \n\n Giocatore 1: {partitaCirulla.giocatore1} \n\n Giocatore 2: {partitaCirulla.giocatore2} \n\n Carte uscite: {partitaCirulla.carteUscite}')

        decino = trovaDecino(partitaCirulla.giocatore1, partitaCirulla.giocatore2)
        bussata = trovaBussata(partitaCirulla.giocatore1,partitaCirulla.giocatore2)
        numeroDeciniTotale += decino
        numeroDeciniSingolaMano += decino
        numeroBussateSingolaMano += bussata
        numeroBussateTotale += bussata
        numeroBussatePartita += bussata
        numeroLuckyTable += trovaLuckyTable(partitaCirulla.tavolaIniziale)

        partitaCirulla.secondaMano()
        numeroDeciniTotale += trovaDecino(partitaCirulla.giocatore1, partitaCirulla.giocatore2)
        bussata = trovaBussata(partitaCirulla.giocatore1,partitaCirulla.giocatore2)
        numeroBussateTotale += bussata
        numeroBussatePartita += bussata
        if(flagOutput): print(f'Giocatore 1: {partitaCirulla.giocatore1} \n\n Giocatore 2: {partitaCirulla.giocatore2} \n\n Carte uscite: {partitaCirulla.carteUscite}')

        partitaCirulla.terzaMano()
        numeroDeciniTotale += trovaDecino(partitaCirulla.giocatore1, partitaCirulla.giocatore2)
        bussata = trovaBussata(partitaCirulla.giocatore1,partitaCirulla.giocatore2)
        numeroBussateTotale += bussata
        numeroBussatePartita += bussata
        if(flagOutput): print(f'Giocatore 1: {partitaCirulla.giocatore1} \n\n Giocatore 2: {partitaCirulla.giocatore2} \n\n Carte uscite: {partitaCirulla.carteUscite}')

        partitaCirulla.quartaMano()
        numeroDeciniTotale += trovaDecino(partitaCirulla.giocatore1, partitaCirulla.giocatore2)
        bussata = trovaBussata(partitaCirulla.giocatore1,partitaCirulla.giocatore2)
        numeroBussateTotale += bussata
        numeroBussatePartita += bussata
        if(flagOutput): print(f'Giocatore 1: {partitaCirulla.giocatore1} \n\n Giocatore 2: {partitaCirulla.giocatore2} \n\n Carte uscite: {partitaCirulla.carteUscite}')

        partitaCirulla.quintaMano()
        numeroDeciniTotale += trovaDecino(partitaCirulla.giocatore1, partitaCirulla.giocatore2)
        bussata = trovaBussata(partitaCirulla.giocatore1,partitaCirulla.giocatore2)
        numeroBussateTotale += bussata
        numeroBussatePartita += bussata
        if(flagOutput): print(f'Giocatore 1: {partitaCirulla.giocatore1} \n\n Giocatore 2: {partitaCirulla.giocatore2} \n\n Carte uscite: {partitaCirulla.carteUscite}')

        partitaCirulla.sestaMano()
        numeroDeciniTotale += trovaDecino(partitaCirulla.giocatore1, partitaCirulla.giocatore2)
        bussata = trovaBussata(partitaCirulla.giocatore1,partitaCirulla.giocatore2)
        numeroBussateTotale += bussata
        numeroBussatePartita += bussata
        if(flagOutput):
            print(f'Giocatore 1: {partitaCirulla.giocatore1} \n\n Giocatore 2: {partitaCirulla.giocatore2} \n\n Carte uscite: {partitaCirulla.carteUscite}')
            print("------------------------------------------")

        if(numeroBussatePartita == 0):
            numeroPartiteSenzaBussate += 1

    print(f'Numero decini totali: {numeroDeciniTotale}')
    print(f'Probabilità decini singola mano: {numeroDeciniSingolaMano * 100/numeroPartiteDaSimulare}')
    print(f'Probabilità decini totale: {numeroDeciniTotale * 100/numeroPartiteDaSimulare}')
    print(f'\nNumero bussate totali: {numeroBussateTotale}')
    print(f'Numero partite senza bussate: {numeroPartiteSenzaBussate}')
    print(f'Probabilità bussata singola mano: {numeroBussateSingolaMano * 100/numeroPartiteDaSimulare}')
    print(f'Probabilità bussate totali: {numeroBussateTotale * 100/numeroPartiteDaSimulare}')
    print(f'Probabilità partite senza bussate: {numeroPartiteSenzaBussate*100/numeroPartiteDaSimulare}')
    print(f'\nNumero Lucky Table totali: {numeroLuckyTable}')
    print(f'Probabilità lucky table: {numeroLuckyTable * 100/numeroPartiteDaSimulare}')
