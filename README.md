# CryptoNova Mainnet (.ai family)

This single repo hosts 3 independent pages, each deployed as its own Vercel
project using a "Root Directory" setting so they don't share routing config
or branch bindings:

| Folder    | Vercel Root Directory | Domain                | Content |
|-----------|------------------------|------------------------|---------|
| `mainnet/`| `mainnet`              | cryptonova.ai, www.cryptonova.ai | Mainnet launch / coming-soon page |
| `ea/`     | `ea`                   | ea.cryptonova.ai       | Early-access testnet-under-mainnet-brand page |
| `admin/`  | `admin`                | admin.cryptonova.ai    | Internal admin preview page |

Each folder is fully self-contained (its own `index.html`, `terms.html`,
`faq.html`, `vercel.json`, `api/log-error.js`) — no cross-folder dependencies,
no host-based rewrites. Editing one page can never break another.

To deploy: create 3 Vercel projects pointed at this one GitHub repo, setting
each project's "Root Directory" (Settings → General → Root Directory) to
`mainnet`, `ea`, or `admin` respectively, then bind the matching domain.
