from itertools import chain

def filetorawlist(filename):
  with open(filename, 'r') as f:
    return f.readlines()

def filetolist(filename):
  with open(filename, 'r') as f:
    return [s.strip() for s in f.readlines()]

def filetointcode(filename):
  with open(filename, 'r') as f:
    return [int(x) for x in list(chain(*[l.split(",") for l in [s.strip() for s in f.readlines()]]))]

def filetointcodelist(filename):
  with open(filename, 'r') as f:
    return [[int(x) for x in l.split(",")] for l in [s.strip() for s in f.readlines()]]

def filetointlist(filename):
  return [int(x) for x in filetolist(filename)]

def splitclean(s, delimiter):
  return s.strip().split(delimiter)

def filetointlistlist(filename, delimiter=" "):
  return [[int(y) for y in splitclean(x, delimiter)] for x in filetolist(filename)]

def filetowordlist(filename):
  return filetolist(filename)

def filetowordlistlist(filename, delimiter=" "):
  return [splitclean(x, delimiter) for x in filetolist(filename)]

def filetocharlist(filename):
  return list("".join(filetolist(filename)))

def filetocleancharlist(filename):
  return list("".join([x.strip() for x in filetolist(filename)]))

def filetocharlistlist(filename):
  return [list(x) for x in filetolist(filename)]

def filetocleancharlistlist(filename):
  return [list(x.strip()) for x in filetolist(filename)]

def maxi(l):
  return l.index(max(l))

def maxdictval(d):
  return max(d.values())

def mini(l):
  return l.index(min(l))

def mindictval(d):
  return min(d.values())

def vecadd(v1, v2):
  return tuple([sum(x) for x in zip(v1, v2)])

def vecminus(v1, v2):
  return tuple([(x[0] - x[1]) for x in zip(v1, v2)])

def manhattan_dist(v1, v2):
  return sum([abs(x[0] - x[1]) for x in zip(v1, v2)])

def adj4(loc):
  return [(loc[0], loc[1] - 1), (loc[0] - 1, loc[1]), (loc[0] + 1, loc[1]), (loc[0], loc[1] + 1)]

def adj8(loc):
  return [(loc[0] - 1, loc[1] - 1), (loc[0], loc[1] - 1), (loc[0] + 1, loc[1] - 1), (loc[0] - 1, loc[1]), (loc[0] + 1, loc[1]), (loc[0] - 1, loc[1] + 1), (loc[0], loc[1] + 1), (loc[0] + 1, loc[1] + 1)]

def adj_all(loc):
  if len(loc) == 1:
    return set([(loc[0] - 1,), (loc[0] + 1,)])
  else:
    adj = set()
    adj_lower = adj_all(loc[1:])
    a, b, c = (loc[0] - 1,), (loc[0],), (loc[0] + 1,)
    adj.update(map(lambda x: a + x, adj_lower))
    adj.update(map(lambda x: b + x, adj_lower))
    adj.update(map(lambda x: c + x, adj_lower))
    adj.add(a + loc[1:])
    adj.add(c + loc[1:])
    return adj

def nthsmallestval(l, n):
  return sorted(list(set(l)))[n]

def sortreading(l):
  return sorted(l, key = lambda x: (x[1], x[0]))

def clear_terminal():
  print(chr(27) + "[2J")

def print_at_loc(loc, s):
  print("\033[" + str(loc[1]) + ";" + str(loc[0]) + "H" + str(s))



