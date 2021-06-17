$(function(){
    $('#delete-photo').click(function(){
        $('#overlay').removeClass('d-none');
    });

    $('#close, #no').click(function(){
    	$('#overlay').addClass('d-none');
    });
});