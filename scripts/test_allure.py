import allure


def test_aa():
    print("aaaa")
    assert 1

@allure.step(title="测试登录")
def test_login():
    allure.attach("登录","输入用户名")
    print("输入用户名")

    allure.attach("登录","输入密码")
    print("输入密码")

    allure.attach("登录", "点击登录")
    print("点击登录")
    assert 0
