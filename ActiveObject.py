import queue
import threading

class ActiveObject(threading.Thread):        
    def __init__(self, name, publish, transitions={}):
        threading.Thread.__init__(self)
        self.name = name
        self.q = queue.Queue()
        self.publish = publish
        self.transitions = transitions
        self.state = None
                
    def post(self, event):
        self.q.put(event)

    def run(self):
        try:
            event = self.q.get(block=False)
        except Exception as err:
            print(err)
            return

        try:
            self.transitions[self.state]['transitions'][event.name]
        except KeyError:
            print('THROWING ON THE FLOOR...\n')
            return

        newState = self.transitions[self.state]['transitions'][event.name]
        hold = self.state
        
        try:
            exit = self.transitions[self.state]['exit']
            if exit != None:
                getattr(self, exit)()
        except KeyError:
            pass
            
        self.state = newState
        
        try:
            entry = self.transitions[self.state]['entry']
            if entry != None:
                getattr(self, entry)()
        except KeyError:
            pass
            
        print('TRANSITION ' + hold + ' => ' + self.state + '\n')
