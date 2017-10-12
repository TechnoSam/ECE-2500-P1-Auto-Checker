
import subprocess
import sys

VALID_TESTS = [1, 2, 3]

INVALID_TESTS = [4, 5, 6]


def file_compare(generated_fname, given_fname):

    with open(generated_fname, "r") as generated_f:
        with open(given_fname, "r") as given_f:

            generated = generated_f.readlines()
            given = given_f.readlines()

            if len(generated) != len(given):
                return False, "Number of lines did not match"

            for line_no in range(0, len(generated)):
                if generated[line_no] != given[line_no]:
                    return (False, "Line %d mismatch:\n\tGiven: %s\n\tYours: %s"
                            % (line_no + 1, given[line_no], generated[line_no]))

            return True, ""


if __name__ == "__main__":

    tests_to_run = [1, 2, 3]
    failures = 0

    for test in tests_to_run:

        print("STARTING TEST FOR \"test_case%d.s\"" % test)

        cmd = ["python", "../myAssembler.py", "test_case%d.obj" % test]

        try:
            subprocess.check_output(cmd, stderr=subprocess.STDOUT, shell=True)
        except subprocess.CalledProcessError as e:
            print(e.output)
            if test in VALID_TESTS:
                print("FAIL: Did not assemble valid \"test_case%d.s\" (returned %d)\n" % (test, e.returncode))
                failures += 1
            else:
                print("PASS: Refused to assemble invalid \"test_case%d.s\" (returned %d)\n" % (test, e.returncode))
            continue

        if test in INVALID_TESTS:
            print("FAIL: Assembled invalid \"test_case%d.s\" with no error\n" % test)
        else:
            result, reason = file_compare("test_case%s.obj" % test, "test_case%s_given.obj" % test)
            if not result:
                failures += 1
                print("FAIL: " + reason + "\n")
            else:
                print("PASS: Generated object file matches given\n")

    print("")
    if failures == 0:
        print("ALL TESTS PASS")
    else:
        print("FAILED %d/%d TESTS" % (failures, len(tests_to_run)))
