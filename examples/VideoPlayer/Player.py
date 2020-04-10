from ActiveObject import ActiveObject

class Player(ActiveObject):
    def __init__(self, publish):
        transitions = {
            'ON': { 'transitions': { 'OFF_SIG': 'OFF'}, 'entry': 'on' },
            'OFF': { 'transitions': { 'ON_SIG': 'ON'}, 'entry': 'off' },
        }
        ActiveObject.__init__(self, 'Player', publish, transitions)
        self.state = 'OFF'
        publish.subscribe(self, 'ON_SIG')
        publish.subscribe(self, 'OFF_SIG')
        
    def on(self):
        print('TURNING ON...')
        
    def off(self):
        print('TURNING OFF...')

    def play(self):
        print('PLAYING...')
    
    def pause(self):
        print('PAUSED...')
    
    def fastforward(self):
        print('FAST FORWARDING...')

    def rewind(self):
        print('REWINDING...')
