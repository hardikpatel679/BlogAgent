import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI,Request
from src.llm.groqllm import Groq_LLM
from src.graph.agent_graph import Agent_Graph
import os
from dotenv import load_dotenv
load_dotenv()


app = FastAPI()

os.environ["LANGSMITH_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT"] = "TestGeanAiApp"


@app.post("/blogs")
async def create_blog(request:Request):
    try:
        data = await request.json()
        topic = data.get("topic","")
        language = data.get("language","")
    except Exception:
        return {"status": "error", "message": "Missing or invalid JSON body"}

    ## get LLM object 

    groqLLM = Groq_LLM() # Step 1: Instantiate
    llm = groqLLM.get_llm() # Step 2: Call the method

    agent_graph = Agent_Graph(llm=llm)
    if topic and language:
        graph_builder = agent_graph.build_blog_graph()
        graph = graph_builder.compile()
        state = graph.invoke({"topic": topic,"language":language})

    return {
        "status":"success",
        "blog_details":state
    }

if __name__ == "__main__":
    uvicorn.run("api:app",host="0.0.0.0",port=8000,reload= True)
