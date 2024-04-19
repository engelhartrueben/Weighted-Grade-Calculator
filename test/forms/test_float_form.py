from forms.float_form import fltForm

"""Testing the float form"""
def test_integer_form():
    """
    Tests good an bad user inputs.
    Only positive floats.
    """
    test_cases ={
        'pass_test_cases' : {
            # Ints pass
            # Can be turned into a float
            'int_pass_1' : 24,
            'int_pass_2' : 0,
            'string_int_pass_1' : '24',
            'string_int_pass_2' : '300',
            'flt_pass_3' : 1.1,
            'flt_pass_4' : 92.6,
            'string_flt_pass' : '11.1',
            'string_flt_pass' : '121.1'
        },
        'fail_test_cases' : {
            'int_fail_1' : -1,
            'int_fail_2' : -101,
            'flt_fail_1' : -1.5,
            'flt_fail_2' : -87.3,
            'string_fail_1' : "91peach2",
            'string_fail_2' : "-45",
            # unsure about testing types
            'type_obj_fail' : {'bad' : 'superbad'},
            'type_tuple_fail' : (2, 'bad',),
            'type_set_fail' : {'apple', 'orange'},
            'type_list_fail' : ['bad', 7]
        }
    }
    
    for test_suits in test_cases:
        for _, val in test_cases[test_suits]:
            # Need to to decide what is returned
            # to show proper/improper input
            assert fltForm(val)