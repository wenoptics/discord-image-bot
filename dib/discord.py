from pathlib import Path

from discordwebhook import Webhook, File


async def post_image(webhook_url: str, image_path: Path, thread_id: str = None):
    """Post an image to a Discord webhook."""

    if thread_id is not None:
        # Construct the webhook URL with the thread ID
        webhook_url = webhook_url + f"?thread_id={thread_id}"

    webhook = Webhook(url=webhook_url)
    attached_file = File(path=str(image_path))

    await webhook.send(file=attached_file)
