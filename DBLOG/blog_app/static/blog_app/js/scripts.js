$(document).ready(function(){
    $('.footer__heading').click(function(event){

        $(this).toggleClass('active').next().slideToggle(300);
    });
});