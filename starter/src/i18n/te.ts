import type { Translation } from './en';

// Telugu. Machine-drafted — have a native speaker review before launch.
export const te: Translation = {
  home: {
    title: 'స్వాగతం',
    body: 'యాక్సెసిబుల్ కాంపోనెంట్లు, డిజైన్ టోకెన్లు, సైన్-ఇన్ మరియు టెస్ట్‌లు సిద్ధంగా ఉన్నాయి. PLAN.md నుండి మీ మొదటి ఫీచర్‌ను నిర్మించండి.',
    setupTitle: 'సెటప్ అవసరం',
    setupBody:
      '.env.example ను .env.local గా కాపీ చేసి, మీ Supabase URL మరియు anon key ను జోడించండి. లేనివి: {{missing}}',
    signIn: 'సైన్ ఇన్',
    language: 'భాష',
  },
  signIn: {
    title: 'సైన్ ఇన్',
    checkEmail: 'మీ ఈమెయిల్ చూడండి',
    email: 'ఈమెయిల్',
    sendCode: 'కోడ్ పంపండి',
    codeSent: '{{email}} కు 6 అంకెల కోడ్ పంపాము.',
    code: '6 అంకెల కోడ్',
    verify: 'ధృవీకరించి కొనసాగండి',
    differentEmail: 'వేరే ఈమెయిల్ వాడండి',
  },
  errors: {
    emailRequired: 'మీ ఈమెయిల్ చిరునామాను నమోదు చేయండి.',
    emailInvalid: 'name@example.com లాంటి ఈమెయిల్ నమోదు చేయండి.',
    codeInvalid: 'మీ ఈమెయిల్‌లో వచ్చిన 6 అంకెల కోడ్ నమోదు చేయండి.',
    sendFailed: 'కోడ్ పంపలేకపోయాము. మీ కనెక్షన్ చూసి మళ్లీ ప్రయత్నించండి.',
    verifyFailed: 'ఆ కోడ్ పని చేయలేదు. దాన్ని సరిచూడండి లేదా కొత్తది అడగండి.',
    notConfigured: 'సైన్-ఇన్ ఇంకా సెటప్ కాలేదు (Supabase కీలు లేవు).',
  },
  states: {
    loading: 'లోడ్ అవుతోంది',
    errorTitle: 'ఏదో తప్పు జరిగింది',
    errorBody: 'దయచేసి మళ్లీ ప్రయత్నించండి.',
    retry: 'మళ్లీ ప్రయత్నించండి',
    offlineTitle: 'మీరు ఆఫ్‌లైన్‌లో ఉన్నారు',
    offlineBody: 'మీ కనెక్షన్ చూసి, మళ్లీ ప్రయత్నించండి.',
  },
};
