import requests, csv
from bs4 import BeautifulSoup

url = "http://quotes.toscrape.com"
response = requests.get(url)
html_data = BeautifulSoup(response.text, "html.parser")
# quotes = html_data.find_all(class_="text")
quotes = html_data.find_all(class_="quote")
i = 1
# for quote in quotes:
#     print(f"{i}. {quote.get_text()}")
#     i += 1

with open("csv_pr/quotes.csv", "w") as file:
    headers_list = ["Quote", "Author", "Tags"]
    csv_writer = csv.DictWriter(file, fieldnames=headers_list)
    csv_writer.writeheader()
    for quote in quotes:
        tags = quote.find(class_='keywords')['content']
        csv_writer.writerow({
            "Quote": quote.find(class_='text').get_text(),
            "Author": quote.find(class_='author').get_text(),
            "Tags": tags
        })
        # print(f"{i}. {quote.find(class_='text').get_text()}\n\tAuthor: {quote.find(class_='author').get_text()}\tTags: {tags}")
        # i += 1




my_html = """
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />

    <link href="style.css" rel="stylesheet" />

    <title>Learning HTML & CSS</title>
  </head>
  <body>
    <h1>JavaScript is fun, but so is HTML & CSS!</h1>
    <p class="first">
      You can learn JavaScript without HTML and CSS, but for DOM manipulation
      it's useful to have some basic ideas of HTML & CSS. You can learn more
      about it
      <a href="https://www.udemy.com/user/jonasschmedtmann/">on Udemy</a>.
    </p>

    <h2 id="header">Another heading</h2>
    <p class="second">
      Just another paragraph
    </p>

    <img
      id="course-image"
      src="https://img-a.udemycdn.com/course/480x270/437398_46c3_9.jpg"
    />

    <form id="your-name">
      <h2>Your name here</h2>
      <p class="first">Please fill in this form :)</p>

      <input type="text" placeholder="Your name" />
      <button>OK!</button>
    </form>
    <p id="id_ex">Some text</p>
    <ol>
        <li class="first bold">One</li>
        <li class="second" id="second">Two</li>
        <li class="third">Three</li>
    </ol>
  </body>
</html>

"""

parsed_html = BeautifulSoup(my_html, "html.parser")
# print(parsed_html.body.h1)
# print(parsed_html.findAll("p"))
# print(parsed_html.find("img"))
# print(parsed_html.find(id="id_ex"))
# print(parsed_html.select("#id_ex"))
# print(parsed_html.select(".second"))
# print(parsed_html.find(class_="first"))
# print(parsed_html.select("li")[1])
# print(parsed_html.find_all("li"))

# second_li = parsed_html.select("li")[1]
# print(second_li.get_text())

# ol_list = parsed_html.select("li")
# for elem in ol_list:
#     print(elem.get_text())
# for elem in ol_list:
#     print(elem.get_name)
# for elem in ol_list:
#     print(elem.attrs)
# for elem in ol_list:
#     print(elem.attrs["class"])
#     print(elem["class"])

# body_content = parsed_html.body.contents
# updated_body_content = [elem for elem in body_content if elem != '\n']
# form = updated_body_content[5].contents
# updated_form_list = [elem for elem in form if elem != '\n']
# h2 = updated_form_list[0]
# print(h2.next_sibling.next_sibling)
# print(h2.parent)
# print(h2.parent.previous_sibling.previous_sibling)
# print(h2.parent.previous_sibling.find_previous_sibling().find_previous_sibling())
# print(h2.parent.previous_sibling.find_previous_sibling().find_previous_sibling(id="header"))
# print(h2.find_next_sibling().find_next_sibling().find_parent())
# print(h2.parent.previous_sibling.find_next_sibling())
# print(parsed_html.body.ol.findChildren())
# print(parsed_html.body.ol.findChildren()[2])
