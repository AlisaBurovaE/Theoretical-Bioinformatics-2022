import os


def fasta(file):
    dot_name = os.path.basename(file)[os.path.basename(file).find('.'):]
    if dot_name == '.fa' or dot_name == '.fasta':
        with open(file, 'r') as f:
            data = f.readlines()
        seq = []
        for line in range(len(data)):
            if data[line].startswith('>'):
                seq.append(data[line + 1])
        return seq
    else:
        print('Invalid format')
        exit()

try:
    P = fasta('P1.fa')[0]

    # Этап 1: формирование таблицы смещений

    S = set()  # уникальные символы в образе
    M = len(P)  # число символов в образе
    d = {}  # словарь смещений

    for i in range(M - 2, -1, -1):  # итерации с предпоследнего символа
        if P[i] not in S:  # если символ еще не добавлен в таблицу
            d[P[i]] = M - i - 1
            S.add(P[i])

    if P[M - 1] not in S:  # отдельно формируем последний символ
        d[P[M - 1]] = M

    d['*'] = M  # смещения для прочих символов

    # Этап 2: поиск образа в строке

    T = fasta('T1.fa')[0]
    N = len(T)

    if N >= M:
        i = M - 1  # счетчик проверяемого символа в строке
        checker = False
        while (i < N):
            k = 0
            j = 0
            flBreak = False
            for j in range(M - 1, -1, -1):
                if T[i - k] != P[j]:
                    if j == M - 1:
                        off = d[T[i]] if d.get(T[i], False) else d['*']  # смещение, если не равен последний символ образа
                    else:
                        off = d[P[j]]  # смещение, если не равен не последний символ образа

                    i += off  # смещение счетчика строки
                    flBreak = True  # если несовпадение символа, то flBreak = True
                    break

                k += 1  # смещение для сравниваемого символа в строке

            if not flBreak:  # если дошли до начала образа, значит, все его символы совпали
                print(f"вхождение по индексу {i - k + 1}")
                i += k
                checker = True
                continue
        else:
            if not checker:
                print("вхождение не найдено") 
    else:
        print("вхождение не найдено")
except: pass
