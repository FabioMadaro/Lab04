from cabina import Cabina
from passeggero import Passeggero

class Crociera:
    def __init__(self, nome):
        """Inizializza gli attributi e le strutture dati"""
        # TODO
        self.nome = nome
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
            campi = line.strip().split(",")
            codice = campi[0]
            if codice[0:3] == "CAB":
                if len(campi) == 4:
                        cabina = Cabina(campi[0], campi[1], campi[2], campi[3])
                else:
                    cabina = Cabina(campi[0], campi[1], campi[2], campi[3], campi[4])
                self.cabine.append(cabina)
            elif codice[0] == "P":
                passeggero = Passeggero(campi[0], campi[1], campi[2])
                self.passeggeri.append(passeggero)


    def assegna_passeggero_a_cabina(self, codice_cabina, codice_passeggero):
        """Associa una cabina a un passeggero"""
        # TODO

        cabina = None
        passeggero = None

        for c in self.cabine:
            if c.codice == codice_cabina:
                cabina = c
                break

        for p in self.passeggeri:
            if p.codice == codice_passeggero:
                passeggero = p
                break

        if cabina is None:
            raise Exception(f"Errore: la cabina '{codice_cabina}' non esiste.")
        if passeggero is None:
            raise Exception(f"Errore: il passeggero '{codice_passeggero}' non esiste.")
        if not cabina.disponibile:
            raise Exception(f"Errore: la cabina '{codice_cabina}' è già occupata.")
        if passeggero.cabina is not None:
            raise Exception(
                f"Errore: il passeggero '{passeggero.nome} {passeggero.cognome}' ha già una cabina assegnata.")

        passeggero.cabina = cabina
        cabina.disponibile = False

        print(f"{passeggero.nome} {passeggero.cognome} assegnato alla cabina {cabina.codice}.")

    def cabine_ordinate_per_prezzo(self):
        """Restituisce la lista ordinata delle cabine in base al prezzo"""
        # TODO

        return sorted(self.cabine, key=lambda c: c.sovrapprezzo())

    def elenca_passeggeri(self):
        """Stampa l'elenco dei passeggeri mostrando, per ognuno, la cabina a cui è associato, quando applicabile """
        # TODO

        for p in self.passeggeri:
            print(p)



