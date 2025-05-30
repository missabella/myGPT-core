# GPT Agents Core 🧠🤖

This is the modular logic engine for dynamic GPT agents, file processors, and Notion-integrated automation. Designed for field-ready deployment across legal workflows, tag-based classification, and intelligent assistant behaviors.

---

## 🗂️ Folder Structure

gpt-agents-core/
├── agents/                     # GPT-based personas (run tasks, make decisions)
│   ├── sharness_update.py
│   └── bestiebot_field_agent.py

├── tools/                      # Reusable logic modules (universal logic)
│   ├── notion.py               # Notion update / query tools
│   ├── tag_mapper.py           # Match text to tags via fuzzy or ID
│   └── auth.py                 # Loads .env securely (optional)

├── processors/                 # File-aware or tag-aware execution handlers
│   ├── extract_conflicts.py    # Pattern scanner
│   └── tag_extractor.py        # Suggest tags from plain text

├── config/                     # Static data + configuration layers
│   ├── .env                    # API keys, token, secrets
│   ├── agent_registry.json     # Identity and permission map for agents
│   └── tag_registry.json       # Path-based tag system (e.g. Complaint > § 1983 Claim)

├── actions/                    # OpenAPI schemas for myGPT or Assistants API
│   └── update_status.json      # POST endpoint for updating fields

├── runner.py                   # Command-line or app-entry to trigger agents/tasks
├── requirements.txt            # Dependencies (openai[agents], notion-client, etc)
└── README.md                   # System overview + onboarding notes


---

## 🛠️ Setup

1. **Clone the repo**

2. **Create your `.env`** inside `config/` with this format:
   ```
   NOTION_TOKEN=your_token_here
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

---

## 📦 What is requirements.txt?## 📦 What is `requirements.txt`?

The `requirements.txt` file tells the server exactly which Python libraries your app needs to run.  
Think of it like a **grocery list** for your code — it won’t work right unless all the ingredients are installed!

---

### 🧠 Why do we use it?

When you deploy your app (like to **Render**, **Replit**, or any cloud host),  
the platform reads this file and installs everything listed.  
If it’s missing something? Your app might crash like a cake with no eggs.

---

### 👩‍💻 For Developers

You create this file to make your project **portable**, **reproducible**, and easy to run anywhere.

To auto-generate it based on your current environment, run:

```bash
pip freeze > requirements.txt
```

---

### 🙋‍♀️ For Users

They don’t need to see this — they just use your app.  
But behind the scenes, this file is what keeps the app functioning and healthy.

---

### ✅ Example contents:

```txt
fastapi         # Our web framework
uvicorn         # The server that runs it
requests        # Lets Python talk to other APIs
pydantic        # Helps with clean input/output data
python-dotenv   # Loads secrets like passwords (safely)
```

---

## 🚀 To Run an Agent

```bash
python agents/sharness_update.py
```

Or for a processor:

```bash
python processors/extract_conflicts.py
```

---

## 🧠 Tag-Aware Architecture

Tags are defined in:
```
config/tag_registry.json
```

Use:
```bash
python tools/tag_mapper.py
```
to dynamically map plain text ➝ structured tag paths (e.g. `Complaint > Claim > Government Official`).

Agents like `sharness` and `scrubwatch` use these paths to determine:
- Field updates
- Logic routing
- Conflict escalation

---

## ➕ Add a New Agent

```bash
touch agents/my_agent.py
```

Inside `my_agent.py`:

```python
from tools.notion import update_field

def run():
    update_field(
        database_id="abc123",
        field_name="Status",
        field_value="Pending"
    )
```

Then run it with:

```bash
python agents/my_agent.py
```
