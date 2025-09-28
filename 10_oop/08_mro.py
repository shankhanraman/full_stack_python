# Method resolution Order 
class A:
    label = "A : Base Class"

class B(A):
    label = "B : Masala Blend"
class C(A):
    label = "C : Herbal Blend"
# It will recognise B as an object
class D(B,C):
    pass
# class D(C,B):
#     pass

cup = D()
print(cup.label)
print(D.__mro__)
