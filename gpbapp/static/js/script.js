// CAROUSEL

$(function (){
    $('#myCarousel').carousel();
});

$('#myCarousel').carousel({interval: 10000});


// MINITEL

function click_on_switch() {
    if ($("#minitel-screen").css("display") == "none"){
        $("#myCarousel").css("display", "none");
        $("#minitel-screen").css("display", "inline-block");
        $("#touch_minitel").css("display", "inline-block");
        $('#InputToFocus').focus();
    } else {
        $("#minitel-screen").css("display", "none");
        $("#touch_minitel").css("display", "none");
        $("#myCarousel").css("display", "inline-block");
    }
    
}
