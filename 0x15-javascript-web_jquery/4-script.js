$(document).ready(function(){

$('header').click(function(){

    if($(this).hasClass('red'))
    {
        $(this).toggleClass('green')
    }
    else
    {
        $(this).toggleClass('red')
    }
})

});