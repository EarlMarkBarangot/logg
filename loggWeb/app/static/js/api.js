
// the main course advising api

$(document).ready(function(){
    $('#loggg').click(function(){
        console.log('earll');
        event.preventDefault();
        var username = $('#username').val();
        var password = $('#password').val();
        $.ajax({
        url: 'http://127.0.0.1:3000/api/login',
        data: {'username':username, 'password':password},
        type:"GET",
        dataType: 'json',
        crossDomain: true,
            success: function(response) {
                if(response.msg=='ok'){
                    $('#formpostlog').submit();
                    // /window.location.assign(response.next_node);
                }
            },
            error: function(error) {
                console.log(error);
            },
        });
    });
});



/*function login(){
    var username = $('#username').val();
    var password = $('#password').val();
    alert(username);
    $.ajax({
        url: 'http://0.0.0.0:3000/api/login',
        data: {'username':username, 'password':password},
        type:"GET",
        dataType: 'json',
        crossDomain: true,
            success: function(response) {
                alert(response.msg)
                if(response.msg=='ok'){
                    alert('welcome');
                    console.log(response.next_node);
                    window.location.assign(response.next_node);
                }
            },
            error: function(error) {
                alert(error);
            },
    });
}*/

function signup(){
    var email = $('#Email').val();
    var username = $('#username').val();
    var password = $('#password').val();
    $.ajax({
        url: 'http://127.0.0.1:3000/api/signup',
        data: {'email': email, 'username':username, 'password':password},
        type:"POST",
        dataType: 'json',
        crossDomain: true,
            success: function(response) {
                if(response.msg=='ok'){
                    console.log('earll')
                    window.location.assign(response.next_node);
                }
            },
            error: function(error) {
                console.log(error);
            },
    });
}

function home(){
    var user = $('#holder').val();
    $.ajax({
        url: 'http://127.0.0.1:3000/api/home',
        data: {'username': user},
        type:"GET",
        dataType: 'json',
        crossDomain: true,
            success: function(response) {
                if(response.msg=='ok'){
                    $('#info').html('');
                    $('#info').append('<h1>'+response.email+'</h1>');
                }
            },
            error: function(error) {
                console.log(error);
            },
    });
}
