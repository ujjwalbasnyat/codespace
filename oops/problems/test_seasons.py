from seasons import get_minutes
import pytest


def test_valid_date():
    assert get_minutes("2024-03-02") == 525600

def test_current_date():
    assert get_minutes("2025-03-02") == 0
# def test_future_date():
#     assert get_minutes("2026-03-02") is None
def test_invalid_format():
    import sys
    from unittest.mock import patch
    with patch('sys.exit') as mock_exit:
        get_minutes("2023/03/20")
        mock_exit.assert_called_with("Invalid date")
