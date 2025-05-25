from textwrap import dedent
from agno.agent import Agent
from agno.models.google import Gemini, gemini
from dotenv import load_dotenv
from agents_knowledge import knowledge_base
from agno.storage.sqlite import SqliteStorage
from agno.tools.duckduckgo import DuckDuckGoTools
from google.genai import types
from textwrap import dedent
from agno.tools.reasoning import ReasoningTools
import os
from sqlalchemy.engine import create_engine
from agno.storage.singlestore import SingleStoreStorage
from agno.playground import Playground, serve_playground_app
load_dotenv()
from agno.tools.tavily import TavilyTools
from agno.models.groq import Groq
travily_api_key = os.environ["TRAVILY_API_KEY"]


# SingleStore Configuration
# USERNAME = os.getenv("SINGLESTORE_USERNAME")
# PASSWORD = os.getenv("SINGLESTORE_PASSWORD")
# HOST = os.getenv("SINGLESTORE_HOST")
# PORT = os.getenv("SINGLESTORE_PORT")
# DATABASE = os.getenv("SINGLESTORE_DATABASE")
# SSL_CERT = os.getenv("SINGLESTORE_SSL_CERT")

# # SingleStore DB URL
# db_url = f"mysql+pymysql://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}?charset=utf8mb4"
# if SSL_CERT:
#     db_url += f"&ssl_ca={SSL_CERT}&ssl_verify_cert=true"

# # Create a database engine
# db_engine = create_engine(db_url)

# # Create a storage backend using the Singlestore database
# storage = SingleStoreStorage(
#     # store sessions in the ai.sessions table
#     table_name="agent_sessions",
#     # db_engine: Singlestore database engine
#     db_engine=db_engine,
#     # schema: Singlestore schema
#     schema=DATABASE,
# )

from agno.storage.sqlite import SqliteStorage

# Create a storage backend using the Sqlite database
sql_storage = SqliteStorage(
    # store sessions in the ai.sessions table
    table_name="agent_sessions",
    # db_file: Sqlite database file
    db_file="tmp/data.db",
)

# agent_storage: str = "tmp/agents.db"
TOOLS = [ReasoningTools(),'TavilyTools()']

instructions = dedent("""

Brand Voice:
- Rooted in Ayurveda
- Warmly educational, not preachy
- Trust-building and authentic
- Forward-thinking: blending tradition with technology
- Emotionally resonant without being overly sentimental
- Aspirational yet humble

General Tone:
- Grounded and healing
- Conscious and empowering
- Modern-traditional blend
- Purpose-driven and culturally aware
- Simple (not simplistic) and balanced

Posting Guidelines:

LinkedIn Posts:
- Tone: Thoughtful, visionary, professional
- Length: 3–4 concise sentences

Blog Posts:
- Tone: Educational, grounded, insightful
- Length: 300–500 words

All Content:
- Integrate Ayurvedic principles naturally
- Use Sanskrit terms sparingly; provide parenthetical explanations (e.g., Aarogya = health)
- Avoid overpromising (e.g., "guaranteed," "quick fix," "magic")
- Minimize jargon unless targeted at expert audiences
- Ensure messaging is clear, holistic, personalized to wellness journeys

Emotional Feel:
- Warm and trustworthy
- Focused on personalized, sustainable wellness journeys (avoid fad-based language)

Use tools like: {TOOLS} as needed as possible.
 Use the Search Tools ONLY when needed, DO NOT USE SEARCH TOOL UNNECESSARYLY                     
""")


# Disable all adjustable filters
safety_settings = [
    types.SafetySetting(category=types.HarmCategory.HARM_CATEGORY_HARASSMENT,
                        threshold=types.HarmBlockThreshold.BLOCK_NONE),
    types.SafetySetting(category=types.HarmCategory.HARM_CATEGORY_HATE_SPEECH,
                        threshold=types.HarmBlockThreshold.BLOCK_NONE),
    types.SafetySetting(category=types.HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT,
                        threshold=types.HarmBlockThreshold.BLOCK_NONE),
    types.SafetySetting(category=types.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT,
                        threshold=types.HarmBlockThreshold.BLOCK_NONE),
    types.SafetySetting(category=types.HarmCategory.HARM_CATEGORY_CIVIC_INTEGRITY,
                        threshold=types.HarmBlockThreshold.BLOCK_NONE),
]

report_agent = Agent(
    name="Report Agent",
    model=Gemini('gemini-2.0-flash',safety_settings=safety_settings,temperature=0.4),
    instructions=instructions,
    markdown=True,
    knowledge=knowledge_base,
    search_knowledge=True,

    storage=sql_storage,
    tools=[TavilyTools(api_key=travily_api_key)],
    # Adds the current date and time to the instructions
    add_datetime_to_instructions=True,
    # Adds the history of the conversation to the messages
    add_history_to_messages=True,
    # Number of history responses to add to the messages
    num_history_responses=15,
    # Adds markdown formatting to the messages
    show_tool_calls=True
)

report_agent_groq = Agent(
    name="Report Agent Groq(Llama 3.3)",
    model=Groq('llama-3.3-70b-versatile',temperature=0.4),
    instructions=instructions,
    markdown=True,
    knowledge=knowledge_base,
    search_knowledge=True,

    storage=sql_storage,
    tools=[
           TavilyTools(api_key=travily_api_key)],
    # Adds the current date and time to the instructions
    add_datetime_to_instructions=True,
    # Adds the history of the conversation to the messages
    add_history_to_messages=True,
    # Number of history responses to add to the messages
    num_history_responses=15,
    # Adds markdown formatting to the messages
    show_tool_calls=True
)

report_agent_groq_qwq = Agent(
    name="Report Agent Groq(Qwen QWQ)",
    model=Groq('qwen-qwq-32b',temperature=0.6),
    instructions=instructions,
    markdown=True,
    knowledge=knowledge_base,
    search_knowledge=True,

    storage=sql_storage,
    tools=[
           TavilyTools(api_key=travily_api_key)],
    # Adds the current date and time to the instructions
    add_datetime_to_instructions=True,
    # Adds the history of the conversation to the messages
    add_history_to_messages=True,
    # Number of history responses to add to the messages
    num_history_responses=15,
    # Adds markdown formatting to the messages
    show_tool_calls=True
)

report_agent_groq_llama_4 = Agent(
    name="Report Agent Groq(Llama 4 scout)",
    model=Groq('meta-llama/llama-4-scout-17b-16e-instruct',temperature=0.6),
    instructions=instructions,
    markdown=True,
    knowledge=knowledge_base,
    search_knowledge=True,

    storage=sql_storage,
    tools=[
           TavilyTools(api_key=travily_api_key)],
    # Adds the current date and time to the instructions
    add_datetime_to_instructions=True,
    # Adds the history of the conversation to the messages
    add_history_to_messages=True,
    # Number of history responses to add to the messages
    num_history_responses=15,
    # Adds markdown formatting to the messages
    show_tool_calls=True
)

app = Playground(
    agents=[report_agent,report_agent_groq, report_agent_groq_qwq,report_agent_groq_llama_4],
).get_app()

if __name__ == "__main__":
    serve_playground_app('playground:app', reload=True)
#
