# [THE MOVIE DB API] (https://www.themoviedb.org/documentation/api)

## ***API Overview***

Our API is available for everyone to use. A TMDb user account is required to request an API key. Professional users are approved on a per application basis.

As always, you must attribute TMDb as the source of your data. Please be sure to read the API FAQ.

### API Documentation

To view all the methods available, you should head over to developers.themoviedb.org. Everything outlined on this page is simply a high level overview to help you understand what is available.

### Finding Data

There are 3 ways to search for and find movies, TV shows and people on TMDb. They're outlined below.

`/search` - Text based search is the most common way. You provide a query string and we provide the closest match. Searching by text takes into account all original, translated, alternative names and titles.

`/discover` - Sometimes it useful to search for movies and TV shows based on filters or definable values like ratings, certifications or release dates. The discover method make this easy. For some example queries, and to get an idea about the things you can do with discover, take a look here.

`/find` - The last but still very useful way to find data is with existing external IDs. For example, if you know the IMDB ID of a movie, TV show or person, you can plug that value into this method and we'll return anything that matches. This can be very useful when you have an existing tool and are adding our service to the mix.

### General Features
* Top rated movies
* Upcoming movies
* Now playing movies
* Popular movies
* Popular TV shows
* Top rated TV shows
* On the air TV shows
* Airing today TV shows
* Popular people

### Account Features
* Get details
* Get lists (created and marked as favourite)
* Get favourite movie list
* Get movie watch list
* Get rated movie list
* Get the account state for a movie (rated, marked as favourite or on watch list)

### Account Session Features
* Rate a movie
* Add/remove a movie to your favourites
* Add/remove a movie to your watch list

### Guest Session Features (no sign up required)
* Rate a movie
* Get a list of rated movies

### Movie Features
* Search: Search for movies with a text query.
* Discover: Search for movies based on data. Movies are queryable by fields like average rating, certifications, release dates and genres.
* Find: Find movies based on an external ID like an IMDB ID.
* Get details
	* Primary info
	* Alternative titles
	* Cast
	* Crew
	* Images (posters, backdrops)
	* Plot keywords
	* Release information
	* Trailers
	* Translations
	* Similiar movies
	* Reviews
	* Belongs to lists
	* Changes

### TV Features
* Search: Search for TV shows with a text query.
* Discover: Search for TV shows based on data. TV shows are queryable by fields like average rating, air date, TV network and genres.
* Find: Find TV shows based on an external ID like an IMDB ID.
* Get details
	* Primary info
	* Cast
	* Changes
	* Crew
	* Images (posters, backdrops)
	* External IDs
	* Translations

### TV Season Features
* Get details
	* Primary info
	* Cast
	* Changes
	* Crew
	* Images (posters, backdrops)
	* External IDs

### TV Episode Features
* Get details
* Primary info
* Cast
* Changes
* Crew
* Images (posters, backdrops)
* External IDs

### Collection Features
* Search
* Get details
	* Images (posters, backdrops)

### People Features
* Search: Search for people with a text query.
* Find: Find people based on an external ID like an IMDB ID.
* Get details
	* Primary info
	* Changes
	* Credits (movie, TV and combined)
	* Images (profile)
	* Tagged images

### Company Features
* Search
* Get details
* Get movies

### List Features
* Search
* Get list movies

### Genre Features
* Get list
* Get movies

### Plot Keyword Features
* Search
* Get details
	* Get movies

### Job Features
* Get list