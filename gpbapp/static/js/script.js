// CAROUSEL

$("#minitel-screen").hide();
$("#touch_minitel").hide();

$(function (){
    $('#myCarousel').carousel();
});

$('#myCarousel').carousel({interval: 10000});


// MINITEL

function click_on_switch() {
    if ($("#minitel-screen").css("display") == "none"){
        $("#myCarousel").hide();
        $("#minitel-screen").show();
        $("#touch_minitel").show();
        $('#InputToFocus').focus();
    } else {
        $("#minitel-screen").hide();
        $("#touch_minitel").hide();
        $("#myCarousel").show();
    }
    
}


// create and add user's message
function create_add_user_msg($new_msg){
    var $new_card = $("<div>").html(
        "<i class='fa fa-user-circle-o fa-2x'></i>");
    $new_card.addClass(
        "msg_user col-md-11 card alert-success text-center");
    $new_card.append($new_msg);
    $("#dialog-area").append($new_card);
    document.getElementById(
        'dialog-area').scrollTop = document.getElementById(
        'dialog-area').scrollHeight;
}

// create and add GrandPy Bot message
function create_add_gpb_msg($new_msg){
    var $img_gpb = $("#gpb_img_msg").clone();
    var $new_card = $("<div>").append($img_gpb).append($('<br />'));
    $new_card;
    $new_card.addClass("msg_gpb col-md-11 col-md-offset-1");
    $new_card.addClass("card alert-info text-center");
    $new_card.append($new_msg);
    $("#dialog-area").append($new_card);
    document.getElementById(
        'dialog-area').scrollTop = document.getElementById(
        'dialog-area').scrollHeight;
}


function prepare_answer(api_response){
    alert(api_response);
}

// event click on button

function click_btn_dialog(){
    var $input_user = $("#input_dialog").val();
    if ($input_user !== ""){
        // Ajax request
        $.getJSON("/api", {a: $input_user}, function(data){
            prepare_answer(data);
        });
        // add msg in dialog box
        var $new_msg = $("<p>").html($input_user);
        create_add_user_msg($new_msg);
        $("#input_dialog").val("");
        // add loading msg
        var $new_msg = $('<img />', {
            class: "card-img", 
            src: "../static/img/loading.gif",
            alt: 'loading'
        });
        create_add_gpb_msg($new_msg);
    }
};

// event return key
$("#input_dialog").keyup(function(e) {
    if(e.keyCode == 13) { // KeyCode return key
        click_btn_dialog();
    }
});

