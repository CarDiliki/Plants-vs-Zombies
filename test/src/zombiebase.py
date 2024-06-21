import objectbase

class ZombieBase(objectbase.objectBase):
    def __init__(self, pathFmt, pathIndex, pos, size=None, pathIndexCount=0):
        super(ZombieBase, self).__init__(pathFmt, pathIndex, pos, size, pathIndexCount)
        
    def getPositioCD(self):
        return 0.2    
    
    def checkPosition(self):
        result =  super(ZombieBase, self).checkPosition()
        if result:
            self.pos[0] -= 2.5
        return result