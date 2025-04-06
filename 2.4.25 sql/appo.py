from sql import City
try:
    city = City("city_id", "city_name")
    city.create_table_cities()
    city.insert_into_table("tel aviv")

except Exception as err:
    print(err)