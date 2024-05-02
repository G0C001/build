var price = document.querySelector(".item-price") 
var input_text = document.querySelector(".input-text") 
var total_price = document.querySelector(".total-price")
var currencyString = price.value

var item_price = parseFloat(currencyString.replace(/[^0-9.]/g, ''));

input_text.innerHTML = "1"
total_price.innerHTML = "Total : " + '₹'+ item_price.toFixed(2)



function incrementQuantity(){
    if (input_text.value < input_text.getAttribute("max")) {
        
        sum = 1
        x = parseInt(input_text.value) + sum
        sum = sum + 1
        input_text.value = x
        input_text.innerHTML = x    
        y = x * parseInt(item_price)
        total_price.innerHTML =  "Total : " + '₹'+ y.toFixed(2)
        console.log(x,y,total_price.innerHTML);
    }
}
function decrementQuantity(){
    if (input_text.value > input_text.getAttribute("min")) {
        sum = 1
        x = parseInt(input_text.value) - sum
        sum = sum + 1
        input_text.value = x
        input_text.innerHTML = x
        y = x * item_price
        total_price.innerHTML =  "Total : " + '₹'+ y.toFixed(2)
    }
}