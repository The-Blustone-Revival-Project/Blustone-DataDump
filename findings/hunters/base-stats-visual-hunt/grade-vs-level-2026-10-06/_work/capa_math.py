"""Capacity-transcendence core-stat multiplier + archive-vs-Lv1 per-stat mismatch."""
from decimal import Decimal as D, getcontext
getcontext().prec = 28

# in-game, Bear 036, star3 / Lv.1, BEFORE capacity transcendence (capa2 frame)
G = {'atk': D(365), 'def': D(423), 'hp': D(619), 'cp': D(2326)}
# in-game, same frame, AFTER one capacity transcendence
A = {'atk': D(401), 'def': D(465), 'hp': D(681), 'cp': D(2704)}
# 2019 JP archive profile row for 036 (level and gear not established)
R = {'atk': D(755), 'def': D(864), 'hp': D(1923), 'cp': D(10011)}

print('=== T6  capacity transcendence, grade AND level both fixed ===')
print('hero 036 Bear, star3 / Lv.1, one キャパ超越')
for k, label in (('atk', 'ATK'), ('def', 'DEF'), ('hp', 'HP '), ('cp', 'CP ')):
    r = A[k] / G[k]
    print('  %s %5s -> %5s   x%s' % (label, G[k], A[k], r.quantize(D('0.000001'))))
core = [A[k] / G[k] for k in ('atk', 'def', 'hp')]
lo, hi = min(core), max(core)
print('  core-stat spread      = %.4f %%  (min %s max %s)'
      % ((hi - lo) / lo * 100, lo.quantize(D('0.000001')),
         hi.quantize(D('0.000001'))))
print('  3-stat mean           = %s' % (sum(core) / 3).quantize(D('0.000001')))
print('  cumulative over 3     = %s  (guide: max 3, one per rank-up)'
      % ((sum(core) / 3) ** 3).quantize(D('0.000001')))
print('  CP / core ratio       = %s'
      % ((A['cp'] / G['cp']) / (sum(core) / 3)).quantize(D('0.000001')))
print('  => CP grows ~%s %% faster than the core stats under an operation'
      % ((((A['cp'] / G['cp']) / (sum(core) / 3)) - 1) * 100).quantize(D('0.001')))
print('     that changes NEITHER grade NOR level.')
print()

print('=== archive row vs in-game star3/Lv.1, same hero 036 ===')
for k, label in (('atk', 'ATK'), ('def', 'DEF'), ('hp', 'HP '), ('cp', 'CP ')):
    print('  %s archive %5s / Lv.1 %4s = %s'
          % (label, R[k], G[k], (R[k] / G[k]).quantize(D('0.0001'))))
rat = [R[k] / G[k] for k in ('atk', 'def', 'hp')]
print('  the three core-stat ratios span %.2fx -> a SINGLE per-level scalar'
      % (max(rat) / min(rat)))
print('  CANNOT map archive -> Lv.1 across HP, ATK and DEF at once.')
print()

print('=== sanity: is 365/423/619 consistent with a 1.0992 step applied to')
print('    anything the archive reports for 036? ===')
for k, label in (('atk', 'ATK'), ('def', 'DEF'), ('hp', 'HP ')):
    print('  archive %s %5s / 1.0992 = %s' % (label, R[k],
                                             (R[k] / (sum(core) / 3)).quantize(D('0.001'))))
print('  (not a level statement -- the archive star and level are unknown;')
print('   printed only to show no single multiplier explains it.)')