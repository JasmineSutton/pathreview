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

**PLAN.md link:** [[link to PLAN.md in your fork]](https://github.com/JasmineSutton/pathreview/blob/enhancement/89-API-Documentation-Update/PLAN.md)

**Walkthrough video (recommended):** [link to your Loom video, ≤2 min — shared for early feedback]

**Blockers or open questions:**
No major blockers. Remaining task is to ensure API.md reflects exact request formats and constraints from code:
POST /profiles uses multipart form data, not JSON.
POST /reviews uses JSON with profile_id.
Login expects OAuth2 form fields username and password.
Mark auth requirements clearly for protected endpoints.
