$(document).ready(function () {
    // Mensaje
    function sendMessage() {
        var message = $('#message').val();
        if (message.trim() !== '') {
            var listItem = $('<li class="collection-item">').text(message);
            $('#chat-messages').append(listItem);
            $('#message').val('');
        }
    }

    $('#send').click(function () {
        sendMessage();
    });

    $('#message').keypress(function (event) {
        if (event.keyCode === 13) {
            sendMessage();
        }
    });
});