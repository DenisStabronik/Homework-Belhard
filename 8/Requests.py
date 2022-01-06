import asyncio
import time
import aiohttp 
import json


async def make_request(path):                                            # Запрос на интернет ресурс
    async with aiohttp.ClientSession() as sess:
        async with sess.request('GET', f'https://jsonplaceholder.typicode.com/{path}/') as req:
            return await req.text()

# async def get_data_sync():                                # Синхронная выгрузка
#     users = await make_request('users')
#     posts = await make_request('posts')
#     albums = await make_request('albums')
#     todos = await make_request('todos')
#     comments = await make_request('comments')
#     photos = await make_request('photos')
    
#     json_data = [json.loads(item) for item in [users, posts, albums, todos, comments, photos]]
#     users, posts, albums, todos, comments, photos = json_data
#     return users, posts, albums, todos, comments, photos

# start = time.time()
# users, posts, albums, todos, comments, photos = asyncio.run(get_data_sync())
# print(time.time() - start)

async def get_data_not_sync():                        # Асинхронная выгрузка
    data = await asyncio.gather(
        make_request("users"),
        make_request("posts"),
        make_request("albums"),
        make_request("todos"),
        make_request("comments"),
        make_request("photos")
    )
    json_data = [json.loads(item) for item in data]
    users, posts, albums, todos, comments, photos = json_data
    return users, posts, albums, todos, comments, photos

start = time.time()
users, posts, albums, todos, comments, photos = asyncio.run(get_data_not_sync())
print(time.time() - start)    
           
def combine_users(users: dict, albums: dict, todos: dict, posts: dict):      # Группируем данные пользователей,альбомов,задач,сообщений в массив словарей
    all_users = []
    for user in users:
        user.update({'СПИСОК АЛЬБОМОВ': []})                                 
        user.update({'СПИСОК ЗАДАЧ': []})
        user.update({'СПИСОК СООБЩЕНИЙ': []})
        for album in albums:
            if album.get('userId') == user.get('id'):
                user['СПИСОК АЛЬБОМОВ'].append(album)
        for todo in todos:
            if todo.get('userId') == user.get('id'):
                user['СПИСОК ЗАДАЧ'].append(todo)
        for post in posts:
            if post.get('userId') == user.get('id'):
                user['СПИСОК СООБЩЕНИЙ'].append(post)
        all_users.append(user)
    return all_users  



def combine_posts_comments(posts: dict, comments: dict):           # Группируем данные постов,коментариев в массив словарей
    all_posts = []
    for post in posts:
        post.update({'СПИСОК КОММЕНТАРИЕВ': []})
        for comment in comments:
            if comment.get('postId') == post.get('id'):
                post['СПИСОК КОММЕНТАРИЕВ'].append(comment)
        all_posts.append(post)
    return all_posts

def combine_albums_photos(albums: dict, photos: dict):            # Группируем данные альбомов,фотографий в массив словарей
    all_albums = []
    for album in albums:
        album.update({'СПИСОК ФОТОГРАФИЙ': []})
        for photo in photos:
            if photo.get('albumId') == album.get('id'):
                album['СПИСОК ФОТОГРАФИЙ'].append(photo)
        all_albums.append(album)
    return all_albums
list_users = combine_users(users, albums, todos, posts)               # массив для всех пользователей с альбомами постами и списками задач
albums_with_list_photos = combine_albums_photos(albums, photos)       # массив для всех альбомов с фотографиями
posts_with_list_comments = combine_posts_comments(posts, comments)    # массив для всех постов с коментариями

# print(list_users)
# print(posts_with_list_comments)
# print(albums_with_list_photos)




