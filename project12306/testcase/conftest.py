
import sys
import os
from Appium.project12306.base.basepage import BasePage

print("Loading conftest.py")

# # 获取当前脚本的绝对路径
# current_dir = os.path.dirname(os.path.abspath(__file__))
# print(f"Current directory: {current_dir}")
#
# # 将项目根目录添加到系统路径
# sys.path.append(os.path.join(current_dir, '..', '..'))
# print(f"Added to path: {os.path.join(current_dir, '..', '..')}")
from Appium.project12306.common.start_util import setup
import pytest

# @pytest.fixture(scope="function", autouse=True)
@pytest.fixture(scope="module")
def setup_teardown():
    print("Setting up teardown")
    driver = setup()
    base_page = BasePage(driver)
    yield driver, base_page
    if hasattr(driver, 'quit'):
        driver.quit()
        base_page.logger.info("Driver quit")