import fresh_tomatoes
import media

jurassic = media.Movie("Jurassic World",
"Finally a decent sequel to Jurassic Park",
"http://cdn1-www.superherohype.com/assets/uploads/gallery/jurassic-world/"
"10623357_908272402550977_6384474390653526950_o.jpg",
"https://www.youtube.com/watch?v=L-6G911eCvg",
"Chris Pratt, Bryce Dallas Howard, Vincent D'Onofrio")

avatar = media.Movie("Avatar",
"The story of a marine who likes trees",
"https://mrmoviefiend.files.wordpress.com/2010/06/avatar-poster-10.jpg",
"https://www.youtube.com/watch?v=5PSNL1qE6VY",
"Sam Worthington, Zoe Saldana, Stephen Lang, Michelle Rodriguez")


prometheus = media.Movie("Prometheus",
"The story of a really old man with a huge ego",
"http://www.joblo.com/posters/images/full/promethus.jpg",
"https://www.youtube.com/watch?v=34cEo0VhfGE",
"Noomi Rapace, Michael Fassbender, Guy Pearce, Idris Elba")

district9 = media.Movie("District9",
"A story about a man who goes full bug",
"http://www.filmofilia.com/wp-content/uploads/2009/07/district9_poster.jpg",
"https://www.youtube.com/watch?v=DyLUwOcR5pk",
"Sharlto Copley, Jason Cope, David James")

antman = media.Movie("Antman",
"The story of a man who shrinks",
"http://blogs-images.forbes.com/scottmendelson/files/2015/05/BF_Payoff_"
"1-Sht_v8_Lg-1309x1940.jpg",
"https://www.youtube.com/watch?v=pWdKf3MneyI",
"Paul Rudd, Evangeline Lilly, Michael Douglas")

limitless = media.Movie("Limitless",
"A man does drugs to be creative",
"http://fo4mw16y1z42edr6j2m4n6vt.wpengine.netdna-cdn.com/wp-content"
"/uploads/Limitless-Poster.jpg",
"https://www.youtube.com/watch?v=jOLqNOfzus4",
"Bradley Cooper, Abbie Cornish, Robert De Niro")

forgetting = media.Movie("Forgetting Sarah Marshall",
"A man tries to get over a break up only to find his ex with another man on vacation",
"http://2.bp.blogspot.com/_DzKCQgfaOjs/TVEvlGBe1uI/AAAAAAAAAIQ/dR0dNkx6XBI/s1600"
"/2008-forgetting_sarah_marshall-3.jpg",
"https://www.youtube.com/watch?v=GSwA6QQW8P4",
"Jason Segel, Kristen Bell, Mila Kunis, Russell Brand")

bladeRunner = media.Movie("Blade Runner",
"A freaking awesome film",
"http://www.findelahistoria.com/web/wp-content/uploads/2014/02/Blade-Runner-poster-7.jpg",
"https://www.youtube.com/watch?v=iYhJ7Mf2Oxs",
"Harrison Ford, Rutger Hauer, Sean Young")

terminator2 = media.Movie("Terminator 2",
"A young John Connor befriends a terminator sent back in time to protect him",
"http://www.schwarzenegger.com/assets/uploads/images/index/Terminator-2-"
"Judgment-Day-movie-poster.jpg",
"https://www.youtube.com/watch?v=eajuMYNYtuY",
"Arnold Schwarzenegger, Linda Hamilton, Robert Patrick")


movies = [jurassic, avatar, prometheus, district9, antman, limitless, forgetting, bladeRunner, terminator2]

fresh_tomatoes.open_movies_page(movies)
