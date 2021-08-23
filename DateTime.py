dailyData["date"] = dailyData.datetime.apply(lambda x : x.split()[0])

dailyData["hour"] = dailyData.datetime.apply(lambda x : x.split()[1].split(":")[0])

dailyData["weekday"] = dailyData.date.apply(lambda dateString : 

calendar.day_name[datetime.strptime(dateString,"%Y-%m-%d").weekday()])

dailyData["month"] = dailyData.date.apply(lambda dateString : 

calendar.month_name[datetime.strptime(dateString,"%Y-%m-%d").month])

dailyData["season"] = dailyData.season.map({1: "Spring", 2 : "Summer", 3 : "Fall", 4 :"Winter" })

dailyData["weather"] = dailyData.weather.map({1: " Clear + Few clouds + Partly cloudy + Partly cloudy",\
                                        2 : " Mist + Cloudy, Mist + Broken clouds, Mist + Few clouds, Mist ", \
                                        3 : " Light Snow, Light Rain + Thunderstorm + Scattered clouds, Light Rain + Scattered clouds", \
                                        4 :" Heavy Rain + Ice Pallets + Thunderstorm + Mist, Snow + Fog " })
