from inheritance import NewStore


class BeerStore(NewStore):
    water = 10000
    beer = 20

    # @classmethod
    def info(self):
        storeInfo = super().info()
        return storeInfo + f' Alcohol: {self.beer} beer.'
    
gradus = BeerStore('Gradus')
print(gradus.info())