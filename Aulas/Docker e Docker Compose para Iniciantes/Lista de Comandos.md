# Lista de Comandos Docker

1. **docker run** - Executa um container Docker a partir de uma imagem. Permite especificar configurações como portas, variáveis de ambiente, volumes, etc.

2. **docker build** - Cria uma imagem Docker a partir de um Dockerfile. É usado para automatizar a criação de imagens com base em instruções escritas no Dockerfile.

3. **docker pull** - Baixa uma imagem ou um repositório de imagens do Docker Hub ou de outro registro.

4. **docker push** - Envia uma imagem ou repositório para um registro de contêineres, como o Docker Hub.

5. **docker images** - Lista todas as imagens Docker locais, mostrando o repositório, a tag e o tamanho de cada uma.

6. **docker rmi** - Remove uma ou mais imagens Docker. Isso libera espaço no sistema que estava sendo usado por essas imagens.

7. **docker ps** - Lista os containers em execução. Usando a opção -a, ele mostra todos os containers, incluindo os inativos.

8. **docker stop** - Para um ou mais containers em execução, enviando um sinal de SIGTERM e, após um grace period, um SIGKILL.

9. **docker start** - Inicia um ou mais containers parados.

10. **docker restart** - Reinicia um ou mais containers. Isso é útil para aplicar atualizações ou configurações alteradas.

11. **docker rm** - Remove um ou mais containers. Containers precisam ser parados antes de serem removidos, a menos que você use a flag -f.

12. **docker logs** - Exibe os logs de um container. Muito útil para debugging e para acompanhar o que está acontecendo dentro do container.

13. **docker exec** - Executa um comando dentro de um container já em execução. É muito usado para interagir com processos em execução dentro de containers.

14. **docker network** - Gerencia redes Docker. Permite criar, listar, inspecionar, remover e conectar containers a redes.

15. **docker volume** - Gerencia os volumes Docker. Os volumes são usados para persistir e compartilhar dados entre containers.
