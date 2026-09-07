# CryptoNova — MAINNET READINESS (Base mainnet, chainId 8453)

Written 2026-09-07 (session 66) for a future session of Claude and the owner. Entry point for all
mainnet work — LIVES IN `C:\CryptoNova-Mainnet-App` (see §0). `MAINNET_TODO.md` (2026-07-23, V4 era) and `DEPLOY_RUNBOOK.md` "Mainnet Differences"
(2026-06-17) are superseded by this file; keep them as history only.

OWNER'S DECISION (2026-09-07, session 66, final — "Ok A, B"): **ONE mainnet deploy, the WHOLE
project, all ten tiers. No soft launch, no caps, no second deploy or migration.** Earn income first,
then an independent audit when affordable, "on the confidence of what we built"; if that audit finds
shortcomings, live with them or rebuild THEN. Reasons given: a soft launch would cost another
launch + migration; audit firms charge "an arm and a leg"; small firms are not trusted with
pre-launch code. Plus option B: a small bug bounty and a plain "not yet independently audited"
line on the site from day one.
Claude's position on record: launching first then auditing removes the pre-launch code-exposure
worry (the source is public on BaseScan after launch anyway); the risk of an unaudited ~4k-nSLOC
custody core is real and UNMEASURED and was stated to the owner plainly; the no-cost conditions
in §1/§2 are what stand between a green testnet and real money. Target: go/no-go review
**~2026-09-21**, gated on §1.

The two rules apply here more than anywhere: nothing in this file is "ready" until it has been
RUN on the target it names. A box that has not been run is not ticked.

---

## 0. WHERE MAINNET THINGS LIVE (owner rule 2026-09-07: "we need to do everything for mainnet there")

**This repo — `C:\CryptoNova-Mainnet-App` (github CryptoTechSXM/cryptonova-mainnet-app, branch `main`) — is
the HOME for all mainnet work: this file, the deploy runbook (§4, to be written here), the `.env`
templates, the wallet setup, and the mainnet frontend.** Moved here from the contracts repo at
this commit; the contracts-repo copy is a pointer only.
What stays in the contracts repo (`C:\CryptoNite-Smart-Contracts\CryptoNova`, branch `v8.1`) and
why: the Solidity, Hardhat config, `deploy_v8.js`, `seed_w1.js`, `postdeploy_check.js`,
`chain_guard.js`, tests. There is ONE source of code for both networks — the mainnet deploy is
the same script run with a mainnet `.env` built from `env.mainnet.deploy.template` here.
Keepers stay in `C:\CryptoNova-Keepers` (one source, T9 makes them chain-parametrised).
Inventory of this repo as found 2026-09-07 (all July, V8.38 era): `mainnet/` (cryptonova.ai
coming-soon + countdown), `ea/` (early-access page + coupon API), `admin/`, each its own Vercel
root (README.md); `env.mainnet.deploy.template`, `env.mainnet.keeper.template`,
`mainnet_wallet_setup.md` (8 wallets, deployer warning about the EIP-7702-delegated 0xCd0Af6),
`set_mainnet_gate.py`, `fix_countdown_label.py`. Last commit 52d9316 (soft-launch countdown
removed, "flagship June 19 2027" — superseded by the 2026-09-07 decision above).
⛔ MEASURED 2026-09-07: `mainnet/index.html` is labelled **V8.15**, 4,216 lines; the live testnet
app `C:\CryptoNova-Testnet-App\index.html` is **V8.52**, 11,674 lines; only 1,857 of the app's
9,134 unique lines appear in the mainnet file. The mainnet frontend is NOT a base to patch — T7
becomes: copy the current Testnet-App pages into `mainnet/` at cutover, then repoint (chainId
8453, real USDC, no faucet, mainnet `ADDRS`). Both templates still name the RPC var
`BASE_SEPOLIA_RPC_URL`; the keeper template carries `SF_TOPUP_AMOUNT_USD` / `SF_AUTOFUND` from
before the no-manual-top-up policy — both templates are re-cut when the runbook is written.

## 1. HARD GATES — none of the rest matters until these are green

