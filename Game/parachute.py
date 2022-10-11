class Parachute():
    """The picture of a parachute
    
    The responsability of Parachute is to display the whole image
    
    Attributes:
        picture (list): List that will contain each part of the parachute
    """

    def __init__(self):
        self._picture = [
         " ___",
        "/___\\",
        "\   /",
         " \ /",
          "  O",
         " /|\\",
         " / \\",
         "",
         "^^^^^^^^^"
        ]
    
    def whole_parachute(self):
        for i in self._picture:
            print(i)

    def index_parachute(self):
        index = self._picture
        return index