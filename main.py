from booking.booking import Booking


# a test try block to catch error caused by chromedriver path
try:
    with Booking() as bot:
        bot.land_first_page()
        bot.change_currency(currency="USD")
        bot.select_place_to_go("lekki")
        bot.select_place("lagos")
        bot.select_dates(check_in_date='2022-02-12', check_out_date='2022-03-18')
        bot.select_adults(1)
        bot.click_search()
        bot.apply_filters()

except Exception as e:
    if "PATH" in str(e):
        print("A problem related to the Chromedriver path")
    else:
        raise
