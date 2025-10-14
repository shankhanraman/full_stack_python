from typing_extensions import TypedDict
from typing import Annotated
from langgraph.graph.message import add_messages
from langgraph.graph import StateGraph, START,END
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langgraph.checkpoint.mongodb import MongoDBSaver


load_dotenv()

llm = init_chat_model(
    model="gpt-4.1-mini",
    model_provider="openai"
)

class State(TypedDict):
    messages: Annotated[list, add_messages]

def chatbot(state: State):
    print("/n/nInside chatbot node", state)
    return {"message": ["Hi , This is a message from Chatbot No"]}


graph_builder = StateGraph(State)

graph_builder.add_node("chatbot", chatbot)

graph_builder.add_edge(START,"chatbot")
graph_builder.add_edge("chatbot",END)

graph = graph_builder.compile()

def compile_graph_with_checkpointer(checkpointer):
    return graph_builder.compile(checkpointer=checkpointer)

DB_URI = "mongodb://admin:admin@localhost:27017/lg"
with MongoDBSaver.from_conn_string(DB_URI) as checkpointer:
    graph_with_checkpointer= compile_graph_with_checkpointer(checkpointer=checkpointer)
    config = {
        "configurable" : {
            "thread_id":"piyush"
        }
    }

    # updated_state = graph_with_checkpointer.invoke(
    #     State({"messages": ["Hi , My name is Piyush Garg"]}),
    #     config
    #     )
    # print("/n/n Updated_State", updated_state)
# (START) => chatbot  => (END)
    for chunk in graph_with_checkpointer.stream(
        State({"messages": ["What is my name?"]}),
        config,
        stream_mode="values"
        ):
            chunk["messages"][-1].pretty_print()

# state = {"messages":["Hi this is a message fromm the Chatbot Node"] }
# node runs : chatbot (state : ["Hey there "]) -> ["Hi this is a message from Chatbot"]
# state = {"Messages:" ["Hey There", "Hi this is a message from the ChatBot Node"]} 

# Types of Memory 
# . Short Term memory 
#     . While you are int he session 
#     . While the task is geting performed

# . Long term memory
#     . Stays forever
#     . Your Name       ----------------> . Factual Memory 
#     . Your age                          . Episodic Memory 
#                                         . Semantic memory

# STM(Short term Memory)
# Hotel , Order(132)
# 132
# You get your order

# AI agent that order Food 
# Hey how can I jelp where is my order number 132
# It is getting prepared whats the status

# An ongoing conversation history 

# Long Term Memory 
# My name is Piyush 132
# Here piyuhs is LTM and 132 is STM 
# Long Term Memory 
# MongoDB, Qdrant , grpahDB 

#  Factual Memory of Agents 
# . Facts about user likename ,age
# . There is something always there in Context 

#Episodic memory 
# he don't like about policies 
# He went to paris in 2023

# Hey do you rememeber when I visted the paris 
# Vector DBlogs

# Semantic Memory stres genralized knowledge over acquired over time 


