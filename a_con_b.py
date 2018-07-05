class Findch():
    def __init__(self,ch):
        self.ch = ch
    def snn(self,firstc,endc):
        first_index = self.ch.index(firstc) + 1
        print(first_index)
        tmp = first_index + 1
        print(self.ch[tmp:])
        end_index = self.ch[tmp:].index(endc) + tmp
        print(end_index)
        return self.ch[first_index:end_index]