- [ ] **G1 Blockaid fully clear.** Peter cleared crypto-nova.app + the V8.52 TierRouter (09-05
      07:57Z) but the registration approval spender — T1 PairManager `0xc2fCD…d42c7` — still shows
      "Malicious" in MetaMask (3 samples 09-05/06/07). A real-money launch behind a red wallet
      warning is dead on arrival. Owner's follow-up (09-05 22:49 local) unanswered; nudge from
      09-08 morning local. Proof = the 62.30 wallet test with NO red tag on every spender the site
      asks for (10 PMs, 20 matrices, router, CouponRegistry, treasury). See memory
      `cryptonova-blockaid`.
- [ ] **G2 The organic measurement (09-03) closed.** Does the loop fund itself at the referral
      rate REAL members produce, organic wallets only, on V8.52 (live since 09-04)? Needs the
      window stated (start block, end block, wallets counted) and the number, not a feel.
      Instrument: `diag_rescue_seat_outcome.js` / SF debt book (memory `cryptonova-rescue-exposure`).
- [x] **G3 Audit decision — DECIDED 2026-09-07: post-launch, funded from income.** Scope when the
      time comes: the ~4k-nSLOC custody core (MatrixLogicLib, FigureEightMatrixV8, PairManagerV8,
      TierRouter, StabilityFund, MatrixKeeper); unique deployed money-moving source ~7,000 nSLOC;
      whole `contracts/` ~10,356 incl. legacy/mocks. Published ranges (not quotes): boutique/solo
      ~$8k–25k for a 2-week core review; mid-tier $15k–70k; contests from ~$37.5k; top firms
      $60k–150k+. `AUDIT_SCOPE.md` is NOT owed before launch; write it when income is there.
- [ ] **G4 Disclosure line live before the first real registration** (option B): a plain sentence
      on the site — the contracts are verified on BaseScan but not yet independently audited; an
      audit is planned from project income. Owner's voice, no legalese, on index.html + faq.html.
- [ ] **G5 Bug bounty published before launch** (option B): amount tiers set by the owner (policy),
      what counts (a reproducible bug in the live mainnet contracts or a way to take funds), how to
      report (cryptocounsels@gmail.com), paid on a confirmed fix. Text on the site + faq.html.

## 2. POSTURE DECISIONS THE OWNER OWNS (Claude gives options + a recommendation, owner picks)

- [x] **P1 Launch caps — DECIDED 2026-09-07: NONE.** All ten tiers open from day one with the
      deploy-time fees T1 $10 … T9 $5,000, T10 $10,000 (`deploy_v8.js:143-152`) and the existing
      gates only (`tierGateThreshold[5..10]`, whale gate). MEASURED for the record: there is no
      on-chain max-open-tier or deposit cap, so the "T1-only" and "deploy only T1–T3 PMs" options
      were code changes, not switches — both dropped, no fork test owed.
- [x] **P2 Pause plan — DECIDED 2026-09-07 (owner: "I will go with you on that as well, automate it").**
      MEASURED first (TierRouter.sol): `systemPaused` (:354) blocks register ×4 + manualUpgrade /
      hybridUpgrade / bulkUpgrade via `whenNotPaused`; withdrawals (`bulkWithdraw` :1063/:1086,
      matrix `withdraw*`) are NOT gated — members can always exit (code read; hardhat test still
      owed before members are told). The only automatic pause today is `checkInactivity()` (:684):
      no registration for N days / N cycles → self-pause. `pauseSystem` is `onlyOwner` (:720), so
      an automatic watchdog would need the owner key on the VPS — rejected (P3).
      DECISION: (1) **new limited `pauser` role in TierRouter before mainnet** — one address that
      may call pause ONLY (never unpause, never any setter); a VPS watchdog keeper holding that key
      pauses automatically when StabilityFund `totalBalance < stabilityFloor`; worst case if that
      key leaks = the front door closes until the owner unpauses. Build = ~10 lines + a test;
      ✅ BUILT + PROVEN 2026-09-07 (contracts `f8cd4b3`, V8.53): `pauser` + `setPauser` +
      owner-or-pauser `pauseSystem`; 6/6 new tests + Elevator suite green (146 passing).
      MEASURED: 24,345 → 24,509 bytes, 67 under EIP-170 — TierRouter is at its ceiling (R15).
      STILL OWED: `postdeploy_check.js` pauser row; the VPS watchdog keeper (T9 env first);
      withdrawals-while-paused test. (2) Human triggers, owner's refinements:
      Blockaid re-flag → pause, investigate, UNPAUSE while dealing with Blockaid if the code is
      clean; silent keeper → ALERT first (Telegram silent-job alert exists), pause only if still
      silent after a look — usually a VPS outage; credible exploit report → pause, always.
      (3) Ready-to-paste pause + unpause commands on the PC, rehearsed on Sepolia; member notice
      template in the owner's voice ("new registrations paused while we check; withdrawals work
      as normal"); unpause only after the cause is written down. Lives in the incident page (P4).
