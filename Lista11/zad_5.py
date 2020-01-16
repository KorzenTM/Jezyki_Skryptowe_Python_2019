import re

string ="PythonExercises"
print(re.sub('([A-Z])', r' \1', string))