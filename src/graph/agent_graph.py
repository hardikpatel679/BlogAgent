from langgraph.graph import StateGraph,END
from src.llm.groqllm import Groq_LLM
from src.state.blockstate import BlogState
from src.node.blog_generation_node import BlogNodes


class Agent_Graph:
    def __init__(self,llm):
        self.llm = llm
        self.graph = StateGraph(BlogState)



    def build_blog_graph(self):
        """
         Build a grph to generate the content for blog based on topic.
        """

        ## add node
        self.nodes = BlogNodes(self.llm)
        self.graph.add_node("title_createion",self.nodes.generate_title)
        self.graph.add_node("blog_content_creation",self.nodes.generate_content)
        
        ## add edge
        self.graph.set_entry_point("title_createion")
        self.graph.add_edge("title_createion","blog_content_creation")
        self.graph.add_edge("blog_content_creation",END)

        return self.graph
    
#below code for langsmith langgraph studio
llm = Groq_LLM().get_llm()

# get graph
graph_builder = Agent_Graph(llm)
graph = graph_builder.build_blog_graph().compile()
