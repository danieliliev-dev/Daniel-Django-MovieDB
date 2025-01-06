API Documentation for Movie App

1. Movie Listing

Endpoint: /
Method: GET
Description:
Fetches a list of all movies in the system. The response will include the titles, descriptions, and any other relevant details of the movies.

2. Movie Detail

Endpoint: /movie/<int:movie_id>/
Method: GET
Description:
Fetches the details of a single movie by its movie_id. This will include all available information about the movie such as title, description, release date, and possibly the movie poster or related data.

Parameters:
movie_id: Integer representing the unique ID of the movie.

3. Movie Search

Endpoint: /search/
Method: GET
Description:
Search for movies based on query parameters. This allows users to search for movies by title, description, or other attributes.

Parameters:
q (required): A search query string used to filter movie results.

4. Add Movie

Endpoint: /add/
Method: POST
Description:
Allows the user to add a new movie to the database by providing movie details such as title, release date, description, and other relevant information.

Parameters:
title (required): The title of the movie.
release_date (required): The release date of the movie in YYYY-MM-DD format.
description (optional): A brief description of the movie.
poster (optional): The movie poster image (can be an uploaded file).

5. Toggle Favorite

Endpoint: /toggle_favorite/<int:movie_id>/
Method: POST
Description:
Allows a user to toggle the favorite status of a movie. This means marking the movie as a favorite or removing it from favorites.

Parameters:
movie_id: Integer representing the unique ID of the movie.

6. Movie Category

Endpoint: /category/<str:category>/
Method: GET
Description:
Fetches a list of movies belonging to a specific category. The category is passed as a string parameter in the URL.
Parameters:
category: The name of the movie category (e.g., "action", "comedy").

7. Authentication and User Accounts

Endpoint: /accounts/
Method: Varies (handled by django.contrib.auth URLs)
Description:
This includes various endpoints for user authentication, such as login, logout, and password management. These routes are provided by Django's built-in authentication system.

/accounts/login/: Log in a user.
/accounts/logout/: Log out a user.
/accounts/password_change/: Change the user's password.
/accounts/password_reset/: Reset the user's password if forgotten.

Notes:
The API uses standard HTTP status codes to communicate the result of each request.
All responses are either in JSON format or HTML depending on whether you're using Django's template rendering or working with an API client.
Authentication is likely required for endpoints such as adding a movie or toggling a favorite (you can implement this using Django's built-in authentication system).

Example of how to use these endpoints:
1. Get a list of all movies:
GET http://example.com/
2. Search for a movie by title:
GET http://example.com/search/?q=inception
3. Add a movie:
POST http://example.com/add/
{
    "title": "The Dark Knight",
    "release_date": "2008-07-18",
    "description": "Batman faces the Joker, a criminal mastermind."
}
4. Get movies in a specific category:
GET http://example.com/category/action/