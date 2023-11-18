import asyncio
import os

import pytest

from dib.common import Config
from dib.__main__ import main, on_cron

# Read test secret from env
DISCORD_WEBHOOK_ID = os.environ['DISCORD_WEBHOOK_ID']
DISCORD_WEBHOOK_TOKEN = os.environ['DISCORD_WEBHOOK_TOKEN']
DISCORD_THREAD_ID = os.environ['DISCORD_THREAD_ID']


@pytest.mark.skip(reason="Manual test")
def test_entrance():
    config = Config(
        cron='*/2 * * * *',  # Every 2 minutes
        image_url='https://live8p.brownrice.com/cam-images/sevensprings.jpg',
        discord_webhook_url=f"https://discord.com/api/webhooks/{DISCORD_WEBHOOK_ID}/{DISCORD_WEBHOOK_TOKEN}",
        discord_thread_id=DISCORD_THREAD_ID
    )

    main(config)


def test_work_load():
    config = Config(
        cron='*/2 * * * *',  # Every 2 minutes
        # image_url='https://live8p.brownrice.com/cam-images/sevensprings.jpg',
        image_url='https://b7.hdrelay.com/camera/14ced094-b906-401c-bd83-06dc36f4c2db/snapshot',
        discord_webhook_url=f"https://discord.com/api/webhooks/{DISCORD_WEBHOOK_ID}/{DISCORD_WEBHOOK_TOKEN}",
        discord_thread_id=DISCORD_THREAD_ID
    )

    asyncio.run(on_cron(config))
