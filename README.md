# PCKasse-sql-export
Exploring and exporting data from PCKasse POS.

This repository is intended for data exploration, testing and debugging. This is not intended to be used in
any operational environment.

# Developer notes
We assume that the PCKasse MS SQL Server database is stored as a backup in /data/sql.bak. You can then restore
the database using /db/restore.sql. This is a prerequisite the code to run.

# Todo:
- Export all images from database.
- Clean vendor names -> Janome, Baby Lock, Brother, etc. based on title
- Get All active products + Sewing machines, sewing machine accessories, etc.

### Notes:
MS SQL Server does not support volume mounts for MacOS: https://github.com/docker/for-win/issues/7259

