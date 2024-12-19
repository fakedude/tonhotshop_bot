import asyncio

import uvloop
from pyrogram.client import Client
from pytgcalls import PyTgCalls, idle
from pytgcalls.filters import stream_end
from pytgcalls.types import MediaStream, Update
from pytgcalls.types.raw import AudioParameters

from config import (API_HASH, API_ID, CHANNEL, MAX_CONCURRENT_TRANSMISSIONS,
                    NAME, SESSION_STRING, STREAM_URL)
from utils.logger import init_module_loggers, logger_factory

init_module_loggers("asyncio", "pytgcalls")
logger = logger_factory("main")


async def handler(client: PyTgCalls, update: Update):
    logger.warning("stream_end: %s", update)


async def main():
    client = Client(name=NAME, api_id=API_ID, api_hash=API_HASH,
                    session_string=SESSION_STRING, max_concurrent_transmissions=MAX_CONCURRENT_TRANSMISSIONS)
    app = PyTgCalls(client)
    app.add_handler(handler, stream_end)  # type: ignore
    await app.start()  # type: ignore
    await app.play(CHANNEL, MediaStream(media_path=STREAM_URL,  # type: ignore
                                        audio_parameters=AudioParameters(bitrate=44100, channels=2),
                                        audio_flags=MediaStream.Flags.AUTO_DETECT,
                                        video_flags=MediaStream.Flags.IGNORE))
    logger.info("pyrogram key: %s", await client.export_session_string())
    await idle()
    app.remove_handler(handler)  # type: ignore


if __name__ == '__main__':
    uvloop.install()
    asyncio.run(main())
