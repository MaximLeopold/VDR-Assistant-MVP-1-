# Architecture

The VDR Assistant uses Retrieval-Augmented Generation (RAG) to answer due diligence questions using uploaded VDR documents.

## Workflow

User Question
↓
Streamlit Interface
↓
OpenAI File Search
↓
Vector Store Retrieval
↓
GPT-4o Analysis
↓
Answer with Source Citations

## Components

### Frontend

* Streamlit

### Retrieval Layer

* OpenAI File Search
* OpenAI Vector Store

### LLM Layer

* GPT-4o

### Data Sources

* These must be uploaded and depend on the individual use-case 
* Financial Statements
* Commercial Documents
* Legal Agreements
* HR Documentation
* Other VDR/DD Materials
