### Projeto A3 - Base de Dados Spotify 2017-2021



A base de dados escolhida, tem como finalidade a demonstração das músicas mais ouvidas do Spotify entre os anos de 2017 e 2021. Nesta base de dados, encontram-se as seguintes variáveis:

* Rank :1st_place_medal: : Indica a posição da música nos últimos 4 anos;
* Track :musical_note: : Demonstra o nome da música;
* Artist :man_singer: : Demonstra o nome dos artistas;
* Streams :tv: : Demonstra o número total de vezes que a música foi reproduzida;
* Link :link: : Nos direciona para a página oficial da música no Spotify;
* Week :calendar: : Demonstra as semanas em que essa música foi mais tocada;
* Album_Name :dvd: : Demonstra o nome do álbum;
* Duration_MS :timer_clock: : Demonstra a duração da música;
* Explicit :underage: : Demonstra com valores booleanos se a música contém ou não palavras obscenas;
* Track_Number_on_Album :cd: : Número da música no álbum de lançamento;
* Artist_Followers :woman_singer: : Demonstra a quantidade de seguidores na plataforma do artista;
* Artist_Genres :guitar: : Demonstra o gênero musical do artista.

Para este dataframe, optamos pela remoção das variáveis: Track, Artist, Link, Week, Album_Name, Track_Number_on_Album e Artist_Genres. Pelo fato de termos que aplicar uma regressão, muitas delas nos atrapalhariam na hora da criação.

## Variáveis Preditoras:

* Rank;
* Streams
* Duration_MS
* Explicit

## Variável de Resposta:

* Artist_Followers

## Interpretação de Coeficientes:

Com base nos valores obtidos, podemos concluir que: 

* A variável Rank é fortemente influenciada pelo total de seguidores do artista;
* A variável Streams, é mediamente influenciada. Isso pode se dar pelo fato de que algumas músicas acabam "bombando" em alguma outra plataforma e muitas vezes o artista dessa música não possui uma grande quantidade de seguidores;
* A variável Duration_MS, demonstra ser bem influenciada pelo total de seguidores;
* A variável Explicit, demonstra não ter muita relevância com a quantidade total de seguidores.

