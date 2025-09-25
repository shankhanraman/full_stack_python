# Docstrings: Stored as metadata, useful for tools like help(), IDEs, and documentation generators.
# Stored in the code object and accessible at runtime with .__doc__.
# Docstring should be first line otherwise it woul rturn None
def chai_flavour(flavour="masala"):
    """Return the falvours of chai  """
    chai = "Ginger"
    return flavour

# Dunder the __ Double Under 
print(chai_flavour.__doc__)
print(chai_flavour.__name__)

# help(len)

def generate_bill(chai=0, samosa=0):
    """Calcualte the total bill for chai and samosa
    :param chai:Nubeer of chai cups (10 rupees each)
    :param samosa: Number of samosa (15 rupees each)
    : return : (total amount , thank ou messsage)
    """
    total = chai*10 + samosa*15
    return total, "Thank you for visiting shankhan"