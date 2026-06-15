# Setup Guide

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Configure Environment Variables

Create a `.env` file:

```env
OPENAI_API_KEY=...
VECTOR_STORE_ID=...
```

## Run Application

```bash
streamlit run src/app.py
```

## Upload Documents

1. Create a vector store in OpenAI.
2. Upload VDR documents.
3. Copy the Vector Store ID.
4. Add the ID to the `.env` file.
5. Launch the application.
