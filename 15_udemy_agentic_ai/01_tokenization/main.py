import tiktoken

enc = tiktoken.encoding_for_model("gpt-4o")
text = "Hey there  My Name is Shankhan Raman "
tokens = enc.encode(text)
# Tokens: [25216, 1354, 220, 3673, 7317, 382, 1955, 1104, 9737, 185326, 220]
print("Tokens:", tokens)

decoded_text = enc.decode(tokens)
print("Decoded Text:", decoded_text)

# Vector embedding gives semanctic meaning to the text
# Example: "I love tea" and "I adore tea" will have similar embeddings
# Embeddings are used to find similarity between texts, clustering, classification, etc.

# #  Positionnal encoding 
# Step 1 tokenization
# dog ate cat 
# 56 74 89 
# Step 2 Vector embedding
# Step 3 Positional encoding
# # Add position information to the embeddings
# Step 4 Self attention
# RIver Bank 
# ICIC Bank  
