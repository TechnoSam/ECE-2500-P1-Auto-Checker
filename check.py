
import argparse
import datetime
import subprocess
import sys

VALID_TESTS = [1, 2, 3, 9]

INVALID_TESTS = [4, 5, 6, 7, 8]

ALL_TESTS = []
ALL_TESTS.extend(VALID_TESTS)
ALL_TESTS.extend(INVALID_TESTS)


def log(line, verbose):

    if verbose:
        sys.stdout.write(line)
    return line


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

    parser = argparse.ArgumentParser(description="ECE 2500 Project 1\nAuto Checker")

    language = parser.add_mutually_exclusive_group(required=True)
    language.add_argument("-p", "--python", help="Specify that myAssembler is written in python", action="store_true")
    language.add_argument("-c", "--cpp", help="Specify that myAssembler is written in C++", action="store_true")
    parser.add_argument("--path", help="Specify the path to the myAssembler script or executable "
                                       "(default \"../myAssembler.py\" or \"../myAssembler\")")
    parser.add_argument("-t", "--tests", help="Specify which tests should be run e.g. \"1, 2, 3\" (default all)")
    parser.add_argument("-o", "--save-output", help="Save the output with a timestamp (default \"last_test.log\")",
                        action="store_true")
    parser.add_argument("-v", "--verbose", help="Enable verbose output", action="store_true")

    args = parser.parse_args()

    if args.tests:
        try:
            tests_to_run = [int(x) for x in args.tests.split(",")]
        except:
            print("Unrecognized test list. Format: \"1, 2, 3\"")
            sys.exit(1)
        for test in tests_to_run:
            if test not in ALL_TESTS:
                print("No such test: %s" % test)
                sys.exit(1)
    else:
        tests_to_run = ALL_TESTS

    failures = 0

    output = ""

    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H.%M.%S")

    output += log("STARTING TESTING AT %s\n\n" % timestamp, True)

    for test in tests_to_run:

        output += log("STARTING TEST FOR \"test_case%d.s\"\n" % test, args.verbose)

        if args.python:
            cmd = ["python", "../myAssembler.py" if not args.path else args.path, "test_case%d.obj" % test]
        else:
            cmd = ["../myAssembler" if not args.path else args.path, "test_case%d.obj" % test]

        try:
            subprocess.check_output(cmd, stderr=subprocess.STDOUT, shell=True)
        except subprocess.CalledProcessError as e:
            output += log(e.output, args.verbose)
            if test in VALID_TESTS:
                output += log("FAIL: Did not assemble valid \"test_case%d.s\" (returned %d)\n\n" % (test, e.returncode),
                              args.verbose)
                failures += 1
            else:
                output += log("PASS: Refused to assemble invalid \"test_case%d.s\" (returned %d)\n\n"
                              % (test, e.returncode), args.verbose)
            continue

        if test in INVALID_TESTS:
            output += log("FAIL: Assembled invalid \"test_case%d.s\" with no error\n\n" % test, args.verbose)
            failures += 1
        else:
            result, reason = file_compare("test_case%s.obj" % test, "test_case%s_given.obj" % test)
            if not result:
                failures += 1
                output += log("FAIL: " + reason + "\n\n", args.verbose)
            else:
                output += log("PASS: Generated object file matches given\n\n", args.verbose)

    output += log("", args.verbose)
    if failures == 0:
        output += log("ALL TESTS PASS\n", True)
    else:
        output += log("FAILED %d/%d TESTS\n" % (failures, len(tests_to_run)), True)

    if args.save_output:
        out_fname = "logs/test_" + timestamp + ".log"
    else:
        out_fname = "logs/last_test.log"

    with open(out_fname, "w") as out_f:
        out_f.write(output)
