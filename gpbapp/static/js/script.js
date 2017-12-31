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


// create and add user's message
function create_add_msg_card($new_msg){
    var $new_card = $("<div>").html("<i class='fa fa-user-circle-o fa-2x'></i>");
    $new_card.addClass("msg_user col-md-11 card alert-success text-center");
    $new_card.append($new_msg);
    $("#dialog-area").append($new_card);
    document.getElementById('dialog-area').scrollTop = document.getElementById('dialog-area').scrollHeight;
}

// event click on button

function click_btn_dialog(){
    var $input_user = $("#input_dialog").val();
    var $new_msg = $("<p>").html($input_user);
    create_add_msg_card($new_msg);
    $("#input_dialog").val("");
}

// event return key
$("#input_dialog").keyup(function(e) {
    if(e.keyCode == 13) { // KeyCode return key
        click_btn_dialog();
    }
});

