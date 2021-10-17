// Create
$(function () {
    $('.js-create-book').click(function () {
        $.ajax({
            url: '/stock/create',
            type: 'get',
            dataType: 'json',
            beforeSend: function () {
                $("#modal-stock").modal("show");
            },
            success: function (data) {
                $('#modal-stock .modal-content').html(data.form)
            }
        })
    })
})

$('modal-stock').on('submit', '.js-stock-create-form', function () {
    var form = $(this)
    $.ajax({
        url: form.attr('action'),
        data: form.serialize(),
        type: form.attr('method'),
        dataType: 'json',
        success: function () {
            if (data.form_is_valid) {
                alert('Order Created');
            }
            else {
                $('#modal-stock .modal-content').html(data.form);
            }
        }
    });
    return false
})