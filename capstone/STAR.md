# My Capstone — S.T.A.R Explanation

Fill this in with your own words. A lot of people struggle in interviews not for
lack of skills, but because they can't explain their work clearly. Bullet points
are fine.

## Situation
<!-- What was the problem or context? -->
- 

## Task
<!-- What were you responsible for? -->
- 

## Action
<!-- What did you actually build/do? Be specific about the tech. -->
- 

## Result
<!-- What changed? Quantify if you can (time saved, errors caught). -->
- 

---

### Example (for reference — replace with your own)

- Situation: Application logs grew daily and manually scanning them for errors
  was slow and error-prone.
- Task: Automate log analysis with Python so issues surface quickly.
- Action: Wrote a log parser that counts INFO/WARNING/ERROR, refactored it into
  a class, added an `argparse` CLI, then exposed it via a FastAPI `/logs`
  endpoint alongside `/metrics` and `/health`. Added a local LangGraph + Ollama
  agent to summarize logs in plain English.
- Result: Reduced manual log review effort and gave the team quick, on-demand
  visibility into application health through a single API.
