from booking.booking import Booking



with Booking() as bot:
    bot.land_first_page()
    bot.change_currency(currency="USD")
    bot.select_place_to_go("lekki")
#obj = Booking()
#obj.land_first_page()
#obj.get("https://web.whatsapp.com")