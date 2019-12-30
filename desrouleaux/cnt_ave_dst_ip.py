import json

with open('./incidents.json') as f:
    df = json.load(f)

files = {}

for ticket in df['tickets']:
    file_hash = ticket['file_hash']
    dst_ip = ticket['dst_ip']
    if not file_hash in files:
        files[file_hash] = [dst_ip]
    elif not dst_ip in files[file_hash]:
        files[file_hash].append(dst_ip)

cnt_ip = 0
cnt_file = len(files)
for v in files.values():
    cnt_ip += len(v)

print('files: %i' % cnt_file)
print("the number of unique ips a file is sent, on average is {0:.2f}".format(cnt_ip / cnt_file))