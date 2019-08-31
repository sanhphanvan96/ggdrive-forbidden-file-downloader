import requests
import easyargs
import mimetypes
from halo import Halo
from selenium.webdriver.firefox.options import Options
from seleniumwire import webdriver

spinner = Halo(text='Loading ... ', spinner='dots')

fp = webdriver.FirefoxProfile()
fp.set_preference('browser.download.folderList', 2)
fp.set_preference('browser.download.manager.showWhenStarting', False)
fp.set_preference('browser.download.dir', '.')
fp.set_preference('media.volume_scale', '0.0')
fp.set_preference(
    'browser.helperApps.neverAsk.saveToDisk', 'application/x-gzip')
options = Options()
options.headless = True
options.firefox_profile = fp

driver = webdriver.Firefox(options=options)

# url = 'https://drive.google.com/file/d/1uOTsAdwYRSLvdpYNPkvrxiCr4SHsx86p/view'
cookies = []


@Halo(text='Loading ... ', spinner='dots')
def get_playback_link(url):
    driver.get(url)
    for request in driver.requests:
        if request.response:
            if '/videoplayback' in request.path:
                # set cookies
                global cookies
                cookies_list = driver.get_cookies()
                for cookie in cookies_list:
                    cookies.append([cookie['name'], cookie['value']])
                cookies = dict(cookies)
                driver.quit()

                return request.path
    driver.quit()
    return None


@Halo(text='Downloading video ... ', spinner='dots')
def download_video(url, filename):
    global cookies
    r = requests.get(url, cookies=cookies, stream=True)
    ext = mimetypes.guess_extension(r.headers.get('content-type'))
    filename += ext
    with open(filename, 'wb') as f:
        f.write(r.content)
    print('\n' + filename)


@easyargs
def main(videourl, filename='video'):
    if videourl:
        download_video(get_playback_link(videourl), filename)


if __name__ == '__main__':
    main()
