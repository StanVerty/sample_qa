from time import sleep

from selenium.common.exceptions import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from pages.base_page import BasePage


class HomePage(BasePage):
    # LOCATORS
    _society6_logo = 'a[id="s6-logo"]'
    _upper_block = '//a[@data-gtm-event="homepageHero"]//h1'  # list of 3 elements in 1st block
    _main_image_upper_block_text = '//div[contains(@class,"heroTextBox")]//h1'  # to use for text comparison on the next page

    _featured_products_block_header = '//div[@qa-id="textHeader"]/h1[text()="Featured Products"]'
    _featured_products_block_imgs = '//h1[contains(text(),"Featured Products")]//parent::div//following-sibling::div[@qa-id="featuredProducts"][1]//label'  # list of 5 images

    _popular_collections_block = 'div[qa-id="latestCollections"] h4'  # list of 3 images in the block

    _introducing_cotton_bedding_block = 'div[qa-id="promoBanner"] h1'

    _featured_artists_block_header = 'div[qa-id="featuredArtists"] h3'
    _featured_artists_block_sub = '//div[@class="slick-slide slick-active slick-current"]//img//following-sibling::label'
    _right_arrow = '//div[@class="slick-slider slick-initialized"]//button[@class="slick-arrow slick-next"]'

    _get_started_block_header = '//div[@qa-id="textHeader"]/h1[text()="Get Started"]'
    _pair_your_favorite_designs_img = '//h1[contains(text(),"Get Started")]//parent::div//following-sibling::div[@qa-id="featuredProducts"][1]//img'
    _with_our_array_of_products_img = '//h1[contains(text(),"Get Started")]//parent::div//following-sibling::div[@qa-id="featuredProducts"][2]//img'

    _trending_now_block_header = '//div[@qa-id="textHeader"]/h1[text()="Trending Now"]'
    _trending_now_block_images = '//div[@qa-id="productsGroup"]//div[contains(@class,"image_product")]'  # list of 16 images in the Trending Now block

    _shop_by_category_header = '//div[@qa-id="homepageLinkFarm"]//div[contains(@class,"header_homepageLinkFarm")]//h3[(text()="Shop by Category")]'
    _shop_by_style_header = '//div[@qa-id="homepageLinkFarm"]//div[contains(@class,"header_homepageLinkFarm")]//h3[(text()="Shop by Style")]'
    _shop_by_room_header = '//div[@qa-id="homepageLinkFarm"]//div[contains(@class,"header_homepageLinkFarm")]//h3[(text()="Shop by Room")]'

    _every_purchase_pays_an_artist_header = 'a[data-gtm-event="fullWidthBanner"] h1'
    _from_the_society6_blog_block_header = 'div[qa-id="blogContent"] h3'
    _from_the_society6_blog_images = '//a[contains(@class,"imageLink_blogContent")]'  # list of 3 images

    def verify_society_logo(self):
        try:
            WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, self._society6_logo)))
            return True
        except TimeoutException:
            return False

    def verify_upper_block(self):
        try:
            upper_block_titles = WebDriverWait(self.driver, 5).until(
                EC.presence_of_all_elements_located((By.XPATH, self._upper_block)))
            return len(upper_block_titles) == 3
        except:
            return False

    def verify_featured_products_block_header(self):
        try:
            featured_products_block_header = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.XPATH, self._featured_products_block_header))).text
            return featured_products_block_header == ['Featured Products']
        except:
            return False

    def verify_featured_products_block(self):
        try:
            featured_products_block_titles = WebDriverWait(self.driver, 5).until(
                EC.presence_of_all_elements_located((By.XPATH, self._featured_products_block_imgs)))
            featured_products_block_titles_text = [title.text for title in featured_products_block_titles]
            return featured_products_block_titles_text == ['Framed Prints', 'Art Prints', 'Phone Cases',
                                                           'Throw Pillows', 'Tote Bags']
        except:
            return False

    def verify_popular_collections_block(self):
        try:
            popular_collections_block_titles = WebDriverWait(self.driver, 5).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, self._popular_collections_block)))
            popular_collections_block_text = [title.text for title in popular_collections_block_titles]
            return popular_collections_block_text == ['Discover Black Artists', 'Trending Drinkware',
                                                      'Top Art Picks']
        except:
            return False

    def verify_introducing_cotton_bedding_block(self):
        try:
            introducing_cotton_bedding_block_title = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, self._introducing_cotton_bedding_block)))
            self.driver.execute_script("arguments[0].scrollIntoView(true);", introducing_cotton_bedding_block_title)
            print(introducing_cotton_bedding_block_title.text)
            return introducing_cotton_bedding_block_title.text == '2021 Spring Decor Guide Has Arrived!'
        except:
            return False

    def verify_featured_artists_block_header(self):
        try:
            featured_artists_block_header = WebDriverWait(self.driver, 20).until \
                (EC.presence_of_element_located((By.CSS_SELECTOR, self._featured_artists_block_header))).text
            return featured_artists_block_header == 'Featured Artists'
        except:
            return False

    def featured_artists_block_click_right_arrow(self):
        featured_artists_block = self.driver.find_element(By.XPATH, self._right_arrow)
        featured_artists_block.click()
        sleep(2)

    def verify_featured_artists_block_subtitles(self):
        featured_artists_block_header = WebDriverWait(self.driver, 20).until \
            (EC.presence_of_element_located((By.CSS_SELECTOR, self._featured_artists_block_header)))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", featured_artists_block_header)
        sleep(2)
        all_subtitles = []
        i = 0
        while i < 3:
            subtitle = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.XPATH, self._featured_artists_block_sub))).text
            print(f"Found {i + 1} label")
            all_subtitles.append(subtitle)
            print(all_subtitles)
            self.featured_artists_block_click_right_arrow()
            i += 1
        return all_subtitles == ['Min Jin', 'Kayla Lane', 'Alejandro Ibarra']

    def verify_get_started_block_header(self):
        try:
            get_started_block_header = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.XPATH, self._get_started_block_header))).text
            return get_started_block_header == "Get Started"
        except:
            return False

    def verify_pair_your_favorite_designs_block(self):
        try:
            get_started_block_header = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.XPATH, self._get_started_block_header)))
            self.driver.execute_script("arguments[0].scrollIntoView(true);", get_started_block_header)
            pair_your_favorite_designs_block = WebDriverWait(self.driver, 5).until(
                EC.presence_of_all_elements_located((By.XPATH, self._pair_your_favorite_designs_img)))
            return len(pair_your_favorite_designs_block) == 5
        except:
            return False


    def verify_trending_now_block_header(self):
        try:
            trending_now_block_header = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.XPATH, self._trending_now_block_header))).text
            return trending_now_block_header == "Trending Now"
        except:
            return False


    def verify_trending_now_block_images(self):
        try:
            trending_now_block_header = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.XPATH, self._trending_now_block_header)))
            self.driver.execute_script("arguments[0].scrollIntoView(true);", trending_now_block_header)
            trending_now_block_images = WebDriverWait(self.driver, 5).until(
                EC.presence_of_all_elements_located((By.XPATH, self._trending_now_block_images)))
            return len(trending_now_block_images) == 16
        except:
            return False

    def verify_shop_by_category_header(self):
        try:
            shop_by_category_header = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.XPATH, self._shop_by_category_header))).text
            return shop_by_category_header == "Shop by Category"
        except:
            return False

    def verify_shop_by_style_header(self):
        try:
            shop_by_style_header = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.XPATH, self._shop_by_style_header))).text
            return shop_by_style_header == "Shop by Style"
        except:
            return False


    def verify_shop_by_room_header(self):
        try:
            shop_by_room_header = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.XPATH, self._shop_by_room_header))).text
            return shop_by_room_header == "Shop by Room"
        except:
            return False


    def verify_every_purchase_pays_an_artist_header(self):
        try:
            every_purchase_pays_an_artist_header = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, self._every_purchase_pays_an_artist_header))).text
            return every_purchase_pays_an_artist_header == "Every purchase pays an artist."
        except:
            return False


    def verify_from_the_society6_blog_block_header(self):
        try:
            from_the_society6_blog_block_header = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, self._from_the_society6_blog_block_header))).text
            return from_the_society6_blog_block_header == "From the Society6 Blog"
        except:
            return False


    def from_the_society6_blog_images(self):
        try:
            from_the_society6_blog_block_header = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, self._from_the_society6_blog_block_header)))
            self.driver.execute_script("arguments[0].scrollIntoView(true);", from_the_society6_blog_block_header)
            from_the_society6_blog_images = WebDriverWait(self.driver, 5).until(
                EC.presence_of_all_elements_located((By.XPATH, self._from_the_society6_blog_images)))
            return len(from_the_society6_blog_images) == 3
        except:
            return False
