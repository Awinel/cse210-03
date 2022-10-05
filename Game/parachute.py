class Parachute():
    """The picture of a parachute
    
    The responsability of Parachute is to display the whole image
    
    Attributes:
        picture (list): List that will contain each part of the parachute
    """

    def __init__(self):
        self._picture = []
    
    def whole_parachute(self):
        self.picture = [
         " ___",
        "/___\\",
        "\   /",
         " \ /",
          "  O",
         " /|\\",
         " / \\",
        ]
