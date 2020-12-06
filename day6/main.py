f = open("data.txt", "rt")

current_sum = 0
current_group = {'count': 0}
groups = []

lines = f.readlines()
lines.append('\n')

for line in lines:

  if line == '\n':
    # current_sum += len(current_group.keys())
    groups.append(current_group)

    current_group = {'count' : -1}
  
  line = line.rstrip()
  current_group['count'] = current_group['count'] + 1
  for char in line:
    
    if char in current_group:
      current_group[char] = current_group[char] + 1
    else:
      current_group[char] = 1


current_sum = 0

for i, g in enumerate(groups):
  count = g['count']
  keys = list(g.keys())

  for k in keys:
    if k != 'count' and g[k] == count:
      print(i, k, g[k], count)
      current_sum += 1

  
print ("Current sum is:", current_sum)

f.close()