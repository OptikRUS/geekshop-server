window.onload = function () {
    $('.basket_list').on('click', 'input[type=number]', function () {
        let target = event.target;
        let basketID = target.name; // basket id
        let basketQuantity = target.value; // basket quantity
        $.ajax({
            url: '/baskets/basket-edit/' + basketID + '/' + basketQuantity + '/',
            success: function (data) {
                $('.basket_list').html(data.result);
            }
        })
    })
}