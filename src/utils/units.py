class Units:
    @staticmethod
    def waterToCarbon(litres):
        return litres/1000*10.6
    @staticmethod
    def powerToCarbon(kwh):
        return kwh*0.433
    @staticmethod
    def fueltoCarbon(kms, fuelType, fuelEfficiency):
        if fuelType=='diesel':
            return kms/100*fuelEfficiency*2.7
        else:
            return kms/100*fuelEfficiency*2.3
