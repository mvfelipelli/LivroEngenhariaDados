---
title: Solução — Imagem em Camadas Determinística
description: "Implementação validada do laboratório de imagem didática."
tags: [linux, containers, laboratorio, solucao]
aliases: [Solução Laboratório OCI]
created: 2026-07-16
updated: 2026-07-16
---

# Solução — Imagem em Camadas Determinística

Salve como `imagem_didatica.py`:

```python
from hashlib import sha256
from io import BytesIO
import json
from pathlib import PurePosixPath
import tarfile


def camada(arquivos):
    buffer = BytesIO()
    with tarfile.open(fileobj=buffer, mode="w", format=tarfile.USTAR_FORMAT) as tar:
        for nome, conteudo in sorted(arquivos.items()):
            dados = conteudo.encode("utf-8")
            info = tarfile.TarInfo(nome)
            info.size = len(dados)
            info.mode = 0o644
            info.uid = info.gid = 0
            info.uname = info.gname = ""
            info.mtime = 0
            tar.addfile(info, BytesIO(dados))
    return buffer.getvalue()


def caminho_seguro(nome):
    caminho = PurePosixPath(nome)
    return not caminho.is_absolute() and ".." not in caminho.parts


def aplicar(blob, rootfs):
    removidos = 0
    with tarfile.open(fileobj=BytesIO(blob), mode="r:") as tar:
        for membro in tar:
            if not caminho_seguro(membro.name) or not membro.isfile():
                raise ValueError(f"entrada insegura: {membro.name}")
            caminho = PurePosixPath(membro.name)
            if caminho.name.startswith(".wh."):
                alvo = str(caminho.with_name(caminho.name[4:]))
                rootfs.pop(alvo, None)
                removidos += 1
            else:
                arquivo = tar.extractfile(membro)
                rootfs[membro.name] = arquivo.read() if arquivo else b""
    return removidos


def construir():
    camadas = [
        camada({"app/config.ini": "env=prod\n", "app/antigo.txt": "remover\n"}),
        camada({"app/.wh.antigo.txt": "", "app/version.txt": "1.0.0\n"}),
    ]
    descritores = [
        {"digest": "sha256:" + sha256(blob).hexdigest(), "size": len(blob)}
        for blob in camadas
    ]
    manifesto = json.dumps(
        {"schemaVersion": 2, "layers": descritores},
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")
    rootfs = {}
    whiteouts = sum(aplicar(blob, rootfs) for blob in camadas)
    return "sha256:" + sha256(manifesto).hexdigest(), rootfs, whiteouts


digest_a, rootfs, whiteouts = construir()
digest_b, _, _ = construir()
assert digest_a == digest_b
assert sorted(rootfs) == ["app/config.ini", "app/version.txt"]

print("camadas=2")
print(f"arquivos={len(rootfs)}")
print(f"whiteouts={whiteouts}")
print("rootfs=" + ",".join(sorted(rootfs)))
print("digest_repetivel=sim")
print("imagem=ok")
```

## Leitura da solução

Ordenação, USTAR e metadata normalizada tornam os blobs repetíveis. O manifesto referencia tamanho e digest de cada camada. A aplicação nunca usa `extractall`, valida cada caminho e interpreta whiteout explicitamente.

> [!note]
> A especificação OCI real inclui media types, configuração, compressão e regras completas de whiteout. O laboratório preserva os fundamentos sem fingir ser um runtime.
