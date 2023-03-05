class intelligence:
    
    def __init__(self, difficulty):
        self.coward = False
        self.moderate = True
        self.bold = False
    
    def coward(self):
        if self.player.turn_score > 6:
            self.game.hold()
            
    def moderate(self):
        if self.player.turn_score > 15:
            self.game.hold()