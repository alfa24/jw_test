import json

from rest_framework.test import APIClient


class DRFClient(APIClient):
    def get(self, *args, **kwargs):
        return self._api_call(
            "get", kwargs.get("expected_status_code", 200), *args, **kwargs
        )

    def post(self, *args, **kwargs):
        return self._api_call(
            "post", kwargs.get("expected_status_code", 201), *args, **kwargs
        )

    def put(self, *args, **kwargs):
        return self._api_call(
            "put", kwargs.get("expected_status_code", 200), *args, **kwargs
        )

    def delete(self, *args, **kwargs):
        return self._api_call(
            "delete", kwargs.get("expected_status_code", 204), *args, **kwargs
        )

    def _api_call(self, method, expected, *args, **kwargs):
        kwargs["format"] = kwargs.get(
            "format", "json"
        )  # by default submit all data in JSON
        as_response = kwargs.pop("as_response", False)

        method = getattr(super(), method)
        response = method(*args, **kwargs)

        if as_response:
            return response

        content = self._decode(response)

        assert (
            response.status_code == expected
        ), f"non-expected statuscode: {response.status_code}: {content}"

        return content

    def _decode(self, response):
        if not len(response.content):
            return

        content = response.content.decode("utf-8", errors="ignore")
        if "application/json" in response.headers["Content-Type"]:
            return json.loads(content)
        else:
            return content
