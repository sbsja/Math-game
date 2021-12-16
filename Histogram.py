from matplotlib import pyplot as plt

class Histogram:

    def läs_in_poäng_från_lista(self):
        poäng_lista = []
        with open('C:/Users/samer/source/repos/Grundläggande programmering P-uppgiften/Grundläggande programmering P-uppgiften/poäng per spel.txt', 'r', encoding='utf-8') as fil:
            for line in fil:
                poäng_lista.append(line)

        return self.Tabort_radbrytning(poäng_lista)


    def Tabort_radbrytning(self, poäng_lista):
        for elem in range(len(poäng_lista)):
            poäng_lista[elem] = int(poäng_lista[elem].strip())
        return poäng_lista


    def skapa_intervall(self, poäng_lista):
        intervall_lista = []
        intervall = 0
        poäng_lista.sort()
        high_score = poäng_lista[-1]
        while True:
            intervall_lista.append(intervall)
            intervall += 5
            if intervall >= high_score:
                break
        return intervall_lista


    def Rita_histogram(self):
        plt.style.use("fivethirtyeight")
        
        poäng_lista = self.läs_in_poäng_från_lista()
        intervall_lista = self.skapa_intervall(poäng_lista)
        
        plt.hist(poäng_lista, bins=intervall_lista, edgecolor="black")

        plt.title("Statestik")
        plt.xlabel("Poäng")
        plt.ylabel("Antal spel omgångar")
        plt.tight_layout()
        plt.show()

if __name__ == "__main__":
    Rita = Histogram()
    Rita.Rita_histogram()
