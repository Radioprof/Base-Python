with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
    result = []
    for _st in f:
        el = _st.split(' ')
        result.append((el[0], el[5][1:], el[6]))
    print(result)