from backend.src.parser_prescription import PrescriptionParser
import pytest                                 #`assert`statement were running with pytest being installed no need to import `pytest`, but as we have write multiple test function in all i am creating `PrescriptionParser` object, hemce need to refactor such duplications, also i have to include multiple "document_text", so for that i need to use pytest fixtures hence need to import pytest

@pytest.fixture()                             # `pytest.fixture` decorator is a powerful feature in the Pytest framework that allows you to define reusable setup and teardown code for your tests. Fixtures provide a way to inject test dependencies into your test functions, making your tests more modular, maintainable, and readable. these function over which they are defined contain setup code, such as creatng objects, initializing resources or connecting to databases,also it contain teardown code{these rae set of instructions or actions that need to be executed after a test case has been run. It is typically used to clean up resources, release memory, close connections, or perform any necessary cleanup tasks after th test has completed its execution}
def doc_1_maria():
    document_text = """
Dr John Smith, M.D
2 Non-Important Street,
New York, Phone (000)-111-2222
Name: Marta Sharapova Date: 5/11/2022
Address: 9 tennis court, new Russia, DC

Prednisone 20 mg
Lialda 2.4 gram
Directions:
Prednisone, Taper 5 mg every 3 days,
Finish in 2.5 weeks -
Lialda - take 2 pill everyday for 1 month
Refill: 3 times
"""
    return PrescriptionParser(document_text)

@pytest.fixture()
def doc_2_virat():
    document_text = """
Dr John Smith, M.D

2 Non-Important Street,
New York, Phone (900)-323-2222

Name: Virat Kohli Date: 2/05/2022

Address: 2 cricket blvd, New Delhi

Omeprazole 40 mg

Directions: Use two tablets daily for three months

Refill: 3 times
"""
    return PrescriptionParser(document_text)

@pytest.fixture()
def doc_3_empty():                     # as we want to test out test fuctions not only for success cases but failed cases too, to make sure everything works
    return PrescriptionParser('')

def test_get_name(doc_1_maria, doc_2_virat, doc_3_empty):
    assert doc_1_maria.get_field('patient_name') == 'Marta Sharapova'      # this function should retunrn this name as we know that from the text we are using to test the implementation of the `parser_prescription` we have written. And the way to express this expectation in the unit test is by writing `assert` statement
                                                                  # and if this does what is expected from this unit test, then we will say that this test is passing
    assert doc_2_virat.get_field('patient_name') == 'Virat Kohli'
    assert doc_3_empty.get_field('patient_name') == None


def test_get_address(doc_1_maria, doc_2_virat, doc_3_empty):
    assert doc_1_maria.get_field('patient_address') == '9 tennis court, new Russia, DC'
    assert doc_2_virat.get_field('patient_address') == '2 cricket blvd, New Delhi'
    assert doc_3_empty.get_field('patient_address') == None

def test_get_medicines(doc_1_maria, doc_2_virat, doc_3_empty):
    assert doc_1_maria.get_field('medicines') == 'Prednisone 20 mg\nLialda 2.4 gram'
    assert doc_2_virat.get_field('medicines') == 'Omeprazole 40 mg'
    assert doc_3_empty.get_field('medicines') == None

def test_get_directions(doc_1_maria, doc_2_virat, doc_3_empty):
    assert doc_1_maria.get_field('directions') == 'Prednisone, Taper 5 mg every 3 days,\nFinish in 2.5 weeks -\nLialda - take 2 pill everyday for 1 month'
    assert doc_2_virat.get_field('directions') == 'Use two tablets daily for three months'
    assert doc_3_empty.get_field('directions') == None

def test_get_refill(doc_1_maria, doc_2_virat, doc_3_empty):
    assert doc_1_maria.get_field('refills') == '3'
    assert doc_2_virat.get_field('refills') == '3'
    assert doc_3_empty.get_field('refills') == None

def test_parse(doc_1_maria, doc_2_virat, doc_3_empty):
    record_maria = doc_1_maria.parse()
    assert record_maria['patient_name'] == 'Marta Sharapova'
    assert record_maria['patient_address'] == '9 tennis court, new Russia, DC'
    assert record_maria['medicines'] == 'Prednisone 20 mg\nLialda 2.4 gram'
    assert record_maria['directions'] == 'Prednisone, Taper 5 mg every 3 days,\nFinish in 2.5 weeks -\nLialda - take 2 pill everyday for 1 month'
    assert record_maria['refills'] == '3'

    record_virat = doc_2_virat.parse()
    assert record_virat == {
        'patient_name': 'Virat Kohli',
        'patient_address': '2 cricket blvd, New Delhi',
        'medicines': 'Omeprazole 40 mg',
        'directions': 'Use two tablets daily for three months',
        'refills': '3'
    }

    record_empty = doc_3_empty.parse()
    assert record_empty == {
        'patient_name': None,
        'patient_address': None,
        'medicines': None,
        'directions': None,
        'refills': None
    }

# we use multiple "document_text" as we might wanna chcek multiple test cases