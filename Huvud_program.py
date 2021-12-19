from tkinter import *
from Generera_uttryck import *
from Histogram import *
from Rita_level import *

class spel:
    """Skapar GUI och ändrar på fönstret under spelets gång så fönsteret uppdateras för spelaren"""
    def __init__(self, fönster):
        self.fönster = fönster
        self.poäng = 0
        self.försök_lista = [1]


    def skapa_widgets(self):
        """Definierar alla nödvändiga etiketter, knappar, listor och tavlor"""
        self.ram = LabelFrame(self.fönster, width=250, height=480)

        self.Level_label = Label(self.ram, text="Level:", state=DISABLED)
        self.score_label = Label(self.ram, text="Score:", state=DISABLED)
        self.poäng_visare = Label(self.ram, text="0", state=DISABLED)
        self.Timer_label = Label(self.ram, text="Timer:", state=DISABLED)
        self.svårighet_label = Label(self.ram, text="Difficulty:")
        self.tid_visare = Label(self.ram)
        self.uttrycks_form_label = Label(self.ram, text="Välj uttrycks form:")

        # Huvud rutorna definieras
        self.Ruta1 = Label(self.ram, text="uttryck1", state=DISABLED, relief="groove", width=30, height=5)
        self.Ruta_equal = Label(self.ram, text="Equal", state=DISABLED, relief="groove", width=30, height=5)
        self.Ruta2 = Label(self.ram, text="uttryck2", state=DISABLED, relief="groove", width=30, height=5)

        self.time = StringVar()

        self.svårighetsgrad_lista = Listbox(self.ram, width=16, height=3, exportselection=0)
        self.svårighetsgrad_lista.insert(0, "1 - 10", "1 - 100", "1 - 1000")
        self.svårighetsgrad_lista.select_set(0)
        self.uttrycks_form_lista = Listbox(self.ram, width=16, height=2, exportselection=0)
        self.uttrycks_form_lista.insert(0, "Samma räknesätt", "Blanda räknesätt")
        self.uttrycks_form_lista.select_set(0)

        self.Start_knapp = Button(self.ram, text="Start", command=self.Klick, width=13, height=2)
        self.histogram_knapp = Button(self.ram, text="Visa statestik", command=self.Skapa_histogram, width=13, height=1)

        self.Rita_nivå = Canvas(self.ram, width=200, height=15)


    def Placera_allt(self):
        """Placerar ut alla definierade etiketter, knappar, listor och tavlor"""
        self.ram.grid(row=0, column=0)

        self.Level_label.place(x=15, y=20)
        self.score_label.place(x=15, y=50)
        self.poäng_visare.place(x=50, y=50)
        self.Timer_label.place(x=170, y=50)
        self.svårighet_label.place(x=15, y=370)
        self.uttrycks_form_label.place(x=130,y=370)
        self.tid_visare.place(x=205, y=50)

        self.Start_knapp.place(x=130, y=430)
        self.histogram_knapp.place(x=15, y=440)
        self.Rita_nivå.place(x=50, y=20)

        self.svårighetsgrad_lista.place(x=15, y=390)
        self.uttrycks_form_lista.place(x=130, y=390)

        self.Ruta1.place(x=15, y=90)
        self.Ruta_equal.place(x=15, y=190)
        self.Ruta2.place(x=15, y=290)


    def Klick(self):
        """Denna funktion körs när användaren trycker på knappen start.
        Startar spelet genom att ändra tillgängligheten på ett antal widgets från DISABLED till NORMAL. 
        Startar timer. 
        Hämtar vald svårighet och uttrycks form från listorna för att anropa Rita_level klassen."""
        self.Level_label.config(state=NORMAL)
        self.score_label.config(state=NORMAL)
        self.poäng_visare.config(state=NORMAL, text="0")
        self.Timer_label.config(state=NORMAL, bg="SystemButtonFace")
        self.svårighet_label.config(state=DISABLED)
        self.svårighetsgrad_lista.config(state=DISABLED)
        self.uttrycks_form_lista.config(state=DISABLED)
        self.uttrycks_form_label.config(state=DISABLED)
        self.Ruta1.config(state=NORMAL, bg="SystemButtonFace")
        self.Ruta_equal.config(state=NORMAL, bg="SystemButtonFace")
        self.Ruta2.config(state=NORMAL, bg="SystemButtonFace")
        self.Start_knapp.config(state=DISABLED)
        self.histogram_knapp.config(state=DISABLED)
        self.poäng = 0

        # Hämta önkad svårighetsgrad och uttrycks_form
        self.vald_svårighet()
        self.vald_uttrycks_form()

        # starta timer
        self.tid = 11
        self.timer()  

        # SKriver ut uttrycket i Rutorna
        self.Klickbara_etiketter()
        self.skapa_uttryck()

        # ritar kvadrater som representerar level
        self.Rita_nivå.delete("all")
        self.level_up()


    def Avsluta_spel(self):
        """Avslutar spelet med given anledning till förlust. 
        Målar korrekt svar med grönt och fel svar med röd."""
        self.Level_label.config(state=DISABLED)
        self.score_label.config(state=DISABLED)
        self.poäng_visare.config(state=DISABLED)
        self.Timer_label.config(state=DISABLED)
        self.svårighet_label.config(state=NORMAL)
        self.svårighetsgrad_lista.config(state=NORMAL)
        self.uttrycks_form_label.config(state=NORMAL)
        self.uttrycks_form_lista.config(state=NORMAL)
        self.Ruta1.config(state=DISABLED)
        self.Ruta_equal.config(state=DISABLED)
        self.Ruta2.config(state=DISABLED)
        self.Start_knapp.config(state=NORMAL)
        self.histogram_knapp.config(state=NORMAL)

        self.Ruta1.unbind("<Button-1>")
        self.Ruta_equal.unbind("<Button-1>")
        self.Ruta2.unbind("<Button-1>")

        self.anledning_till_förlust()
        self.ram.after_cancel(self.stopp_tid_räkning)
        self.Resultat_till_fil()


    def Resultat_till_fil(self):
        with open(r'C:\Users\samer\source\repos\Pyhton spel\Matematik spel\poäng per spel.txt', 'a', encoding='utf-8') as fil:
            fil.write(str(self.poäng) + "\n")


    def anledning_till_förlust(self):
        """Skriver ut varför spelaren förlorade både med text och färger"""
        if self.tid <= 0:
            self.poäng_visare.config(text="Förlust, Tiden är ute")
            self.Timer_label.config(bg="red")
        else:
            self.poäng_visare.config(text="Förlust, Fel svar")

        if self.uträkning_ruta1 > self.uträkning_ruta2:
            self.Ruta1.config(bg="green")
        elif self.uträkning_ruta1 == self.uträkning_ruta2:
            self.Ruta_equal.config(bg="green")
        else:
            self.Ruta2.config(bg="green")


    def level_up(self):
        """uppdaterar antal ritna kvadrater som ska representera spelarens level"""
        Level = Rita_level(self.poäng, self.Rita_nivå, self.level) 
        Level.Rita_kvadrat()


    def timer(self):
        """Skapar timer. 
        Om timern når 0 anropas avsluta_spel och anledning_till_förlust."""  
        self.tid = self.tid - 1
        
        self.time.set(str(self.tid))
        self.tid_visare.config(textvariable=self.time)
            
        self.stopp_tid_räkning = self.ram.after(1000, self.timer)

        if self.tid <= 0:
            self.ram.after_cancel(self.stopp_tid_räkning)
            self.Avsluta_spel()


    def vald_svårighet(self):
        """Hämtar vald svårighet från listan"""
        vald_svårighet = self.svårighetsgrad_lista.curselection()
        self.svårighet = self.svårighetsgrad_lista.get(vald_svårighet[0])
        if self.svårighet == "1 - 10":
           self.svårighet = 10
        elif self.svårighet == "1 - 100":
           self.svårighet = 100
        else:
            self.svårighet = 1000


    def vald_uttrycks_form(self):
        """Hämtar vald uttrycks form"""
        uttrycks_form = self.uttrycks_form_lista.curselection()
        self.uttrycks_form = self.uttrycks_form_lista.get(uttrycks_form[0])  


    def Klickbara_etiketter(self):
        """kopplar Ruta1, Ruta_equal och Ruta2 till ett klick commando såsom för knappar"""
        self.Ruta1.bind("<Button-1>", self.Ruta1_klick)
        self.Ruta_equal.bind("<Button-1>", self.Ruta_equal_klick)
        self.Ruta2.bind("<Button-1>", self.Ruta2_klick)


    def Ruta1_klick(self, event):
        """Om uttryck1 är större än uttryck 2 körs Rätt_svar annars avsluta_spel"""
        if self.uträkning_ruta1 > self.uträkning_ruta2:
            self.Rätt_svar()

        else:
            self.Ruta1.config(bg="red")
            self.Avsluta_spel()


    def Ruta_equal_klick(self, event):
        """Om uttryck1 är lika stor som uttryck 2 körs Rätt_svar annars avsluta_spel"""
        if self.uträkning_ruta1 == self.uträkning_ruta2:
            self.Rätt_svar()

        else:
            self.Ruta_equal.config(bg="red")
            self.Avsluta_spel()


    def Ruta2_klick(self, event):
        """Om uttryck1 är mindre än uttryck 2 körs Rätt_svar annars avsluta_spel"""    
        if self.uträkning_ruta1 < self.uträkning_ruta2:
            self.Rätt_svar()

        else:
            self.Ruta2.config(bg="red")
            self.Avsluta_spel()


    def Rätt_svar(self):
        """Anropas av Klick på Ruta1, Ruta_equal och Ruta2"""
        self.poäng += 1
        self.poäng_visare.config(text=self.poäng)
        
        self.skapa_uttryck()
        self.level_up()
        self.återställ_tid_räkningen()


    def skapa_uttryck(self):
        """Skapar nya uttryck och skriver ut de i Ruta1 och Ruta2"""
        if str(self.poäng)[:-1] == "":
            self.level = 1
        else:
            self.level = int(str(self.poäng)[:-1])+1

        uttryck = Generera_uttryck(self.svårighet, self.level, self.uttrycks_form)
        self.uttryck_ruta1, self.uttryck_ruta2, self.uträkning_ruta1, self.uträkning_ruta2 = uttryck.Generera_slump_värden()
        self.Ruta1.config(text=self.uttryck_ruta1)
        self.Ruta2.config(text=self.uttryck_ruta2)


    def Skapa_histogram(self):
        histogram = Histogram()
        histogram.Rita_histogram()


    def återställ_tid_räkningen(self):
        """Om spelaren svarat rätt så återsälls timern"""
        self.tid = 11
        if self.poäng >= 40:
            self.tid = 7
        elif self.poäng >= 30:
          self.poäng = 8
        elif self.poäng >= 20:
            self.tid = 9
        elif self.poäng >= 10:
            self.tid = 10


def Huvudprogram():
    """Genrerar GUI genom anrop till nödvädiga metoder"""
    fönster = Tk()
    spel_meny = spel(fönster)
    spel_meny.skapa_widgets()
    spel_meny.Placera_allt()

    fönster.mainloop()


if __name__ == "__main__":
    Huvudprogram()
