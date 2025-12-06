from langchain_community.utilities import SQLDatabase
from langchain_community.agent_toolkits import create_sql_agent
from langchain_community.llms import Ollama
import time

# Database Connection
db = SQLDatabase.from_uri("sqlite:///Chinook.db")

# Initialize Ollama LLM
llm = Ollama(model="llama3", temperature=0)

# Create SQL Agent
agent = create_sql_agent(
    llm=llm,
    db=db,
    verbose=True,  # shows reasoning steps
    agent_executor_kwargs={"handle_parsing_errors":True}

)

# Quick demo query
answer = agent.run("List total sales per country")
print(answer)

if __name__ == "__main__":
    # Test code for assignment
    queries = [
        "List total sales per country and which country spent the most.",
        "Which artist has the most albums in the database?",
        "What are the top 5 most popular music genres by number of tracks?"
    ]

    for q in queries:
        print(f"\nQuery: {q}")
        start_time = time.time()  # start timer
        try:
            result = agent.run(q)
        except Exception as e:
            result = f"Error occurred: {e}"
        end_time = time.time()  # end timer
        elapsed = end_time - start_time
        print(f"Result: {result}")
        print(f"Response time: {elapsed:.2f} seconds")

        
