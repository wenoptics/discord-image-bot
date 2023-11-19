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

