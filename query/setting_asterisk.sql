insert into ps_endpoints (id,transport,aors,auth,context,disallow,allow,ice_support,use_avpf,media_encryption,from_domain,dtls_verify,dtls_setup,
media_use_received_transport,rtcp_mux,webrtc,dtls_auto_generate_cert) 
values('WRTC01','transport-ws','WRTC01','WRTC01','testing','all','ulaw, alaw','yes','yes','dtls','sakura.cayangqu.com',
'fingerprint','actpass','yes','yes','yes','yes');

insert into ps_auths (id,auth_type,password,username)
        values('WRTC01','userpass','0','0');

insert into ps_aors (id,max_contacts)
        values('WRTC01','1');

insert into ps_endpoints (id, transport, aors, auth, context, disallow, allow, direct_media, rtp_symmetric, rewrite_contact) 
        values (102, 'transport-udp', '102', '102', 'testing', 'all', 'ulaw, alaw', 'no', 'yes','yes');



insert into ps_endpoints (id,transport,aors,context,disallow,allow,direct_media,from_domain) 
        values('violeta','violeta-transport','violeta_aor','dari_violeta','all','ulaw, alaw','no','sakura.cayangqu.com')

insert into ps_aors (id,contact) values ('violeta_aor','sip:violeta.cayangqu.com:35070')

insert into ps_auths (id,auth_type,password,username) values ('agent','userpass','1234','agent')

insert into ps_endpoint_id_ips (id,endpoint,match) values ('violeta_identify','violeta','209.97.162.54')


insert into acd.user (username,full_name,st,salt,saltedpassword,data,role_id)
values ('lisa-servodev','lisa servo dev',1,'bpeFmFjcFJAXUBPXkVhNkxHiMQKImZdH','7460f2e6994a1ecc67d29c2897f8694c54685d27fc235d436804ab794c0b4b60','{}',10);