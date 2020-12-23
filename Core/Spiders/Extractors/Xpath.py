from lxml import html , etree


class Xpath_selector:

    def Extract(self, source, selector):
        try:
            source = html.fromstring(source)
            result = source.xpath(selector)
            return result
        except etree.ParseError:
            pass
            # print 17
        except etree.XPathEvalError:
            pass
            # print 18
