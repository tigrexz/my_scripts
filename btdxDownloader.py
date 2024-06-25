import requests
from bs4 import BeautifulSoup
import re

def get_magnet_links(url):
    headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
        ,'Cookie': '_ga=GA1.2.212789730.1698606341; _ym_uid=1698606342552739664; Hm_lvt_99227487c7b463737ebb51a4713742c9=1712357932,1713865708,1714038255,1714515353; _ym_d=1714515355; b-user-id=6ed265b3-6185-c4e1-3927-adf9603e8399; guardok=U5Ev3fsEzq6RUxN+sA0pr9eL2xlGtjIkW8MaF9NOcJBU48dNBkGAUXr1FxrS9Gb9Da2s2/4AkuMtO7q3QVpWWA==; btpc_156951=156951'
    }
    try:
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.content, 'html.parser')
        magnet_links = []
        print=(response.content)
        # Find all <a> tags with href containing 'magnet:'
        for link in soup.find_all('a', href=re.compile(r'magnet:')):
            magnet_links.append(link['href'])

        return magnet_links
    except Exception as e:
        print(f"Error fetching magnet links: {e}")
        return []

if __name__ == "__main__":
    target_url = "https://www.btdx8.vip/torrent/jywxsj_2024.html"
    mp4_magnet_links = get_magnet_links(target_url)

    if mp4_magnet_links:
        for link in mp4_magnet_links:
            print(link)
    else:
        print("No MP4 magnet links found on the page.")


#for troubleshooting
# import requests
# url="https://www.btdx8.vip/torrent/xqjq%ef%bc%9axsj_2024.html"
# headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
#           ,'Cookie': '_ga=GA1.2.212789730.1698606341; _ym_uid=1698606342552739664; Hm_lvt_99227487c7b463737ebb51a4713742c9=1712357932,1713865708,1714038255,1714515353; _ym_d=1714515355; b-user-id=6ed265b3-6185-c4e1-3927-adf9603e8399; guardok=U5Ev3fsEzq6RUxN+sA0pr9eL2xlGtjIkW8MaF9NOcJBU48dNBkGAUXr1FxrS9Gb9Da2s2/4AkuMtO7q3QVpWWA==; btpc_156951=156951'}
# # cookies= {"_ga=GA1.2.212789730.1698606341; _ym_uid=1698606342552739664; Hm_lvt_99227487c7b463737ebb51a4713742c9=1712357932,1713865708,1714038255,1714515353; _ym_d=1714515355; b-user-id=6ed265b3-6185-c4e1-3927-adf9603e8399; guardok=U5Ev3fsEzq6RUxN+sA0pr9eL2xlGtjIkW8MaF9NOcJBU48dNBkGAUXr1FxrS9Gb9Da2s2/4AkuMtO7q3QVpWWA==; btpc_156951=156951"}
# response = requests.get(url, headers=headers,)
# a=response.content.decode('utf-8')
# with open("tdx.html","w",encoding='utf-8') as f:
#     f.write(a)