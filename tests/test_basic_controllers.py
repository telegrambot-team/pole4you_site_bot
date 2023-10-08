from controllers.basic_controllers import produce_hello_answer


def test_produce_hello_answer():
    name = "smth"
    assert produce_hello_answer(name) == f"Hello, {name}"
