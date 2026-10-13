import { getLocales } from 'expo-localization';
import { createInstance } from 'i18next';
import { initReactI18next } from 'react-i18next';
import { en } from './en';
import { hi } from './hi';
import { te } from './te';

/**
 * Translations. Add a language: create xx.ts typed as Translation, add it below.
 * Screens use:  const { t } = useTranslation();  t('home.title')
 */
export const resources = {
  en: { translation: en },
  te: { translation: te },
  hi: { translation: hi },
};
export type Language = keyof typeof resources;
export const languages: { code: Language; label: string }[] = [
  { code: 'en', label: 'English' },
  { code: 'te', label: 'తెలుగు' },
  { code: 'hi', label: 'हिन्दी' },
];

/** Scripts that need extra line height so tall glyphs/matras aren't clipped. */
export const tallScriptLanguages: Language[] = ['te', 'hi'];

// Use the phone's language if we support it, otherwise English.
const deviceLanguage = getLocales()[0]?.languageCode ?? 'en';
const initial: Language = deviceLanguage in resources ? (deviceLanguage as Language) : 'en';

// Own instance (not the global default) keeps tests and hot-reload predictable.
const i18n = createInstance();
i18n.use(initReactI18next).init({
  resources,
  lng: initial,
  fallbackLng: 'en',
  interpolation: { escapeValue: false }, // React already escapes text.
  initAsync: false, // Load synchronously: strings are bundled, and tests need them immediately.
});

export default i18n;
