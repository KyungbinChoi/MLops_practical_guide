from hello import add

def test_add():
    assert 2 == add(1,1) #assert는 뒤의 조건이 True가 아니면 AssertError를 발생한다.