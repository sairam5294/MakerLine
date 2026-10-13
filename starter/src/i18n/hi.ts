import type { Translation } from './en';

// Hindi. Machine-drafted — have a native speaker review before launch.
export const hi: Translation = {
  home: {
    title: 'स्वागत है',
    body: 'सुलभ कंपोनेंट, डिज़ाइन टोकन, साइन-इन और टेस्ट तैयार हैं। PLAN.md से अपना पहला फ़ीचर बनाएँ।',
    setupTitle: 'सेटअप ज़रूरी है',
    setupBody:
      '.env.example को .env.local में कॉपी करें और अपना Supabase URL और anon key जोड़ें। मौजूद नहीं: {{missing}}',
    signIn: 'साइन इन',
    language: 'भाषा',
  },
  signIn: {
    title: 'साइन इन',
    checkEmail: 'अपना ईमेल देखें',
    email: 'ईमेल',
    sendCode: 'कोड भेजें',
    codeSent: 'हमने {{email}} पर 6 अंकों का कोड भेजा है।',
    code: '6 अंकों का कोड',
    verify: 'पुष्टि करें और आगे बढ़ें',
    differentEmail: 'दूसरा ईमेल इस्तेमाल करें',
  },
  errors: {
    emailRequired: 'अपना ईमेल पता दर्ज करें।',
    emailInvalid: 'name@example.com जैसा ईमेल दर्ज करें।',
    codeInvalid: 'अपने ईमेल में आया 6 अंकों का कोड दर्ज करें।',
    sendFailed: 'हम कोड नहीं भेज सके। अपना कनेक्शन जाँचें और फिर कोशिश करें।',
    verifyFailed: 'यह कोड काम नहीं किया। इसे जाँचें या नया कोड माँगें।',
    notConfigured: 'साइन-इन अभी सेट नहीं है (Supabase कुंजियाँ नहीं हैं)।',
  },
  states: {
    loading: 'लोड हो रहा है',
    errorTitle: 'कुछ गड़बड़ हो गई',
    errorBody: 'कृपया फिर कोशिश करें।',
    retry: 'फिर कोशिश करें',
    offlineTitle: 'आप ऑफ़लाइन हैं',
    offlineBody: 'अपना कनेक्शन जाँचें, फिर कोशिश करें।',
  },
};
