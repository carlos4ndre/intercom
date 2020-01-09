import subprocess


def test_customer_list_is_valid(list_customers_output):
    result = subprocess.run(["python", "-m", "src"], stdout=subprocess.PIPE)
    assert result.stdout == list_customers_output
