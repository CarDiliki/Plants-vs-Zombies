import image
import time

class objectBase(image.Image):
    def __init__(self, pathFmt, pathIndex, pos, size = None, pathIndexCount = 0):
        super(objectBase, self).__init__(pathFmt, pathIndex, pos, size, pathIndexCount)
        self.preIndexTime = 0
        self.prePositionTime = 0
        
    def getPositioCD(self):
        pass
        
    def update(self):
        self.checkImageIndex()
        self.checkPosition()
        
    def checkImageIndex(self):
        if time.time() - self.preIndexTime <= 0.2:
            return
        self.preIndexTime = time.time()
        if self.pathIndexCount != 0:
            idx = (self.pathIndex + 1) % self.pathIndexCount
            self.updateIndex(idx)
    
    def checkPosition(self):
        if time.time() - self.prePositionTime <= self.getPositioCD():
            return False
        self.prePositionTime = time.time()
        return True