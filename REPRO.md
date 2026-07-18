# Reproduction for Issue #89

Issue: https://github.com/ascherj/pathreview/issues/89

## Summary
I compared `docs/API.md` against current endpoint implementations.  
I confirmed that `POST /profiles` and `POST /reviews` are missing request body schemas in docs.

## What Matches
- Health endpoint in docs matches implementation: `API.md:9`, `health.py:12`
- Auth endpoints match: `API.md:13`, `API.md:14`, `auth.py:19`, `auth.py:66`
- Profile create/get/delete match: `API.md:18`, `API.md:19`, `API.md:20`, `profiles.py:23`, `profiles.py:111`, `profiles.py:196`
- Review create/get/list match: `API.md:24`, `API.md:25`, `API.md:26`, `reviews.py:22`, `reviews.py:65`, `reviews.py:101`

## Implemented But Not Documented
- Root endpoint exists but is undocumented: `main.py:98`
- Profile update endpoint is missing from docs: `profiles.py:147`
- Review status endpoint is missing from docs: `reviews.py:139`

## API Contract Gaps
- Login payload format not specified; implementation expects OAuth2 form fields `username` and `password` (not JSON email/password): `auth.py:68`
- Profile creation docs imply resume + GitHub username, but implementation accepts multipart form fields `github_username`, `portfolio_url`, and optional file upload: `profiles.py:25`, `profiles.py:26`, `profiles.py:27`
- Auth requirement is undocumented for profiles/reviews routes; implementation requires bearer auth via dependency injection: `profiles.py:28`, `reviews.py:26`, `auth.py:18`
- Health docs are high-level only; implementation returns dependency statuses and may return 503 with detail payload when unhealthy: `health.py:18`, `health.py:84`
- Docs say GET review retrieves a completed review, but implementation returns by ID regardless of status: `API.md:25`, `reviews.py:65`, `review.py:18`

## Issue-specific Observation
For issue #89 specifically, request body schemas are missing in `docs/API.md` for:
- `POST /profiles`
- `POST /reviews`