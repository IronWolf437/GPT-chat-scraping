from playwright.sync_api import sync_playwright

link = input("Enter the ChatGPT share link: ")

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto(link, wait_until="networkidle")

    page.wait_for_timeout(5000)

    page.wait_for_selector(f"div.whitespace-pre-wrap")
    my_messages = page.query_selector_all(f"div.whitespace-pre-wrap")
    GPT_messages = page.locator("div.markdown p")
    count = GPT_messages.count()

    with open ("scraped_page.txt", "a", encoding="utf-8") as file:
        for m,i in zip(my_messages,range(count)):
            file.write(f'Me: {m.inner_text()}\n')
            file.write(f'GPT: {GPT_messages.nth(i).inner_text()}\n')
            file.write('-'*40+'\n')

    browser.close()
