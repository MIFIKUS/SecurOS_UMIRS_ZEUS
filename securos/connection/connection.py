from securos.connection.connection_info import SecurOsConnectionInfo
from pathlib import Path
import ctypes

current_path = Path.cwd()
print("Текущий путь:", current_path)
libiidk = ctypes.CDLL(f'{current_path}/libiidk.so')


class SecurOsConnection:
    @staticmethod
    def connect() -> int:
        return libiidk.ConnectEx(SecurOsConnectionInfo.ip, SecurOsConnectionInfo.port,
                                 SecurOsConnectionInfo.interface_id, SecurOsConnectionInfo.callback_func,
                                 None, SecurOsConnectionInfo.connect_type, SecurOsConnectionInfo.connection_attempts)

    @staticmethod
    def disconect():
        libiidk.Disconect(SecurOsConnectionInfo.interface_id)
