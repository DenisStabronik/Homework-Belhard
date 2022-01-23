import requests
import time
import json


# Запрос на пользователей с постами, альбомами, задачами
def get_users_data():
    response_users = requests.get("https://jsonplaceholder.typicode.com/users")
    all_users = json.loads(response_users.text)
    for user in all_users:
        albums, posts, todos = users_posts_albums_todos(user['id']) 
        user.update({"albums": albums})
        user.update({"posts": posts})
        user.update({"todos": todos})
    return all_users
def users_posts_albums_todos(users_id):   
    response_posts = requests.get(f"https://jsonplaceholder.typicode.com/users/{users_id}/posts")   
    all_posts = json.loads(response_posts.text)
    response_albums = requests.get(f"https://jsonplaceholder.typicode.com/users/{users_id}/albums")   
    all_albums = json.loads(response_albums.text)
    response_todos = requests.get(f"https://jsonplaceholder.typicode.com/users/{users_id}/todos")   
    all_todos = json.loads(response_todos.text) 
    return all_albums, all_posts, all_todos


# Запрос на посты с комментами
def get_posts_data():
    response_posts = requests.get("https://jsonplaceholder.typicode.com/posts")
    all_posts = json.loads(response_posts.text)
    for post in all_posts:
        comments = posts_comments(post['id'])   
        post.update({"Comments": comments})       
    return all_posts
def posts_comments(post_id):   
    response_comments = requests.get(f"https://jsonplaceholder.typicode.com/posts/{post_id}/comments")   
    all_comments = json.loads(response_comments.text)   
    return all_comments

# Запрос на альбомы с фото
def get_albums_data():
    response_albums = requests.get("https://jsonplaceholder.typicode.com/albums")
    all_albums = json.loads(response_albums.text)
    for album in all_albums:
        photos = albums_photos(album['id'])   
        album.update({"Photos": photos})       
    return all_albums
def albums_photos(album_id):   
    response_photos = requests.get(f"https://jsonplaceholder.typicode.com/albums/{album_id}/photos")   
    all_photos = json.loads(response_photos.text)   
    return all_photos


start_time =time.time()
user_list = get_users_data()
post_with_comments = get_posts_data()
album_with_photos = get_albums_data()

# print(user_list)
# print(post_with_comments)
# print(album_with_photos)
print(time.time()-start_time)
