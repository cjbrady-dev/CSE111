from names import make_full_name, extract_family_name, extract_given_name
import pytest

def test_make_full_name():



    full_name = make_full_name("Brady","James")
    assert isinstance(full_name, str)

    assert make_full_name("Santa","Claws") == "Claws;Santa"
    assert make_full_name("lol",";")  == ";;lol"
    assert make_full_name("Ted","0") == "0;Ted"
    #Write assert statements inside this function to test the value returned from the make_full_name function.
def test_extract_family_name():
    fam_name = extract_family_name("Brady; James")
    assert isinstance(fam_name, str)
    #Write assert statements inside this function to test the value returned from the extract_family_name function
    assert extract_family_name("Brown; Sally") == "Brown"
    assert extract_family_name("lol; non") == "lol"
    assert extract_family_name("Hi; [[]]") == "Hi"
def test_extract_given_name():
    giv_name = extract_given_name("Brady; James")
    assert isinstance(giv_name, str)

    assert extract_given_name("Brown; Sally") == "Sally"
    assert extract_given_name("lol; non") == "non"
    assert extract_given_name("Hi; [[]]") == "[[]]"
    #Write assert statements inside this function to test the value returned from the extract_given_name function.
# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])

#Core Requirements
#Write test_make_full_name so that it tests make_full_name with various names, including long names, short names, and hyphenated names. Fix the mistake in the make_full_name function.
#Write test_extract_family_name so that it tests extract_family_name with various names, including long names, short names, and hyphenated names.
#Write test_extract_given_name so that it tests extract_given_name with various names, including long names, short names, and hyphenated names. Fix the mistake in the extract_given_name function.