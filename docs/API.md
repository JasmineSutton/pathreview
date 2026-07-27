# API Reference

Base URL: `http://localhost:8000`

## Endpoints

### Health

`GET /health` — Returns service status and dependency health.

### Authentication

`POST /auth/register` — Create a new account.
`POST /auth/login` — Obtain a JWT access token.

### Profiles

`POST /profiles` — Create a profile with optional resume upload. Requires Bearer authentication.

Request Body (multipart/form-data)

Fields:
- `github_username` (string, optional): GitHub username for the profile. Maximum length: 255 characters. Example: `octocat`.
- `portfolio_url` (string, optional): Portfolio URL associated with the profile. Maximum length: 500 characters. Example: `https://github.com/octocat`.
- `resume_file` (file, optional): Resume file to upload. Accepted formats: PDF or Markdown. Example: `resume.md`.

Example:

```bash
curl -X POST http://localhost:8000/profiles \
  -H "Authorization: Bearer <token>" \
  -F "github_username=octocat" \
  -F "portfolio_url=https://github.com/octocat" \
  -F "resume_file=@resume.md"
```

`GET /profiles/{profile_id}` — Retrieve a profile.
`DELETE /profiles/{profile_id}` — Delete a profile and associated data.

### Reviews

`POST /reviews` — Request a new portfolio review for a profile. Requires Bearer authentication.

Request Body (application/json)

```json
{
  "profile_id": "123e4567-e89b-12d3-a456-426614174000"
}
```

Fields:
- `profile_id` (string, required): UUID of the profile to review. Example: `123e4567-e89b-12d3-a456-426614174000`.

`GET /reviews/{review_id}` — Retrieve a completed review.
`GET /reviews` — List reviews for the authenticated user (paginated).

## Interactive Docs

When the API is running, visit:
- **Swagger UI:** http://localhost:8000/docs
- **ReDoc:** http://localhost:8000/redoc
