from hello import hello


def test_hello():
    name = "niikun"
    assert "hello niikun" == hello("niikun")