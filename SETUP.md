# Setup

Do this once and every module will just run. Takes about five minutes.

## 1. Python

You need Python 3.10 or newer (3.13 recommended).

```bash
python3 --version
```

If you don't have it: https://www.python.org/downloads/ (or use your package
manager / pyenv).

## 2. Get the code

```bash
git clone https://github.com/TrainWithShubham/python-for-devops.git
cd python-for-devops
```

## 3. Virtual environment

A venv keeps this course's packages separate from the rest of your system.

```bash
python3 -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
```

Your prompt should now start with `(venv)`. Run `deactivate` when you're done.

## 4. Install dependencies

Install everything for the whole course:

```bash
pip install -r requirements.txt
```

Or install just one module's dependencies when you get to it, e.g.:

```bash
pip install -r 02-apis-and-json/requirements.txt
```

Modules 03, 04 and 05 use only the Python standard library — nothing to install.

## 5. Ollama (only for module 08 — AI agents)

The AI agent runs a model locally with [Ollama](https://ollama.com), so there
are no API keys and nothing leaves your machine.

```bash
# install Ollama from https://ollama.com, then:
ollama serve                    # starts the local server
ollama pull llama3.2            # download the default model (~2GB)

# verify it's up and the model is there:
curl http://localhost:11434/api/tags
```

Stronger summaries (optional): `ollama pull qwen3-coder:30b`, then run the agent
with `OLLAMA_MODEL=qwen3-coder:30b`.

## 6. AWS (only for module 06 — AWS automation)

Configure credentials locally. The course only *reads* from AWS — it never
creates, changes, or deletes anything.

```bash
aws configure
# or export AWS_ACCESS_KEY_ID / AWS_SECRET_ACCESS_KEY / AWS_DEFAULT_REGION
```

No AWS account? You can still watch the module and read the code — just skip
running the live calls.

## 7. Check it works

Run the environment check — it verifies your Python version, every course
package, and whether Ollama is ready:

```bash
python check_setup.py
```

You want every line to read `[ok]`. Anything marked `[!!]` needs fixing (usually
`pip install -r requirements.txt`); `[..]` lines are optional and only matter for
module 08.

Want to see real code run? These two work with no extra setup:

```bash
# should print INFO=10, WARNING=2, ERROR=3
python 03-file-handling-and-logs/log_analyzer.py

# the agent's tests (no Ollama needed): should pass
cd 08-ai-agents-for-devops && python -m pytest . && cd ..
```

You're ready — start with [`01-python-foundations`](01-python-foundations/).

## Troubleshooting

- **`pip` installs into the wrong place / `command not found`** — you probably
  forgot to activate the venv. Check for `(venv)` in your prompt.
- **`ModuleNotFoundError`** — install that module's `requirements.txt` (step 4).
- **Agent can't connect** — make sure `ollama serve` is running and `llama3.2`
  is pulled (`curl http://localhost:11434/api/tags`).
- **AWS `NoCredentialsError` / `ClientError`** — credentials aren't configured
  (step 6); expected if you're skipping AWS.
- **Windows activate fails** — use `venv\Scripts\activate` (PowerShell:
  `venv\Scripts\Activate.ps1`).
