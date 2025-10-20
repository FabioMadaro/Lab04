class Cabina:
    def __init__(self, codice, letti, ponte, prezzo_base, extra = None):
        self.codice = codice
        self.letti = int(letti)
        self.ponte = int(ponte)
        self.prezzo_base = float(prezzo_base)
        self.extra = extra
        self.disponibile = True

    def tipo(self):
        if self.extra is None:
            return "Standard"
        elif str(self.extra).isdigit():
            return "Animali"
        else:
            return f"Deluxe ({self.extra})"

    def sovrapprezzo(self):
        if self.extra is None:
            prezzo = self.prezzo_base
        elif str(self.extra).isdigit():
            max_animali = int(self.extra)
            prezzo = self.prezzo_base * (1 + 0.10 * max_animali)
        else:
            prezzo = self.prezzo_base * 1.20

        return prezzo


    def __str__(self):
        if self.disponibile:
            stato = "Disponibile"
        else:
            stato = "Occupata"

        tipo_cabina = self.tipo()
        prezzo = self.sovrapprezzo()

        base = f"{self.codice}: {tipo_cabina} | {self.letti} letti - ponte {self.ponte} - prezzo {prezzo}€"

        if self.extra is None:
            descrizione = f"{base} - {stato}"
        elif self.extra.isdigit():
            descrizione = f"{base} - Max Animali: {self.extra} - {stato}"
        else:
            descrizione = f"{base} - Stile: {self.extra} - {stato}"

        return descrizione