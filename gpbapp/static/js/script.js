//
// CAROUSEL
//

$("#minitel-screen").hide();
$("#btn_minitel").hide();

$(function (){
    $('#myCarousel').carousel();
});

$('#myCarousel').carousel({interval: 10000});

//
// MINITEL
//

function click_on_switch() {
    if ($("#minitel-screen").css("display") === "none"){
        $("#myCarousel").hide();
        $("#minitel-screen").show();
        $("#btn_minitel").show();
        $("#input_minitel").focus();
    } else {
        $("#minitel-screen").hide();
        $("#touch_minitel").hide();
        $("#myCarousel").show();
    }
}

//
// DIALOG BOX
//

$("#input_dialog").focus();

function fixe_scroll_down() {
    document.getElementById(
        'dialog-area').scrollTop = document.getElementById(
        'dialog-area').scrollHeight;
}

fixe_scroll_down();

// create and add user's message
function create_add_user_msg($new_msg){
    var $new_card = $("<div>").html(
        "<i class='fa fa-user-circle-o fa-2x'></i>");
    $new_card.addClass(
        "msg_user col-md-12 card alert-success text-center");
    $new_card.append($new_msg);
    $("#dialog-area").append($new_card);
}

// create and add GrandPy Bot message
function create_add_gpb_msg($new_msg){
    var $img_gpb = $("#gpb_img_msg").clone();
    var $new_card = $("<div>").append($img_gpb).append($('<br />'));
    $new_card.addClass("msg_gpb col-md-12");
    $new_card.addClass("card alert-info text-center");
    $new_card.append($new_msg);
    $("#dialog-area").append($new_card);
    fixe_scroll_down();
}

//
// ANSWER
//

// Create map
function initMap(map_div, location) {
    $("#dialog-area").append(map_div);
    var uluru = location;
    var map = new google.maps.Map(
        document.getElementById(map_div.attr('id')), {
        zoom: 4,
        center: uluru
        }
    );
    var marker = new google.maps.Marker({
        position: uluru,
        map: map
    });
    fixe_scroll_down();
}

// create and add GrandPy Bot message with server's result
var $map_div = $("<div id='map' class='col-md-12'></div>");

function prepare_answer(api_response){
    if (api_response.found === "NO"){
        var $new_msg = $("<p>").html(api_response.response);
        $("#loading_img").replaceWith($new_msg);
    } else {
        var $response = api_response.response;
        var $new_msg = "Ah oui!!!";
        $new_msg = $("<p>").html($new_msg);
        $("#loading_img").replaceWith($new_msg);
        $new_msg = $response.name + " dont l'adresse exacte est ";
        $new_msg += $response.address;
        create_add_gpb_msg($new_msg);
        // create map
        $location = $response.location;
        initMap($map_div, $location);
        $new_msg = (
            "Oh mais j'y suis déjà allé, et si je me souviens bien... ");
        $new_msg += $response.text;
        create_add_gpb_msg($new_msg); 
    }
}

//
// EVENTS
//

// event click on button
function click_btn(input_user){
    if (input_user !== ""){
        // Ajax request
        $.getJSON("/api", {a: input_user}, function(data){
            prepare_answer(data)
        });
        // add msg in dialog box
        var $new_msg = $("<p>").html(input_user);
        create_add_user_msg($new_msg);
        // add loading msg
        var $new_msg = $('<img />', {
            id: "loading_img",
            class: "card-img", 
            src: "../static/img/loading.gif",
            alt: 'loading'
        });
        create_add_gpb_msg($new_msg);
        fixe_scroll_down();
    }
}


function click_btn_dialog(){
    var $input_user = $("#input_dialog").val();
    $("#input_dialog").val("");
    $("#input_dialog").focus();
    click_btn($input_user);
}

function click_btn_minitel(){
    var $input_user = $("#input_minitel").val();
    $("#input_minitel").val("");
    $("#input_minitel").focus();
    click_btn($input_user);
}

// event return key
$("#input_dialog").keyup(function(e) {
    if(e.keyCode == 13) { // KeyCode return key
        click_btn_dialog();
    }
});


