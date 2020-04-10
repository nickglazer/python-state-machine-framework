class Event(object):
    
    def __init__(self, src, dest, name, data=None):
        self.src = src
        self.dest = dest
        self.name = name
        self.data = data
        
    def __repr__(self):
        return f"{str(self.src)} -> {str(self.dest)} :: {self.name}"

    def __str__(self):
        return f"{str(self.src)} -> {str(self.dest)} :: {self.name}"
