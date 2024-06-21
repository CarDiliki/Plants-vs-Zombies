import objectbase

class PeaBullet(objectbase.ObjectBase):  
    def checkPosition(self):
        result = super(PeaBullet, self).checkPosition()
        if result:
            self.pos[0] += 4
        return result