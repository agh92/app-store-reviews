import requests
from lxml import etree
from lxml.etree import tostring

from stores.Model.review import AppStoreReview

# an other posible source:
# http://ax.phobos.apple.com.edgesuite.net/WebObjects/MZStoreServices.woa/wa/wsLookup?id=343200656&country=us
# ${opts.country} ${opts.page} ${id}  sortby={}/${opts.sort}
# use xml because it has two more fields than the json updated and html - json also availible
_resource = "https://itunes.apple.com/{}/rss/customerreviews/page={}/id={}/sortBy=mostRecent/xml"


def raw_reviews(app_id: str, country_code: str):
    received = 1
    page = 1
    while received > 0:
        url = _resource.format(country_code, page, app_id)
        resp = requests.post(url)
        tree = etree.fromstring(resp.content)
        received = len(list(tree.iter("{" + tree.nsmap[None] + "}entry")))
        page += 1
        tpl = (resp.text, resp.content)
        # check that we are not adding content that is the same
        if received > 0:
            yield tpl


def _parse_reviews(content, app_id=None):
    tree = etree.fromstring(content)
    std_namespace = tree.nsmap[None]
    # im_namespace = tree.nsmap['im']
    r = []
    # skip the first entry because its the itunes description and not a review
    iter_child = tree.iter("{" + std_namespace + "}entry")
    # itunes_entry = tree.find('{' + std_namespace + '}entry')
    # if itunes_entry is not None:  # the first entry is itunes information not review
    #     app_id = itunes_entry.find('{' + std_namespace + '}id').get('{' + im_namespace + '}id')
    # else:
    #     app_id = None
    for child in iter_child:
        if _text_body(child):
            parsed_review = _parse_review(child)
            parsed_review.app_id = app_id
            r.append(parsed_review)
    return r


def _text_body(entry, std_namespace="http://www.w3.org/2005/Atom"):
    body = ""
    # content < type="text"> text
    for content in entry.iter("{" + std_namespace + "}content"):
        if content.get("type") == "text":
            body = content.xpath("string()")
            break
    return body


def _parse_review(
    entry,
    std_namespace="http://www.w3.org/2005/Atom",
    im_namespace="http://itunes.apple.com/rss",
):
    # tostring will return bytes and we cant json serelize bytes so call str
    raw = str(tostring(entry))
    review_id = entry.find("{" + std_namespace + "}id").xpath("string()")
    updated = entry.find("{" + std_namespace + "}updated").xpath("string()")
    # title <title> text
    title = entry.find("{" + std_namespace + "}title").xpath("string()")
    body = _text_body(entry)
    # rating <im:rating> text
    rating = entry.find("{" + im_namespace + "}rating")
    if rating is not None:
        rating = rating.xpath("string()")
    # version <im:version> text
    version = entry.find("{" + im_namespace + "}version")
    if version is not None:
        version = version.xpath("string()")
    author_name = entry.find(
        "{" + std_namespace + "}author/" + "{" + std_namespace + "}name"
    )  # author_name <author><name> text
    if author_name is not None:
        author_name = author_name.xpath("string()")
    return AppStoreReview(
        None, review_id, author_name, updated, rating, title, body, version, raw
    )
