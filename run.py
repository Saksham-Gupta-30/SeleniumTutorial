from selenium.webdriver.common.by import By
from booking.booking import Booking

try:
    with Booking() as bot:
        bot.land_first_page()
        bot.find_element(
            By.CSS_SELECTOR, 'button[aria-label="Dismiss sign-in info."]'
        ).click()
        # bot.change_currency(currency='ARS')
        bot.select_place_to_go('Jaipur')
        bot.select_dates(check_in_date='2023-04-19', check_out_date='2023-05-19')
        bot.search()
        bot.apply_filtration()
        bot.refresh()
        bot.report_results()

except Exception as e:
    if 'in PATH' in str(e):
        print(
            'You are trying to run the bot from command line \n'
            'Please add to PATH your Selenium Drivers \n'
            'Windows: \n'
            '    set PATH=%PATH%;C:path-to-your-folder \n \n'
            'Linux: \n'
            '    PATH=$PATH:/path/toyour/folder/ \n'
        )
    else:
        raise
