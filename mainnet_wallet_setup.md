# Mainnet Wallet Setup — CryptoNova V8.38
Last updated: 2026-07-18

Before running the mainnet deploy, every wallet below must exist and be funded.
Go through this list top to bottom. Each row tells you: what the wallet IS, whether
it already exists, and what it needs before launch.

---

## Wallet Inventory

### 1. Deployer — `DEPLOYER_PRIVATE_KEY`
| | |
|---|---|
| Address | 0x5EaEfA3... (clean EOA) |
| Status | ✅ Exists |
| Key lives in | CryptoNite-Smart-Contracts/CryptoNova/.env |
| Needs | Base ETH for deploy gas (~$20–50 worth at current gas) |
| Action | **Verify ETH balance on Base mainnet before deploying** |
| ⚠️ WARNING | NEVER use 0xCd0Af6 — it is EIP-7702 delegated and will fail on mainnet |

---

### 2. AccountOne (W1) — `W1_PRIVATE_KEY`
| | |
|---|---|
| Address | 0x6512e9B5FE1690F2570AFEE5E7b904EF106C9435 |
| Status | ✅ Exists |
| Key lives in | CryptoNite-Smart-Contracts/CryptoNova/.env |
| Needs | Real USDC on Base mainnet ($10 minimum — covers T1 entry via seed_w1.js) |
| Action | **Send at least $15 USDC to this address on Base mainnet** |
| Purpose | First registered member; all referrer links trace back here |

---

### 3. Dev Wallet — `DEV_WALLET_ADDRESS`
| | |
|---|---|
| Address | 0x7fc2158892F14b9A1fB6e39B788d4d08daF49C0a |
| Status | ✅ Exists (address only — no key needed in deploy) |
| Needs | Nothing upfront — it receives earnings passively |
| Action | None |

---

### 4. Ops Wallet — `OPS_WALLET_ADDRESS`
| | |
|---|---|
| Address | 0xa23A0492A823a2FfB6D3998dDd487695F5ba4019 |
| Status | ✅ Exists (address only — no key needed in deploy) |
| Needs | Nothing upfront — it receives earnings passively |
| Action | None |

---

### 5. Admin Wallet — `ADMIN_WALLET_ADDRESS`
| | |
|---|---|
| Purpose | Holds DEFAULT_ADMIN_ROLE on all contracts — can pause, upgrade, set params |
| Status | Not yet set — defaults to deployer if left blank |
| Recommendation | **For launch day: use the deployer address (0x5EaEfA3...)** |
| Post-launch plan | Migrate to a Gnosis Safe multi-sig for security |
| Action | **Set ADMIN_WALLET_ADDRESS to deployer address for now** |

---

### 6. Liquidity Reserve — `LIQUIDITY_RESERVE_ADDRESS`
| | |
|---|---|
| Purpose | Receives the LP allocation from DirectSale CNOVA purchases |
| Status | ❌ NOT SET — defaults to OPS_WALLET if blank |
| Recommendation | Create a dedicated address (or use Ops wallet for launch) |
| Action | **Decide: new dedicated address or OPS_WALLET_ADDRESS** |

---

### 7. Gas Gift Wallet — `GAS_GIFT_WALLET_ADDRESS`
| | |
|---|---|
| Purpose | Sends small ETH amounts (~0.002 ETH) to new members who have no gas |
| Status | ❌ NOT SET — must be created |
| Needs | Create new wallet + fund with 0.5 ETH on Base mainnet for launch |
| Also needed | Private key must go in Vercel env as `GAS_GIFT_PRIVATE_KEY` |
| Action | **Create new wallet. Fund with 0.5 ETH. Add to both .env files and Vercel** |

---

### 8. Keeper Wallet — `KEEPER_PRIVATE_KEY` (VPS)
| | |
|---|---|
| Purpose | Signs performUpkeep(), rescue TXs, and system_keeper admin calls on mainnet |
| Status | ❌ NOT CONFIRMED for mainnet — can reuse deployer key or use dedicated wallet |
| Needs | Base ETH for gas (suggest 0.1–0.2 ETH to start) |
| Recommendation | For launch: reuse deployer key. Post-launch: dedicated keeper wallet |
| Action | **Fund chosen wallet with ETH on Base mainnet. Add key to keeper-mainnet/.env** |

---

## Required Funding Summary (Before Deploy)

| Wallet | What to fund | Minimum |
|---|---|---|
| Deployer (0x5EaEfA3) | Base ETH for deploy gas | ~$50 worth |
| W1 (0x6512e9B5) | Real USDC on Base mainnet | $15 |
| Gas Gift wallet (new) | Base ETH | 0.5 ETH |
| Keeper wallet | Base ETH (if separate from deployer) | 0.1 ETH |
| Stability Fund (post-deploy) | Real USDC (via sf_topup script) | $500 minimum |

---

## Vercel Env Vars — Mainnet Project (cryptonova-mainnet-app)

These go in the Vercel dashboard for the mainnet Vercel project:

| Var | Value |
|---|---|
| `BASE_RPC_URL` | Base mainnet RPC (same Alchemy key, mainnet endpoint) |
| `ANTHROPIC_API_KEY` | Same Claude API key as testnet |
| `TELEGRAM_QA_BOT_TOKEN` | Bot token for the QA bot (same or dedicated) |
| `GITHUB_TOKEN` | Fine-grained PAT, Contents R+W on cryptonova-testnet-app repo |
| `BUG_REPORT_PASSWORD` | Same as testnet |
| `GAS_GIFT_PRIVATE_KEY` | Private key of gas-gift wallet (new — created above) |
| `FAUCET_PRIVATE_KEY` | Leave EMPTY on mainnet (testnet only) |

---

## What Needs to Be Done RIGHT NOW (before deploy)

1. **Create the gas-gift wallet** — new wallet, write down the address and private key
2. **Fund wallets on Base mainnet:**
   - Deployer: ETH for gas
   - W1: $15 USDC
   - Gas-gift wallet: 0.5 ETH
3. **Fill in `env.mainnet.deploy.template`** with the real values (all `<REQUIRED>` fields)
4. **Fill in `env.mainnet.keeper.template`** with the real values
5. **Set Vercel env vars** in the mainnet Vercel project (cryptonova-mainnet-app)
6. **Then copy `env.mainnet.deploy.template` to** `CryptoNite-Smart-Contracts/CryptoNova/.env`
   and run the deploy command
