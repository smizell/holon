from holon import __version__
from holon.formats.alps import ALPS, Descriptor, DescriptorType, Doc, Link
from holon.ietf.rfc2119 import Keyword
from holon.design_system import APIDesignSystem, PrincipleRule
from holon.models import wadm


def test_version():
    assert __version__ == "0.1.0"


def test_design_system():
    APIDesignSystem(
        principles=[
            PrincipleRule(keyword=Keyword.SHOULD, principle=wadm.resource_centric),
            PrincipleRule(keyword=Keyword.MAY, principle=wadm.affordance_centric),
            PrincipleRule(keyword=Keyword.MUST_NOT, principle=wadm.database_centric),
        ]
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
