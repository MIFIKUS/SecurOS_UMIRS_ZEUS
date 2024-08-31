from securos.connection.connection_info import SecurOsConnectionInfo
import ctypes

libiidk = ctypes.CDLL('libiidk.so')


class SecurOsConnection:
    @staticmethod
    def connect() -> int:
        return libiidk.ConnectEx(SecurOsConnectionInfo.ip, SecurOsConnectionInfo.port,
                                 SecurOsConnectionInfo.interface_id, SecurOsConnectionInfo.callback_func,
                                 None, SecurOsConnectionInfo.connect_type, SecurOsConnectionInfo.connection_attempts)

    @staticmethod
    def disconect():
        libiidk.Disconect(SecurOsConnectionInfo.interface_id)
