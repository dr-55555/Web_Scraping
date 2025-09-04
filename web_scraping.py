import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://github.com/trending"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

repos = soup.find_all("h2", class_="lh-condensed")
descriptions = soup.find_all("p", class_="col-9 color-fg-muted my-1 pr-4")
stars = soup.find_all("a", class_="Link--muted d-inline-block mr-3")
langs = soup.find_all("span", itemprop="programmingLanguage")

data = []
for i in range(len(repos)):
    repo_name = repos[i].text.strip().replace("\n", "").replace(" ", "")
    repo_link = "https://github.com" + repos[i].a["href"]
    repo_desc = descriptions[i].text.strip() if i < len(descriptions) else "No description"
    repo_stars = stars[i].text.strip() if i < len(stars) else "0"
    repo_lang = langs[i].text.strip() if i < len(langs) else "Not specified"

    data.append({
        "Repository": repo_name,
        "Description": repo_desc,
        "Language": repo_lang,
        "Stars": repo_stars,
        "Link": repo_link
    })

df = pd.DataFrame(data)
df.to_csv("/content/github_trending.csv", index=False, encoding="utf-8")

print("✅ Scraping completed! Data saved to github_trending.csv")
print(df.head())
