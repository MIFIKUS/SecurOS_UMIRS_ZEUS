from securos.receiver.connection_callback import receive_msg
import enum


class SecurOsConnectionInfo(enum):
    ip = '127.0.0.1'
    port = '960'
    interface_id = '1'
    callback_func = receive_msg
    connect_type = {'Sync': 0, 'Async': 1}.get('Async')
    connection_attempts = 0
