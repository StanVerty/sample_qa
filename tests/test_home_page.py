import pytest
from pages.home_page import HomePage

@pytest.mark.homepage
class HomePageTest():

    def test_society_logo_present(self, driver):
        hp = HomePage(driver)
        hp.go_to_homepage()
        assert hp.verify_society_logo()

    def test_upper_block_present(self, driver):
        hp = HomePage(driver)
        hp.go_to_homepage()
        assert hp.verify_upper_block()

    def test_featured_products_block_header(self,driver):
        hp = HomePage(driver)
        hp.go_to_homepage()
        assert hp.verify_featured_products_block_header

    def test_featured_products_block(self, driver):
        hp = HomePage(driver)
        hp.go_to_homepage()
        assert hp.verify_featured_products_block()

    def test_popular_collections_block(self, driver):
        hp = HomePage(driver)
        hp.go_to_homepage()
        assert hp.verify_popular_collections_block()


    def test_introducing_cotton_bedding_block(self, driver):
        hp = HomePage(driver)
        hp.go_to_homepage()
        assert hp.verify_introducing_cotton_bedding_block()

    def test_verify_featured_artists_block_header(self, driver):
        hp = HomePage(driver)
        hp.go_to_homepage()
        assert hp.verify_featured_artists_block_header()


    def test_verify_featured_artists_block_subtitles(self, driver):
        hp = HomePage(driver)
        hp.go_to_homepage()
        assert hp.verify_featured_artists_block_subtitles()


    def test_verify_get_started_block_header(self, driver):
        hp = HomePage(driver)
        hp.go_to_homepage()
        assert hp.verify_get_started_block_header()


    def test_verify_pair_your_favorite_designs_block(self, driver):
        hp = HomePage(driver)
        hp.go_to_homepage()
        assert hp.verify_pair_your_favorite_designs_block()


    def test_verify_trending_now_block_header(self, driver):
        hp = HomePage(driver)
        hp.go_to_homepage()
        assert hp.verify_trending_now_block_header()


    def test_verify_trending_now_block_images(self, driver):
        hp = HomePage(driver)
        hp.go_to_homepage()
        assert hp.verify_trending_now_block_images()


    def test_verify_shop_by_category_header(self, driver):
        hp = HomePage(driver)
        hp.go_to_homepage()
        assert hp.verify_shop_by_category_header()


    def test_verify_shop_by_style_header(self, driver):
        hp = HomePage(driver)
        hp.go_to_homepage()
        assert hp.verify_shop_by_style_header()


    def test_verify_shop_by_room_header(self, driver):
        hp = HomePage(driver)
        hp.go_to_homepage()
        assert hp.verify_shop_by_room_header()

    @pytest.mark.run
    def test_verify_every_purchase_pays_an_artist_header(self, driver):
        hp = HomePage(driver)
        hp.go_to_homepage()
        assert hp.verify_every_purchase_pays_an_artist_header()

    @pytest.mark.run
    def test_verify_from_the_society6_blog_block_header(self, driver):
        hp = HomePage(driver)
        hp.go_to_homepage()
        assert hp.verify_from_the_society6_blog_block_header()

    @pytest.mark.run
    def test_from_the_society6_blog_images(self, driver):
        hp = HomePage(driver)
        hp.go_to_homepage()
        assert hp.from_the_society6_blog_images()