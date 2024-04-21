clips = {}
while True:
    received = input()
    if received == 'q':
        break
    id, *tags = received.split()
    clips[id] = set(tags)

watched_clips = input().split()
watched_tags = set()
for watched in watched_clips:
    watched_tags = watched_tags | (clips[watched] if watched in clips else set())

filtered = sorted([(-len(watched_tags & t), c) for c, t in clips.items() if c not in watched_clips])
print(' '.join(sorted([c for a, c in filtered if a == filtered[0][0] and a != 0])) or 'No suggested clip')
