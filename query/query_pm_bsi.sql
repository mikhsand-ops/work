cred su - qrismerc = rahasia



jumlah merchant aktif sebulan terakhir sebulan terakhir:

select 
	to_timestamp(create_time)::date as tanggal, 
	count(*) as jumlah_merchant 
from qm_account 
where create_time >= 1706749261 and create_time <= 1709280340
group by tanggal;


jumlah pengguna merchant app sebulan terakhir

select 
	to_timestamp(tstamp)::date as tanggal, 
	count(distinct account_id) 
from qm_session_log 
where tstamp >= 1706749261 and tstamp <= 1709280340
group by tanggal;


transaksi on us/off us sebulan terakhir

select 
	trx_type as tipe_transaksi, 
	settlement_date as tanggal, 
	count(*) 
from qm_trx 
where settlement_date >= '20240201' and settlement_date <='20240301' 
group by tipe_transaksi, tanggal


jumlah keseluruhan merchant BSI saat ini

select count(*) from qm_account;