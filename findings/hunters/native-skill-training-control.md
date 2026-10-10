# Native skill training control — Tyltyl5, singleton batch

2026-10-04, instrumented +7 PID27038. Native observer confirmed ordinary Raise target5, followed by responsive Back to that hunter's details. Free Skill Training showed slot1 level1/10, Healing52.00→54.59, price200; slots2..5 were locked at0.

One normal upgrade produced **/gym/MultiSkillUp** at12:49:31.358Z, target_inst_id5, body key `mulit_skill_up_count`, HTTP200/plaintext308. It did not use the single SkillUp route. The raw vector was not logged; singleton `[1,0,0,0,0]` is inferred from the sole selected slot, UI delta, price and validated server behavior, not claimed as captured transport text.

Persisted gold11130→10930; hunter5 skill1 level1→2 and EXP130 unchanged. Hunters1/2/4/5 remain owned with previous EXP130/30/30/130; other skill slots unchanged, AP50/BP10 and teamEXP270 unchanged. No card/source/lock/rank/gacha operation occurred.

Screenshots67–69 verified by eye: updated skill2/10, next price300, detail strength57→67, HP1020/ATK102/DEF52 unchanged. Back remained responsive. No distinct movie was observed in the two-second sample; UI/icon update is confirmed without an animation claim.

This validates native singleton batch pricing/mutation/UI integration under local price/skill fixtures. Original balances/effects/prices, arbitrary multi-slot/count batches, single-route SkillUp, battle healing and restart display remain separate validation gaps. Pending Gym tutorial8/1 was not cleared by this ordinary transaction.
