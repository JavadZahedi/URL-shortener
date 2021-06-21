$(function(){
    $('#delete-photo').click(function(){
        $('#delete-photo-overlay').removeClass('d-none');
    });

    $('#close-delete-photo, #cancel-delete-photo').click(function(){
    	$('#delete-photo-overlay').addClass('d-none');
    });
});