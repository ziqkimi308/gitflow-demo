DEFAULT_LANGUAGE = "en"
MAX_NAME_LENGTH = 50
SUPPORTED_LANGUAGES = ["en", "ms", "zh"]

def get_config():
    return {
        "language": DEFAULT_LANGUAGE,
        "max_name_length": MAX_NAME_LENGTH,
        "supported_languages": SUPPORTED_LANGUAGES
    }