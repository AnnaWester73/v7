import re
from playwright.sync_api import Page, expect

URL = "https://lejonmanen.github.io/agile-helper/"

# Test User story 1

def test_user_story_1_sprint_planning(page: Page):
    page.goto(URL)

    first_button = page.get_by_test_id("btn-first")
    first_button.click()
    begin_button = (page.get_by_role("button", name="Börja sprinten med Sprint"))
    begin_button.click()
    plan_button = (page.get_by_role("heading", name="Sprint planning"))
    plan_button.click()

    expect(page.get_by_role("heading", name="Sprint planning")).to_be_visible()

# Test User story 2

def test_user_story_2_byta_sprak(page: Page):
    page.goto(URL)

    page.get_by_test_id("language-en").click()
    expect(page.get_by_role("button", name="First")).to_be_visible()

    page.get_by_test_id("language-sv").click()
    expect(page.get_by_role("button", name="Första")).to_be_visible()