from sqlalchemy import desc
from app import app
from flask import render_template, redirect, url_for, flash, request
from flask_login import login_user, login_required, logout_user, current_user
from app.forms import CommentsForm, GameForm, SignUpForm, PostForm, LoginForm
from app.models import Post, User, Game
#import xmltodict
import requests
import xml.etree.ElementTree as ET

@app.route("/")
def index():
    games = Game.query.all()
    return render_template('list.html', games=games)

@app.route("/list")
def list():
    games = Game.query.all()
    return render_template('list.html', games=games)

@app.route("/listalpha")
def listalpha():
    #Sort games alphabetically
    games= Game.query.order_by(Game.title).all()
    return render_template('listalpha.html', games=games)


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignUpForm()
    if form.validate_on_submit():
        # Get the data from the form fields
        email = form.email.data
        username = form.username.data
        password = form.password.data
        # Query the User table for any users with username/email from form
        user_check = User.query.filter((User.email == email)|(User.username == username)).all()
        if user_check:
            flash('A user with that username and/or email already exists. Please try again.', 'danger')
            return redirect(url_for('signup'))

        # Add the user to the database
        new_user = User(email=email, username=username, password=password)

        # Show message of success
        flash(f'{new_user.username} has successfully signed up!', 'success')
        # redirect back to the homepage
        return redirect(url_for('list'))

    return render_template('signup.html', form=form)


@app.route('/create-post', methods=["GET", "POST"])
@login_required
def create_post():
    form = PostForm()
    if form.validate_on_submit():
        # Get data from the form
        post_title = form.title.data
        user_id = current_user.id
        #Get data from BGG API pull
        post_body = form.body.data
        # Add new post to database with form info
        new_post = Post(title=post_title, body=post_body, user_id=user_id)
        # Flash a success message to the user
        flash(f'"{new_post.title}" by {new_post.author.username} has been created', 'success')
        # Return to the home page
        return redirect(url_for('index'))

    return render_template('create_post.html', form=form)

@app.route('/create-game', methods=["GET", "POST"])
@login_required
def create_game():
    form = GameForm()
    if form.validate_on_submit():
        # Get data from the form
        title = form.title.data
        user_id = current_user.id
        comments = "Edit this to display your thoughts about the game."
        title_check = Game.query.filter((Game.title == title)&(Game.user_id == user_id)).all()
        
        if title_check:
            flash('You have already entered that game. Enter another,', 'danger')
            return redirect(url_for('list'))
        #Search for the game, find game ID
        r = requests.get(f'https://boardgamegeek.com/xmlapi2/search?query={title}&exact=1')
        root = ET.fromstring(r.content)
        attrib = root[0].attrib
        BGGid = (attrib['id'])
        print(BGGid)

        r2 = requests.get(f'https://boardgamegeek.com/xmlapi2/thing?id={BGGid}')

        root2 = ET.fromstring(r2.content)
        
        #Getting the description
        for child in root2.iter('*'):
            if child.tag == 'description':
                body = child.text
                #print(body)
            if child.tag == 'thumbnail':
                picture = child.text

        # Add new game to database with form info
        new_game = Game(title=title, body=body, comments=comments, picture=picture, user_id=user_id)
        # Flash a success message to the user
        flash(f'"{new_game.title}" has been created', 'success')
        # Return to the home page
        return redirect(url_for('list'))

    return render_template('create_game.html', form=form)


@app.route('/named', methods=['GET', 'POST'])
def name_entry():
    form = GameForm()
    if form.validate_on_submit():
        # Get the data from the form fields
        title = form.title.data

        # Add the game to the database
        new_game = Game(title = title)

        # Show message of success
        flash(f'{new_game.title} successfully processed', 'success')
        
        print(new_game)
        return redirect(url_for('linking'), title)

    return render_template('named.html', form=form)

@app.route('/linking', methods=["GET", "POST"])
def linking(title):
    r = requests.get(f'https://boardgamegeek.com/xmlapi2/search?query={title}&exact=1')
    root = ET.fromstring(r.content)
    for child in root:
        print(child.tag, child.attrib)
    info = root[0][4].text
        
        # Add new post to database with form info

    return render_template('linking.html', title = title)


