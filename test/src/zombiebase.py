import objectbase

class ZombieBase(objectbase.ObjectBase):
    def checkPosition(self):
        result =  super(ZombieBase, self).checkPosition()
        if result:
            self.pos[0] -= 2.5
        return result