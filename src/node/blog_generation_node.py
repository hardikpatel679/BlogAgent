from src.state.blockstate import BlogState

class BlogNodes:
    """
    class contain the blogs nodes
    """
    def __init__(self,llm):
        self.llm = llm


    def generate_title(self,state:BlogState):
        """
        crate title generate for the blog
        """
        if state.get('topic'):
            prompt = """
            You are a Senior SEO Content Strategist. Your goal is to generate a high-ranking, SEO-optimized blog title for the topic: {topic}.

            Strict Requirements:
            1. Length: Between 50-60 characters (ideal for Google Search snippets).
            2. Keywords: Place the primary topic as close to the beginning of the title as possible.
            3. Structure: Use a proven SEO formula (e.g., "How to...", "X Best...", "The Ultimate Guide to...").
            4. Power Words: Include one high-impact word (e.g., "Proven", "Essential", "Powerful", "Simplified").
            5. Formatting: Return ONLY the plain text of the title. No quotes, no "Title:", and no Markdown bolding.

            Generate the best SEO title now:
            """
            system_prompt = prompt.format(topic = state['topic'])
            response = self.llm.invoke(system_prompt)
            
            return {"blog":{"title":response.content.strip()}}
        
        

    def generate_content(self,state:BlogState):
    
        """
        blog content generation on given topic 
        """

        if state.get('topic'):
            topic = state.get('topic')
            title = state.get('title')

            prompt = """
                You are a professional technical blogger. Write a comprehensive blog post based on the following:
                
                TOPIC: {topic}
                TITLE: {title}

                STRICT FORMATTING RULES:
                1. Use ONLY '#' style headers (ATX headers).
                - # for the main title
                - ## for main sections
                - ### for subsections
                2. NEVER underline headers with '===' or '---'.
                3. Use standard Markdown for bolding (**text**) and bullet points (* item).
                4. Do NOT include literal backslashes like '\\n'. Use actual newlines.
                5. Start directly with the content. Do not say "Here is your blog".

                Write the blog in clean Markdown format:
                """
            
            system_prompt = prompt.format(
                topic=state['topic'],
                title = state['blog']['title']
                )
            
            response = self.llm.invoke(system_prompt)
            clean_content = response.content.replace("\\n", "\n")
            # Updating state with the new content
            return {"blog":{"title":state.get("blog").get("title"),"content":clean_content}}




            
