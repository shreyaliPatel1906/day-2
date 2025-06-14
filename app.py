from bs4 import BeautifulSoup
def load_html(file_path):
    with open(file_path, 'r',encoding="utf-8") as f:
        content = f.read()
        return content

def extract_posts(soup):
    posts = []
    post_elements = soup.find_all(name='div', class_='post')
    # print(post_elements)
    for post in post_elements:
        username = post.find(name='h2', class_='username').text
        content = post.find(name='p', class_='content').text
        timestamp = post.find(name='span', class_='timestamp').text
        # print(username, content ,timestamp )

        posts.append({'username': username, 'content': content, 'timestamp': timestamp})
    return posts
html_content = load_html("social_media.html")
soup = BeautifulSoup(html_content,features="html.parser")

posts = extract_posts(soup)
print(posts)

for post in posts:
    print(f"Username: {post['username']}")
    print(f"content: {post['content']}")
    print(f"timestamp: {post['timestamp']}")
