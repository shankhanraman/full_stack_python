from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_qdrant import QdrantVectorStore
from dotenv import load_dotenv
from openai import OpenAI 


load_dotenv()

# Vector Embeddings 
embedding_model = OpenAIEmbeddings(
    model="text-embedding-3-large"
)

openai_client = OpenAI()

vector_db = QdrantVectorStore.from_existing_collection(
    url="http://localhost:6333",
    collection_name="learning_rag",
    embedding=embedding_model,
)

# Take user_input 
user_query = input("Ask something: ")

# Relevant chunks from the vector Db
search_results =vector_db.similarity_search(query=user_query)

# print(search_results)

context = "\n\n\n".join([f"Page Content: {results.page_content}\n Page Number:{results.metadata['page_label']}\n File Location: {results.metadata['source']}" for results in search_results])


system_prompt = """You are a helpful assistant who answers user
 query based on the available context retrieved from 
 a PDF file along with page_contents and page_number.
 You should only ans the user based on the folowing
 context and naviaget the user to open the right page number 
 to know more.

Context:
{context}   
 
 """

response = openai_client.chat.completions.create(
    model="gpt-5",
    messages=[
        {"role":"system","content":system_prompt},
        {"role":"user","content":user_query},
    ]
)

print(f"Response : {response.choices[0].message.content}")


