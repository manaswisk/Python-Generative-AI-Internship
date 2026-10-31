# Task 2 – Document Q&A Assistant using RAG

## Project Overview
This project implements a Retrieval-Augmented Generation (RAG) system that allows users to ask questions about PDF documents.

## Technologies Used
- Python
- Google Gemini
- LangChain
- ChromaDB
- Google Generative AI Embeddings
- PyPDF

## Project Workflow
1. Upload a PDF document.
2. Extract text from the PDF.
3. Split the text into smaller chunks.
4. Generate vector embeddings.
5. Store embeddings in ChromaDB.
6. Retrieve relevant document sections.
7. Generate answers using Gemini.
8. Display relevant source page references.

## Key Features
- PDF document processing
- Semantic search
- Vector database storage
- AI-powered question answering
- Source page references
- Interactive notebook interface

## How to Run
1. Open the notebook in Google Colab.
2. Install the required dependencies.
3. Configure your Gemini API key using Colab Secrets.
4. Upload a PDF.
5. Run the notebook cells in order.
6. Ask questions about the uploaded document.

## Security
API keys are stored securely using Google Colab Secrets and are not included in the repository.

## Project Status
Core RAG retrieval and AI question-answering functionality implemented. Interactive chatbot and additional evaluation tests are pending completion.
