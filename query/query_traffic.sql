select a.id, a.name, a.email, b.data::jsonb->>'package_type' package_type, b.data::jsonb->>'promo' promo
from portal_account_company a
left join portal_registration_draft b
on b.id = a.registration_id
where b.data::jsonb->>'promo' is not null order by a.id;

select a.company_id, b.name, b.email, a.total_session
from (select company_id, count(*) total_session from portal_chat_session where created_tstamp between 1714521601 and 1714953599 group by company_id) a
left join portal_account_company b
on b.id = a.company_id order by a.company_id;


select a.session_type, count(*), b.name from portal_chat_session a left join portal_account_company b on b.id = a.company_id where a.created_tstamp between 1714496401 and 1714928399 and a.company_id = 123 group by a.session_type,b.name;

SELECT s.session_type, count(*) FROM portal_chat_session s LEFT JOIN portal_chat_messages m ON m.chat_id = s.reference_id
WHERE s.company_id = 123 AND s.created_tstamp >= 1714496401 AND s.created_tstamp < 1714928399
AND m.st != 'sent' GROUP BY s.session_type;

SELECT * FROM portal_chat_session s LEFT JOIN portal_chat_messages m ON m.chat_id = s.reference_id
WHERE s.company_id = 123 AND s.created_tstamp >= 1714496401 AND s.created_tstamp < 1714928399
AND m.st != 'sent' and session_type = 'service';