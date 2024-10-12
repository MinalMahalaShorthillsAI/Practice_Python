class Solution(object):
    def subdomainVisits(self, cpdomains):
        count_map = {}

        for entry in cpdomains:
            count, domain = entry.split()
            count = int(count)

            # Split the domain into its components
            subdomains = domain.split('.')

            # Construct subdomains and update the count in the hashmap
            for i in range(len(subdomains)):
                subdomain = '.'.join(subdomains[i:])
                if subdomain in count_map:
                    count_map[subdomain] += count
                else:
                    count_map[subdomain] = count

            # Prepare the result in the required format
        result = []
        for domain, count in count_map.items():
            result.append("{} {}".format(count, domain))

        return result