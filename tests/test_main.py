from tbraille import tbraille


def test_rendering():
    # test with default raster font
    expected_result = '⢠⡄⠀⠀⠀⠀⠀⠀⠀⢠⡄\n⢹⡏⣁⣾⠽⠆⠺⢯⣅⢹⡏⣁\n⠀⠉⠁⠈⠉⠁⠉⠉⠁⠀⠉⠁\n\n⣰⣆⡀⢀⣀⠀⢀⣀⡀⣰⣆⡀\n⠸⣇⡤⢿⣚⡃⣙⣳⡦⠸⣇⡤'  # noqa
    result = tbraille(fontname=None, size=None, text='test\ntest')
    print(result)
    assert result == expected_result
