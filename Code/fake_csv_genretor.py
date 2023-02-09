import csv
import random
import string
# The script generates a CSV file containing Random Mac Addresses
with open("music_players.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["mac_addresses"])
    for i in range(999):
        mac_address = ':'.join(["{:02x}".format(random.randint(0, 255)) for j in range(6)])
        writer.writerow([mac_address])
