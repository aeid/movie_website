import fresh_tomatoes
import media

toy_story = media.Movie("Toy Story", "A story of a boy", "http://imageserver.moviepilot.com/group-disney-announces-toy-story-4-is-happening.webp?width=960&height=648", "https://www.youtube.com/watch?v=Bj4gS1JQzjk")
death_of_a_salesman = media.Movie("Death of a salesman", "a story", "http://upload.wikimedia.org/wikipedia/en/2/20/DeathOfASalesman.jpg", "https://www.youtube.com/watch?v=0fyh3ihHt4w")
spacejam = media.Movie("Space Jam", "a story", "http://upload.wikimedia.org/wikipedia/en/1/14/Space_jam.jpg", "https://www.youtube.com/watch?v=0fyh3ihHt4w")

movies = [toy_story, death_of_a_salesman, spacejam]

fresh_tomatoes.open_movies_page(movies)