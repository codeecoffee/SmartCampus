# Smart Campus OS: AI-Powered University Management System

A production-ready, Full-Stack Academic Management System that integrates **Agentic AI** to automate student support and administrative tasks. Unlike traditional portals, this system uses **RAG (Retrieval-Augmented Generation)** to provide instant, context-aware answers regarding university regulations, course syllabi, and student performance.

---

## 🚀 Key Features

* **Student & Faculty Portals:** Comprehensive CRUD for course enrollment, grade management, and attendance tracking.
* **AI Academic Assistant:** An integrated chatbot capable of:
    * **Contextual Q&A:** Answering questions based on uploaded university PDFs (using RAG).
    * **Performance Analysis:** Summarizing student grades and suggesting focus areas.
    * **Action Execution:** Navigating the UI or initiating administrative requests via natural language.
* **Vectorized Search:** Hybrid search capabilities using SQL and Semantic Search.
* **Real-time Notifications:** AI-generated summaries of campus announcements and academic updates.

## 🏗 Architecture & Design Patterns

The system is built with a focus on **Separation of Concerns** and **Scalability**:

* **Clean Architecture:** Separation between the Domain, Use Cases, and Infrastructure layers.
* **Repository Pattern:** Abstracting data access to allow seamless switching between database providers (e.g., migrating from SQLite to PostgreSQL).
* **Strategy Pattern:** Implemented in the LLM service to toggle between different models (GPT-4o, Llama 3, Claude 3.5) based on cost and task complexity.
* **RAG Pipeline:** Utilizing `pgvector` for efficient document retrieval, ensuring the AI stays within the scope of university-verified data.

## 🛠 Tech Stack

* **Frontend:** [Next.js 14+](https://nextjs.org/) (App Router), Tailwind CSS, Shadcn/UI.
* **Backend:** [FastAPI](https://fastapi.tiangolo.com/) (Python) for high-performance asynchronous AI processing.
* **Database:** [PostgreSQL](https://www.postgresql.org/) with [pgvector](https://github.com/pgvector/pgvector) for relational and vector data.
* **AI/LLM:** [LangChain](https://www.langchain.com/) / [LangGraph](https://blog.langchain.dev/langgraph/), OpenAI API.
* **Authentication:** Clerk or NextAuth.js.
* **DevOps:** Docker, GitHub Actions (CI/CD).

## 🧠 Technical Challenges & Solutions

### 1. Reducing RAG Latency
**Challenge:** Initial queries to the vector database and subsequent LLM processing were taking upwards of 5 seconds.
**Solution:** Implemented **Semantic Caching** with Redis to store common queries and utilized **Streaming Responses** via FastAPI to deliver text to the UI as it is generated, improving the perceived performance significantly.

### 2. Guardrailing Student Data
**Challenge:** Ensuring the AI does not leak one student's grades to another student.
**Solution:** Integrated **Row-Level Security (RLS)** in PostgreSQL and injected strict user-specific metadata filters into the vector search queries.

## 🏁 Getting Started

### Prerequisites
* Docker & Docker Compose
* Python 3.10+
* Node.js 18+

### Installation
1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/youruser/smart-campus-os.git](https://github.com/youruser/smart-campus-os.git)
    ```
2.  **Environment Setup:**
    Create a `.env` file in the root directory and add:
    ```env
    DATABASE_URL=your_postgres_url
    OPENAI_API_KEY=your_key
    ```
3.  **Run with Docker:**
    ```bash
    docker-compose up --build
    ```

---
**Author:** [Fellipe Ferreira Lopes ]
**Role:** AI Software Engineer
**Portfolio:** []
**LinkedIn:** [https://www.linkedin.com/in/fellipeferreiral/]