import requests
from dotenv import load_dotenv
import os

load_dotenv()

git_token = os.getenv("GIT_TOKEN") # git_token is gonna be a Personal Access Token

url = "https://api.github.com/orgs/ORG_NAME_HERE/repos?per_page=100&page=1"
res=requests.get(url,headers={"Authorization": git_token})
repos=res.json()
#adds the following pages to repos
while 'next' in res.links.keys():
  res=requests.get(res.links['next']['url'],headers={"Authorization": git_token})
  repos.extend(res.json())
#print list of repos
for rep in repos:
  print(rep['name'])
