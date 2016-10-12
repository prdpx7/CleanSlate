import pkg_resources
class NSFW(object):
    RESOURCE_PATH_URL  = pkg_resources.resource_filename('cleanslate','nsfw_urls.txt')
    RESOURCE_PATH_WORD  = pkg_resources.resource_filename('cleanslate','nsfw_words.txt')
    URLS = open(RESOURCE_PATH_URL).read().split()
    KEYWORDS = open(RESOURCE_PATH_WORD).read().split()
