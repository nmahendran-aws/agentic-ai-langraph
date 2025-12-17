# LangGraph E-Commerce Support Agent

A simple but powerful AI agent built with LangGraph that demonstrates tool-calling capabilities for e-commerce customer support. The agent can understand customer requests and autonomously execute order cancellations.

## 🌟 Features

- **Intelligent Tool Calling**: The agent automatically decides when to use the `cancel_order` tool based on customer intent
- **State Management**: Uses LangGraph's StateGraph for robust conversation state handling
- **Multi-Step Reasoning**: The agent makes multiple LLM calls to execute tools and generate natural responses
- **Production-Ready Structure**: Uses modern Python practices with `uv` for dependency management

## 🏗️ How It Works

The agent follows a simple but effective workflow:

1. **User Request**: Customer asks to cancel an order
2. **First LLM Pass**: GPT-4 analyzes the request and decides to call the `cancel_order` tool
3. **Tool Execution**: The order cancellation function runs with the extracted order ID
4. **Second LLM Pass**: GPT-4 generates a natural confirmation message
5. **Response**: Customer receives a friendly confirmation

```
User: "Please cancel my order A12345"
  ↓
Agent analyzes → Calls cancel_order(order_id="A12345")
  ↓
Tool returns: "Order A12345 has been cancelled"
  ↓
Agent responds: "I have successfully cancelled your order A12345."
```

## 📋 Prerequisites

- **Python 3.13+**
- **OpenAI API Key** ([Get one here](https://platform.openai.com/api-keys))
- **uv** package manager ([Install instructions](https://docs.astral.sh/uv/))

## 🚀 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/nmahendran-aws/agentic-ai-langraph.git
   cd agentic-ai-langraph
   ```

2. **Install dependencies with uv**
   ```bash
   uv sync
   ```

3. **Set up your OpenAI API key**
   
   Create a `.env` file in the project root:
   ```bash
   echo "OPENAI_API_KEY=your-api-key-here" > .env
   ```
   
   **⚠️ Security**: Make sure `.env` is in your `.gitignore` to avoid committing your API key!

## 🎯 Usage

Run the agent with the example scenario:

```bash
uv run main.py
```

Expected output:
```
human: Please cancel my order A12345.
ai: 
tool: Order A12345 has been cancelled.
ai: I have successfully cancelled your order A12345.
```

## 📁 Project Structure

```
.
├── main.py              # Main agent implementation
├── pyproject.toml       # Project dependencies and metadata
├── uv.lock             # Locked dependency versions
├── .env                # Environment variables (not committed)
└── README.md           # This file
```

## 🧩 Key Components

### State Definition
```python
class State(TypedDict):
    messages: Annotated[list[BaseMessage], add_messages]
    order: dict
```
The state tracks conversation messages and order information throughout the agent's execution.

### Tool Definition
```python
@tool
def cancel_order(order_id: str) -> str:
    """Cancel an order that hasn't shipped."""
    return f"Order {order_id} has been cancelled."
```

### StateGraph Setup
```python
g = StateGraph(State)
g.add_node("assistant", call_model)
g.set_entry_point("assistant")
g.set_finish_point("assistant")
```

## 🔧 Customization

### Add More Tools

Extend the agent's capabilities by adding new tools:

```python
@tool
def check_order_status(order_id: str) -> str:
    """Check the current status of an order."""
    # Your implementation here
    return f"Order {order_id} status: Shipped"

@tool
def issue_refund(order_id: str, amount: float) -> str:
    """Issue a refund for an order."""
    # Your implementation here
    return f"Refund of ${amount} processed for order {order_id}"
```

Then update the tool binding:
```python
llm = ChatOpenAI(model="gpt-4", temperature=0).bind_tools([
    cancel_order,
    check_order_status,
    issue_refund
])
```

### Change LLM Model

Modify the model in `call_model()`:
```python
llm = ChatOpenAI(model="gpt-4-turbo", temperature=0).bind_tools([cancel_order])
```

## 📚 Dependencies

- **langchain** - Framework for building LLM applications
- **langchain-core** - Core LangChain abstractions and messages
- **langchain-openai** - OpenAI integration for LangChain
- **langgraph** - Library for building stateful, multi-actor applications
- **python-dotenv** - Environment variable management

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Add new tools for common e-commerce operations
- Improve error handling
- Add unit tests
- Enhance the conversation flow

## 📄 License

MIT License - feel free to use this project for learning or as a foundation for your own agents!

## 🙏 Acknowledgments

Built with:
- [LangChain](https://www.langchain.com/) - LLM application framework
- [LangGraph](https://langchain-ai.github.io/langgraph/) - Stateful agent orchestration
- [OpenAI](https://openai.com/) - GPT-4 language model

---

**Need help?** Open an issue or check the [LangGraph documentation](https://langchain-ai.github.io/langgraph/)
