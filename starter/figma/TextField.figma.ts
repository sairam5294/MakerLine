// url=https://www.figma.com/design/Vjdm4Jlw4SnV5Prtaz1IFP?node-id=1-72
// Code Connect template: Figma "TextField" → src/components/TextField.tsx.
import figma from 'figma';

const instance = figma.selectedInstance;
const hasError = instance.getEnum('State', { Default: false, Error: true });

export default {
  example: figma.code`<TextField
  label="Email"
  value={email}
  onChangeText={setEmail}${hasError ? '\n  error={t(errorKey)}' : ''}
  keyboardType="email-address"
  autoComplete="email"
/>`,
  imports: ['import { TextField } from "@/components/TextField"'],
  id: 'text-field',
};
