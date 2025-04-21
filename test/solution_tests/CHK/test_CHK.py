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
        assert CheckoutSolution.checkout(self, "FF") == 20
        assert CheckoutSolution.checkout(self, "FFF") == 20
        assert CheckoutSolution.checkout(self, "FFFF") == 30
        assert CheckoutSolution.checkout(self, "FFFFF") == 40
        assert CheckoutSolution.checkout(self, "FFFFFF") == 40
        assert CheckoutSolution.checkout(self, "") == 0
        assert CheckoutSolution.checkout(self, "123") == -1
        assert CheckoutSolution.checkout(self, None) == -1
        assert CheckoutSolution.checkout(self, "A") == 50
        assert CheckoutSolution.checkout(self, "C") == 20
        assert CheckoutSolution.checkout(self, "Z") == 50
        assert CheckoutSolution.checkout(self, "AAA") == 130
        assert CheckoutSolution.checkout(self, "AAAAA") == 200
        assert CheckoutSolution.checkout(self, "AAAAAA") == 250
        assert CheckoutSolution.checkout(self, "ABCD") == 115
        assert CheckoutSolution.checkout(self, "AAABBCCDD") == 245
        assert CheckoutSolution.checkout(self, "EEBBB") == 125
        assert CheckoutSolution.checkout(self, "AABCDEFGHIJKLMNOPQRSTUVWXYZ") == 965
        assert CheckoutSolution.checkout(self, "EENNRRFFUUVV") == 490
        assert CheckoutSolution.checkout(self, "AAAAAABBEEHHHHHHHHHHKK") == 475
