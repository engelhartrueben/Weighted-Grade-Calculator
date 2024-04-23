import sys
sys.path.insert(1, '/home/ruby/school/practical_programming/wgc')

from forms.name_form import NameForm

def test_name_form():
    test_cases = {
        'pass_test_cases' : {
            'str_pass_1' : ('Ruby Engelhart', 'Ruby Engelhart'),
            'str_pass_2' : ('ruby engelhart', 'Ruby Engelhart'),
            'str_pass_3' : ('jOe brO STEVE', 'Joe Bro Steve'),
            'str_pass_4' : ('Mr. SteVENS', 'Mr. Stevens'),
            'str_pass_5' : ('leSS not MORE', 'Less Not More'),
            'str_pass_6' : ('  ruby ruby  ', 'Ruby Ruby'),
            'str_pass_7' : ('michael   michael', 'Michael Michael'),
        },
        'fail_test_cases' : {
            'int_fail_1' : 25,
            'int_fail_2' : -3,
            'int_fail_3' : 0,
            'flt_fail_1' : 2.2,
            'flt_fail_2' : -905.6,
            'bool_fail_1' : True,
            'bool_fail_2' : False,
            'none_fail' : None,
            'empty_string_fail_1' : '',
            'empty_string_fail_2' : ' ',
            'empty_string_fail_3' : '  ',
            'large_string_fail' : 'ruby ruby ruby ruby',
             # unsure about testing types
            'type_obj_fail' : {'really' : 'silly'},
            'type_tuple_fail' : (2, 'really',),
            'type_set_fail' : {'peach', 'mango'},
            'type_list_fail' : ['wolf', 3]
        }
    }

    check = NameForm()

    for test_suit in test_cases:
        for key in test_cases[test_suit]:
            value = test_cases[test_suit][key]
            # Need to to decide what is returned
            # to show proper/improper input
            if test_suit == 'pass_test_cases':
                assert check.check_name(value[0]) == value[1]
            else:
                assert check.check_name(value) == None

test_name_form()