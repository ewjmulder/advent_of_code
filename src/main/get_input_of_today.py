import os
import requests
from datetime import datetime

now = datetime.now()
if now.month != 12:
    print("It's not even december yet, have a little patience! :)")
elif now.hour < 6:
    print("It's still too early, have a little patience! :)")
else:
    print("Going to get the input for you!")
    day_of_month = now.day
    input_url = f"https://adventofcode.com/{now.year}/day/{day_of_month}/input"
    output_file = f"dec{day_of_month}/input"

    headers = {"Cookie": f"session={os.environ['SESSIONID']}"}

    r = requests.get(input_url, headers=headers)
    with open(output_file, 'wb') as f:
        for chunk in r.iter_content(1024):
            f.write(chunk)

    print(f"Saved {input_url} in {output_file}, good luck!")
