# 🚀 Getting Started with the ADK on GitHub Codespaces

Welcome! This guide is designed to help you set up and run the Agent Development Kit (ADK) on **GitHub Codespaces** safely, securely, and seamlessly—perfect for mobile or web-based development.

---

## 🔒 Step 1: Security First (Set Up Your API Keys)

To run agents, you need an API key (like a Google Gemini API Key). We must ensure these keys are **never** committed to GitHub.

There are two secure ways to configure your API keys:

### Option A: Using Codespaces Secrets (Recommended)
This is the easiest and safest method for cloud development. It injects your keys directly as environment variables when the Codespace starts up, without saving them to any files.

1. Go to your GitHub account settings: **Settings** ➡️ **Codespaces** ➡️ **Codespaces secrets** (or navigate directly to `https://github.com/settings/secrets/codespaces`).
2. Click **New secret**.
3. Name your secret `GEMINI_API_KEY` and paste your Gemini API key (from [Google AI Studio](https://aistudio.google.com/)) as the value.
4. Set the **Repository access** to allow access from this repository.
5. Click **Add secret**.
6. (Optional) Repeat the same process to add other keys if you plan to use multiple providers (e.g., `OPENAI_API_KEY` or `ANTHROPIC_API_KEY`).

### Option B: Local `.env` file (Fallback)
If you prefer not to use Codespaces Secrets, you can use a local environment file.
1. In the file explorer, duplicate `.env.template` and rename the copy to `.env`.
2. Open `.env` and paste your API key next to `GEMINI_API_KEY=`.
3. *Note: `.env` is already configured in `.gitignore` so it will never be tracked or pushed to GitHub.*

---

## 💻 Step 2: Open in GitHub Codespaces

1. Click the green **Code** button on your GitHub repository.
2. Select the **Codespaces** tab.
3. Click **Create codespace on main**.
4. GitHub will automatically detect the `.devcontainer/` setup, provision a virtual machine, configure Python, install `uv`, restore all dependencies, and set up the pre-commit tools. This might take 1–2 minutes on the first launch.

---

## 🧪 Step 3: Run Your First Multi-Agent Workflow

We have created an awesome beginner-friendly **Researcher & Formatter** multi-agent workflow under `contributing/samples/workflows/researcher/`.

### Run via interactive CLI:
Open a terminal in Codespaces and run:
```bash
adk run contributing/samples/workflows/researcher
```
When prompted, type a topic you'd like researched (e.g., *"The history of autonomous flight"* or *"How photosynthesis works"*).

* **The Researcher Agent** will gather rich factual information.
* **The Formatter Agent** will receive the raw research and format it into a gorgeous Markdown document.

---

## 🌐 Step 4: Run the ADK Web UI

The Web UI is a beautiful web-based playground where you can visual and run your multi-agent workflows.

1. Run the web server in the terminal:
   ```bash
   adk web contributing/samples/workflows
   ```
2. Codespaces will detect that port `8000` is open and display a small notification: **"Application running on port 8000"**.
3. Click **Open in Browser**. A new tab will open displaying the ADK Web UI!
4. From here, you can select the `researcher_workflow` and test it interactively.

---

## 🛠️ Step 5: Modifying or Swapping Providers (Learning Multi-Agent Flow)

Open `contributing/samples/workflows/researcher/agent.py` to see how the agents are declared.

* You can tweak their `instruction` strings to change their behaviors.
* To switch models or try other AI providers, edit the `model` parameter of the agents as described in the comments inside `agent.py`.
