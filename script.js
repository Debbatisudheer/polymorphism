$(document).ready(function() {
    $(".draggable").draggable({
        revert: "invalid",
        helper: "clone"
    });

    $(".droppable").droppable({
        drop: function(event, ui) {
            let subclass = $(this).attr('id'); // Get the ID of the subclass container
            let price = parseFloat($(ui.draggable).data('price'));
            let quantity = 1; // Assuming quantity is always 1 for simplicity
            let totalPrice = calculateTotalPrice(price, quantity, subclass);
            $(this).append(`<p>Total Price: $${totalPrice.toFixed(2)}</p>`);
        }
    });

    // Set default electronic price and discount
    $('#electronics-container').data('price', 100);
    $('#electronics-container').data('discount', 10); // Setting default discount

    // Set default clothing price and discount
    $('#clothing-container').data('price', 800);
    $('#clothing-container').data('discount', 200); // Setting default discount

    // Set default book price and gift coupon amount
    $('#book-container').data('price', 299);
    $('#book-container').data('coupon', 10); // Setting default gift coupon amount
});

function calculateTotalPrice(basePrice, quantity, subclass) {
    let totalPrice = basePrice * quantity;
    // Additional pricing logic based on subclass
    if (subclass === 'electronics-container') {
        let electronicPrice = parseFloat($('#electronics-container').data('price')) || 0;
        let discount = parseFloat($('#electronics-container').data('discount')) || 0; // Retrieve default discount
        totalPrice = (electronicPrice - discount) * quantity;
    } else if (subclass === 'clothing-container') {
        let clothingPrice = parseFloat($('#clothing-container').data('price')) || 0;
        let discount = parseFloat($('#clothing-container').data('discount')) || 0; // Retrieve default discount
        totalPrice = (clothingPrice - discount) * quantity;
    } else if (subclass === 'book-container') {
        let bookPrice = parseFloat($('#book-container').data('price')) || 0;
        let coupon = parseFloat($('#book-container').data('coupon')) || 0; // Retrieve default coupon amount
        totalPrice = (bookPrice - coupon) * quantity;
    }
    // Add additional conditions for other subclasses if needed
    return totalPrice;
}