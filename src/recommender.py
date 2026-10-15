from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        # TODO: Implement recommendation logic
        return self.songs[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        # TODO: Implement explanation logic
        return "Explanation placeholder"

def load_songs(csv_path: str) -> List[Dict]:
    """
    Loads songs from a CSV file.
    Required by src/main.py
    """
    # TODO: Implement CSV loading logic
    print(f"Loading songs from {csv_path}...")
    return []

def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """
    Scores a single song against user preferences.
    Required by recommend_songs() and src/main.py
    """
    # TODO: Implement scoring logic using your Algorithm Recipe from Phase 2.
    # Expected return format: (score, reasons)

    preferred_genres = user_prefs.get("preferred_genres", {})
    preferred_moods = user_prefs.get("preferred_moods", {})

    if preferred_genres:
        genre_points = 2.0 * preferred_genres.get(song["genre"], 0.0)
    else:
        genre_points = 2.0 if song["genre"] == user_prefs.get("favorite_genre") else 0.0

    if preferred_moods:
        mood_points = preferred_moods.get(song["mood"], 0.0)
    else:
        mood_points = 1.0 if song["mood"] == user_prefs.get("favorite_mood") else 0.0

    target_energy = user_prefs.get(
        "energy_preference",
        user_prefs.get("target_energy", 0.5),
    )
    energy_points = 1.0 - abs(song["energy"] - target_energy)

    score = genre_points + mood_points + energy_points
    reasons = []

    if genre_points > 0:
        reasons.append(f"Genre match: +{genre_points:.1f}")
    if mood_points > 0:
        reasons.append(f"Mood match: +{mood_points:.1f}")
    reasons.append(f"Energy similarity: +{energy_points:.2f}")

    return score, reasons

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """
    Functional implementation of the recommendation logic.
    Required by src/main.py
    """
    # TODO: Implement scoring and ranking logic
    # Expected return format: (song_dict, score, explanation)
    return []
