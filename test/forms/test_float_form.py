import sys
sys.path.insert(1, '/home/ruby/school/practical_programming/wgc')

from forms.float_form import FloatForm

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
            'string_int_pass_1' : ('44', 44.0),
            'string_int_pass_2' : ('0', 0.0),
            'string_int_pass_3' : ('24', 24.0),
            'string_int_pass_4' : ('300', 300.),
            'string_flt_pass_1' : ('1.1', 1.1),
            'string_flt_pass_2' : ('92.6', 92.6),
            'string_flt_pass_3' : ('11.1', 11.1),
            'string_flt_pass_4' : ('121.1', 121.1)
        },
        'fail_test_cases' : {
            'int_fail_1' : -1,
            'int_fail_2' : -101,
            'flt_fail_1' : -1.5,
            'flt_fail_2' : -87.3,
            'string_fail_1' : "91peach2",
            'string_fail_2' : "-45",
            'bool_fail_1' : True,
            'bool_fail_2' : False,
            # unsure about testing types
            'type_obj_fail' : {'bad' : 'superbad'},
            'type_tuple_fail' : (2, 'bad',),
            'type_set_fail' : {'apple', 'orange'},
            'type_list_fail' : ['bad', 7]
        }
    }
    
    check = FloatForm()

    for test_suits in test_cases:
        for key in test_cases[test_suits]:
            value = test_cases[test_suits][key]
            # Need to to decide what is returned
            # to show proper/improper input
            if test_suits == 'pass_test_cases':
                assert check.check_float(value[0]) == value[1]
            else:
                assert check.check_float(value) == None