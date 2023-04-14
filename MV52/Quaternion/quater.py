from math import sqrt

class Vector:

    def __init__(self,x,y,z):
        self.x: float = x
        self.y: float = y
        self.z: float = z
    
    def mult(self, a):  
        return Vector(self.x * a, self.y * a, self.z * a)
    
    def sum(self, v):
        return Vector(self.x+v.x, self.y+v.y, self.z+v.z)

    def scalprod(self,v2):
        return self.x * v2.x + self.y * v2.y + self.z * v2.z

    def vectprod(self,v2):
        return Vector(self.y * v2.z - self.z * v2.y,self.z * v2.x - self.x * v2.z,self.x * v2.y - self.y * v2.x)
    
    def prin(self):
        print("x: "+str(self.x)+" y: "+str(self.y)+" z: "+str(self.z))
    

class Quaternion:

    def __init__(self,s,v):
        self.v: Vector = v
        self.s: float = s

    def multi(self, q2):
        x = q2.v.mult(self.s)
        y = self.v.mult(q2.s)
        z = self.v.vectprod(q2.v)
        return Quaternion(self.s * q2.s - self.v.scalprod(q2.v), x.sum(y).sum(z) )

    def conj(self):
        return Quaternion(self.s, self.v.mult(-1))
    
    def rotate(self,q2):
        return q2.multi(self).multi(q2.conj())
    
    def prin(self):
        print("s: "+str(self.s),end='')
        self.v.prin()


# v1 = Vector(1,2,3)
# v2 = Vector(2,3,4)
# v1.mult(2).prin()
# v1.sum(v2).prin()
# print(v1.scalprod(v2))
# v1.vectprod(v2).prin()

qr = Quaternion(0, Vector(sqrt(2)/2,sqrt(2)/2,0))
qa = Quaternion(0, Vector(1,2,3))
qap = qa.rotate(qr)
qap.prin()

qr = (Quaternion(0,Vector(0,sqrt(2)/2,sqrt(2)/2)))
qapp = qap.rotate(qr)
qapp.prin()