- [x] **P3 Key custody — DECIDED 2026-09-07 (owner: "B now and A later").**
      Today: ONE hot key = deployer = owner = keeper, in `.env` on the PC AND in `/root/keeper` on
      the VPS — one file, whole system. DECISION: **(B) hardware wallet as `owner`** of every
      contract before mainnet (Ledger/Trezor, ~$80–150; the owner key never exists as a file);
      keepers get their OWN hot key that can only do keeper jobs (`upkeepCaller` grant), and the
      P2 pauser gets its own pause-only key; deployer may stay a hot key used once at deploy and
      then demoted by `transferOwnership` to the hardware address. **(A) later:** once owner
      actions have been seen to be rare in live operation, hand ownership to a 2-of-3 Safe
      (owner + two CryptoCounsel members). NON-NEGOTIABLE either way: keeper key ≠ pauser key ≠
      owner key on mainnet. Build items this creates (Claude): a `transfer_ownership.js` that
      walks every Ownable contract in the book (46 rows — measure which are Ownable first) and
      hands them to the hardware address, with a read-back check; a Sepolia rehearsal of pause +
      unpause + one setter signed from the hardware wallet; `mainnet_wallet_setup.md` re-cut with
      the three-key layout. Rows go into `MAINNET_DEPLOY_RUNBOOK.md` (§4).
      Owner's follow-up questions 2026-09-07, answered from the code: (a) Safe signers + threshold
      are changeable later by multisig approval — the contracts only ever see the Safe's address.
      (b) MEASURED which recipients can move after deploy — CORRECTED after the owner asked
      "I thought Community, Stability and Buyback were contract based?" (they are: the V8.52 book
      rows are the CommunityWallet / StabilityFund / CNOVABuybackReserve CONTRACTS; only
      liquidityReserve and accountOne are wallets). Each matrix holds a re-pointable address for
      all five (`FigureEightMatrixV8.sol:266-310`, read by the split code `self.liquidityReserve`
      :1189 / `self.buybackReserve` :1243 / `self.stabilityFund` :628) — so: liquidityReserve + W1
      can be moved to a hardware WALLET later (one owner tx per matrix; payout-to-new-address
      still to be proven by test); SF / BBR / CommunityWallet are stateful CONTRACTS — re-pointing
      is a migration (ledger + balances do not follow), their setters are deploy wiring / repair,
      and they are secured by OWNING them with the hardware wallet (P3), not by moving them.
      NO setter for **devWallet, opsWallet, treasury** inside the 20 live matrices — fixed by
      `DeployParams` at birth, paid by `MatrixLogicLib.sol:1190-1205` for the life of the deploy
      (`MatrixPairFactory.setWallets` :177 only affects matrices created afterwards). Owner intends
      these to be hardware wallets. DECISION (Claude's recommendation, owner to confirm at the
      wallet-setup step): no new setters; Dev / Ops / Treasury-recipient addresses are hardware
      addresses that EXIST BEFORE deploy day and go into `env.mainnet.deploy.template`.
