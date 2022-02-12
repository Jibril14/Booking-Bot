from booking.booking import Booking


with Booking() as bot:
    bot.land_first_page()
    bot.change_currency(currency="USD")
    bot.select_place_to_go("lekki")
    bot.select_place("lagos")
    bot.select_dates(check_in_date='2022-02-12', check_out_date='2022-03-18')

    bot.select_adults(2)
    bot.click_search()
