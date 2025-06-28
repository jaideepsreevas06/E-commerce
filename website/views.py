from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify
from flask_login import login_required, current_user
from .models import Product, CartItem
from . import db

views = Blueprint('views', __name__)

# 🔥 Home - Product Listing
@views.route('/')
@login_required
def home():
    products = Product.query.all()
    return render_template("home.html", user=current_user, products=products)


# 🛒 Add to Cart
@views.route('/add-to-cart/<int:product_id>', methods=['POST'])
@login_required
def add_to_cart(product_id):
    quantity = int(request.form.get('quantity', 1))

    # Check if product exists
    product = Product.query.get_or_404(product_id)

    # Check if item already in cart
    cart_item = CartItem.query.filter_by(user_id=current_user.id, product_id=product_id).first()

    if cart_item:
        cart_item.quantity += quantity
    else:
        cart_item = CartItem()
        cart_item.user_id = current_user.id
        cart_item.product_id = product_id
        cart_item.quantity = quantity
        db.session.add(cart_item)

    db.session.commit()
    flash(f'Added {product.name} to cart!', category='success')
    return redirect(url_for('views.home'))


# 🛒 View Cart
@views.route('/cart')
@login_required
def cart():
    cart_items = CartItem.query.filter_by(user_id=current_user.id).all()
    
    # Calculate totals
    subtotal = sum(item.quantity * item.product.price for item in cart_items)
    total_items = sum(item.quantity for item in cart_items)
    
    return render_template('cart.html', 
                         user=current_user, 
                         cart_items=cart_items,
                         subtotal=subtotal,
                         total_items=total_items)


# 🔄 Update Cart Item Quantity
@views.route('/update-quantity/<int:cart_item_id>/<int:quantity>')
@login_required
def update_quantity(cart_item_id, quantity):
    cart_item = CartItem.query.get_or_404(cart_item_id)
    
    if cart_item.user_id != current_user.id:
        flash('Unauthorized action.', category='error')
        return redirect(url_for('views.cart'))
    
    if quantity <= 0:
        # Remove item if quantity is 0 or negative
        db.session.delete(cart_item)
        flash('Item removed from cart.', category='success')
    else:
        cart_item.quantity = quantity
        flash(f'Quantity updated to {quantity}.', category='success')
    
    db.session.commit()
    return redirect(url_for('views.cart'))


# ❌ Remove from Cart
@views.route('/remove-from-cart/<int:cart_item_id>')
@login_required
def remove_from_cart(cart_item_id):
    cart_item = CartItem.query.get_or_404(cart_item_id)

    if cart_item.user_id != current_user.id:
        flash('Unauthorized action.', category='error')
        return redirect(url_for('views.cart'))

    db.session.delete(cart_item)
    db.session.commit()
    flash('Item removed from cart.', category='success')
    return redirect(url_for('views.cart'))


# 🗑️ Clear Cart
@views.route('/clear-cart')
@login_required
def clear_cart():
    cart_items = CartItem.query.filter_by(user_id=current_user.id).all()
    
    for item in cart_items:
        db.session.delete(item)
    
    db.session.commit()
    flash('Cart cleared successfully.', category='success')
    return redirect(url_for('views.cart'))


# ✅ Checkout (Dummy)
@views.route('/checkout')
@login_required
def checkout():
    cart_items = CartItem.query.filter_by(user_id=current_user.id).all()

    if not cart_items:
        flash('Your cart is empty!', category='error')
        return redirect(url_for('views.home'))

    total = sum(item.quantity * item.product.price for item in cart_items)

    # In a real app, process payment here.

    # Clear cart after checkout
    for item in cart_items:
        db.session.delete(item)
    db.session.commit()

    flash(f'Checkout successful! Total: ₹{total}', category='success')
    return redirect(url_for('views.home'))
