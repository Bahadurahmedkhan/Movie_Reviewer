# Requirements Elicitation Chatbot

A Python-based chatbot that helps gather product requirements and generates user stories with acceptance criteria.

## Features

- Interactive conversation flow for requirement gathering
- Structured user story generation
- Formatted output in YAML/JSON
- Easy-to-follow conversation pattern

## Setup

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the chatbot:
```bash
python src/main.py
```

## Output Format

The chatbot generates user stories in the following format:

```yaml
title: "<Story Title>"
description: "<User Story Description>"
acceptance_criteria:
  - "<Criterion 1>"
  - "<Criterion 2>"
  - "<Criterion 3>"
```

## Project Structure

```
requirements_chatbot/
├── src/
│   ├── main.py
│   ├── chatbot.py
│   ├── story_generator.py
│   └── templates/
│       └── story_template.yaml
├── tests/
├── requirements.txt
└── README.md
``` 