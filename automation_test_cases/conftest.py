
def pytest_generate_tests(metafunc):
    # the serial numbers parameter for test case: Warranty_0005
    if "various_number_length" in metafunc.fixturenames:
        sn = ['1', '1111', '11111', '111111']
        metafunc.parametrize("various_number_length",
                             sn,
                             ids=['1', '1111', '11111', '111111']
                             )
