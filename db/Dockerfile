# Adventure Works Database on SQL Server 2019
FROM mcr.microsoft.com/mssql/server:2019-latest

ARG MSSQL_SA_PASSWORD
ARG ACCEPT_EULA=Y

COPY data/backup/sql.bak /var/opt/mssql/data/sql.bak

USER root
RUN chown -R mssql /var/opt/mssql/data
USER mssql

# Launch SQL Server, confirm startup is complete, restore the database, then terminate SQL Server.
RUN ( /opt/mssql/bin/sqlservr & ) | grep -q "Service Broker manager has started" \
    && sleep 5s \
    && touch /var/opt/mssql/data/pck_log.ldf \
    && touch /var/opt/mssql/data/pck.mdf \
    && /opt/mssql-tools/bin/sqlcmd -U sa -P ${MSSQL_SA_PASSWORD} -Q 'RESTORE DATABASE [PCK] FROM DISK = "/var/opt/mssql/data/sql.bak" WITH MOVE "PCK" TO "/var/opt/mssql/data/pck.mdf", MOVE "PCK_log" TO "/var/opt/mssql/data/pck_log.ldf"' \
    # && /opt/mssql-tools/bin/sqlcmd -U sa -P ${MSSQL_SA_PASSWORD} -Q 'USE PCK ; ALTER DATABASE PCK SET RECOVERY FULL;' \
    && pkill sqlservr
