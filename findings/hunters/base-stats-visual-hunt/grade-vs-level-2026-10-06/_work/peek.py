import os
p = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..',
                 'grade-vs-level-factor-2026-10-06.md')
t = open(p, encoding='utf-8').read()
i = t.find('### T7')
print(t[i:i + 300])
print('...............')
k = t.find('img/rank3-1024x911.jpg')
print(t[max(0, k - 500):k + 150])