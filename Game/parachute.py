class Parachute():
    """The picture of a parachute
    
    The responsability of Parachute is to display the whole image
    
    Attributes:
        picture (list): List that will contain each part of the parachute
    """

    def __init__(self):
        self._picture = []
    
    def whole_parachute(self):
        self._picture = [
         " ___",
        "/___\\",
        "\   /",
         " \ /",
          "  O",
         " /|\\",
         " / \\",
        ]
        print(self._picture[0])
        print(self._picture[1])
        print(self._picture[2])
        print(self._picture[3])
        print(self._picture[4])
        print(self._picture[5])
        print(self._picture[6])
        print("")
        print(self._picture[7])

    def index_parachute(self):
        index = self._picture
        return index