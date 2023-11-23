import os

TOKEN = os.environ.get("TOKEN", None) # Dapatkan di @botfather
OWNER = os.environ.get("OWNER", "rChoiHyunWook") # Isi dengan username kalian tanpa tanda @
GROUP = os.environ.get("GROUP", "mutualanstaryy") # Isi dengan username group kalian tanpa tanda @ kalau gak punya gak usah isi
CHANNEL = os.environ.get("CHANNEL", "randomajaboss") # Isi dengan username channel kalian tanpa tanda @ kalau gak punya gak usah isi
DB_URI = os.environ.get("DATABASE_URL", "")
