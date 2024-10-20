class IDiscountStrategy():
    def GetDiscount():
        pass

class VipDiscountStrategy(IDiscountStrategy):
    def GetDiscount(monto: float):
        return monto * 0.2




class DiscountService():
    def __init__(self, vip:IDiscountStrategy):
        self.discountstrategy = vip

    def calculateDiscount(self, monto:float):
        return self.discountstrategy.GetDiscount(monto)

a = DiscountService(VipDiscountStrategy)
print(a.calculateDiscount(1000))

class PremiumDiscountStrategy(IDiscountStrategy):
    def GetDiscount(monto: float):
        return monto * 0.1

class RegularDiscountStrategy(IDiscountStrategy):
    def GetDiscount(monto: float):
        return monto * 0.05

a = DiscountService(PremiumDiscountStrategy)
print(a.calculateDiscount(1000))

a = DiscountService(RegularDiscountStrategy)
print(a.calculateDiscount(1000))