from pathlib import Path
import re
import random
from klongpy import KlongInterpreter

random.seed(73)
klong = KlongInterpreter()

input_file = Path('cheatsheet.kg')
output_file = input_file.with_suffix('.md')

def run_examples():
  with input_file.open() as fp:
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

with output_file.open('w') as fp:
  fp.write('# Examples\n')
  for line in run_examples():
    fp.write(line)
