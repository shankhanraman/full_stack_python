from mem0 import Memory
from dotenv import load_dotenv
import os
import json
from openai import OpenAI

load_dotenv()


OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
NEO4J_URI = os.getenv("NEO4J_URI")
NEO4J_USERNAME = os.getenv("NEO4J_USERNAME")
NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD")

client = OpenAI()


config = {
    "version":"v1.1",
    "embedder":{
        "provider":"openai",
        "config":{"api_key": OPENAI_API_KEY,"model":"gpt-4.1"}
    },
    "llm":{
        "provider":"openai",
        "config":{"api_key": OPENAI_API_KEY,"model":"gpt-4.1"}
    },
    "graph_store":{
        "provider":"neo4j",
        "config" : {
            "url": NEO4J_URI,
            "username": NEO4J_USERNAME,
            "password": NEO4J_PASSWORD
        }
    },
    "vector_store":{
        "provider":"qdrant",
        "config":{
            "host":"localhost",
            "port": 6333
        }
    }
}
mem_client = Memory.from_config(config)

while True:

    user_query = input("> ")
    search_memory = mem_client.search(query=user_query,user_id="Piyush Garg",) # Here we get dictionary from the output
    
    memory = [
        f"ID:{mem.get("id")} \n Memory: {mem.get("memory")}" for mem in search_memory.get("results")
    ]
    
    SYSYTEM_PROMPT = f"""
       Here is the context about user:
       {json.dump(memory)}
    """
    response = client.chat.completions.create(
        model = "gpt-4.1-mini",
        messages=[
            {"role":"user","content": user_query}
        ]
    )

    ai_response = response.choices[0].message.content
    print("AI:", ai_response)

    mem_client.add(
        user_id="Piyush Garg",
        messages=[
            {"role":"user","content":  SYSYTEM_PROMPT},
            {"role":"assistant","content": ai_response}
            
        ]
    )

    print("Memory has been saved ")
#  Speech to Voice agents
# Speech-to speech : Native audio handling by the model using the Realtime API
#  User -> Agent(Function, Search, Handoff){low latency interactions} ->app
#  Chained arch 
#  user_voice -> Text(STT) ->LLM -> Text -> Audio (TTS)
#  Langrapgh and Langchain

