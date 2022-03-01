from os import getenv
from dotenv import load_dotenv

load_dotenv()
que = {}
admins = {}

API_ID = int(getenv("API_ID", "5056243"))
API_HASH = getenv("API_HASH", "bca20d3b84de3c45b34e5716279b93b5")
BOT_TOKEN = getenv("BOT_TOKEN","5275676202:AAHjsGjeV6XS3-fuL9OhAF2NmKtt_az0TbE")
BOT_NAME = getenv("BOT_NAME","Kaal-music")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "120"))
SESSION_NAME = getenv("SESSION_NAME", "AQC_TNSGQMKF0RqDrfEhJwrcMKWgtSAei2cDSbu_QdgoEj4cEadByt5Q4tBUsjtoG6q47m17w97yGJejAZZOGDTsjLEXnJb_JnEHsIUOJHxSthKjvZI3Nq-RAKhM9sHZf2QKfcyD2_t5U0c0ZzULlLEUXoRDqaSw70bKNx9aF73hYK5Jx3Sag-i3wKHotYKRLNKMlsd5cEQr9WHjUD88Ikl5fx3v_Tak0uLky6XOUm0cd00zXCBEOriLeZDkrHFenCUgbjPQgEoWDJtKpkaF8uRkllYsVDDCCFYYcCVrQlMiwA1sca4soI0RonrpJum0TNgzMhJ-VCFg8fk4hOYWKDjNcJmHiAA")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())
PMPERMIT = getenv("PMPERMIT", "ENABLE")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1783702093").split()))
