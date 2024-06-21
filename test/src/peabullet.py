import objectbase

class PeaBullet(objectbase.objectBase):
    def __init__(self, pathFmt, pathIndex, pos, size=None, pathIndexCount=0):
        super(PeaBullet, self).__init__(pathFmt, pathIndex, pos, size, pathIndexCount)
        
    def getPositioCD(self):
        return 0.008
        
    def checkPosition(self):
        result = super(PeaBullet, self).checkPosition()
        if result:
            self.pos[0] += 4
        return result