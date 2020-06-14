class Score:
    def __init__(self, C=None, E=None, M=None):
        self.Chinese = C
        self.English = E
        self.Math = M
    
    def avg(self):
        count = 0
        scoreSum = 0

        for i in [self.Chinese, self.English, self.Math]:
            if i != None:
                count += 1
                scoreSum += i
        if count != 0:
            return scoreSum/count
        return None

class Student:
    def __init__(self, NAME, ID, C=None, E=None, M=None):
        self.name = NAME
        self.__id = ID
        self.score = Score(C, E, M)

    def getID(self):
        return self.__id
    
    def getAvg(self):
        average = self.score.avg()
        if average != None:
            return average
        return 'None Score'

studA = Student(NAME='hi',ID=123, C=60, M=100)
studB = Student(NAME='bye',ID=-1,E=0)
print(studA.name, studA.getID(),studA.getAvg())
print(studB.name, studB.getID(),studB.getAvg())