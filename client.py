from   proj.tasks        import add

def test_add():
    result = add.delay(4, 4)
    print result.get(timeout=1)

test_add()
