$(document).ready(function() {
    // URL of the SWAPI films endpoint
    var apiUrl = 'https://swapi-api.alx-tools.com/api/films/?format=json';

    // Fetch movie data from SWAPI
    $.ajax({
      url: apiUrl,
      method: 'GET',
      dataType: 'json',
      success: function(data) {
        // Check if the data contains results
        if (data.results && data.results.length > 0) {
          // Iterate through each movie and append its title to the list
          $.each(data.results, function(index, movie) {
            $('#list_movies').append('<li>' + movie.title + '</li>');
          });
        } else {
          // Handle the case where no results are found
          $('#list_movies').append('<li>No movies found</li>');
        }
      },
      error: function(error) {
        // Handle errors
        console.error('Error:', error);
        $('#list_movies').append('<li>Error fetching movie data</li>');
      }
    });
  });