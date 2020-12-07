f = open("data.txt", "rt")

types = {}

def extractRule (rule):
  original = rule;

  rule = rule.strip()
  rule = rule.rstrip()

  
  if rule[0] == " ":
    rule = rule[1:]

  if rule[-1] == ".":
    rule = rule[:-1]

  rule = rule.rstrip()[2:-1].split(" ")[0] + " " + rule.rstrip()[2:-1].split(" ")[1]
  
  return 
  

def parseHoldRule(holdStr):
  h = holdStr.strip()
  return {'count': h.split(" ")[0], 'bag': h.split(" ")[1] + " " + h.split(" ")[2]}

def parseHoldsStr(holdStrs):
  holdRules = holdStrs.split(",")

  holds = map (parseHoldRule, holdRules)
  return list(holds)

def buildBagsHold (lines):
  for line in lines:
    #get bag name
    bagColour = line.split("contain")[0]

    #get the holds string.
    holdsStr = line.split("contain")[1].rstrip()
    #remove the leading space
    holdsStr = holdsStr[1:]

    # remove the trailing full stop.
    if holdsStr[-1] == ".":
      holdsStr = holdsStr[:-1]

    print (holdsStr)

    if holdsStr.rstrip() == "no other bags":
      holds = [] 
    else:
      holds = parseHoldsStr(holdsStr)

    #  rules = list(map(extractRule, rules))
      
    types[bagColour[:-6]] = {'id': bagColour[:-6], 'holds':holds, 'heldBy': []}


# This builds the data structure, a kind of double linked list.
# 
def buildBagsHeld (types):

  #loop through bags
  for bagKey in types:

    bag= types[bagKey]
    holds = bag['holds']

    #add held by 
    for holdBag in holds: 
      key = holdBag['bag']
      heldBag = types[key]
      heldBag['heldBy'].append({'parent': bagKey, 'holds': holdBag['count']}) 


lines = list(f.readlines())

#Build Holds Structure
buildBagsHold(lines)


buildBagsHeld (types)


for t in types:
  print(t, types[t])

print ()
print()


def listBags(target, result):
  bag = types[target]
  

  childHolds = 0
  #if not(target in result):
  #  result.append(target)

  #print(target)
  for t in bag['heldBy']:
    
    result.append(t)
    children, result = listBags(t['parent'], result)
    childHolds += children * int(t['holds'])

  return len(bag['holds']) +  childHolds, result



  

def countBags(bag):
  count = 0
  me = 1

  if len(bag['holds']) == 0:
    return me 
  
  for h in bag['holds']:
    holds = int(h['count'])
    childBags = holds * countBags(types[h['bag']])

    count +=  childBags
  
  
  return me + count  


target = "shiny gold"
print ("Searching for ", target)
result = []
holds, result = listBags(target, result)
#print (holds, len(result))

for r in result:
  print(r)

bags = countBags(types["shiny gold"])
print(bags -  1)
f.close()

