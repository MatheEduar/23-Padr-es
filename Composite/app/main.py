from Classes.arquivo import Arquivo
from Classes.pasta import Pasta


raiz = Pasta("/")
raiz.adicionar(Arquivo("leia_me.txt"))
raiz.adicionar(Arquivo("manual.pdf"))

subpasta1 = Pasta("Vídeos")
subpasta1.adicionar(Arquivo("video1.mp4"))
subpasta1.adicionar(Arquivo("video2.mp4"))


subpasta = Pasta("fotos")
subpasta.adicionar(Arquivo("foto1.jpg"))
subpasta.adicionar(Arquivo("foto2.jpg"))


raiz.adicionar(subpasta)
raiz.adicionar(subpasta1)

raiz.exibir()
