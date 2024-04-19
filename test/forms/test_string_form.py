from forms.string_form import strForm

def test_string_form():
    test_cases = {
        'pass_test_cases' : {
            'str_pass_1' : 'Math',
            'str_pass_2' : 'enGlIsh',
            'str_pass_3' : 'maTH 207',
            'str_pass_4' : '137 CS',
            # bit of user freedom with this one,
            # can't control everything
            'str_pass_5' : '% soci 3033',
            'str_pass_6' : '6578'
        },
        'fail_test_cases' : {
            'int_fail_1' : 25,
            'int_fail_2' : -3,
            'int_fail_3' : 0,
            'flt_fail_1' : 2.2,
            'flt_fail_2' : -905.6,
            # unsure about testing types
            'type_obj_fail' : {'really' : 'silly'},
            'type_tuple_fail' : (2, 'really',),
            'type_set_fail' : {'peach', 'mango'},
            'type_list_fail' : ['wolf', 3]
        }
    }

    for test_suits in test_cases:
        for _, val in test_cases[test_suits]:
            # Need to to decide what is returned
            # to show proper/improper input
            assert strForm(val)