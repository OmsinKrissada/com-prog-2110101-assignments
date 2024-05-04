class BigWallet:
    def __init__(self, NOTES):
        self.notes = {v: 0 for v in NOTES}
    
    def valid_note(self, v):
        return v in self.notes

    def add(self, v, n):
        if not self.valid_note(v):
            return
        self.notes[v] += n
    
    def total(self):
        s = 0
        for k,v in self.notes.items():
            s += k * v
        return s

    def __lt__(self, rhs):
        return self.total() < rhs.total()