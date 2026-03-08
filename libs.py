def get_count(stringer, symb):
    s = 0
    for i in stringer:
        if i == symb:
            s +=1
    return s

def get_len(stringer):
    s=0
    for i in stringer:
        s +=1
    return s

if __name__ == '__main__':
    print(__name__)         #тут то что не выполнится когда импортируемый, сработает только если ег вызывать