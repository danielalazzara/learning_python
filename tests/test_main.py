import pytest
import main


def test_main(capsys):
    main.main()
    captured = capsys.readouterr()
    assert captured.out == "Hello, world!\n"
