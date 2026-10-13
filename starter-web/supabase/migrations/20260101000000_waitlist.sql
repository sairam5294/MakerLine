-- Waitlist. Only the website's server (service key) can add rows; nobody can read, change or delete
-- them through the public API. The owner reads sign-ups in the Supabase dashboard.
create table public.waitlist (
  id bigint generated always as identity primary key,
  email text not null unique check (char_length(email) <= 254 and email ~* '^[^@\s]+@[^@\s]+\.[^@\s]+$'),
  created_at timestamptz not null default now()
);

-- RLS on + no policies = the public (anon) key can do nothing with this table.
-- The server action inserts with the service key, after validation + honeypot checks.
alter table public.waitlist enable row level security;
