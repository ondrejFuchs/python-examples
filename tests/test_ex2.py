import os

from ex2.os_env import Settings


def test_os_env_descriptor():
    assert Settings.var1 == "default"
    assert Settings.var2 == 2
    settings = Settings()
    assert settings.var1 == "default"
    assert settings.var2 == 2
    # In this line, script not run set. Also variables are immutables
    os.environ["var1"] = "new_value_from_env"
    assert settings.var1 == "new_value_from_env"
    settings.var1 = "value_from_instance"
    assert os.environ["var1"] == "value_from_instance"
    settings.var2 = "3"
    assert os.environ["var2"] == "3"
    assert settings.var2 == 3

