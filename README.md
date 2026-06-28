# AI Math Contributions

NOTE: This repo is being updated weekly by an agent. If you see an issue, please let me know.

A curated dataset tracking mathematics problems solved or meaningfully advanced with AI assistance. Each entry records the problem, the AI system(s) involved, the human collaborators, and the solution status.

This dataset intends to be used to better understand the current limitations and success cases of AI being used in mathematics. It would be nice to have the LLM output (CoT included) for problems where this is possible.

## Dataset

**File:** `ai_math_contributions.json`  
**Schema version:** 1.1  
**Entries:** 158

## Schema

Each entry in the `entries` array has the following fields:

| Field | Type | Description |
|---|---|---|
| `id` | string | Unique identifier (`math_001`, `math_002`, …) |
| `source` | string \| null | Named problem list the problem comes from (e.g. `"Erdős Problems"`, `"OEIS"`) |
| `source_problem_number` | number \| null | Problem number within the source list |
| `level_of_contribution` | string | `"AI standalone"` or `"AI collaborating with humans"` |
| `ai_systems` | string[] | AI model(s) that contributed to the solution |
| `humans` | string[] | Human researchers who collaborated |
| `solution_status` | string | Nature of the result (see values below) |
| `problem_tag` | string | Short slug describing the problem |
| `problem_statement` | string | Full problem statement in LaTeX |
| `date_solved` | string | Date or month solved (`YYYY-MM-DD` or `YYYY-MM`) |
| `mathematical_area` | string | Primary mathematical area |
| `solution_reference` | string | URL to the paper or source where the solution appears |
| `verification_status` | string | `"Verified"` (peer-reviewed / confirmed) or `"Unverified"` (preprint) |
| `was_conjecture` | boolean \| null | `true` if the problem was a longstanding conjecture posed by someone other than the solving paper's authors; `false` if self-posed; `null` if unclear |
| `literature` | string \| null | Citation for prior work on the problem |
| `literature_found_on` | string \| null | Where the prior literature was located |
| `literature_similar` | string \| null | Related results in the literature |

### `solution_status` values

- `Full solution` — complete solution to the open problem
- `Full solution (Lean)` — complete solution formally verified in Lean
- `New proof found` — a new proof of a known result
- `New proof found (Lean)` — new proof formally verified in Lean
- `Partial contribution` — significant partial progress
- `Improved explicit bound` / `Improved lower bounds` — quantitative improvement
- `Solution to stronger problem` — stronger result than originally asked
- `Counterexample found` — conjecture refuted

## Statistics

### By source
| Source | Entries |
|---|---|
| Erdős Problems | 87 |
| OEIS | 38 |
| Individual papers | 31 |
| Green's Open Problems | 1 |
| D. Anderson Conjectures | 1 |

### By mathematical area (top 8)
| Area | Entries |
|---|---|
| Number Theory | 70 |
| Analysis | 16 |
| Combinatorics | 14 |
| Geometry | 13 |
| Graph Theory | 11 |
| Additive Combinatorics | 9 |
| Optimization | 5 |
| Algebraic Geometry | 4 |

### Was it a pre-existing conjecture?
- **139 entries** (`was_conjecture: true`) - longstanding conjectures posed by others
- **16 entries** (`was_conjecture: false`) - open research problems posed by the solving paper's own authors
- **3 entries** (`was_conjecture: null`) - unclear

### AI systems represented
Aletheia, AlphaEvolve, AlphaProof, AlphaTensor, Archivara, Archon, Aristotle, AxiomProver, ChatGPT GPT-5 Pro, ChatGPT-5.2 (Thinking), Claude, Claude Code, Claude Mythos, Claude Opus, Claude Opus 4.5, Claude Opus 4.7, Codex, DeepMind prover agent, DeepMind supervised learning models, FullProof, FunSearch (LLM-based program search), GPT, GPT-5, GPT-5 Pro, GPT-5.2, GPT-5.2 Pro, GPT-5.2 Thinking, GPT-5.4 Pro, GPT-5.4 Thinking, GPT-5.5, GPT-5.5 Pro, GPT-5.5 Thinking, Gemini, Gemini 3, Gemini 3 Flash, Gemini 3 Pro, Gemini 3.1 Pro, Gemini Pro, Google Gemini DeepThink, Multiscalar Fields System, OpenAI internal model, Rethlas, Seed Prover, Seed Prover 1.5

## Sources

- **[Erdős Problems](https://www.erdosproblems.com/)** — open problems compiled from Erdős's notebooks and papers
- **[OEIS](https://oeis.org/)** — sequences with open conjectures from the On-Line Encyclopedia of Integer Sequences
- **[Green's Open Problems](https://people.maths.ox.ac.uk/greenbj/papers/open-problems.pdf)** — Ben Green's list of open problems in additive combinatorics
- **D. Anderson Conjectures** — conjectures by Dave Anderson (algebraic geometry / flag varieties)
- **Individual papers** — results from arXiv preprints and published papers, cited per entry in `solution_reference`

## Adding an entry

Append one object to the `entries` array in `ai_math_contributions.json`.

Recommended workflow:

1. Find a candidate result with a reliable public source.
2. Confirm that AI made a meaningful mathematical contribution, not just editing or exposition.
3. Use the next unused `math_###` id.
4. Fill every schema field, using `null` only where the schema allows it.
5. Add a direct `solution_reference` URL to the paper, official problem page, formalization, or project page.
6. Run `python validate_dataset.py`.
7. Run `python update_readme_stats.py`.
8. Re-run `python validate_dataset.py` and review the diff before committing.

Key rules:

- `was_conjecture: true` only if the problem was established and publicly known before the solving paper.
<<<<<<< HEAD
- `was_conjecture: false` if the paper's authors posed the problem themselves.
- `was_conjecture: null` if the prior status is unclear after a reasonable literature check.
- `verification_status: "Verified"` only if the result has been peer-reviewed or confirmed by independent mathematicians.
- Use a Lean verification status only when a formal proof artifact is available.
- List each distinct conjecture or problem as its own entry.
- Do not add speculative claims, announcements without a durable source, or results where the AI contribution is unclear.

## Source review policy

Prefer sources that can be checked later:

- arXiv, journal, conference, or institutional paper pages
- official problem-list pages such as Erdos Problems, OEIS, or a maintained open-problem list
- formal proof repositories or project pages for Lean-verified results
- author-maintained pages that link to the underlying paper or proof

Avoid using social posts, screenshots, private messages, or informal claims as the only evidence. They can be useful leads, but entries should point to a durable mathematical source.

## Automation checklist

A weekly automation should be able to:

1. Search approved sources for new candidate results.
2. Add only entries with clear evidence for the mathematical result and AI contribution.
3. Preserve the existing JSON field order.
4. Run `python validate_dataset.py`.
5. Run `python update_readme_stats.py`.
6. Report the candidate sources checked, entries added, validation result, and any uncertain cases left out.
=======
- `verification_status: "Verified"` only if the result has been peer-reviewed or confirmed by independent mathematicians. If the result has been verified in Lean or another language, use "Lean Verified"
- List each distinct conjecture or problem as its own entry
>>>>>>> 8fcdf8651503bcde5c136e83484ea4a7e017b0af
