# file with help functions that can be utilized across all the tests


def take_screenshot(page, screenshot_name) -> None:
    page.screenshot(path=f"../Results/screenshots/{screenshot_name}.png")
