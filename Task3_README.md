# Task 3 – Multi-Tool Autonomous AI Agent

## Project Overview
This project implements a Multi-Tool Autonomous AI Agent using Python, LangChain, and Google Gemini.

The agent understands user questions, autonomously selects suitable tools, executes tasks, and generates meaningful responses.

## Technologies Used
- Python 3.11
- LangChain
- Google Gemini (`gemini-3.5-flash`)
- DuckDuckGo Search
- Python
- python-dotenv

## Features

### 1. DuckDuckGo Web Search
Searches the internet and retrieves relevant information based on user queries.

### 2. Python Calculator
Performs mathematical calculations using a safe expression evaluator.

### 3. Local File Reader
Reads and summarizes supported local text files from the `sample_files` directory.

### 4. Autonomous Tool Selection
The agent automatically determines which tool to use based on the user's request. It can also execute multiple tools to solve a single task.

## Project Structure

```text
Task3_Autonomous_AI_Agent/
│
├── sample_files/
│   └── sample.txt
│
├── agent.py
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

## Installation

1. Clone the repository:

```bash
git clone https://github.com/manaswisk/Python-Generative-AI-Internship.git
```

2. Navigate to the Task 3 folder.

3. Create a virtual environment:

```bash
python -m venv .venv
```

4. Activate it on Windows:

```powershell
.venv\Scripts\Activate.ps1
```

5. Install dependencies:

```bash
pip install -r requirements.txt
```

6. Create a `.env` file and add your Gemini API key:

```text
GOOGLE_API_KEY=your_google_api_key
```

## Run the Project

```bash
python agent.py
```

## Example Queries

**Calculator:**
```text
Calculate 1250 * 48 + 750
```

**File Reader:**
```text
Read sample.txt and summarize its contents.
```

**Web Search:**
```text
Search the web for the latest developments in Generative AI.
```

**Multi-Tool Execution:**
```text
Read sample.txt, identify the tools mentioned,
and calculate 2500 * 36 + 1500.
```

## Testing Results

| Test | Status |
|---|---|
| Python Calculator | Passed |
| Local File Reader | Passed |
| DuckDuckGo Web Search | Passed |
| Multi-Tool Execution | Passed |

## Conclusion

The project successfully demonstrates an autonomous AI agent capable of selecting and executing multiple tools using LangChain and Google Gemini. It showcases practical applications of Generative AI, tool calling, and multi-step problem solving.
