# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

Give your model a short, descriptive name.  
Example: **VibeFinder 1.0**  

---

## 2. Intended Use  

Describe what your recommender is designed to do and who it is for. 

Prompts:  

- What kind of recommendations does it generate  
- What assumptions does it make about the user  
- Is this for real users or classroom exploration  

---

## 3. How the Model Works  

Explain your scoring approach in simple language.  

Prompts:  

- What features of each song are used (genre, energy, mood, etc.)  
- What user preferences are considered  
- How does the model turn those into a score  
- What changes did you make from the starter logic  

Avoid code here. Pretend you are explaining the idea to a friend who does not program.

The recommender works by comparing each song to the user’s taste profile using simple musical features like genre, mood, energy, and tempo. It gives each song a score based on how closely it matches the traits the user seems to prefer, and it lowers the score when a song is very different from those preferences. In other words, songs that feel similar to the user’s favorite styles are ranked higher, while songs that do not fit those patterns are pushed lower. After scoring all songs, the model sorts them from best match to worst and recommends the top results. This is similar to how a friend might make a playlist: they look at what you usually like, notice the patterns in your tastes, and then choose songs that fit those patterns best while still keeping the list interesting and varied.

---

## 4. Data  

Describe the dataset the model uses.  

Prompts:  

- How many songs are in the catalog  
- What genres or moods are represented  
- Did you add or remove data  
- Are there parts of musical taste missing in the dataset  

---

## 5. Strengths  

Where does your system seem to work well  

Prompts:  

- User types for which it gives reasonable results  
- Any patterns you think your scoring captures correctly  
- Cases where the recommendations matched your intuition  

---

## 6. Limitations and Bias 

Where the system struggles or behaves unfairly. 

Prompts:  

- Features it does not consider  
- Genres or moods that are underrepresented  
- Cases where the system overfits to one preference  
- Ways the scoring might unintentionally favor some users  

The implemented score_song function has a few potential biases and filter-bubble effects:

- Strong genre preference: A genre match can add up to 2 points, compared with 1 point for mood and 1 point for energy similarity. This can make genre dominate the ranking, even when a song is a poor match on other dimensions.
- Exact-match bias: Without weighted preference dictionaries, only the single favorite genre and mood earn points. Songs from neighboring or similar genres and moods get no credit, which may narrow recommendations.
- Narrow preference input: If preferred_genres or preferred_moods is supplied, the function uses that dictionary instead of the corresponding favorite value. Any song category not explicitly included in the dictionary gets zero points.
- Limited feature coverage: The scoring ignores tempo, valence, danceability, acousticness, and likes_acoustic. Users who care about those traits may get recommendations that don’t reflect their preferences.
- No diversity step: Recommendations are sorted by score and the top k are returned. There is no mechanism to encourage variety, so similar songs or genres can fill the list.
- Catalog and tie-order effects: Songs with equal scores retain their original catalog order. If the dataset overrepresents certain genres or orders them first, those songs could appear more often in recommendations.

---

## 7. Evaluation  

How you checked whether the recommender behaved as expected. 

Prompts:  

- Which user profiles you tested  
- What you looked for in the recommendations  
- What surprised you  
- Any simple tests or comparisons you ran  

No need for numeric metrics unless you created some.

---

## 8. Future Work  

Ideas for how you would improve the model next.  

Prompts:  

- Additional features or preferences  
- Better ways to explain recommendations  
- Improving diversity among the top results  
- Handling more complex user tastes  

---

## 9. Personal Reflection  

A few sentences about your experience.  

Prompts:  

- What you learned about recommender systems  
- Something unexpected or interesting you discovered  
- How this changed the way you think about music recommendation apps  
