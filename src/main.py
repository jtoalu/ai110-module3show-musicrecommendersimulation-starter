"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from recommender import load_songs, recommend_songs


def main() -> None:
    songs = load_songs("data/songs.csv") 

    # Starter example profile. Various profiles can be tested by changing the values below.
    # Example profies are avaiable in the README.md file.
    user_prefs = {
        "favorite_genre": "rock",
        "favorite_mood": "intense",
        "target_energy": 1.0,
    }

    print("\nUSER PREFERENCES (edge_case_high_energy_prefs)")
    print("=" * 60)
    for name, value in user_prefs.items():
        print(f"{name.replace('_', ' ').title():<20} {value}")
    print("=" * 60)

    recommendations = recommend_songs(user_prefs, songs, k=5)    

    print("\nTOP RECOMMENDATIONS")
    print("=" * 60)

    for rank, (song, score, explanation) in enumerate(recommendations, start=1):
        print(f"\n{rank}. {song['title']} - {song['artist']}")
        print(f"   Score: {score:.2f}")
        print("   Why this was recommended:")

        for reason in explanation.split("; "):
            print(f"   - {reason}")

    print("\n" + "=" * 60)

if __name__ == "__main__":
        main()
