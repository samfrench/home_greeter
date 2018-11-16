class Matcher():
    MATCHES   = ['delivery', 'package', 'parcel']
    MIN_LEVEL = 0.9

    def is_delivery(self, classifications):
        threshold_items = { k: v for k, v in classifications.items() if v > self.MIN_LEVEL }
        return any([concept in threshold_items for concept in self.MATCHES])
