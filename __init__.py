from user import User
from datetime import datetime

if __name__ == '__main__':
    u1 = User('Daki', 'Praki', int(datetime.timestamp(datetime.now())), ['addr11'])
    u2 = User('Laki', 'Staki', int(datetime.timestamp(datetime.now())), ['addr21'])

    u1.add_address('addr12')
    u2.remove_addr(0)
