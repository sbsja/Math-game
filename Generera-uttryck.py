from random import randint

class Generera_uttryck:
    """Genererar två uttryck och returnerar uttryck1 och uttryck2 dessutom resultaten av uttryck1 och uttryck2"""
    def __init__(self, svårighet, level, uttrycks_form):
        self.svårighet = svårighet
        self.level = level
        self.uttrycks_form = uttrycks_form
        self.slump_tals_lista = []
        self.räknesätt_lista = []
        self.Text_ruta1 = ""
        self.Text_ruta2 = ""

    
    def Generera_slump_värden(self):
        """Generarar slump tal och slump tecken där teckenen översätts enligt unicode till +,-,/,*"""
        for slump_tal in range(4+(self.level-1)*2):
            self.slump_tals_lista.append(randint(1, self.svårighet))
        for slump_räknesätt in range(4+(self.level-1)*2):
            self.räknesätt_lista.append(randint(42, 47))    
        
        self.Fel_tecken()
        self.Skriva_text_i_rutorna()
        self.Resultat_från_Uträkning()
        return self.uttryck_1, self.uttryck_2, self.Uträkning1, self.Uträkning2
        
    
    def Fel_tecken(self):
        """Tar bort de nummren som inte mostvarar ett räknesätt enligt unicode"""
        for slump_räknesätt in range(len(self.räknesätt_lista)):
            while self.räknesätt_lista[slump_räknesätt] == 44 or self.räknesätt_lista[slump_räknesätt] == 46:
                self.räknesätt_lista[slump_räknesätt] = randint(42, 47)
        
        if self.level == 1:
            for tecken in range(0, len(self.räknesätt_lista)-1, 2):
                self.räknesätt_lista[tecken+1] = self.räknesätt_lista[tecken]

    
    def Skriva_text_i_rutorna(self):
        """Skriver ut uttrycken i stäng form från de genererade strängar"""
        uttryck = []
        if self.uttrycks_form == "Blanda räknesätt":
            uttryck = self.Blanda_räknesätt(uttryck, self.slump_tals_lista, self.räknesätt_lista)
        
        if self.uttrycks_form == "Samma räknesätt":
            uttryck = self.Bara_ett_räknesätt(uttryck, self.slump_tals_lista, self.räknesätt_lista)

        self.slå_ihop_listor(uttryck)
    
    
    def Bara_ett_räknesätt(self, uttryck, tal_lista, tecken_lista):
        """Sätter ihop tal listan med det första teckenet från räknesätt listan till en lista med hela uttrycken"""
        for tal in tal_lista:
            uttryck.append(str(tal))
            uttryck.append(chr(tecken_lista[0]))
        return uttryck
            
    
    def Blanda_räknesätt(self, uttryck, tal_lista, tecken_lista):
        """Sätter ihop tal lista med tecken listan till en lista med hela uttryck1 och uttryck2"""
        for elem in range(len(tal_lista)):
           uttryck.append(str(tal_lista[elem]))
           uttryck.append(chr(tecken_lista[elem]))
        return uttryck 

    
    def slå_ihop_listor(self, uttryck):
        """Delar upp listan med båda uttrycken till två listor och slår ihop listan till en sträng"""    
        self.uttryck_1 = " ".join(uttryck[:len(uttryck)//2][:-1])
        self.uttryck_2 = " ".join(uttryck[len(uttryck)//2:][:-1])

    
    def Resultat_från_Uträkning(self):
        """Beräknar resultatet från uttrycken"""
        self.Uträkning1 = eval(self.uttryck_1)
        self.Uträkning2 = eval(self.uttryck_2)

if __name__ == "__main__": 
    vad = Generera_uttryck(10, 6, "Blanda räknesätt")
    vad.Generera_slump_värden()
