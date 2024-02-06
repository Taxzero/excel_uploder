OPTIONS (SKIP=1)
LOAD DATA
    characterset UTF8
    INFILE 'C:\.csv'
    BADFILE 'C:\.bad'
    DISCARDFILE 'C:\.dsc'
    into table oracle_Dbname.tableName
    FIELDS TERMINATED BY '|'
    TRAILING NULLCOLS
    ('upload table column list')'