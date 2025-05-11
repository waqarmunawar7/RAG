import requests
from urllib.parse import urljoin, urlparse
from bs4 import BeautifulSoup


class Helper():  


    @staticmethod
    def get_all_valid_links(url, domain=None, visited=None):
        if visited is None:
            visited = set()

        if domain is None:
            domain = urlparse(url).netloc

        if url in visited:
            return visited

        try:
            response = requests.get(url, timeout=5)
            if response.status_code != 200:
                print(f"Skipping {url} - HTTP {response.status_code}")
                return visited

            if "nothing found" in response.text.lower():
                print(f"Skipping {url} - 'Nothing Found' in content")
                return visited

            visited.add(url)
            print(f"Valid URL: {url}")

            soup = BeautifulSoup(response.content, "html.parser")
            for tag in soup.find_all("a", href=True):
                href = tag['href']
                full_url = urljoin(url, href)
                parsed_href = urlparse(full_url)

                if parsed_href.netloc == domain:
                    normalized_url = parsed_href.scheme + "://" + parsed_href.netloc + parsed_href.path
                    if normalized_url not in visited:
                        Helper.get_all_valid_links(normalized_url, domain, visited)

        except Exception as e:
            print(f"Error visiting {url}: {e}")

        return list(visited)
