import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    data = txt_importer(path_file)

    result = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(data),
        "linhas_do_arquivo": data,
    }

    for index in range(0, len(instance)):
        searched = instance.search(index)
        if searched == result:
            return None

    instance.enqueue(result)
    print(result, file=sys.stdout)


def remove(instance):
    if len(instance) == 0:
        print("Não há elementos", file=sys.stdout)
        return

    removed = instance.dequeue()['nome_do_arquivo']

    print(f"Arquivo {removed} removido com sucesso", file=sys.stdout)


def file_metadata(instance, position):
    if position < 0 or position > len(instance):
        print("Posição inválida", file=sys.stderr)
        return

    searched = instance.search(position)
    print(searched, file=sys.stdout)
