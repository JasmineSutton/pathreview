"""API contract tests for documented request bodies."""

import pytest

from api.main import app


@pytest.mark.unit
def test_profiles_and_reviews_endpoints_expose_request_bodies():
    """Ensure the FastAPI schema documents request bodies for the documented endpoints."""
    schema = app.openapi()

    profiles_post = schema["paths"]["/profiles"]["post"]
    assert "requestBody" in profiles_post
    assert "multipart/form-data" in profiles_post["requestBody"]["content"]

    multipart_schema = profiles_post["requestBody"]["content"]["multipart/form-data"]["schema"]
    assert "$ref" in multipart_schema
    assert multipart_schema["$ref"] == "#/components/schemas/Body_create_profile_endpoint_profiles_post"

    reviews_post = schema["paths"]["/reviews"]["post"]
    assert "requestBody" in reviews_post
    assert "application/json" in reviews_post["requestBody"]["content"]

    json_schema = reviews_post["requestBody"]["content"]["application/json"]["schema"]
    assert "$ref" in json_schema
    assert json_schema["$ref"] == "#/components/schemas/ReviewCreate"
