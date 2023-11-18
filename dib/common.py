import pydantic

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 '
                  '(KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36',
}


class Config(pydantic.BaseModel):
    discord_webhook_url: str
    discord_thread_id: str = None

    image_url: str
    cron: str

    timeout: int = 10
