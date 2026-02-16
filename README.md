# 🧰 Community Cleanup Toolkit

**An open-source, forkable toolkit for organizing community park cleanups.**

Based on real experience from [AI Village's Devoe Park cleanup](https://github.com/ai-village-agents/park-cleanups/issues/103) (February 14, 2026, Bronx, NY), where 5 volunteers collected ~180 gallons of trash in one hour.

## What's Inside

### 📋 Templates
- **[Volunteer Signup Form](templates/volunteer-signup-form.md)** — Instructions to create a Google Form for volunteer signups
- **[Outreach Templates](templates/outreach-templates.md)** — Ready-to-use text for social media, newsletters, and flyers
- **[Post-Event Report Template](templates/post-event-report.md)** — Structured cleanup report form
- **[Thank-You Message Template](templates/thank-you.md)** — Post-cleanup volunteer appreciation messages

### 📖 Guides
- **[Safety & Privacy Quickstart](guides/safety-privacy-quickstart.md)** — 5–10 minute checklist and sample language for safe, privacy-aware cleanups
- **[Organizing a Cleanup (Start to Finish)](guides/organizing-a-cleanup.md)** — Complete step-by-step guide
- **[Evidence Collection Guide](guides/evidence-collection.md)** — How to document before/during/after with photos
- **[Day-of Execution Checklist](guides/day-of-checklist.md)** — What to do on cleanup day
- **[Volunteer Coordination](guides/volunteer-coordination.md)** — Managing signups, confirmations, and logistics

### 🌐 Website
The toolkit includes a static website you can deploy on GitHub Pages. See the `docs/` folder.

**Live demo:** [ai-village-agents.github.io/community-cleanup-toolkit](https://ai-village-agents.github.io/community-cleanup-toolkit/)

## Quick Start

1. **Fork this repo** to your own GitHub account or organization
2. **Customize** the templates in `templates/` for your park and community
3. **Enable GitHub Pages** (Settings → Pages → Source: main, folder: /docs)
4. **Follow the guide** in `guides/organizing-a-cleanup.md` to plan your event

## Real-World Results

This toolkit was born from organizing a real park cleanup:

| Metric | Value |
|--------|-------|
| Volunteers | 5 |
| Trash collected | ~180 gallons (6 × 30-gal bags) + 4 boxes |
| Duration | ~1 hour |
| Area covered | Sidewalks, 2 playgrounds, park entrance |
| Safety incidents | 0 |
| Cost | $0 (volunteers brought their own grabbers) |

## Contributing

Contributions welcome! If you've used this toolkit for a cleanup, we'd love to hear about it — open an issue or PR with your experience.

## License

MIT License — use freely, attribution appreciated.

---

*Made by the [AI Village](https://theaidigest.org/village) agents, based on the [Devoe Park cleanup project](https://github.com/ai-village-agents/park-cleanups).*

## Safety, Privacy, and Guardrails

This toolkit is designed to help you organize cleanups that are **effective, safe, and respectful**. We borrow our safety and privacy norms from the broader AI Village park cleanup ecosystem and the [civic-safety-guardrails](https://github.com/ai-village-agents/civic-safety-guardrails) project.

### What belongs in this repo (and your fork)

- High-level guides, checklists, and templates.
- Code and configuration needed to run your cleanup tooling or website.
- Public recap reports and case studies that have passed a **privacy redaction check** (no volunteer PII, no identifying photos).

### What does *not* belong here

- Personal contact information (emails, phone numbers, home addresses, private social handles).
- Raw sign-up sheets, RSVP lists, or survey exports with per-person data.
- Photos or videos that clearly show faces, license plates, encampments, or private homes.
- Authentication secrets (API keys, tokens, passwords) or private internal URLs.

Store volunteer and participant details in a **private system** you control (e.g., a private spreadsheet), not in your public GitHub repo.

### People-first and non-carceral norms

When you use this toolkit in the real world, we recommend the following norms:

- **We clean trash, not people.** The goal is to remove litter and hazards, not to police, displace, or shame anyone.
- Do **not** organize or participate in encampment sweeps or punitive cleanups that target unhoused neighbors.
- Volunteers should **not** directly handle sharps (needles, medical waste), suspicious chemicals, or heavy unstable objects; treat these as hazards to **mark and report** via local non-emergency channels.
- When in doubt, prioritize **privacy, de-escalation, and leaving if it feels unsafe** over "finishing" the cleanup.

For a deeper explanation and additional examples, see the [civic-safety-guardrails documentation](https://github.com/ai-village-agents/civic-safety-guardrails/tree/main/docs).
