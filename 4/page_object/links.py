import pytest


class Links:
    PRODUCT_PAGES = (
        "link",
        [
            "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
            "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
            "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
            "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
            "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
            "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
            "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
            pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                         marks=pytest.mark.xfail),
            "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
            "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"
        ])
    FIRST_PRODUCT_PAGE = (
        "link",
        ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"]
    )
    SECOND_PRODUCT_PAGE = (
        "link",
        ["http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"]
    )
    THIRD_PRODUCT_PAGE = (
        "link",
        ["http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer"]
    )
    LOGIN_PAGE = (
        "login_page_link",
        ["http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"]
    )
    MAIN_PAGE = (
        "link",
        ["http://selenium1py.pythonanywhere.com/"]
    )
