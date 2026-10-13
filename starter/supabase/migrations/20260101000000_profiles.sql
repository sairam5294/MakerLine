-- Profiles: one row per signed-in user, created automatically at sign-up.
-- Pattern to copy for every user-owned table: owner column + RLS ON + one policy per action.

create table public.profiles (
  id uuid primary key references auth.users (id) on delete cascade, -- deleting the account deletes the profile
  display_name text check (char_length(display_name) <= 60),         -- limit input size at the database too
  created_at timestamptz not null default now(),                      -- always store UTC
  updated_at timestamptz not null default now()
);

-- Row Level Security: without policies, NOBODY can read/write via the public API. Deny by default.
alter table public.profiles enable row level security;

-- Users can read only their own profile. (select auth.uid()) is cached per query → faster.
create policy "profiles: read own"
  on public.profiles for select
  to authenticated
  using ((select auth.uid()) = id);

-- Users can update only their own profile, and can't change the id to someone else's.
create policy "profiles: update own"
  on public.profiles for update
  to authenticated
  using ((select auth.uid()) = id)
  with check ((select auth.uid()) = id);

-- No insert/delete policies on purpose: rows are created by the trigger below and removed
-- when the auth user is deleted (on delete cascade).

-- Create a profile automatically when someone signs up.
-- security definer = runs with the function owner's rights; search_path is pinned so it can't be hijacked.
create function public.handle_new_user()
returns trigger
language plpgsql
security definer
set search_path = ''
as $$
begin
  insert into public.profiles (id) values (new.id);
  return new;
end;
$$;

create trigger on_auth_user_created
  after insert on auth.users
  for each row execute function public.handle_new_user();

-- Keep updated_at current.
create function public.touch_updated_at()
returns trigger
language plpgsql
set search_path = ''
as $$
begin
  new.updated_at = now();
  return new;
end;
$$;

create trigger profiles_touch_updated_at
  before update on public.profiles
  for each row execute function public.touch_updated_at();
