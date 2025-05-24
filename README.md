# 📘 Ayurveda Knowledge Base – Setup Guide

## Clone the Repository and Run the Embedding Script

1. **Clone this repository to your local system**:

   `git clone https://github.com/omarnahdi/Ayurveda.git`

2. **Navigate into the project directory**:

   `cd Ayurveda`

3. **Rename the example environment file**:

   Rename the file named `example.env` to `.env`:

4. **Add your required API keys**:

   Open the `.env` file in any text editor and fill in all the required API keys (e.g., OpenAI, Gemini, or others based on your embedding setup).

   > ⚠️ Make sure all keys are correct and active — the embedding process depends on them.

5. **Run the main script after Docker is up and PDF files are in the `data/` folder**:

   `python agents_knowledge.py`

---

6. **Download all the dependencies by running**
   ```python
   python -r requirements.txt
   ```
# **Follow the next steps**


## 📂 Download PDF Files into `data` Folder

1. Go to the Releases section of this repository.

2. **Download all the PDF provided in the release.**

3. Create a folder named `data` in the root of your project (if it doesn't already exist):

4. Move all downloaded files into the `data` folder:

These files will be parsed and embedded into the database using the provided scripts.


# Docker Setup

This project uses a PostgreSQL database with `pgvector` extension to embed and store PDF content as vector representations. These embeddings are essential for enabling intelligent features like semantic search and retrieval-based generation (RAG).

## 🚨 Prerequisite: Database Setup (Required)

Before running any processing or embedding scripts, you **must set up the PostgreSQL database with pgvector support**. This step is **mandatory** to embed the PDF files into a vector database.

### 🐳 Step 1: Install Docker

Make sure Docker is installed and running on your system.  
If not installed, download it from: [https://www.docker.com/get-started](https://www.docker.com/get-started)

---

### Run PostgreSQL + pgvector Container

Use the following one-liner command to start the required PostgreSQL container with the necessary configuration:

```bash
docker run -d -e POSTGRES_DB=brand_data_new -e POSTGRES_USER=ai -e POSTGRES_PASSWORD=ai -e PGDATA=/var/lib/postgresql/data/pgdata -v pgvolume:/var/lib/postgresql/data -p 5532:5432 --name pgvector agnohq/pgvector:16
```

## Interacting with Your Agents via Agno Agent UI

Agno provides a beautiful, open-source, and self-hosted UI for interacting with your agents. This interface allows you to chat with your agents, view their memory, knowledge, and more, all while keeping your data stored locally. [1]

To get started with the Agno Agent UI:

1.  **Clone the Agno Agent UI repository:**

    You can either use `npx` for a quick setup:
    ```bash
    npx create-agent-ui@latest
    # Follow the prompts (e.g., enter 'y' to create a new project and install dependencies)
    ```

2.  **Run the Agent UI:**

    After installing dependencies, start the UI:
    ```bash
    cd agent-ui && npm run dev
    ```

3.  **Connect to your Local Agents:**

    The Agno Agent UI needs to connect to a local playground server where your agents are running. Ensure your `agents_knowledge.py` script is set up to serve your agents.

    Once your agent server is running, you can connect the Agent UI to it. The UI will be available on [http://localhost:3000/](http://localhost:3000/)

    
For more detailed information on setting up and using the Agno Agent UI, including how to configure your agent playground server, please refer to the official documentation: [https://docs.agno.com/agent-ui/introduction](https://docs.agno.com/agent-ui/introduction)

# Important ⚠️

Please comment out the following line in the `agents_knowledge.py` file **after the first run** to avoid reloading and upserting the knowledge base multiple times:

```python
knowledge_base.load(recreate=True, upsert=True)
