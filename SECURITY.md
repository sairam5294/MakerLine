# Security policy

Product Kit ships safety hooks, permission rules, CI checks and starter apps that other people run on their machines and deploy. A weakness in any of those matters.

## Supported versions
Only the latest minor version receives fixes. Upgrade projects with `scripts/upgrade-project.sh`.

## Reporting a vulnerability
Please do **not** open a public issue. Use GitHub's private vulnerability reporting ("Report a vulnerability" under the Security tab) and include:
- which file or starter is affected
- steps to reproduce or a proof of concept
- the impact you believe it has

You will get an acknowledgement within 7 days and a fix or mitigation plan within 30 days for confirmed issues.

## Scope
In scope: hook and permission bypasses (for example a command the dangerous-command guard should block but allows), secret leakage paths, CI workflow weaknesses, starter-app vulnerabilities (auth, RLS, CSP, rate limiting), and supply-chain issues (unpinned or compromised dependencies and actions).

Out of scope: vulnerabilities in third-party services the starters integrate with (report those to the vendor), and issues that require a user to disable the kit's own checks.
