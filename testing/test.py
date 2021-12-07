import subprocess


class UnitTest:

    def __init__(self, file_name):
        self.file_name = file_name

    def run_file(self):
        output = subprocess.Popen(["python3", "../papy.py", f"tests/{self.file_name}.papy"], stdout=subprocess.PIPE).communicate()[0]
        return output.decode("utf-8").rstrip("\n")

    def make_test(self, expected_output):
        output = self.run_file()

        message = "PASSED"

        if output != expected_output:
            message = f"ERROR ON FILE tests/{self.file_name}.papy! EXPECTED: {expected_output} GOT: {output}"
        
        print(f"[TEST] {message}")


UnitTest("euclidean_algorithm").make_test("7");
UnitTest("quadratic_equation").make_test("2");


