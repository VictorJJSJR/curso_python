class Sport:
    """ Clase para representar un deporte """

    def __init__(self, name:str, players:int, league:str):
        self.name = name
        if type(player != int):
            self.players = int(players)
            self.league = league

    def __str__(self):
        """Representacion en string de Sport"""
        return f"Sport: {self.name}, {self.players}, {self.league}"
    
    def __repr__(self)->str:
        """Representacion en string de Sport"""
        return f"Sport(Name='{self.name}', Players={self.players}, leagues='{self.league}')"
    
    def to_json(self)->dict:
        """Regresa un diccionario con la informacion de Sport"""
        return {'name':self.name, 'players':self.players, 'league':self.league}
    
    if __name__ == '__main__':
        nfl = Sport('Football', 11, 'NFL')
        print(nfl)
        print(repr(nfl))
        print(nfl.to_json())
        print(f"nfl: {id(nfl)}")