from typing import Union


# tupla com os tamanhos oficiais permitidos
VALID_SIZES = ("P", "M", "G", "GG", "XG")


def check_product_size(product_id: int, size_label: str) -> Union[dict, str]:
    """Valida e padroniza o tamanho de uma roupa.

    Recebe o id do produto e a etiqueta de tamanho.
    Retorna um dicionario quando o tamanho e valido ou
    uma mensagem de erro quando nao e.
    """
    try:
        # verifica se a etiqueta e texto
        if not isinstance(size_label, str):
            return "Erro: a etiqueta de tamanho deve ser um texto."

        # remove espacos e deixa em maiusculo
        cleaned_label = size_label.strip().upper()

        # verifica se ficou vazio
        if len(cleaned_label) == 0:
            return "Erro: a etiqueta de tamanho nao pode estar vazia."

        # verifica o tamanho do texto (1 ou 2 caracteres)
        if len(cleaned_label) < 1 or len(cleaned_label) > 2:
            return "Erro: a etiqueta deve ter entre 1 e 2 caracteres."

        # verifica se existe na grade oficial
        if cleaned_label not in VALID_SIZES:
            return (
                f"Erro: o tamanho '{cleaned_label}' nao existe na grade oficial. "
                f"Tamanhos permitidos: {VALID_SIZES}."
            )

        # tudo certo, retorna o dicionario
        return {"product_id": product_id, "size_tag": cleaned_label}

    except AttributeError:
        return "Erro: nao foi possivel processar a etiqueta de tamanho."
    except Exception as error:
        return f"Erro: falha inesperada na validacao ({error})."


# casos de sucesso
print(check_product_size(product_id=101, size_label="P"))
print(check_product_size(product_id=102, size_label="GG"))
print(check_product_size(product_id=103, size_label="XG"))

# casos com espacos e letras minusculas
print(check_product_size(product_id=201, size_label=" g "))
print(check_product_size(product_id=202, size_label="xg"))
print(check_product_size(product_id=203, size_label="  m  "))

# casos de erro
print(check_product_size(product_id=301, size_label="XXG"))
print(check_product_size(product_id=302, size_label="K"))
print(check_product_size(product_id=303, size_label=""))
print(check_product_size(product_id=304, size_label="   "))
print(check_product_size(product_id=305, size_label=42))