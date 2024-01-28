#    This file is part of the Compressor distribution.
#    Copyright (c) 2021 Danish_00
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, version 3.
#
#    This program is distributed in the hope that it will be useful, but
#    WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
#    General Public License for more details.
#
# License can be found in <
# https://github.com/1Danish-00/CompressorQueue/blob/main/License> .

from decouple import config

try:
    APP_ID = config("APP_ID", 4018758)
    API_HASH = config("API_HASH", "622bba3cf046315531f71f9d97fa6c2a")
    BOT_TOKEN = config("BOT_TOKEN", "5822396703:AAG7sX8J2gaYpF9J_ZHGphpqZ4VXSdpF-P8")
    DEV = 5385471287
    OWNER = config("OWNER", "5385471287")
    FFMPEG = config("FFMPEG", "ffmpeg -i '''{}''' -preset ultrafast -c:v libx265 -crf 27 -map 0:v -c:a aac -map 0:a -c:s copy -map 0:s? '''{}'''")
    THUMB = config("THUMBNAIL", "https://telegra.ph//file/5808b35c7a279a8bcdc99.jpg")
except Exception as e:
    LOGS.info("Environment vars Missing")
    LOGS.info("something went wrong")
    LOGS.info(str(e))
    exit(1)
