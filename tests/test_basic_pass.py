from baseclass import BaseClass


def test_basic_pass():
    testcase = BaseClass()
    procedure_steps(testcase, 1)
    procedure_steps(testcase, 2)
    testcase.compare_images()
    testcase.cleanup()


def procedure_steps(object_testcase, run=1):
    object_testcase.load_page("https://ethisphere.com/")
    object_testcase.take_screenshot(run)



if __name__ == '__main__':
    test_basic_pass()
