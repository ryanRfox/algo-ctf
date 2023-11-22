import subprocess

my_keyword = "" # TODO: replace "" with your 3 character KEYWORD using only letters A - Z and numbers 2 - 7 (e.g. "FOX")

subprocess.run(["algokit", "task", "vanity-address", my_keyword, "--output", "file", "--file-path", ".env_account"])
