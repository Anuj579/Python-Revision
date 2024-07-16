class Vector:
    def __init__(self,x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)
    
    def __str__(self) -> str:
        return f'Vector ({self.x}i + {self.y}j + {self.z}k)'
    
v1 = Vector(1,2,3)
v2 = Vector(4,5,6)

print(v1+v2)
# print(v1*v2)