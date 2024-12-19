import asyncio

import uvloop
from pyrogram.client import Client
from pytgcalls import PyTgCalls, idle
from pytgcalls.types import AudioQuality, MediaStream, VideoQuality

from config import (API_HASH, API_ID, BACKGROUND, CHANNEL, NAME,
                    SESSION_STRING, STREAM_URL)


async def main():
    client = Client(name=NAME, api_id=API_ID, api_hash=API_HASH, session_string=SESSION_STRING)
    app = PyTgCalls(client)
    await app.start()  # type: ignore
    await app.play(CHANNEL, MediaStream(BACKGROUND, audio_path=STREAM_URL,  # type: ignore
                                        audio_parameters=AudioQuality.HIGH,
                                        video_parameters=VideoQuality.HD_720p))
    print(await client.export_session_string())
    await idle()


if __name__ == '__main__':
    uvloop.install()
    asyncio.run(main())
