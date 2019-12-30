import json

ip = input('src ip address:')

with open('./incidents.json') as f:
    df = json.load(f)

dst_ip = set()

for ticket in df['tickets']:
    src_ip = ticket['src_ip']
    if src_ip == ip:
        dst_ip.add(ticket['dst_ip'])

print("%i ip addresses were targeted by src_ip." % len(dst_ip))