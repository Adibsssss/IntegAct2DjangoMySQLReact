import xml.etree.ElementTree as ET
from django.http import HttpResponse


def parse_xml_request(body):

    try:
        root = ET.fromstring(body)

        data = {}

        for child in root:
            data[child.tag] = child.text

        return data

    except:
        return None


def dict_to_xml(root_tag, data):

    root = ET.Element(root_tag)

    for key, value in data.items():

        child = ET.SubElement(root, key)

        child.text = str(value)

    return ET.tostring(root)


def xml_response(data, status=200, root_tag="response"):

    xml = dict_to_xml(root_tag, data)

    return HttpResponse(xml, content_type="application/xml", status=status)