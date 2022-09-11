# Project 5 (RATING)
This project is all about a web application that users can get information about movies such as rating , directors ,actors, etc… 
They can even rate to them or leave comments, even reading other people's comments 
This project is inspired by IMDb and based on it and this is completely different from the project 2 & project 4. Maybe it's not as interactive as them but it's so useful 
Users can find out their favorite movies, watch trailers and create their own watchlit
Even they can recommend them to the others and leave comments

## Models.py
User : same as previous projects in this class we save users information in database <br/>
Actors : here we save actors name, information and image url <br/> 
Directors : here we save directors name, information and image url <br/>
Movies : in this class we try to save name, information, trailer url, image url, gener, 
rate (sum of all rates) , rate_num (number of raters), rate_user (users who have rated)
rate_resualt ( rate / rate_num ), also there are ForeignKeys to Actors & Directors class <br/>
Trend : there is a ForeignKey to Movies to saving trend and hot movies uptodate\
### so far we can add or update these data only by superuser (admin) <br/>
Watchlist : by this class we can add or remove movies to the user watchlist <br/>
Comment : users' comments include (user, movie, comment, timestampe) come to this class and they'll be saved in database <br/>

## Urls.py 
Here we have a default route called index , ( login, logout, register ) for users, movie_page to show movies details, watchlist to update users watchlists, user-watchlist to show user watchlist, 
Rate to record rates, info_page to show directors&actors informations, comment to save comments and category to show movies by category

## Specification :
The default route shows two to of the most trend and hot movies in top of the page and under that are top 5 movies order by ranting and you can see these info ( rate, name and trailer button ), clicking on each of them take user to the movie's information page
On movie_page user see full information about the movie if user is authenticated he/she can vote for that movie, add/remove it from watchlist ( this action will be done by javascript ) and leave comments . clicking on "comments" link display all comments
Clicking on every directors or actors name takes users to info_page where they can see information about that director/actor
On the navbar if user is authenticated he/she can see own username, Home link (takes user to default rout), category dropbutton ( takes user to category page ), whatchlist link ( takes user to own watchlist ) and logout link ( logout user )
if user is not authenticated only Home , category, login and register link will appear
clicking on category dropdown shows  categories and clicking on each of them takes user to category page where user can see all movies order by that category 
clicking on watchlist link (from the navbar)takes users to their own watchlist and they can remove them from there ( this action will be done by javascript ), clicking on each of the takes user to movie_page
button "watch trailer on you tube" takes user to youtube where they can watch trailer  
and my web application is responsive
