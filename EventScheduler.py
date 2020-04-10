from collections import defaultdict
import time
import queue

class EventScheduler(object):

    def __init__(self):
        self.subscriptions = defaultdict(list)
        self.publishQ = []
        self.activeObjects = []

    def registerActiveObjects(self, *activeObjects):
        self.activeObjects = activeObjects
    
    def tick(self):
        for event in self.publishQ:
            for activeObject in self.subscriptions[event.name]:
                activeObject.post(event)
            self.publishQ.remove(event)
        for activeObject in self.activeObjects:
            activeObject.run()

    async def start(self):
        while(True):
            self.tick()
            time.sleep(0.1)
        
    def publish(self, event):
        self.publishQ.append(event)

    def subscribe(self, activeObject, signal):
        if activeObject not in self.subscriptions[signal] :
            self.subscriptions[signal].append(activeObject)

    def unsubscribe(self, activeObject, signal):
        self.subscriptions[signal].remove(activeObject)
