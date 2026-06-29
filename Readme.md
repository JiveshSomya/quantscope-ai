# QuantScope AI

AI-powered Financial Research Platform.

## Tech Stack

- FastAPI
- Next.js
- PostgreSQL
- Redis
- Qdrant
- Docker

## Architecture
| Folder       | Responsibility                   |
| ------------ | -------------------------------- |
| api          | HTTP endpoints                   |
| services     | Business logic                   |
| repository   | Database queries                 |
| models       | SQLAlchemy models                |
| schemas      | Pydantic request/response models |
| database     | Database connection              |
| core         | Config, security, constants      |
| ai           | LLM logic                        |
| rag          | Vector search                    |
| quant_engine | Rust microservice integration    |



                 Browser
                    │
              Next.js Frontend
                    │
              FastAPI Gateway
         ┌──────────┴──────────┐
         │                     │
         ▼                     ▼
 Authentication          AI Service
         │                     │
         │                     ▼
         │               OpenAI/Gemini
         │
         ▼
     Rust Quant Engine
         │
         ▼
 PostgreSQL / Redis / Qdrant



## How the services communicate

 GET /portfolio
↓
FastAPI
↓
Load portfolio from PostgreSQL
↓
HTTP POST
↓
Rust
↓
Compute analytics
↓
Return JSON
↓
FastAPI
↓
LLM explanation
↓
Frontend