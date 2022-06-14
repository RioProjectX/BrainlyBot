BOT_TOKEN = getenv('BOT_TOKEN')
API_ID = int(getenv('API_ID', "12"))
API_HASH = getenv('API_HASH')
MUST_JOIN = getenv("MUST_JOIN", None)
if MUST_JOIN.startswith("@"):
    MUST_JOIN = MUST_JOIN.replace("@", "")
