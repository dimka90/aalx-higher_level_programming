$(document).ready(function(){

    let apiurl = "https://swapi-api.alx-tools.com/api/people/5/?";

    $.ajax({
        url: apiurl,
        method:"GET",
        datatype:'json',
        success: function(data){
            $('#character').text(data.name);
        },
        error:function(error){
            console.log(error);
        }


    });
});