from forms.integer_form import intForm

"""Testing the integer form"""
def test_integer_form():
    """tests good an bad user inputs"""
    test_cases ={
        'pass_test_cases' : {
            'int_pass_1' : 24,
            'int_pass_2' : 0,
            'flt_pass_1' : 1.1,
            'flt_pass_2' : 92.6,
            'string_pass_1' : "24",
            'string_pass_2' : "300"
        },
        'fail_test_cases' : {
            'int_fail_1' : -1,
            'int_fail_2' : -101,
            'flt_fail_1' : -1.5,
            'flt_fail_2' : -87.3,
            'string_fail_1' : "1peach2",
            'string_fail_2' : "-25",
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
            assert intForm(val)