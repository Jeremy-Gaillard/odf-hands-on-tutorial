# coding: utf-8

from bs4 import BeautifulSoup
import json

def dictionary2omi_r(hierarchy):
    xml = ""
    if type(hierarchy) == dict:
        for k, v in hierarchy.items():
            children = ""
            children += dictionary2omi_r(v)
            xml += \
"""<Object>
    <id>{}</id>{}
</Object>""".format(k, children)
    else:
        for k in hierarchy:
            xml += \
"""<Object>
    <id>{}</id>
</Object>""".format(k)
    return xml

def dictionary2omi(hierarchy, newest=None):
    parameters = ""
    if newest is not None:
        parameters = ' newest="{}"'.format(newest)
    root = dictionary2omi_r(hierarchy)
    return \
"""<omiEnvelope xmlns="http://www.opengroup.org/xsd/omi/1.0/" version="1.0" ttl="0">
    <read msgformat="odf"{}>
        <msg>
            <Objects xmlns="http://www.opengroup.org/xsd/odf/1.0/">
                {}
            </Objects>
        </msg>
    </read>
</omiEnvelope>""".format(parameters, root)