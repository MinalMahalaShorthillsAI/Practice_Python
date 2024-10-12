import unittest
from code import Solution

class TestSubdomainVisits(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_single_domain_with_subdomains(self):
        self.assertEqual(sorted(self.solution.subdomainVisits(["9001 discuss.leetcode.com"])), 
                         sorted(["9001 leetcode.com", "9001 discuss.leetcode.com", "9001 com"]))

    def test_multiple_count_paired_domains(self):
        self.assertEqual(sorted(self.solution.subdomainVisits(["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"])), 
                         sorted(["901 mail.com", "50 yahoo.com", "900 google.mail.com", "5 wiki.org", "5 org", "1 intel.mail.com", "951 com"]))

    def test_no_subdomains(self):
        self.assertEqual(sorted(self.solution.subdomainVisits(["10 example.com"])), 
                         sorted(["10 example.com", "10 com"]))

    def test_single_count_paired_domain_without_subdomains(self):
        self.assertEqual(sorted(self.solution.subdomainVisits(["1 a.com"])), 
                         sorted(["1 a.com", "1 com"]))

    def test_multiple_subdomain_levels(self):
        self.assertEqual(sorted(self.solution.subdomainVisits(["5001 music.apple.com", "5001 itunes.apple.com"])), 
                         sorted(["10002 apple.com", "5001 itunes.apple.com", "5001 music.apple.com", "10002 com"]))

    def test_duplicate_domains(self):
        self.assertEqual(sorted(self.solution.subdomainVisits(["300 google.com", "200 google.com"])), 
                         sorted(["500 google.com", "500 com"]))

    def test_single_visit_with_multiple_levels(self):
        self.assertEqual(sorted(self.solution.subdomainVisits(["1 a.b.c.com"])), 
                         sorted(["1 a.b.c.com", "1 b.c.com", "1 c.com", "1 com"]))

    def test_multiple_domains_with_varied_visits(self):
        self.assertEqual(sorted(self.solution.subdomainVisits(["1000 a.com", "200 b.com", "300 c.d.e.com"])), 
                         sorted(["1000 a.com", "1500 com", "200 b.com", "300 c.d.e.com", "300 d.e.com", "300 e.com"]))

    def test_maximal_visits(self):
        self.assertEqual(sorted(self.solution.subdomainVisits(["10000 high.visit.com"])), 
                         sorted(["10000 high.visit.com", "10000 visit.com", "10000 com"]))

    def test_empty_input(self):
        self.assertEqual(self.solution.subdomainVisits([]), [])

if __name__ == '__main__':
    unittest.main()