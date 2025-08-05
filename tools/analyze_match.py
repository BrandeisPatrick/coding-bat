#!/usr/bin/env python3
"""Analyze a Deadlock match and compute average player rank for each team.

This script fetches match metadata from the Deadlock API and calculates the
average rank of players on both teams. Ranks are provided as badge strings
(such as "Gold 2" or "Diamond 3") and are mapped to numeric values so that an
average can be computed.

Usage:
    python tools/analyze_match.py MATCH_ID [API_KEY]

If an API key is provided it will be used as a Bearer token when calling the
API. Otherwise the request is unauthenticated.
"""
from __future__ import annotations

import sys
from typing import List, Dict, Optional

try:
    import requests
except Exception as exc:  # pragma: no cover - requests should be available
    raise SystemExit("The 'requests' package is required to run this script") from exc

# Ordered list of tiers as exposed by the game.
TIERS: List[str] = [
    "Iron",
    "Bronze",
    "Silver",
    "Gold",
    "Platinum",
    "Diamond",
    "Master",
    "Grandmaster",
]


def badge_to_value(badge: Optional[str]) -> int:
    """Convert a badge string like ``"Gold 2"`` to a numeric value.

    Unranked players return ``0``. Tiers up to Diamond have three sub-ranks
    (1‑3). Master and Grandmaster are treated as single levels.
    """
    if not badge or badge.lower() == "unranked":
        return 0

    parts = badge.split()
    tier = parts[0].capitalize()

    # Determine tier offset
    try:
        tier_index = TIERS.index(tier)
    except ValueError:
        return 0

    # Determine subrank, defaulting to 1 if not present.
    level = int(parts[1]) if len(parts) > 1 and parts[1].isdigit() else 1

    if tier_index <= 5:  # Iron -> Diamond (three sub-levels)
        return tier_index * 3 + level
    # Master and Grandmaster: single levels
    return 18 + (tier_index - 5)


def value_to_badge(value: float) -> str:
    """Convert a numeric rank value back to the closest badge string."""
    if value <= 0:
        return "Unranked"

    # Master and Grandmaster are single levels
    if value >= 19:
        return "Master" if value < 20 else "Grandmaster"

    # Calculate tier and level for Iron -> Diamond
    tier_index = int((value - 1) // 3)
    level = int(round(value - tier_index * 3))
    tier = TIERS[tier_index]
    return f"{tier} {level}"


def average_rank(players: List[Dict]) -> float:
    values = [badge_to_value(p.get("badge")) for p in players]
    return sum(values) / len(values) if values else 0.0


def analyze(match_id: str, api_key: Optional[str] = None) -> None:
    url = f"https://api.deadlock-api.com/v1/matches/{match_id}/metadata"
    headers = {"Accept": "application/json"}
    if api_key:
        headers["Authorization"] = f"Bearer {api_key}"

    resp = requests.get(url, headers=headers, timeout=30)
    resp.raise_for_status()
    data = resp.json()

    team_a = data.get("team_a", {}).get("players", [])
    team_b = data.get("team_b", {}).get("players", [])

    avg_a = average_rank(team_a)
    avg_b = average_rank(team_b)

    print(f"Team A average rank: {avg_a:.2f} ({value_to_badge(avg_a)})")
    print(f"Team B average rank: {avg_b:.2f} ({value_to_badge(avg_b)})")


if __name__ == "__main__":
    if len(sys.argv) < 2 or len(sys.argv) > 3:
        raise SystemExit("Usage: python tools/analyze_match.py MATCH_ID [API_KEY]")
    match_id = sys.argv[1]
    api_key = sys.argv[2] if len(sys.argv) == 3 else None
    analyze(match_id, api_key)
