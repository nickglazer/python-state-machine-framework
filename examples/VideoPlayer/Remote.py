from ActiveObject import ActiveObject
from Event import Event

class Remote(ActiveObject):
    def __init__(self, publish, player):
        ActiveObject.__init__(self, 'Remote', publish)
        self.player = player
        self.on = True

    def run(self):
        signal = 'ON_SIG' if self.on else 'OFF_SIG'
        # self.player.post(Event(self, self.player, signal))
        self.publish.publish(Event(self, None, signal))
        self.on = not self.on
