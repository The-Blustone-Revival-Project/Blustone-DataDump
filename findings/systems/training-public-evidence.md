# Public training evidence — 2026-10-03

Independent public-web research. No source/runtime changes. Two original-game screenshots downloaded from a dated community guide and visually inspected individually. Findings below are historical observations, not verified final 2.8.0.1 values.

## Newly recovered visual anchors

Source article: [Caragublu, Blustone Game Guide Tips & Trik](https://www.caragublu.com/2018/12/blustone-game-guide.html). Its live HTML `itemprop=datePublished` is **2018-12-05T02:23:00+07:00**. The game build itself is not shown.

### Hunter cap and advancement reset

Saved as `analysis/research/public-training/caragublu-train.jpg`.

Direct [full-resolution screenshot](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh_vhbz4K9jSSEzSfkqcsLAnXuOPQVjhPn6MoKzhzqh3NL_EWTAvoW3oesKGDa3KGezaWX3aasq21bbsXVHNkKkNmK_6KFdgFuYYkl6SLO7kKXlXKgawUDroiR0x7xTIPzoa38X4nB4_FIC/s0/Blustone+Train+Hunter.jpg).

The side-by-side screenshots show **Natalia**, title **Noble Spear**, three-star badge, Experienced Hunter:

- Left: **Lv.1**, strength **2480**, **Train** button.
- Right: **Lv.30**, badge marked **Lv.MAX**, strength **3323**, **Advance** button.

[COMMUNITY-SOURCED / VISUALLY VERIFIED] Ordinary **rank3 has maximum level30** in this historical screenshot. This directly disproves the replica's rank1/two-level table as a representation of the original game's *entire* ordinary progression; it does not establish the missing rank1/rank2/rank4/rank5 caps by itself. The article's prose describes hunter maximum30 generally, but the pictured rank-specific proof is rank3 only. Do not treat strength as HP, experience, or a stat growth coefficient.

### Advancement cost, source count and new level

Saved as `analysis/research/public-training/caragublu-advance.jpg`.

Direct [full-resolution screenshot](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEglwZOXjLhvf-ioglxDJPzvQaTAG79TSBs99lDmeBJVubDS-zAqwrg3LFtwhPPp8NutQA3GpVsKJ3O8u_B30HOSuEOi0MEkccn90tUDAHvsnBmpV4erYUUplRz98NEFQG6x1uu6MyY8tAO7/s0/Blustone+Hunter+Adcance.jpg).

Both panels show **Advancement Match**, a **three-star Lv.MAX target**, with wallet **43009**. Left has two selected sources, one empty source slot, **a faded four-star destination preview**, and displayed button price **8000**. Right has three selected sources, **a lit four-star Lv.1 destination preview**, and price **12000**. Sources visible in the selected row are at **Lv.1**. On-screen warning states that selected hunters are spent and leave the dormitory. **Retraction2026-10-04:** my intermediate correction wrongly called the fadedleftbadge three-star; both badges havefourstarshapes. Neither previewcaptures anacceptedpartialpromotion response. See `rank-up-partial-arithmetic.md`.

[VISUALLY VERIFIED] Historical **rank3→rank4 advancement** uses **three source slots**, displays **12000** when all three are selected, and previews a **level1** destination. Two-selected **8000** is a partial preview, not proof that advancing with only two sources succeeds. **4000 per added source** is the arithmetic difference in these two views; generalizing it to all ranks or to Raise would be unsupported.

**This is ADVANCEMENT, not ordinary Raise.** It cannot replace `trainingPrices.level` or ordinary source experience. Rank-up has a separate native price vector.

## Additional public evidence, with limited scope

- [MrGuider training guide](https://www.mrguider.org/guides/blustone-game-guide-tips-cheats-strategy/) describes normal training consuming another hunter and advancement occurring at maximum level. No cumulative XP/source-XP table or numeric Raise cost found there.
- [TapTap Chinese community guide](https://www.taptap.io/post/73623) lists advancement **to2★:1000; to3★:3000; to4★:12000; to5★:60000**. This is a reposted community guide, not an official balance table, and no exact publication/build date was verified in this pass. Its 12000 rank3→4 price agrees with the screenshot. No Raise cost or XP thresholds appear in the retrieved text. Keep this separate from any per-source rank-price indexing.
- [Reddit, Training hunters](https://www.reddit.com/r/Blustone/comments/8h6fmv/training_hunters/) supports using raised low-star hunters as advancement fodder; no XP numbers.
- [Reddit, advancing characters](https://www.reddit.com/r/Blustone/comments/qqcl7k/question_about_advancing_characters/) supports consumed source hunters and using3★ training dummies or promoted1★/2★ as materials. The page's Top Posts footer dates it **November9,2021**; no game version is identified. This is firsthand community testimony, not native wire evidence.
- [Reddit, EXP farming](https://www.reddit.com/r/Blustone/comments/8fkdcd/which_stage_is_the_best_to_farm_exp/) has a **April28,2018** Top Posts footer. One player reports 1★ capped after19 dispatches at stage40, 2★ after30 dispatches at61–64; another reports 1★ capped after9 dispatches at121–130. They do not specify initial XP, clear reward, role bonuses, or a cumulative threshold. These are farming-count observations, **not a solvable XP curve**.
- [Reddit, Farming Stages](https://www.reddit.com/r/Blustone/comments/9ztinx/farming_stages/) is dated **November24,2018** by its footer; comments explicitly say an update substantially changed stages and EXP. This limits reuse of April2018 dispatch counts for later builds.

## Local community-guide recheck

Read the human-readable first606 lines of `recovered-assets/community-notes-2026-09-30/Blustone Guide FAQ.md` (avoided printing its multi-MB base64 definitions). Its table of contents advertises **DISPATCHES AND TRAINING NEEDED TO MAX**, but that anchor has no corresponding body section in this Markdown copy. The preserved FAQ therefore does not supply the missing training table in its prose. The equipment level10/20/30/40/50 references refer to **gear**, not hunter maximum levels or XP.

## Unresolved original data

No supported complete original **`min_exp` cumulative level curve**, **`upgrade_exp` source-rank/source-level table**, **ordinary Raise rupee-price table**, or **per-star maximum-level table covering all ordinary ranks** was obtained. No claim is made that these cannot exist elsewhere.

The original community forum links [share_en/1260](http://bs.visualshower.com/share_en/1260) and [share_en/192223](http://bs.visualshower.com/share_en/192223), cited by [this Reddit guide](https://www.reddit.com/r/Blustone/comments/9bo5bd/guide_for_noobs_and_seminoobs_check_this_out/), timed out. Attempts to open2021 Wayback versions via the browser tool failed; this does not prove no archived copies exist. Miraheze Hunters page and Namu hunter page were also inaccessible through the tool. Indexed Namu text provided mechanics but not the needed curve.

General web queries are noisy: Blustone sales training companies, similarly named RPGs, and unrelated Korean content swamp results. No unrelated game's XP formula was reused. No new video was downloaded in this pass; prior four-video stat scans do not establish absence of training evidence in other videos.

## Practical implication

There is a solid historical **rank3 level30 cap / advancement-to-level1** anchor and a visually supported **rank3→4 total advancement price12000**. The server may deliberately implement a broader playable replica curve, but its intermediate XP thresholds, source-XP yields, and ordinary Raise prices must stay **[FIXTURE]** until independently recovered. Do not multiply a level1 stat or interpolate XP from the two Strength values and call it original balance.
