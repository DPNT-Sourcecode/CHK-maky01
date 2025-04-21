from lib.solutions.CHK.checkout_solution import CheckoutSolution

class TestCheckout():
    def test_checkout(self):
        assert CheckoutSolution.checkout(self, "AAA") == 130
        assert CheckoutSolution.checkout(self, "AA") == 100
        assert CheckoutSolution.checkout(self, "BB") == 45
        assert CheckoutSolution.checkout(self, "AAAA") == 180
        assert CheckoutSolution.checkout(self, "AAB") == 130
        assert CheckoutSolution.checkout(self, "ABCD") == 115
        assert CheckoutSolution.checkout(self, "AAABBCCDD") == 245
        assert CheckoutSolution.checkout(self, "EE") == 80
        assert CheckoutSolution.checkout(self, "EEB") == 80
        assert CheckoutSolution.checkout(self, "EEBB") == 110
        assert CheckoutSolution.checkout(self, "EEBBB") == 125

