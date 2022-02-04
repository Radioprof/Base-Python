import collections
with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
    spamers = []
    for _st in f:
        spamers.append(_st[:_st.index(' ')])
    c = collections.Counter(spamers)
    print(f'С адреса: {c.most_common(1)[0][0]} было {c.most_common(1)[0][1]} обращений!')
