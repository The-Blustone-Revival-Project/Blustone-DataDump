# Arena parser literals: original Thumb register corroboration

2026-10-04. Read-only original ELF PT_LOAD reads and Capstone Thumb instructions. All G addresses below equal ELF+0x10000. This is deliberately independent of greedy LDR/next-ADD resolver pairing.

- **ParseSeason G942e24 first field `season_no`.** LDRr1 G942e34 reads slotG9430d8 word0x14304d8; ADD r1,pc G942e42 uses architectural PCG942e46. Result G1d7331e is bytes `season_no` followed by NUL. r1 remains intact across zero-fill stores through JSON operator[] G942e56. No missing-key guess needed.
- **ParseUser G9430f8 first field `pvid`.** LDRr1 G943106 reads slotG9433ec word0x1425594; ADD r1,pc G943112 uses PCG943116, resulting G1d686aa `pvid`. The earlier ADD G94310c operates r0, which is the stack-guard/global pointer, not r1. Using it as the r1 string ADD falsely produced a neighboring tail. r1 survives initial zero-fill through JSON operator[] G943156; inputJSON r2 moves to r0 at G943154.
- **ParseDefender G943958 first container `chain_bonus`.** LDRr1 G943966 reads slotG943c80; correct ADD r1,pc G943974 uses PCG943978, resulting G1d73439 `chain_bonus`. ADD G94396c operates r0/global stack guard; pairing it with r1 incorrectly produced `h_price` tail. JSON operator[] is G9439ee, result retainedr6. Null/empty container skips the loop.

Defender row keys are initialized once then reused by the ordinal loop:

```
LDR G943a2e slotG943c84; ADD G943a3a PCG943a3e -> ref_id -> sp+24
LDR G943a3e slotG943c88; ADD G943a40 PCG943a44 -> map-constructor metadata -> sp+1c
LDR G943a44 slotG943c8c; ADD G943a46 PCG943a4a -> atk -> sp+18
LDR G943a4a slotG943c90; ADD G943a4c PCG943a50 -> def -> sp+14
LDR G943a50 slotG943c94; ADD G943a52 PCG943a56 -> hp -> sp+10
```

The slotG943c88 pointer is passed as map emplacement constructor metadata at G943aac/G943ab4; it is **not an extra JSON key** and must not be forced through string decoding. Row obtained from container via numeric index G943a86 is retainedr4. JSON[] calls: ref_id G943a8e, atk G943ac0, def G943b12, hp G943b64. Each numeric bonus is multiplied by10000 in native storage (atk+0x14, def+0x18, hp+0x1c); this describes native representation, not original balance or a license to publish percentages of a guessed scale.

Verified minimum recovered fragment is therefore `chain_bonus:[{ref_id:string,atk:number,def:number,hp:number}]`. It is a defender parser fragment, not proof that the whole arena response is complete. Original season/rival/deck/reward contracts remain separately recovered or unknown.
