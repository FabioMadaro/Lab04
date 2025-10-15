from cabina import Cabina
from passeggero import Passeggero

class Crociera:
    def __init__(self, nome):
        """Inizializza gli attributi e le strutture dati"""
        # TODO
        self.cabine = []
        self.passeggeri = []

    """Aggiungere setter e getter se necessari"""
    # TODO

    def carica_file_dati(self, file_path):
        """Carica i dati (cabine e passeggeri) dal file"""
        # TODO
        try:
            file = open(file_path, "r", encoding="utf-8")
        except FileNotFoundError:
            return None

        for line in file:
            campi = line.split(",")
            if len(campi) == 3:
                codice = campi[0]
                nome = campi[1]
                cognome = campi[2]
                passeggero = Passeggero(codice, nome, cognome)
                self.passeggeri.append(passeggero)
            else:
                codice = campi[0]
                letti = campi[1]
                ponte = campi[2]



    def assegna_passeggero_a_cabina(self, codice_cabina, codice_passeggero):
        """Associa una cabina a un passeggero"""
        # TODO

    def cabine_ordinate_per_prezzo(self):
        """Restituisce la lista ordinata delle cabine in base al prezzo"""
        # TODO


    def elenca_passeggeri(self):
        """Stampa l'elenco dei passeggeri mostrando, per ognuno, la cabina a cui è associato, quando applicabile """
        # TODO

