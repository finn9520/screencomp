from baseclass import BaseClass


def test_basic_fail():
    testcase = BaseClass()
    procedure_steps(testcase, 1)
    procedure_steps(testcase, 2)
    testcase.compare_images()
    testcase.cleanup()


def procedure_steps(object_testcase, run=1):
    object_testcase.load_page("https://ethisphere.com/")
    if run == 1:
        object_testcase.take_screenshot(1)
    else:
        object_testcase.set_elem_by_id("menu-item-32181")
        object_testcase.do_mouseover()
        object_testcase.take_screenshot(2)


if __name__ == '__main__':
    test_basic_fail()
