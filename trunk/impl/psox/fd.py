class FdDict(dict):
    def append(self, thing):
        self[sorted(list(set(range(0,256)) - set(self.keys())))[0]] = thing
