import image
import time
import data_objest

class ObjectBase(image.Image):
    def __init__(self, id, pos):
        self.id = id
        self.preIndexTime = 0
        self.prePositionTime = 0
        super(ObjectBase, self).__init__(
            self.getData()['PATH'],
            0,
            pos,
            self.getData()['SIZE'],
            self.getData()['IMAGE_INDEX_MAX']
        )
        
    def getData(self):
        return data_objest.data[self.id]
    
    def getImageIndexCD(self):
        return self.getData()['IMAGE_INDEX_CD']
    
    def getPositionCD(self):
        return self.getData()['POSITION_CD']
        
        
    def update(self):
        self.checkImageIndex()
        self.checkPosition()
        
    def checkImageIndex(self):
        if time.time() - self.preIndexTime <= 0.2:
            return
        self.preIndexTime = time.time()
        if self.getData()['IMAGE_INDEX_MAX'] != 0:
            idx = (self.pathIndex + 1) % self.getData()['IMAGE_INDEX_MAX']
            self.updateIndex(idx)
    
    def checkPosition(self):
        if time.time() - self.prePositionTime <= self.getPositionCD():
            return False
        self.prePositionTime = time.time()
        return True