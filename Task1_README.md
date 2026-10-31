# Task 1 – Structured LLM Prompt Pipeline & JSON Extractor

## Project Overview

This project is part of the Python + Generative AI & LangChain Internship.

The objective is to build an AI-powered information extraction pipeline that takes unstructured candidate information and converts it into structured, validated JSON data using a Large Language Model (LLM).

## Objectives

- Extract candidate details from unstructured text.
- Use Google's Gemini model for information extraction.
- Generate structured JSON output.
- Validate extracted information using Pydantic.
- Handle missing or invalid information through data validation.

## Technologies Used

- Python
- Google Gemini API
- Google Gen AI SDK
- Pydantic
- Google Colab
- JSON

## Project Workflow

1. Provide unstructured candidate information as input.
2. Send the input to the Gemini model.
3. Instruct the model to extract the required candidate fields.
4. Generate structured JSON output.
5. Validate the output using a Pydantic data model.
6. Display the validated candidate information.

## Extracted Candidate Fields

- Name
- Email
- Job Role
- Years of Experience
- Expected Salary

## Project File

`Task_1_AI_JSON_Extractor.ipynb`

## How to Run

1. Open the notebook using Google Colab.
2. Add your Gemini API key to Google Colab Secrets using the name `GEMINI_API_KEY`.
3. Enable notebook access to the secret.
4. Run the notebook cells in order.
5. Provide candidate information and review the structured JSON output.

## Security

The Gemini API key is stored in Google Colab Secrets and should never be hardcoded into the notebook or uploaded to GitHub.

## Learning Outcomes

- Understanding structured prompting with LLMs.
- Working with the Gemini API.
- Generating JSON responses from AI models.
- Validating structured data using Pydantic.
- Building a basic Generative AI pipeline.

## Internship Project

**Python + Generative AI & LangChain Internship**

**Task 1: Structured LLM Prompt Pipeline & JSON Extractor**
