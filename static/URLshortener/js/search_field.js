$(function(){
    $('#search-field').on('focus keyup', function(){
        var key = $(this).val();
        if (key.length === 0)
            $('#search-result').html('');
        else {
            var url = $(this).attr('url');
            var page = $(this).attr('search_page');
            var request_url = url + '?search_page=' + page + '&search_key=' + key;
            $.get(request_url, function(data, status){
                $('#search-result').html(data);
            });
        }
    });

    $('#search-field').blur(function(){
        $('#search-result').html('');
    });
});