import { createClient, type SupabaseClient } from '@supabase/supabase-js';
import { env } from './env';
import { sessionStorage } from './secureStorage';

/**
 * Supabase client, or null when .env.local isn't set up yet (the app then shows setup help
 * instead of crashing). Uses the public anon key — data protection comes from Row Level
 * Security policies in supabase/migrations, not from hiding this key.
 */
export const supabase: SupabaseClient | null = env.ok
  ? createClient(env.env.EXPO_PUBLIC_SUPABASE_URL, env.env.EXPO_PUBLIC_SUPABASE_ANON_KEY, {
      auth: {
        storage: sessionStorage,
        autoRefreshToken: true,
        persistSession: true,
        detectSessionInUrl: false, // Mobile apps receive sessions via deep links, not the URL bar.
      },
    })
  : null;
