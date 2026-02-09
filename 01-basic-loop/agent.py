"""
01-basic-loop: Simple terminal chat loop calling Claude API.

Run:
    python agent.py
"""

import anthropic


def main():
    client = anthropic.Anthropic()
    conversation = []

    print("Chat with Claude (ctrl-c to quit)\n")

    while True:
        try:
            user_input = input("you: ")
        except (EOFError, KeyboardInterrupt):
            print("\nbye!")
            break

        if not user_input.strip():
            continue

        conversation.append({"role": "user", "content": user_input})

        response = client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=1024,
            system="You are a helpful assistant.",
            messages=conversation,
        )

        assistant_text = response.content[0].text
        conversation.append({"role": "assistant", "content": assistant_text})

        print(f"\nclaude: {assistant_text}\n")


if __name__ == "__main__":
    main()
