from miio.device import Device

plug = Device("你的设备ip地址", "你的设备tooken")
#打开
plug.send("set_properties", [{'did': 'MYDID', 'siid': 2, 'piid': 1, 'value': True}])
#关闭
plug.send("set_properties", [{'did': 'MYDID', 'siid': 2, 'piid': 1, 'value': False}])
