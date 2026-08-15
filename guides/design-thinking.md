# Thinking Before Coding

The most valuable habit in this whole course: plan first, then automate.

Coding without thinking causes bugs, and bad automation breaks in production.
Before you open your editor, answer four questions.

## The four questions

Pick any script you've written (or want to write) and write down:

1. What problem am I solving?
   - One or two sentences. If you can't state the problem, you're not ready to code.
2. What input does it need?
   - A file path? User input? An API response? AWS credentials?
3. What output should it give?
   - Terminal text? A JSON file? An HTTP response? An exit code?
4. What are the main steps?
   - The rough algorithm, in bullet points — read, process, report.

## Example: the log analyzer

- Problem: Manually scanning logs for errors is slow.
- Input: A path to a `.log` file.
- Output: Counts of INFO / WARNING / ERROR, printed and saved as JSON.
- Steps:
  1. Read the file line by line.
  2. For each line, check which level it contains.
  3. Increment a counter per level.
  4. Print the summary and write it to a file.

That four-line plan is enough to write the code confidently — and to explain it
to a teammate before a single line exists.

## Why it matters

In real DevOps work, scripts run in production, failures are common, and other
people read and modify your code. A clear plan makes your automation easier to
debug, easier to maintain, and safer to run.

Try it: before your next script, write a short `design.md` answering the four
questions. It takes five minutes and saves hours.
