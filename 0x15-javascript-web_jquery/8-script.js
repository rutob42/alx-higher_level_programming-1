$(document).ready(function(){
    $.get('https://swapi-api.alx-tools.com/api/films/?format=json', function(data){
        const movies = data.results;
        for (let i = 0; i < movies.length; i++){
            const movieTitle = movies[i].title;
            $('UL#list_movies').text(movieTitle);
        }

    })
})