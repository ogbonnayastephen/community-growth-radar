# Growth Radar

An open-source AI agent that finds events, expos, and community gatherings for **any audience you define** — scored by Claude AI and delivered to your inbox every Monday.

Built for founders, community builders, and growth teams who need to show up where their people are.

## Live Demo

Try it at [growth-radar.streamlit.app](https://growth-radar.streamlit.app) — no setup required.

## Quick Start (Local)

```bash
git clone https://github.com/YOURUSERNAME/growth-radar
cd growth-radar
pip install -r requirements.txt
cp .env.example .env
# Add your API keys to .env
python main.py --once
```

## Get Your API Keys

| Key | Source | Purpose |
|-----|--------|---------|
| `ANTHROPIC_API_KEY` | [console.anthropic.com](https://console.anthropic.com) | Powers AI scoring (~$0.50/run) |
| `RESEND_API_KEY` | [resend.com](https://resend.com) | Free email delivery |
| `RESEND_FROM_EMAIL` | Your verified Resend sender | From address for emails |
| `ALERT_EMAIL` | Your email | Where results get delivered |

## How It Works

1. **Define your audience** — Run `app.py` in Streamlit, describe your community, add keywords, pick cities. Saved to `radar_profile.json`.
2. **Scrape** — Rotates through your selected cities per run, searching AlleEvents and Luma for events matching your keywords.
3. **Score** — Claude AI scores each event 1–10 for relevance to your specific audience.
4. **Deliver** — Sends one HTML email with the top 50 events sorted by date, plus city-level opportunity scores.
5. **Outreach** — Click any event in the Streamlit app to generate a personalized first outreach email in 30 seconds.

## Setting Your Audience Profile

The first time you run the Streamlit app, define:
- **Community description** — who you are trying to reach (be specific)
- **Keywords** — terms your community searches for and organizes around
- **Cities** — up to 7 US cities per run

This saves to `radar_profile.json` and is used by both the app and the automated email pipeline.

## Automated Weekly Email (GitHub Actions — free)

1. Push this repo to GitHub
2. Go to **Settings → Secrets → Actions** and add:
   - `ANTHROPIC_API_KEY`
   - `RESEND_API_KEY`
   - `RESEND_FROM_EMAIL`
   - `ALERT_EMAIL`
3. Commit your `radar_profile.json` to the repo so GitHub Actions knows your audience
4. Enable Actions — runs automatically every **Monday at 6am EST**
5. Trigger a manual run anytime via **Actions → Run workflow**

## Project Structure

```
growth-radar/
├── main.py              # Headless pipeline — scrape, score, email
├── app.py               # Streamlit UI — interactive runs + outreach generator
├── config.py            # Profile loader, defaults, thresholds
├── radar_profile.json   # Your saved audience (auto-created on first run)
├── scrapers/
│   └── events.py        # AlleEvents + Luma scrapers
├── scoring/
│   ├── event_scorer.py  # Claude AI event scoring (audience-aware)
│   └── city_scorer.py   # Claude AI city opportunity scoring
├── alerts/
│   └── digest.py        # HTML email builder + Resend delivery
└── .github/workflows/
    └── radar.yml        # GitHub Actions weekly schedule
```

## Customization

- **Audience and keywords** → Run the Streamlit app or edit `radar_profile.json` directly
- **Score threshold** → Change `MIN_SCORE_THRESHOLD` in `config.py`
- **Email design** → Edit `alerts/digest.py`
- **Add scrapers** → Drop new scrapers in `scrapers/` and import in `events.py`

## License

MIT — free to use, fork, and build on.
