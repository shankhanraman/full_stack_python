# @classmethod recievecs the cls (the class itself)
# Operate on the class not instance 
# Access to cls yes
# Access to self no
class ChaiOrder:
    def __init__(self,tea_type,sweetness,size):
        self.tea_type = tea_type
        self.sweetness =sweetness
        self.size = size

    #cls is keyword wihc whole clss as a refernce 
    @classmethod
    def from_dicts(cls,order_data):
        return cls(
            order_data["tea_type"],
            order_data["sweetness"],
            order_data["size"],
        )
    
    @classmethod
    def from_string(cls,order_string):
        tea_type,sweetness,size = order_string.split("-")
        return cls(tea_type,sweetness,size)

# @static method recives no autotic first argument 
# Utlity function related to the class
# Access to cls no
# Access to self no

class ChaiUtils:
    @staticmethod
    def is_valid_size(size):
        return size in ["Small", "Medium" , "Large"] 


order1 = ChaiOrder.from_dicts({"tea_type":"masala","sweetness":"medium","size":"Large"})
order2 = ChaiOrder.from_string("Ginger-Low_Small")
order3 = ChaiOrder("Large","Low","Sugar")


print(order1.__dict__)
print(order2.__dict__)
print(order3.__dict__)
