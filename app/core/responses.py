from fastapi import APIRouter, Response, Body, Depends, Request
import json
import typing

class PrettyJSONResponse(Response):
    media_type = "application/json"

    def render(self, content: typing.Any) -> bytes:
        return json.dumps(
            content,
            ensure_ascii=False,
            allow_nan=False,
            indent=6,
            separators=(", ", ": "),
        ).encode("utf-8")
