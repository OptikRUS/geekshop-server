window.onload = function () {
    $('.product_list').on('click', 'input[type=button]', function () {
        let productID = event.target.id;
        $.ajax({
            url: '/baskets/basket-add/' + productID + '/',
            success: function (data) {
                $('.product_list').html(data.result);
            }
        })
    })
}