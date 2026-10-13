// Tests describe behaviour the way users experience it: find by role + name, not by styles.
import { fireEvent, render, screen } from '@testing-library/react-native';
import { Button } from '../Button';

describe('Button', () => {
  it('is announced as a button with its label and responds to taps', async () => {
    const onPress = jest.fn();
    await render(<Button label="Save" onPress={onPress} />);
    await fireEvent.press(screen.getByRole('button', { name: 'Save' }));
    expect(onPress).toHaveBeenCalledTimes(1);
  });

  it('blocks taps and reports busy while loading (prevents double submit)', async () => {
    const onPress = jest.fn();
    await render(<Button label="Save" onPress={onPress} loading />);
    const button = screen.getByRole('button', { name: 'Save' });
    await fireEvent.press(button);
    expect(onPress).not.toHaveBeenCalled();
    expect(button).toBeDisabled();
    expect(button).toBeBusy();
  });

  it('uses a custom screen-reader label when given', async () => {
    await render(<Button label="+" accessibilityLabel="Add item" onPress={() => {}} />);
    expect(screen.getByRole('button', { name: 'Add item' })).toBeOnTheScreen();
  });
});
