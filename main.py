from booking.booking import Booking



with Booking() as bot:
    bot.land_first_page()
    print("Exiting!")
#obj = Booking()
#obj.land_first_page()
#obj.get("https://web.whatsapp.com")