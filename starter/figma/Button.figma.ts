// url=https://www.figma.com/design/Vjdm4Jlw4SnV5Prtaz1IFP?node-id=1-62
// Code Connect template: maps the Figma "Button" component to src/components/Button.tsx.
import figma from 'figma';

const instance = figma.selectedInstance;
const label = instance.getString('Label');
const variant = instance.getEnum('Variant', { Primary: 'primary', Secondary: 'secondary' });
const disabled = instance.getEnum('State', { Default: false, Pressed: false, Disabled: true });

export default {
  example: figma.code`<Button
  label="${label}"
  variant="${variant}"${disabled ? '\n  disabled' : ''}
  onPress={() => {}}
/>`,
  imports: ['import { Button } from "@/components/Button"'],
  id: 'button',
  metadata: { nestable: true },
};
