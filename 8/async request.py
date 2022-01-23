
import json
import time
import asyncio
import aiohttp

# Запрос на альбомы с фото
async def get_albums_with_photos(): 
    async with aiohttp.ClientSession() as session: 
        async with session.get("https://jsonplaceholder.typicode.com/albums") as resp:            
            all_albums = json.loads(await resp.read())
            tasks = []
            for album in all_albums:
                tasks.append(get_photos(album))
            await asyncio.gather(*tasks)
            return all_albums

async def get_photos(album):
    photos = await make_request_photos(album['id'])
    album.update({"Photos": photos})
async def make_request_photos(album_id): 
    async with aiohttp.ClientSession() as session: 
        async with session.get(f"https://jsonplaceholder.typicode.com/albums/{album_id}/photos") as resp:            
            all_photos = json.loads(await resp.read())
            return all_photos


# Запрос на посты с комментами
async def get_posts_with_comments(): 
    async with aiohttp.ClientSession() as session: 
        async with session.get("https://jsonplaceholder.typicode.com/posts") as resp:            
            all_posts = json.loads(await resp.read())
            tasks = []
            for post in all_posts:
                tasks.append(get_comments(post))
            await asyncio.gather(*tasks)
            return all_posts

async def get_comments(post):
    comments = await make_request_comments(post['id'])
    post.update({"Comments": comments})
async def make_request_comments(post_id): 
    async with aiohttp.ClientSession() as session: 
        async with session.get(f"https://jsonplaceholder.typicode.com/albums/{post_id}/photos") as resp:            
            all_comments = json.loads(await resp.read())
            return all_comments

# Запрос на пользователей с постами, альбомами, задачами
async def get_users_with_posts_albums_todos(): 
    async with aiohttp.ClientSession() as session: 
        async with session.get("https://jsonplaceholder.typicode.com/users") as resp:            
            all_users = json.loads(await resp.read())
            tasks = []
            for user_id in all_users:
                tasks.append(get_posts_albums_todos(user_id))
                tasks.append(get_posts_albums_todos(user_id))
                tasks.append(get_posts_albums_todos(user_id))

            await asyncio.gather(*tasks)
            return all_users

async def get_posts_albums_todos(user):
    posts = await make_request(user['id'])
    user.update({"POSTS": posts})
    albums = await make_request(user['id'])
    user.update({"ALBUMS": albums})
    todos = await make_request(user['id'])
    user.update({"TODOS": todos})


async def make_request(user_id): 
    async with aiohttp.ClientSession() as session: 
        async with session.get(f"https://jsonplaceholder.typicode.com/users/{user_id}/posts") as resp:            
            all_posts = json.loads(await resp.read())
        async with session.get(f"https://jsonplaceholder.typicode.com/users/{user_id}/albums") as resp:            
            all_albums = json.loads(await resp.read())
        async with session.get(f"https://jsonplaceholder.typicode.com/users/{user_id}/todos") as resp:            
            all_todos = json.loads(await resp.read())        
            return all_posts, all_albums, all_todos






start_time =time.time()    

# albums_with_photos = asyncio.run(get_albums_with_photos())
posts_with_comments = asyncio.run(get_posts_with_comments())
# users_with_posts_albums_todos = asyncio.run(get_users_with_posts_albums_todos())

# print(users_with_posts_albums_todos)
print(posts_with_comments)
# print(albums_with_photos)

print(time.time()-start_time)
