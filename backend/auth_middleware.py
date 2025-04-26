from fastapi import Request, HTTPException
from fastapi.routing import APIRoute

API_KEY = "serenity_super_secret"  # Store securely in environment variable

class APIKeyMiddleware:
    def __init__(self, app):
        self.app = app

    async def __call__(self, scope, receive, send):
        if scope["type"] == "http":
            headers = dict(scope["headers"])
            api_key = headers.get(b"x-api-key")
            if api_key != API_KEY.encode():
                raise HTTPException(status_code=403, detail="Unauthorized")
        await self.app(scope, receive, send)
