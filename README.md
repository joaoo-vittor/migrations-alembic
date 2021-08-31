<div align="center">
    <h1>
        Estudo de Migrations com SQLAlchemy e Alembic
    </h1>
    <h4>
        <i>Status dos estudos</i>: completo. 🤓 🤓 
    </h4> 
</div>

----

## Descrição

Objetivo desse repositório é uma breve explicação de como usar o `SQLAlchemy` e o `Alembic`, com base na **Clean Architecture**.

> Observação: Nesse projeto estou usando o MySQL, caso queira usar outro banco de dados mude as `connections_strings` no arquivo `alembic.ini` e `db_config.py`.

----

## Estrutura do projeto

```
test-alembic/
    src/
      infra/
        config/
          db_base.py
          db_config.py
        entities/
          user.py
        migrations/
            env.py
            README
            script.py.mako
            versions/
                bca950936911_create_test_ecommerce_db_and_table.py
        repo/
          user_repository_test.py        
          user_repository.py
    alembic.ini 
```

----

## Crie o ambiente virtual

> É necessário ter o virtualenv instalado.

```
virtualenv -p python3 venv
```

## Ativar o ambiente virtual

```
source venv/bin/activate
```

## Instalando as dependências

```
pip install -r requirements.txt
```

## Criar novo arquivo para a migrate

```
alembic init src/infra/migrations
```

Ao execultar esse comando será criado o diretório `migrations` e dentro do diretório é criado um arquivo para você fazer usas migrations.




