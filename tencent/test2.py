import os

print(
    os.environ.get("HOMEDRIVE") + (os.environ.get("HOME") or os.environ.get("HOMEPATH"))
)