- [ ] **P4 Incident playbook** — one page: detect (Telegram alerts already live: balance,
      frozen-pair, silent-job, RPC, site/faucet probes), decide (who), act (pause tx block ready
      to paste), tell (member post template in the owner's voice), review. Lives in
      `GO_LIVE_RUNBOOK.md` as a new PHASE.
- [ ] **P5 Entity / disclosure.** No company, no licence, four-person unincorporated co-op —
      stated to Blockaid already. Decide what the public site says about this before real money
      (privacy.html exists; a plain "who we are / what we are not" line is owed).

## 3. MEASURED GAPS IN THE TOOLING (Claude fixes; each needs a run to tick)

- [x] **T1 `deploy_v8.js` W1 seed — FIXED + PROVEN 2026-09-07 (both paths).**
      Was: `usdc.mint(W1_ADDR, T1_FEE)` unconditional inside the W1 try/catch → on real Base USDC
      (`0x833589fCD6eDb6E08f4c7C32D4f71b54bdA02913`, no public mint) revert → swallowed → W1 NOT
      registered, `setDefaultReferrer` skipped. Now: external USDC → require W1 balance ≥ T1_FEE,
      fail loud; non-testnet W1 failure rethrows; `seed_w1.js` same guard. PROVEN on `--network
      hardhat` 18:42Z (MockUSDC path, W1 registered). Balance guard PROVEN via `seed_w1.js` on a
      `hardhat node` chain with a $0 wallet → `Error: W1 holds $0 USDC on external USDC …; needs
      $10` (the deploy_v8 branch is the same guard, exercised only through seed_w1). ⚠ A full
      deploy over `--network localhost` took the owner 1h13m; use `--network hardhat` (~1 min)
      unless the chain must survive the run.
- [x] **T1b `USDC_ADDRESS` code check — ADDED + PROVEN 2026-09-07.** Step 1 reads `getCode`; no
      code on a real network = hard stop naming the chainId (wrong chain / typo can no longer wire
      46 contracts to nothing); on hardhat/localhost = notice + MockUSDC deploy. Also fixed on the
      way: `EXPECTED_DEPLOYER` guard skipped on local networks; MockUSDC constructor arg (`admin`)
      restored in the deploy branch, which had not run since the shared Sepolia token took over.
- [x] **T2 Network guard — contracts side DONE 2026-09-07 (live run PASSED: `postdeploy_check.js` on V8.52,
      block 46525181, no `chain_guard:` line — book chainId 84532 matched the RPC); keeper side folded into T9.** Census: contracts repo `scripts/` 223 of 353 scripts read an addresses
      book, ONE real guard (`deploy_v8.js` T1b getCode), `keeper_w1.js` only detects testnet vs
      mainnet; the book itself carried only `"network": "baseSepolia"`, no chainId; no shared
      loader (each script opens the file itself, 15 different spellings) — so a per-script fix is
      ~130 edits and NOT owed for read-only diags. Keepers repo: 82 of 105 read a book, ZERO check
      the chain; 64 hard-code `new JsonRpcProvider(RPC_URL, 84532, {staticNetwork:true})`,
      `rpcProvider.js` falls back to Sepolia-only public RPCs, and ALL 12 scripts on the live
      crontab (`crontab_live_mirror.txt`: rr_keeper ×3, system_keeper, sf_invariant_check,
      onramp_keeper, monitor_v8, integrity_check, growth_snapshot, fastlane_rescue, dupe_watch,
      direct_keeper, copay_rescue, channel_pulse) are Sepolia-bound by literal or URL. So the
      keeper fleet cannot run on mainnet at all as written — that is T9's job, not a guard.
      BUILT: `deploy_v8.js` now writes `chainId` into every book (`:1029`); new
      `scripts/chain_guard.js` `assertChain(book, provider, label)` — match → continue, mismatch
      → throw naming both chainIds, book without chainId → throw unless `ALLOW_LEGACY_BOOK=1`
      (warns); PROVEN 4/4 branches on a fake provider (no RPC). Wired into `postdeploy_check.js`
      (`:46`, `:73`) so the post-deploy step refuses a wrong-chain book. `deployed_addresses_
      v8_52.json` given `"chainId": 84532` (repo copy only; the box copy is unchanged and the
      keepers do not read the field). ⚠ UNRUN: `postdeploy_check.js` live against V8.52 with the
      new guard (owner, PowerShell — this proves the match branch on a real RPC and closes T5's
      "on a run against V8.52"). Still to wire before mainnet: `verify_all.js` (T4) and the
      frontend repoint tool (`update_addrs` in the app repo) — both are new/edited anyway.
- [ ] **T3 Grace period default** — already fails safe: unknown network → 48h mainnet policy
      (`deploy_v8.js:947-951`). Tick after one dry run prints `172800` for `baseMainnet`.
- [x] **T4 Verify-before-repoint as a script gate — DONE 2026-09-07 (live: V8.52 book, 46 VERIFIED, 1 wallet,
      0 unverified, 0 unknown, `verify_gate exit 0 (OPEN)`; pushed `30532f2`).**
      `scripts/verify_gate.js` (contracts repo; was `check_verification_v850.js`, session 45):
      read-only, chain + explorer taken from the book's `chainId`, one `getsourcecode` per address
      with `eth_getCode` to tell wallets from unverified contracts, EXIT 0 only when every contract
      row is VERIFIED, 1 on any UNVERIFIED or UNKNOWN (a read failure is not a pass), 2 on setup.
      Verdict function proven 4/4 offline. `scripts/verify_all.js` (was `_v850`) is the SUBMITTER,
      book required, chain-guarded against `--network`. `postdeploy_check.js` step 4 runs the gate
      and fails its verdict on non-zero, so "Safe to cut over" cannot print on an unverified set.
      Tick after: `$env:ADDRESSES_FILE="deployed_addresses_v8_52.json"; node scripts/verify_gate.js`
      on the PC → expect 46 VERIFIED, wallets listed, `verify_gate exit 0 (OPEN)`.
- [x] **T5 `postdeploy_check.js` reads `upkeepCaller`** — DONE 2026-09-07: live run on V8.52 block
      46525181 printed `PASS upkeepCaller[keeper EOA] granted` (plus stabilityFloor, graduationEnabled).
- [ ] **T6 Faucet must not exist on mainnet.** `api/faucet.js` holds a funded key on the testnet
      app; the mainnet Vercel project must have NO faucet env/key and the site's faucet UI must be
      hidden by chain. `site_probe.js` expects `/api/faucet` → 400; on mainnet expect 404.
- [ ] **T7 Wallet RPC + chain params** (`WALLET_RPC_URLS`, chainId 8453, explorer basescan.org)
      in the frontend `ADDRS`/network block; the "Rabby on Base Sepolia" FAQ paragraph is
      testnet-only copy.
- [ ] **T8 Vercel: the `mainnet` branch trap (57.0).** `cryptonova-mainnet.vercel.app` PRODUCTION
      tracks branch `mainnet` = the 23-file June-19 marketing tree. Anything from `v8.1` merged
      into `mainnet` publishes the handoff to the world. The mainnet app needs its OWN project +
      domain plan written BEFORE any push; do not reuse that project casually.
- [ ] **T9 Keepers (absorbs T2's keeper half).** MEASURED: 64/105 scripts hard-code chainId 84532 with `staticNetwork:true`, `rpcProvider.js` fallbacks are Sepolia-only, all 12 live-crontab scripts are Sepolia-bound. Fix shape when the time comes: one `keeper_env.js` (RPC + chainId + book from `.env`, `assertChain` on start) required by the 12 live scripts; the other ~50 stay Sepolia-only and are never installed on the mainnet box. The box's crontab/`.env` point at `deployed_addresses_v8_52.json` on
      Sepolia. Mainnet keepers = a separate box or a separate user + `.env` + addresses file, with
      their own key (P3), their own Telegram source tags, and job A (stress fill) NEVER installed.
- [ ] **T10 Gas ceiling.** The measured Sepolia per-tx cap is 2^24 (memory
      `cryptonova-gas-ceiling`); Base mainnet's block gas limit differs. Measure `forceCross` /
      full-matrix registration gas on a mainnet fork before launch.

## 4. THE MAINNET DEPLOY RUNBOOK (to be written — separate file, after §3 T1/T2/T4 land)

`MAINNET_DEPLOY_RUNBOOK.md`: `.env` diff from testnet (USDC_ADDRESS, BASE_RPC_URL, no
CNOVA_ADDRESS, fresh deployer funded with real ETH — amount measured from the V8.52 deploy gas
total × mainnet gas price), the `--network baseMainnet` command, verify-all gate, W1 seed with
pre-funded USDC, `set_upkeep_caller`, postdeploy_check, frontend repoint on a NEW Vercel
project, Blockaid pre-notification (send the 46-row table BEFORE any member is pointed at it),
keeper start order, and the owner human test with a $10 real registration + withdrawal.

## 5. NEXT ACTIONS, IN ORDER

1. Blockaid nudge from 09-08 morning local (G1). Re-test after any reply.
2. ~~T1, T1b, T2-contracts, T4, T5 all proven live (09-07).~~
3. ~~P2 + P3 decided (automated pauser role; hardware-wallet owner now, Safe later).~~ ~~pauser role built.~~ Build: postdeploy_check pauser row → watchdog keeper (needs T9 env) → withdraw-while-paused test → ownership-transfer script (Ownable2Step; census first) → P4 incident page.
4. G4 disclosure line + G5 bounty text — drafted in the owner's voice, owner sets the amounts.
5. G2 measurement window: agree start block (V8.52 first organic registration) and run it.
6. `MAINNET_DEPLOY_RUNBOOK.md` (§4) once T1/T2/T4 are landed.
