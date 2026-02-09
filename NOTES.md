# Agent Runtime Notes

## Step 1 - Basic Loop

### What Claude Code and I built

- A simple REPL that chats with Claude via Anthropic SDK

### How it works

- Create Anthropic client
- conversation array holds chat history between user and Claude
- Every API call sends entire conversation array
- Claude re-reads everything each time
- while True loop runs until Ctrl+C or Ctrl+D

### Key concepts

- Agent runtime: loop that orchestrates the LLM calls
- REPL: read, eval, print, loop design pattern

### Next:

- Add tools, web server, memory between sessions
