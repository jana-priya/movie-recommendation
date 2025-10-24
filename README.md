# Movie Recommendation System

A simple **Python + SQLite** project that recommends movies to users based on their favorite genre. This project demonstrates basic usage of **Python**, **pandas**, **SQLite**, and a simple AI/ML-like recommendation logic.

## Features
- Store movie data in an **SQLite database**.
- Filter movies by **genre**.
- Show all recommended movies and highlight the **top-rated movie**.
- Easy to extend with more movies or additional recommendation logic.

## Project Structure
```
movieProject/
├── movies.csv
├── setup_Db.py
├── recommend.py
└── README.md
```

## Installation
1. Clone the repository:
```bash
git clone https://github.com/yourusername/movie-recommendation-system.git
```
2. Navigate to the project folder:
```bash
cd movieProject
```


## How to Use
1. Setup the database (run once):
```bash
python setup_Db.py
```
2. Run the recommendation script:
```bash
python recommend.py
```
3. Enter your favorite genre when prompted (e.g., Sci-Fi, Action, Romance, Adventure).

4. See the list of recommended movies and the top-rated movie.

## Sample Output
```
Enter your favorite genre (Sci-Fi, Action, Romance, Adventure): Sci-Fi

Recommended Movies:
        title  rating
0   Inception     8.8
1  Interstellar     8.6

Top Movie for You:
        title  rating
0   Inception     8.8
```

## Technologies Used
- Python 3.x
- SQLite
- pandas library

## Files Description
| File | Description |
|------|-------------|
| `movies.csv` | Sample dataset containing movie titles, genres, and ratings. |
| `setup_Db.py` | Script to create SQLite database and insert data from CSV. |
| `recommend.py` | Script to recommend movies based on user input genre. |

## Author
Janapriya S P 
GitHub: https://github.com/jana-priya