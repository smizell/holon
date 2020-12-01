from holon import __version__
from holon.ietf import rfc7232
from holon.design_system import (
    APIDesignSystem,
    HeaderRule,
    HTTPRuleSet,
    MediaTypeRule,
    PrincipleRule,
)
from holon.formats.alps import ALPS, Descriptor, DescriptorType, Doc, Link
from holon.http import HTTPMessage, HTTPMethod
from holon.ietf.rfc2119 import Keyword
from holon.media_types import MediaType
from holon.models import wadm


def test_version():
    assert __version__ == "0.1.0"


def test_design_system():
    APIDesignSystem(
        principles=[
            PrincipleRule(keyword=Keyword.SHOULD, principle=wadm.resource_centric),
            PrincipleRule(keyword=Keyword.MAY, principle=wadm.affordance_centric),
            PrincipleRule(keyword=Keyword.MUST_NOT, principle=wadm.database_centric),
        ],
        http_rules=HTTPRuleSet(
            headers=[
                HeaderRule(
                    keyword=Keyword.MAY,
                    header=rfc7232.if_match,
                ),
                HeaderRule(
                    keyword=Keyword.MAY,
                    header=rfc7232.if_none_match,
                ),
                HeaderRule(
                    keyword=Keyword.MAY,
                    header=rfc7232.etag,
                ),
            ],
            media_types=[
                MediaTypeRule(
                    keyword=Keyword.MUST,
                    media_type=MediaType(
                        name="application/json",
                        reference="https://tools.ietf.org/html/rfc8259",
                    ),
                )
            ],
        ),
    )


def test_alps():
    ALPS(
        version="1.0",
        doc=Doc(text="A contact list."),
        links=[Link(rel="help", href="http://example.org/help/contacts.html")],
        descriptors=[
            Descriptor(
                id="collection",
                type=DescriptorType.SAFE,
                rt="contact",
                doc=Doc(text="A simple link/form for getting a list of contacts."),
                descriptors=[
                    Descriptor(
                        id="nameSearch", doc=Doc(text="Input for a search form.")
                    )
                ],
            ),
            Descriptor(
                id="contact",
                descriptors=[
                    Descriptor(
                        id="item",
                        type=DescriptorType.SAFE,
                        doc=Doc(text="A link to an individual contact."),
                    ),
                    Descriptor(id="fullName"),
                    Descriptor(id="email"),
                    Descriptor(id="phone"),
                ],
            ),
        ],
    )
