age = int(input('How old are you?\n'))

decade = age // 10
year = age % 10

print(f"You are {f'{decade} decades' if decade > 1 else f'{decade} decade'} and {f'{year} years' if year > 1 else f'{year} year'} old")