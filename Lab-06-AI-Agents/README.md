# Lab 06 - Building a Tool-Using AI Agent

## Student Information

- **Student Name:** M.M.C.D. Bandara
- **Student Number:** 10965093
- **Module:** PUSL3205 - Large Language Models and Generative AI
- **Submission Type:** Individual

## 1. Introduction

This laboratory explores the development of intelligent AI agents capable of interacting with external tools, retrieving information, maintaining memory, and performing automated tasks.

The practical activity focuses on developing an Intelligent University Assistant using Large Language Models, Retrieval-Augmented Generation, SQLite memory, and Google Workspace APIs.

## 2. Objectives

- Understand tool-based AI agent architectures.
- Integrate external tools with Large Language Models.
- Implement persistent conversation memory.
- Integrate Retrieval-Augmented Generation.
- Connect AI agents with Google Workspace services.
- Implement human approval for sensitive actions.
- Understand the limitations of autonomous AI agents.

## 3. Technologies Used

- Python
- Ollama
- LangChain
- SQLite
- Retrieval-Augmented Generation (RAG)
- Google Calendar API
- Google Sheets API
- Google Docs API
- Gmail API
- Kaggle Notebooks
- Google OAuth 2.0

## 4. System Architecture

The university assistant processes user requests through an AI agent that selects appropriate tools based on the requested task.

The architecture combines:

- User interaction and request processing
- Large Language Model reasoning
- Tool selection and execution
- SQLite-based memory
- University knowledge retrieval
- Google Workspace integrations
- Human approval mechanisms

## 5. Implemented Features

### Calculator Tool

Enables the AI agent to perform mathematical calculations using an external tool rather than relying entirely on language model predictions.

### Conversation Memory

Uses SQLite to store and retrieve information across interactions.

### University RAG Search

Retrieves relevant university information and policies from a knowledge base.

### Google Calendar

Supports calendar schedule retrieval and event creation with user approval.

### Google Sheets

Supports searching and retrieving student records.

### Google Docs

Demonstrates automated document generation through the Google Docs API.

### Gmail

Demonstrates email generation and sending with user approval.

### Human Approval

Calendar event creation and email sending require explicit user confirmation before execution.

## 6. Implementation Status

| Component | Status |
|---|---|
| Python AI Agent | Developed |
| Calculator Tool | Tested |
| SQLite Memory | Tested |
| University RAG Search | Tested |
| Google Calendar Integration | Tested |
| Calendar Event Approval | Tested |
| Google Sheets Student Search | Tested |
| Google Docs Generation | Tested |
| Gmail Integration | Tested |
| Calendar Availability Checking | Requires further development |
| Student Record Updating | Not implemented |
| Unified Natural Language Routing | Partially implemented |
| Complete Chat Interface | Requires further development |

The testing statuses are based on the shared practical implementation and its recorded experimental evidence.

## 7. Experimental Evidence

The notebook contains 127 code cells documenting implementation, experimentation, debugging, tool integration, and testing.

Supporting screenshots demonstrate the development process and recorded execution results.

The notebook and screenshots document the shared implementation and recorded experimental results.

## 8. Repository Structure

    Lab-06-AI-Agents/
    |-- README.md
    |-- notebook/
    |   |-- lab6-aiagent.ipynb
    |   |-- README.md
    |-- screenshots/

## 9. Security Considerations

- OAuth credentials are retrieved using Kaggle Secrets.
- Private credentials should never be committed to GitHub.
- External actions require appropriate authorization.
- Calendar event creation and email sending use approval mechanisms.
- Sensitive student information must be protected.

## 10. Limitations and Future Improvements

- Improve natural language tool selection.
- Complete calendar availability checking.
- Implement student record updates.
- Develop a unified conversational interface.
- Improve error handling and authentication.
- Extend end-to-end integration testing.
- Explore n8n-based workflow automation.

## 11. Learning Outcomes

This practical demonstrates how Large Language Models can be extended beyond text generation through external tools, persistent memory, knowledge retrieval, and API integrations.

It also highlights the importance of secure authentication, human approval, reliable tool execution, and responsible automation.

## 12. Conclusion

The Intelligent University Assistant demonstrates a practical prototype of a tool-using AI agent. It combines multiple AI and automation techniques to support university-related tasks while identifying opportunities for further development.



