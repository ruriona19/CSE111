import names
import pytest


def test_make_full_name():
    assert names.make_full_name("Roberto", "Uriona") == "Uriona; Roberto"
    assert names.make_full_name("", "") == "; "


def test_extract_family_name():
    assert names.extract_family_name("Uriona; Roberto") == "Uriona"
    assert names.extract_family_name("; ") == ""


def test_extract_given_name():
    assert names.extract_given_name("Uriona; Roberto") == "Roberto"
    assert names.extract_given_name("; ") == ""


pytest.main(["-v", "--tb=line", "-rN", __file__])