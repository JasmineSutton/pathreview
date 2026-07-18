## Solution plan

**Issue:**  https://github.com/jamjamgobambam/pathreview/issues/89 - API reference doc is missing the POST /profiles request body schema #89

### Understand
What is the root cause of this issue? What behavior is expected vs. actual?

Root cause:
docs/API.md currently documents response schemas but omits request body schemas for two POST endpoints: POST /profiles and POST /reviews.

Expected behavior:
API reference should include both request and response schemas for each endpoint, including:

    field names
    types/constraints
    descriptions
    example values

Actual behavior:
For POST /profiles and POST /reviews, readers can see what comes back, but not what payload they must send.
Map

Likely scope is documentation-only.

### Map
Which files, functions, or modules are involved?
List the specific files you expect to touch.

Primary file to touch:
    docs/API.md

### Plan
What are the steps to fix this issue?
Break it into 3–5 concrete sub-tasks.

Plan

    Inspect current endpoint sections in docs/API.md for POST /profiles and POST /reviews format/style.

    Add “Request Body” schema blocks for each endpoint, matching existing doc conventions.
    
    Document each field with type, required/optional status, description, and example values.
    
    Validate consistency (naming, JSON examples, markdown formatting, and heading structure).
    
    QA pass to ensure no ambiguity and examples are copy/paste-friendly.

### Inputs & outputs
What does your fix take as input? What should it produce or change?

Inputs to fix:

    Existing endpoint behavior/contracts (from code/tests or existing examples)
    Current structure/style in docs/API.md
    Issue requirements (include schema + field descriptions + example values)

Outputs / changes produced:

    Updated docs/API.md with request body schemas for:
        POST /profiles
        POST /reviews
    Clear, complete request examples aligned with current API contract.

### Risks & unknowns
What could go wrong? What are you still unsure about?

Schema drift risk: Doc updates may not match actual server validation if inferred incorrectly.
    Required vs optional uncertainty: If not explicit in code/tests, docs may overstate requirements.
    Field constraints missing: Length/range/enums might be undocumented in code, making docs vague.
    Formatting mismatch: Could break consistency with rest of API docs.

Unknowns to confirm:

    Exact required fields for both endpoints
    Whether nested objects/arrays exist in either request body
    Any defaults, validation rules, or nullable fields

### Edge cases
What inputs or states should your fix handle gracefully?

The updated docs should gracefully handle/clarify:

    Missing optional fields
    Empty strings vs omitted fields
    Null handling (allowed or not)
    Extra/unknown fields (ignored vs rejected)
    Validation constraints (min/max length, enum values, rating bounds, etc.)
    Content type expectations (application/json) and malformed JSON behavior (if documented elsewhere)

------------



