import feedparser
import pathlib

root = pathlib.Path(__file__).parent.resolve()

def fetch_blog_entries():
    entries = feedparser.parse("https://caixiangyue.github.io/rss.xml")["entries"]
    return [
        {
            "title": entry["title"],
            "url": entry["link"].split("#")[0],
        }
        for entry in entries
    ]

if __name__ == "__main__":
    readme = root / "README.md"

    readme_content = """
<img src='https://qpluspicture.oss-cn-beijing.aliyuncs.com/6LjjQA/Hi.gif' alt='Hi' width="24"/> hi

![](https://github-readme-stats.vercel.app/api?username=caixiangyue)

#### 🤹‍♀️ <a href="https://cxy.fun/" target="_blank">Recent Blog</a>

"""

    entries = fetch_blog_entries()[:5]
    entries_md = "\n".join(
        ["* <a href='{url}' target='_blank'>{title}</a>".format(**entry) for entry in entries]
    )

    readme.open('w').writelines(readme_content+entries_md)
