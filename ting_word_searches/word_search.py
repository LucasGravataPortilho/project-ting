def exists_word(word, instance):
    data = list()
    for x in range(len(instance)):
        ocorrencias = list()
        for index, line in enumerate(instance.search(x)['linhas_do_arquivo']):
            if word.lower() in line.lower():
                ocorrencias.append({'linha': index + 1})

        if ocorrencias:
            data.append({
                'palavra': word,
                'arquivo': instance.search(x)['nome_do_arquivo'],
                'ocorrencias': ocorrencias,
            })

    return data


def search_by_word(word, instance):
    data = list()
    for x in range(len(instance)):
        ocorrencias = list()
        for index, line in enumerate(instance.search(x)['linhas_do_arquivo']):
            if word.lower() in line.lower():
                ocorrencias.append({'linha': index + 1,
                                    'conteudo': line})

        if ocorrencias:
            data.append({
                'palavra': word,
                'arquivo': instance.search(x)['nome_do_arquivo'],
                'ocorrencias': ocorrencias,
            })

    return data