@app.route('/login', methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # Get the data from form
        username = form.username.data
        password = form.password.data
        # Query our user table for a user with the username from the form
        user = User.query.filter_by(username=username).first()
        # If the user exists and the password for that user is correct
        if user is not None and user.check_password(password):
            # log the user in
            login_user(user)
            # Flash a success message
            flash(f"Welcome back, {user.username}!", "primary")
            # Redirect to the home page
            return redirect(url_for('list'))
        
        # If user is None or password incorrect, flash message and redirect to login
        flash('Incorrect username and/or password. Please try again.', 'danger')
        return redirect(url_for('login'))

    return render_template('login.html', form=form)


@app.route('/logout')
def logout():
    logout_user()
    flash('You have logged out of the blog', 'secondary')
    return redirect(url_for('list'))


@app.route('/posts/<post_id>')
def view_single_post(post_id):
    post = Post.query.get_or_404(post_id) # SELECT * FROM post WHERE id = post_id  --(post_id comes from the URL)
    return render_template('single_post.html', post=post)

@app.route('/theory')
def theory():
    return render_template('theory.html')


@app.route('/games/<game_id>')
def view_single_game(game_id):
    game = Game.query.get_or_404(game_id) # SELECT * FROM post WHERE id = post_id  --(post_id comes from the URL)
    return render_template('single_game.html', game=game)


@app.route('/edit-posts/<post_id>', methods=["GET", "POST"])
@login_required
def edit_single_post(post_id):
    post_to_edit = Post.query.get_or_404(post_id)
    if current_user != post_to_edit.author:
        flash("You do not have permission to edit that post", "danger")
        return redirect(url_for('index'))
    form = PostForm()
    if form.validate_on_submit():
        # Get form data
        new_title = form.title.data
        new_body = form.body.data
        # update the post to edit with the form data
        post_to_edit.update(title=new_title, body=new_body)

        flash(f'{post_to_edit.title} has been updated', 'primary')
        return redirect(url_for('view_single_post', post_id=post_to_edit.id))

    return render_template('edit_post.html', post=post_to_edit, form=form)

@app.route('/edit-games/<game_id>', methods=["GET", "POST"])
@login_required
def edit_single_game(game_id):
    game_to_edit = Game.query.get_or_404(game_id)
    if current_user != game_to_edit.author:
        flash("You do not have permission to edit that game", "danger")
        return redirect(url_for('list'))
    form = CommentsForm()
    if form.validate_on_submit():
        # Get form data
        new_comments = form.comments.data
        # update the post to edit with the form data
        game_to_edit.update(comments = new_comments)

        flash(f'{game_to_edit.title} has been updated', 'primary')
        return redirect(url_for('view_single_game', game_id=game_to_edit.id))

    return render_template('edit_game.html', game=game_to_edit, form=form)


@app.route('/delete-posts/<post_id>')
@login_required
def delete_single_post(post_id):
    post_to_delete = Post.query.get_or_404(post_id)
    if current_user != post_to_delete.author:
        flash("You do not have permission to delete that post", "danger")
        return redirect(url_for('index'))
    post_to_delete.delete()
    flash(f'{post_to_delete.title} has been deleted', 'info')
    return redirect(url_for('index'))

@app.route('/delete-games/<game_id>')
@login_required
def delete_single_game(game_id):
    game_to_delete = Game.query.get_or_404(game_id)
    if current_user != game_to_delete.author:
        flash("You do not have permission to delete that post", "danger")
        return redirect(url_for('list'))
    game_to_delete.delete()
    flash(f'{game_to_delete.title} has been deleted', 'info')
    return redirect(url_for('list'))

@app.route("/test")
def zugbu():
    return render_template('test.html', r =requests.get('https://boardgamegeek.com/xmlapi2/thing?id=68264'))

# @app.route("/named", methods = ['GET', 'POST'])
# def name_entry():
#     form = GameForm()
#     if form.validate_on_submit():
#         title = form.title.data
    
# Add a check if game already added to list.
#               




@app.route("/testapp", methods = ['GET'], strict_slashes=False)
def parseRequest():
    r = requests.get('https://boardgamegeek.com/xmlapi2/thing?id=68264')
    #print(r.content)
    #print (content)
    return r.content


@app.route("/picture", methods = ['POST', 'GET'])
def picture():
    r = requests.get('https://boardgamegeek.com/xmlapi2/thing?id=68264')
    #print(r.content)
    #print (content)
    root =ET.fromstring(r.content)
    for child in root:
        print(child.tag, child.attrib)

    return root[0][4].text