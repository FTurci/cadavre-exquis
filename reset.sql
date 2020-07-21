select @maxnum :=  max(num) from Frasi;
delete from Frasi where num>1 && num<@maxnum;
update Frasi set num=2 where num=@maxnum;
