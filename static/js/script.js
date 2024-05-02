document.querySelector(".loading-page").style.display = "flex"

document.querySelector("header").style.display = 'none'

document.querySelector(".container-body").style.display = 'none'

document.querySelector(".fot-con").style.display = 'none'


setTimeout(() => {
    document.querySelector(".loading-page").style.display = "none"

    document.querySelector("header").style.display = ''

    document.querySelector(".container-body").style.display = ''

    document.querySelector(".fot-con").style.display = ''
}, 0);

var view_wishlist = document.querySelector(".top-wish-list")

var shop_icon = document.querySelector(".fa-cart-shopping")

var wishlistItems = document.querySelectorAll('.item-wish');

var cart_count = document.querySelector(".cart-count")

function cart_icon_colour() {
    setTimeout(() => {
        view_wishlist.style.color = ''
    }, 1000);
}
wishlistItems.forEach(function(item) {
    let clickCount = 0;
    count = 0
    item.addEventListener('click', function() {
        clickCount++;
        
        if (clickCount % 2 === 1) {
            item.style.color = 'red';
            cart_count.innerHTML = count + 1
            count = count + 1
            view_wishlist.style.color = 'red'
            cart_icon_colour()
        } else {
            item.style.color = '';
            cart_count.innerHTML = count - 1
            count = count - 1
        }
    });
});



