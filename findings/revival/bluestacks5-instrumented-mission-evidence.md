# BlueStacks 5 instrumented mission evidence

Source: Docker instrumentation collector, session
`295ece32-47f1-4a39-936b-7b014602af0e`. The trace is from the side-by-side
`com.vshower.prd_sr.instrumented` package on BlueStacks 5; no QEMU data is used
for this report.

## Ordered missing UI records

The native lookup trace reached the following EN records in order:

1. `EN/SR_COMMON/0_UI_CM_FR`
2. `EN/SR_COMMON/BTN_W_FRM`
3. `EN/SR_GLOBAL/LOADING_BAR`
4. `EN/SR_FLOW/FL_PV_POP`
5. `EN/SR_MAIN/0_SR_MN_BG`
6. `EN/SR_MAIN/7_SR_MAIN`
7. `EN/SR_MAIN/NEW_V_MENU`
8. `EN/SR_MAIN/NEW_T_MENU`
9. `EN/SR_MAIN/6_SR_MN_CHA`
10. `EN/SR_COMMON/4_UI_CM_DIL/2_UI_CM_GS`
11. `EN/NEW/SR_DIALOG/0_UI_DIA3`
12. `EN/NEW/SR_MISSION/1_SR_UI_MS_AR/0_MS_AR_EX`
13. `EN/SR_COMMON/0_UI_CM_PV`
14. `EN/NEW/SR_MISSION/2_SR_UI_MS_ST/1_MS_ST_MAP`
15. `EN/NEW/SR_MISSION/2_SR_UI_MS_ST/5_MS_ST_GL`
16. `EN/NEW/SR_MISSION/2_SR_UI_MS_ST/6_UPDOWNBTN`
17. `EN/NEW/SR_MISSION/2_SR_UI_MS_ST/2_MS_ST_MK2`
18. `EN/NEW/SR_MISSION/2_SR_UI_MS_ST/4_MS_ST_FT`

The native failure immediately afterward was:

```text
ASSERTION Failed on GMLevelDB.cpp(63)
```

This is stronger than the earlier QEMU-only evidence because it includes the
additional pre-map records and comes from the instrumented app's durable log
stream. The collector also retained the app-private database artifacts and
CDN repair snapshots for separate comparison.

## Interpretation

The next patch target is the complete 18-key EN lookup set, not only the three
stage-map keys. The patch must preserve the BlueStacks client’s existing CDN
repair/bootstrap lifecycle; direct wholesale LevelDB replacement is not yet
safe. The active BlueStacks serial is `127.0.0.1:5555` and the collector is
`http://127.0.0.1:8099`.
