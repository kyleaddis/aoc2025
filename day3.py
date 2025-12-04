import sys

if len(sys.argv) != 2:
    sys.exit(1)
banks = ""

with open(sys.argv[1]) as f:
    banks = f.read()


def find_battery(bat, bat_str, bat_len, start_index=0, end_index=None):
    if len(bat_str) == bat_len:
        return bat_str
    if end_index is None:
        end_index = len(bat)
    max_value = max(bat[start_index:end_index])
    i = bat.index(max_value, start_index, end_index)

    if i > len(bat) - bat_len + len(bat_str):
        return find_battery(bat, bat_str, bat_len, start_index=start_index, end_index=i)
    else:
        bat_str += max_value
        return find_battery(bat, bat_str, bat_len, start_index=(i + 1), end_index=None)


joltage_2 = []
joltage_12 = []
for bank in banks.split():
    bat = list(bank)
    bat_str = find_battery(bat, "", 12)
    joltage_12.append(int("".join(bat_str)))
    joltage_2.append(int("".join(find_battery(bat, "", 2))))
print(f"Part 1: {sum(joltage_2)}")
print(f"Part 2: {sum(joltage_12)}")
