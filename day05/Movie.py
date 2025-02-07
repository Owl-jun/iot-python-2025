

class Movie:

    def __init__(self, _title=None, _releaseYear=None, _company=None, _rate=None):
        self.__title = _title
        self.__releaseYear = _releaseYear
        self.__company = _company
        self.__rate = _rate
    
    def __str__(self):
        return (f"title = {self.__title}\n"
                f"releaseYear = {self.__releaseYear}\n"
                f"company = {self.__company}\n"
                f"rate = {self.__rate}")
    
    def isNameContain(self, name):
        if name in self.__title:
            return True
        else: return False
        
    get_title = lambda self : self.__title
    get_releaseYear = lambda self : self.__releaseYear
    get_company = lambda self : self.__company
    get_rate = lambda self : self.__rate
    




