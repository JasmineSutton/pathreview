## Week 7 — Issue selection

**Issue link:** [https://github.com/jamjamgobambam/pathreview/issues/89]

**Issue title:** [API reference doc is missing the POST /profiles request body schema #89]

**Tier:** [x] Tier 1  [ ] Tier 2  [ ] Tier 3

**Problem summary:**
The API document is missing the request information. POST request examples inform users of how to ask a service for data/information, not having this information makes it incredibly difficult for users to communicate appropriately with the service. 
The proper fix for this issue would be including the schema for POST /profiles and /reviews; a skeleton request with placeholder tags for information to be input would be ideal.


**Branch name:** [JasmineSutton/enhancement/89-API-Documentation-Update]

**Setup confirmation:** [ ] App runs locally at localhost:5173

**Cohort ledger:** [ ] Issue added to cohort ledger


## Week 8 — Reproduction & solution planning

**Reproduction commit link:** https://github.com/JasmineSutton/pathreview/blob/enhancement/89-API-Documentation-Update/REPRO.md

**Reproduction summary:**
I reproduced issue #89 by comparing API.md to the implemented routes and schemas in the API code. I confirmed that request body documentation is missing for POST /profiles and POST /reviews, which makes the API contract incomplete for consumers. I also confirmed related documentation gaps: missing POST /profiles multipart form details (github_username, portfolio_url, optional resume_file), missing POST /reviews request schema (profile_id UUID), and missing mention that profiles/reviews routes require Bearer authentication.

**PLAN.md link:** [[link to PLAN.md]](https://github.com/JasmineSutton/pathreview/blob/enhancement/89-API-Documentation-Update/PLAN.md)

**Walkthrough video (recommended):** [link to your Loom video, ≤2 min — shared for early feedback]

**Blockers or open questions:**
No major blockers. Remaining task is to ensure API.md reflects exact request formats and constraints from code:
POST /profiles uses multipart form data, not JSON.
POST /reviews uses JSON with profile_id.
Login expects OAuth2 form fields username and password.
Mark auth requirements clearly for protected endpoints.

## Week 9 — Solution building & PR submission

### Check-in 1 (mid-week)

**Current progress:**
Updated the API reference in docs/API.md to document the request bodies for POST /profiles and POST /reviews, including the multipart form fields for profile creation and the JSON payload for review creation. I also verified the implementation details against the actual route handlers so the documentation matches the real API behavior.

**Next steps:**
Add a focused regression test for the API contract and run the relevant test command to confirm the documentation change is backed by executable validation.

**Blockers:**
The wider unit test suite still has unrelated existing failures, so I’m keeping the validation focused on the endpoint contract relevant to this issue.

---

### Check-in 2 (end of week)

**PR link:** [TBD — not submitted yet]

**Branch:** [JasmineSutton/enhancement/89-API-Documentation-Update]

**What you built:**
Updated the API reference in docs/API.md so users can see the request body format for both POST /profiles and POST /reviews. The profile documentation now explains the multipart/form-data fields used by the implementation, and the review documentation now includes the JSON payload schema with the required profile_id field. I also clarified that these protected endpoints require Bearer authentication.

**Tests added or updated:**
Added a focused API contract test in tests/unit/test_api_contract.py to verify that FastAPI exposes request bodies for the documented endpoints. I verified it with pytest tests/unit/test_api_contract.py -v, and it passed with 1 passing test.

**Self-review confirmation:** [ ] make check passes  [x] make test-unit passes

**Draft PR feedback received from:** [none]

## Week 10 - Iteration & reflection

### Reviewer feedback

**Feedback received:** [ ] Yes  [x] No - still awaiting review

**Summary of feedback:**
No reviewer feedback was provided in Summer 2026. I checked my open PR and documented the status here as required.

**How you responded:**

---

### Reflection

**What was harder than you expected?**
The hardest part was translating code behavior into documentation that is both precise and useful. At first glance the issue looked simple, but validating the exact request contract took careful tracing across routes, schemas, and auth behavior. The tricky detail was making sure I did not imply JSON where the endpoint actually expects multipart/form-data, and confirming that protected endpoints were clearly marked.

**What did you learn about working in a large codebase?**
I learned that correctness depends on cross-checking multiple layers instead of trusting a single file. In a larger codebase, route handlers, schema definitions, middleware, and docs each carry part of the API contract. Contributing to production-style code is less about writing lots of new code and more about reducing ambiguity so future contributors and users can rely on what is documented.

**How did AI tools help - and where did they fall short?**
AI tools helped most with fast orientation: finding related files, summarizing endpoint flow, and drafting structured documentation language. They fell short on source-of-truth accuracy unless I verified each claim against the repository. I still had to manually confirm request formats, auth expectations, and test scope because plausible suggestions were not always exact for this specific project state.

**What would you do differently if you started over?**
I would create a verification checklist earlier (endpoint, payload type, required fields, auth, example request) and use it before writing any docs text. I would also add the focused contract test earlier in the process so documentation updates and validation moved together from day one. That would have reduced backtracking and increased confidence sooner.

**What are you most proud of from this module?**
I am most proud of treating a documentation issue as an engineering quality task rather than a wording task. I left the API docs more reliable for users, and I backed that improvement with a targeted test to keep the contract visible and verifiable over time.