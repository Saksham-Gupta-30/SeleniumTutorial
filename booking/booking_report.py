# This file is going to include method that will parse
# the specific data that we need from each one of the deal boxes.

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

class BookingReport:
    def __init__(self, boxes_selection_element:WebElement):
        self.boxes_selection_element = boxes_selection_element
        self.deal_boxes = self.pull_deal_boxes()

    def pull_deal_boxes(self):
        return self.boxes_selection_element.find_elements(
            By.CSS_SELECTOR, 'div[data-testid="property-card"]'
        )
    
    def pull_deal_box_attribute(self):
        collection = []
        for deal_box in self.deal_boxes:
            hotel_name = deal_box.find_element(
                By.CSS_SELECTOR, 'div[data-testid="title"]'
            ).get_attribute('innerHTML').strip()
            
            hotel_price = deal_box.find_element(
                By.CSS_SELECTOR, 'span[data-testid="price-and-discounted-price"]'
            ).get_attribute('innerHTML').strip().replace('&nbsp;', ' ').replace('₹', 'Rs.')

            try:
                hotel_review = deal_box.find_element(
                    By.CSS_SELECTOR, 'div[data-testid="review-score"]'
                )
                hotel_score = hotel_review.find_element(
                    By.CSS_SELECTOR, 'div[class="b5cd09854e d10a6220b4"]'
                ).get_attribute('innerHTML').strip()
            except:
                hotel_score = 'No score'

            collection.append(
                [hotel_name, hotel_price, hotel_score]
            )
        return collection