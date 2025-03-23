let cart = [];

function addToCart(item, price) {
    cart.push({ item, price });
    updateCart();
}

function updateCart() {
    let cartItems = document.getElementById("cart-items");
    let totalPrice = 0;
    cartItems.innerHTML = "";
    
    cart.forEach(product => {
        let li = document.createElement("li");
        li.textContent = `${product.item} - $${product.price.toFixed(2)}`;
        cartItems.appendChild(li);
        totalPrice += product.price;
    });

    document.getElementById("cart-total").textContent = `Total: $${totalPrice.toFixed(2)}`;
}

function clearCart() {
    cart = [];
    updateCart();
}
