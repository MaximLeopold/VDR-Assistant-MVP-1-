# VDR-Assistant-MVP-1-
AI-powered assistant for Virtual Data Rooms that helps users analyze due diligence documents and retrieve source-backed insights.


# VDR Assistant

VDR Assistant is a prototype application for querying Virtual Data Room (VDR) documents using Retrieval-Augmented Generation (RAG).

The application combines OpenAI File Search, vector-based retrieval, and GPT-4o to answer due diligence questions based on uploaded documents. Responses are generated using retrieved document content and include source references where available.

The project was developed to explore how large language models can support document-intensive workflows commonly encountered during due diligence processes.

## Functionality

The application allows users to:

* Ask natural-language questions about VDR documents
* Retrieve relevant document excerpts using vector search
* Generate answers based on retrieved content
* Review source references associated with generated responses
* Access predefined due diligence questions from the user interface

## Example Questions

### Commercial

* What is the customer concentration?
* Which customers account for the largest share of revenue?
* Are change-of-control clauses present in customer contracts?

### Financial

* How has revenue developed over the last three years?
* What is the EBITDA margin?
* Is a financial forecast available?

### Legal

* Are there any ongoing legal disputes?
* Which material contractual obligations are disclosed?

### Human Resources

* How many employees does the company have?
* Which key management positions are identified?

## Technology Stack

* Python
* Streamlit
* OpenAI API
* GPT-4o
* OpenAI File Search
* OpenAI Vector Stores

## Repository Contents

* `src/app.py` – Streamlit application
* `docs/` – Supporting documentation
* `examples/` – Example due diligence questions
* `screenshots/` – Application screenshots

## Disclaimer

This repository is intended as a proof-of-concept and learning project exploring the use of retrieval-augmented generation for document analysis workflows.
