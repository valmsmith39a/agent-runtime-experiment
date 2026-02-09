# Agent Runtime Experiment

## Goal

An educational repo showing the progression of building an AI agent
runtime from scratch. Each directory is a self-contained, runnable
step that builds on the previous one. No frameworks — raw Python.

## Structure

agent-runtime-experiment/
├── 01-basic-loop/ # Simple input/print loop calling Claude API
├── 02-with-tools/ # Add local Python tool functions
├── 03-fastapi/ # Wrap in a web server
├── 04-with-memory/ # Add conversation memory
├── 05-mcp-tools/ # Replace local tools with MCP servers
└── README.md

## Rules

- Each directory is self-contained with its own requirements.txt
- No LangGraph, no LangChain, no frameworks
- Use Anthropic SDK directly
- Python 3.11+
- Build one step at a time — don't create future steps until asked
