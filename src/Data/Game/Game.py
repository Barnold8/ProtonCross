# This is basically a data class

class Game:

    def __init__(self,name:str,status:str,is_deck_verified:str,is_chromebook_ready:str,details:str):
        
        self.name                   = name
        self.status                 = status
        self.is_deck_verified       = is_deck_verified
        self.is_chromebook_ready    = is_chromebook_ready
        self.details                = details
        
