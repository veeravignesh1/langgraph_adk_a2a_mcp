from pydantic import BaseModel


class Settings(BaseModel):
    mcp_prefix: str = "/llm"


settings = Settings()
