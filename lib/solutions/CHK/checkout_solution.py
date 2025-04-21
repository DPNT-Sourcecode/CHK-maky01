class CheckoutSolution:
    # skus = unicode string
    def checkout(self, skus):

        self.PRICES = {'A': 50, 'B': 30, 'C': 20, 'D': 15, 'E': 40, 'F': 10, 
                       'G': 20, 'H': 10, 'I': 35, 'J': 60, 'K': 70, 'L': 90,
                       'M': 15, 'N': 40, 'O': 10, 'P': 50, 'Q': 30, 'R': 50,
                       'S': 20, 'T': 20, 'U': 40, 'V': 50, 'W': 20, 'X': 17,
                       'Y': 20, 'Z': 21}
        self.SPECIAL_OFFERS_DISCOUNT = {'A': [(5, 200), (3, 130)], 'B': [(2, 45)], 'F': [(3, 20)],
                                        'H': [(10, 80), (5, 45)], 'K': [(2, 120)], 'P': [(5, 200)],
                                        'Q': [(3, 80)], 'U':[(4, 120)], 'V': [(3, 130), (2, 90)]}
        self.SPECIAL_OFFERS_FREE = {'E': (2, 'B'), 'N': (3, 'M'), 'R': (3, 'Q')}
        self.SPECIAL_OFFERS_GROUP = {'Z', 'S', 'T', 'Y', 'X'}

        # Check to see input is a string
        if not isinstance(skus, str):
            return -1

        # Create a dictionary with zero count for each SKU
        sku_counts_dict = {sku: 0 for sku in self.PRICES.keys()}

        # Check to see if each SKU is in the PRICES dictionary and add to count of each SKU is it is
        for char in skus:
            if char not in self.PRICES:
                return -1
            sku_counts_dict[char] += 1

        print(f"SKU counts: {sku_counts_dict}")

        for sku, count in sku_counts_dict.items():
            if sku in self.SPECIAL_OFFERS_FREE:
                free_count, free_sku = self.SPECIAL_OFFERS_FREE[sku]
                free_items = count // free_count
                sku_counts_dict[free_sku] = max(0, sku_counts_dict[free_sku] - free_items)

        # need to do group offers in reverse order so that we can favour the removal of the most expensive items first and have the remaining items be the cheapest
        # e.g. X is 17 and Z is 21, so remove the Z first.
        # group count, do price, then remove the items in order of the group

        total_price = 0

        group_count = 0
        group_list = []
        for sku in self.SPECIAL_OFFERS_GROUP:
            group_list.append((sku, sku_counts_dict[sku]))
            group_count += sku_counts_dict[sku]
        total_price += (group_count // 3) * 45
        # for sku, count in group_list:
                

        for sku, count in sku_counts_dict.items():
            if sku in self.SPECIAL_OFFERS_DISCOUNT:
                offers = self.SPECIAL_OFFERS_DISCOUNT[sku]
                for offer_count, offer_price in offers:
                    num_offers = count // offer_count
                    total_price += num_offers * offer_price
                    count %= offer_count

            total_price += count * self.PRICES[sku]
        return total_price

# test function
if __name__ == "__main__":
    checkout = CheckoutSolution()
    print(checkout.checkout("AABCDEFGHIJKLMNOPQRSTUVWXYZ"))
    print(checkout.checkout("EENNRRFFUUVV"))
    print(checkout.checkout("AAAAAABBEEHHHHHHHHHHKK"))
