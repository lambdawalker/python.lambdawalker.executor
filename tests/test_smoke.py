def test_smoke():
    from lambdawalker.executor.engine import SubprocessExecutor
    from lambdawalker.executor.models import TaskConfig
    assert SubprocessExecutor is not None
    print("executor OK")
