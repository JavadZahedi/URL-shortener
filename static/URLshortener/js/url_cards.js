$(function(){
    $('.delete-url').click(function(){
        var label = $(this).attr('label');
        var address = $(this).attr('address');
        var message = 'نشانی با عنوان \"' + label + '\" و آدرس <br>' + address + '<br>' +' حذف شود؟';
        $('#delete-url-message').html(message);
        $('#delete-url-confirm').attr('href',  $(this).attr('request_url'));
        $('#delete-url-overlay').removeClass('d-none');
    });

    $('#close-delete-url, #cancel-delete-url').click(function(){
    	$('#delete-url-overlay').addClass('d-none');
    });
});