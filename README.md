# Discord image posting bot

Fetch images from a given URL and post them to a Discord channel periodically. 
 Supports CRON syntax for scheduling.

## Usages

### CLI

```bash
$ dib -h
```

```text
usage: __main__.py [-h] [--config-file CONFIG_FILE]
                   [--discord_webhook_url DISCORD_WEBHOOK_URL]
                   [--discord_thread_id DISCORD_THREAD_ID]
                   [--image_url IMAGE_URL] [--cron CRON] [--timeout TIMEOUT]

options:
  -h, --help            show this help message and exit
  --config-file CONFIG_FILE
                        Path to the config file.
  --discord_webhook_url DISCORD_WEBHOOK_URL
  --discord_thread_id DISCORD_THREAD_ID
  --image_url IMAGE_URL
  --cron CRON
  --timeout TIMEOUT
```

### Docker

Image: [wenoptics/discord-image-bot:latest](https://hub.docker.com/r/wenoptics/discord-image-bot)

Docker compose usage example:

```yaml
version: "3.8"
services:
  mountaincam-7s-bot:
    image: wenoptics/discord-image-bot:0.1.0
    command:
      - --discord_webhook_url
      - https://discord.com/api/webhooks/<your-secret>/<your-secret-token>
      - --image_url
      - https://live8p.brownrice.com/cam-images/sevensprings.jpg
      # Every 45 minutes
      - --cron
      - '*/45 * * * *'
```
