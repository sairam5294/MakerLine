-- Authorization test: user A must never see or change user B's profile.
-- Run with the Supabase CLI:  npx supabase test db   (uses pgTAP)
begin;
create extension if not exists pgtap with schema extensions;  -- test framework (built into Supabase)
select plan(4);

-- Two fake users (the trigger creates their profiles).
insert into auth.users (id, email) values
  ('00000000-0000-0000-0000-00000000000a', 'a@example.com'),
  ('00000000-0000-0000-0000-00000000000b', 'b@example.com');

-- Act as user A.
set local role authenticated;
set local request.jwt.claims = '{"sub":"00000000-0000-0000-0000-00000000000a"}';

select is((select count(*) from public.profiles)::int, 1, 'A sees exactly one profile (their own)');
select is((select id from public.profiles), '00000000-0000-0000-0000-00000000000a'::uuid, 'and it is A''s');

-- A tries to rename B: the update silently affects 0 rows because RLS hides B's row.
update public.profiles set display_name = 'hacked' where id = '00000000-0000-0000-0000-00000000000b';
reset role;
select is((select display_name from public.profiles where id = '00000000-0000-0000-0000-00000000000b'), null, 'B''s profile unchanged');

-- Anonymous visitors see nothing.
set local role anon;
select is((select count(*) from public.profiles)::int, 0, 'anon sees no profiles');

select * from finish();
rollback;
