create table SoFar_Highest_History
(
id NUMBER GENERATED BY DEFAULT ON NULL AS IDENTITY,
datasource varchar2(50),
metric_name varchar2(50),
sofar_highest number(10,2),
sofar_highest_timestamp date,
constraints unique_histSoFarHighest unique(datasource, metric_name, sofar_highest_timestamp ),
constraints pk_histSoFarHighest primary key(id)
)