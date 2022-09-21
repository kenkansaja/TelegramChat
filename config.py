import os

TOKEN = os.environ.get("TOKEN", None) # Dapatkan di @botfather
OWNER = os.environ.get("OWNER", "kenkanasw") # Isi dengan username kalian tanpa tanda @
GROUP = os.environ.get("GROUP", "aruna_mutual") # Isi dengan username group kalian tanpa tanda @ kalau gak punya gak usah isi
CHANNEL = os.environ.get("CHANNEL", "gabutan_escape") # Isi dengan username channel kalian tanpa tanda @ kalau gak punya gak usah isi
DB_URI = os.environ.get("DATABASE_URL", "")
