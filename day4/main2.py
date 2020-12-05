import re

class Passport:
  def __init__(self, p):
    self.data = {}
    self.process(p)
    
  def __str__(self):
    return f"{self.get('byr',):4} | {self.get('iyr'):4} | {self.get('eyr'):4} | {self.get('hgt', ):6} | {self.get('hcl'):7} | {self.get('ecl'):7} | {self.get('pid'):10} |"

  def process(self, p):
    items = p.strip().split(" ")

    for item in items:
      key = item.split(":")[0]
      value = item.split(":")[1].strip().rstrip()
      self.data[key] = value

  def get(self, fld):
    return self.data.get(fld, "***")


def isValid_passport(p):
  return p.get("byr") != "***" and p.get("iyr") != "***" and p.get("eyr") != "***" and p.get("hgt") != "***" and p.get("hcl") != "***" and p.get("ecl") != "***" and p.get("pid") != "***" 
      
def isValid_byr(p):
  
  byr = p.get("byr") 
  if byr == "***":
    return False

  if 1920 <= int(byr) <= 2002:
    return True

  return False  
 
def isValid_iyr (p):
  iyr = p.get('iyr')

  if (iyr == '***'):
    return False 

  if (2010 <= int(iyr) <= 2020):
    return True

  return True

def isValid_eyr (p):
  eyr = p.get('eyr')

  if (eyr == '***'):
    return False 

  if (2020 <= int(eyr) <= 2030):
    return True

  return True

def isValid_hgt (p):
  hgt = p.get('hgt')

  if (hgt == '***'):
    return False 
  
  return  (hgt[-2:] == "cm" and 150 <= int(hgt[:-2]) <= 193) or (hgt[-2:] == "in" and 59 <= int(hgt[:-2]) <= 76) 

def isValid_hcl(p):
  hcl = p.get("hcl")

  if hcl == '***':
    return False 

  return re.search(r'^#(?:[0-9a-f]{3}){1,2}$', hcl)

  

  return True

def isValid_ecl(p):
  ecl = p.get("ecl")

  if ecl == '***':
    return False 

  return ecl in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    
def isValid_pid(p):
  pid = p.get("pid")

  if pid == '***':
    return False 

  return len(pid) == 9 and pid.isnumeric() 


if __name__ == "__main__":
  f = open("data.txt", "rt")

  lines = f.readlines()

  data = [""]

  # Compile multi line data to single line data
  for line in lines:
    if line == "\n":
      data.append("")
    data[len(data) - 1] = data[len(data) - 1] + " " + line.strip()

  #create a set of passports
  passports = []
  for d in data:
    p = Passport(d)
    passports.append(p)



  p_count = len(passports)
  print(f"Found {p_count} passports")

  filtered_passports = list(filter(isValid_passport, passports))
  p_count = len(filtered_passports)
  print(f"Found {p_count} valid passports")

  filtered_passports = list(filter(isValid_byr, passports))
  p_count = len(filtered_passports)
  print(f"Found {p_count} passports with valid BYR")

  filtered_passports = list(filter(isValid_iyr, filtered_passports))
  p_count = len(filtered_passports)
  print(f"Found {p_count} passports with valid IYR")

  filtered_passports = list(filter(isValid_eyr, filtered_passports))
  p_count = len(filtered_passports)
  print(f"Found {p_count} passports with valid EYR")

  filtered_passports = list(filter(isValid_hgt, filtered_passports))
  p_count = len(filtered_passports)
  print(f"Found {p_count} passports with valid HGT")

  filtered_passports = list(filter(isValid_hcl, filtered_passports))
  p_count = len(filtered_passports)
  print(f"Found {p_count} passports with valid HCL")

  filtered_passports = list(filter(isValid_ecl, filtered_passports))
  p_count = len(filtered_passports)
  print(f"Found {p_count} passports with valid ECL")

  filtered_passports = list(filter(isValid_pid, filtered_passports))
  p_count = len(filtered_passports)
  print(f"Found {p_count} passports with valid PID")


  for p in filtered_passports:
    print (p)




