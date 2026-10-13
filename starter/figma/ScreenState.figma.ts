// url=https://www.figma.com/design/Vjdm4Jlw4SnV5Prtaz1IFP?node-id=1-91
// Code Connect template: Figma "ScreenState" → src/components/ScreenState.tsx.
import figma from 'figma';

const instance = figma.selectedInstance;
const kind = instance.getEnum('Kind', { Empty: 'empty', Error: 'error', Offline: 'offline', Loading: 'loading' });

const props = {
  empty: 'kind="empty" title="No lessons yet" actionLabel="Browse lessons" onAction={browse}',
  error: 'kind="error" onRetry={refetch}',
  offline: 'kind="offline" onRetry={refetch}',
  loading: 'kind="loading"',
}[kind];

export default {
  example: figma.code`<ScreenState ${props} />`,
  imports: ['import { ScreenState } from "@/components/ScreenState"'],
  id: 'screen-state',
};
