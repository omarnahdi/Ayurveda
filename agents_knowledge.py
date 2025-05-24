from agno.knowledge.pdf import PDFKnowledgeBase, PDFReader
from agno.vectordb.pgvector import PgVector
from agno.embedder.google import GeminiEmbedder

knowledge_base = PDFKnowledgeBase(
    path="./data",  # Your local PDF folder
    vector_db=PgVector(
        table_name="brand_data_new",  # Table name inside your Postgres
        db_url="postgresql+psycopg://ai:ai@localhost:5532/brand_data_new",  # Updated DB name!
        embedder=GeminiEmbedder(id='text-embedding-004',dimensions=768),  # Use Gemini to embed the content
    ),
    reader=PDFReader(chunk=True),
)

# knowledge_base.load(recreate=False, upsert=True)  # Force fresh table creation and upload
