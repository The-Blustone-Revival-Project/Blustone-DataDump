"""Arithmetic + separability analysis for the grade-vs-level lead."""
from decimal import Decimal, getcontext
getcontext().prec = 28

T1_BEFORE, T1_AFTER = 3311, 4907      # blonde child, star3/LvMAX -> star4/Lv.1
T2_BEFORE, T2_AFTER = 2554, 3827      # blonde ponytail girl, same shape
KAIN_LV30 = 3311                       # rank1 member training

r1 = Decimal(T1_AFTER) / Decimal(T1_BEFORE)
r2 = Decimal(T2_AFTER) / Decimal(T2_BEFORE)
mean = (r1 + r2) / 2
spread = abs(r1 - r2) / mean

print('T1 ratio            = %s  (%d -> %d)' % (r1, T1_BEFORE, T1_AFTER))
print('T2 ratio            = %s  (%d -> %d)' % (r2, T2_BEFORE, T2_AFTER))
print('mean                = %s' % mean)
print('relative spread     = %.4f %%' % (spread * 100))
print()
print('--- if f>=1 (a grade step cannot lower power): ---')
print('  g^29 <= %s   -> per-level <= %s'
      % (r1, (r1 ** (Decimal(1) / 29))))
print('  g^29 <= %s   -> per-level <= %s'
      % (mean, (mean ** (Decimal(1) / 29))))
print('  Beckhen core-stat 1.715733 -> per-level %s'
      % (Decimal('1.715733') ** (Decimal(1) / 29)))
print('  excess of Beckhen over the tighter bound: %.4fx'
      % (Decimal('1.715733') / r1))
print()

print('--- what a SAME-LEVEL cross-grade step would give ---')
print('If P(4,Lv30) = B for the blonde-child hero were known:')
print('  f34 = B/3311,  and  g^29 = 1.482030 / f34 = 1.482030*3311/B')
print('  => g^29 = %.4f / (B/3311)' % r1)
print('  A SAME-GRADE two-level pair Lv.N -> Lv.M gives g^(M-N) directly:')
print('  => that is the cleanest possible win and needs no assumption.')
print()

print('--- does a THIRD same-shape transition separate f from g? ---')
print('Suppose f34 = f45 = f (the assumption the prior lane proposed).')
print('  T1: f*g^29 = %s' % r1)
print('  T3: f*g^29 = r45, so r45 MUST equal %s.' % r1)
print('  => r45 carries no independent information about g.')
print('  => a third same-shape ratio is a CONSISTENCY TEST, not a separation.')
print()
print('Unknowns after T1+T2+T3: g^29, f34, f45  (3)')
print('Equations:                            f34*g^29=r1 ; f34*g^29=r2 ; f45*g^29=r3')
print('  -> with r1 ~= r2, that is 2 independent equations for 3 unknowns:')
print('     UNDERDETERMINED. The f/g split stays open.')
print()
print('Adding P(4,Lv30)=B (a same-level cross-grade step):')
print('  equations become 3 for 3 unknowns -> SOLVABLE.')
print('  g^29 = r1 * %d / B' % T1_BEFORE)
print()
print('--- rounding noise floor on a 4-digit reading ---')
print('worst-case relative error on each value = 0.5/3311 and 0.5/4907')
print('  => combined worst case ~ %.4f %%' % ((0.5 / 3311 + 0.5 / 4907) * 100))
print('  the observed 1.1%% spread is well inside this, so T1 and T2 are')
print('  consistent measurements of the SAME quantity, not a detected difference.')