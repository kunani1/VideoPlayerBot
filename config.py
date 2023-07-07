"""
VideoPlayerBot, Telegram Video Chat Bot
Copyright (c) 2021  Asm Safone <https://github.com/AsmSafone>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>
"""

import os
from os import getenv
from dotenv import load_dotenv

load_dotenv()

admins = {}
OLD_PMS = {}
AUDIO_CALL = {}
VIDEO_CALL = {}
API_ID = "2929027"
API_HASH = "2beecc3ee357e6e3f2b2e783d4159f9f"
BOT_TOKEN = "1799299844:AAHXWUfImCIP3FRC6DDYB_41xCjAOkZHo-k"
SESSION_STRING = "BQAlz9hB87KVAkMWGyTVkicRi_gGB1veYjTtZbWNt8GaDpYrpo9M62zPQAGMLUgUNJlF1lJq-PklbeQ1DW-AO55QOgCCslM2tAd5M5wc0CRZ-C-FDrQHsz00CHsxnstqpAbrUgeJfMd4hH_ABRUU6ekHLxtbCG3YhmGSl84_xGgdkEwhS23djoWmAaMfQ8fX93R8_U9dW4vTJIfzEMJ_q20R8saisK6XUaoyxOGZXm2rrKiHzs_pe2s4CQ-9yMCK1OCdhhprjOMPs-LvmvzTOFI8pBnLCScoQloUbyDUSuZEDfNW5YH3DMPuH9Xqin-632rulmJv-QLpjd7AOql6LW0MAAAAAUzwIWEA"
SUPPORT_GROUP = ""
UPDATES_CHANNEL = ""
ASSISTANT_NAME = "Epic12484"
SUDO_USERS = "959184369"
REPLY_MESSAGE = "Hello Sir, I'm a bot to stream videos on telegram voice chat, not having time to chat with you 😂!"
if not REPLY_MESSAGE:
    REPLY_MESSAGE = None
else:
    REPLY_MESSAGE = REPLY_MESSAGE
