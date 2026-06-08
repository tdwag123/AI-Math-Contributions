# AI Math Contributions

A curated dataset tracking mathematics problems solved or meaningfully advanced with AI assistance. Each entry records the problem, the AI system(s) involved, the human collaborators, and the solution status.

This dataset intends to be used to better understand the current limitations and success cases of AI being used in mathematics. It would be nice to have the LLM output (CoT included) for problems where this is possible.

## Dataset

**File:** `ai_math_contributions.json`  
**Schema version:** 1.1  
**Entries:** 145

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
| Individual papers | 18 |
| D. Anderson Conjectures | 1 |
| Green's Open Problems | 1 |

### By mathematical area (top 8)
| Area | Entries |
|---|---|
| Number Theory | 70 |
| Analysis | 15 |
| Combinatorics | 14 |
| Geometry | 13 |
| Additive Combinatorics | 9 |
| Graph Theory | 9 |
| Optimization | 5 |
| Extremal Combinatorics | 2 |

### Was it a pre-existing conjecture?
- **133 entries** (`was_conjecture: true`) — longstanding conjectures posed by others (Erdős, OEIS labels, Green, Courtade–Kumar, Anderson, etc.)
- **10 entries** (`was_conjecture: false`) — open research problems posed by the solving paper's own authors
- **2 entries** (`was_conjecture: null`) — unclear

### AI systems represented
GPT-5.5 Pro, GPT-5.4 Pro, GPT-5.2 Pro, GPT-5.2 Thinking, OpenAI internal model, Claude Mythos, Claude Opus, Gemini, Aristotle, Aletheia, AlphaProof, AlphaEvolve, DeepMind prover agent, FunSearch, Seed Prover, and others.

## Sources

- **[Erdős Problems](https://www.erdosproblems.com/)** — open problems compiled from Erdős's notebooks and papers
- **[OEIS](https://oeis.org/)** — sequences with open conjectures from the On-Line Encyclopedia of Integer Sequences
- **[Green's Open Problems](https://people.maths.ox.ac.uk/greenbj/papers/open-problems.pdf)** — Ben Green's list of open problems in additive combinatorics
- **D. Anderson Conjectures** — conjectures by Dave Anderson (algebraic geometry / flag varieties)
- **Individual papers** — results from arXiv preprints and published papers, cited per entry in `solution_reference`

## Adding an entry

Append to the `entries` array in `ai_math_contributions.json`. Key rules:

- `was_conjecture: true` only if the problem was established and publicly known before the solving paper.
- `verification_status: "Verified"` only if the result has been peer-reviewed or confirmed by independent mathematicians. If the result has been verified in Lean or another language, use "Lean Verified"
- List each distinct conjecture or problem as its own entry
