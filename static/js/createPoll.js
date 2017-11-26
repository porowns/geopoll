$(function() {
    $('#btnCreatePoll').click(function() {

        $.ajax({
            url: '/createPoll',
            data: $('form').serialize(),
            type: 'POST',
            success: function(response) {
                console.log(response);
            },
            error: function(error) {
                console.log(error);
            }
        });
    });
});