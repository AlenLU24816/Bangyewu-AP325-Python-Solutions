n, m  = map(int, input().split())
team_masks = dict()
for i in range(m):
    mask = 0
    team = set(input())
    for char in team:
        mask += (1 << (ord(char) - ord("A")))
    if mask not in team_masks:
        team_masks[mask] = 1
    else:
        team_masks[mask] += 1
del team

full_teams = (1 << n)-1

ANS = 0
print(team_masks)
for team, quantity in team_masks.items():
    for _ in range(quantity):
        if (full_teams-team) in team_masks and team_masks[full_teams-team] != 0:
            team_masks[full_teams-team]-=1
            team_masks[team]-=1
            ANS+=1
print(ANS)