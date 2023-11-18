import asyncio
import datetime
import json
import logging
import tempfile
import time
from pathlib import Path

import pydantic

from dib import downloader
from dib.common import Config, HEADERS
from dib.discord import post_image
from dib.utils import arguments_from_pydantic

from croniter import croniter

logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s')
logger = logging.getLogger(__name__)


async def on_cron(config: Config):
    """The main logic"""

    with tempfile.TemporaryDirectory() as tmpdir:
        # Download the image file
        image_path = Path(tmpdir) / 'cam.jpg'
        await downloader.download_image(config.image_url, image_path, headers=HEADERS)

        # Upload the image file to Discord
        await post_image(config.discord_webhook_url, image_path, config.discord_thread_id)


def main(config: Config):
    cron = croniter(config.cron)

    async def _run():
        # Schedule the cron job
        while True:
            next_time = cron.get_next(ret_type=float)
            delay = next_time - time.time()
            logger.info(f'Next run at {datetime.datetime.fromtimestamp(next_time)}. Sleeping for {delay:.2f}s')
            await asyncio.sleep(delay)
            try:
                await on_cron(config)
            except Exception as e:
                logger.exception(e)
            except KeyboardInterrupt:
                logger.info('KeyboardInterrupt, exiting')
                break

    asyncio.run(_run())


def cli():
    logging.basicConfig(level=logging.DEBUG)

    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--config-file', help='Path to the config file.')
    arguments_from_pydantic(parser, Config)
    args = parser.parse_args()

    if args.config_file:
        logger.info('Loading config from {}'.format(args.config_file))
        with open(args.config_file, 'r') as f:
            config = json.load(f)
            config = Config(**config)
    else:
        try:
            config = Config(**vars(args))
        except pydantic.ValidationError as e:
            logger.error('Provided arguments are invalid: {}'.format(e))
            parser.print_help()
            exit(1)

    main(config)


if __name__ == '__main__':
    cli()
