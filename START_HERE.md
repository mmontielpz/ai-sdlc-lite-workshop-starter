# Start here: build a landing page with Copilot (15-20 minutes)

Everything you need is in this repository: the website starter, its placeholder images, and the instructions. No other repository or download is required.

**You need:** Git, Node.js 20.19+ or 22.12+ (the starter's Vite requirement), npm, and GitHub Copilot CLI signed in (`copilot login`).

## Steps
1. **Clone and set up** (the checks must pass *before* you change anything):
   ```bash
   git clone https://github.com/mmontielpz/ai-sdlc-lite-workshop-starter.git
   cd ai-sdlc-lite-workshop-starter
   node --version && npm --version
   (cd website && npm ci && npm run lint && npm run build)
   ```
2. **Install AI-SDLC Lite** (experimental) from the repository root:
   ```bash
   copilot skill add --project https://raw.githubusercontent.com/mmontielpz/ai-sdlc-lite/master/.agents/skills/ai-sdlc-lite/SKILL.md
   copilot skill list        # expect: ai-sdlc-lite, project, enabled
   ```
3. **Open Copilot** in the repository root: `copilot` (choose "Yes" for this session only if it asks to trust the folder).
4. **Give it the challenge:** paste the prompt from [WEBSITE_TASK.md](WEBSITE_TASK.md).
5. **Approve the plan once.** Approve each tool prompt once (never "don't ask again").
6. **Run and verify** with the commands in [WEBSITE_ACCEPTANCE.md](WEBSITE_ACCEPTANCE.md): lint, build, dev server, phone and desktop widths, and `git diff`.

Done when every row of WEBSITE_ACCEPTANCE.md is satisfied. Stuck? [TROUBLESHOOTING.md](TROUBLESHOOTING.md). No Copilot or no budget? [FALLBACK.md](FALLBACK.md). Discussion: [DISCUSSION.md](DISCUSSION.md).

Cost note: Copilot usage may consume your plan allowance; `/usage` shows it and `/limits` offers only a soft cap. Spend only what you have authorized.

Optional second exercise (Python): [PYTHON_START_HERE.md](PYTHON_START_HERE.md).
