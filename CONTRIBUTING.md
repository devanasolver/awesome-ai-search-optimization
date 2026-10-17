# Contributing

Thanks for helping. This list stays useful only if every entry is real and honestly described.

## What gets in

A repo can be added if all of these are true:

1. It is **public** and **not archived**.
2. It has **a license**, or says clearly how it can be used.
3. It has had **a commit in the last 12 months**.
4. It works for this list's niche (AI SEO, AEO, GEO, AI-search visibility, llms.txt and close neighbours).
5. It does something you can show in the README. No empty shells, no "coming soon".
6. It is **not a copy** of another repo on the list.

Owners may add their own repo. It is judged by the same rules. Mark it with "(by the maintainer)" or "(by the author)" in the description if you are the owner.

## How to add a repo

1. Fork this repo.
2. Add **one** object to `data/entries.json`:
   ```json
   {
     "repo": "owner/name",
     "category": "audit",
     "description": "One plain sentence. What it does. Say if it needs paid keys.",
     "license": "MIT",
     "verified": "YYYY-MM-DD",
     "last_commit": "YYYY-MM-DD"
   }
   ```
   Categories: `audit`, `track`, `llms`, `cms`, `skills`, `platform`, `research`, `lists`.
3. Run `python scripts/build_readme.py` to rebuild `README.md`. Do not edit `README.md` by hand.
4. Open a pull request using the template. One repo per PR.

## Writing the description

- Plain words. Short. One sentence, two at most.
- Say what it does, not how great it is. No "best", "powerful", "revolutionary".
- If it needs paid API keys or a paid service, say so.
- If the repo's claims are unproven, do not repeat them as facts.
- No affiliate or tracking links. Link to the GitHub repo only.

## Removing or fixing entries

A weekly check (GitHub Action) opens an issue when a listed repo is archived, renamed, missing or has no commits for a year. Maintainers remove or fix those. You can also open a PR to remove a dead repo.

## Changelog

Add a line to `CHANGELOG.md` under "Unreleased" for each change.
