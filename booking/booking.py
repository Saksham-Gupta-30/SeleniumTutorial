from booking.constants import BASE_URL
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from booking.booking_filtration import BookingFiltration
from booking.booking_report import BookingReport
from prettytable import PrettyTable


class Booking(webdriver.Chrome):
    def __init__(self, driver_path=r"C:/SeleniumDrivers", teardown=False):
        self.teardown = teardown
        self.driver_path = driver_path
        # self.options = options
        os.environ['PATH'] += self.driver_path
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        options.add_experimental_option("detach", True)
        super(Booking, self).__init__(options=options)
        self.implicitly_wait(10)
        self.maximize_window()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if (self.teardown):
            self.quit()

    def land_first_page(self):
        self.get(BASE_URL)

    def change_currency(self, currency=None):
        currency_element = self.find_element(
            By.CSS_SELECTOR, 'button[data-testid="header-currency-picker-trigger"]'
        )
        currency_element.click()

        # selected_currency_element = self.find_element(
        #     By.LINK_TEXT, currency
        # )
        # selected_currency_element.click()

    def select_place_to_go(self, place_to_go):
        search_field = self.find_element(
            By.CSS_SELECTOR, 'input[id=":Ra9:"]'
        )
        search_field.clear()
        search_field.send_keys(place_to_go)

    def select_dates(self, check_in_date, check_out_date):
        check_in_field = self.find_element(
            By.CSS_SELECTOR, 'div[data-testid="searchbox-dates-container"]'
        )
        check_in_field.click()

        check_in_date_element = self.find_element(
            By.CSS_SELECTOR, f'span[data-date="{check_in_date}"]'
        )
        check_in_date_element.click()

        check_out_date_element = self.find_element(
            By.CSS_SELECTOR, f'span[data-date="{check_out_date}"]'
        )
        check_out_date_element.click()

    def select_guests(self, adults, children, rooms):
        guests_field = self.find_element(
            By.CSS_SELECTOR, 'button[data-testid="occupancy-config"]'
        )
        guests_field.click()

    def search(self):
        search_button = self.find_element(
            By.CSS_SELECTOR, 'button[type="submit"]'
        )
        search_button.click()

    def apply_filtration(self):
        filtration = BookingFiltration(driver=self)
        filtration.apply_star_rating(3, 4, 5)
        filtration.sort_price_lowest_first()

    def report_results(self):
        hotel_boxes = self.find_element(
            By.CLASS_NAME, 'd4924c9e74'
        )
        report = BookingReport(hotel_boxes)

        table = PrettyTable(
            field_names = ['Hotel Name', 'Price', 'Rating']
        )
        table.add_rows(report.pull_deal_box_attribute())
        print(table)