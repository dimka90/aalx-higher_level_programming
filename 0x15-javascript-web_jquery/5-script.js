$(document).ready(function()
{

    $('#add_item').click(function (){

        let text = $('<li>').text('item');

        $('.my_list').append(text);
    });

});