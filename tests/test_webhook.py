import json
import os
from pathlib import Path

import httpx

CUR_DIR = Path(__file__).parent

# Read test secret from env
DISCORD_WEBHOOK_ID = os.environ['DISCORD_WEBHOOK_ID']
DISCORD_WEBHOOK_TOKEN = os.environ['DISCORD_WEBHOOK_TOKEN']
DISCORD_THREAD_ID = os.environ['DISCORD_THREAD_ID']


def test_webhook():
    url = f"https://discord.com/api/webhooks/{DISCORD_WEBHOOK_ID}/{DISCORD_WEBHOOK_TOKEN}"
    image_url = "https://live8p.brownrice.com/cam-images/sevensprings.jpg"

    data = {
        "embeds": [{
            "image": {
                "url": image_url
            }
        }]
    }

    params = {
        "thread_id": DISCORD_THREAD_ID
    }

    headers = {
        "Content-Type": "application/json"
    }

    req = httpx.post(url, json=data, params=params, headers=headers)
    print(req.status_code)
    print(req.text)
    assert req.is_success


def test_webhook_local_image():
    url = f"https://discord.com/api/webhooks/{DISCORD_WEBHOOK_ID}/{DISCORD_WEBHOOK_TOKEN}"
    image_path = CUR_DIR / 'data' / "test_image.jpg"
    image_name = 'test.png'

    data = {
        "content": "test",
        "embeds": [{
            "image": {
                "url": f"attachment://{image_name}"
            }
        }]
    }

    params = {
        "thread_id": DISCORD_THREAD_ID
    }

    headers = {
        "Content-Type": "multipart/form-data"
    }

    files = {
        "payload_json": (None, json.dumps(data).encode(), "application/json"),
        "files[0]": (image_name, open(image_path, "rb"), "image/jpeg")
    }

    req = httpx.post(url, files=files, params=params, headers=headers)
    print(req.status_code)
    print(req.text)
    assert req.is_success


def test_discordwebhook():
    from discordwebhook import Webhook, File
    image = str(CUR_DIR / 'data' / "test_image.jpg")

    url = f'https://discord.com/api/webhooks/{DISCORD_WEBHOOK_ID}/{DISCORD_WEBHOOK_TOKEN}'

    params = {
        "thread_id": DISCORD_THREAD_ID
    }

    url = url + '?' + '&'.join([f'{k}={v}' for k, v in params.items()])

    webhook = Webhook(url)
    attach_file = File(path=image)
    webhook.send_sync(content='test', file=attach_file)
