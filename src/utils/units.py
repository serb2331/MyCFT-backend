class Units:
    month_day = {
        "Jan": 0,
        "Feb": 31,
        "Mar": 59,
        "Apr": 90,
        "May": 120,
        "Jun": 151,
        "Jul": 181,
        "Aug": 212,
        "Sep": 243,
        "Oct": 273,
        "Nov": 304,
        "Dec": 334
    }
    @staticmethod
    def waterToCarbon(litres):
        return litres/1000*10.6
    @staticmethod
    def powerToCarbon(kwh):
        return kwh*0.433
    @staticmethod
    def fuelToCarbon(kms, fuelType, fuelEfficiency):
        if fuelType=='diesel':
            return kms/100*fuelEfficiency*2.7
        else:
            return kms/100*fuelEfficiency*2.3
    @staticmethod
    def calcDateDay(date: str):
        date_arr = date.split('-')
        return Units.month_day[date_arr[0]] + int(date_arr[1]) + int(date_arr[2]) * 365