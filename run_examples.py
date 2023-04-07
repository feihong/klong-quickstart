from pathlib import Path
import re
from klongpy import KlongInterpreter

klong = KlongInterpreter()

def run_examples():
  with Path('examples.kg').open() as fp:
    for line in fp:
      line = line.strip()
      if line == '':
        continue

      m = re.match(r'\:"(.*)"', line)
      if m:
        yield f'\n## {m.group(1)}\n\n'
        continue

      result = klong(line)
      yield f'    {line}  -->  {result}\n'

with open('examples.md', 'w') as fp:
  fp.write('# Examples\n')
  for line in run_examples():
    fp.write(line)
