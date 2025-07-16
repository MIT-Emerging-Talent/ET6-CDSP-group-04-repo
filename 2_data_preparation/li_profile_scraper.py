import asyncio
import pandas as pd
from playwright.async_api import async_playwright
import re
import os
import random
import argparse
from datetime import datetime
import time

SEARCH_URL = ""
NUM_PAGES = 8
SAVE_DIR = "linkedin_html_profiles"
MAX_PROFILES = 50
os.makedirs(SAVE_DIR, exist_ok=True)


def clean_filename(name):
    return re.sub(r'[\\/*?:"<>|]', "", name.replace(" ", "_"))


def apply_time_of_day_pacing():
    hour = datetime.now().hour
    if 8 <= hour < 10 or 12 <= hour < 14 or 18 <= hour < 21:
        delay = random.uniform(1, 5)
        print(f"🌅 Time-of-day pacing delay: {delay:.1f} sec")
        time.sleep(delay)


async def simulate_mouse_hover(profile):
    hover_targets = [
        "h1",
        "section.pv-top-card",
        "div.pvs-entity",
        "div.inline-show-more-text",
        "span.visually-hidden",
    ]

    start_time = time.time()
    random.shuffle(hover_targets)
    hovered = 0

    for selector in hover_targets:
        if time.time() - start_time > 4:
            print("⏱️ Hover timeout reached")
            break
        try:
            await profile.hover(selector, timeout=1500)
            await asyncio.sleep(random.uniform(0.3, 0.9))
            hovered += 1
            if hovered >= random.randint(2, 3):
                break
        except Exception:
            continue


async def simulate_human_scroll(profile):
    scroll_pattern = random.choice([1, 2, 3])
    print(f"🌀 Scroll mode: {scroll_pattern}")

    if scroll_pattern == 1:
        for _ in range(random.randint(3, 4)):
            await profile.mouse.wheel(0, random.randint(400, 1000))
            await asyncio.sleep(random.uniform(0.5, 1.0))
        await profile.mouse.wheel(0, -2000)
        await asyncio.sleep(random.uniform(0.5, 1.0))
        await profile.evaluate("window.scrollTo(0, document.body.scrollHeight/2)")

    elif scroll_pattern == 2:
        for _ in range(random.randint(4, 6)):
            pos = random.randint(500, 3500)
            await profile.evaluate(f"window.scrollTo(0, {pos})")
            await asyncio.sleep(random.uniform(0.8, 1.5))
        await profile.evaluate("window.scrollTo(0, 0)")

    elif scroll_pattern == 3:
        await profile.evaluate("window.scrollTo(0, document.body.scrollHeight)")
        await asyncio.sleep(random.uniform(1.5, 3))
        await profile.mouse.wheel(0, -2500)
        await asyncio.sleep(random.uniform(1, 2))


async def simulate_clicks(profile):
    try:
        if random.random() < 0.5:
            buttons = profile.locator(
                "button:has-text('See more'), a[href*='company'], a[href*='school']"
            )
            count = await buttons.count()
            if count > 0:
                for _ in range(random.randint(1, min(3, count))):
                    index = random.randint(0, count - 1)
                    btn = buttons.nth(index)
                    if await btn.is_visible():
                        await btn.scroll_into_view_if_needed()
                        await asyncio.sleep(random.uniform(0.5, 1.0))
                        await btn.click()
                        print("🖱️ Clicked internal link")
                        await asyncio.sleep(random.uniform(1.5, 3))
    except Exception as e:
        print(f"⚠️ Error clicking link: {e}")


async def extract_profiles_from_page(
    page, context, visited_links, all_profiles, safe_mode
):
    await page.wait_for_selector("a[href*='/in/']", timeout=20000)
    await page.mouse.wheel(0, 20000)
    await asyncio.sleep(random.randint(4, 8))

    profile_urls = set()
    primary_links = await page.locator("a[href*='/in/']").all()
    for el in primary_links:
        href = await el.get_attribute("href")
        if href and "/in/" in href:
            profile_urls.add(href)

    print(f"🔗 Found {len(profile_urls)} profile links")

    for url in profile_urls:
        if len(all_profiles) >= MAX_PROFILES:
            print("🚦 Max profile limit reached. Stopping scrape.")
            return
        if url in visited_links:
            continue
        visited_links.add(url)

        print(f"➡️ Visiting profile: {url}")
        profile = await context.new_page()
        try:
            await profile.goto(url, timeout=60000)
            await asyncio.sleep(random.uniform(2.5, 5.0))

            await simulate_mouse_hover(profile)

            name_el = await profile.locator("h1").first.text_content()
            name = name_el.strip() if name_el else "unknown"
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            safe_name = clean_filename(name or "unknown")[:30]
            file_name = f"{safe_name}_{timestamp}.html"
            file_path = os.path.join(SAVE_DIR, file_name)

            html_content = await profile.content()
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(html_content)

            print(f"✅ Saved: {file_name}")
            all_profiles.append({"Name": name, "Link": url, "Saved_HTML": file_name})

            await simulate_human_scroll(profile)

            if random.random() < 0.6:
                await simulate_clicks(profile)

        except Exception as e:
            print(f"❌ Error scraping {url}: {e}")
        finally:
            await profile.close()

        apply_time_of_day_pacing()
        await asyncio.sleep(random.randint(3, 7))


async def run(safe_mode):
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context(viewport={"width": 1920, "height": 1080})
        page = await context.new_page()

        await page.goto("https://www.linkedin.com/login")
        print("🔐 Please log in manually...")
        while True:
            if "feed" in page.url or "search/results" in page.url:
                break
            await asyncio.sleep(1)
        input("✅ Logged in. Press ENTER to proceed to search results...")

        await page.goto(SEARCH_URL, wait_until="networkidle")
        visited_links = set()
        all_profiles = []

        for page_num in range(NUM_PAGES):
            print(f"\n🌍 Scraping search result page {page_num + 1}...")
            await extract_profiles_from_page(
                page, context, visited_links, all_profiles, safe_mode
            )

            if len(all_profiles) >= MAX_PROFILES:
                break

            try:
                next_btn = page.locator(
                    "button.artdeco-pagination__button--next[aria-label='Next']"
                )
                if await next_btn.is_visible() and await next_btn.is_enabled():
                    old_url = page.url
                    await next_btn.click()
                    for _ in range(20):
                        if page.url != old_url:
                            break
                        await asyncio.sleep(1)
                    else:
                        print("❌ Pagination failed: URL did not change.")
                        break
                    await asyncio.sleep(random.randint(3, 6))
                    await page.mouse.wheel(0, 10000)
                    await asyncio.sleep(random.randint(3, 5))
                else:
                    print("⚠️ Reached last page.")
                    break
            except Exception as e:
                print(f"⚠️ Pagination error: {e}")
                break

        await browser.close()

        if all_profiles:
            df = pd.DataFrame(all_profiles)
            df.to_csv("linkedin_profile_index.csv", index=False)
            print("\n📦 All profile HTMLs saved. Index: linkedin_profile_index.csv")
        else:
            print("⚠️ No profiles saved.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--safe", action="store_true", help="Run in safe mode with slower scraping"
    )
    args = parser.parse_args()
    asyncio.run(run(safe_mode=args.safe))
