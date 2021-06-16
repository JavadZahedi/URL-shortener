$(function(){

    $('#copy-btn').click(function(){
        var $field = $('#shortened-url');
        $field.select();
        document.execCommand("copy");
        alert('نشانی کوتاه شده کپی شد!');
        //$field.off('select');
    });

});