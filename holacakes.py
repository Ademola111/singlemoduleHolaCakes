from flask import Flask, render_template, redirect, request, redirect, url_for,flash
app=Flask(__name__)

"""Home page view"""
@app.route('/')
@app.route('/home/')
def home():
    return render_template('index.html')

"""about us page view"""
@app.route('/about/us/')
def about():
    return render_template('about.html')

"""signup view page"""
@app.route('/signup/')
def signup():
    # query = (f"INSERT INTO user SET")
    return render_template('signup.html')

"""login page view"""
@app.route('/login/')
def login():
    # query = (f"SELECT * user WHERE username='{username}' and password='{password}'")
    return render_template('login.html')

"""profile view page"""
@app.route('/profile/')
def profile():
    return render_template('profile.html',)

"""custom view page"""
@app.route('/custom/')
def custom():
    return render_template('custom.html')

"""birthday view page"""
@app.route('/product/birthday')
def birthday():
    return render_template('birthday.html')

"""wedding view page"""
@app.route('/product/wedding')
def wedding():
    return render_template('wedding.html')

"""cupcake view page"""
@app.route('/product/cupcake')
def cupcake():
    return render_template('cupcake.html')

"""product detail view page"""
@app.route('/product/')
def product():
    return render_template('product.html')

"""product detail view page"""
@app.route('/cart/')
def cart():
    return render_template('cart.html')

"""admin login"""
@app.route('/admin/')
def admin_login():
    return render_template('admin_login.html')

"""admin login submit"""
@app.route('/admin/submit', methods=['POST','GET'])
def admin_login_submit():
    data=request.get.value()
    return redirect(url_for('adminDashboard'), data=data)

""" Admin Dashboard submit"""
@app.route('/admin/dashboard')
def admin_dashboard():
    return render_template('admin_dashboard.html')

""" Admin signup """
@app.route('/admin/signup')
def admin_signup():
    return render_template('admin_signup.html')

""" Admin signup submit"""
@app.route('/admin/signup')
def admin_signup_submit():
    return render_template('admin_signup.html')

"""admin products"""
@app.route('/admin/products')
def admin_product():
    return render_template('list_product.html')

"""admin products categories"""
@app.route('/admin/products/categories')
def admin_categories():
    return render_template('admin_categories.html')

"""admin images"""
@app.route('/admin/products/images')
def admin_images():
    return render_template('admin_images.html')

"""admin products order"""
@app.route('/admin/products/order')
def admin_orderproduct():
    return render_template('admin_orderproduct.html')

"""admin products order detail"""
@app.route('/admin/products/order/detail')
def admin_orderdetail():
    return render_template('admin_orderdetail.html')

"""admin products order detail"""
@app.route('/admin/products/delivery')
def admin_delivery():
    return render_template('admin_delivery.html')

"""admin products order detail"""
@app.route('/admin/products/payment')
def admin_payment():
    return render_template('admin_payment.html')

"""admin products reviews"""
@app.route('/admin/products/reviews')
def admin_reviews():
    return render_template('admin_reviews.html')

"""admin products reviews"""
@app.route('/admin/user')
def admin_user():
    return render_template('admin_user.html')


















if __name__ == '__main__':
    app.run(debug=True)

