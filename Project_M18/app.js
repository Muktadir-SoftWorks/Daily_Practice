document.addEventListener("DOMContentLoaded", function() {
    const products = [
        { id: 1, name: "Google Pixel 6", description: "Comfortable cotton t-shirt", price: 19.99, image: "https://www.digitaltrends.com/wp-content/uploads/2022/11/Pixel-7-Pro-and-Pixel-6-Pro-Back.jpg?fit=3000%2C2000&p=1.jpg" },
        { id: 2, name: "Google Pixel 7", description: "Latest music album", price: 9.99, image: "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTnkc1DsM8zHCUfUXl1DWMp1wn1qqt_KVRzzG_tcN4IfzipLobPci65XPI7KI8H3nKvmoo&usqp=CAU.jpg" },
        { id: 3, name: "Google Pixel 6", description: "Comfortable cotton t-shirt", price: 19.99, image: "https://www.digitaltrends.com/wp-content/uploads/2022/11/Pixel-7-Pro-and-Pixel-6-Pro-Back.jpg?fit=3000%2C2000&p=1.jpg" },
        { id: 4, name: "Google Pixel 7", description: "Latest music album", price: 9.99, image: "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTnkc1DsM8zHCUfUXl1DWMp1wn1qqt_KVRzzG_tcN4IfzipLobPci65XPI7KI8H3nKvmoo&usqp=CAU.jpg" },
        { id: 5, name: "Google Pixel 6", description: "Comfortable cotton t-shirt", price: 19.99, image: "https://www.digitaltrends.com/wp-content/uploads/2022/11/Pixel-7-Pro-and-Pixel-6-Pro-Back.jpg?fit=3000%2C2000&p=1.jpg" },
        { id: 6, name: "Google Pixel 7", description: "Latest music album", price: 9.99, image: "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTnkc1DsM8zHCUfUXl1DWMp1wn1qqt_KVRzzG_tcN4IfzipLobPci65XPI7KI8H3nKvmoo&usqp=CAU.jpg" }
    ];
    const cart = [];

    const productList = document.getElementById('product-list');
    const cartItems = document.getElementById('cart-items');
    const totalPrice = document.getElementById('total-price');

    function updateCart() {
        cartItems.innerHTML = '';
        let total = 0;
        cart.forEach(item => {
            total += item.price * item.quantity;
            cartItems.innerHTML += `<li class="cart-item">
                ${item.name} $${item.price} x ${item.quantity}
                <button onclick="removeFromCart(${item.id})">REMOVE</button>
            </li>`;
        });
        totalPrice.textContent = total.toFixed(2);
    }

    products.forEach(product => {
        const html = `
            <div class="col-md-4 product-card">
                <div class="card">
                    <img src="${product.image}" class="card-img-top product-image" alt="${product.name}">
                    <div class="card-body">
                        <h5 class="card-title">${product.name}</h5>
                        <p class="card-text">${product.description}</p>
                        <p class="card-text">$${product.price}</p>
                        <button onclick="addToCart(${product.id})" class="btn btn-primary">Add to Cart</button>
                    </div>
                </div>
            </div>
        `;
        productList.innerHTML += html;
    });

    window.addToCart = function(productId) {
        const product = products.find(p => p.id === productId);
        const cartItem = cart.find(item => item.id === productId);
        if (cartItem) {
            cartItem.quantity++;
        } else {
            cart.push({ ...product, quantity: 1 });
        }
        updateCart();
    };

    window.removeFromCart = function(productId) {
        const index = cart.findIndex(item => item.id === productId);
        if (index > -1) {
            cart.splice(index, 1);
        }
        updateCart();
    };
});
