# Bobby Yankou
# Artificial Intelligence
# Project #1
# Checkers
# Flatten

# Stolen from http://stackoverflow.com/questions/12976927/getting-all-elements-of-a-python-list-including-sublists
def flatten(iterable):
   out = []
   for i in iterable:
      if hasattr(i,'__iter__'):
         out.extend(flatten(i))
      else:
         out.append(i)
   return out
