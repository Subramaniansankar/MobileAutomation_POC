from utilities.android_driver import get_driver as get_android_driver
from utilities.ios_driver import get_driver as get_ios_driver


def get_driver(platform):

    platform = platform.lower()

    if platform == "android":
        return get_android_driver()

    elif platform == "ios":
        return get_ios_driver()

    raise ValueError(f"Unsupported platform: {platform}")