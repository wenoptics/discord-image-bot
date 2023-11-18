import logging
from pathlib import Path

import aiohttp


logger = logging.getLogger(__name__)


async def download_image(url: str, dst: Path, headers: dict = None):
    """Download an image from a URL and save it to a destination path."""
    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers) as response:
            _bytes = await response.read()
            logger.debug(f"Downloaded {len(_bytes)} bytes from {url}")

            with open(dst, 'wb') as f:
                f.write(_bytes)
                logger.info(f"Downloaded image from {url} to {dst}")
