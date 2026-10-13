import { fireEvent, render, screen } from '@testing-library/react-native';
import { ScreenState } from '../ScreenState';

describe('ScreenState', () => {
  it('error state offers a retry', async () => {
    const onRetry = jest.fn();
    await render(<ScreenState kind="error" onRetry={onRetry} />);
    await fireEvent.press(screen.getByRole('button', { name: 'Try again' }));
    expect(onRetry).toHaveBeenCalled();
  });

  it('empty state explains and offers the next action', async () => {
    const onAction = jest.fn();
    await render(
      <ScreenState
        kind="empty"
        title="No lessons yet"
        actionLabel="Browse lessons"
        onAction={onAction}
      />,
    );
    expect(screen.getByRole('header', { name: 'No lessons yet' })).toBeOnTheScreen();
    await fireEvent.press(screen.getByRole('button', { name: 'Browse lessons' }));
    expect(onAction).toHaveBeenCalled();
  });

  it('offline state tells the user what to do', async () => {
    await render(<ScreenState kind="offline" onRetry={() => {}} />);
    expect(screen.getByText(/check your connection/i)).toBeOnTheScreen();
  });
});
