
import ast
import math
import operator
from pathlib import Path

from dotenv import load_dotenv
from ddgs import DDGS
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_google_genai import ChatGoogleGenerativeAI


# --------------------------------------------------
# 1. LOAD ENVIRONMENT VARIABLES
# --------------------------------------------------

load_dotenv()

SAMPLE_DIR = (Path(__file__).parent / "sample_files").resolve()


# --------------------------------------------------
# 2. TOOL 1: DUCKDUCKGO WEB SEARCH
# --------------------------------------------------

@tool
def web_search(query: str) -> str:
    """Search the internet using DuckDuckGo and return relevant results."""

    try:
        results = list(DDGS().text(query, max_results=5))

        if not results:
            return "No search results found."

        output = []

        for index, result in enumerate(results, start=1):
            output.append(
                f"{index}. {result.get('title', 'No title')}\n"
                f"URL: {result.get('href', 'No URL')}\n"
                f"Summary: {result.get('body', 'No summary')}"
            )

        return "\n\n".join(output)

    except Exception as error:
        return f"Web search error: {error}"


# --------------------------------------------------
# 3. TOOL 2: PYTHON CALCULATOR
# --------------------------------------------------

@tool
def calculator(expression: str) -> str:
    """Calculate mathematical expressions using safe arithmetic operations."""

    operations = {
        ast.Add: operator.add,
        ast.Sub: operator.sub,
        ast.Mult: operator.mul,
        ast.Div: operator.truediv,
        ast.FloorDiv: operator.floordiv,
        ast.Mod: operator.mod,
        ast.Pow: operator.pow,
    }

    unary_operations = {
        ast.UAdd: operator.pos,
        ast.USub: operator.neg,
    }

    def evaluate(node):

        if isinstance(node, ast.Expression):
            return evaluate(node.body)

        elif isinstance(node, ast.Constant):
            if type(node.value) not in (int, float):
                raise ValueError("Only numeric values are allowed.")
            return node.value

        elif isinstance(node, ast.BinOp):
            operation = operations.get(type(node.op))

            if operation is None:
                raise ValueError("Unsupported mathematical operation.")

            left = evaluate(node.left)
            right = evaluate(node.right)

            if isinstance(node.op, ast.Pow) and abs(right) > 10:
                raise ValueError("Exponent is too large.")

            return operation(left, right)

        elif isinstance(node, ast.UnaryOp):
            operation = unary_operations.get(type(node.op))

            if operation is None:
                raise ValueError("Unsupported unary operation.")

            return operation(evaluate(node.operand))

        else:
            raise ValueError("Invalid mathematical expression.")

    try:
        tree = ast.parse(expression, mode="eval")
        result = evaluate(tree)

        if not math.isfinite(result) or abs(result) > 1e100:
            return "Error: Result is too large or invalid."

        return f"Calculation result: {result}"

    except Exception as error:
        return f"Calculator error: {error}"


# --------------------------------------------------
# 4. TOOL 3: LOCAL FILE READER
# --------------------------------------------------

@tool
def read_local_file(filename: str) -> str:
    """Read a text, Markdown or CSV file from the sample_files folder."""

    try:
        if Path(filename).name != filename:
            return "Error: Only filenames are allowed."

        if Path(filename).suffix.lower() not in (".txt", ".md", ".csv"):
            return "Error: Only TXT, MD and CSV files are supported."

        file_path = (SAMPLE_DIR / filename).resolve()

        if not file_path.is_relative_to(SAMPLE_DIR):
            return "Error: Access outside the sample_files folder is forbidden."

        if not file_path.is_file():
            return f"File not found: {filename}"

        if file_path.stat().st_size > 100_000:
            return "Error: File exceeds the 100 KB size limit."

        content = file_path.read_text(encoding="utf-8")

        return f"Contents of {filename}:\n\n{content}"

    except Exception as error:
        return f"File reader error: {error}"


# --------------------------------------------------
# 5. INITIALIZE GEMINI MODEL
# --------------------------------------------------

model = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash",
    temperature=0
)



# --------------------------------------------------
# 6. REGISTER ALL TOOLS
# --------------------------------------------------

tools = [
    web_search,
    calculator,
    read_local_file
]


# --------------------------------------------------
# 7. CREATE AUTONOMOUS AI AGENT
# --------------------------------------------------

agent = create_agent(
    model=model,
    tools=tools,
    system_prompt="""
    You are an intelligent autonomous AI assistant.

    You have access to three tools:

    1. web_search:
       Use this tool to find current information on the internet.

    2. calculator:
       Use this tool for mathematical calculations.

    3. read_local_file:
       Use this tool to read files stored in the sample_files folder.

    Instructions:
    - Select the appropriate tool based on the user's request.
    - Use tools whenever the task requires them.
    - You may use multiple tools for a single question.
    - Use the tool results to prepare your final answer.
    - Never invent tool results.
    - If a tool fails, clearly explain the problem.
    - Give clear and helpful final answers.
    """
)


# --------------------------------------------------
# 8. RUN THE AGENT
# --------------------------------------------------

def run_agent(user_input):

    print("\n" + "=" * 60)
    print("AUTONOMOUS AI AGENT")
    print("=" * 60)

    try:
        response = agent.invoke(
            {
                "messages": [
                    {"role": "user", "content": user_input}
                ]
            }
        )

        # Display tool actions and observations
        for message in response["messages"]:

            tool_calls = getattr(message, "tool_calls", [])

            for call in tool_calls:
                print(f"\n[ACTION] Tool: {call['name']}")
                print(f"Arguments: {call['args']}")

            if getattr(message, "type", "") == "tool":
                print(f"\n[OBSERVATION]\n{message.content}")

        # Display final response
        print("\n" + "-" * 60)
        print("FINAL ANSWER")
        print("-" * 60)

        print(response["messages"][-1].content)

    except Exception as error:
        print(f"\nAgent execution error: {error}")


# --------------------------------------------------
# 9. INTERACTIVE CONSOLE
# --------------------------------------------------

if __name__ == "__main__":

    print("\nWelcome to the Multi-Tool Autonomous AI Agent!")
    print("Available tools: Web Search, Calculator, File Reader")
    print("Type 'exit' to close the application.")

    while True:

        question = input("\nYou: ").strip()

        if question.lower() in ("exit", "quit"):
            print("Agent stopped. Goodbye!")
            break

        if not question:
            print("Please enter a question.")
            continue

        run_agent(question)
