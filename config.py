import json
import os

PROFILE_PATH = os.path.join(os.path.dirname(__file__), "radar_profile.json")

# Defaults — used when no profile exists yet
_DEFAULT_CITIES = [
    "Atlanta", "Houston", "Chicago", "New York", "Washington DC",
    "Los Angeles", "Philadelphia", "Charlotte", "Detroit", "Memphis",
    "Baltimore", "Dallas", "Miami", "Oakland", "New Orleans", "Richmond",
]

_DEFAULT_KEYWORDS = [
    "business", "entrepreneur", "networking", "startup", "founder",
    "community", "professional", "commerce", "market", "conference",
]

_DEFAULT_COMMUNITY = "business owners and entrepreneurs"


def load_profile() -> dict:
    if os.path.exists(PROFILE_PATH):
        try:
            with open(PROFILE_PATH) as f:
                return json.load(f)
        except Exception:
            pass
    return {}


def save_profile(profile: dict) -> None:
    with open(PROFILE_PATH, "w") as f:
        json.dump(profile, f, indent=2)


profile = load_profile()

CITIES = profile.get("cities", _DEFAULT_CITIES)
KEYWORDS = profile.get("keywords", _DEFAULT_KEYWORDS)
COMMUNITY = profile.get("community", _DEFAULT_COMMUNITY)

CITIES_PER_RUN = 7
MAX_EVENTS_TO_SCORE = 200
MIN_SCORE_THRESHOLD = 5
TOP_N_EVENTS = 50
