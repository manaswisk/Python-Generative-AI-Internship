# Task 3 – Multi-Tool Autonomous AI Agent

## Project Overview
This project implements an autonomous AI agent that can select and use different tools to answer user requests.

## Technologies Used
- Python
- LangChain
- Google Gemini
- DuckDuckGo Search
- Python AST and operator modules

## Available Tools

### 1. Web Search
Uses DuckDuckGo to retrieve information from the internet.

### 2. Calculator
Performs mathematical calculations using Python.

### 3. File Reader
Reads permitted local text files.

## Key Features
- Autonomous tool selection
- Multiple tool integration
- Mathematical calculations
- Web information retrieval
- Local text file reading
- Agent execution logging
- Error handling

## How to Run
1. Open the notebook in Google Colab.
2. Install the required packages.
3. Configure the Gemini API key using Colab Secrets.
4. Create and test the three tools.
5. Initialize the Gemini model.
6. Create the autonomous agent.
7. Run the agent test questions.

## Security
API keys are stored using Google Colab Secrets. They must never be committed to GitHub.

## Project Status
The three tools and the autonomous agent have been implemented. Full agent testing and execution logs are to be completed.
