# Ritar röda kvadrater som representerar level
class Rita_level:
    """Ritar röda kvadrater som representerar level. 
    Tar emot poäng_visare för att veta vilken level spelaren ligger på. 
    Tar emot canvas kallad Rita_nivå där kvadraterna ska ritas."""
    def __init__(self, poäng, Rita_nivå, level):
        self.poäng = poäng
        self.Rita_nivå = Rita_nivå
        self.level = level

    
    def Rita_kvadrat(self):
        """Ritar kvadraterna i Rita_nivå"""
        nivå = 20 + (self.level-1) * 25
        for x_kordinat in range(5, nivå, 25):
            self.Rita_nivå.create_rectangle(x_kordinat, 0, x_kordinat+15, 15, fill="red", outline="red")

if __name__ == "__main__":
    Rita = Rita_level()
