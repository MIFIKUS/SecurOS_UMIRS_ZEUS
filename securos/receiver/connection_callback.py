import ctypes

def receive_msg(msg, slave_id, user_param):
    print(f'Got the msg from slave {slave_id}: {msg}\nUserParam: {user_param}')
ctypes._