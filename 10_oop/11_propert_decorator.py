class TeaLeaf:
    #  self._age = age in Python, 
    # where _age starts with a single underscore, 
    # signifies a "protected" member. 
    # This is part of Python's approach to 
    # encapsulation and indicates that _age is intended for internal use within the class and its subclasses, rather than direct access from outside the class.
    # Deflaut is alos treated this way if we don't apply uunderscore
    def __init__(self,age):
        self._age =age
    
    @property
    def age(self):
        return self._age+2
    
    @age.setter
    def age(self,age):
        if 1 <=age <= 5:
            self._age = age
        else:
            raise ValueError("Tea Leaf age must be between 1 and 5 years")
        
leaf = TeaLeaf(2)
print(leaf.age)
leaf.age =5
print(leaf.age)